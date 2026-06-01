from __future__ import annotations

import argparse
from pathlib import Path

from utils import RESEARCH_FILES, read_sources, target_dir


def target_label(target_type: str) -> str:
    return {
        "consulting_company": "HR咨询方法论专家",
        "benchmark_company": "标杆公司组织管理专家",
        "hr_software_company": "HR数字化与产品实践专家",
    }.get(target_type, "HR方法论专家")


def build(target: str, target_type: str) -> Path:
    base = target_dir(target)
    rows = [r for r in read_sources(base / "sources.csv") if r.get("source_id") and r.get("source_id") != "manual_001"]
    video_count = sum(1 for r in rows if r.get("source_type") in {"video", "transcript"})
    full_thresholds = {
        "consulting_company": (50, 8, 25),
        "hr_software_company": (40, 5, 15),
        "benchmark_company": (40, 5, 15),
        "auto": (20, 2, 8),
    }
    usable_thresholds = {
        "consulting_company": (20, 5, 10),
        "hr_software_company": (18, 4, 8),
        "benchmark_company": (20, 4, 8),
        "auto": (12, 2, 5),
    }
    source_req, video_req, official_req = full_thresholds.get(target_type, full_thresholds["auto"])
    usable_source_req, usable_video_req, usable_official_req = usable_thresholds.get(target_type, usable_thresholds["auto"])
    official_count = sum(1 for r in rows if "official" in (r.get("source_tier") or ""))
    full = len(rows) >= source_req and video_count >= video_req and official_count >= official_req
    usable = len(rows) >= usable_source_req and video_count >= usable_video_req and official_count >= usable_official_req
    version = "Full Version" if full else ("Usable Candidate" if usable else "Light Version")
    research_dir = base / "references" / "research"
    research_index = "\n".join(f"- `{name}`" for name in RESEARCH_FILES)
    title = f"{target} {target_label(target_type)}"
    text = f"""---
name: {target.lower().replace(' ', '-')}-hr-expert
description: 基于公开资料蒸馏的 {target} HR/组织/人才/绩效/激励方法论专家 Skill。用于参考 {target} 的公开方法论、案例、视频字幕、工具和外部评价，帮助用户诊断组织与人力资源问题、设计方案、生成访谈提纲、证据清单、交付物和落地路径。仅基于公开资料、用户授权资料和专业推断，不代表 {target} 官方立场，不包含内部资料、客户项目资料、专有数据库或商业机密。
metadata:
  short-description: {target} HR方法论专家
---

# {title}

{"**Light Version:** 当前资料未达到可用候选版门槛，所有模型均为候选框架，使用时必须继续补充资料和验证。\n" if version == "Light Version" else ""}
{"**Usable Candidate:** 当前资料已达到可用候选版门槛，但未达到完整版门槛。可以用于分析和方案初稿；核心模型必须标注置信度，并在正式项目中继续验证。\n" if version == "Usable Candidate" else ""}
本 Skill 基于公开资料、视频/字幕资料、案例、工具和外部评价，对 {target} 的 HR / 组织 / 人才 / 绩效 / 激励相关方法论进行专业蒸馏。

## 诚实边界

- 不代表 {target} 官方立场。
- 不包含内部培训、客户项目资料、专有数据库或商业机密。
- 具体公司、行业、法规、薪酬和市场数据必须重新查证。
- 证据不足处必须标注为专业推断或候选判断。

## 使用场景

- 组织诊断、组织设计、组织能力建设。
- 人才战略、关键岗位、干部标准、领导力发展。
- 绩效管理、薪酬激励、总回报、销售激励。
- HR转型、HR数字化、员工体验、文化和变革管理。
- 生成咨询方案、访谈提纲、证据清单、交付物和落地路线图。

## 回答工作流

```text
用户问题
-> 判断问题域
-> 查阅公开资料和本 Skill 研究文件
-> 区分事实、综合判断、专业推断
-> 提炼诊断问题
-> 选择工具/框架
-> 设计管理动作和交付物
-> 标注证据边界和落地风险
```

## 研究文件

{research_index}

## 默认输出结构

```markdown
# {target}-style HR方法论分析

## 1. 核心结论
## 2. 问题域判断
## 3. 可借鉴的公开方法论
## 4. 证据清单
## 5. 诊断框架
## 6. 方案设计
## 7. 交付物建议
## 8. 中国落地转换
## 9. 风险与反模式
## 10. 公开资料与专业推断边界
```

## 搜索与更新规则

遇到最新趋势、具体公司案例、视频访谈、薪酬/法规/市场动态，必须重新查证公开资料。视频字幕是高权重来源，更新时必须处理 `02-video-transcripts.md`。

## 资料状态

- Sources: {len(rows)}
- Video/Transcript sources: {video_count}
- Version: {version}
"""
    out = base / "SKILL.md"
    out.write_text(text, encoding="utf-8")
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    parser.add_argument("--type", default="auto", dest="target_type")
    args = parser.parse_args()
    print(build(args.target, args.target_type))


if __name__ == "__main__":
    main()
