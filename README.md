# **KnowMat**：用于材料科学数据抽取的 Agentic 流水线

![KnowMat-logo](docs/_static/KnowMat-logo.jpg)

*图：KnowMat Agentic 流水线示意图，用于从科学文献中抽取结构化材料数据。*

---

## 概述

**KnowMat** 是一个先进的、AI 驱动的 Agentic 流水线，可将非结构化科学文献（`.pdf` / `.txt`）自动抽取为结构化、机器可读的材料科学数据。项目基于 **LangGraph**，并可对接 **OpenAI 兼容的 LLM API**（包括 ERNIE/Qianfan），通过多个智能代理协同完成论文解析、成分抽取、工艺条件抽取、表征信息抽取和材料性能抽取。

### 核心能力

- **科研级批处理**：可批量处理整个目录中的 PDF/TXT 文件
- **高准确度**：多代理架构，支持最多 3 轮抽取/评估迭代优化
- **高级 PDF 解析**：使用 **PaddleOCR-VL** 进行 OCR 解析
- **两阶段校验**：规则聚合 + LLM 幻觉修正
- **属性标准化**：自动将属性名称映射为标准形式
- **质量保障**：置信度打分、人工复核标记与复核指南
- **面向机器学习**：输出结构化 JSON，便于入库和建模

---

## 关键特性

### 🤖 多代理架构

- **Parser Agent**：基于 PaddleOCR-VL 的 PDF 解析
  - 将 PDF 页面转图片并逐页 OCR
  - 保存页面图片和 OCR 原始结果，便于调试
  - 生成用于后续抽取的清洗文本
- **Subfield Detection Agent**：识别论文类型（实验/计算/机器学习）并动态调整提示词
- **Extraction Agent**：基于 TrustCall 的结构化数据抽取
- **Evaluation Agent**：抽取质量评估与置信度评分（最多 3 轮）
- **Two-Stage Manager**：
  - **Stage 1（Aggregation）**：快速规则化合并多轮结果
  - **Stage 2（Validation）**：LLM 幻觉检测与修正
- **Flagging Agent**：最终质量评估与人工复核建议

### 📊 数据抽取范围

- 材料成分（元素、化学计量、归一化配方）
- 工艺条件（温度、压力、气氛、时间）
- 表征方法与结果
- 材料性能（机器学习友好格式）：
  - 精确值、区间、上下界（`>`、`<`、`≥`、`≤`）
  - 数值抽取（并正确处理定性属性）
  - 数值类型：`exact`、`lower_bound`、`upper_bound`、`range`、`qualitative`

### 🔬 属性标准化

- 使用配置的 LLM 将属性名称自动映射为标准形式
- 支持符号、缩写和领域术语

### 🛡️ 质量保障

- 每轮抽取均有置信度评分
- 基于评估反馈的幻觉检测
- 人工复核标记机制
- 详细推理说明与复核指南

### ⚡ 工程化能力

- 支持整目录批处理
- 每篇论文独立输出目录
- 完整 JSON + 可读分析报告 + 多轮记录
- 支持 LangSmith tracing 调试
- 支持按代理单独配置模型（成本/质量平衡）
- **回归测试工具**：自动化 AI vs Ground Truth 对比，量化关键指标

---

## 输出目录结构

每篇论文会生成一个独立目录：

```text
data/processed/
└── <PaperName>/
    ├── <PaperName>_extraction.json          # 最终结构化结果
    ├── <PaperName>_analysis_report.txt      # 可读分析报告
    ├── <PaperName>_runs.json                # 各轮抽取详情
    ├── paddleocrvl_parse/                   # 仅 PDF 输入时生成
    │   ├── <PaperName>_final_output.md
    │   ├── <PaperName>_parse_metadata.json
    │   ├── page_images/
    │   └── ocr_raw/
    └── txt_parse/                           # TXT 输入时生成
        ├── <PaperName>_final_output.md
        └── <PaperName>_parse_metadata.json
```

