"""
Top‑level assembly of the KnowMat 2.0 LangGraph workflow.

This module defines two functions: :func:`build_graph` constructs the
LangGraph state machine wiring the individual nodes together, and
:func:`run` orchestrates the end‑to‑end extraction process for a single
PDF document.  The flow is as follows:

1. The PDF is parsed into text.
2. The sub‑field detection agent analyses the text and updates the prompt.
3. An extraction is performed according to the current prompt.
4. The evaluation agent scores the extraction and determines whether another
   cycle is necessary.  Up to ``max_runs`` (default 3) cycles are
   attempted.
5. The manager agent aggregates all runs and produces the final output.

The run function can be invoked from the command line via ``python -m
knowmat2``.  It handles environment and settings initialisation similarly
to the MI‑Agent project and writes the final extraction to the specified
output directory.
"""

import os
import json
import textwrap
import uuid
import re
from typing import Optional

from langgraph.graph import StateGraph, START, END
from langgraph.checkpoint.memory import MemorySaver

from knowmat.states import KnowMatState
from knowmat.post_processing import PostProcessor
from knowmat.nodes.paddleocrvl_parse_pdf import parse_pdf_with_paddleocrvl
from knowmat.nodes.subfield_detection import detect_sub_field
from knowmat.nodes.extraction import extract_data
from knowmat.nodes.evaluation import evaluate_data
from knowmat.nodes.aggregator import aggregate_runs  # Stage 1: Simple data merging
from knowmat.nodes.validator import validate_and_correct  # Stage 2: Hallucination correction & validation
from knowmat.nodes.flagging import assess_final_quality
from knowmat.app_config import Settings, settings
from knowmat.config import _env_path


def _parse_temperature_to_k(measurement_condition: Optional[str]) -> Optional[int]:
    """Best-effort parse of temperature from measurement condition text.
    
    Prioritizes 'at XXX K' format (prompt-optimized), then general patterns.
    Returns integer Kelvin values for consistency with source data.
    """
    if not measurement_condition:
        return None
    txt = measurement_condition.lower()
    
    # Try prompt-optimized format first: "at XXX K"
    m_at = re.search(r"at\s+(-?\d+(?:\.\d+)?)\s*k\b", txt)
    if m_at:
        return round(float(m_at.group(1)))
    
    # Fallback to general pattern
    m = re.search(r"(-?\d+(?:\.\d+)?)\s*(k|°c|c)\b", txt)
    if not m:
        return None
    value = float(m.group(1))
    unit = m.group(2)
    if unit in {"°c", "c"}:
        return round(value + 273)  # Convert to K without .15 offset
    return round(value)  # Ensure integer output


def _build_composition_json(formula: str) -> dict:
    """Convert formula string like Ti42Hf21Nb21V16 to a composition dict.
    
    Handles nested parentheses (e.g., '(Nb15Ta10W75)98.5C1.5') by:
    - Removing all parentheses before parsing
    - Extracting element-number pairs globally
    
    For normalized formulas, atomic percentages should sum to 100.
    """
    comp = {}
    if not formula:
        return comp
    
    # Remove all parentheses and brackets to simplify parsing
    cleaned = re.sub(r"[()[\]{}]", "", formula)
    
    # Extract all element-number pairs
    for element, amount in re.findall(r"([A-Z][a-z]?)(\d+(?:\.\d+)?)", cleaned):
        comp[element] = float(amount)
    
    return comp


# Complete periodic table of valid element symbols
VALID_ELEMENTS = {
    # Period 1-2
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
    # Period 3
    "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
    # Period 4
    "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
    "Ga", "Ge", "As", "Se", "Br", "Kr",
    # Period 5
    "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd",
    "In", "Sn", "Sb", "Te", "I", "Xe",
    # Period 6
    "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy",
    "Ho", "Er", "Tm", "Yb", "Lu",
    "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi", "Po", "At", "Rn",
    # Period 7
    "Fr", "Ra", "Ac", "Th", "Pa", "U", "Np", "Pu", "Am", "Cm", "Bk", "Cf",
}


