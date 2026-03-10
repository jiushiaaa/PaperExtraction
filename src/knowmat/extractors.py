"""
TrustCall extractor definitions for KnowMat 2.0.

This module defines all of the Pydantic models used by TrustCall tools and
provides lazily bound extractors so that each invocation constructs a fresh
ChatOpenAI instance with the current settings.  The pattern follows that
used in the MI‑Agent project.

The three extractors defined here correspond to the three agents in the
KnowMat 2.0 pipeline:

* ``subfield_extractor`` returns a ``SubFieldDetection`` model with two
  fields: ``sub_field`` and ``updated_prompt``.
* ``extraction_extractor`` returns a ``CompositionList`` model consisting
  of compositions and their properties.  The schema mirrors the original
  Pydantic classes from KnowMat v1.
* ``evaluation_extractor`` returns an ``EvaluationFeedback`` model used
  by the evaluation agent to determine whether another extraction pass
  should be performed and to capture suggestions for improving the prompt.

The lazy binding of extractors ensures that long‑running workloads do not
hold onto stale language model instances and makes it straightforward to
adjust the model name or temperature via environment variables.
"""

import os
from typing import List, Optional, Dict, Any
from pydantic import BaseModel, Field, model_validator
from langchain_openai import ChatOpenAI
from trustcall import create_extractor

from knowmat.app_config import settings


def _llm_connection_kwargs() -> Dict[str, str]:
    """Build optional connection kwargs for OpenAI-compatible endpoints."""
    kwargs: Dict[str, str] = {}
    api_key = os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("LLM_BASE_URL") or os.getenv("OPENAI_BASE_URL")
    if api_key:
        kwargs["api_key"] = api_key
    if base_url:
        kwargs["base_url"] = base_url
    return kwargs


def get_llm(agent_type: str = "default") -> ChatOpenAI:
    """Instantiate a ChatOpenAI using the current settings for a specific agent.

    A new instance is created on each call to avoid stale connections
    persisting across multiple extractions.
    
    Parameters
    ----------
    agent_type: str
        The type of agent requesting the LLM. One of: "subfield", "extraction",
        "evaluation", "manager", "flagging", or "default".
    
    Returns
    -------
    ChatOpenAI
        Configured ChatOpenAI instance for the specified agent.
    """
    # Map agent types to their configured models
    model_map = {
        "subfield": settings.subfield_model,
        "extraction": settings.extraction_model,
        "evaluation": settings.evaluation_model,
        "manager": settings.manager_model,
        "flagging": settings.flagging_model,
        "default": settings.model_name
    }
    
    model = model_map.get(agent_type, settings.model_name)
    
    base_kwargs = {
        "model": model,
        "request_timeout": 1200,  # 20 minute timeout per API call (not per pipeline)
        "max_retries": 3,  # Retry failed requests up to 3 times
        **_llm_connection_kwargs(),
    }

    # GPT-5 models don't support temperature parameter
    if any(gpt5_variant in model for gpt5_variant in ["gpt-5", "gpt-5-mini", "gpt-5-nano"]):
        return ChatOpenAI(**base_kwargs)
    else:
        return ChatOpenAI(temperature=settings.temperature, **base_kwargs)


class _LazyExtractor:
    """Wrapper around create_extractor that binds to a fresh LLM each call.

    TrustCall extractors need to be constructed with a particular LLM.
    However, long‑lived extractors can cause open connections and stale
    authentication.  This wrapper delays construction until the first
    invocation and uses the latest settings from ``knowmat2.app_config``.

    Parameters
    ----------
    tools: list
        A list of Pydantic models that define the tool schema.
    tool_choice: str
        The name of the tool (usually the name of the Pydantic class) to
        select when multiple tools are provided.
    enable_inserts: bool
        If True, allow the extractor to insert text into the prompt.
    agent_type: str
        The type of agent this extractor is for (determines which model to use).
    """

    def __init__(self, tools: list, tool_choice: str, enable_inserts: bool = False, 
                 agent_type: str = "default") -> None:
        self.tools = tools
        self.tool_choice = tool_choice
        self.enable_inserts = enable_inserts
        self.agent_type = agent_type

    def invoke(self, *args, **kwargs) -> Dict[str, Any]:
        llm = get_llm(agent_type=self.agent_type)
        extractor = create_extractor(
            llm,
            tools=self.tools,
            tool_choice=self.tool_choice,
            enable_inserts=self.enable_inserts,
        )
        return extractor.invoke(*args, **kwargs)