---

## 安装

### 前置要求

1. **Python 3.11**（建议配合 Conda）
2. **OpenAI 兼容 LLM API Key**（例如 ERNIE/Qianfan）
3. **LangChain API Key**（可选，用于 LangSmith tracing）

### 安装步骤

1. **克隆仓库**

```bash
git clone https://github.com/hasan-sayeed/KnowMat2.git
cd KnowMat2
```

2. **创建 Conda 环境**

```bash
conda env create -f environment.yml
conda activate KnowMat
```

如 `paddleocr` 安装时提示缺少后端 wheel，请先为你的平台安装 `paddlepaddle` 后再重试。  
如果要处理 PDF，建议预下载 PaddleOCR-VL 模型到项目目录：

```bash
python scripts/download_paddleocrvl_models.py --model-dir models/paddleocrvl1_5
```

3. **配置 API Key**

将 `.env_example` 重命名为 `.env` 并填写：

```bash
LLM_API_KEY=<your_llm_api_key_here>
LLM_BASE_URL=<your_openai_compatible_base_url>
LLM_MODEL=<your_model_name_or_endpoint>
PADDLEOCRVL_MODEL_DIR=models/paddleocrvl1_5
LANGCHAIN_API_KEY=<your_langchain_api_key_here>  # 可选
LANGCHAIN_TRACING_V2=false                        # 可选
```

ERNIE/Qianfan 示例：

```bash
LLM_API_KEY="bce-v3/xxxx"
LLM_BASE_URL="https://qianfan.bj.baidubce.com/v2"
LLM_MODEL="ep_xxxxx"
```

也可以直接设置环境变量：

```bash
# Windows PowerShell
$env:LLM_API_KEY="your_key"
$env:LLM_BASE_URL="https://qianfan.bj.baidubce.com/v2"
$env:LLM_MODEL="ep_xxxxx"

# Linux/Mac
export LLM_API_KEY="your_key"
export LLM_BASE_URL="https://qianfan.bj.baidubce.com/v2"
export LLM_MODEL="ep_xxxxx"
```

4. **验证安装**

```bash
python -m knowmat --help
```

---

## 使用方法

### 推荐目录与自动处理逻辑

请将待抽取论文统一放在：

```text
data/raw/
```

程序运行时会按“同名文件基名”执行以下逻辑：

1. 若存在 `xxx.txt`，直接用该 TXT 进入大模型抽取；
2. 若存在 `xxx.pdf` 且不存在同名 `xxx.txt`，先调用 PaddleOCR 解析 PDF，自动生成 `data/raw/xxx.txt`，再用该 TXT 进入大模型抽取；
3. 若 `xxx.pdf` 与 `xxx.txt` 同时存在，优先复用现有 TXT，不重复 OCR。

默认输出位置为：

```text
data/processed/
```

每篇论文的结果在：

```text
data/processed/<论文基名>/
```

其中重点查看：

- `<论文基名>_extraction.json`：结构化抽取结果
- `<论文基名>_analysis_report.txt`：分析报告
- `<论文基名>_runs.json`：多轮运行明细

### 基础命令行用法

使用默认目录（推荐）：

```bash
python -m knowmat
```

等价于从 `data/raw` 读取输入，并输出到 `data/processed`。  

也可以指定自定义目录（会覆盖默认值）：

```bash
python -m knowmat --input-folder path/to/files --output-dir output/directory
```

行为说明：

- `.pdf`：先使用本地 PaddleOCR-VL 1.5 解析，再进行 LLM 抽取
- `.txt`：跳过 OCR，直接进入 LLM 抽取流程

### 进阶参数示例

