# Pipeline（Result A）vs 人工（Result B）差距分析报告

> 基于 25 篇评测文件（5 位评审 × 5 篇），仅聚焦 **Result A（Pipeline 输出）** 的问题，对照 Result B（人工修正）提炼共性缺陷与个例，并结合代码根因分析，给出改进建议。
>
> **Phase 2 更新**：已对照全部 25 篇论文的 OCR 原文（`*_final_output.md`）与 Pipeline 提取结果（`*_extraction.json`）进行交叉验证，补充了原文级别的具体证据和新发现的问题。

---

## 一、共性问题（多篇反复出现）

### 🔴 P0 级共性问题

---

#### 1. 样品条目拆分不足 / 漏提取样品

**覆盖文件：** 齐洋_01（目标合金/无Ni对照/铸造态，及沉积态/8h时效/48h时效未拆分）、齐洋_04（LPBF 与 UV-LPBF 未拆分为独立条目）、李希海_02（仅提取 θ=0°，遗漏 θ=45°/θ=90°）、王新田_01（缺少参考文献样品条目）、王新田_04（仅提取热稳定态，缺打印态条目）

**问题描述：**
Pipeline 对"同一合金不同处理状态"或"实验矩阵多行"常常只提取一个代表性条目，导致多处理状态（沉积态/时效/热处理）、多参数水平（激光功率、VED 等）、多角度（θ=0°/45°/90°）等被合并或遗漏。此外对打印态（as-built）与热稳定/退火态作为平行样品时，Pipeline 有时只提取后处理态。

**根因分析：**
- `extraction_system_template.txt` 的 Item Definition 规则写得较完整，但 LLM 在实践中对"同成分+不同处理"的矩阵枚举理解不稳定。
- 当论文用简写符号矩阵（如 S0/S5/S10/S30/S45）定义样品时，LLM 倾向于只抓代表性样品而非逐行输出。
- `process_category` 字段对工艺区分力弱，导致拆分依据不足。

**代码关联：**
- `prompts/extraction_user_template.txt`：Example F/G 有矩阵枚举示例，但缺乏对"时效态/热处理态"链的显式 Example。
- `extractors.py` 的 `CompositionProperties` schema 无显式校验"样品数量下限"。

---

#### 2. process_category 工艺类别错误

**覆盖文件：** 李希海_03（PBF-EB 被错标为 AM_LPBF）、潘星宇_02（Casting 应为 Powder Metallurgy）、王新田_05（全部 5 个样品标为 Unknown，应为 AM_DED/AM_LAAM）、王卓_02（5 个铸锭样品被标为 AM_LPBF，应为 Casting）、齐洋_01（Al-7075 参考样品标为 Casting，应为 Wrought）

**问题描述：**
Pipeline 对制造工艺类别判断错误，常见于：
- 将 Arcam（电子束）误判为 LPBF（激光）——李希海_03 OCR 原文明确写 "electron beam powder bed fusion (PBF-EB)"
- 将粉末冶金（PM/HIP/挤压/等温锻造）误判为铸造——潘星宇_02 OCR 原文明确写 "Powder metallurgy route: hot isostatic pressed, extruded, and isothermally forged"
- 将 LAAM/DED 工艺标为 Unknown——王新田_05 OCR 原文明确写 "laser-aided additive manufacturing (LAAM)"，但 5 个样品全部标为 Unknown
- 将铸造工艺标为 AM_LPBF——王卓_02 论文中 5 个铸锭（ingot #1-#5）用于筛选成分，仅最终粉末化后的 #5-LPBF 样品才是增材制造
- 将变形态（Wrought）标为铸造——齐洋_01 Al-7075 参考合金为变形铝合金

**根因分析：**
- `domain_rules.yaml` 的 `process_category_keywords` 中 `EBM` 关键词列表仅含 `ebm`/`electron beam melting`，未覆盖 `Arcam`、`PBF-EB`、`electron beam powder bed fusion` 等常用表述。
- `Powder_Metallurgy`（PM）完全没有对应类别，HIP/挤压/锻造被错归为 Casting。

**代码关联：**
- `src/knowmat/domain_rules.yaml`：`process_category_keywords.EBM` 需补充同义词；缺 `PM`/`Powder_Metallurgy` 分类。
- `prompts/extraction_system_template.txt`：`process_category` 字段枚举中缺 `EBM`、`PM` 等类别的明确说明。

---

#### 3. 关键工艺参数 Key_Params 缺失或留空

**覆盖文件：** 齐洋_01、齐洋_04（激光功率/扫描速度/层厚/间距全部缺失）、王新田_04（光斑直径、体能量密度未提取）、王新田_01（粉末干燥条件 120°C/4h、制件尺寸 60×15×6 mm 缺失）、潘星宇_02（固溶温度和双级时效参数过于笼统，未提取具体数值）、王卓_03（热处理升温速率 10°C/min 缺失）

