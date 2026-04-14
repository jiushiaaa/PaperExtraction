# Pipeline（Result A）vs 人工（Result B）差距分析报告

> 基于 25 篇评测文件（5 位评审 × 5 篇），仅聚焦 **Result A（Pipeline 输出）** 的问题，对照 Result B（人工修正）提炼共性缺陷与个例，并结合代码根因分析，给出改进建议。

---

## 一、共性问题（多篇反复出现）

### 🔴 P0 级共性问题

---

#### 1. 样品条目拆分不足 / 漏提取样品

**覆盖文件：** 齐洋_01、齐洋_04、李希海_02（仅提取 θ=0° 漏了 θ=45°/θ=90°）、李希海_04（R2 样品完全遗漏）、潘星宇_04（H230 合金数据完全缺失）、王卓_04（缺多功率 200W/250W/300W 拆分）、王卓_05（CL/PL 样品数据严重错误）

**问题描述：**
Pipeline 对"同一合金不同处理状态"或"实验矩阵多行"常常只提取一个代表性条目，导致多处理状态（沉积态/时效/热处理）、多参数水平（激光功率、VED 等）、多角度（θ=0°/45°/90°）等被合并或遗漏。

**根因分析：**
- `extraction_system_template.txt` 的 Item Definition 规则写得较完整，但 LLM 在实践中对"同成分+不同处理"的矩阵枚举理解不稳定。
- 当论文用简写符号矩阵（如 S0/S5/S10/S30/S45）定义样品时，LLM 倾向于只抓代表性样品而非逐行输出。
- `process_category` 字段对工艺区分力弱，导致拆分依据不足。

**代码关联：**
- `prompts/extraction_user_template.txt`：Example F/G 有矩阵枚举示例，但缺乏对"时效态/热处理态"链的显式 Example。
- `extractors.py` 的 `CompositionProperties` schema 无显式校验"样品数量下限"。

---

#### 2. process_category 工艺类别错误

**覆盖文件：** 李希海_03（PBF-EB 被错标为 AM_LPBF）、潘星宇_02（Casting 应为 Powder Metallurgy）、王新田_05（Unknown 应为 AM_DED/LAAM）

**问题描述：**
Pipeline 对制造工艺类别判断错误，常见于：
- 将 Arcam（电子束）误判为 LPBF（激光）
- 将粉末冶金（PM/HIP/挤压/等温锻造）误判为铸造
- 对激光辅助增材（LAAM/DED）标注为 Unknown

**根因分析：**
- `domain_rules.yaml` 的 `process_category_keywords` 中 `EBM` 关键词列表仅含 `ebm`/`electron beam melting`，未覆盖 `Arcam`、`PBF-EB`、`electron beam powder bed fusion` 等常用表述。
- `Powder_Metallurgy`（PM）完全没有对应类别，HIP/挤压/锻造被错归为 Casting。
- LAAM 未在关键词列表中定义。

**代码关联：**
- `src/knowmat/domain_rules.yaml`：`process_category_keywords.EBM` 需补充同义词；缺 `PM`/`Powder_Metallurgy` 分类。
- `prompts/extraction_system_template.txt`：`process_category` 字段枚举中缺 `EBM`、`PM`、`WAAM` 等类别的明确说明。

---

#### 3. 关键工艺参数 Key_Params 缺失或留空

**覆盖文件：** 齐洋_01、齐洋_04（激光功率/扫描速度/层厚/间距全部缺失）、王新田_04（光斑直径、体能量密度未提取）、李希海_01（粉末干燥条件缺失）

**问题描述：**
Pipeline 对工艺参数（`processing_params`）提取覆盖率低，常留空或只提取了部分参数。激光功率、扫描速度、层厚、间距等核心 AM 参数经常全部缺失。

