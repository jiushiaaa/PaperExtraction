# KnowMat 工具集

## regression_diff.py - 回归测试工具（三模式）

### 功能概述

KnowMat 回归测试工具支持三种运行模式，覆盖不同的测试场景：

| 模式 | 说明 | 需要 GT | 适用场景 |
|------|------|---------|----------|
| **gt** | AI vs Ground Truth | ✅ 需要 | 精确评估 6 篇有手工标注的论文 |
| **self** | Run vs Run（自回归） | ❌ 不需要 | 对比两次 AI 抽取结果的差异，验证 prompt 优化效果 |
| **qa** | 质量基线检查 | ❌ 不需要 | 扫描所有论文，快速发现完全失败或质量极差的论文 |

---

## 模式 1: GT 模式（AI vs Ground Truth）

### 功能说明

对比 AI 抽取结果与手工标注，量化以下指标：

- **结构指标**：Material/Sample/Property 数量
- **字段准确率**：DOI、Main_Phase、Has_Precipitates、Process_Category、Grain_Size
- **温度质量**：测试温度偏移统计
- **成分质量**：Composition_JSON 完整性、非法元素检测、原子百分比和验证

### 使用方法

#### 基础用法

```bash
# 对比全部 6 篇有 GT 的论文
python tools/regression_diff.py gt --all

# 对比指定论文（编号 1-6）
python tools/regression_diff.py gt --papers 1 2 3

# 向后兼容（等价于 gt --all）
python tools/regression_diff.py --all
```

#### 指定输出格式

```bash
# 只生成 Markdown 报告
python tools/regression_diff.py --all --format markdown

# 只生成 JSON 报告（便于自动化集成）
python tools/regression_diff.py --all --format json

# 同时生成两种格式（默认）
python tools/regression_diff.py --all --format both
```

#### 自定义输出路径

```bash
# 指定输出文件名（不含扩展名，会自动添加 .md/.json）
python tools/regression_diff.py --all --output reports/my_regression_test

# 如果不指定 --output，默认使用时间戳命名：
# reports/regression_YYYYMMDD_HHMMSS.md
# reports/regression_YYYYMMDD_HHMMSS.json
```

### 输出说明

#### Markdown 报告

包含三个主要部分：

1. **总体指标**
   - 结构指标表（Materials/Samples/Properties 数量对比）
   - 字段准确率表（DOI/Phase/Process 等命中率）
   - 温度质量统计（平均/最大偏移，偏移测试数）
   - 成分质量问题汇总

2. **逐篇对比详情**
   - 每篇论文的详细指标
   - 标记 ✅（达标）或 ❌（未达标）
   - 列出具体的成分解析问题

3. **评价标准**
   - DOI 命中率 ≥ 80%
   - Main_Phase 填充率 ≥ 70%
   - Process_Category 非 Unknown ≥ 85%
   - 温度平均偏移 < 0.5 K
   - 无成分解析问题

#### JSON 报告

机器可读格式，包含：

```json
{
  "timestamp": "2026-03-09T17:49:21.556258",
  "papers_compared": 6,
  "papers_total": 6,
  "summary": {
    "structure": { ... },
    "field_accuracy": { ... },
    "temperature": { ... },
    "composition_quality": { ... }
  },
  "details": [ ... ]
}
```

适用于 CI/CD 集成、自动化监控、版本对比等场景。

### 典型工作流

#### 优化验证工作流

```bash
# 1. 基线测试（优化前）
python tools/regression_diff.py gt --all --output reports/gt_baseline

# 2. 修改 prompt 或 schema
# (编辑 src/knowmat/prompt_generator.py 或 extractors.py)

# 3. 重跑 AI 抽取
python -m knowmat --force-rerun --max-runs 1

# 4. 对比验证（优化后）
python tools/regression_diff.py gt --all --output reports/gt_after_optimization

# 5. 手动对比两次报告，确认关键指标是否改善
```

---

## 模式 2: Self 模式（Run vs Run 自回归）

### 功能说明