**问题描述：**
Pipeline 对工艺参数（`processing_params`）提取覆盖率低，常留空或只提取了部分参数。激光功率、扫描速度、层厚、间距等核心 AM 参数经常全部缺失。

**根因分析：**
- `domain_rules.yaml` 中 `parameter_patterns` 的正则只匹配 `laser power = X W` 或 `P = X W` 这种格式，对 OCR 输出中常见的 `P: 200 W`、`200W`、`power of 200 W` 等写法无法匹配。
- 当参数散落在 Methods 段落而非表格时，LLM 提取率明显下降。

**代码关联：**
- `src/knowmat/domain_rules.yaml`：`parameter_patterns` 正则需扩展覆盖更多自然语言表述。
- `prompts/extraction_system_template.txt`：`Key_Params` 规则中可增加"优先从 Methods/Experimental 节提取参数"的显式提示。

---

#### 4. 名义成分（Nominal_Composition）与实测成分（Measured_Composition）语义混用

**覆盖文件：** 王卓_01（粉末设计成分 vs ICP-OES 实测成分混用）、潘星宇_05（Table 1 标注实测值却填入 Nominal）、王新田_04（粉末 ICP-OES 成分 vs SEM-EDS 成分未区分）、王卓_01（参考文献样品的 Composition_Type 错标为 at%，应为 wt% 或不填）、潘星宇_04（Nominal 与 Measured 填入完全相同数据，OCR 原文仅有一套成分数据，Measured 应为 null）、齐洋_04（HAM-HT Measured_Composition 使用 at% 但 Nominal 使用 wt%，同一样品成分单位不一致）、李希海_03（Nominal 成分标为 wt%，但合金命名 Ti-48Al-2Cr-2Nb 为 at% 体系）

**问题描述：**
Pipeline 经常将粉末/设计成分（Nominal）和加工后实测成分（Measured）混为一谈，或将两者颠倒填入。此外，成分单位（at% vs wt%）的标注有时与原文不一致——当原文 Table 给出 wt% 成分时，Pipeline 有时错填为 at%。

**根因分析：**
- `extraction_system_template.txt` 虽然说明了 Nominal/Measured 的区分，但未给出当"原文同时提供两者"时的优先级判断规则。
- LLM 对"Table 1 标注为实测值（Measured）但放在 Nominal 字段"的分辨较难，尤其是当表格标题模糊时。
- 对参考文献/对照样品的成分单位未二次核实，容易将 wt% 误标为 at%。

**代码关联：**
- `prompts/extraction_system_template.txt`：Composition Extraction 节可补充示例："Table 1 labeled as 'measured/ICP-OES' → `measured_composition`；design/nominal formula → `nominal_composition`"。需额外增加规则："应忠实记录原文的成分单位（at% vs wt%），不得在未明确转换的情况下更改"。

---

#### 5. 核心数据字段数值计算错误

**覆盖文件：** 王新田_04（位错密度数量级错误：2.75 m⁻² 应为 0.16–5.34×10¹⁵ m⁻²，差 15 个数量级——OCR 原文明确写 "the dislocation density from 0.16 to 5.34 × 10^15 m^-2"，Pipeline 丢弃了 ×10^15 指数）、齐洋_03（两步时效 UTS 值 150 MPa 应为 175 MPa）、李希海_02（Ti 成分计算错误：将 Al=48 名义值误当实测值，Ti 计算值偏低）、王卓_04（Hardness_HV = 3.5 GPa——OCR 原文写 "Hardness contour... 2.5 to 4.5 GPa" 来自纳米压痕，非维氏硬度 HV，属性类型与单位均错误）

**问题描述：**
Pipeline 出现数量级错误、数值抄录错误和单位/属性类型错误，如位错密度单位换算错误（差多个数量级）、力学性能数值抄录出错、成分余量计算时错误引用名义值、纳米压痕硬度（GPa）被错标为维氏硬度（HV）。

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

#### 6. 余量元素（Bal.）处理不当

**覆盖文件：** 潘星宇_01（Ni=100.0——OCR Table 1 明确写 "Bal."，实际 Ni≈62 wt%）、潘星宇_02（ME3 合金 `"other": 0.1` 为虚构值；LSHR 的 Ni 被计算为 50.895）、潘星宇_03（`"other"` 字段含 Hf+Ni 余量混合）、潘星宇_04（Ni 被存入 `"other": 61.03/59.57`，应显式标注为 Ni）、潘星宇_05（`"other": 28.0` 对应 OCR 中 "Co+Cr+W+Mo=28" 的粗略汇总，丢失元素明细）、王卓_01（Al 余量存入 `"other": 94.2`，应为 Al=Bal.）、齐洋_01（Gong-benchmark 合金 `"other": 94.38` 为 Al 余量）

**问题描述：**
Pipeline 对合金中"余量"元素（通常是 Ni、Al 或 Ti）处理策略不一致：有时填 100.0、有时填 `other`、有时将余量元素名存入 `other` 字段值、有时留空，而非计算实际余量值。OCR 原文交叉验证确认此问题涉及至少 7 篇论文。

