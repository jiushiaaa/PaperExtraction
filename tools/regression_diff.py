"""
KnowMat 回归测试工具

对比 AI 抽取结果与手工标注的 ground truth，计算关键指标差异，
生成可读报告用于验证 prompt/schema 优化效果。

Usage:
    python tools/regression_diff.py --all
    python tools/regression_diff.py --papers 1 2 3
    python tools/regression_diff.py --all --format json --output reports/result.json
"""

import argparse
import json
import re
import sys
import shutil
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional, Tuple
from collections import defaultdict

# 设置控制台输出编码为 UTF-8（Windows 兼容）
if sys.platform == "win32":
    try:
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    except AttributeError:
        import codecs
        sys.stdout = codecs.getwriter("utf-8")(sys.stdout.buffer, "strict")
        sys.stderr = codecs.getwriter("utf-8")(sys.stderr.buffer, "strict")


class RegressionDiff:
    """回归对比工具核心类"""
    
    def __init__(self, workspace_root: Path):
        self.workspace_root = workspace_root
        self.ai_results_dir = workspace_root / "data" / "processed"
        self.gt_results_dir = workspace_root / "手工标注结果"
        self.reports_dir = workspace_root / "reports"
        self.reports_dir.mkdir(exist_ok=True)
        
    def find_ai_extraction(self, paper_id: int) -> Optional[Path]:
        """根据论文编号查找 AI 抽取结果文件"""
        pattern = f"{paper_id}-*"
        matching_dirs = list(self.ai_results_dir.glob(pattern))
        
        if not matching_dirs:
            return None
        
        # 在匹配的目录中查找 _extraction.json
        for dir_path in matching_dirs:
            extraction_files = list(dir_path.glob("*_extraction.json"))
            if extraction_files:
                return extraction_files[0]
        
        return None
    
    def find_gt_data(self, paper_id: int) -> Optional[Path]:
        """根据论文编号查找手工标注文件"""
        gt_file = self.gt_results_dir / f"{paper_id}-data.json"
        return gt_file if gt_file.exists() else None
    
    def load_json(self, path: Path) -> dict:
        """加载 JSON 文件"""
        try:
            with open(path, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception as e:
            print(f"[ERROR] Failed to load {path}: {e}")
            return {}
    
    def compare_paper(self, paper_id: int) -> Optional[Dict]:
        """对比单篇论文的 AI 结果和手工标注"""
        ai_path = self.find_ai_extraction(paper_id)
        gt_path = self.find_gt_data(paper_id)
        
        if not ai_path or not gt_path:
            print(f"[SKIP] Paper {paper_id}: AI={ai_path}, GT={gt_path}")
            return None
        
        ai_data = self.load_json(ai_path)
        gt_data = self.load_json(gt_path)
        
        if not ai_data or not gt_data:
            return None
        
        print(f"[COMPARE] Paper {paper_id}: {ai_path.name} vs {gt_path.name}")
        
        # 提取 Materials 列表
        ai_materials = ai_data.get("Materials", [])
        gt_materials = gt_data.get("Materials", [])
        
        # 计算各项指标
        result = {
            "paper_id": paper_id,
            "ai_file": str(ai_path.relative_to(self.workspace_root)),
            "gt_file": str(gt_path.relative_to(self.workspace_root)),
            "structure": self._compare_structure(ai_materials, gt_materials),
            "doi": self._compare_doi(ai_materials, gt_materials),
            "phases": self._compare_phases(ai_materials, gt_materials),
            "precipitates": self._compare_precipitates(ai_materials, gt_materials),
            "process_categories": self._compare_process_categories(ai_materials, gt_materials),
            "grain_sizes": self._compare_grain_sizes(ai_materials, gt_materials),
            "temperatures": self._compare_temperatures(ai_materials, gt_materials),
            "compositions": self._compare_compositions(ai_materials, gt_materials),
        }
        
        return result
    
    def _compare_structure(self, ai_materials: List, gt_materials: List) -> Dict:
        """对比结构指标：Material/Sample/Property 数量"""
        ai_samples = [s for m in ai_materials for s in m.get("Processed_Samples", [])]
        gt_samples = [s for m in gt_materials for s in m.get("Processed_Samples", [])]
        
        ai_properties = [t for s in ai_samples for t in s.get("Performance_Tests", [])]
        gt_properties = [t for s in gt_samples for t in s.get("Performance_Tests", [])]
        
        return {
            "materials": {"ai": len(ai_materials), "gt": len(gt_materials)},
            "samples": {"ai": len(ai_samples), "gt": len(gt_samples)},
            "properties": {"ai": len(ai_properties), "gt": len(gt_properties)},
        }
    
    def _compare_doi(self, ai_materials: List, gt_materials: List) -> Dict:
        """对比 DOI 字段"""
        ai_doi = ai_materials[0].get("Source_DOI", "") if ai_materials else ""
        gt_doi = gt_materials[0].get("Source_DOI", "") if gt_materials else ""
        
        # 标准化（去空格、转小写）
        ai_doi_norm = ai_doi.strip().lower()
        gt_doi_norm = gt_doi.strip().lower()
        
        match = ai_doi_norm == gt_doi_norm and gt_doi_norm != ""
        
        return {
            "ai": ai_doi,
            "gt": gt_doi,
            "match": match,
        }
    
    def _compare_phases(self, ai_materials: List, gt_materials: List) -> Dict:
        """对比 Main_Phase 字段（Sample 级）"""
        ai_samples = [s for m in ai_materials for s in m.get("Processed_Samples", [])]
        gt_samples = [s for m in gt_materials for s in m.get("Processed_Samples", [])]
        
        ai_phases = [s.get("Main_Phase", "") for s in ai_samples]
        gt_phases = [s.get("Main_Phase", "") for s in gt_samples]
        
        ai_filled = sum(1 for p in ai_phases if p)
        gt_filled = sum(1 for p in gt_phases if p)
        
        # 简单匹配：只要 AI 和 GT 的非空 phase 数量一致且值相同
        matches = 0
        for ai_p, gt_p in zip(ai_phases, gt_phases):
            if gt_p and ai_p:
                # 支持部分匹配（BCC 包含在 "BCC + sigma" 中）
                if gt_p.lower() in ai_p.lower() or ai_p.lower() in gt_p.lower():
                    matches += 1
        
        return {
            "ai_filled_count": ai_filled,
            "gt_filled_count": gt_filled,
            "matches": matches,
            "ai_filled_rate": ai_filled / len(ai_samples) if ai_samples else 0,
            "gt_filled_rate": gt_filled / len(gt_samples) if gt_samples else 0,
            "match_rate": matches / gt_filled if gt_filled else 0,
        }
    
    def _compare_precipitates(self, ai_materials: List, gt_materials: List) -> Dict:
        """对比 Has_Precipitates 字段（Sample 级）"""
        ai_samples = [s for m in ai_materials for s in m.get("Processed_Samples", [])]
        gt_samples = [s for m in gt_materials for s in m.get("Processed_Samples", [])]
        
        ai_precip = [s.get("Has_Precipitates", False) for s in ai_samples]
        gt_precip = [s.get("Has_Precipitates", False) for s in gt_samples]
        
        matches = sum(1 for ai_p, gt_p in zip(ai_precip, gt_precip) if ai_p == gt_p)
        
        return {
            "ai_true_count": sum(ai_precip),
            "gt_true_count": sum(gt_precip),
            "matches": matches,
            "match_rate": matches / len(gt_samples) if gt_samples else 0,
        }
    
    def _compare_process_categories(self, ai_materials: List, gt_materials: List) -> Dict:
        """对比 Process_Category 字段（Sample 级）"""
        ai_samples = [s for m in ai_materials for s in m.get("Processed_Samples", [])]
        gt_samples = [s for m in gt_materials for s in m.get("Processed_Samples", [])]
        
        ai_cats = [s.get("Process_Category", "Unknown") for s in ai_samples]
        gt_cats = [s.get("Process_Category", "Unknown") for s in gt_samples]
        
        # 别名映射
        aliases = {
            "AM_SLM": ["AM_LPBF", "LPBF"],
            "AM_LPBF": ["AM_SLM", "LPBF"],
            "LPBF": ["AM_SLM", "AM_LPBF"],
        }
        
        matches = 0
        for ai_cat, gt_cat in zip(ai_cats, gt_cats):
            if ai_cat == gt_cat:
                matches += 1
            elif gt_cat in aliases.get(ai_cat, []) or ai_cat in aliases.get(gt_cat, []):
                matches += 0.5  # 部分匹配
        
        ai_unknown = sum(1 for c in ai_cats if c == "Unknown")
        gt_unknown = sum(1 for c in gt_cats if c == "Unknown")
        
        return {
            "ai_unknown_count": ai_unknown,
            "gt_unknown_count": gt_unknown,
            "matches": matches,
            "match_rate": matches / len(gt_samples) if gt_samples else 0,
        }
    
    def _compare_grain_sizes(self, ai_materials: List, gt_materials: List) -> Dict:
        """对比 Grain_Size_avg_um 字段"""
        ai_samples = [s for m in ai_materials for s in m.get("Processed_Samples", [])]
        gt_samples = [s for m in gt_materials for s in m.get("Processed_Samples", [])]
        
        ai_sizes = [s.get("Grain_Size_avg_um") for s in ai_samples]
        gt_sizes = [s.get("Grain_Size_avg_um") for s in gt_samples]
        
        ai_filled = sum(1 for g in ai_sizes if g is not None)
        gt_filled = sum(1 for g in gt_sizes if g is not None)
        
        return {
            "ai_filled_count": ai_filled,
            "gt_filled_count": gt_filled,
            "ai_filled_rate": ai_filled / len(ai_samples) if ai_samples else 0,
            "gt_filled_rate": gt_filled / len(gt_samples) if gt_samples else 0,
        }
    
    def _compare_temperatures(self, ai_materials: List, gt_materials: List) -> Dict:
        """对比测试温度（Performance_Tests 级）"""
        ai_samples = [s for m in ai_materials for s in m.get("Processed_Samples", [])]
        gt_samples = [s for m in gt_materials for s in m.get("Processed_Samples", [])]
        
        ai_tests = [t for s in ai_samples for t in s.get("Performance_Tests", [])]
        gt_tests = [t for s in gt_samples for t in s.get("Performance_Tests", [])]
        
        ai_temps = [t.get("Test_Temperature_K") for t in ai_tests]
        gt_temps = [t.get("Test_Temperature_K") for t in gt_tests]
        
        # 计算偏移（只对比相同索引位置的测试）
        offsets = []
        for ai_t, gt_t in zip(ai_temps, gt_temps):
            if ai_t is not None and gt_t is not None:
                offsets.append(abs(ai_t - gt_t))
        
        ai_filled = sum(1 for t in ai_temps if t is not None)
        gt_filled = sum(1 for t in gt_temps if t is not None)
        
        return {
            "ai_filled_count": ai_filled,
            "gt_filled_count": gt_filled,
            "offsets": offsets,
            "mean_offset_K": sum(offsets) / len(offsets) if offsets else 0,
            "max_offset_K": max(offsets) if offsets else 0,
            "tests_with_offset": sum(1 for o in offsets if o > 1),  # 超过 1K 视为偏移
        }
    
    def _compare_compositions(self, ai_materials: List, gt_materials: List) -> Dict:
        """对比 Composition_JSON 字段"""
        issues = []
        
        for ai_mat in ai_materials:
            comp_json = ai_mat.get("Composition_JSON", {})
            formula = ai_mat.get("Formula_Normalized", "")
            
            # 检查非法元素
            valid_elements = {
                "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
                "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
                "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
                "Ga", "Ge", "As", "Se", "Br", "Kr",
                "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd",
                "In", "Sn", "Sb", "Te", "I", "Xe",
                "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy",
                "Ho", "Er", "Tm", "Yb", "Lu",
                "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi",
            }
            
            invalid_elements = [e for e in comp_json.keys() if e not in valid_elements]
            if invalid_elements:
                issues.append(f"{formula}: Invalid elements {invalid_elements}")
            
            # 检查原子百分比和
            if comp_json:
                total = sum(comp_json.values())
                if abs(total - 100) > 2:
                    issues.append(f"{formula}: Sum={total:.1f}% (expected ~100%)")
            
            # 检查是否为空
            if not comp_json and formula:
                issues.append(f"{formula}: Composition_JSON is empty")
        
        return {
            "invalid_elements_count": sum(1 for i in issues if "Invalid elements" in i),
            "sum_issues_count": sum(1 for i in issues if "Sum=" in i),
            "empty_count": sum(1 for i in issues if "is empty" in i),
            "issues": issues,
        }
    
    def compare_all(self, paper_ids: List[int]) -> Dict:
        """对比所有指定的论文，返回汇总结果"""
        results = []
        
        for paper_id in paper_ids:
            result = self.compare_paper(paper_id)
            if result:
                results.append(result)
        
        if not results:
            return {"error": "No valid comparisons"}
        
        # 汇总统计
        summary = self._aggregate_results(results)
        
        return {
            "timestamp": datetime.now().isoformat(),
            "papers_compared": len(results),
            "papers_total": len(paper_ids),
            "summary": summary,
            "details": results,
        }
    
    def _aggregate_results(self, results: List[Dict]) -> Dict:
        """汇总所有论文的指标"""
        n = len(results)
        
        # 结构指标
        avg_materials_ai = sum(r["structure"]["materials"]["ai"] for r in results) / n
        avg_materials_gt = sum(r["structure"]["materials"]["gt"] for r in results) / n
        avg_samples_ai = sum(r["structure"]["samples"]["ai"] for r in results) / n
        avg_samples_gt = sum(r["structure"]["samples"]["gt"] for r in results) / n
        avg_props_ai = sum(r["structure"]["properties"]["ai"] for r in results) / n
        avg_props_gt = sum(r["structure"]["properties"]["gt"] for r in results) / n
        
        # DOI 命中率
        doi_matches = sum(1 for r in results if r["doi"]["match"])
        doi_hit_rate = doi_matches / n
        
        # Phase 填充率和准确率
        phase_ai_filled_rate = sum(r["phases"]["ai_filled_rate"] for r in results) / n
        phase_gt_filled_rate = sum(r["phases"]["gt_filled_rate"] for r in results) / n
        phase_match_rate = sum(r["phases"]["match_rate"] for r in results) / n
        
        # Precipitates 准确率
        precip_match_rate = sum(r["precipitates"]["match_rate"] for r in results) / n
        
        # Process_Category 准确率
        process_match_rate = sum(r["process_categories"]["match_rate"] for r in results) / n
        process_unknown_ai = sum(r["process_categories"]["ai_unknown_count"] for r in results)
        total_samples_ai = sum(r["structure"]["samples"]["ai"] for r in results)
        process_unknown_rate = process_unknown_ai / total_samples_ai if total_samples_ai else 0
        
        # Grain_Size 填充率
        grain_ai_filled_rate = sum(r["grain_sizes"]["ai_filled_rate"] for r in results) / n
        grain_gt_filled_rate = sum(r["grain_sizes"]["gt_filled_rate"] for r in results) / n
        
        # 温度偏移
        temp_mean_offset = sum(r["temperatures"]["mean_offset_K"] for r in results) / n
        temp_max_offset = max(r["temperatures"]["max_offset_K"] for r in results)
        temp_tests_with_offset = sum(r["temperatures"]["tests_with_offset"] for r in results)
        
        # 成分问题
        comp_invalid = sum(r["compositions"]["invalid_elements_count"] for r in results)
        comp_sum_issues = sum(r["compositions"]["sum_issues_count"] for r in results)
        comp_empty = sum(r["compositions"]["empty_count"] for r in results)
        
        return {
            "structure": {
                "materials_per_paper": {"ai": round(avg_materials_ai, 2), "gt": round(avg_materials_gt, 2)},
                "samples_per_paper": {"ai": round(avg_samples_ai, 2), "gt": round(avg_samples_gt, 2)},
                "properties_per_paper": {"ai": round(avg_props_ai, 1), "gt": round(avg_props_gt, 1)},
            },
            "field_accuracy": {
                "doi_hit_rate": round(doi_hit_rate, 3),
                "main_phase_ai_filled_rate": round(phase_ai_filled_rate, 3),
                "main_phase_match_rate": round(phase_match_rate, 3),
                "has_precipitates_match_rate": round(precip_match_rate, 3),
                "process_category_match_rate": round(process_match_rate, 3),
                "process_unknown_rate": round(process_unknown_rate, 3),
                "grain_size_ai_filled_rate": round(grain_ai_filled_rate, 3),
                "grain_size_gt_filled_rate": round(grain_gt_filled_rate, 3),
            },
            "temperature": {
                "mean_offset_K": round(temp_mean_offset, 3),
                "max_offset_K": round(temp_max_offset, 3),
                "tests_with_offset": temp_tests_with_offset,
            },
            "composition_quality": {
                "papers_with_invalid_elements": comp_invalid,
                "papers_with_sum_issues": comp_sum_issues,
                "papers_with_empty_composition": comp_empty,
            },
        }
    
    def generate_markdown_report(self, comparison_result: Dict, output_path: Path):
        """生成 Markdown 格式的可读报告"""
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("# KnowMat 回归测试报告\n\n")
            f.write(f"**生成时间**: {comparison_result['timestamp']}\n\n")
            f.write(f"**对比论文数**: {comparison_result['papers_compared']}/{comparison_result['papers_total']}\n\n")
            f.write("---\n\n")
            
            # 总体指标
            summary = comparison_result["summary"]
            f.write("## 总体指标\n\n")
            
            # 结构指标表
            f.write("### 结构指标\n\n")
            f.write("| 指标 | AI 均值 | GT 均值 | AI/GT 比率 |\n")
            f.write("|------|---------|---------|------------|\n")
            
            struct = summary["structure"]
            f.write(f"| Materials per paper | {struct['materials_per_paper']['ai']} | {struct['materials_per_paper']['gt']} | {struct['materials_per_paper']['ai']/struct['materials_per_paper']['gt']:.1%} |\n")
            f.write(f"| Samples per paper | {struct['samples_per_paper']['ai']} | {struct['samples_per_paper']['gt']} | {struct['samples_per_paper']['ai']/struct['samples_per_paper']['gt']:.1%} |\n")
            f.write(f"| Properties per paper | {struct['properties_per_paper']['ai']} | {struct['properties_per_paper']['gt']} | {struct['properties_per_paper']['ai']/struct['properties_per_paper']['gt']:.1%} |\n")
            f.write("\n")
            
            # 字段准确率表
            f.write("### 字段准确率\n\n")
            f.write("| 字段 | 指标 | 数值 | 评价 |\n")
            f.write("|------|------|------|------|\n")
            
            acc = summary["field_accuracy"]
            f.write(f"| DOI | 命中率 | {acc['doi_hit_rate']:.1%} | {'✅' if acc['doi_hit_rate'] >= 0.8 else '❌'} |\n")
            f.write(f"| Main_Phase | AI 填充率 | {acc['main_phase_ai_filled_rate']:.1%} | {'✅' if acc['main_phase_ai_filled_rate'] >= 0.7 else '❌'} |\n")
            f.write(f"| Main_Phase | 匹配率 | {acc['main_phase_match_rate']:.1%} | {'✅' if acc['main_phase_match_rate'] >= 0.7 else '❌'} |\n")
            f.write(f"| Has_Precipitates | 匹配率 | {acc['has_precipitates_match_rate']:.1%} | {'✅' if acc['has_precipitates_match_rate'] >= 0.7 else '❌'} |\n")
            f.write(f"| Process_Category | 匹配率 | {acc['process_category_match_rate']:.1%} | {'✅' if acc['process_category_match_rate'] >= 0.85 else '❌'} |\n")
            f.write(f"| Process_Category | Unknown 占比 | {acc['process_unknown_rate']:.1%} | {'✅' if acc['process_unknown_rate'] < 0.15 else '❌'} |\n")
            f.write(f"| Grain_Size | AI 填充率 | {acc['grain_size_ai_filled_rate']:.1%} | {'✅' if acc['grain_size_ai_filled_rate'] >= 0.5 else '❌'} |\n")
            f.write("\n")
            
            # 温度质量
            f.write("### 温度质量\n\n")
            temp = summary["temperature"]
            f.write(f"- **平均偏移**: {temp['mean_offset_K']:.2f} K\n")
            f.write(f"- **最大偏移**: {temp['max_offset_K']:.2f} K\n")
            f.write(f"- **偏移测试数** (>1K): {temp['tests_with_offset']}\n")
            f.write(f"- **评价**: {'✅ 无显著偏移' if temp['mean_offset_K'] < 0.5 else '❌ 存在偏移'}\n\n")
            
            # 成分质量
            f.write("### 成分质量\n\n")
            comp = summary["composition_quality"]
            f.write(f"- **非法元素问题**: {comp['papers_with_invalid_elements']} 篇\n")
            f.write(f"- **原子百分比和异常**: {comp['papers_with_sum_issues']} 篇\n")
            f.write(f"- **Composition_JSON 为空**: {comp['papers_with_empty_composition']} 篇\n")
            f.write(f"- **评价**: {'✅ 成分解析质量良好' if comp['papers_with_invalid_elements'] == 0 else '❌ 存在成分解析问题'}\n\n")
            
            f.write("---\n\n")
            
            # 逐篇详情
            f.write("## 逐篇对比详情\n\n")
            
            for result in comparison_result["details"]:
                paper_id = result["paper_id"]
                f.write(f"### 论文 {paper_id}\n\n")
                f.write(f"**AI 文件**: `{result['ai_file']}`\n\n")
                f.write(f"**GT 文件**: `{result['gt_file']}`\n\n")
                
                # 结构
                struct = result["structure"]
                f.write(f"- **Materials**: AI={struct['materials']['ai']}, GT={struct['materials']['gt']} {'✅' if struct['materials']['ai'] == struct['materials']['gt'] else '⚠️'}\n")
                f.write(f"- **Samples**: AI={struct['samples']['ai']}, GT={struct['samples']['gt']} {'✅' if struct['samples']['ai'] == struct['samples']['gt'] else '⚠️'}\n")
                f.write(f"- **Properties**: AI={struct['properties']['ai']}, GT={struct['properties']['gt']} {'✅' if struct['properties']['ai'] >= struct['properties']['gt'] * 0.8 else '⚠️'}\n")
                
                # DOI
                doi = result["doi"]
                doi_status = '✅ 匹配' if doi['match'] else f'❌ AI="{doi["ai"]}" vs GT="{doi["gt"]}"'
                f.write(f"- **DOI**: {doi_status}\n")
                
                # Phase
                phases = result["phases"]
                f.write(f"- **Main_Phase**: AI填充={phases['ai_filled_count']}/{struct['samples']['ai']}, 匹配率={phases['match_rate']:.1%} {'✅' if phases['match_rate'] >= 0.7 else '❌'}\n")
                
                # Precipitates
                precip = result["precipitates"]
                f.write(f"- **Has_Precipitates**: 匹配率={precip['match_rate']:.1%} {'✅' if precip['match_rate'] >= 0.7 else '❌'}\n")
                
                # Process
                process = result["process_categories"]
                f.write(f"- **Process_Category**: 匹配率={process['match_rate']:.1%}, Unknown={process['ai_unknown_count']}/{struct['samples']['ai']} {'✅' if process['match_rate'] >= 0.85 else '❌'}\n")
                
                # Temperature
                temp = result["temperatures"]
                f.write(f"- **温度偏移**: 平均={temp['mean_offset_K']:.2f}K, 最大={temp['max_offset_K']:.2f}K {'✅' if temp['mean_offset_K'] < 0.5 else '❌'}\n")
                
                # Composition
                comp = result["compositions"]
                if comp["issues"]:
                    f.write(f"- **成分问题**: ❌\n")
                    for issue in comp["issues"][:3]:  # 只显示前3个
                        f.write(f"  - {issue}\n")
                else:
                    f.write(f"- **成分问题**: ✅ 无问题\n")
                
                f.write("\n")
            
            f.write("---\n\n")
            f.write("*报告生成工具: KnowMat regression_diff.py*\n")
    
    def generate_json_report(self, comparison_result: Dict, output_path: Path):
        """生成 JSON 格式的机器可读报告"""
        with open(output_path, "w", encoding="utf-8") as f:
            json.dump(comparison_result, f, ensure_ascii=False, indent=2)


class SelfRegression:
    """自回归对比工具：Run vs Run"""
    
    def __init__(self, workspace_root: Path):
        self.workspace_root = workspace_root
        self.processed_dir = workspace_root / "data" / "processed"
        self.snapshots_dir = workspace_root / "reports" / "snapshots"
        self.snapshots_dir.mkdir(parents=True, exist_ok=True)
    
    def list_snapshots(self):
        """列出所有快照"""
        snapshots = [d for d in self.snapshots_dir.iterdir() if d.is_dir()]
        
        if not snapshots:
            print("没有找到任何快照")
            return
        
        print(f"可用快照列表（共 {len(snapshots)} 个）：")
        print("=" * 60)
        
        for snapshot in sorted(snapshots):
            meta_file = snapshot / "snapshot_meta.json"
            if meta_file.exists():
                with open(meta_file, "r", encoding="utf-8") as f:
                    meta = json.load(f)
                papers_count = meta.get("papers_count", 0)
                timestamp = meta.get("timestamp", "Unknown")
                print(f"  - {snapshot.name:20s}  ({papers_count} 篇论文, {timestamp})")
            else:
                print(f"  - {snapshot.name:20s}  (元信息缺失)")
        print("=" * 60)
    
    def create_snapshot(self, snapshot_name: str):
        """创建快照"""
        snapshot_dir = self.snapshots_dir / snapshot_name
        
        if snapshot_dir.exists():
            response = input(f"快照 '{snapshot_name}' 已存在，是否覆盖？(y/N): ")
            if response.lower() != 'y':
                print("已取消")
                return
            shutil.rmtree(snapshot_dir)
        
        snapshot_dir.mkdir(parents=True, exist_ok=True)
        
        # 查找所有 _extraction.json 文件
        extraction_files = list(self.processed_dir.glob("*/*_extraction.json"))
        
        if not extraction_files:
            print("错误：未找到任何 extraction.json 文件")
            return
        
        print(f"正在创建快照 '{snapshot_name}'...")
        papers_copied = []
        
        for src_file in extraction_files:
            paper_name = src_file.stem.replace("_extraction", "")
            dest_file = snapshot_dir / f"{paper_name}.json"
            shutil.copy2(src_file, dest_file)
            papers_copied.append(paper_name)
            print(f"  已复制: {paper_name}")
        
        # 写入元信息
        meta = {
            "snapshot_name": snapshot_name,
            "timestamp": datetime.now().isoformat(),
            "papers_count": len(papers_copied),
            "papers": papers_copied,
        }
        
        meta_file = snapshot_dir / "snapshot_meta.json"
        with open(meta_file, "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
        
        print(f"\n✅ 快照已创建: {snapshot_dir}")
        print(f"   包含 {len(papers_copied)} 篇论文")
    
    def compare_with_snapshot(self, snapshot_name: str, format_type: str, output_path: Optional[str]):
        """与快照对比"""
        snapshot_dir = self.snapshots_dir / snapshot_name
        
        if not snapshot_dir.exists():
            print(f"错误：快照 '{snapshot_name}' 不存在")
            self.list_snapshots()
            return
        
        # 读取快照元信息
        meta_file = snapshot_dir / "snapshot_meta.json"
        if not meta_file.exists():
            print("错误：快照元信息缺失")
            return
        
        with open(meta_file, "r", encoding="utf-8") as f:
            meta = json.load(f)
        
        print(f"[Self 模式] 对比快照: {snapshot_name}")
        print(f"快照创建时间: {meta.get('timestamp', 'Unknown')}")
        print("=" * 60)
        
        # 对比每篇论文
        results = []
        snapshot_files = list(snapshot_dir.glob("*.json"))
        snapshot_files = [f for f in snapshot_files if f.name != "snapshot_meta.json"]
        
        for snapshot_file in snapshot_files:
            paper_name = snapshot_file.stem
            result = self._compare_paper(paper_name, snapshot_file)
            if result:
                results.append(result)
        
        if not results:
            print("没有找到可对比的论文")
            return
        
        # 汇总结果
        comparison_result = {
            "timestamp": datetime.now().isoformat(),
            "snapshot_name": snapshot_name,
            "snapshot_time": meta.get("timestamp"),
            "papers_compared": len(results),
            "summary": self._aggregate_self_results(results),
            "details": results,
        }
        
        # 生成报告
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if output_path:
            base_path = Path(output_path)
        else:
            base_path = self.workspace_root / "reports" / f"self_regression_{timestamp}"
        
        if format_type in ["markdown", "both"]:
            md_path = base_path.with_suffix(".md")
            self._generate_markdown_report(comparison_result, md_path)
            print(f"\n✅ Markdown 报告已生成: {md_path}")
        
        if format_type in ["json", "both"]:
            json_path = base_path.with_suffix(".json")
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(comparison_result, f, ensure_ascii=False, indent=2)
            print(f"✅ JSON 报告已生成: {json_path}")
        
        # 控制台摘要
        self._print_summary(comparison_result["summary"])
    
    def _compare_paper(self, paper_name: str, snapshot_file: Path) -> Optional[Dict]:
        """对比单篇论文的两次运行结果"""
        # 查找当前的 extraction.json
        current_candidates = list(self.processed_dir.glob(f"*{paper_name}*/*_extraction.json"))
        
        if not current_candidates:
            print(f"[SKIP] {paper_name}: 未找到当前结果")
            return None
        
        current_file = current_candidates[0]
        
        # 加载两个版本
        with open(snapshot_file, "r", encoding="utf-8") as f:
            snapshot_data = json.load(f)
        
        with open(current_file, "r", encoding="utf-8") as f:
            current_data = json.load(f)
        
        print(f"[COMPARE] {paper_name}")
        
        # 提取数据
        snap_materials = snapshot_data.get("Materials", [])
        curr_materials = current_data.get("Materials", [])
        
        snap_samples = [s for m in snap_materials for s in m.get("Processed_Samples", [])]
        curr_samples = [s for m in curr_materials for s in m.get("Processed_Samples", [])]
        
        snap_props = [t for s in snap_samples for t in s.get("Performance_Tests", [])]
        curr_props = [t for s in curr_samples for t in s.get("Performance_Tests", [])]
        
        # 计算变化
        return {
            "paper_name": paper_name,
            "materials": {
                "snapshot": len(snap_materials),
                "current": len(curr_materials),
                "delta": len(curr_materials) - len(snap_materials)
            },
            "samples": {
                "snapshot": len(snap_samples),
                "current": len(curr_samples),
                "delta": len(curr_samples) - len(snap_samples)
            },
            "properties": {
                "snapshot": len(snap_props),
                "current": len(curr_props),
                "delta": len(curr_props) - len(snap_props)
            },
            "doi": self._compare_doi(snap_materials, curr_materials),
            "phase_filled": self._compare_phase_filled(snap_samples, curr_samples),
            "process_unknown": self._compare_process_unknown(snap_samples, curr_samples),
        }
    
    def _compare_doi(self, snap_materials: List, curr_materials: List) -> Dict:
        """对比 DOI 变化"""
        snap_doi = snap_materials[0].get("Source_DOI", "") if snap_materials else ""
        curr_doi = curr_materials[0].get("Source_DOI", "") if curr_materials else ""
        
        if not snap_doi and curr_doi:
            status = "新增"
        elif snap_doi and not curr_doi:
            status = "丢失"
        elif snap_doi == curr_doi:
            status = "不变"
        else:
            status = "变更"
        
        return {
            "snapshot": snap_doi,
            "current": curr_doi,
            "status": status
        }
    
    def _compare_phase_filled(self, snap_samples: List, curr_samples: List) -> Dict:
        """对比 Phase 填充率变化"""
        snap_filled = sum(1 for s in snap_samples if s.get("Main_Phase"))
        curr_filled = sum(1 for s in curr_samples if s.get("Main_Phase"))
        
        snap_rate = snap_filled / len(snap_samples) if snap_samples else 0
        curr_rate = curr_filled / len(curr_samples) if curr_samples else 0
        
        return {
            "snapshot_rate": round(snap_rate, 3),
            "current_rate": round(curr_rate, 3),
            "delta": round(curr_rate - snap_rate, 3)
        }
    
    def _compare_process_unknown(self, snap_samples: List, curr_samples: List) -> Dict:
        """对比 Process Unknown 率变化"""
        snap_unknown = sum(1 for s in snap_samples if s.get("Process_Category") == "Unknown")
        curr_unknown = sum(1 for s in curr_samples if s.get("Process_Category") == "Unknown")
        
        snap_rate = snap_unknown / len(snap_samples) if snap_samples else 0
        curr_rate = curr_unknown / len(curr_samples) if curr_samples else 0
        
        return {
            "snapshot_rate": round(snap_rate, 3),
            "current_rate": round(curr_rate, 3),
            "delta": round(curr_rate - snap_rate, 3)
        }
    
    def _aggregate_self_results(self, results: List[Dict]) -> Dict:
        """汇总自回归结果"""
        n = len(results)
        
        # 统计改善/恶化/不变的论文数
        improved = sum(1 for r in results if r["properties"]["delta"] > 0 or (
            r["doi"]["status"] == "新增" and r["properties"]["delta"] >= 0
        ))
        degraded = sum(1 for r in results if r["properties"]["delta"] < 0 or (
            r["doi"]["status"] == "丢失" and r["properties"]["delta"] <= 0
        ))
        unchanged = n - improved - degraded
        
        return {
            "papers_improved": improved,
            "papers_degraded": degraded,
            "papers_unchanged": unchanged,
            "avg_materials_delta": sum(r["materials"]["delta"] for r in results) / n,
            "avg_samples_delta": sum(r["samples"]["delta"] for r in results) / n,
            "avg_properties_delta": sum(r["properties"]["delta"] for r in results) / n,
            "avg_phase_filled_delta": sum(r["phase_filled"]["delta"] for r in results) / n,
            "avg_process_unknown_delta": sum(r["process_unknown"]["delta"] for r in results) / n,
        }
    
    def _generate_markdown_report(self, comparison_result: Dict, output_path: Path):
        """生成 Markdown 报告"""
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("# KnowMat 自回归测试报告 (Run vs Run)\n\n")
            f.write(f"**对比快照**: {comparison_result['snapshot_name']}\n\n")
            f.write(f"**快照时间**: {comparison_result['snapshot_time']}\n\n")
            f.write(f"**当前时间**: {comparison_result['timestamp']}\n\n")
            f.write(f"**对比论文数**: {comparison_result['papers_compared']}\n\n")
            f.write("---\n\n")
            
            summary = comparison_result["summary"]
            f.write("## 总体变化\n\n")
            f.write("| 指标 | 改善 | 恶化 | 不变 |\n")
            f.write("|------|------|------|------|\n")
            f.write(f"| 论文数 | {summary['papers_improved']} | {summary['papers_degraded']} | {summary['papers_unchanged']} |\n\n")
            
            f.write("| 指标 | 平均变化 | 趋势 |\n")
            f.write("|------|----------|------|\n")
            f.write(f"| Materials 数量 | {summary['avg_materials_delta']:+.2f} | {'📈' if summary['avg_materials_delta'] > 0 else '📉' if summary['avg_materials_delta'] < 0 else '➡️'} |\n")
            f.write(f"| Samples 数量 | {summary['avg_samples_delta']:+.2f} | {'📈' if summary['avg_samples_delta'] > 0 else '📉' if summary['avg_samples_delta'] < 0 else '➡️'} |\n")
            f.write(f"| Properties 数量 | {summary['avg_properties_delta']:+.2f} | {'📈' if summary['avg_properties_delta'] > 0 else '📉' if summary['avg_properties_delta'] < 0 else '➡️'} |\n")
            f.write(f"| Phase 填充率 | {summary['avg_phase_filled_delta']:+.3f} | {'📈' if summary['avg_phase_filled_delta'] > 0 else '📉' if summary['avg_phase_filled_delta'] < 0 else '➡️'} |\n")
            f.write(f"| Process Unknown 率 | {summary['avg_process_unknown_delta']:+.3f} | {'📉' if summary['avg_process_unknown_delta'] < 0 else '📈' if summary['avg_process_unknown_delta'] > 0 else '➡️'} |\n\n")
            
            f.write("---\n\n")
            f.write("## 逐篇详情\n\n")
            
            for result in comparison_result["details"]:
                f.write(f"### {result['paper_name']}\n\n")
                
                # 材料/样品/属性变化
                mat_delta = result["materials"]["delta"]
                sam_delta = result["samples"]["delta"]
                pro_delta = result["properties"]["delta"]
                
                f.write(f"- **Materials**: {result['materials']['snapshot']} → {result['materials']['current']} ({mat_delta:+d})\n")
                f.write(f"- **Samples**: {result['samples']['snapshot']} → {result['samples']['current']} ({sam_delta:+d})\n")
                f.write(f"- **Properties**: {result['properties']['snapshot']} → {result['properties']['current']} ({pro_delta:+d})\n")
                
                # DOI 变化
                doi_status = result["doi"]["status"]
                doi_emoji = {"新增": "✅", "丢失": "❌", "不变": "➡️", "变更": "🔄"}
                f.write(f"- **DOI**: {doi_emoji.get(doi_status, '')} {doi_status}\n")
                
                # Phase/Process 变化
                phase_delta = result["phase_filled"]["delta"]
                process_delta = result["process_unknown"]["delta"]
                f.write(f"- **Phase 填充率**: {result['phase_filled']['snapshot_rate']:.1%} → {result['phase_filled']['current_rate']:.1%} ({phase_delta:+.3f})\n")
                f.write(f"- **Process Unknown 率**: {result['process_unknown']['snapshot_rate']:.1%} → {result['process_unknown']['current_rate']:.1%} ({process_delta:+.3f})\n")
                
                f.write("\n")
            
            f.write("---\n\n")
            f.write("*报告生成工具: KnowMat regression_diff.py (self mode)*\n")
    
    def _print_summary(self, summary: Dict):
        """打印控制台摘要"""
        print("\n" + "=" * 60)
        print("自回归测试摘要")
        print("=" * 60)
        
        print(f"\n📊 论文变化统计:")
        print(f"  改善: {summary['papers_improved']} 篇")
        print(f"  恶化: {summary['papers_degraded']} 篇")
        print(f"  不变: {summary['papers_unchanged']} 篇")
        
        print(f"\n📈 平均变化:")
        print(f"  Materials:  {summary['avg_materials_delta']:+.2f}")
        print(f"  Samples:    {summary['avg_samples_delta']:+.2f}")
        print(f"  Properties: {summary['avg_properties_delta']:+.2f}")
        print(f"  Phase 填充率: {summary['avg_phase_filled_delta']:+.3f}")
        print(f"  Process Unknown 率: {summary['avg_process_unknown_delta']:+.3f} {'✅' if summary['avg_process_unknown_delta'] < 0 else '⚠️'}")
        
        print("\n" + "=" * 60)


class QABaseline:
    """质量基线检查工具：无需 GT"""
    
    def __init__(self, workspace_root: Path):
        self.workspace_root = workspace_root
        self.processed_dir = workspace_root / "data" / "processed"
        self.reports_dir = workspace_root / "reports"
        self.reports_dir.mkdir(exist_ok=True)
        
        # 有效元素集合
        self.VALID_ELEMENTS = {
            "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne",
            "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
            "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn",
            "Ga", "Ge", "As", "Se", "Br", "Kr",
            "Rb", "Sr", "Y", "Zr", "Nb", "Mo", "Tc", "Ru", "Rh", "Pd", "Ag", "Cd",
            "In", "Sn", "Sb", "Te", "I", "Xe",
            "Cs", "Ba", "La", "Ce", "Pr", "Nd", "Pm", "Sm", "Eu", "Gd", "Tb", "Dy",
            "Ho", "Er", "Tm", "Yb", "Lu",
            "Hf", "Ta", "W", "Re", "Os", "Ir", "Pt", "Au", "Hg", "Tl", "Pb", "Bi",
        }
    
    def scan_and_report(self, paper_ids: Optional[List[int]], format_type: str, output_path: Optional[str]):
        """扫描所有论文并生成质量报告"""
        print("[QA 模式] 扫描论文质量指标")
        print("=" * 60)
        
        # 查找所有 extraction.json 文件
        extraction_files = list(self.processed_dir.glob("*/*_extraction.json"))
        
        if not extraction_files:
            print("错误：未找到任何 extraction.json 文件")
            return
        
        # 如果指定了论文编号，过滤
        if paper_ids:
            extraction_files = [
                f for f in extraction_files
                if any(f.parent.name.startswith(f"{pid}-") for pid in paper_ids)
            ]
        
        if not extraction_files:
            print("错误：未找到匹配的论文")
            return
        
        # 分析每篇论文
        results = []
        for extraction_file in extraction_files:
            result = self._analyze_paper(extraction_file)
            if result:
                results.append(result)
        
        if not results:
            print("没有找到可分析的论文")
            return
        
        # 汇总结果
        qa_result = {
            "timestamp": datetime.now().isoformat(),
            "papers_scanned": len(results),
            "summary": self._aggregate_qa_results(results),
            "details": sorted(results, key=lambda x: x["quality_score"]),  # 按质量得分排序
        }
        
        # 生成报告
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        
        if output_path:
            base_path = Path(output_path)
        else:
            base_path = self.reports_dir / f"qa_baseline_{timestamp}"
        
        if format_type in ["markdown", "both"]:
            md_path = base_path.with_suffix(".md")
            self._generate_markdown_report(qa_result, md_path)
            print(f"\n✅ Markdown 报告已生成: {md_path}")
        
        if format_type in ["json", "both"]:
            json_path = base_path.with_suffix(".json")
            with open(json_path, "w", encoding="utf-8") as f:
                json.dump(qa_result, f, ensure_ascii=False, indent=2)
            print(f"✅ JSON 报告已生成: {json_path}")
        
        # 控制台摘要
        self._print_summary(qa_result)
    
    def _analyze_paper(self, extraction_file: Path) -> Optional[Dict]:
        """分析单篇论文的质量指标"""
        paper_name = extraction_file.parent.name
        print(f"[SCAN] {paper_name}")
        
        try:
            with open(extraction_file, "r", encoding="utf-8") as f:
                data = json.load(f)
        except Exception as e:
            print(f"  [ERROR] 加载失败: {e}")
            return None
        
        materials = data.get("Materials", [])
        samples = [s for m in materials for s in m.get("Processed_Samples", [])]
        properties = [t for s in samples for t in s.get("Performance_Tests", [])]
        
        # 计算各项指标
        materials_count = len(materials)
        samples_count = len(samples)
        properties_count = len(properties)
        
        # DOI
        doi_present = bool(materials and materials[0].get("Source_DOI"))
        
        # Phase 填充率
        phase_filled = sum(1 for s in samples if s.get("Main_Phase"))
        phase_filled_rate = phase_filled / samples_count if samples_count else 0
        
        # Process Unknown 率
        process_unknown = sum(1 for s in samples if s.get("Process_Category") == "Unknown")
        process_unknown_rate = process_unknown / samples_count if samples_count else 0
        
        # Grain Size 填充率
        grain_filled = sum(1 for s in samples if s.get("Grain_Size_avg_um") is not None)
        grain_filled_rate = grain_filled / samples_count if samples_count else 0
        
        # Composition 有效率
        comp_valid, comp_total = self._check_composition_quality(materials)
        composition_valid_rate = comp_valid / comp_total if comp_total else 0
        
        # 红线告警
        red_lines = []
        if materials_count == 0:
            red_lines.append("NO_MATERIALS")
        if properties_count == 0:
            red_lines.append("NO_PROPERTIES")
        if process_unknown_rate > 0.5:
            red_lines.append("HIGH_UNKNOWN_PROCESS")
        if composition_valid_rate < 0.5 and comp_total > 0:
            red_lines.append("LOW_COMPOSITION_QUALITY")
        
        # 计算质量得分（0-100）
        quality_score = self._calculate_quality_score(
            materials_count, properties_count, doi_present,
            phase_filled_rate, process_unknown_rate, composition_valid_rate
        )
        
        return {
            "paper_name": paper_name,
            "materials_count": materials_count,
            "samples_count": samples_count,
            "properties_count": properties_count,
            "doi_present": doi_present,
            "phase_filled_rate": round(phase_filled_rate, 3),
            "process_unknown_rate": round(process_unknown_rate, 3),
            "grain_filled_rate": round(grain_filled_rate, 3),
            "composition_valid_rate": round(composition_valid_rate, 3),
            "red_lines": red_lines,
            "needs_review": len(red_lines) > 0,
            "quality_score": quality_score,
        }
    
    def _check_composition_quality(self, materials: List) -> Tuple[int, int]:
        """检查成分 JSON 质量"""
        valid_count = 0
        total_count = 0
        
        for mat in materials:
            comp_json = mat.get("Composition_JSON", {})
            if not comp_json:
                total_count += 1
                continue
            
            total_count += 1
            
            # 检查非法元素
            has_invalid = any(e not in self.VALID_ELEMENTS for e in comp_json.keys())
            
            # 检查百分比和
            total_pct = sum(comp_json.values())
            sum_valid = abs(total_pct - 100) <= 2
            
            if not has_invalid and sum_valid:
                valid_count += 1
        
        return valid_count, total_count
    
    def _calculate_quality_score(
        self, materials_count: int, properties_count: int, doi_present: bool,
        phase_filled_rate: float, process_unknown_rate: float, composition_valid_rate: float
    ) -> int:
        """计算质量得分（0-100）"""
        score = 0
        
        # 材料数（最多 10 分）
        score += min(materials_count * 5, 10)
        
        # 属性数（最多 20 分）
        score += min(properties_count * 2, 20)
        
        # DOI（10 分）
        if doi_present:
            score += 10
        
        # Phase 填充率（20 分）
        score += phase_filled_rate * 20
        
        # Process Unknown 率（20 分，越低越好）
        score += (1 - process_unknown_rate) * 20
        
        # Composition 有效率（20 分）
        score += composition_valid_rate * 20
        
        return int(score)
    
    def _aggregate_qa_results(self, results: List[Dict]) -> Dict:
        """汇总 QA 结果"""
        n = len(results)
        
        # 统计红线告警
        failed = sum(1 for r in results if "NO_MATERIALS" in r["red_lines"] or "NO_PROPERTIES" in r["red_lines"])
        warning = sum(1 for r in results if r["needs_review"] and r not in [r2 for r2 in results if "NO_MATERIALS" in r2["red_lines"] or "NO_PROPERTIES" in r2["red_lines"]])
        passed = n - failed - warning
        
        return {
            "papers_passed": passed,
            "papers_warning": warning,
            "papers_failed": failed,
            "avg_quality_score": sum(r["quality_score"] for r in results) / n,
            "avg_materials_count": sum(r["materials_count"] for r in results) / n,
            "avg_properties_count": sum(r["properties_count"] for r in results) / n,
            "doi_present_rate": sum(1 for r in results if r["doi_present"]) / n,
            "avg_phase_filled_rate": sum(r["phase_filled_rate"] for r in results) / n,
            "avg_process_unknown_rate": sum(r["process_unknown_rate"] for r in results) / n,
            "avg_composition_valid_rate": sum(r["composition_valid_rate"] for r in results) / n,
        }
    
    def _generate_markdown_report(self, qa_result: Dict, output_path: Path):
        """生成 Markdown 报告"""
        with open(output_path, "w", encoding="utf-8") as f:
            f.write("# KnowMat 质量基线报告 (QA Baseline)\n\n")
            f.write(f"**生成时间**: {qa_result['timestamp']}\n\n")
            f.write(f"**扫描论文数**: {qa_result['papers_scanned']}\n\n")
            f.write("---\n\n")
            
            summary = qa_result["summary"]
            f.write("## 总体统计\n\n")
            f.write("| 状态 | 论文数 | 占比 |\n")
            f.write("|------|--------|------|\n")
            f.write(f"| ✅ 通过 | {summary['papers_passed']} | {summary['papers_passed']/qa_result['papers_scanned']:.1%} |\n")
            f.write(f"| ⚠️ 警告 | {summary['papers_warning']} | {summary['papers_warning']/qa_result['papers_scanned']:.1%} |\n")
            f.write(f"| ❌ 失败 | {summary['papers_failed']} | {summary['papers_failed']/qa_result['papers_scanned']:.1%} |\n\n")
            
            f.write("## 平均指标\n\n")
            f.write("| 指标 | 数值 | 评价 |\n")
            f.write("|------|------|------|\n")
            f.write(f"| 平均质量得分 | {summary['avg_quality_score']:.1f}/100 | {'✅' if summary['avg_quality_score'] >= 70 else '⚠️' if summary['avg_quality_score'] >= 50 else '❌'} |\n")
            f.write(f"| 平均 Materials 数 | {summary['avg_materials_count']:.2f} | - |\n")
            f.write(f"| 平均 Properties 数 | {summary['avg_properties_count']:.1f} | - |\n")
            f.write(f"| DOI 存在率 | {summary['doi_present_rate']:.1%} | {'✅' if summary['doi_present_rate'] >= 0.8 else '❌'} |\n")
            f.write(f"| Phase 填充率 | {summary['avg_phase_filled_rate']:.1%} | {'✅' if summary['avg_phase_filled_rate'] >= 0.7 else '❌'} |\n")
            f.write(f"| Process Unknown 率 | {summary['avg_process_unknown_rate']:.1%} | {'✅' if summary['avg_process_unknown_rate'] < 0.15 else '❌'} |\n")
            f.write(f"| Composition 有效率 | {summary['avg_composition_valid_rate']:.1%} | {'✅' if summary['avg_composition_valid_rate'] >= 0.8 else '❌'} |\n\n")
            
            f.write("---\n\n")
            f.write("## 逐篇详情（按质量得分排序）\n\n")
            
            for result in qa_result["details"]:
                status_emoji = "❌" if result["quality_score"] < 50 else "⚠️" if result["quality_score"] < 70 else "✅"
                f.write(f"### {status_emoji} {result['paper_name']} (得分: {result['quality_score']}/100)\n\n")
                
                f.write(f"- **Materials**: {result['materials_count']}\n")
                f.write(f"- **Samples**: {result['samples_count']}\n")
                f.write(f"- **Properties**: {result['properties_count']}\n")
                f.write(f"- **DOI**: {'✅' if result['doi_present'] else '❌'}\n")
                f.write(f"- **Phase 填充率**: {result['phase_filled_rate']:.1%}\n")
                f.write(f"- **Process Unknown 率**: {result['process_unknown_rate']:.1%}\n")
                f.write(f"- **Grain Size 填充率**: {result['grain_filled_rate']:.1%}\n")
                f.write(f"- **Composition 有效率**: {result['composition_valid_rate']:.1%}\n")
                
                if result["red_lines"]:
                    f.write(f"- **红线告警**: {', '.join(result['red_lines'])}\n")
                
                f.write("\n")
            
            f.write("---\n\n")
            f.write("*报告生成工具: KnowMat regression_diff.py (qa mode)*\n")
    
    def _print_summary(self, qa_result: Dict):
        """打印控制台摘要"""
        summary = qa_result["summary"]
        
        print("\n" + "=" * 60)
        print("质量基线检查摘要")
        print("=" * 60)
        
        print(f"\n📊 论文状态统计:")
        print(f"  ✅ 通过: {summary['papers_passed']} 篇")
        print(f"  ⚠️ 警告: {summary['papers_warning']} 篇")
        print(f"  ❌ 失败: {summary['papers_failed']} 篇")
        
        print(f"\n📈 平均质量指标:")
        print(f"  质量得分: {summary['avg_quality_score']:.1f}/100 {'✅' if summary['avg_quality_score'] >= 70 else '⚠️' if summary['avg_quality_score'] >= 50 else '❌'}")
        print(f"  DOI 存在率: {summary['doi_present_rate']:.1%} {'✅' if summary['doi_present_rate'] >= 0.8 else '❌'}")
        print(f"  Phase 填充率: {summary['avg_phase_filled_rate']:.1%} {'✅' if summary['avg_phase_filled_rate'] >= 0.7 else '❌'}")
        print(f"  Process Unknown 率: {summary['avg_process_unknown_rate']:.1%} {'✅' if summary['avg_process_unknown_rate'] < 0.15 else '⚠️'}")
        print(f"  Composition 有效率: {summary['avg_composition_valid_rate']:.1%} {'✅' if summary['avg_composition_valid_rate'] >= 0.8 else '❌'}")
        
        # 列出需要复核的论文
        failed_papers = [r for r in qa_result["details"] if r["needs_review"]]
        if failed_papers:
            print(f"\n⚠️ 需要人工复核的论文 ({len(failed_papers)} 篇):")
            for paper in failed_papers[:10]:  # 只显示前 10 篇
                print(f"  - {paper['paper_name']} (得分: {paper['quality_score']}/100, 问题: {', '.join(paper['red_lines'])})")
            if len(failed_papers) > 10:
                print(f"  ... 及其他 {len(failed_papers) - 10} 篇")
        
        print("\n" + "=" * 60)


def main_gt(args):
    """GT 模式：AI vs Ground Truth 对比"""
    # 确定要对比的论文
    if args.all:
        paper_ids = list(range(1, 7))
    elif args.papers:
        paper_ids = sorted(set(args.papers))
    else:
        print("错误：必须指定 --all 或 --papers")
        return
    
    # 执行对比
    workspace_root = Path(__file__).parent.parent
    differ = RegressionDiff(workspace_root)
    
    print(f"[GT 模式] 开始回归对比，论文编号: {paper_ids}")
    print("=" * 60)
    
    result = differ.compare_all(paper_ids)
    
    if "error" in result:
        print(f"[ERROR] {result['error']}")
        return
    
    # 生成报告
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if args.output:
        base_path = Path(args.output)
    else:
        base_path = workspace_root / "reports" / f"regression_{timestamp}"
    
    if args.format in ["markdown", "both"]:
        md_path = base_path.with_suffix(".md")
        differ.generate_markdown_report(result, md_path)
        print(f"\n✅ Markdown 报告已生成: {md_path}")
    
    if args.format in ["json", "both"]:
        json_path = base_path.with_suffix(".json")
        differ.generate_json_report(result, json_path)
        print(f"✅ JSON 报告已生成: {json_path}")
    
    # 控制台摘要
    summary = result["summary"]
    print("\n" + "=" * 60)
    print("回归测试摘要")
    print("=" * 60)
    
    acc = summary["field_accuracy"]
    print(f"\n📊 关键指标:")
    print(f"  DOI 命中率:             {acc['doi_hit_rate']:.1%} {'✅' if acc['doi_hit_rate'] >= 0.8 else '❌'}")
    print(f"  Main_Phase 填充率:      {acc['main_phase_ai_filled_rate']:.1%} {'✅' if acc['main_phase_ai_filled_rate'] >= 0.7 else '❌'}")
    print(f"  Process_Category 准确率: {acc['process_category_match_rate']:.1%} {'✅' if acc['process_category_match_rate'] >= 0.85 else '❌'}")
    print(f"  温度平均偏移:           {summary['temperature']['mean_offset_K']:.2f} K {'✅' if summary['temperature']['mean_offset_K'] < 0.5 else '❌'}")
    
    comp = summary["composition_quality"]
    print(f"\n⚠️ 成分质量问题:")
    print(f"  非法元素:   {comp['papers_with_invalid_elements']} 篇")
    print(f"  百分比异常: {comp['papers_with_sum_issues']} 篇")
    print(f"  空成分:     {comp['papers_with_empty_composition']} 篇")
    
    print("\n" + "=" * 60)


def main_self(args):
    """Self 模式：Run vs Run 自回归对比"""
    workspace_root = Path(__file__).parent.parent
    self_reg = SelfRegression(workspace_root)
    
    if args.list:
        self_reg.list_snapshots()
    elif args.snapshot:
        self_reg.create_snapshot(args.snapshot)
    elif args.compare:
        self_reg.compare_with_snapshot(args.compare, args.format, args.output)
    else:
        print("错误：必须指定 --snapshot, --compare 或 --list")


def main_qa(args):
    """QA 模式：质量基线检查"""
    workspace_root = Path(__file__).parent.parent
    qa_tool = QABaseline(workspace_root)
    
    qa_tool.scan_and_report(args.papers, args.format, args.output)


def main():
    parser = argparse.ArgumentParser(
        description="KnowMat 回归测试工具 - 支持 GT/Self/QA 三种模式",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例用法:
  # GT 模式（AI vs 手工标注）
  python tools/regression_diff.py gt --all
  python tools/regression_diff.py gt --papers 1 2 3
  
  # Self 模式（Run vs Run 自回归）
  python tools/regression_diff.py self --snapshot baseline
  python tools/regression_diff.py self --compare baseline
  python tools/regression_diff.py self --list
  
  # QA 模式（质量基线检查）
  python tools/regression_diff.py qa
  python tools/regression_diff.py qa --papers 1 5 8 12
  
  # 向后兼容（等价于 gt --all）
  python tools/regression_diff.py --all
        """
    )
    
    # 检查是否使用向后兼容模式（无子命令）
    if len(sys.argv) > 1 and sys.argv[1] in ["--all", "--papers"]:
        # 向后兼容：插入 "gt" 子命令
        sys.argv.insert(1, "gt")
    
    subparsers = parser.add_subparsers(dest="mode", help="选择运行模式")
    
    # GT 模式
    parser_gt = subparsers.add_parser("gt", help="AI vs Ground Truth 对比（需要手工标注）")
    parser_gt.add_argument("--all", action="store_true", help="对比全部 6 篇论文")
    parser_gt.add_argument("--papers", nargs="+", type=int, help="指定论文编号")
    parser_gt.add_argument("--format", choices=["markdown", "json", "both"], default="both", help="输出格式")
    parser_gt.add_argument("--output", help="输出文件路径（不含扩展名）")
    
    # Self 模式
    parser_self = subparsers.add_parser("self", help="Run vs Run 自回归对比（无需 GT）")
    parser_self.add_argument("--snapshot", metavar="NAME", help="创建快照")
    parser_self.add_argument("--compare", metavar="NAME", help="与快照对比")
    parser_self.add_argument("--list", action="store_true", help="列出所有快照")
    parser_self.add_argument("--format", choices=["markdown", "json", "both"], default="both", help="输出格式")
    parser_self.add_argument("--output", help="输出文件路径（不含扩展名）")
    
    # QA 模式
    parser_qa = subparsers.add_parser("qa", help="质量基线检查（无需 GT）")
    parser_qa.add_argument("--papers", nargs="+", type=int, help="指定论文编号（可选）")
    parser_qa.add_argument("--format", choices=["markdown", "json", "both"], default="both", help="输出格式")
    parser_qa.add_argument("--output", help="输出文件路径（不含扩展名）")
    
    args = parser.parse_args()
    
    if not args.mode:
        parser.print_help()
        return
    
    # 路由到相应的处理函数
    if args.mode == "gt":
        main_gt(args)
    elif args.mode == "self":
        main_self(args)
    elif args.mode == "qa":
        main_qa(args)


if __name__ == "__main__":
    main()