def _validate_composition_json(comp_json: dict, formula_source: str = "") -> tuple[dict, list[str]]:
    """Validate and clean composition JSON.
    
    Checks:
    1. All element symbols are valid (removes invalid ones)
    2. Atomic percentages sum to approximately 100 (±2% tolerance)
    
    Returns:
        tuple: (cleaned_composition_dict, warnings_list)
    """
    warnings = []
    cleaned = {}
    
    for elem, val in comp_json.items():
        if elem not in VALID_ELEMENTS:
            warnings.append(f"Invalid element '{elem}' removed from {formula_source}")
            continue
        cleaned[elem] = val
    
    # Check sum if composition is non-empty
    if cleaned:
        total = sum(cleaned.values())
        if abs(total - 100) > 2:
            warnings.append(
                f"Composition sum = {total:.2f} at%, expected ~100 (±2%). Formula: {formula_source}"
            )
    
    return cleaned, warnings


def _extract_first_doi(text: Optional[str]) -> str:
    """Extract first DOI-like token from text."""
    if not text:
        return ""
    m = re.search(r"\b10\.\d{4,9}/[-._;()/:A-Za-z0-9]+\b", text)
    return m.group(0) if m else ""


def _infer_main_phase(char_text: str) -> str:
    """Infer main phase from characterization text (fallback heuristic)."""
    if not char_text:
        return ""
    ctext = char_text.lower()
    
    # Check for common phase mentions
    phases = []
    if "bcc" in ctext:
        phases.append("BCC")
    if "fcc" in ctext:
        phases.append("FCC")
    if "hcp" in ctext:
        phases.append("HCP")
    if "amorphous" in ctext or "glassy" in ctext:
        phases.append("amorphous")
    
    # Check for ordered structures
    if "l12" in ctext or "l1_2" in ctext:
        phases.append("L12")
    if "laves" in ctext:
        phases.append("Laves")
    if "sigma" in ctext and "phase" in ctext:
        phases.append("sigma")
    
    if not phases:
        return ""
    
    # Return combined if multiple
    return " + ".join(phases[:3])  # Limit to 3 main phases


def _infer_precipitates(char_text: str) -> bool:
    """Infer presence of precipitates from characterization text (fallback heuristic)."""
    if not char_text:
        return False
    ctext = char_text.lower()
    keywords = [
        "precipitate", "precipitates", "precipitation",
        "carbide", "nitride", "oxide",
        "nbc", "tic", "tac", "vc", "cr23c6",
        "sigma phase", "mu phase", "chi phase",
        "l12", "l21", "laves",
    ]
    return any(kw in ctext for kw in keywords)