```bash
python -m knowmat \
    --input-folder path/to/files \
    --output-dir output/directory \
    --max-runs 1 \
    --workers 4 \
    --force-rerun \
    --only 1-2024-MSEA-Ti₄₂Hf₂₁Nb₂₁V₁₆-DED 2-2025-Acta-Nb₁₅Ta₁₀W₇₅---添加NbC\ 纳米沉淀 \
    --extraction-model ${LLM_MODEL} \
    --evaluation-model ${LLM_MODEL} \
    --manager-model ${LLM_MODEL} \
    --subfield-model ${LLM_MODEL} \
    --flagging-model ${LLM_MODEL}
```

### 命令行参数

| 参数 | 说明 | 默认值 |
|------|------|--------|
| `--input-folder` | 输入目录（包含 `.pdf`/`.txt`） | `data/raw` |
| `--pdf-folder` | `--input-folder` 的旧别名 | - |
| `--output-dir` | 输出目录 | `data/processed` |
| `--max-runs` | 每篇论文的最大抽取/评估轮数 | `1` |
| `--workers` | 并发处理文件数 | `1` |
| `--full-pipeline` | 启用完整多阶段流水线 | `False` |
| `--enable-property-standardization` | 启用属性标准化后处理 | `False` |
| `--force-rerun` | 即使已有 `_extraction.json` 也强制重跑所有论文 | `False` |
| `--only` | 仅处理指定文件（按 stem 或完整文件名匹配，可传多个） | - |
| `--subfield-model` | 子领域识别模型 | `LLM_MODEL` |
| `--extraction-model` | 抽取模型 | `LLM_MODEL` |
| `--evaluation-model` | 评估模型 | `LLM_MODEL` |
| `--manager-model` | 二阶段校验模型 | `LLM_MODEL` |
| `--flagging-model` | 最终质量评估模型 | `LLM_MODEL` |

### Python API

```python
from knowmat.orchestrator import run
import os

result = run(
    pdf_path="path/to/paper.pdf",  # 也支持 .txt
    output_dir="data/processed",
    max_runs=3,
    subfield_model=os.getenv("LLM_MODEL"),
    extraction_model=os.getenv("LLM_MODEL"),
    evaluation_model=os.getenv("LLM_MODEL"),
    manager_model=os.getenv("LLM_MODEL"),
    flagging_model=os.getenv("LLM_MODEL"),
)

print(f"Extracted {len(result['final_data']['compositions'])} compositions")
print(f"Confidence: {result.get('confidence_score', 0):.2f}")
print(f"Flagged: {result['flag']}")
```

---

## 输出示例

```json
{
  "compositions": [
    {
      "composition": "Zr64.13Cu15.75Ni10.12Al10",
      "composition_normalized": "Zr64Cu16Ni10Al10",
      "processing_conditions": {
        "method": "melt spinning",
        "temperature": "1400 K",
        "cooling_rate": "10^6 K/s",
        "atmosphere": "argon"
      },
      "characterization": {
        "XRD": "amorphous structure confirmed",
        "DSC": "glass transition at 625 K; crystallization at 705 K"
      },
      "properties_of_composition": [
        {
          "property_name": "glass transition temperature",
          "property_symbol": "Tg",
          "value": "625",
          "value_numeric": 625.0,
          "value_type": "exact",
          "units": "K"
        },
        {
          "property_name": "fracture strength",
          "property_symbol": "σ_max",
          "value": ">1800",
          "value_numeric": 1800.0,
          "value_type": "lower_bound",
          "units": "MPa"
        }
      ]
    }
  ]
}
```

---

## 项目结构

