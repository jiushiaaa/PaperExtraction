"""
Global configuration and environment handling for KnowMat 2.0.

This module attempts to locate and load environment variables from a
``.env`` file if present.  It also ensures that critical secrets such as
``LLM_API_KEY`` are set.  When required variables are missing the code will
prompt interactively for them at runtime.

In addition, this module can configure LangSmith tracing when a
``LANGCHAIN_API_KEY`` is provided.
"""

import os
from dotenv import load_dotenv, find_dotenv


# Try to locate a .env file.  The search order is:
# 1) A .env in the current working directory
# 2) A path specified by KNOWMAT2_ENV_FILE
# 3) The first .env found upwards from cwd
_cwd_dotenv = os.path.join(os.getcwd(), ".env")
if os.path.isfile(_cwd_dotenv):
    _env_path = _cwd_dotenv
else:
    _env_path = os.getenv("KNOWMAT2_ENV_FILE", "")
    if not _env_path:
        _env_path = find_dotenv(usecwd=True) or ""

if _env_path:
    load_dotenv(_env_path, override=False)


def _set_env(var: str, required: bool = True) -> None:
    """Prompt for an environment variable when required and missing.

    Parameters
    ----------
    var: str
        Name of the environment variable to ensure.
    required: bool
        Whether this variable is required for runtime execution.
    """
    if required and var not in os.environ:
        import getpass
        os.environ[var] = getpass.getpass(f"{var}: ")


# Ensure that the primary LLM key exists.
_set_env("LLM_API_KEY", required=True)

# Keep LangSmith key optional.
_set_env("LANGCHAIN_API_KEY", required=False)

# Provide OpenAI-compatible env aliases for libraries that still read OPENAI_*.
if os.getenv("LLM_API_KEY") and not os.getenv("OPENAI_API_KEY"):
    os.environ["OPENAI_API_KEY"] = os.environ["LLM_API_KEY"]
if os.getenv("LLM_BASE_URL") and not os.getenv("OPENAI_BASE_URL"):
    os.environ["OPENAI_BASE_URL"] = os.environ["LLM_BASE_URL"]

# LangSmith tracing is optional. Enable by default only if API key is provided.
if os.getenv("LANGCHAIN_API_KEY"):
    os.environ.setdefault("LANGCHAIN_TRACING_V2", "true")
    os.environ.setdefault("LANGCHAIN_PROJECT", "KnowMat2")
else:
    os.environ.setdefault("LANGCHAIN_TRACING_V2", "false")
