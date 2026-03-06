# -*- coding: utf-8 -*-
"""从 PDF 提取纯文本、清洗截断、分块，供后续 LLM 分析。"""

import re
import logging
from pathlib import Path

logger = logging.getLogger(__name__)

# 前端裁剪：从 Experimental / Materials and Methods 等章节开始保留
_FRONT_TRUNCATE = re.compile(
    r"(?im)^\s*(?:#{1,4}\s*)?(?:"
    r"2[\.\s]+(?:Experimental|Materials|Methods)"
    r"|Experimental\s*(?:Procedure|Section|Details|Methods|Setup)?"
    r"|Materials?\s*and\s*Methods?"
    r"|Methodology"
    r"|实验(?:部分|方法|过程)?"
    r")\s*$"
)

# 后端裁剪：在文本后 30% 区域内匹配以下独立行标题，取最早位置截断
_TRUNCATE_PATTERN = re.compile(
    r"(?im)^\s*("
    r"Acknowledgements|Acknowledgments|"
    r"Declaration of Competing Interest|"
    r"Conflict of interest|"
    r"CRediT authorship contribution statement|"
    r"References|REFERENCES|"
    r"致谢|参考文献"
    r")\s*$"
)


def extract_text_from_pdf(pdf_path: str | Path) -> str:
  """从单个 PDF 提取全文，优先 PyMuPDF，失败时尝试 pdfplumber。"""
  pdf_path = Path(pdf_path)
  if not pdf_path.is_file():
    raise FileNotFoundError(f"PDF 不存在: {pdf_path}")

  try:
    import pymupdf
    doc = pymupdf.open(pdf_path)
    parts = []
    for page in doc:
      parts.append(page.get_text())
    doc.close()
    return "\n".join(parts)
  except Exception as e1:
    try:
      import pdfplumber
      with pdfplumber.open(pdf_path) as doc:
        parts = [p.extract_text() or "" for p in doc.pages]
      return "\n".join(parts)
    except Exception as e2:
      raise RuntimeError(
          f"PyMuPDF 与 pdfplumber 均无法解析 {pdf_path}: pymupdf={e1}, pdfplumber={e2}"
      ) from e2


def list_pdfs(dir_path: str | Path) -> list[Path]:
  """列出目录下所有 .pdf 文件（按文件名排序）。"""
  dir_path = Path(dir_path)
  if not dir_path.is_dir():
    return []
  return sorted(dir_path.glob("*.pdf"))


def clean_and_truncate_text(text: str, trim_front: bool = True) -> str:
  """
  在分块前裁剪论文无关内容。

  裁剪策略：
    1. 前端裁剪（trim_front=True 时）：
       找 Experimental / Materials and Methods 等标题，从此处开始保留，
       丢弃 Abstract、Introduction 等。
    2. 后端裁剪：
       在文本后 30% 区域找 References / Acknowledgements 等标题，截断。

  Returns:
    裁剪后的文本（若匹配不到任何标题则保留原文）。
  """
  if not text or len(text) < 100:
    return text

  start = 0
  end = len(text)

  try:
    # 前端裁剪
    if trim_front:
      m_front = _FRONT_TRUNCATE.search(text)
      if m_front:
        start = m_front.start()
        logger.info(
            "clean_and_truncate: 前端裁剪到 '%s' (pos %d)",
            m_front.group().strip()[:60], start,
        )

    # 后端裁剪
    search_start = max(start, int(len(text) * 0.7))
    search_zone = text[search_start:]
    m = _TRUNCATE_PATTERN.search(search_zone)
    if m:
      end = search_start + m.start()
      logger.info(
          "clean_and_truncate: 后端截断于 '%s' (pos %d), 长度 %d -> %d",
          m.group(1).strip(), end, len(text), end - start,
      )
  except Exception as e:
    logger.warning("clean_and_truncate 异常，保留原文: %s", e)
    return text

  result = text[start:end].rstrip()
  if len(result) < 100 and len(text) > 100:
    logger.warning("裁剪后过短 (%d), 回退原文", len(result))
    return text
  return result


def chunk_text(
  text: str,
  chunk_size: int,
  overlap: int = 500,
) -> list[str]:
  """
  将长文本按固定大小分块，块间保留 overlap 字符重叠以保持上下文连贯。

  Args:
    text: 全文
    chunk_size: 每块目标长度（字符）
    overlap: 块与块之间的重叠长度（字符）

  Returns:
    文本块列表
  """
  if not text or chunk_size <= 0:
    return []
  if len(text) <= chunk_size:
    return [text]

  chunks = []
  start = 0
  while start < len(text):
    end = min(start + chunk_size, len(text))
    chunks.append(text[start:end])
    if end >= len(text):
      break
    start = end - overlap
    if start >= end:
      start = end
  return chunks