**根因分析：**
- `extraction_system_template.txt` 规则："If sum < 100 and no explicit balance element is given, you may add `other`"，但未规定"已知余量元素时应计算填入实际值"。
- LLM 对"Bal."的处理缺乏统一策略，`other` 字段语义不清。

**代码关联：**
- `prompts/extraction_system_template.txt`：增加规则："当成分表中明确某元素为 Bal./余量时，应以 100 减去其余元素之和计算填入，而非填 100.0 或 `other`"。

---

#### 7. 高温力学性能数据漏提取

**覆盖文件：** 齐洋_02（高温 UTS/蠕变大面积缺失——OCR Table S3 有 RT~400°C 完整数据）、齐洋_03（200°C 延伸率/蠕变寿命遗漏）、王新田_05（中间合金 x=0.1/0.2/0.3/0.4 的 UTS 以及 x=0.4 的 YS 缺失——OCR Table S1 有完整数据）、潘星宇_01（Paper 测试 5 个蠕变条件但仅提取 1030°C/230MPa 一条）、潘星宇_03（**ALL 4 samples Properties_Info 为空——OCR 中有 750°C/455MPa 蠕变数据完全未提取，P0 级遗漏**）、潘星宇_04（蠕变数据仅提取 1 条，65 和 85 MPa 条件下数据缺失）、王新田_04（Yield_Strength 未提取——OCR 补充数据中有 YS≈730 MPa）

**问题描述：**
Pipeline 对高温测试数据（蠕变寿命、高温 UTS/YS、应变速率敏感系数）提取覆盖率不足，尤其当数据散落在图表而非文本段落时。同样，在多成分系列实验中（如 x=0~0.5 合金系列），Pipeline 常只提取端点和峰值，漏提中间成分的属性数据。

**根因分析：**
- `properties_of_composition` schema 中虽有 `test_temperature_k` 字段，但 LLM 对"图表数据"（data_source=image）的提取积极性低。
- Prompt 中 Properties 提取规则未明确要求"遍历所有测试温度"。
- 多成分系列中 LLM 倾向于只提取论文重点讨论的端点样品，忽略中间成分的完整数据。

**代码关联：**
- `prompts/extraction_system_template.txt`：可增加"Properties 提取时须枚举所有明确的测试温度点"的指导，以及"多成分系列须对每个成分/参数水平提取完整属性"。

---

#### 8. 微观结构定量参数未结构化提取

**覆盖文件：** 王新田_01（微观尺度异质性误判为 Gradient_Material；内/壁区域体积分数未入 AdvFeat）、王新田_02（KAM 值/胞状结构尺寸/晶格失配建议入 Advanced_Quantitative_Features）、王新田_03（FCC/B2 体积分数/层片厚度/层片粗化参数未入 Advanced_Quantitative_Features；Advanced_Quantitative_Features 整体为空）、王卓_03（双模晶粒结构取单一综合平均值，掩盖等轴晶/柱状晶的独立尺寸信息）、李希海_01（O 相晶粒尺寸未提取）

**问题描述：**
Pipeline 对 EBSD/TEM/APT 等定量微观结构参数（位错密度、晶格失配、相体积分数、胞状结构尺寸等）提取不完整，或将其错误放入 `Properties_Info` 而非 `Advanced_Quantitative_Features`。特别地，当合金具有双模或多模晶粒结构（等轴晶+柱状晶）时，Pipeline 倾向于取单一综合平均值，丢失了双模分布信息。

**根因分析：**
- `CompositionProperties` schema 中 `Advanced_Quantitative_Features` 字段在 `extractors.py` 中未定义（schema 缺失该字段），导致 LLM 即便想填也无处存放。
- Prompt 虽提及 `Advanced_Quantitative_Features`，但 Pydantic schema 中无对应字段。
- 对"双模晶粒分布"没有专门的提取规则，LLM 默认取单一平均值。

**代码关联：**
- `src/knowmat/extractors.py`：`CompositionProperties` 类缺少 `advanced_quantitative_features: Optional[Dict[str, Any]]` 字段。
- `prompts/extraction_system_template.txt`：需在输出格式（Output Format）中补充该字段的 JSON 示例；并增加规则："当原文报告了等轴晶和柱状晶的独立尺寸时，不得取综合平均值，应分别记录于 Advanced_Quantitative_Features"。

---

#### 9. 参考文献对照材料（Reference 条目）未提取

**覆盖文件：** 李希海_01（Table 6 文献对比数据未提取）、李希海_04（铸造参考样品未提取）、王新田_01（应提取参考文献材料数据）、王新田_04（可提取参考文献数据）

**问题描述：**
Pipeline 对原文中用于对比的文献数据（reference alloys）几乎不提取，导致数据库缺少比较基准。

