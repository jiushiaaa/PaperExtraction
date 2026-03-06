# -*- coding: utf-8 -*-
"""OpenAI compatible provider with extra request passthrough support."""

from __future__ import annotations

import concurrent.futures
import json
import logging
import os
import time
import re
from collections.abc import Iterator, Sequence
from typing import Any

from langextract.core import data
from langextract.core import exceptions
from langextract.core import types as core_types
from langextract.providers import router
from langextract.providers.openai import OpenAILanguageModel

log = logging.getLogger(__name__)


@router.register(r"^OpenAICompatibleLanguageModel$", priority=10_000)
class OpenAICompatibleLanguageModel(OpenAILanguageModel):
  """Drop-in replacement for OpenAI provider with extra_body support."""

  _CONFIG_KEYS = (
      "frequency_penalty",
      "presence_penalty",
      "seed",
      "stop",
      "logprobs",
      "top_logprobs",
      "reasoning_effort",
      "reasoning",
      "response_format",
      "extra_body",
      "extra_headers",
      "extra_query",
      "timeout",
  )
  _DISABLE_RESPONSE_FORMAT = os.environ.get(
      "LLM_DISABLE_RESPONSE_FORMAT", ""
  ).lower() in {"1", "true", "yes"}
  _MAX_RETRIES = max(0, int(os.environ.get("LLM_MAX_RETRIES", "2")))
  _RETRY_BACKOFF_SECONDS = float(
      os.environ.get("LLM_RETRY_BACKOFF_SECONDS", "1.5")
  )

  @staticmethod
  def _is_retryable_error(exc: Exception) -> bool:
    msg = str(exc).lower()
    retry_markers = (
        "timed out",
        "timeout",
        "rate limit",
        "too many requests",
        "connection error",
        "temporarily unavailable",
        "service unavailable",
        "502",
        "503",
        "504",
    )
    return any(marker in msg for marker in retry_markers)

  @staticmethod
  def _extract_first_balanced_json(text: str) -> str | None:
    """Extract first balanced JSON object/array from arbitrary text."""
    start = -1
    opener = ""
    for i, ch in enumerate(text):
      if ch in "{[":
        start = i
        opener = ch
        break
    if start < 0:
      return None

    closer = "}" if opener == "{" else "]"
    depth = 0
    in_string = False
    escaped = False

    for j in range(start, len(text)):
      ch = text[j]
      if in_string:
        if escaped:
          escaped = False
        elif ch == "\\":
          escaped = True
        elif ch == '"':
          in_string = False
        continue

      if ch == '"':
        in_string = True
      elif ch == opener:
        depth += 1
      elif ch == closer:
        depth -= 1
        if depth == 0:
          return text[start : j + 1]
    return None

  @classmethod
  def _normalize_json_text(cls, output_text: str) -> str:
    """Best-effort cleanup for OpenAI-compatible responses with extra text."""
    text = output_text.strip()
    if not text:
      return text

    # Remove common reasoning wrapper blocks.
    text = re.sub(r"<think>.*?</think>\s*", "", text, flags=re.DOTALL).strip()

    # If wrapped in fenced code block, keep the fenced payload.
    fence_match = re.search(
        r"```(?:json)?\s*([\s\S]*?)\s*```", text, flags=re.IGNORECASE
    )
    if fence_match:
      text = fence_match.group(1).strip()

    # If still not pure JSON, extract the first balanced JSON object/array.
    if text and text[0] not in "{[":
      candidate = cls._extract_first_balanced_json(text)
      if candidate:
        text = candidate.strip()

    return text

  @staticmethod
  def _coerce_message_content(message: Any) -> str:
    """Normalize provider-specific message content to plain text."""
    if message is None:
      return ""

    content = getattr(message, "content", None)
    if isinstance(content, str):
      return content
    if isinstance(content, list):
      parts: list[str] = []
      for item in content:
        if isinstance(item, str):
          parts.append(item)
          continue
        if isinstance(item, dict):
          # OpenAI-like blocks: {"type":"text","text":"..."}
          text = item.get("text")
          if isinstance(text, str):
            parts.append(text)
          # Some gateways use {"type":"output_text","content":"..."}
          content_text = item.get("content")
          if isinstance(content_text, str):
            parts.append(content_text)
      return "".join(parts).strip()

    # Some compatible gateways return a top-level "text" field in message.
    text_attr = getattr(message, "text", None)
    if isinstance(text_attr, str):
      return text_attr

    return ""

  def _process_single_prompt(
      self, prompt: str, config: dict[str, Any]
  ) -> core_types.ScoredOutput:
    """Process a single prompt with OpenAI-compatible extra params."""
    try:
      normalized_config = self._normalize_reasoning_params(config)

      system_message = ""
      if self.format_type == data.FormatType.JSON:
        system_message = (
            "You are a helpful assistant that responds in JSON format."
        )
      elif self.format_type == data.FormatType.YAML:
        system_message = (
            "You are a helpful assistant that responds in YAML format."
        )

      messages = [{"role": "user", "content": prompt}]
      if system_message:
        messages.insert(0, {"role": "system", "content": system_message})

      api_params: dict[str, Any] = {
          "model": self.model_id,
          "messages": messages,
          "n": 1,
      }

      temp = normalized_config.get("temperature", self.temperature)
      if temp is not None:
        api_params["temperature"] = temp

      if (
          self.format_type == data.FormatType.JSON
          and not self._DISABLE_RESPONSE_FORMAT
      ):
        api_params.setdefault("response_format", {"type": "json_object"})

      if (v := normalized_config.get("max_output_tokens")) is not None:
        api_params["max_tokens"] = v
      if (v := normalized_config.get("top_p")) is not None:
        api_params["top_p"] = v

      for key in self._CONFIG_KEYS:
        if (v := normalized_config.get(key)) is not None:
          api_params[key] = v

      response = None
      last_error: Exception | None = None
      for attempt in range(self._MAX_RETRIES + 1):
        try:
          response = self._client.chat.completions.create(**api_params)
          last_error = None
          break
        except Exception as e:
          last_error = e
          if attempt >= self._MAX_RETRIES or not self._is_retryable_error(e):
            raise
          sleep_s = self._RETRY_BACKOFF_SECONDS * (2 ** attempt)
          log.warning(
              "LLM 请求失败（可重试）: %s；%.1fs 后第 %d 次重试",
              str(e)[:120],
              sleep_s,
              attempt + 1,
          )
          time.sleep(sleep_s)

      if response is None:
        # 理论上不会走到这里，兜底保护。
        raise exceptions.InferenceRuntimeError(
            f"OpenAI API error: {str(last_error) if last_error else 'unknown'}"
        )
      message = response.choices[0].message if response.choices else None
      output_text = self._coerce_message_content(message)

      if not output_text:
        if os.environ.get("LLM_DEBUG_RAW", "").lower() in {"1", "true", "yes"}:
          try:
            raw = response.model_dump_json()
          except Exception:
            raw = str(response)
          log.warning("LLM 原始返回为空 content: %s", raw[:2000])
        raise exceptions.InferenceRuntimeError(
            "OpenAI API returned empty message content."
        )

      if os.environ.get("LLM_DEBUG_RAW", "").lower() in {"1", "true", "yes"}:
        preview = output_text[:500].replace("\n", "\\n")
        log.info("LLM 原始输出预览: %s", preview)

      if self.format_type == data.FormatType.JSON:
        normalized = self._normalize_json_text(output_text)
        if normalized != output_text:
          if os.environ.get("LLM_DEBUG_RAW", "").lower() in {"1", "true", "yes"}:
            preview_norm = normalized[:500].replace("\n", "\\n")
            log.info("LLM JSON 清洗后预览: %s", preview_norm)
        output_text = normalized

      return core_types.ScoredOutput(score=1.0, output=output_text)
    except Exception as e:
      raise exceptions.InferenceRuntimeError(
          f"OpenAI API error: {str(e)}",
          original=e,
      ) from e

  def infer(
      self, batch_prompts: Sequence[str], **kwargs: Any
  ) -> Iterator[Sequence[core_types.ScoredOutput]]:
    """Runs inference with OpenAI-compatible extra params."""
    merged_kwargs = self.merge_kwargs(kwargs)

    config: dict[str, Any] = {}
    temp = merged_kwargs.get("temperature", self.temperature)
    if temp is not None:
      config["temperature"] = temp
    if "max_output_tokens" in merged_kwargs:
      config["max_output_tokens"] = merged_kwargs["max_output_tokens"]
    if "top_p" in merged_kwargs:
      config["top_p"] = merged_kwargs["top_p"]

    for key in self._CONFIG_KEYS:
      if key in merged_kwargs:
        config[key] = merged_kwargs[key]

    if len(batch_prompts) > 1 and self.max_workers > 1:
      with concurrent.futures.ThreadPoolExecutor(
          max_workers=min(self.max_workers, len(batch_prompts))
      ) as executor:
        future_to_index = {
            executor.submit(
                self._process_single_prompt, prompt, config.copy()
            ): i
            for i, prompt in enumerate(batch_prompts)
        }

        results: list[core_types.ScoredOutput | None] = [None] * len(
            batch_prompts
        )
        for future in concurrent.futures.as_completed(future_to_index):
          index = future_to_index[future]
          try:
            results[index] = future.result()
          except Exception as e:
            raise exceptions.InferenceRuntimeError(
                f"Parallel inference error: {str(e)}",
                original=e,
            ) from e

        for result in results:
          if result is None:
            raise exceptions.InferenceRuntimeError(
                "Failed to process one or more prompts"
            )
          yield [result]
    else:
      for prompt in batch_prompts:
        result = self._process_single_prompt(prompt, config.copy())
        yield [result]