无需 Ground Truth，对比同一批论文的两次 AI 抽取结果，适用于：

- 验证 prompt 优化后所有论文的结果变化
- 检测改动是否引入了"改好6篇却改坏其他论文"的问题
- 监控批量论文抽取结果的一致性

### 使用方法

#### 1. 创建快照

在优化前保存当前的 AI 抽取结果：

```bash
python tools/regression_diff.py self --snapshot baseline
```

快照会保存到 `reports/snapshots/baseline/`，包含所有当前的 `_extraction.json` 文件。

#### 2. 列出所有快照

```bash
python tools/regression_diff.py self --list
```

#### 3. 优化后对比

修改 prompt/schema 并重新抽取后，与快照对比：

```bash
# 重跑 AI 抽取
python -m knowmat --force-rerun --max-runs 1

# 对比差异
python tools/regression_diff.py self --compare baseline
```

### 对比维度

Self 模式对比以下指标的变化（无需 GT）：

- **Materials/Samples/Properties 数量**：增加/减少/不变
- **DOI 状态**：新增/丢失/不变/变更
- **Phase 填充率**：填充率的增减
- **Process Unknown 率**：Unknown 比例的增减

### 输出报告

**Markdown 报告示例**：

```markdown
## 总体变化

| 指标 | 改善 | 恶化 | 不变 |
|------|------|------|------|
| 论文数 | 15 | 3 | 12 |

| 指标 | 平均变化 | 趋势 |
|------|----------|------|
| Materials 数量 | +0.20 | 📈 |
| Properties 数量 | +5.30 | 📈 |
| Phase 填充率 | +0.15 | 📈 |
| Process Unknown 率 | -0.12 | 📉 |
```

**控制台输出**：

```
📊 论文变化统计:
  改善: 15 篇
  恶化: 3 篇
  不变: 12 篇

📈 平均变化:
  Materials:  +0.20
  Properties: +5.30
  Phase 填充率: +0.150
  Process Unknown 率: -0.120 ✅
```

### 典型工作流

```bash
# 1. 保存优化前的快照
python tools/regression_diff.py self --snapshot before_prompt_v2

# 2. 修改 prompt（如加负例块）
# (编辑 src/knowmat/prompt_generator.py)

# 3. 重跑所有论文
python -m knowmat --force-rerun --max-runs 1

# 4. 对比变化
python tools/regression_diff.py self --compare before_prompt_v2

# 5. 如果效果好，保存新快照作为新基线
python tools/regression_diff.py self --snapshot after_prompt_v2
```

---

## 模式 3: QA 模式（质量基线检查）

### 功能说明

无需 Ground Truth，扫描所有论文的抽取结果，计算内在质量指标，适用于：

- 快速发现完全失败的论文（Materials=0, Properties=0）
- 批量扫描数十篇论文，按质量得分排序
- 红线告警：自动标记需要人工复核的论文

### 使用方法

#### 扫描所有论文

```bash
python tools/regression_diff.py qa
```

#### 扫描指定论文

```bash
python tools/regression_diff.py qa --papers 1 5 8 12 15
```

### 质量指标

QA 模式计算以下内在质量指标（无需 GT）：

| 指标 | 说明 | 评价标准 |
|------|------|----------|
| materials_count | 材料数 | 0 = 失败 |
| properties_count | 属性数 | 0 = 失败 |
| doi_present | DOI 是否存在 | True = 通过 |
| phase_filled_rate | Main_Phase 填充率 | ≥ 70% = 通过 |
| process_unknown_rate | Process Unknown 占比 | < 15% = 通过 |
| composition_valid_rate | Composition_JSON 有效率 | ≥ 80% = 通过 |
| grain_filled_rate | Grain_Size 填充率 | - |
| **quality_score** | **综合质量得分** | **0-100 分** |

### 红线告警

以下情况会触发红线告警（`needs_review=true`）：

