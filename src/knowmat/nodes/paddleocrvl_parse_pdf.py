"""
PDF parsing node using PaddleOCR-VL (with PaddleOCR fallback).

This parser renders each PDF page to an image, runs OCR, and returns a single
markdown-like text block for downstream extraction agents.
"""

import os
import json
import re
from pathlib import Path
from typing import Any, Dict, List, Tuple

from knowmat.states import KnowMatState


def _default_model_dir() -> Path:
    """Return the default local model directory in this project."""
    repo_root = Path(__file__).resolve().parents[3]
    model_dir = os.getenv("PADDLEOCRVL_MODEL_DIR", str(repo_root / "models" / "paddleocrvl1_5"))
    return Path(model_dir).expanduser().resolve()


def _prepare_ocr_home(model_dir: Path) -> None:
    """Ensure local model directory exists and is used by PaddleOCR."""
    model_dir.mkdir(parents=True, exist_ok=True)
    os.environ["PADDLEOCR_HOME"] = str(model_dir)


def _create_ocr_engine(model_dir: Path) -> Tuple[Any, str]:
    """Create a PaddleOCR-VL engine, or fallback to PaddleOCR."""
    _prepare_ocr_home(model_dir)

    try:
        from paddleocr import PaddleOCRVL  # type: ignore

        for kwargs in ({}, {"lang": "en"}, {"model_dir": str(model_dir)}, {"lang": "en", "model_dir": str(model_dir)}):
            try:
                return PaddleOCRVL(**kwargs), "paddleocrvl"
            except TypeError:
                continue
    except Exception:
        pass

    try:
        from paddleocr import PaddleOCR  # type: ignore
    except Exception as exc:
        raise ImportError(
            "PaddleOCR is not installed. Install `paddleocr` and `paddlepaddle` first."
        ) from exc

    init_candidates = (
        {"use_angle_cls": True, "lang": "en"},
        {"lang": "en"},
        {},
    )
    last_error: Exception | None = None
    for kwargs in init_candidates:
        try:
            return PaddleOCR(**kwargs), "paddleocr"
        except TypeError as exc:
            last_error = exc

    if last_error:
        raise RuntimeError(f"Failed to initialize PaddleOCR engine: {last_error}") from last_error
    raise RuntimeError("Failed to initialize PaddleOCR engine.")


def _run_ocr(engine: Any, image_path: Path) -> Any:
    """Run OCR for a single page image with broad API compatibility."""
    img = str(image_path)

    if hasattr(engine, "predict"):
        try:
            return engine.predict(img)
        except TypeError:
            return engine.predict(input=img)
        except Exception:
            pass

    if hasattr(engine, "ocr"):
        try:
            return engine.ocr(img, cls=True)
        except TypeError:
            return engine.ocr(img)

    if callable(engine):
        return engine(img)

    raise RuntimeError("OCR engine does not expose a known inference method.")


def _collect_text(obj: Any, out: List[str]) -> None:
    """Recursively collect OCR text from mixed response structures."""
    if obj is None:
        return

    if isinstance(obj, str):
        text = obj.strip()
        if text:
            out.append(text)
        return

    if isinstance(obj, dict):
        for key in ("text", "rec_text", "ocr_text", "content", "transcription"):
            val = obj.get(key)
            if isinstance(val, str):
                val = val.strip()
                if val:
                    out.append(val)
        for val in obj.values():
            _collect_text(val, out)
        return

    if isinstance(obj, (list, tuple)):
        # PaddleOCR classic format: [box, (text, score)]
        if (
            len(obj) == 2
            and isinstance(obj[1], (list, tuple))
            and len(obj[1]) > 0
            and isinstance(obj[1][0], str)
        ):
            text = obj[1][0].strip()
            if text:
                out.append(text)
            return
        for item in obj:
            _collect_text(item, out)


def _normalize_lines(lines: List[str]) -> List[str]:
    """Clean and deduplicate line-level OCR text."""
    normalized: List[str] = []
    prev = ""
    for line in lines:
        text = re.sub(r"\s+", " ", line).strip()
        if not text or text == prev:
            continue
        normalized.append(text)
        prev = text
    return normalized


def _strip_references_section(text: str) -> str:
    """Drop references/bibliography section from parsed text."""
    out: List[str] = []
    for line in text.splitlines():
        stripped = line.strip()
        if re.match(r"^#+\s*(references?|bibliography|citations?)\s*$", stripped, re.IGNORECASE):
            break
        if re.match(r"^(references?|bibliography|citations?)\s*$", stripped, re.IGNORECASE):
            break
        out.append(line)
    return "\n".join(out).strip()


