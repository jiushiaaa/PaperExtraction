# -*- coding: utf-8 -*-
"""
PaddleOCR 文档解析预处理模块（PaddleOCR-VL 1.5 / PPStructureV3 自动选择）。

将 PDF 通过 PaddleOCR 解析为结构化 Markdown（表格自动转 Markdown 表格），
再裁剪掉 Abstract / Introduction / References / Acknowledgements 等无关章节，
仅保留 Experimental → Conclusions 之间的正文，最终保存为 .txt 供 LangExtract 使用。

管线选择策略：
  - 默认使用 PaddleOCR-VL 1.5（需 GPU，SOTA 效果最优）
  - 设置环境变量 OCR_ENGINE=structurev3 可切换到 PPStructureV3（CPU/GPU 均可，速度更快）

流程：
  PDF ──► PaddleOCR-VL / PPStructureV3 ──► Markdown ──► 章节裁剪 ──► .txt
"""

from __future__ import annotations

import logging
import os
import re
import tempfile
import threading
from pathlib import Path

log = logging.getLogger(__name__)

os.environ.setdefault("PADDLE_PDX_DISABLE_MODEL_SOURCE_CHECK", "True")

# ------------------------------------------------------------------
# 章节匹配正则
# ------------------------------------------------------------------

_BODY_START = re.compile(
    r"(?i)^[\s#]*(?:"
    r"2[\.\s]+(?:Experimental|Materials|Methods)"
    r"|Experimental\s*(?:Procedure|Section|Details|Methods|Setup)?"
    r"|Materials?\s*and\s*Methods?"
    r"|Methodology"
    r"|Experimental\s*and\s*(?:Computational\s*)?Methods?"
    r"|实验(?:部分|方法|过程|内容)?"
    r"|材料与方法"
    r")\s*$",
    re.MULTILINE,
)

_BACK_SECTIONS = re.compile(
    r"(?i)^[\s#]*(?:"
    r"Acknowledg(?:e)?ments?"
    r"|Declaration\s*of\s*(?:Competing\s*)?Interest"
    r"|Conflict\s*of\s*[Ii]nterest"
    r"|CRediT\s*[Aa]uthorship"
    r"|References"
    r"|REFERENCES"
    r"|Data\s*[Aa]vailability"
    r"|Supplementary\s*(?:[Mm]aterial|[Ii]nformation)"
    r"|Appendix"
    r"|致谢"
    r"|参考文献"
    r")\s*$",
    re.MULTILINE,
)

# ------------------------------------------------------------------
# PaddleOCR 管线单例
# ------------------------------------------------------------------

_pipeline = None
_pipeline_type = None


def _get_pipeline():
    """
    延迟初始化 PaddleOCR 管线（首次调用会下载模型）。

    默认使用 PaddleOCR-VL 1.5（GPU，效果最优）。
    设置 OCR_ENGINE=structurev3 切换到 PPStructureV3（CPU 友好）。
    """
    global _pipeline, _pipeline_type
    if _pipeline is not None:
        return _pipeline

    engine = os.environ.get("OCR_ENGINE", "vl").lower().strip()

    try:
        if engine == "structurev3":
            from paddleocr import PPStructureV3
            log.info("正在初始化 PPStructureV3（CPU 友好，首次会下载模型）…")
            _pipeline = PPStructureV3()
            _pipeline_type = "StructureV3"
        else:
            from paddleocr import PaddleOCRVL
            log.info("正在初始化 PaddleOCR-VL 1.5（GPU 推荐，首次会下载模型）…")
            _pipeline = PaddleOCRVL()
            _pipeline_type = "VL"
    except ImportError as e:
        raise RuntimeError(
            "PaddleOCR 未安装。请先执行：\n"
            "  pip install paddlepaddle-gpu  # 或 CPU: pip install paddlepaddle\n"
            "  pip install \"paddleocr[doc-parser]\"\n"
            "详见 https://github.com/PaddlePaddle/PaddleOCR"
        ) from e

    log.info("PaddleOCR 管线初始化完成 (type=%s)", _pipeline_type)
    return _pipeline


# ------------------------------------------------------------------
# 核心函数
# ------------------------------------------------------------------