**根因分析：**
- `domain_rules.yaml` 中 `parameter_patterns` 的正则只匹配 `laser power = X W` 或 `P = X W` 这种格式，对 OCR 输出中常见的 `P: 200 W`、`200W`、`power of 200 W` 等写法无法匹配。
- 当参数散落在 Methods 段落而非表格时，LLM 提取率明显下降。

**代码关联：**
- `src/knowmat/domain_rules.yaml`：`parameter_patterns` 正则需扩展覆盖更多自然语言表述。
- `prompts/extraction_system_template.txt`：`Key_Params` 规则中可增加"优先从 Methods/Experimental 节提取参数"的显式提示。

---

#### 4. DOI 缺失

**覆盖文件：** 李希海_01（无 DOI 字段）、李希海_05（DOI 缺失）、潘星宇_03（DOI 错误）

**问题描述：**
Pipeline 经常未能提取 DOI，或提取了错误的 DOI。

**根因分析：**
- DOI 通常位于 PDF 头部/页眉或首页版权栏，OCR 对页眉/页脚过滤可能误删 DOI 所在区域。
- `extraction_system_template.txt` 中 `source_doi` 规则较简单，未指导 LLM 在多处检索（首页、参考文献、版权行）。

**代码关联：**
- `src/knowmat/pdf/doi_extractor.py`：专门的 DOI 提取模块，但可能未充分覆盖所有格式。
- `prompts/extraction_system_template.txt`：可在 `source_doi` 字段说明中补充"检索首页、版权行、参考文献首条"。

---

#### 5. 名义成分（Nominal_Composition）与实测成分（Measured_Composition）语义混用

**覆盖文件：** 王卓_01（粉末设计成分 vs ICP-OES 实测成分混用）、潘星宇_05（Table 1 标注实测值却填入 Nominal）、王新田_04（粉末 ICP-OES 成分 vs SEM-EDS 成分未区分）

**问题描述：**
Pipeline 经常将粉末/设计成分（Nominal）和加工后实测成分（Measured）混为一谈，或将两者颠倒填入。

**根因分析：**
- `extraction_system_template.txt` 虽然说明了 Nominal/Measured 的区分，但未给出当"原文同时提供两者"时的优先级判断规则。
- LLM 对"Table 1 标注为实测值（Measured）但放在 Nominal 字段"的分辨较难，尤其是当表格标题模糊时。

**代码关联：**
- `prompts/extraction_system_template.txt`：Composition Extraction 节可补充示例："Table 1 labeled as 'measured/ICP-OES' → `measured_composition`；design/nominal formula → `nominal_composition`"。

---

#### 6. 核心数据字段数值计算错误

**覆盖文件：** 李希海_01（PBF-LB 功率 1400W 应为 140W，十倍错误）、齐洋_01（Al 归一化值 98.27% 应为 97.27%）、王新田_04（位错密度数量级错误：差 1 个数量级）、王新田_03（名义成分计算错误）

**问题描述：**
Pipeline 出现数量级错误和计算错误，如功率值偷换数量级、成分归一化加总出错、位错密度单位换算错误。

**根因分析：**
- LLM 对 OCR 输出中的数字（尤其是上下标、×10^n 格式）容易误读。
- 成分归一化计算（百分比加和=100）无后处理校验机制。
- `extractors.py` 的 `_coerce_numeric_leaf` 仅做字符串→数值转换，未校验量级合理性。

**代码关联：**
- `src/knowmat/extractors.py`：`_coerce_numeric_leaf` 可增加量级合理性检测（如激光功率合理范围 10–10000 W）。
- 后处理层（`post_processing.py`）可增加成分加和校验（sum 应接近 100）。

---

### 🟡 P1 级共性问题

---

#### 7. 余量元素（Bal.）处理不当

**覆盖文件：** 潘星宇_01（Ni=100.0 表示 Bal.）、潘星宇_02、潘星宇_03（other 字段含义混乱）、潘星宇_04（Ni 余量未计算）

**问题描述：**
Pipeline 对合金中"余量"元素（通常是 Ni 或 Ti）处理策略不一致：有时填 100.0、有时填 `other`、有时留空，而非计算实际余量值。

