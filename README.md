# 高熵合金论文结构化抽取 Pipeline

从高熵合金（HEA）领域学术 PDF 中抽取「成分–工艺–性能」结构化数据，输出 JSONL，供下游机器学习或知识库使用。

采用 **PaddleOCR-VL 1.5 + LangExtract** 双引擎架构：先用 [PaddleOCR-VL 1.5](https://github.com/PaddlePaddle/PaddleOCR)（本地部署）将 PDF 解析为高质量 Markdown 文本（表格自动转 Markdown 表格），裁剪掉 Abstract / Introduction / References 等无关章节后保存为 `.txt`；再由 [LangExtract](https://github.com/google/langextract) 对清洗后的文本执行结构化抽取。默认按 **OpenAI 兼容接口** 调用 LLM，支持 `.env` 自定义 API Key / Base URL / Model。

---

## 功能概览

| 功能 | 说明 |
|------|------|
| **PaddleOCR-VL 预处理** | 本地部署 PaddleOCR-VL 1.5（SOTA 文档解析），PDF → Markdown（表格/公式/图表自动识别），裁剪 Abstract / Introduction / References，输出干净 `.txt`，大幅减少 LLM 幻觉 |
| **开放模型接入** | 支持任意 OpenAI 兼容 API（可直传 model_id）；Gemini 单独保留 |
| **章节裁剪** | 前端裁剪 Abstract / Introduction；后端截断 Acknowledgements / References，仅保留 Experimental → Conclusions 核心正文 |
| **分块抽取** | 按字符数分块 + 重叠，单块失败可切半重试；单块超时（默认 240s）跳过，不拖死整程 |
| **结构化输出** | 扁平 Extraction → 按 `material_id` 聚合为 MaterialEntity → 转目标 JSON 模板（`Composition_Info` / `Process_Info` / `Properties_Info`）写入 JSONL |
| **去噪过滤** | 在 Schema 中增加 `role ∈ {Target, Reference, Other}`，仅保留 `role == 'Target'` 的材料记录（本文作者亲自制备和研究的材料），自动跳过 316L、Ti64 等对比/引用材料。 |

---

## 项目结构

```
AM/
├── main.py              # 入口：argparse、OCR 预处理、分块、lx.extract、聚合、写 JSONL
├── ocr_preprocess.py    # PaddleOCR-VL 1.5 预处理（PDF→Markdown→章节裁剪→.txt）
├── config_manager.py    # 模型工厂：环境变量驱动（OpenAI 兼容 + Gemini）
├── openai_compatible_provider.py  # 本地 OpenAI provider 扩展（支持 extra_body 等）
├── pdf_utils.py         # PDF 提文本（PyMuPDF 备选）、clean_and_truncate_text、chunk_text
├── schemas.py           # Pydantic 模型 + Prompt + 聚合 + 转目标 JSON
├── .env                 # 本地 API Key + 模型配置
├── AMpdf/               # 待处理 PDF（及 OCR 生成的 .txt）
├── output/              # 输出 he_data_{model}.jsonl
├── requirements.txt     # 依赖
└── README.md            # 本文件
```

可选：仓库内可含 `langextract-main/` 作为 LangExtract 子模块或本地参考，运行时不依赖该目录。

### 处理流程

```
PDF ──► PaddleOCR-VL 1.5（本地）──► Markdown（表格/公式/图表自动识别）
    ──► 裁剪 Abstract / Introduction / References ──► .txt
    ──► 手动分块 ──► LangExtract 逐块抽取 ──► 聚合 MaterialEntity ──► JSONL
```

---

## 环境要求

- **Python** ≥ 3.10
- 建议使用虚拟环境：`python -m venv .venv` 后激活再安装依赖

---

## 安装

```bash
git clone https://github.com/jiushiaaa/langextract-AM.git
cd AM

# 1. 安装 PaddlePaddle（PaddleOCR 底层框架）
#    GPU 版（推荐，需匹配 CUDA 版本，详见 https://www.paddlepaddle.org.cn/install/quick）：
pip install paddlepaddle-gpu
#    CPU 版：
# pip install paddlepaddle

# 2. 安装项目依赖（含 PaddleOCR + LangExtract）
pip install -r requirements.txt
```

---

## 配置

在项目根目录创建 `.env` 文件：

```env
# OpenAI 兼容接口（推荐；支持 python-dotenv 的 export 写法）
export LLM_API_KEY="bce-v3/xxx"
export LLM_BASE_URL="https://qianfan.bj.baidubce.com/v2"
export LLM_MODEL="ep_3nr55ube9_ernie"

# 常用生成参数
export LLM_TEMPERATURE="0.1"
export LLM_MAX_OUTPUT_TOKENS="8192"

# 显式关闭深度思考（会注入 extra_body.enable_thinking=false）
export LLM_ENABLE_THINKING="false"

# 思考预算（仅在 enable_thinking=true 时有意义，范围 100~60000）
# export LLM_THINKING_BUDGET="800"

# 额外请求体（可选；JSON 对象）
# export LLM_EXTRA_BODY='{"enable_thinking": false, "foo": "bar"}'

# 高级透传（可选；直接合并到 provider_kwargs）
# export LLM_OPENAI_KWARGS='{"top_p":0.9,"response_format":{"type":"json_object"}}'

# 部分 OpenAI 兼容网关不支持 response_format，可关闭强制 JSON 模式（可选）
# export LLM_DISABLE_RESPONSE_FORMAT="true"

# 调试原始输出（可选）
# export LLM_DEBUG_RAW="true"

# 单块超时秒数（可选，默认 240）
# export CHUNK_TIMEOUT_SECONDS="300"

# 请求重试（可选，默认重试 2 次，指数退避）
# export LLM_MAX_RETRIES="2"
# export LLM_RETRY_BACKOFF_SECONDS="1.5"

# 实体落地校验（默认 true：实体名/化学式需能在原文命中，减少幻觉）
# export STRICT_ENTITY_GROUNDING="true"

# Gemini（仅在 --model gemini 时）
# export GOOGLE_API_KEY="你的Gemini密钥"
```

说明：
- 默认 `python main.py` 会走 `--model env`，因此需要先配置 `LLM_MODEL`。
- OpenAI 兼容模式下必须配置：`LLM_API_KEY`、`LLM_BASE_URL`、`LLM_MODEL`。
- 可通过 `LLM_EXTRA_BODY` 传任何网关私有字段；`LLM_ENABLE_THINKING=false` 会自动写入 `extra_body.enable_thinking=false`。
- ERNIE 5.0 思考模型建议：`LLM_ENABLE_THINKING=true/false` + `LLM_THINKING_BUDGET`（100~60000）。

---

## 使用方法

### 完整流程（推荐：PaddleOCR + LangExtract）

```bash
# 默认：PaddleOCR-VL 预处理 + LangExtract 抽取
# 首次运行会自动下载 PaddleOCR-VL 模型
python main.py

# 限制篇数、分块大小
python main.py --max 2 --chunk 12000
```

### 仅预处理（只跑 PaddleOCR，不跑 LangExtract）

```bash
# 批量将 AMpdf/ 下的 PDF 转为 .txt（适合先检查 OCR 质量）
python main.py --preprocess-only

# 强制重新 OCR（即使 .txt 已存在）
python main.py --preprocess-only --force-ocr
```

### CPU 环境切换 PPStructureV3

```bash
# 无 GPU 时，设置 OCR_ENGINE 使用 PPStructureV3（CPU 可跑）
export OCR_ENGINE="structurev3"
python main.py --preprocess-only
```

### 跳过 PaddleOCR（旧模式，直接 PyMuPDF 提文本）

```bash
python main.py --no-ocr
```

### 其他示例

```bash
# 使用 Gemini
python main.py --model gemini

# 直接传 OpenAI 兼容 model_id
python main.py --model ep_3nr55ube9_ernie

# 强制重新 OCR + LangExtract 全流程
python main.py --force-ocr --max 2 --chunk 12000
```

### ERNIE 5.0 思考参数示例

```env
export LLM_MODEL="ernie-5.0-thinking-preview"

# 关闭思考（推荐抽取任务）
export LLM_ENABLE_THINKING="false"

# 开启思考 + 限制思考 token
# export LLM_ENABLE_THINKING="true"
# export LLM_THINKING_BUDGET="800"
```

### 参数说明

| 参数 | 默认 | 说明 |
|------|------|------|
| `--model` | `env` | 取值：`gemini` / `env` / 任意 OpenAI 兼容 `model_id` |
| `--max` | 0 | 最多处理 PDF 数量，0 表示全部 |
| `--chunk` | 6000 | 分块大小（字符），单块失败会切半重试 |
| `--workers` | 1 | 分块并发数，1 为串行（便于排查卡住） |
| `--no-ocr` | — | 跳过 PaddleOCR 预处理，直接用 PyMuPDF 提文本 |
| `--force-ocr` | — | 强制重新运行 PaddleOCR（即使 .txt 已存在） |
| `--preprocess-only` | — | 仅运行 PaddleOCR 预处理生成 .txt，不执行抽取 |

---

## 输出

- 路径：`output/he_data_{model}.jsonl`
- 格式：每行一条 JSON，核心结构为：
  - `Composition_Info`：成分信息（`Mat_ID`、`Alloy_Name_Raw`、`Formula_Normalized`、`Composition_JSON` 等）；
  - `Process_Info`：工艺与微观组织信息（`Process_Category`、`Process_Text_For_AI`、`Key_Params_JSON`、`Microstructure_Text_For_AI` 等）；
  - `Properties_Info`：力学性能列表（每条含 `Test_ID`、`Test_Temperature_K`、`Property_Type`、`Property_Value`、`Property_Unit`）。
- 其中 `Composition_JSON` 与 `Key_Params_JSON` 为 **字符串格式的 JSON**（由 `json.dumps(..., ensure_ascii=False)` 生成），满足甲方对“转义 JSON 字符串”的要求。
- 顶层还包含 `_source_pdf`（溯源 PDF 文件名）与 `role` 字段，方便后续再次筛选/统计。
- 每次运行会**覆盖**该模型对应的 JSONL 文件；多篇 PDF 时按篇追加写入（线程安全）。

---

## 常见问题与优化方向

1. **403 访问过于频繁**  
   星河社区 API 限流：保持 `--workers 1` 或改为 2，并适当增大 `--chunk` 减少请求次数。

2. **某块一直卡在 “HTTP 200 OK” 之后**  
   已加单块超时（默认 240 秒），超时会自动跳过该块并继续下一块；可在 `main.py` 中调整 `CHUNK_TIMEOUT`。思考模型推理慢，建议保持 240 或更大。

3. **JSON 解析失败（Expecting value: line 1 column 1 / Unterminated string）**  
   单块会先切半重试；若仍失败则跳过该块。**思考模型** 常在 JSON 前输出推理内容，易触发 “Expecting value”，属已知现象，可改用其他模型或增大 chunk 减少请求次数。

4. **Connection error / Server disconnected**  
   网络或服务端断开时，该块会跳过并打简短日志，不打断整程；可稍后重跑或换网络。

5. **可优化方向**  
   - 增加更多 Few-shot 示例或细化 `schemas.py` 中 Field 的 description，提升抽取质量。  
   - 对星河社区内的模型做简单请求频率限制（如 token bucket），避免 403。  
   - 支持从本地 `langextract-main` 安装开发版：`pip install -e ./langextract-main`。  
   - 输出层增加去重、与已有 JSONL 的 merge 策略。  
   - 将 `CHUNK_TIMEOUT`、`MIN_CHUNK_RETRY` 等做成命令行或配置文件项。

---

## 依赖（见 requirements.txt）

- `paddlepaddle` / `paddlepaddle-gpu`：PaddleOCR 底层框架（需单独安装）
- `paddleocr[doc-parser]`：PaddleOCR-VL 1.5 文档解析
- `langextract`：结构化抽取
- `pydantic`：数据模型与校验
- `pymupdf`：PDF 文本提取（PyMuPDF，`--no-ocr` 时使用）
- `pdfplumber`：PDF 提取备选
- `python-dotenv`：加载 `.env`

---
