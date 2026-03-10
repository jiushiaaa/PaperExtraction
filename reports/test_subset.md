# KnowMat 回归测试报告

**生成时间**: 2026-03-09T17:49:31.926801

**对比论文数**: 3/3

---

## 总体指标

### 结构指标

| 指标 | AI 均值 | GT 均值 | AI/GT 比率 |
|------|---------|---------|------------|
| Materials per paper | 1.33 | 1.33 | 100.0% |
| Samples per paper | 1.33 | 2.33 | 57.1% |
| Properties per paper | 28.3 | 18.0 | 157.2% |

### 字段准确率

| 字段 | 指标 | 数值 | 评价 |
|------|------|------|------|
| DOI | 命中率 | 0.0% | ❌ |
| Main_Phase | AI 填充率 | 0.0% | ❌ |
| Main_Phase | 匹配率 | 0.0% | ❌ |
| Has_Precipitates | 匹配率 | 66.7% | ❌ |
| Process_Category | 匹配率 | 33.3% | ❌ |
| Process_Category | Unknown 占比 | 50.0% | ❌ |
| Grain_Size | AI 填充率 | 0.0% | ❌ |

### 温度质量

- **平均偏移**: 136.20 K
- **最大偏移**: 796.00 K
- **偏移测试数** (>1K): 14
- **评价**: ❌ 存在偏移

### 成分质量

- **非法元素问题**: 1 篇
- **原子百分比和异常**: 1 篇
- **Composition_JSON 为空**: 0 篇
- **评价**: ❌ 存在成分解析问题

---

## 逐篇对比详情

### 论文 1

**AI 文件**: `data\processed\1-2024-MSEA-Ti₄₂Hf₂₁Nb₂₁V₁₆-DED\1-2024-MSEA-Ti₄₂Hf₂₁Nb₂₁V₁₆-DED_extraction.json`

**GT 文件**: `手工标注结果\1-data.json`

- **Materials**: AI=1, GT=1 ✅
- **Samples**: AI=1, GT=1 ✅
- **Properties**: AI=17, GT=8 ✅
- **DOI**: ❌ AI="" vs GT="10.1016/j.msea.2024.147225"
- **Main_Phase**: AI填充=0/1, 匹配率=0.0% ❌
- **Has_Precipitates**: 匹配率=100.0% ✅
- **Process_Category**: 匹配率=100.0%, Unknown=0/1 ✅
- **温度偏移**: 平均=0.00K, 最大=0.00K ✅
- **成分问题**: ❌
  - Ti42Hf21Nb21V16(T42): Invalid elements ['T']
  - Ti42Hf21Nb21V16(T42): Sum=142.0% (expected ~100%)

### 论文 2

**AI 文件**: `data\processed\2-2025-Acta-Nb₁₅Ta₁₀W₇₅---添加NbC 纳米沉淀\2-2025-Acta-Nb₁₅Ta₁₀W₇₅---添加NbC 纳米沉淀_extraction.json`

**GT 文件**: `手工标注结果\2-data.json`

- **Materials**: AI=2, GT=2 ✅
- **Samples**: AI=2, GT=4 ⚠️
- **Properties**: AI=46, GT=28 ✅
- **DOI**: ❌ AI="" vs GT="10.1016/j.actamat.2025.121325"
- **Main_Phase**: AI填充=0/2, 匹配率=0.0% ❌
- **Has_Precipitates**: 匹配率=50.0% ❌
- **Process_Category**: 匹配率=0.0%, Unknown=1/2 ❌
- **温度偏移**: 平均=77.05K, 最大=599.85K ❌
- **成分问题**: ✅ 无问题

### 论文 3

**AI 文件**: `data\processed\3-2024-JMST- Co42Cr20Ni30Ti4Al4\3-2024-JMST- Co42Cr20Ni30Ti4Al4_extraction.json`

**GT 文件**: `手工标注结果\3-data.json`

- **Materials**: AI=1, GT=1 ✅
- **Samples**: AI=1, GT=2 ⚠️
- **Properties**: AI=22, GT=18 ✅
- **DOI**: ❌ AI="" vs GT="10.1016/j.jmst.2024.02.077"
- **Main_Phase**: AI填充=0/1, 匹配率=0.0% ❌
- **Has_Precipitates**: 匹配率=50.0% ❌
- **Process_Category**: 匹配率=0.0%, Unknown=1/1 ❌
- **温度偏移**: 平均=331.56K, 最大=796.00K ❌
- **成分问题**: ✅ 无问题

---

*报告生成工具: KnowMat regression_diff.py*