```text
├── AUTHORS.md              <- 开发者与维护者列表
├── CHANGELOG.md            <- 版本变更记录（新功能与修复）
├── CONTRIBUTING.md         <- 项目贡献指南
├── LICENSE.txt             <- MIT 许可证
├── README.md               <- 项目说明文档（当前文件）
├── environment.yml         <- Conda 环境依赖定义
├── pyproject.toml          <- 构建系统配置
├── setup.cfg               <- 包元数据与依赖配置
├── setup.py                <- 安装脚本（已弱化，建议使用 pip install -e .）
│
├── configs/                <- 配置文件目录
│   └── properties.json     <- 属性标准化词库
│
├── data/                   <- 数据目录
│   ├── raw/                <- 原始输入目录（放待抽取的 .pdf/.txt）
│   └── processed/          <- 抽取结果输出目录
│       └── <PaperName>/    <- 按论文分组的输出子目录
│
├── src/                    <- 源代码目录
│   └── knowmat/            <- 主包
│       ├── __init__.py
│       ├── __main__.py     <- CLI 入口
│       ├── orchestrator.py <- 流水线编排（LangGraph）
│       ├── app_config.py   <- 应用配置（默认输入/输出目录与模型配置）
│       ├── config.py       <- 环境变量加载与运行时配置
│       ├── states.py       <- LangGraph 状态定义
│       ├── extractors.py   <- TrustCall/Pydantic 抽取结构定义
│       ├── prompt_generator.py <- 动态提示词生成
│       ├── post_processing.py  <- 属性标准化后处理
│       └── nodes/          <- 各代理节点实现
│           ├── paddleocrvl_parse_pdf.py  <- PDF/TXT 解析节点（含 OCR 逻辑）
│           ├── subfield_detection.py      <- 子领域识别节点
│           ├── extraction.py              <- 结构化抽取节点
│           ├── evaluation.py              <- 抽取质量评估节点
│           ├── aggregator.py              <- Manager 第 1 阶段：规则聚合
│           ├── validator.py               <- Manager 第 2 阶段：LLM 校验修正
│           └── flagging.py                <- 最终质量标记节点
│
├── tools/                  <- 开发工具集
│   ├── regression_diff.py  <- 回归测试工具（AI vs GT 对比）
│   └── README.md           <- 工具使用说明
│
├── reports/                <- 回归测试报告输出目录
│   ├── regression_*.md     <- Markdown 格式报告
│   └── regression_*.json   <- JSON 格式报告
│
├── tests/                  <- 单元测试（pytest）
├── notebooks/              <- 数据分析与实验笔记
└── docs/                   <- 文档目录（Sphinx，已同步中文说明）
```

---

## 高级能力

### 两阶段 Manager 架构

KnowMat 将“合并”和“校验”分离，兼顾效率与可靠性：

**Stage 1 - Aggregation（规则化）**：
- 快速、确定性地合并多轮抽取结果
- 无 LLM 调用（零额外模型成本）
- 以高置信度轮次为基础补全信息

**Stage 2 - Validation（LLM 校验）**：
- 基于评估反馈定位幻觉字段
- 修正疑似幻觉内容
- 检查输出是否满足机器学习可用格式
- 提供重试机制与人工复核建议

### 属性标准化

PostProcessor 会将抽取出的属性名称映射为标准术语。  
示例：

- `"Dimensionless figure of merit ZT"` → `"thermoelectric figure of merit"`
- `"glass transition temp"` → `"glass transition temperature"`
- `"ultimate tensile strength"` → `"tensile strength"`
- `"Young's modulus"` → `"elastic modulus"`

### 批处理能力

```bash
python -m knowmat --input-folder data/raw/papers --output-dir data/processed
```

控制台示例：

```text
Processing file 1/150: paper001.pdf
Processing file 2/150: notes002.txt
...

Total files: 150
Successful: 147
Failed: 3
Flagged for review: 23
Total compositions: 2,341
```

### LangSmith Tracing

启用后可在 LangSmith 观察完整链路：

- 每次 LLM 调用与响应
- 抽取决策与提示词效果
- 各代理交互过程
- Token 消耗与成本

访问：<https://smith.langchain.com/>

---

## 模型选择与成本优化

支持按代理单独配置模型，以平衡成本与精度。  
使用 ERNIE/Qianfan 时，设置 `LLM_MODEL` 后可按需覆盖各代理模型。