**根因分析：**
- Prompt 规定了 `role: Reference`，但 LLM 默认只提取 Target 材料，对"论文中引用的对比数据"的识别率低。
- `extraction_user_template.txt` 的 Example H（"comparison-route retention"）说明了保留逻辑，但实际执行中 LLM 执行率不稳定。

---

#### 10. Main_Phase 缺失或填充不准确

**覆盖文件：** 王新田_02（时效态 Main_Phase 应为 "FCC + L12"）、潘星宇_04（H230AM 析出相错误填入 Main_Phase）

**问题描述：**
Pipeline 对主相标识存在缺失或错误，如将时效后双相结构只标注单相，或将析出相（ZrC）混入主相。

**根因分析：**
- `main_phase` 字段的 schema 描述限定"不得使用 Laves/carbides/gamma-prime 作为主相"，但对双相或多相基体的标注规则（如 "FCC + L12"）未明确。

---

### 🟢 P2 级共性问题

---

#### 11. 相对密度继承问题（热处理态自动复制制备态密度）

**覆盖文件：** 王卓_01（T6 态密度不应自动继承制备态）、王卓_03

**问题描述：**
Pipeline 对热处理后样品自动沿用制备态的 `relative_density_pct`，即便原文未给出热处理后密度。

**根因分析：**
- `extractors.py` 中 `fill_composition_from_normalized` model_validator 无密度继承限制。
- Prompt 规定"Relative_Density_pct must be null when not reported"，但 LLM 在处理派生条目时倾向于继承父条目数值。

---

#### 12. 工艺文本标准化术语不准确

**覆盖文件：** 王卓_03（300°C/1h 被标注为 Solution_Temperature，应为退火/时效 Annealing）、李希海_03（合金命名过于简化）、李希海_04（合金名称过于简化）

**问题描述：**
Pipeline 对热处理工艺名称（固溶/时效/退火）标注有误，常将低温退火/时效处理误标为固溶处理（Solution），合金名称提取也常过于简化。

---

## 二、个例问题（仅见于特定论文）

| 文件 | 问题简述 | 优先级 |
|------|---------|--------|
| 李希海_02 | Ti 成分余量计算错误：将 Al=48（名义值）误当实测值参与计算，导致 Ti 偏低约 2 个百分点 | P1 |
| 李希海_03 | Arcam 设备的束流电流被错误存入 Laser_Power_W 字段（PBF-EB 应用 Beam_Current_mA） | P0 |
| 李希海_05 | 粉末循环数据（Table 2 氧含量/Al 含量）及成品件化学成分（Table 3）完全缺失 | P0 |
| 齐洋_01 | 峰值拉伸强度 395 MPa 误归入 Reference 样品（应属时效 8h 样品）；L1₂ 面积分数 17% 未提取 | P1 |
| 齐洋_02 | Measurement_Method 填入 "Gas atomization"（粉末制备方法≠测量方法） | P1 |
| 齐洋_04 | 样品名义成分中 "other:0.49" 来源不明；UV-LPBF 相对密度与常规 LPBF 数据交叉赋值 | P1 |
| 齐洋_05 | 成分严重简化：Cu/Mg/B 等关键元素被合并为 "other:1.5"；自然时效条件 25°C/30 days 未提取 | P0 |
| 潘星宇_01 | γ' 体积分数同时存在枝晶干和枝晶间两个值，Pipeline 未区分 | P1 |
| 潘星宇_03 | 晶粒尺寸 750 μm 来源存疑（OCR 文本中未找到该数值，可能为幻觉） | P1 |
| 潘星宇_04 | H230AM 热处理条件错误（应为 1200°C/1h+空冷）；析出相错误（ZrC 应为 M₆C）；Zr 元素完全遗漏；蠕变寿命（1500h@45MPa）未提取 | P0 |
| 王新田_01 | Gradient_Material 字段误判（微观尺度内/壁异质性被标为梯度材料=true，应为 false） | P0 |
| 王新田_03 | 退火态 UEL 标准差来源不明（直接照用打印态 ±0.3，原文对退火态未明确给出标准差） | P1 |
| 王卓_01 | 参考文献样品 Composition_Type 错标为 at%（原文 Table 1 所有成分均为 wt%） | P0 |
| 王卓_02 | 个例注意：Result A 核心数值与原文完全一致，是本次评测中提取质量最好的案例之一 | — |
| 王卓_04 | 200W 样品 Precipitate_Volume_Fraction 错误继承了 300W 数据（应填 null） | P1 |
| **以下为 Phase 2 原文交叉验证新增** | | |
| 李希海_02 | Measured_Composition 中 `"other": 2.276` 为虚构——OCR 原文分别列出 C/O/N 各元素值，不应合并为 other | P1 |
| 李希海_03 | Key_Params `"Laser_Power_W": 25` 应为 `"Beam_Current_mA": 25`——OCR 明确为电子束工艺参数 | P0 |
| 李希海_04 | Nominal_Composition `"other": 8.0`（Ti-44Al-4Cr 合金）——应为 Ti=52(Bal.)，other 字段语义错误 | P1 |
| 潘星宇_02 | ME3 合金 `"other": 0.1` 在 OCR Table 1 中无来源，属 LLM 幻觉 | P1 |
| 潘星宇_05 | Process_Category 对测试条件标为 "HeatTreat"——基体材料为 AM_DED，HeatTreat 仅为后处理 | P1 |
| 齐洋_03 | Creep_Minimum_Strain_Rate = 0.0——OCR 写 "near-zero secondary creep rates"，应标注为"低于测量阈值"而非精确 0.0 | P1 |
| 王卓_03 | Key_Params `"Solution_Temperature_K": 573.15`（=300°C）——OCR 明确为退火/时效温度，非固溶处理 | P1 |
| 王卓_04 | Hardness 标为 "HV" 但值为 3.5 GPa——OCR 明确为纳米压痕硬度，非维氏硬度，属性类型错误 | P1 |
| 王新田_03 | As-Annealed Process_Category 标为 "HeatTreat"——基体为 AM_LPBF (PBF-LB)，应注明基础工艺 | P2 |
| 王新田_05 | x=0.4 合金条目完全缺失——OCR Table S1 有该成分数据 | P0 |