- ❌ `NO_MATERIALS`：材料数 = 0（完全失败）
- ❌ `NO_PROPERTIES`：属性数 = 0（完全失败）
- ⚠️ `HIGH_UNKNOWN_PROCESS`：Process Unknown 率 > 50%
- ⚠️ `LOW_COMPOSITION_QUALITY`：Composition 有效率 < 50%

### 输出报告

**Markdown 报告示例**：

```markdown
## 总体统计

| 状态 | 论文数 | 占比 |
|------|--------|------|
| ✅ 通过 | 25 | 83.3% |
| ⚠️ 警告 | 3 | 10.0% |
| ❌ 失败 | 2 | 6.7% |

## 逐篇详情（按质量得分排序）

### ❌ 4-2025-IJP-xxx (得分: 20/100)

- **Materials**: 0
- **Properties**: 0
- **红线告警**: NO_MATERIALS, NO_PROPERTIES
```

**控制台输出**：

```
📊 论文状态统计:
  ✅ 通过: 25 篇
  ⚠️ 警告: 3 篇
  ❌ 失败: 2 篇

📈 平均质量指标:
  质量得分: 72.5/100 ✅
  DOI 存在率: 85.0% ✅
  Phase 填充率: 68.3% ❌
  Process Unknown 率: 12.5% ✅

⚠️ 需要人工复核的论文 (5 篇):
  - 4-2025-IJP-xxx (得分: 20/100, 问题: NO_MATERIALS, NO_PROPERTIES)
  - 12-2024-MSEA-yyy (得分: 45/100, 问题: HIGH_UNKNOWN_PROCESS)
  ...
```

### 典型工作流

```bash
# 1. 批量抽取完成后扫描质量
python -m knowmat  # 抽取所有论文
python tools/regression_diff.py qa

# 2. 查看 QA 报告，找到失败论文
# (打开 reports/qa_baseline_*.md)

# 3. 针对性修复失败论文
python -m knowmat --only 4-2025-IJP-xxx --force-rerun

# 4. 再次扫描验证
python tools/regression_diff.py qa --papers 4
```

---

## 三模式对比总结

| 特性 | GT 模式 | Self 模式 | QA 模式 |
|------|---------|-----------|---------|
| 需要 GT | ✅ 需要 | ❌ 不需要 | ❌ 不需要 |
| 适用论文数 | 6 篇（有标注） | 所有论文 | 所有论文 |
| 主要用途 | 精确评估准确率 | 检测变化/回归 | 快速发现失败论文 |
| 输出内容 | 准确率、召回率 | 变化趋势、差异 | 质量得分、红线告警 |
| 典型频率 | 每次优化后 | 每次优化后 | 每批抽取完成后 |

---

### 常见问题

#### Q: 为什么有些论文找不到？

A: 确保 AI 结果目录结构正确：

```
data/processed/
├── 1-2024-MSEA-Ti₄₂Hf₂₁Nb₂₁V₁₆-DED/
│   └── 1-*_extraction.json
├── 2-2025-Acta-*/
│   └── 2-*_extraction.json
...
```

手工标注目录结构：

```
手工标注结果/
├── 1-data.json
├── 2-data.json
...
```

#### Q: 温度偏移为什么这么大？

A: 当前 AI 结果可能使用了摄氏度但未转换为开尔文，或者转换时加了 273.15 导致精度损失。检查 `orchestrator.py` 中的 `_parse_temperature_to_k` 函数。

#### Q: Main_Phase 填充率为什么这么低？

A: LLM 可能未被提示提取相结构信息，或者后处理逻辑未正确解析。检查 `prompt_generator.py` 是否包含 Phase 提取指令。

#### Q: 如何只看某个指标的对比？

A: 打开生成的 JSON 报告，解析 `summary.field_accuracy` 或 `details[i].phases` 等字段。

### 后续扩展

- [ ] 支持对比两次 AI 结果（diff between runs）
- [ ] 增加 CI 集成脚本（自动判断是否回归）
- [ ] 增加可视化报告（HTML 格式，带图表）
- [ ] 支持增量对比（只对比新增/修改的论文）

---

**维护者**: KnowMat 开发团队  
**最后更新**: 2026-03-09