def _collect_markdown(output) -> str:
    """从 PaddleOCR 结果对象中提取 Markdown 文本。"""
    parts: list[str] = []
    for res in output:
        md = getattr(res, "markdown", None)
        if isinstance(md, dict) and "text" in md:
            text = md["text"]
            if isinstance(text, str) and text.strip():
                parts.append(text)
                continue
        if hasattr(res, "save_to_markdown"):
            with tempfile.TemporaryDirectory() as tmpdir:
                res.save_to_markdown(save_path=tmpdir)
                md_files = sorted(Path(tmpdir).rglob("*.md"))
                for f in md_files:
                    if f.stat().st_size > 0:
                        parts.append(f.read_text(encoding="utf-8"))
    return "\n\n".join(parts)


def _ocr_pdf_via_images(pdf_path: Path, pipeline) -> str:
    """回退方案：将 PDF 逐页转图片后处理。"""
    import pymupdf

    doc = pymupdf.open(pdf_path)
    all_parts: list[str] = []

    with tempfile.TemporaryDirectory() as tmpdir:
        for page_idx in range(len(doc)):
            page = doc[page_idx]
            pix = page.get_pixmap(dpi=200)
            img_path = Path(tmpdir) / f"page_{page_idx:03d}.png"
            pix.save(str(img_path))

            try:
                output = pipeline.predict(str(img_path))
                text = _collect_markdown(output)
                if text.strip():
                    all_parts.append(text)
            except Exception as e:
                log.warning("  第 %d 页 OCR 失败: %s", page_idx + 1, e)

    doc.close()
    return "\n\n".join(all_parts)


def _ocr_progress_logger(stop_event: threading.Event, pdf_name: str = "") -> None:
    """后台线程：每 60 秒打印一次，避免用户误以为程序卡死。pdf_name 用于提示当前正在处理哪一篇。"""
    count = 0
    while not stop_event.wait(timeout=60):
        count += 1
        if pdf_name:
            msg = "  … OCR 仍在处理中（当前: %s，已等待约 %d 分钟）" % (pdf_name, count)
        else:
            msg = "  … OCR 仍在处理中（已等待约 %d 分钟，大 PDF 首次可能较久）" % count
        print(msg, flush=True)
        log.info(msg)


def ocr_pdf_to_text(pdf_path: Path) -> str:
    """
    将 PDF 解析为 Markdown 文本。

    自动处理：
      - 文本段落识别与排序
      - 表格 → Markdown 表格
      - 公式识别
      - 布局分析（PPStructureV3）
    """
    # 先打提示再加载管线，否则会被 Paddle 大量加载日志淹没
    pdf_name = pdf_path.name
    msg_start = "  [OCR] 正在加载 PaddleOCR 管线并准备解析 PDF（首次会加载模型，请勿中断）…"
    print(msg_start, flush=True)
    log.info(msg_start)
    pipeline = _get_pipeline()

    try:
        msg_parse = "  [OCR] 开始解析: %s（大文件可能需要数分钟），请勿中断…" % pdf_name
        print(msg_parse, flush=True)
        log.info(msg_parse)
        stop_event = threading.Event()
        progress_thread = threading.Thread(
            target=_ocr_progress_logger, args=(stop_event, pdf_name), daemon=True
        )
        progress_thread.start()
        try:
            output = pipeline.predict(str(pdf_path))
            pages_res = list(output)
        finally:
            stop_event.set()
        msg_done = "  [OCR] 完成: %s，共 %d 页" % (pdf_name, len(pages_res))
        print(msg_done, flush=True)
        log.info(msg_done)

        if _pipeline_type == "VL" and len(pages_res) > 1:
            restructured = pipeline.restructure_pages(
                pages_res,
                merge_tables=True,
                relevel_titles=True,
                concatenate_pages=True,
            )
            text = _collect_markdown(restructured)
        else:
            text = _collect_markdown(pages_res)

        if text.strip():
            return text
    except Exception as e:
        log.warning("PaddleOCR 直接解析 PDF 失败 (%s)，回退逐页转图处理", e)

    return _ocr_pdf_via_images(pdf_path, pipeline)