---

## 三、Result A 与 Result B 共同弱点（双方均存在的系统性不足）

> 以下问题并非 Pipeline 特有，人工修正（Result B）同样存在，反映了当前 schema 设计或评测规范的系统性盲区。

| 弱点类别 | 描述 | 涉及文件 |
|---------|------|---------|
| **蠕变完整条件缺失** | 蠕变实验的完整条件列表（应力/温度组合矩阵）均未逐行提取，仅保留部分数据点 | 潘星宇_01/02/03/04 |
| **APT/STEM 定量数据缺失** | 原子探针（APT）分析给出的相成分、晶界偏聚等定量结果，双方均未系统提取 | 齐洋_01/03、潘星宇_02/03/04 |
| **强化机制定量分解缺失** | 文献中计算或测量的各强化贡献（Hall-Petch/Orowan/固溶强化等分量）双方均漏提 | 齐洋_01/03/04/05 |
| **图表数据（image）覆盖不足** | 仅存在于图而非文字/表格的性能曲线数据（如图表中读取的 YS、加工硬化率），双方提取率均低 | 王新田_05、齐洋多篇 |
| **相组成演变/反应动力学缺失** | 热处理过程中相变序列、各相体积分数随温度/时间演变的定量数据均未提取 | 李希海_05、潘星宇系列 |
| **粒径分布（D10/D50/D90）缺失** | 粉末粒径分布参数普遍缺失，仅部分提取了平均粒径 | 李希海_05 |
| **热处理参数的次要细节遗漏** | 升温速率、保护气氛等热处理次要参数普遍未提取 | 王卓_03、潘星宇系列 |

---

## 四、Phase 2 原文交叉验证：逐篇 OCR vs Extraction JSON 关键发现

> 以下基于全部 25 篇论文的 OCR 原文（`*_final_output.md`）与 Pipeline 提取结果（`*_extraction.json`）逐一比对，列出每篇论文中发现的关键问题。已归入共性问题或个例问题表的不再重复描述，仅列出补充发现。

### 4.1 李希海（增材制造 TiAl）

| 论文 | 发现 | 严重度 |
|------|------|--------|
| 李希海_01 | OCR 编码问题导致无法完整读取原文（Windows 编码），但 extraction JSON 中 O 相晶粒尺寸未提取已在共性问题 #8 覆盖 | — |
| 李希海_02 | 仅提取 θ=0° 样品，θ=45°/θ=90° 完全遗漏（共性 #1）；RT 延伸率未提取；`"other": 2.276` 为 C/O/N 合并值（不应合并） | P0/P1 |
| 李希海_03 | 3 个样品全标 AM_LPBF 但实为 PBF-EB（共性 #2）；Beam_Current 误存 Laser_Power（个例）；Nominal 标 wt% 但合金命名为 at% 体系 | P0 |
| 李希海_04 | Nominal `"other": 8.0` 应为 Ti=Bal.=52 at%（共性 #6 变体）；铸造参考样品未提取（共性 #9） | P1 |
| 李希海_05 | 粉末循环 Table 2/3 完全缺失（个例）；Phase 2 确认 OCR 中这些 Table 内容存在但 LLM 未提取 | P0 |

### 4.2 潘星宇（高温合金）