# -----------------------------------------------------------------------------
# Pydantic schemas defining the structure of TrustCall tool outputs
# -----------------------------------------------------------------------------

class SubFieldDetection(BaseModel):
    """Output schema for the sub‑field detection agent.

    Attributes
    ----------
    sub_field: str
        The niche domain of materials science that best describes the paper.
        One of ``experimental``, ``computational``, ``simulation``,
        ``machine learning`` or ``hybrid``.
    updated_prompt: str
        An updated extraction prompt tailored to the detected sub‑field.
    """

    sub_field: str = Field(
        description=(
            "The detected materials science sub‑field.  Must be one of: experimental, "
            "computational, simulation, machine learning, or hybrid."
        )
    )
    updated_prompt: str = Field(
        description=(
            "An extraction prompt modified to emphasise instructions relevant to the detected sub‑field."
        )
    )


class Property(BaseModel):
    """Represents a material property extracted from the text.
    
    This schema supports both high-fidelity extraction (preserving inequalities,
    ranges, and qualitative values) and ML-ready numeric values for downstream
    database usage and model training.
    """

    property_name: str = Field(
        description=(
            "Full descriptive name of the material property (e.g., 'glass transition temperature', "
            "'melting temperature', 'critical casting diameter', 'fracture strength', 'compressive plasticity')."
        )
    )
    
    property_symbol: Optional[str] = Field(
        default=None,
        description=(
            "Standard symbol or abbreviation for the property as used in the paper (e.g., 'Tg', 'Tm', 'Tx', "
            "'Dc', 'σ_max', 'σ_y', 'ε_p'). Use null if no standard symbol is provided in the paper."
        )
    )
    
    value: Optional[str] = Field(
        description=(
            "Original value as reported in the paper. Can be: "
            "(1) A numeric string like '683.0' for exact measurements, "
            "(2) An inequality like '>50' or '<2000' for bounds, "
            "(3) A range like '12-30' for interval values, "
            "(4) A qualitative descriptor like 'no plasticity' or 'brittle', "
            "(5) null for missing/unreported values (e.g., table shows '-')."
        )
    )
    
    value_numeric: Optional[float] = Field(
        default=None,
        description=(
            "ML-ready numeric value extracted for database and model training. "
            "For exact measurements: the measured value (e.g., 683.0). "
            "For inequalities: the boundary value (e.g., '>50' → 50.0, '<2000' → 2000.0). "
            "For ranges: the midpoint (e.g., '12-30' → 21.0). "
            "For qualitative: a mapped numeric value (e.g., 'no plasticity' → 0.0). "
            "For missing: null."
        )
    )
    
    value_type: str = Field(
        description=(
            "Classification of the value type for downstream processing: "
            "'exact' - precise measurement (e.g., '683.0' K), "
            "'lower_bound' - inequality with '>' (e.g., '>50 mm'), "
            "'upper_bound' - inequality with '<' (e.g., '<2000 MPa'), "
            "'range' - interval (e.g., '12-30 mm'), "
            "'qualitative' - textual descriptor (e.g., 'no plasticity'), "
            "'missing' - not reported in paper (null value)."
        )
    )
    
    unit: Optional[str] = Field(
        default=None,
        description="Measurement unit of the property (e.g., 'K', 'MPa', 'mm', '%')."
    )
    
    measurement_condition: Optional[str] = Field(
        default=None,
        description=(
            "Conditions under which the property was measured. "
            "CRITICAL: If a test temperature is mentioned, ALWAYS start with 'at XXX K' or 'at XXX °C'. "
            "Then add other conditions (pressure, sample geometry, heating rate, strain rate). "
            "Examples: 'at 298 K; strain rate 1e-3 /s', 'at 1073 K; heating rate 20 K/min; Ar atmosphere'. "
            "Use null if not provided."
        )
    )
    
    additional_information: Optional[str] = Field(
        default=None,
        description=(
            "Any additional context related to this property, such as anisotropy details, "
            "figure/table references, uncertainty notes, or data quality flags."
        ),
    )