def _to_target_schema(data: dict, source_path: str, paper_text: Optional[str] = None) -> dict:
    """Convert internal extraction schema to target HEA dataset schema.
    
    New behavior:
    - Filters out compositions where role != "Target"
    - Groups compositions by normalized formula (removing condition suffixes like '[As-Built]')
    - Creates one Material per unique formula with multiple Samples for different conditions
    """
    if not isinstance(data, dict):
        return {"Dataset_Description": "High Entropy Alloy Data Extraction Template", "Materials": []}
    if "Materials" in data and "Dataset_Description" in data:
        return data

    from collections import defaultdict
    
    compositions = data.get("compositions", []) or []
    source_name = os.path.basename(source_path)
    source_doi = _extract_first_doi(paper_text)
    
    # Helper functions (defined first to be accessible in loops)
    def normalize_property_name(name: Optional[str]) -> Optional[str]:
        """Map common property name variants to standardized names."""
        if not name:
            return name
        key = name.strip().lower()
        mapping = {
            # Mechanical - Tensile
            "yield strength": "Yield_Strength",
            "compressive yield strength": "Yield_Strength",
            "ultimate tensile strength": "Ultimate_Tensile_Strength",
            "ultimate compressive strength": "Ultimate_Compressive_Strength",
            "tensile strength": "Ultimate_Tensile_Strength",
            "uts": "Ultimate_Tensile_Strength",
            
            # Mechanical - Elongation
            "total elongation": "Total_Elongation",
            "uniform elongation": "Uniform_Elongation",
            "elongation": "Elongation",
            "fracture strain": "Fracture_Strain",
            "ductility": "Elongation",
            
            # Mechanical - Modulus
            "young's modulus": "Youngs_Modulus",
            "elastic modulus": "Youngs_Modulus",
            "modulus": "Youngs_Modulus",
            
            # Microstructure
            "grain size": "Grain_Size",
            "average grain size": "Grain_Size",
            "grain diameter": "Grain_Size",
            "relative density": "Relative_Density",
            "density": "Density",
            "porosity": "Porosity",
            "dislocation density": "Dislocation_Density",
            
            # Thermal/Physical
            "lattice parameter": "Lattice_Parameter",
            "lattice constant": "Lattice_Parameter",
            "stacking fault energy": "Stacking_Fault_Energy",
            "sfe": "Stacking_Fault_Energy",
        }
        return mapping.get(key, re.sub(r"[^A-Za-z0-9]+", "_", name).strip("_"))

    def infer_process_category(process_text: str) -> str:
        """Infer manufacturing process category from processing conditions text."""
        t = (process_text or "").lower()
        
        # Additive Manufacturing - DED
        if any(k in t for k in ("lens", "ded", "directed energy deposition", "laser-engineered net shaping", "laser cladding")):
            return "AM_DED"
        
        # Additive Manufacturing - LPBF
        if any(k in t for k in ("lpbf", "l-pbf", "laser powder bed fusion", "powder bed fusion")):
            return "AM_LPBF"
        
        # Additive Manufacturing - SLM (more specific than LPBF)
        if any(k in t for k in ("slm", "selective laser melting")):
            return "AM_SLM"
        
        # Additive Manufacturing - WAAM
        if any(k in t for k in ("waam", "wire arc additive", "wire + arc")):
            return "WAAM"
        
        # Additive Manufacturing - EBM
        if any(k in t for k in ("ebm", "electron beam melting")):
            return "EBM"
        
        # Spark Plasma Sintering
        if any(k in t for k in ("sps", "spark plasma sintering")):
            return "SPS"
        
        # Hot Isostatic Pressing
        if any(k in t for k in ("hip", "hot isostatic pressing")):
            return "HIP"
        
        # Arc Melting
        if any(k in t for k in ("arc melting", "vacuum arc melting", "arc-melting")):
            return "Arc_Melting"
        
        # Heat Treatment (post-processing only)
        if any(k in t for k in ("heat treat", "annealed", "annealing", "aged", "aging", "solution treatment", "quench")):
            return "HeatTreat"
        
        # Casting
        if any(k in t for k in ("cast", "casting", "melt spinning", "suction casting", "induction melting")):
            return "Casting"
        
        # Forging
        if any(k in t for k in ("forging", "forged", "hot forging", "cold forging")):
            return "Forging"
        
        # Rolling
        if any(k in t for k in ("rolling", "rolled", "hot rolling", "cold rolling")):
            return "Rolling"
        
        # Mechanical Alloying
        if any(k in t for k in ("mechanical alloying", "ball milling", "high-energy ball milling")):
            return "Mechanical_Alloying"
        
        return "Unknown"
    
    # Step 1: Filter only Target materials
    target_compositions = [c for c in compositions if c.get("role", "Target") == "Target"]
    
    # Step 2: Group by base formula (remove [...] condition suffixes)
    groups = defaultdict(list)
    for comp in target_compositions:
        comp_raw = comp.get("composition", "") or ""
        # Prioritize LLM's composition_normalized
        formula_norm = comp.get("composition_normalized")
        if not formula_norm:
            formula_norm = comp_raw.replace(" ", "")
        
        # Remove condition suffix like '[As-Built]' or '[Annealed 973K/64h]' to get base formula
        base_formula = re.sub(r"\s*\[.*?\]\s*$", "", formula_norm).strip()
        if not base_formula:
            base_formula = formula_norm  # Fallback if no condition suffix
        
        groups[base_formula].append(comp)
    
    materials = []

    # Step 3: Build Materials with multiple Samples
    for mat_idx, (base_formula, comps) in enumerate(sorted(groups.items()), start=1):
        # Use first composition's metadata for Material-level fields
        first_comp = comps[0]
        comp_raw_first = first_comp.get("composition", "") or ""
        
        # Material-level DOI: prioritize LLM output, fallback to global
        material_doi = first_comp.get("source_doi")
        if not material_doi:
            material_doi = source_doi
        
        # Build Samples from each composition in this group
        samples = []
        for s_idx, comp in enumerate(comps, start=1):
            comp_raw = comp.get("composition", "") or ""
            
            # Extract condition suffix for Sample_ID
            match = re.search(r"\[(.*?)\]\s*$", comp_raw)
            condition_suffix = match.group(1).replace(" ", "_") if match else "Default"
            
            # Build Performance_Tests from properties
            props = comp.get("properties_of_composition", []) or []
            tests = []
            for j, p in enumerate(props, start=1):
                numeric_val = p.get("value_numeric")
                if numeric_val is None:
                    continue
                tests.append(
                    {
                        "Test_ID": f"T{j:03d}",
                        "Test_Temperature_K": _parse_temperature_to_k(p.get("measurement_condition")),
                        "Property_Type": normalize_property_name(p.get("property_name")),
                        "Property_Value": numeric_val,
                        "Property_Unit": p.get("unit"),
                    }
                )
            
            process_text = comp.get("processing_conditions")
            if isinstance(process_text, dict):
                process_text = json.dumps(process_text, ensure_ascii=False)
            char_text = comp.get("characterisation")
            if isinstance(char_text, dict):
                char_text = "; ".join([f"{k}: {v}" for k, v in char_text.items()])
            
            # Prioritize LLM outputs, fallback to inference
            main_phase = comp.get("main_phase")
            if not main_phase:
                main_phase = _infer_main_phase(char_text or "")
            
            has_precipitates_val = comp.get("has_precipitates")
            if has_precipitates_val is None:
                has_precipitates_val = _infer_precipitates(char_text or "")
            
            grain_size_um = comp.get("grain_size_avg_um")
            
            process_category = comp.get("process_category")
            if not process_category or process_category == "Unknown":
                process_category = infer_process_category(process_text or "")
            
            sample = {
                "Sample_ID": f"S{mat_idx:03d}_{s_idx:02d}_{condition_suffix}",
                "Process_Category": process_category,
                "Process_Text_For_AI": process_text or "not provided",
                "Key_Params_JSON": {},
                "Main_Phase": main_phase or "",
                "Microstructure_Text_For_AI": char_text or "not provided",
                "Has_Precipitates": has_precipitates_val,
                "Grain_Size_avg_um": grain_size_um,
                "Performance_Tests": tests,
            }
            samples.append(sample)
        
        # Build and validate Composition_JSON
        raw_comp_json = _build_composition_json(base_formula)
        validated_comp_json, comp_warnings = _validate_composition_json(raw_comp_json, base_formula)
        
        # Print warnings if any
        for warning in comp_warnings:
            print(f"[COMPOSITION WARNING] {warning}")
        
        # Build Material entry
        material = {
            "description": f"--- Material {mat_idx}: {base_formula} ---",
            "Mat_ID": f"M{mat_idx:03d}",
            "Alloy_Name_Raw": comp_raw_first,
            "Formula_Normalized": base_formula,
            "Composition_JSON": validated_comp_json,
            "Source_DOI": material_doi or "",
            "Source_File": source_name,
            "Processed_Samples": samples,
        }
        materials.append(material)

    return {
        "Dataset_Description": "High Entropy Alloy Data Extraction Template",
        "schema_version": "2.1",
        "pipeline_version": "knowmat-2.0.1",
        "Materials": materials,
    }