def _extract_pdf_with_paddleocrvl(pdf_path: str, output_dir: str, model_dir: Path) -> Tuple[str, Dict[str, Any]]:
    """Render PDF pages, run OCR, and return merged text with metadata."""
    try:
        import fitz  # type: ignore
    except Exception as exc:
        raise ImportError(
            "PyMuPDF is required for PaddleOCR parsing. Install `pymupdf`."
        ) from exc

    pdf = Path(pdf_path)
    out_dir = Path(output_dir)
    image_dir = out_dir / "page_images"
    raw_dir = out_dir / "ocr_raw"
    image_dir.mkdir(parents=True, exist_ok=True)
    raw_dir.mkdir(parents=True, exist_ok=True)

    engine, backend = _create_ocr_engine(model_dir=model_dir)

    page_blocks: List[str] = []
    doc = fitz.open(str(pdf))
    try:
        for page_idx, page in enumerate(doc, start=1):
            image_path = image_dir / f"{pdf.stem}-page-{page_idx:04d}.png"
            page.get_pixmap(dpi=300, alpha=False).save(str(image_path))

            raw = _run_ocr(engine, image_path)
            with open(raw_dir / f"page-{page_idx:04d}.json", "w", encoding="utf-8") as f:
                json.dump(raw, f, ensure_ascii=False, indent=2, default=str)

            lines: List[str] = []
            _collect_text(raw, lines)
            lines = _normalize_lines(lines)

            if not lines:
                fallback = page.get_text("text")
                lines = [x.strip() for x in fallback.splitlines() if x.strip()]

            page_text = "\n".join(lines).strip()
            page_blocks.append(f"## Page {page_idx}\n\n{page_text}")
    finally:
        doc.close()

    merged = "\n\n".join(page_blocks).strip()
    metadata = {
        "backend": backend,
        "model_dir": str(model_dir),
        "pages": len(page_blocks),
        "image_dir": str(image_dir),
        "ocr_raw_dir": str(raw_dir),
    }
    return merged, metadata


def _read_txt_file(path: Path) -> str:
    """Read plain text file with robust fallback encoding handling."""
    try:
        return path.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        return path.read_text(encoding="utf-8", errors="ignore")


def parse_pdf_with_paddleocrvl(state: KnowMatState) -> dict:
    """Parse PDF/TXT and return cleaned paper text."""
    input_path = state.get("pdf_path")
    if not input_path:
        raise ValueError("No input file path provided in state for parse_pdf_with_paddleocrvl node.")

    output_dir = state.get("output_dir", ".")
    source_path = Path(input_path)
    suffix = source_path.suffix.lower()

    if suffix == ".txt":
        parse_output_dir = Path(output_dir) / "txt_parse"
        parse_output_dir.mkdir(parents=True, exist_ok=True)

        raw_text = _read_txt_file(source_path)
        cleaned_text = _strip_references_section(raw_text)
        stem = source_path.stem

        final_md_path = parse_output_dir / f"{stem}_final_output.md"
        with open(final_md_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)
        print(f"Saved txt parsed output to: {final_md_path}")

        meta_path = parse_output_dir / f"{stem}_parse_metadata.json"
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump({"backend": "txt-direct", "source_file": str(source_path)}, f, ensure_ascii=False, indent=2)
        print(f"Saved parser metadata to: {meta_path}")

        return {"paper_text": cleaned_text}

    if suffix != ".pdf":
        raise ValueError(f"Unsupported file type: {source_path.suffix}. Only .pdf and .txt are supported.")

    parse_output_dir = Path(output_dir) / "paddleocrvl_parse"
    parse_output_dir.mkdir(parents=True, exist_ok=True)
    model_dir = _default_model_dir()

    try:
        extracted_text, metadata = _extract_pdf_with_paddleocrvl(str(source_path), str(parse_output_dir), model_dir)
        cleaned_text = _strip_references_section(extracted_text)

        pdf_name = source_path.stem
        final_md_path = parse_output_dir / f"{pdf_name}_final_output.md"
        with open(final_md_path, "w", encoding="utf-8") as f:
            f.write(cleaned_text)
        print(f"Saved final markdown output to: {final_md_path}")

        meta_path = parse_output_dir / f"{pdf_name}_parse_metadata.json"
        with open(meta_path, "w", encoding="utf-8") as f:
            json.dump(metadata, f, ensure_ascii=False, indent=2)
        print(f"Saved parser metadata to: {meta_path}")

        return {"paper_text": cleaned_text, "metadata": metadata}
    except Exception as exc:
        raise RuntimeError(f"Failed to parse PDF with PaddleOCR-VL: {str(exc)}") from exc