| 论文 | 发现 | 严重度 |
|------|------|--------|
| 潘星宇_01 | Ni=100.0 应为≈62 wt%（共性 #6）；OCR 确认 5 个蠕变条件仅提取 1 条 | P1 |
| 潘星宇_02 | Process_Category "Casting" 应为 "Powder_Metallurgy"（共性 #2，OCR 确认）；ME3 `"other": 0.1` 为幻觉 | P0 |
| 潘星宇_03 | **所有 4 个样品 Properties_Info 为空**——OCR 明确有 750°C/455MPa 蠕变数据。这是 Phase 2 最严重的新发现之一 | **P0** |
| 潘星宇_04 | Ni 存入 `"other"` 而非显式标注（共性 #6）；Nominal 与 Measured 填入相同值，Measured 应为 null；缺 65/85 MPa 蠕变数据 | P1 |
| 潘星宇_05 | `"other": 28.0` 对应 OCR "Co+Cr+W+Mo=28" 是有损汇总；HeatTreat 标签掩盖了 AM_DED 基础工艺 | P1 |

### 4.3 齐洋（增材铝合金）

| 论文 | 发现 | 严重度 |
|------|------|--------|
| 齐洋_01 | Al-7075 参考合金标为 "Casting" 应为 "Wrought"（共性 #2）；Gong-benchmark `"other": 94.38` 为 Al 余量（共性 #6） | P1 |
| 齐洋_02 | OCR Table S3 有 RT~400°C 完整机械性能数据，高温数据仅部分提取；蠕变速率 300°C/100-150MPa 数据待验证 | P1 |
| 齐洋_03 | Creep_Minimum_Strain_Rate=0.0——OCR 写 "near-zero"/"no measurable"，0.0 近似正确但应标注为低于阈值 | P1 |
| 齐洋_04 | HAM-HT Measured 用 at% 但 Nominal 用 wt%（共性 #4）；Key_Params 缺 Laser_Power/Scanning_Speed（在 Supplementary Table S1） | P1 |
| 齐洋_05 | AA2024 baseline Properties_Info 为空——OCR 表明 AA2024 有严重裂纹（4.698% 缺陷率），可能无法测试力学性能，此处留空**可接受** | — |

### 4.4 王新田（增材高熵合金）

| 论文 | 发现 | 严重度 |
|------|------|--------|
| 王新田_01 | HT-HEA Process_Category "HeatTreat" 掩盖了 AM_DED 基础工艺；Relative_Density 99.999% 经 OCR 确认正确 | P2 |
| 王新田_02 | 无拉伸力学性能——OCR 确认论文为腐蚀研究，仅有电化学数据，Properties 留空**合理** | — |
| 王新田_03 | As-Annealed Process_Category "HeatTreat" 应注明基础工艺 PBF-LB（共性 #2 变体）；Nominal `"other": 0.01` 为归一化误差 | P2 |
| 王新田_04 | 位错密度 2.75 m⁻² 丢弃 ×10¹⁵ 指数（共性 #5，OCR 确认）；缺 YS（OCR 补充材料有 YS≈730 MPa） | P0 |
| 王新田_05 | **全部 5 样品 Process_Category "Unknown"** 应为 AM_DED/AM_LAAM（共性 #2，OCR 确认）；x=0.4 合金条目完全缺失；部分样品缺 Elongation | P0 |

### 4.5 王卓（增材铝合金）

| 论文 | 发现 | 严重度 |
|------|------|--------|
| 王卓_01 | Al 余量存入 `"other": 94.2`（共性 #6）；参考样品 Composition_Type 错标 at%（个例） | P1 |
| 王卓_02 | **5 个铸锭样品全标 AM_LPBF**——OCR 确认为铸造+激光熔覆筛选，仅 #5-LPBF 为增材（共性 #2，Phase 2 最严重新发现之一） | **P0** |
| 王卓_03 | Key_Params Solution_Temperature_K=573.15 实为退火温度（个例）；HT 条目 Process_Category 应注明 AM_LPBF 基础工艺 | P1 |
| 王卓_04 | Hardness "HV"=3.5 GPa 实为纳米压痕硬度（共性 #5）；200W Precipitate_Volume_Fraction 错误继承（个例） | P1 |
| 王卓_05 | CL vs PL LPBF 数据提取较完整，孔隙率数据正确；Phase 2 未发现重大新问题 | — |

### 4.6 Phase 2 新增/升级的共性问题汇总

| 编号 | 问题 | Phase 1 状态 | Phase 2 变化 |
|------|------|-------------|-------------|
| #2 | Process_Category 错误 | 2 篇 | **升级至 5+ 篇**（新增王新田_05 全 5 样品 Unknown、王卓_02 全 5 铸锭标 AM_LPBF、齐洋_01 Wrought→Casting） |
| #4 | Nominal/Measured 混用 | 4 篇 | **升级至 7 篇**（新增潘星宇_04、齐洋_04、李希海_03 单位问题） |
| #5 | 数值计算错误 | 3 篇 | **升级至 4 篇**（新增王卓_04 硬度单位/类型错误） |
| #6 | Bal. 处理不当 | 4 篇 | **升级至 7+ 篇**（新增潘星宇_05、王卓_01、齐洋_01） |
| #7 | 高温/蠕变数据漏提取 | 4 篇 | **升级至 7+ 篇**（新增潘星宇_01/03/04、王新田_04） |
| NEW | 潘星宇_03 全部 Properties 为空 | — | **新增 P0**——最严重的数据完整性问题 |
| NEW | 后处理态 Process_Category 标注不完整 | — | **新增 P2**——HeatTreat 标签掩盖 AM 基础工艺（王新田_01/03、潘星宇_05） |