def evaluation_condition(state: KnowMatState) -> str:
    """Decide whether to rerun extraction or proceed to aggregation.

    Called by the graph when the evaluation node completes.  If
    ``state['needs_rerun']`` is true and ``state['run_count']`` is less
    than ``state['max_runs']`` the function returns the name of the
    extraction node to trigger another cycle.  Otherwise it returns
    ``aggregate_runs`` to begin the two-stage manager process.
    """
    run_count = state.get("run_count", 0)
    max_runs = state.get("max_runs", 3)
    needs_rerun = state.get("needs_rerun", False)
    if needs_rerun and run_count < max_runs:
        return "extract_data"
    return "aggregate_runs"


def build_graph(full_pipeline: bool = True) -> StateGraph:
    """Construct the LangGraph for KnowMat 2.0 with two-stage manager."""
    builder = StateGraph(KnowMatState)
    
    # Register all nodes
    builder.add_node("parse_pdf", parse_pdf_with_paddleocrvl)
    builder.add_node("extract_data", extract_data)

    builder.add_edge(START, "parse_pdf")
    if not full_pipeline:
        # Fast mode: parse -> extract -> end
        builder.add_edge("parse_pdf", "extract_data")
        builder.add_edge("extract_data", END)
    else:
        builder.add_node("detect_sub_field", detect_sub_field)
        builder.add_node("evaluate_data", evaluate_data)
        builder.add_node("aggregate_runs", aggregate_runs)  # Stage 1: Merge runs
        builder.add_node("validate_and_correct", validate_and_correct)  # Stage 2: Correct hallucinations
        builder.add_node("assess_final_quality", assess_final_quality)

        # Wire edges - full manager flow
        builder.add_edge("parse_pdf", "detect_sub_field")
        builder.add_edge("detect_sub_field", "extract_data")
        builder.add_edge("extract_data", "evaluate_data")
        builder.add_conditional_edges("evaluate_data", evaluation_condition, ["extract_data", "aggregate_runs"])
        builder.add_edge("aggregate_runs", "validate_and_correct")  # Stage 1 → Stage 2
        builder.add_edge("validate_and_correct", "assess_final_quality")  # Stage 2 → Flagging
        builder.add_edge("assess_final_quality", END)
    
    return builder.compile(checkpointer=MemorySaver())