class CompositionProperties(BaseModel):
    """Represents the properties, processing conditions, and characterisation for a composition."""

    composition: str = Field(
        default="",
        description="The chemical composition of the material as written in the paper (including any abbreviations)."
    )

    role: Optional[str] = Field(
        default="Target",
        description=(
            "Material role in this paper. "
            "'Target' = synthesized, processed, or tested in this work (has original experimental data). "
            "'Reference' = only cited from other papers for comparison (no original data). "
            "Default to 'Target' if unclear."
        )
    )
    
    composition_normalized: Optional[str] = Field(
        default=None,
        description=(
            "Normalized chemical formula containing ONLY element symbols and numbers. "
            "Remove any parenthetical abbreviations or sample codes. "
            "E.g., 'Ti42Hf21Nb21V16 (T42)' → 'Ti42Hf21Nb21V16', "
            "'FeCoCrNiMo0.5' → 'Fe22.22Co22.22Cr22.22Ni22.22Mo11.11'."
        )
    )
    
    source_doi: Optional[str] = Field(
        default=None,
        description=(
            "The DOI of the paper if found in the text. "
            "E.g., '10.1016/j.msea.2024.147225'. Use null if not found."
        )
    )
    
    main_phase: Optional[str] = Field(
        default=None,
        description=(
            "Primary crystal structure identified from XRD, EBSD, or similar characterization. "
            "Use standard abbreviations: BCC, FCC, HCP, amorphous, or combinations like 'FCC + L12', 'BCC + sigma'. "
            "Use null if not mentioned."
        )
    )
    
    has_precipitates: bool = Field(
        default=False,
        description=(
            "Whether any secondary phases or precipitates are mentioned in the microstructure description. "
            "Examples: sigma phase, mu phase, L12, NbC, carbides, nitrides. "
            "Set to true if ANY precipitates are mentioned, false otherwise."
        )
    )
    
    grain_size_avg_um: Optional[float] = Field(
        default=None,
        description=(
            "Average grain size in micrometers (μm). "
            "If reported in nanometers, convert to micrometers (divide by 1000). "
            "Use null if not reported."
        )
    )
    
    processing_conditions: str = Field(
        default="not provided",
        description="Processing conditions applied to the material, or 'not provided'."
    )

    process_category: Optional[str] = Field(
        default=None,
        description=(
            "Manufacturing process category. Use one of: "
            "AM_DED, AM_LPBF, AM_SLM, SPS, Arc_Melting, HeatTreat, Casting, or Unknown. "
            "AM_DED: Directed Energy Deposition / LENS. "
            "AM_LPBF: Laser Powder Bed Fusion. "
            "AM_SLM: Selective Laser Melting. "
            "SPS: Spark Plasma Sintering. "
            "HeatTreat: Heat treatment, annealing, aging. "
            "Casting: Arc melting, melt spinning, casting."
        )
    )
    
    characterisation: Dict[str, str] = Field(
        default_factory=dict,
        description=(
            "Characterisation techniques and their findings keyed by technique names."
        )
    )
    properties_of_composition: List[Property] = Field(
        default_factory=list,
        description="List of standard properties extracted for this composition."
    )
    # non_standard_properties_of_composition: List[Property] = Field(
    #     description="List of non‑standard properties extracted for this composition."
    # )

    @model_validator(mode="after")
    def fill_composition_from_normalized(self) -> "CompositionProperties":
        """When LLM returns only composition_normalized, use it as composition."""
        if not self.composition and self.composition_normalized:
            return self.model_copy(update={"composition": self.composition_normalized})
        return self