推荐配置（生产）：

```bash
--subfield-model ${LLM_MODEL}
--extraction-model ${LLM_MODEL}
--evaluation-model ${LLM_MODEL}
--manager-model ${LLM_MODEL}
--flagging-model ${LLM_MODEL}
```

---

## 工具集

### 回归测试工具（Regression Diff - 三模式）

KnowMat 提供了功能强大的回归测试工具 `tools/regression_diff.py`，支持三种运行模式：

| 模式 | 说明 | 需要 GT | 适用场景 |
|------|------|---------|----------|
| **gt** | AI vs Ground Truth | ✅ 需要 | 精确评估有手工标注的论文（6篇） |
| **self** | Run vs Run（自回归） | ❌ 不需要 | 对比两次 AI 抽取结果，验证 prompt 优化效果（所有论文） |
| **qa** | 质量基线检查 | ❌ 不需要 | 快速发现完全失败或质量极差的论文（所有论文） |

#### 核心功能

**GT 模式**（AI vs Ground Truth）：

- 结构指标对比（Materials/Samples/Properties 数量）
- 字段准确率评估（DOI、Main_Phase、Process_Category 等）
- 温度质量检查（偏移统计）
- 成分解析质量（非法元素、百分比和校验）

**Self 模式**（Run vs Run）：
- 创建快照保存当前抽取结果
- 对比两次抽取的差异（Materials/Samples/Properties 数量变化）
- 检测 DOI/Phase/Process 的变化趋势
- 无需 GT，适用于所有论文

**QA 模式**（质量基线检查）：
- 扫描所有论文抽取结果，计算质量得分（0-100）
- 红线告警：自动标记需人工复核的论文
- 质量指标：材料数、属性数、DOI 存在率、Phase 填充率等
- 按质量得分排序，快速定位最差论文

#### 快速开始

```bash
# GT 模式：对比 6 篇有手工标注的论文
python tools/regression_diff.py gt --all

# Self 模式：保存快照并对比变化
python tools/regression_diff.py self --snapshot baseline
# (修改 prompt 后重跑 AI 抽取)
python tools/regression_diff.py self --compare baseline

# QA 模式：扫描所有论文质量
python tools/regression_diff.py qa

# 向后兼容（等价于 gt --all）
python tools/regression_diff.py --all
```

#### 输出报告

**Markdown 报告**（人类可读）：
- 总体指标表格（结构指标、字段准确率、温度质量、成分质量）
- 逐篇详细对比（标记 ✅ 达标 / ❌ 未达标）
- 具体问题列表（成分错误、DOI 缺失等）

**JSON 报告**（机器可读）：
- 结构化数据，便于 CI/CD 集成
- 包含所有指标的详细数值
- 支持程序化分析和趋势监控

#### 典型工作流

```bash
# 1. 基线测试（优化前）
python tools/regression_diff.py --all --output reports/baseline

# 2. 修改 prompt 或 schema
# (编辑 src/knowmat/prompt_generator.py 或 extractors.py)

# 3. 重跑 AI 抽取
python -m knowmat --force-rerun --max-runs 1

# 4. 对比验证（优化后）
python tools/regression_diff.py --all --output reports/after_optimization

# 5. 对比两次报告，确认关键指标是否改善：
#    - DOI 命中率是否提升？
#    - Main_Phase 填充率是否改善？
#    - Process_Category Unknown 占比是否降低？
#    - 温度偏移是否消除？
#    - 成分解析问题是否减少？
```

#### 控制台输出示例

```
============================================================
回归测试摘要
============================================================

📊 关键指标:
  DOI 命中率:             0.0% ❌
  Main_Phase 填充率:      16.7% ❌
  Process_Category 准确率: 16.7% ❌
  温度平均偏移:           127.09 K ❌

⚠️ 成分质量问题:
  非法元素:   1 篇
  百分比异常: 5 篇
  空成分:     1 篇
============================================================
```