**根因分析：**
- `extraction_system_template.txt` 规则："If sum < 100 and no explicit balance element is given, you may add `other`"，但未规定"已知余量元素时应计算填入实际值"。
- LLM 对"Bal."的处理缺乏统一策略，`other` 字段语义不清。

**代码关联：**
- `prompts/extraction_system_template.txt`：增加规则："当成分表中明确某元素为 Bal./余量时，应以 100 减去其余元素之和计算填入，而非填 100.0 或 `other`"。

---

#### 8. 高温力学性能数据漏提取

**覆盖文件：** 齐洋_02（高温 UTS/蠕变大面积缺失）、齐洋_03（200°C 延伸率/蠕变寿命遗漏）、王新田_05（中间合金 UTS 数值缺失）、潘星宇_04（蠕变数据缺失）、潘星宇_02（核心定量数据严重缺失）

**问题描述：**
Pipeline 对高温测试数据（蠕变寿命、高温 UTS/YS、应变速率敏感系数）提取覆盖率不足，尤其当数据散落在图表而非文本段落时。

**根因分析：**
- `properties_of_composition` schema 中虽有 `test_temperature_k` 字段，但 LLM 对"图表数据"（data_source=image）的提取积极性低。
- Prompt 中 Properties 提取规则未明确要求"遍历所有测试温度"。

**代码关联：**
- `prompts/extraction_system_template.txt`：可增加"Properties 提取时须枚举所有明确的测试温度点"的指导。

---

#### 9. 微观结构定量参数未结构化提取

**覆盖文件：** 王新田_01（微观尺度异质性误判为 Gradient_Material）、王新田_02（KAM 值/胞状结构尺寸/晶格失配建议入 Advanced_Quantitative_Features）、王新田_03（FCC/B2 体积分数未入 Advanced_Quantitative_Features）、李希海_01（O 相晶粒尺寸未提取）

**问题描述：**
Pipeline 对 EBSD/TEM/APT 等定量微观结构参数（位错密度、晶格失配、相体积分数、胞状结构尺寸等）提取不完整，或将其错误放入 `Properties_Info` 而非 `Advanced_Quantitative_Features`。

**根因分析：**
- `CompositionProperties` schema 中 `Advanced_Quantitative_Features` 字段在 `extractors.py` 中未定义（schema 缺失该字段），导致 LLM 即便想填也无处存放。
- Prompt 虽提及 `Advanced_Quantitative_Features`，但 Pydantic schema 中无对应字段。

**代码关联：**
- `src/knowmat/extractors.py`：`CompositionProperties` 类缺少 `advanced_quantitative_features: Optional[Dict[str, Any]]` 字段。
- `prompts/extraction_system_template.txt`：需在输出格式（Output Format）中补充该字段的 JSON 示例。

---

#### 10. 参考文献对照材料（Reference 条目）未提取

**覆盖文件：** 李希海_01（Table 6 文献对比数据未提取）、李希海_04（铸造参考样品未提取）、王新田_01（应提取参考文献材料数据）、王新田_04（可提取参考文献数据）

**问题描述：**
Pipeline 对原文中用于对比的文献数据（reference alloys）几乎不提取，导致数据库缺少比较基准。

**根因分析：**
- Prompt 规定了 `role: Reference`，但 LLM 默认只提取 Target 材料，对"论文中引用的对比数据"的识别率低。
- `extraction_user_template.txt` 的 Example H（"comparison-route retention"）说明了保留逻辑，但实际执行中 LLM 执行率不稳定。

---

#### 11. Main_Phase 缺失或填充不准确

**覆盖文件：** 王新田_02（时效态 Main_Phase 应为 "FCC + L12"）、潘星宇_04（H230AM 析出相错误填入 Main_Phase）

**问题描述：**
Pipeline 对主相标识存在缺失或错误，如将时效后双相结构只标注单相，或将析出相（ZrC）混入主相。