---

## 五、系统性根因总结

| 类别 | 根因 | 影响问题编号 |
|------|------|-------------|
| **Schema 缺失字段** | `CompositionProperties` 缺 `advanced_quantitative_features` 字段 | 8 |
| **process_category 关键词不完整** | `domain_rules.yaml` 未覆盖 EBM/PBF-EB/Arcam、PM/HIP/挤压 | 2 |
| **Prompt 规则执行不稳定** | LLM 对矩阵枚举/多状态拆分的 Item Definition 执行率低 | 1, 7 |
| **成分处理规则不完整** | Bal./余量计算规则未明确；Nominal vs Measured 识别示例不足；at%/wt% 忠实记录缺规定 | 4, 6 |
| **参数正则覆盖不足** | `parameter_patterns` 正则只覆盖固定格式，自然语言变体未覆盖 | 3 |
| **数值校验缺失** | 无量级合理性校验、无成分加和校验；×10^n 格式数量级错误无后处理拦截 | 5 |
| **继承逻辑缺陷** | 派生条目（热处理态）自动继承父条目的密度；跨功率条目 Precipitate_Volume_Fraction 继承 | 11 |
| **双模结构表示缺规则** | 无针对"等轴晶+柱状晶双模"多模分布的专项提取规则，LLM 默认取均值 | 8 |
| **LAAM/DED 关键词未覆盖** | `domain_rules.yaml` 未覆盖 `laam`/`laser aided additive manufacturing`，导致 LAAM 工艺被标为 Unknown | 2（王新田_05） |
| **非 AM 工艺（铸造/锻造）识别能力不足** | LLM 对论文中出现的铸锭筛选步骤误判为增材制造，缺乏"铸造→增材"工艺链的识别逻辑 | 2（王卓_02） |
| **Properties 提取对蠕变/creep 数据的覆盖率极低** | 当蠕变数据仅在 Results 段落或图表中出现而非独立表格时，LLM 几乎不提取 | 7（潘星宇_03 全空） |
| **后处理态 Process_Category 标注逻辑缺失** | 当样品为 AM+热处理时，仅标 "HeatTreat" 丢失了基础 AM 工艺信息 | 2 变体 |

---

## 六、改进建议

### 6.1 Schema 层（extractors.py）

1. **补充 `advanced_quantitative_features` 字段**：在 `CompositionProperties` 中添加 `advanced_quantitative_features: Optional[Dict[str, Any]]`，用于存放位错密度、KAM 值、胞状结构尺寸、相体积分数等不在主 schema 的定量微观特征。

2. **增加量级合理性校验**：在 `model_validator` 中对关键数值（`Laser_Power_W` 合理范围 10–10000 W，`Elongation_Total` ≤ 200% 等）增加 warning 标注，而非静默接受。

3. **成分加和后验校验**：在 `fill_composition_from_normalized` 或独立 validator 中，若 `nominal_composition` 数值之和偏离 100 超过 5%，自动在 `composition_note` 中标注 "Sum check failed: X%"。

### 6.2 Prompt 层（extraction_system_template.txt / extraction_user_template.txt）

4. **补充多状态枚举 Example**：增加 Example P："同一合金存在沉积态/8h 时效/48h 时效三个明确状态 → 必须输出三个独立 item，每个有独立 sample_id"。

5. **余量元素计算规则**：在 Composition Extraction 节明确："当成分表将某元素标注为 Bal. 或 balance 时，应以 `round(100 - sum(其他元素), 2)` 计算后填入，而非使用 `other` 字段"。

6. **Nominal vs Measured 区分示例**：增加明确示例："Table 1 标注 'ICP-OES measured' → `measured_composition`；设计公称成分或粉末供应商标称成分 → `nominal_composition`"。

7. **高温属性遍历提示**：在 Properties Extraction 节补充："提取时须枚举原文所有明确的测试温度点（RT、200°C、800°C 等），每个温度点应有独立的 Property 条目"。

8. **Beam_Current_mA 字段说明**：在 Key_Params 规范中补充 `Beam_Current_mA`（PBF-EB 工艺专用）和 `Acceleration_Voltage_kV`，与 Laser_Power_W 并列说明，避免 EBM 参数填入激光字段。

9. **relative_density 继承禁止规则**：明确说明"派生条目（热处理态）的 `relative_density_pct` 若原文未单独给出，应填 null，不得从前驱工艺态继承"。

### 6.3 domain_rules.yaml 层