def run(
    pdf_path: str,
    output_dir: Optional[str] = None,
    model_name: Optional[str] = None,
    max_runs: int = 3,
    subfield_model: Optional[str] = None,
    extraction_model: Optional[str] = None,
    evaluation_model: Optional[str] = None,
    manager_model: Optional[str] = None,
    flagging_model: Optional[str] = None,
    full_pipeline: bool = False,
    enable_property_standardization: bool = False,
) -> dict:
    """Run the full KnowMat 2.0 pipeline on a given input file and write results.
    
    Parameters
    ----------
    pdf_path : str
        Path to the materials science paper in ``.pdf`` or ``.txt`` format.
    output_dir : Optional[str]
        Directory where results will be saved. If not provided, uses default from settings.
    model_name : Optional[str]
        Override the base model (e.g., "gpt-4", "gpt-5-mini"). If not provided, uses default from settings.
    max_runs : int
        Maximum number of extraction/evaluation cycles. Default is 3.
    subfield_model : Optional[str]
        Model for subfield detection agent. Overrides default.
    extraction_model : Optional[str]
        Model for extraction agent. Overrides default.
    evaluation_model : Optional[str]
        Model for evaluation agent. Overrides default.
    manager_model : Optional[str]
        Model for manager aggregation agent. Overrides default.
    flagging_model : Optional[str]
        Model for flagging/quality assessment agent. Overrides default.
    full_pipeline : bool
        If True, run subfield/evaluation/aggregation/validation stages.
        If False, run fast template extraction only (default).
    enable_property_standardization : bool
        If True, run optional property post-processing (extra LLM calls).
    
    Returns
    -------
    dict
        Results dictionary containing final_data, flag, output_dir, etc.
    """
    
    # Load environment variables if a .env was found
    if _env_path:
        print(f"Loaded environment variables from: {_env_path}")

    # Apply any CLI overrides to settings
    overrides = {}
    if output_dir:
        overrides["output_dir"] = output_dir
    if model_name:
        overrides["model_name"] = model_name
    
    # Per-agent model overrides
    if subfield_model:
        overrides["subfield_model"] = subfield_model
    if extraction_model:
        overrides["extraction_model"] = extraction_model
    if evaluation_model:
        overrides["evaluation_model"] = evaluation_model
    if manager_model:
        overrides["manager_model"] = manager_model
    if flagging_model:
        overrides["flagging_model"] = flagging_model
    
    if overrides:
        new_settings = Settings(**overrides)
        settings.__dict__.update(new_settings.model_dump())
    
    # Default all per-agent models to model_name when not overridden.
    if not subfield_model and not overrides.get("subfield_model"):
        settings.subfield_model = settings.model_name
    if not extraction_model and not overrides.get("extraction_model"):
        settings.extraction_model = settings.model_name
    if not evaluation_model and not overrides.get("evaluation_model"):
        settings.evaluation_model = settings.model_name
    if not manager_model and not overrides.get("manager_model"):
        settings.manager_model = settings.model_name
    if not flagging_model and not overrides.get("flagging_model"):
        settings.flagging_model = settings.model_name

    # Print model configuration
    print(f"\nModel Configuration:")
    print(f"   Subfield Detection: {settings.subfield_model}")
    print(f"   Extraction:         {settings.extraction_model}")
    print(f"   Evaluation:         {settings.evaluation_model}")
    print(f"   Aggregation:        rule-based (no LLM)")
    print(f"   Validation:         {settings.manager_model}")
    print(f"   Flagging:           {settings.flagging_model}")

    # Create paper-specific subfolder BEFORE running the graph
    # This ensures all nodes (including OCR parser) save to the correct location
    base_name = os.path.splitext(os.path.basename(pdf_path))[0]
    paper_output_dir = os.path.join(settings.output_dir, base_name)
    os.makedirs(paper_output_dir, exist_ok=True)
    
    print(f"\nOutput directory: {paper_output_dir}\n")

    # Prepare the initial state with paper-specific output directory
    state: KnowMatState = {
        "pdf_path": pdf_path,
        "output_dir": paper_output_dir,  # Use paper-specific directory
        "run_count": 0,
        "run_results": [],
        "max_runs": max_runs,
    }

    # Use a unique thread ID for each paper to avoid context accumulation
    thread_id = f"knowmat2_{base_name}_{uuid.uuid4().hex[:8]}"
    thread_config = {"configurable": {"thread_id": thread_id}}

    # Execute the graph
    graph = build_graph(full_pipeline=full_pipeline)
    for _ in graph.stream(state, thread_config, stream_mode="values"):
        pass

    final_state = graph.get_state(thread_config).values
    final_data = final_state.get("final_data", {})
    if not final_data:
        final_data = final_state.get("latest_extracted_data", {})
    flag = final_state.get("flag", False) if full_pipeline else False

    # Apply property standardization using PostProcessor
    if enable_property_standardization and final_data and final_data.get("compositions"):
        print(f"\nStandardizing property names...")
        try:
            # Initialize PostProcessor with properties.json
            properties_file = os.path.join(os.path.dirname(__file__), "properties.json")
            api_key = os.getenv("LLM_API_KEY") or os.getenv("OPENAI_API_KEY")
            base_url = os.getenv("LLM_BASE_URL") or os.getenv("OPENAI_BASE_URL")
            
            if not api_key:
                print("Warning: LLM_API_KEY not found. Skipping property standardization.")
            elif not os.path.exists(properties_file):
                print(f"Warning: properties.json not found at {properties_file}. Skipping.")
            else:
                processor = PostProcessor(
                    properties_file=properties_file,
                    api_key=api_key,
                    base_url=base_url,
                    gpt_model=settings.flagging_model or settings.model_name,
                )
                
                # Create a mock structure for the PostProcessor
                # It expects: [{"data": {"compositions": [...]}}]
                mock_result = [{"data": final_data}]
                
                # Update with standardized properties
                processor.update_extracted_json(mock_result)
                
                # Extract the updated final_data back (it's modified in place)
                final_data = mock_result[0]["data"]
                
                # Print statistics
                processor._print_match_stats()
                print(f"Property standardization complete\n")
        except Exception as e:
            print(f"Warning: Property standardization failed: {str(e)}")
            print(f"Continuing with non-standardized properties.\n")

    # Convert output to requested target schema
    final_data = _to_target_schema(final_data, pdf_path, final_state.get("paper_text"))

    # Write final extraction JSON
    output_path = os.path.join(paper_output_dir, f"{base_name}_extraction.json")
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(final_data, f, ensure_ascii=False, indent=2)
    print(f"Saved extraction to {output_path}")

    # Write comprehensive analysis report
    report_path = os.path.join(paper_output_dir, f"{base_name}_analysis_report.txt")
    with open(report_path, "w", encoding="utf-8") as f:
        _write_comprehensive_report(f, final_state)
    print(f"Saved analysis report to {report_path}")

    # Write run details for debugging
    runs_path = os.path.join(paper_output_dir, f"{base_name}_runs.json")
    with open(runs_path, "w", encoding="utf-8") as f:
        json.dump(final_state.get("run_results", []), f, ensure_ascii=False, indent=2)

    # Generate QA Report with red-line checks
    materials = final_data.get("Materials", [])
    all_samples = [s for m in materials for s in m.get("Processed_Samples", [])]
    all_tests = [t for s in all_samples for t in s.get("Performance_Tests", [])]
    
    # Count metrics
    unknown_process_count = sum(1 for s in all_samples if s.get("Process_Category") == "Unknown")
    phase_filled_count = sum(1 for s in all_samples if s.get("Main_Phase"))
    phase_filled_rate = phase_filled_count / len(all_samples) if all_samples else 0
    
    # Red-line checks
    red_line_triggers = []
    if len(materials) == 0:
        red_line_triggers.append("NO_TARGET_MATERIALS")
    if len(all_tests) == 0:
        red_line_triggers.append("NO_PROPERTIES")
    if all_samples:
        unknown_ratio = unknown_process_count / len(all_samples)
        if unknown_ratio > 0.5:
            red_line_triggers.append("HIGH_UNKNOWN_PROCESS_RATIO")
    
    qa_report = {
        "paper_name": base_name,
        "pipeline_version": "knowmat-2.0.1",
        "materials_target_count": len(materials),
        "samples_count": len(all_samples),
        "properties_count": len(all_tests),
        "unknown_process_count": unknown_process_count,
        "phase_filled_rate": round(phase_filled_rate, 3),
        "missing_doi": 1 if not materials or not materials[0].get("Source_DOI") else 0,
        "needs_review": len(red_line_triggers) > 0,
        "red_line_triggers": red_line_triggers,
        "final_confidence_score": final_state.get("final_confidence_score"),
    }
    
    qa_path = os.path.join(paper_output_dir, f"{base_name}_qa_report.json")
    with open(qa_path, "w", encoding="utf-8") as f:
        json.dump(qa_report, f, ensure_ascii=False, indent=2)
    print(f"Saved QA report to {qa_path}")
    
    # Print red-line warnings
    if red_line_triggers:
        print(f"\n[RED LINE] QA check failed: {', '.join(red_line_triggers)}")
        print(f"           Human review REQUIRED for {base_name}")

    return {
        "final_data": final_data,
        "flag": flag,
        "output_dir": paper_output_dir,  # Return paper-specific directory
        "final_confidence_score": final_state.get("final_confidence_score"),
        "aggregation_rationale": final_state.get("aggregation_rationale"),
        "human_review_guide": final_state.get("human_review_guide"),
    }


