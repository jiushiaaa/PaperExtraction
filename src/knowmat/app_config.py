"""
Application configuration for KnowMat 2.0.

This module defines a ``Settings`` class using pydantic's ``BaseSettings``
mechanism to manage environment‑configurable options such as the default
output directory, the model to use and the generation temperature.

Environment variables are prefixed with ``KNOWMAT2_``.  For example,
``KNOWMAT2_OUTPUT_DIR`` overrides the default output directory and
``KNOWMAT2_MODEL_NAME`` changes the base model.  See the attributes of
``Settings`` for supported options.
"""

import os
from dotenv import load_dotenv, find_dotenv
from pydantic_settings import BaseSettings

# Load .env early so model defaults can read LLM_MODEL before settings instantiation.
_env_path = find_dotenv(usecwd=True)
if _env_path:
    load_dotenv(_env_path, override=False)

DEFAULT_LLM_MODEL = os.getenv("LLM_MODEL", "gpt-5")


class Settings(BaseSettings):
    """Configuration options for KnowMat 2.0.

    Attributes
    ----------
    input_dir: str
        Default folder where raw ``.pdf``/``.txt`` files are stored. Defaults to
        ``"data/raw"`` relative to the current working directory.

    output_dir: str
        Where extracted results and artifacts will be written.  Defaults to
        ``"data/processed"`` relative to the current working directory.
    
    model_name: str
        The default model name for all agents.  Defaults to ``LLM_MODEL`` when
        set, otherwise ``"gpt-5"``.
    
    temperature: float
        Sampling temperature when generating with the language model.  A
        temperature of 0 yields deterministic outputs.  The default is 0.0.
        Note: GPT-5 models don't support custom temperature settings.
    
    subfield_model: str
        Model for subfield detection agent. Defaults to ``LLM_MODEL``.
    
    extraction_model: str
        Model for extraction agent. Defaults to ``LLM_MODEL``.
    
    evaluation_model: str
        Model for evaluation agent. Defaults to ``LLM_MODEL``.
    
    manager_model: str
        Model for validation agent (Stage 2: hallucination correction).
        Note: "manager_model" name kept for backward compatibility.
        Defaults to ``LLM_MODEL``.
    
    flagging_model: str
        Model for flagging/quality assessment agent. Defaults to ``LLM_MODEL``.
    """

    # IO defaults (can be overridden by env or CLI)
    input_dir: str = "data/raw"
    output_dir: str = "data/processed"
    model_name: str = DEFAULT_LLM_MODEL
    temperature: float = 0.0  # Note: ignored for GPT-5 models
    
    # Per-agent model configuration
    subfield_model: str = DEFAULT_LLM_MODEL
    extraction_model: str = DEFAULT_LLM_MODEL
    evaluation_model: str = DEFAULT_LLM_MODEL
    manager_model: str = DEFAULT_LLM_MODEL
    flagging_model: str = DEFAULT_LLM_MODEL

    class Config:
        env_prefix = "KNOWMAT2_"


# Singleton instance to be imported throughout the package
settings = Settings()