10. **扩充 EBM/PBF-EB 关键词**：在 `EBM` 类别下增加：`arcam`、`pbf-eb`、`powder bed fusion electron beam`、`electron beam powder bed fusion`、`a2xx`。

11. **新增 Powder_Metallurgy 类别**：增加 `PM` 类别，关键词包含：`hip`、`hot isostatic pressing`、`powder metallurgy`、`isothermal forging`、`extrusion`、`sintering`（需与 SPS 区分）。

12. **新增 LAAM/Laser_Cladding 子类**：在 `AM_DED` 下补充：`laam`、`laser aided additive manufacturing`、`laser cladding`、`laser metal deposition`。

13. **扩充 parameter_patterns 正则**：对 `Laser_Power_W` 等参数增加自然语言变体：`"(?:laser\\s+)?power\\s+of\\s+(\\d+(?:\\.\\d+)?)\\s*W"`、`"(\\d+(?:\\.\\d+)?)\\s*W\\s+laser"`。

### 6.4 后处理/验证层

14. **Gradient_Material 判断标准明确化**：在 `evaluation.yaml` 或 Flagging prompt 中增加检查点："若 `gradient_material=true` 但成分字段均相同，应触发 QA 标注，提示人工核查"。

15. **双模晶粒结构提取规则**：在 Prompt 或 schema 中增加："当原文同时报告了等轴晶和柱状晶尺寸（或 FG/CG 区域尺寸）时，应分别记录于 Advanced_Quantitative_Features，不得取综合平均值作为单一 Grain_Size_avg_um"。

16. **成分单位（at%/wt%）忠实记录**：在 Composition Extraction 节增加明确规则："应忠实记录原文的成分单位，不得在未注明转换过程的情况下擅自将 wt% 改为 at% 或反之"。

17. **参考文献成分填充保守策略**：增加规则："当参考文献样品的原始论文未在本文中提供成分数据时，Composition_Type 不应填入；若需记录，应在 Note 中注明 '来源于参考文献，单位未在本文明确' "。

### 6.5 Phase 2 新增改进建议

18. **Process_Category 复合标注支持**：当样品为"AM 制造 + 后续热处理"时，建议 schema 支持 `base_process_category`（如 AM_DED）和 `post_process`（如 HeatTreat）两个字段，避免仅标 HeatTreat 丢失基础工艺信息。涉及：王新田_01/03、潘星宇_05 等。

19. **Properties_Info 非空校验**：在后处理层增加检查——若论文明确包含力学/蠕变测试数据（可通过 OCR 文本中关键词 "tensile"/"creep"/"stress-strain" 判断），但所有样品 Properties_Info 均为空，应触发 QA 告警。涉及：潘星宇_03（4 个样品全空）。

20. **科学计数法 ×10^n 专项解析**：在 `_coerce_numeric_leaf` 中增加对 `X × 10^Y`、`X×10^Y`、`X E+Y` 格式的专项解析逻辑，确保指数部分不被丢弃。涉及：王新田_04 位错密度差 15 个数量级。

21. **硬度属性类型细化**：在 schema 中区分 Vickers Hardness (HV)、Nanoindentation Hardness (GPa)、Rockwell Hardness (HRC) 等不同硬度类型，避免将纳米压痕 GPa 值错标为 HV。涉及：王卓_04。

22. **LAAM/Laser Cladding 等 DED 变体识别**：在 `domain_rules.yaml` 的 AM_DED 关键词中补充 `laam`、`laser-aided additive manufacturing`、`laser aided additive manufacturing`，确保 LAAM 工艺不被标为 Unknown。涉及：王新田_05 全部 5 样品。

23. **铸造筛选 vs 增材制造的工艺链识别**：在 Prompt 中增加规则："当论文中存在铸造筛选→粉末化→增材制造的多步工艺链时，铸锭筛选阶段的样品应标为 Casting，仅最终增材制造的样品标为 AM_LPBF/AM_DED"。涉及：王卓_02（5 个铸锭误标 AM_LPBF）。

24. **`other` 字段语义限制**：在 Prompt 中明确规则："`other` 字段仅用于表示'成分表中未逐一列出的微量杂质总和'，不得用于存放已知余量元素（Ni/Al/Ti 的 Bal.）、多个已知元素的汇总值、或任何可以显式标注元素名的成分"。涉及：潘星宇_04 Ni→other、潘星宇_05 Co+Cr+W+Mo→other、王卓_01 Al→other。

---

*报告生成时间：2026-04-14*
*最后更新：2026-04-14（Phase 2 原文交叉验证完成，整合全部 25 篇评测文件 + 25 篇 OCR 原文 + 25 篇 extraction JSON）*
*覆盖评测文件：25 篇（李希海×5、潘星宇×5、齐洋×5、王新田×5、王卓×5）*
*覆盖原文数据：25 篇 OCR 原文 + 25 篇 Pipeline extraction JSON（24/25 OCR 成功读取，李希海_01 有编码问题）*