def _write_comprehensive_report(f, final_state):
    """Write a comprehensive analysis report to the file handle."""
    
    f.write(f"{'='*80}\n")
    f.write(f"KNOWMAT 2.0 EXTRACTION ANALYSIS REPORT\n")
    f.write(f"{'='*80}\n\n")
    
    # Final Assessment Section
    f.write(f"{'█'*80}\n")
    f.write(f"FINAL ASSESSMENT\n")
    f.write(f"{'█'*80}\n\n")
    
    final_confidence = final_state.get("final_confidence_score", "N/A")
    needs_review = final_state.get("needs_human_review", True)
    confidence_rationale = final_state.get("confidence_rationale", "")
    
    f.write(f"Final Confidence Score: {final_confidence}\n")
    f.write(f"Human Review Required: {'Yes' if needs_review else 'No'}\n")
    f.write(f"Review Flag: {'🚩 FLAGGED' if needs_review else '✅ PASSED'}\n\n")
    
    if confidence_rationale:
        f.write(f"Confidence Assessment Rationale:\n")
        f.write(f"{'-'*40}\n")
        wrapped_rationale = textwrap.fill(confidence_rationale, width=80, subsequent_indent="  ")
        f.write(f"{wrapped_rationale}\n\n")
    
    # Manager Aggregation Section
    f.write(f"{'█'*80}\n")
    f.write(f"MANAGER AGGREGATION ANALYSIS\n")
    f.write(f"{'█'*80}\n\n")
    
    aggregation_rationale = final_state.get("aggregation_rationale", "")
    if aggregation_rationale:
        f.write(f"How Data Was Combined:\n")
        f.write(f"{'-'*25}\n")
        wrapped_aggregation = textwrap.fill(aggregation_rationale, width=80, subsequent_indent="  ")
        f.write(f"{wrapped_aggregation}\n\n")
    
    # Human Review Guide Section
    f.write(f"{'█'*80}\n")
    f.write(f"HUMAN REVIEW GUIDANCE\n")
    f.write(f"{'█'*80}\n\n")
    
    human_review_guide = final_state.get("human_review_guide", "")
    if human_review_guide:
        f.write(f"Items to Double-Check:\n")
        f.write(f"{'-'*22}\n")
        wrapped_guide = textwrap.fill(human_review_guide, width=80, subsequent_indent="  ")
        f.write(f"{wrapped_guide}\n\n")
    
    # Per-Run Analysis Section
    f.write(f"{'█'*80}\n")
    f.write(f"INDIVIDUAL RUN ANALYSIS\n")
    f.write(f"{'█'*80}\n\n")
    
    run_results = final_state.get("run_results", [])
    for i, run in enumerate(run_results, 1):
        f.write(f"{'▓'*60}\n")
        f.write(f"RUN {run.get('run_id', i)} DETAILS\n")
        f.write(f"{'▓'*60}\n")
        f.write(f"Confidence Score: {run.get('confidence_score', 0.0):.2f}\n\n")
        
        rationale_text = run.get('rationale', 'N/A')
        f.write(f"Evaluation Rationale:\n")
        wrapped_rationale = textwrap.fill(rationale_text, width=80, subsequent_indent="  ")
        f.write(f"  {wrapped_rationale}\n\n")
        
        missing = run.get('missing_fields') or []
        if missing:
            f.write(f"Missing Fields ({len(missing)} items):\n")
            for j, field in enumerate(missing[:15], 1):  # Show first 15
                f.write(f"  {j:2d}. {field}\n")
            if len(missing) > 15:
                f.write(f"      ... and {len(missing) - 15} more items\n")
            f.write("\n")
        
        hallucinated = run.get('hallucinated_fields') or []
        if hallucinated:
            f.write(f"Hallucinated Fields ({len(hallucinated)} items):\n")
            for j, field in enumerate(hallucinated[:15], 1):  # Show first 15
                f.write(f"  {j:2d}. {field}\n")
            if len(hallucinated) > 15:
                f.write(f"      ... and {len(hallucinated) - 15} more items\n")
            f.write("\n")
        
        suggestions = run.get('suggested_prompt')
        if suggestions and suggestions.strip():
            f.write(f"Improvement Suggestions:\n")
            wrapped_suggestions = textwrap.fill(suggestions, width=80, subsequent_indent="  ")
            f.write(f"  {wrapped_suggestions}\n\n")
        
        # Add composition summary
        extracted_data = run.get('extracted_data', {})
        compositions = extracted_data.get('compositions', [])
        f.write(f"Compositions Extracted: {len(compositions)}\n")
        if compositions:
            f.write(f"Sample Compositions: ")
            comp_names = [comp.get('composition', 'Unknown') for comp in compositions[:3]]
            f.write(f"{', '.join(comp_names)}")
            if len(compositions) > 3:
                f.write(f" (and {len(compositions) - 3} more)")
            f.write("\n")
        f.write("\n")
    
    # Summary Statistics
    f.write(f"{'█'*80}\n")
    f.write(f"EXTRACTION STATISTICS\n")
    f.write(f"{'█'*80}\n\n")
    
    if run_results:
        scores = [run.get('confidence_score', 0.0) for run in run_results]
        f.write(f"Number of Extraction Runs: {len(run_results)}\n")
        f.write(f"Average Run Confidence: {sum(scores)/len(scores):.2f}\n")
        f.write(f"Best Run Confidence: {max(scores):.2f}\n")
        f.write(f"Worst Run Confidence: {min(scores):.2f}\n\n")
        
        total_missing = sum(len(run.get('missing_fields') or []) for run in run_results)
        total_hallucinated = sum(len(run.get('hallucinated_fields') or []) for run in run_results)
        f.write(f"Total Missing Fields Across Runs: {total_missing}\n")
        f.write(f"Total Hallucinated Fields Across Runs: {total_hallucinated}\n\n")
    
    final_data = final_state.get("final_data", {})
    final_compositions = final_data.get('compositions', [])
    f.write(f"Final Extracted Compositions: {len(final_compositions)}\n")
    if final_compositions:
        total_props = sum(len(comp.get('properties_of_composition', [])) for comp in final_compositions)
        f.write(f"Total Properties in Final Result: {total_props}\n")
    
    f.write(f"\n{'='*80}\n")
    f.write(f"END OF REPORT\n")
    f.write(f"{'='*80}\n")