**根因分析：**
- `main_phase` 字段的 schema 描述限定"不得使用 Laves/carbides/gamma-prime 作为主相"，但对双相或多相基体的标注规则（如 "FCC + L12"）未明确。

---

### 🟢 P2 级共性问题

---

#### 12. 相对密度继承问题（热处理态自动复制制备态密度）

**覆盖文件：** 王卓_01（T6 态密度不应自动继承制备态）、王卓_03

**问题描述：**
Pipeline 对热处理后样品自动沿用制备态的 `relative_density_pct`，即便原文未给出热处理后密度。

**根因分析：**
- `extractors.py` 中 `fill_composition_from_normalized` model_validator 无密度继承限制。
- Prompt 规定"Relative_Density_pct must be null when not reported"，但 LLM 在处理派生条目时倾向于继承父条目数值。

---

#### 13. 工艺文本标准化术语不准确

**覆盖文件：** 王卓_03（300°C/1h 被标注为 Solution 应为 Aging/Annealing）、李希海_03（合金命名过于简化）、李希海_04（合金名称过于简化）

**问题描述：**
Pipeline 对热处理工艺名称（固溶/时效/退火）标注有误，合金名称提取也常过于简化。

---

## 二、个例问题（仅见于特定论文）

| 文件 | 问题简述 | 优先级 |
|------|---------|--------|
| 李希海_03 | Arcam 设备的束流电流被错误存入 Laser_Power_W 字段（PBF-EB 应用 Beam_Current_mA） | P0 |
| 李希海_03 | MultiSpot_90 重复条目 | P0（人工问题） |
| 齐洋_02 | Measurement_Method 填入 "Gas atomization"（粉末制备方法≠测量方法） | P1 |
| 齐洋_04 | 样品名义成分中 "other:0.49" 来源不明 | P1 |
| 齐洋_05 | 自然时效条件不精确（25°C/30 days 未提取） | P0 |
| 潘星宇_01 | γ' 体积分数同时存在枝晶干和枝晶间两个值，Pipeline 未区分 | P1 |
| 潘星宇_04 | Zr 元素（核心设计元素）完全遗漏 | P0 |
| 王新田_01 | Gradient_Material 字段误判（微观尺度异质性被标为梯度材料） | P0 |
| 王新田_04 | 位错密度数量级错误（差 1 个数量级） | P0 |
| 王卓_02 | 个例极端：Result B（人工）自身所有核心数值都与原文不符（AI 输出比人工好） | — |
| 王卓_04 | 200W 样品 Precipitate_Volume_Fraction 错误继承了 300W 数据 | P1 |
| 李希海_05 | 粉末循环数据（Table 2 氧含量/Al 含量）及成品件化学成分（Table 3）完全缺失 | P0 |

---

## 三、系统性根因总结

| 类别 | 根因 | 影响问题编号 |
|------|------|-------------|
| **Schema 缺失字段** | `CompositionProperties` 缺 `advanced_quantitative_features` 字段 | 9 |
| **process_category 关键词不完整** | `domain_rules.yaml` 未覆盖 EBM/PBF-EB/Arcam、PM/HIP/挤压 | 2 |
| **Prompt 规则执行不稳定** | LLM 对矩阵枚举/多状态拆分的 Item Definition 执行率低 | 1, 8 |
| **成分处理规则不完整** | Bal./余量计算规则未明确；Nominal vs Measured 识别示例不足 | 5, 7 |
| **参数正则覆盖不足** | `parameter_patterns` 正则只覆盖固定格式，自然语言变体未覆盖 | 3 |
| **数值校验缺失** | 无量级合理性校验、无成分加和校验 | 6 |
| **DOI 提取策略** | 页眉过滤可能误删 DOI，提取规则未指导多处检索 | 4 |
| **继承逻辑缺陷** | 派生条目（热处理态）自动继承父条目的密度/相对密度 | 12 |

