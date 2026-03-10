"""
Entry point for running the KnowMat 2.0 pipeline via the command line.

Usage
-----
::

    python -m knowmat --input-folder path/to/files [--output-dir out] [--max-runs 1]

This will parse all supported files (PDF/TXT) in the given folder, run the
agentic extraction workflow and write the results to the specified output
directory. Each file is processed
sequentially. The final JSON, rationale and intermediate run records are saved
separately for each paper.
"""

import argparse
import json
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from knowmat.nodes.paddleocrvl_parse_pdf import parse_pdf_with_paddleocrvl
from knowmat.orchestrator import run
from knowmat.app_config import settings

# 进度打印间隔（秒）
_PROGRESS_INTERVAL_SEC = 60


def _run_with_elapsed_progress(description: str, current_file: str, fn, *args, **kwargs):
    """在子线程中执行 fn，主线程每 _PROGRESS_INTERVAL_SEC 秒打印一次「仍在处理中，已等待约 N 分钟」。"""
    result_holder: list = []
    exc_holder: list = []

    def target():
        try:
            result_holder.append(fn(*args, **kwargs))
        except Exception as e:
            exc_holder.append(e)

    th = threading.Thread(target=target, daemon=False)
    th.start()
    start = time.time()
    while th.is_alive():
        time.sleep(_PROGRESS_INTERVAL_SEC)
        if not th.is_alive():
            break
        mins = int((time.time() - start) / 60)
        print(f"... {description} 仍在处理中 (当前: {current_file}, 已等待约 {mins} 分钟)")
    th.join()
    if exc_holder:
        raise exc_holder[0]
    return result_holder[0] if result_holder else None


def _prepare_txt_inputs(input_folder: Path, pdf_files: list[Path], existing_txt_files: list[Path]) -> list[Path]:
    """Ensure each PDF has a corresponding TXT sidecar, returning all TXT paths.

    - If a TXT with the same stem as a PDF already exists, it is reused directly.
    - If no TXT exists for a PDF, PaddleOCR-VL is invoked to create one, and the
      cleaned text is saved as <stem>.txt in the same folder.
    - Only TXT files are returned for downstream processing so the main pipeline
      always runs on plain text inputs.
    """
    txt_by_stem = {p.stem: p for p in existing_txt_files}

    if pdf_files:
        ocr_root = input_folder / "_ocr_cache"
        for pdf in pdf_files:
            stem = pdf.stem
            if stem in txt_by_stem:
                continue

            print(f"\nNo TXT found for {pdf.name}. Running OCR to create {stem}.txt ...")
            parse_output_dir = ocr_root / stem
            parse_output_dir.mkdir(parents=True, exist_ok=True)

            state = {
                "pdf_path": str(pdf),
                "output_dir": str(parse_output_dir),
            }

            try:
                result = _run_with_elapsed_progress(
                    "OCR", pdf.name, parse_pdf_with_paddleocrvl, state
                )  # type: ignore[arg-type]
            except Exception as exc:  # pragma: no cover - defensive
                print(f"[ERROR] Failed to OCR {pdf.name}: {exc}")
                continue

            text = result.get("paper_text") if isinstance(result, dict) else None
            if not text:
                print(f"[ERROR] OCR returned no text for {pdf.name}, skipping.")
                continue

            txt_path = input_folder / f"{stem}.txt"
            txt_path.write_text(text, encoding="utf-8")
            txt_by_stem[stem] = txt_path
            print(f"Saved OCR text to: {txt_path}")
            pages = result.get("metadata", {}).get("pages") if isinstance(result, dict) else None
            if pages is not None:
                print(f"[OCR] 完成; {pdf.name}: 共{pages}页")

    return sorted(txt_by_stem.values(), key=lambda x: x.name.lower())