class CompositionList(BaseModel):
    """Encapsulates a list of compositions with extracted details."""

    compositions: List[CompositionProperties] = Field(
        description="A list of extracted material compositions."
    )


class EvaluationFeedback(BaseModel):
    """Schema for the evaluation agent's output."""

    confidence_score: float = Field(
        description=(
            "A float between 0 and 1 indicating how accurate the extracted data is compared to the paper."
        )
    )
    rationale: str = Field(
        description="A brief explanation of the evaluation, including missing or hallucinated fields."
    )
    missing_fields: Optional[List[str]] = Field(
        default=None,
        description="A list of fields that were missing from the extraction but present in the paper."
    )
    hallucinated_fields: Optional[List[str]] = Field(
        default=None,
        description="A list of fields that were present in the extraction but not supported by the paper."
    )
    update_prompt: Optional[str] = Field(
        default=None,
        description=(
            "Suggested text to append to the current extraction prompt to improve future extractions."
        )
    )
    needs_rerun: bool = Field(
        description=(
            "Whether another extraction/evaluation cycle should be performed to improve accuracy."
        )
    )


class ManagerFeedback(BaseModel):
    """Schema for the manager agent's output - focused only on aggregation."""

    final_extracted_data: CompositionList = Field(
        description="The final aggregated extraction data combining the best information from all runs."
    )
    
    aggregation_rationale: str = Field(
        description=(
            "Detailed explanation of how data from multiple runs was combined. "
            "Explain what decisions were made, what conflicts were resolved, "
            "which run data was preferred and why."
        )
    )
    
    human_review_guide: str = Field(
        description=(
            "Specific guidance for human reviewers on what to double-check in the final result. "
            "Highlight areas where runs disagreed, uncertain values, or potential issues. "
            "Be specific about compositions, properties, or values to verify."
        )
    )


class FlaggingFeedback(BaseModel):
    """Schema for the flagging agent's output - focused only on quality assessment."""

    final_confidence_score: float = Field(
        description=(
            "A float between 0 and 1 indicating confidence in the final aggregated result. "
            "Base this on the manager's aggregation quality, consistency across runs, "
            "and the complexity of issues noted in the human review guide."
        )
    )
    
    confidence_rationale: str = Field(
        description=(
            "Explanation of why this confidence score was assigned. "
            "Reference the manager's aggregation decisions, run consistency, "
            "and potential review areas."
        )
    )
    
    needs_human_review: bool = Field(
        description=(
            "Whether human review is recommended based on confidence score and review complexity. "
            "Generally true if confidence < 0.8 OR if human review guide indicates significant issues."
        )
    )

# -----------------------------------------------------------------------------
# Lazy extractors exposed for use in nodes
# -----------------------------------------------------------------------------

subfield_extractor = _LazyExtractor(
    [SubFieldDetection], "SubFieldDetection", enable_inserts=True, agent_type="subfield"
)

# The extraction output may be large, so we do not enable inserts here.
extraction_extractor = _LazyExtractor(
    [CompositionList], "CompositionList", enable_inserts=True, agent_type="extraction"
)

evaluation_extractor = _LazyExtractor(
    [EvaluationFeedback], "EvaluationFeedback", enable_inserts=True, agent_type="evaluation"
)

manager_extractor = _LazyExtractor(
    [ManagerFeedback], "ManagerFeedback", enable_inserts=True, agent_type="manager"
)

flagging_extractor = _LazyExtractor(
    [FlaggingFeedback], "FlaggingFeedback", enable_inserts=True, agent_type="flagging"
)