def remove_unwanted_sections(text: str) -> str:
    """
    移除论文中无关章节，仅保留 Experimental → Conclusions 核心正文。

    裁剪策略：
      1. 前端：找 "Experimental / Materials and Methods" 等标题，从此处开始保留
         （丢弃 Title / Abstract / Introduction）。
      2. 后端：在文本后 30% 区域找 References / Acknowledgements 等标题，截断。
      3. 若裁剪后文本过短（< 200 字符），回退使用原文。
    """
    if not text or len(text) < 200:
        return text

    body_start = 0
    m_front = _BODY_START.search(text)
    if m_front:
        body_start = m_front.start()
        log.info(
            "  前端裁剪: 从 '%s' (pos %d) 开始保留",
            m_front.group().strip()[:60], body_start,
        )

    body_end = len(text)
    search_from = max(body_start, int(len(text) * 0.7))
    m_back = _BACK_SECTIONS.search(text, pos=search_from)
    if m_back:
        body_end = m_back.start()
        log.info(
            "  后端裁剪: 在 '%s' (pos %d) 截断",
            m_back.group().strip()[:60], body_end,
        )

    result = text[body_start:body_end].strip()
    if len(result) < 200 and len(text) > 200:
        log.warning(
            "  裁剪后文本仅 %d 字符，回退使用原文 (%d 字符)", len(result), len(text)
        )
        return text

    return result


def preprocess_pdf(
    pdf_path: Path,
    output_dir: Path | None = None,
) -> Path:
    """
    完整预处理流程：PDF → PaddleOCR → 章节裁剪 → .txt。

    Args:
        pdf_path:   输入 PDF 路径。
        output_dir: .txt 输出目录，默认与 PDF 同目录。

    Returns:
        生成的 .txt 文件路径。
    """
    if output_dir is None:
        output_dir = pdf_path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    txt_path = output_dir / (pdf_path.stem + ".txt")

    log.info("OCR 预处理: %s", pdf_path.name)

    raw_md = ocr_pdf_to_text(pdf_path)
    log.info("  PaddleOCR 输出: %d 字符", len(raw_md))

    cleaned = remove_unwanted_sections(raw_md)
    ratio = (1 - len(cleaned) / max(len(raw_md), 1)) * 100
    log.info(
        "  章节裁剪后: %d 字符 (裁剪 %.0f%%)", len(cleaned), ratio
    )

    txt_path.write_text(cleaned, encoding="utf-8")
    log.info("  已保存: %s", txt_path)
    return txt_path


def preprocess_all(
    pdf_dir: Path,
    output_dir: Path | None = None,
    force: bool = False,
    max_count: int = 0,
) -> list[Path]:
    """
    批量预处理：对目录下 PDF 执行 OCR + 章节裁剪。

    Args:
        pdf_dir:    PDF 所在目录。
        output_dir: .txt 输出目录，默认与 PDF 同目录。
        force:      True 时强制重新 OCR（即使 .txt 已存在）。
        max_count:   最多处理篇数，0 表示不限制（全部处理）。

    Returns:
        生成的 .txt 文件路径列表。
    """
    if output_dir is None:
        output_dir = pdf_dir
    pdfs = sorted(pdf_dir.glob("*.pdf"))
    if not pdfs:
        log.warning("未在 %s 下找到 PDF", pdf_dir)
        return []
    if max_count > 0:
        pdfs = pdfs[:max_count]
        log.info("仅预处理前 %d 篇 PDF", len(pdfs))

    results: list[Path] = []
    for i, pdf in enumerate(pdfs, 1):
        txt_path = output_dir / (pdf.stem + ".txt")
        if txt_path.is_file() and not force:
            msg_skip = "  [%d/%d] 跳过（已有）: %s" % (i, len(pdfs), txt_path.name)
            print(msg_skip, flush=True)
            log.info("[%d/%d] 跳过（已有）: %s", i, len(pdfs), txt_path.name)
            results.append(txt_path)
            continue

        msg_doing = "  [%d/%d] 正在处理: %s" % (i, len(pdfs), pdf.name)
        print(msg_doing, flush=True)
        log.info("[%d/%d] 处理: %s", i, len(pdfs), pdf.name)
        try:
            path = preprocess_pdf(pdf, output_dir=output_dir)
            results.append(path)
        except Exception as e:
            log.exception("  预处理失败: %s", e)

    return results