def main(argv: list[str] | None = None) -> None:
    parser = argparse.ArgumentParser(description="Run the KnowMat 2.0 extraction pipeline for PDF/TXT inputs.")
    parser.add_argument("--input-folder", default=None, help="Path to the folder containing PDF/TXT files to process.")
    parser.add_argument("--pdf-folder", default=None, help="Legacy alias of --input-folder.")
    parser.add_argument("--output-dir", default=None, help="Directory to write outputs to (default: ./knowmat_output).")
    parser.add_argument("--max-runs", type=int, default=1, help="Maximum extraction/evaluation cycles per paper.")
    parser.add_argument("--workers", type=int, default=1, help="Number of files to process concurrently.")
    parser.add_argument("--full-pipeline", action="store_true", help="Enable full multi-stage pipeline.")
    parser.add_argument(
        "--enable-property-standardization",
        action="store_true",
        help="Enable optional property standardization (slower, more LLM calls).",
    )
    parser.add_argument(
        "--force-rerun",
        action="store_true",
        help="Re-run all files even if extraction outputs already exist.",
    )
    parser.add_argument(
        "--only",
        nargs="+",
        default=None,
        help="Only process files whose stem or full name matches any of the given values.",
    )
    
    # Per-agent model overrides
    parser.add_argument("--subfield-model", default=None, help="Model for subfield detection agent.")
    parser.add_argument("--extraction-model", default=None, help="Model for extraction agent.")
    parser.add_argument("--evaluation-model", default=None, help="Model for evaluation agent.")
    parser.add_argument("--manager-model", default=None, help="Model for validation agent (Stage 2: hallucination correction).")
    parser.add_argument("--flagging-model", default=None, help="Model for flagging/quality assessment agent.")
    
    args = parser.parse_args(argv)
    
    # 优先级：CLI (--input-folder / --pdf-folder) > 环境变量 KNOWMAT2_INPUT_DIR > 默认 "data/raw"
    input_folder_arg = args.input_folder or args.pdf_folder or settings.input_dir
    input_folder = Path(input_folder_arg)
    if not input_folder.exists():
        # 若目录不存在，则创建空目录并提示用户
        print(f"Input folder not found, creating: {input_folder}")
        input_folder.mkdir(parents=True, exist_ok=True)
    
    if not input_folder.is_dir():
        print(f"Error: Path is not a directory: {input_folder}")
        return

    pdf_files = sorted(
        [p for p in input_folder.iterdir() if p.is_file() and p.suffix.lower() == ".pdf"],
        key=lambda x: x.name.lower(),
    )
    existing_txt_files = sorted(
        [p for p in input_folder.iterdir() if p.is_file() and p.suffix.lower() == ".txt"],
        key=lambda x: x.name.lower(),
    )

    if not pdf_files and not existing_txt_files:
        print(f"Error: No supported files (.pdf/.txt) found in: {input_folder}")
        print("Please place your PDF/TXT files into this folder or specify --input-folder explicitly.")
        return

    processing_files = _prepare_txt_inputs(input_folder, pdf_files, existing_txt_files)
    if not processing_files:
        print(f"Error: No TXT files available for processing in: {input_folder}")
        return

    # 如果指定了 --only，则只保留匹配给定文件名或 stem 的文件
    if args.only:
        requested = set(args.only)
        before = len(processing_files)
        processing_files = [
            p for p in processing_files
            if p.stem in requested or p.name in requested
        ]
        if not processing_files:
            print(f"Error: No TXT files matched --only filter in: {input_folder}")
            print(f"Requested: {', '.join(sorted(requested))}")
            return
        else:
            print(f"\nFiltered files with --only ({before} -> {len(processing_files)} to process)")

    print(f"\nFound {len(processing_files)} TXT files to process")
    print("=" * 60)
    
    # 计算当前运行实际使用的输出根目录（CLI > 配置默认值）
    root_output_dir = Path(args.output_dir or settings.output_dir)

    def _process_one(file_path: Path) -> dict:
        try:
            # 如果该论文已经有成功的抽取结果，且未显式要求重跑，则直接跳过
            base_name = file_path.stem
            paper_output_dir = root_output_dir / base_name
            extraction_path = paper_output_dir / f"{base_name}_extraction.json"
            if extraction_path.exists() and not args.force_rerun:
                try:
                    data = json.loads(extraction_path.read_text(encoding="utf-8"))
                    materials = data.get("Materials", [])
                    compositions_count = len(materials)
                except Exception:
                    compositions_count = 0
                print(f"Skipping {file_path.name}: existing extraction found at {extraction_path}")
                return {
                    "file": file_path.name,
                    "success": True,
                    "flag": False,
                    "compositions": compositions_count,
                    "output_dir": str(paper_output_dir),
                    "skipped": True,
                }

            result = _run_with_elapsed_progress(
                "大模型解析",
                file_path.name,
                run,
                pdf_path=str(file_path),
                output_dir=args.output_dir,
                model_name=None,  # Use defaults from settings
                max_runs=args.max_runs,
                subfield_model=args.subfield_model,
                extraction_model=args.extraction_model,
                evaluation_model=args.evaluation_model,
                manager_model=args.manager_model,
                flagging_model=args.flagging_model,
                full_pipeline=args.full_pipeline,
                enable_property_standardization=args.enable_property_standardization,
            )

            materials = result.get("final_data", {}).get("Materials", [])
            compositions_count = len(materials)
            return {
                "file": file_path.name,
                "success": True,
                "flag": result.get("flag"),
                "compositions": compositions_count,
                "output_dir": result.get("output_dir"),
                "skipped": False,
            }
        except Exception as e:
            return {"file": file_path.name, "success": False, "error": str(e)}

    results_summary = []
    workers = max(1, args.workers)
    if workers == 1:
        for i, file_path in enumerate(processing_files, 1):
            print(f"\n{'='*60}")
            print(f"Processing file {i}/{len(processing_files)}: {file_path.name}")
            print(f"{'='*60}\n")
            summary = _process_one(file_path)
            results_summary.append(summary)
            if summary["success"]:
                if summary.get("skipped"):
                    print(f"\nSkipped (already processed): {file_path.name}")
                    print(f"   Output: {summary.get('output_dir')}")
                    print(f"   Materials: {summary.get('compositions', 0)}")
                else:
                    flag_str = "[FLAGGED]" if summary.get("flag") else "[OK]"
                    print(f"\n[大模型解析] 完成; {file_path.name}")
                    print(f"Finished extraction: {file_path.name}")
                    print(f"   Status: {flag_str}")
                    print(f"   Output: {summary.get('output_dir')}")
                    print(f"   Materials: {summary.get('compositions', 0)}")
            else:
                print(f"\nError processing {file_path.name}: {summary.get('error')}")
    else:
        print(f"Running with {workers} workers...")
        with ThreadPoolExecutor(max_workers=workers) as pool:
            fut_map = {pool.submit(_process_one, p): p for p in processing_files}
            for fut in as_completed(fut_map):
                summary = fut.result()
                results_summary.append(summary)
                if summary["success"]:
                    if summary.get("skipped"):
                        print(f"[SKIPPED] {summary['file']}: {summary.get('compositions', 0)} materials (already processed)")
                    else:
                        flag_str = "[FLAGGED]" if summary.get("flag") else "[OK]"
                        print(f"[大模型解析] 完成; {summary['file']}")
                        print(f"{flag_str} {summary['file']}: {summary.get('compositions', 0)} materials")
                else:
                    print(f"[ERROR] {summary['file']}: {summary.get('error')}")
    
    # Print final summary
    print(f"\n{'='*60}")
    print("PROCESSING SUMMARY")
    print(f"{'='*60}\n")
    
    successful = sum(1 for r in results_summary if r['success'])
    failed = len(results_summary) - successful
    
    print(f"Total files: {len(results_summary)}")
    print(f"Successful: {successful}")
    print(f"Failed: {failed}")
    
    if successful > 0:
        flagged = sum(1 for r in results_summary if r['success'] and r.get('flag'))
        print(f"Flagged for review: {flagged}")
        total_compositions = sum(r.get('compositions', 0) for r in results_summary if r['success'])
        print(f"Total materials: {total_compositions}")
    
    print(f"\n{'='*60}\n")
    
    # Print individual results
    for r in results_summary:
        if r['success']:
            if r.get("skipped"):
                print(f"[SKIPPED] {r['file']}: {r.get('compositions', 0)} materials (already processed)")
            else:
                flag_icon = "[FLAGGED]" if r['flag'] else "[OK]"
                print(f"{flag_icon} {r['file']}: {r['compositions']} materials")
        else:
            print(f"[ERROR] {r['file']}: {r.get('error', 'Unknown error')}")


if __name__ == "__main__":  # pragma: no cover
    main()