---

## 四、改进建议

### 4.1 Schema 层（extractors.py）

1. **补充 `advanced_quantitative_features` 字段**：在 `CompositionProperties` 中添加 `advanced_quantitative_features: Optional[Dict[str, Any]]`，用于存放位错密度、KAM 值、胞状结构尺寸、相体积分数等不在主 schema 的定量微观特征。

2. **增加量级合理性校验**：在 `model_validator` 中对关键数值（`Laser_Power_W` 合理范围 10–10000 W，`Elongation_Total` ≤ 200% 等）增加 warning 标注，而非静默接受。

3. **成分加和后验校验**：在 `fill_composition_from_normalized` 或独立 validator 中，若 `nominal_composition` 数值之和偏离 100 超过 5%，自动在 `composition_note` 中标注 "Sum check failed: X%"。

### 4.2 Prompt 层（extraction_system_template.txt / extraction_user_template.txt）

4. **补充多状态枚举 Example**：增加 Example P："同一合金存在沉积态/8h 时效/48h 时效三个明确状态 → 必须输出三个独立 item，每个有独立 sample_id"。

5. **余量元素计算规则**：在 Composition Extraction 节明确："当成分表将某元素标注为 Bal. 或 balance 时，应以 `round(100 - sum(其他元素), 2)` 计算后填入，而非使用 `other` 字段"。

6. **Nominal vs Measured 区分示例**：增加明确示例："Table 1 标注 'ICP-OES measured' → `measured_composition`；设计公称成分或粉末供应商标称成分 → `nominal_composition`"。

7. **高温属性遍历提示**：在 Properties Extraction 节补充："提取时须枚举原文所有明确的测试温度点（RT、200°C、800°C 等），每个温度点应有独立的 Property 条目"。

8. **Beam_Current_mA 字段说明**：在 Key_Params 规范中补充 `Beam_Current_mA`（PBF-EB 工艺专用）和 `Acceleration_Voltage_kV`，与 Laser_Power_W 并列说明，避免 EBM 参数填入激光字段。

9. **relative_density 继承禁止规则**：明确说明"派生条目（热处理态）的 `relative_density_pct` 若原文未单独给出，应填 null，不得从前驱工艺态继承"。

### 4.3 domain_rules.yaml 层

10. **扩充 EBM/PBF-EB 关键词**：在 `EBM` 类别下增加：`arcam`、`pbf-eb`、`powder bed fusion electron beam`、`electron beam powder bed fusion`、`a2xx`。

11. **新增 Powder_Metallurgy 类别**：增加 `PM` 类别，关键词包含：`hip`、`hot isostatic pressing`、`powder metallurgy`、`isothermal forging`、`extrusion`、`sintering`（需与 SPS 区分）。

12. **新增 LAAM/Laser_Cladding 子类**：在 `AM_DED` 下补充：`laam`、`laser aided additive manufacturing`、`laser cladding`、`laser metal deposition`。

13. **扩充 parameter_patterns 正则**：对 `Laser_Power_W` 等参数增加自然语言变体：`"(?:laser\\s+)?power\\s+of\\s+(\\d+(?:\\.\\d+)?)\\s*W"`、`"(\\d+(?:\\.\\d+)?)\\s*W\\s+laser"`。

### 4.4 后处理/验证层

14. **DOI 多位置检索**：在 `pdf/doi_extractor.py` 中增加对首页版权栏（通常含 `https://doi.org/`）的专项检索，补充 `Received/Accepted/Available online` 行附近的 DOI 扫描。

15. **Gradient_Material 判断标准明确化**：在 `evaluation.yaml` 或 Flagging prompt 中增加检查点："若 `gradient_material=true` 但成分字段均相同，应触发 QA 标注，提示人工核查"。

---

*报告生成时间：2026-04-14*
*覆盖评测文件：25 篇（李希海×5、潘星宇×5、齐洋×5、王新田×5、王卓×5）*