#### 评价标准

工具采用以下阈值标记 ✅ 达标 / ❌ 未达标：

- **DOI 命中率** ≥ 80%
- **Main_Phase 填充率** ≥ 70%
- **Process_Category 非 Unknown** ≥ 85%
- **温度平均偏移** < 0.5 K
- **无成分解析问题**（无非法元素、百分比和正常）

详细使用说明见 [`tools/README.md`](tools/README.md)。

---

## 故障排查

### 常见问题

**1）API Key 未设置**

```text
Error: LLM_API_KEY not set
```

解决：确保设置 `LLM_API_KEY`、`LLM_BASE_URL`、`LLM_MODEL`。

**2）PaddleOCR-VL 解析失败**

```text
Error: Failed to parse PDF with PaddleOCR-VL
```

解决：检查 PDF 是否损坏或加密，必要时重新下载。

**3）属性标准化失败**

```text
Warning: Property standardization failed
```

解决：确认属性配置文件存在且为合法 JSON。

**4）ERNIE 接口报 Unrecognized function call PatchFunction**

```text
Unrecognized function call PatchFunction
```

说明：该提示来自 **LLM 客户端**（TrustCall/LangChain）在解析 ERNIE/千帆 API 的**返回结果**时发现工具调用名不是我们请求的 `CompositionList`，而是 `PatchFunction`。**ERNIE 官方文档中未公开该接口**，很可能是其 OpenAI 兼容层或内部实现返回的非标准工具名。

影响：客户端无法按预期解析工具调用，可能伴随 `CompositionList` 的校验错误；我们已在 schema 中为必填字段增加默认值，部分返回仍可通过校验并写入结果（QA 会标记需复核）。
。

---

## 规划路线

### 已完成 ✅

- [x] **回归测试工具**：自动化 AI 抽取结果与 Ground Truth 对比
- [x] **Role 分类**：区分 Target（本文主材料）与 Reference（引用材料）
- [x] **Material-Sample-Property 三层架构**：精确区分成分/状态/测试
- [x] **成分质量校验**：非法元素检测、原子百分比和校验
- [x] **QA 报告生成**：红线告警、自动标记需人工复核的论文
- [x] **温度标准化增强**：防止重复转换、统一输出格式
- [x] **Process_Category 扩展**：支持 14 种工艺分类（WAAM/EBM/HIP 等）

### 规划中 🔮

- [ ] Web 界面（面向非技术用户）
- [ ] 数据库集成（PostgreSQL/MongoDB）
- [ ] 科研图表数据抽取（表格、曲线识别）
- [ ] 多领域扩展（化学、生物、物理）
- [ ] 增量学习（基于用户反馈优化提示词）

---

## 引用

如果你的研究使用了 KnowMat，请引用：

```bibtex
@software{knowmat2024,
  title = {KnowMat: Agentic Pipeline for Materials Science Data Extraction},
  author = {Sayeed, Hasan},
  year = {2024},
  url = {https://github.com/hasan-sayeed/KnowMat2}
}
```

---

## 贡献

欢迎贡献代码与建议。详情见 `CONTRIBUTING.md`。

基本流程：

1. Fork 仓库
2. 新建分支（如 `feature/amazing-feature`）
3. 提交修改
4. 推送分支
5. 发起 Pull Request

---

## 许可证

本项目使用 MIT License，详见 `LICENSE.txt`。

---

## 致谢

- Built with [PyScaffold](https://pyscaffold.org/)
- Powered by [LangGraph](https://github.com/langchain-ai/langgraph) and [LangChain](https://github.com/langchain-ai/langchain)
- PDF parsing by [PaddleOCR](https://github.com/PaddlePaddle/PaddleOCR)

---

## 支持

- GitHub Issues：<https://github.com/hasan-sayeed/KnowMat2/issues>
- Email：hasan.sayeed@utah.edu
