from __future__ import annotations

import argparse
import csv
from pathlib import Path

from utils import target_dir


HR_TOPICS = [
    "organization capability",
    "organization design",
    "HR operating model",
    "talent strategy",
    "leadership development",
    "performance management",
    "compensation rewards",
    "total rewards",
    "people analytics",
    "HR digital transformation",
    "组织能力",
    "组织设计",
    "人才战略",
    "绩效管理",
    "薪酬绩效",
    "领导力",
    "干部管理",
]

SOURCE_TYPES = [
    "white paper",
    "report",
    "PDF",
    "case study",
    "webinar",
    "podcast",
    "interview",
    "transcript",
    "framework",
    "toolkit",
    "白皮书",
    "案例",
    "视频",
    "访谈",
    "直播",
    "播客",
    "字幕",
]

VIDEO_PATTERNS = [
    "{company} HR webinar",
    "{company} organization design webinar",
    "{company} talent strategy interview",
    "{company} leadership development podcast",
    "{company} performance management video",
    "{company} CHRO interview",
    "{company} total rewards webinar",
    "{company} 人力资源 视频",
    "{company} 组织能力 访谈",
    "{company} 绩效管理 直播",
    "{company} 人才管理 论坛",
    "{company} 薪酬绩效 视频",
]

VIDEO_PLATFORM_PATTERNS = [
    "site:youtube.com {company} HR webinar",
    "site:youtube.com {company} organization design webinar",
    "site:youtube.com {company} leadership development podcast",
    "site:bilibili.com {company} 人力资源 视频",
    "site:bilibili.com {company} 组织能力 访谈",
    "site:bilibili.com {company} 薪酬绩效 公开课",
    "site:vimeo.com {company} HR webinar",
    "site:vimeo.com {company} leadership development",
    "site:linkedin.com/events {company} HR webinar",
    "site:podcasts.apple.com {company} HR",
    "site:open.spotify.com {company} leadership podcast",
    "site:xiaoyuzhoufm.com {company} 人力资源",
    "site:ximalaya.com {company} 薪酬 绩效",
    "site:shrm.org {company} webinar talent",
    "site:gartner.com {company} HR webinar",
    "site:hrtechconference.com {company} HR",
    "site:worldatwork.org {company} total rewards",
    "site:cipd.org {company} leadership",
    "site:td.org {company} talent development",
    "site:thinkers50.com {company} leadership",
    "site:ted.com {company} leadership",
    "{company} business school lecture HR organization",
    "{company} conference replay talent organization",
]

SOURCE_CARD_QUERY_PATTERNS = {
    "official_methodology": [
        "{company} official methodology HR organization framework",
        "{company} white paper organization design talent performance",
        "{company} methodology compensation rewards leadership development",
        "{company} 官方 方法论 组织 人才 绩效 薪酬",
    ],
    "diagnostic_question": [
        "{company} diagnostic questions organization capability",
        "{company} maturity model HR transformation diagnostic",
        "{company} assessment tool leadership talent organization",
        "{company} 诊断 问题 组织能力 人才管理",
    ],
    "tool_template": [
        "{company} tool template framework HR",
        "{company} scorecard checklist toolkit people organization",
        "{company} job evaluation tool performance management template",
        "{company} 工具 模板 评分卡 诊断表",
    ],
    "case_practice": [
        "{company} case study HR transformation organization design",
        "{company} client story talent strategy performance management",
        "{company} implementation case rewards leadership",
        "{company} 案例 实践 组织变革 人才 绩效",
    ],
    "video_transcript": [
        "{company} webinar transcript HR organization",
        "{company} podcast transcript talent leadership",
        "{company} interview transcript performance rewards",
        "{company} 视频 字幕 访谈 直播 回放",
    ],
    "external_boundary": [
        "{company} criticism limitation review HR methodology",
        "{company} analyst view organization talent performance",
        "{company} controversy limitation compensation leadership",
        "{company} 局限 评价 争议 方法论",
    ],
    "china_localization": [
        "{company} China HR case organization performance",
        "{company} Chinese market talent rewards leadership",
        "{company} 中国 企业 案例 组织 人才 绩效 薪酬",
        "{company} 中文 方法论 人力资源 咨询",
    ],
}


def aliases(target: str) -> list[str]:
    base = [target]
    known = {
        "hay": ["Hay Group", "Korn Ferry Hay Group", "Hay Guide Chart", "海氏"],
        "korn ferry": ["Korn Ferry", "光辉国际", "Korn Ferry Hay Group"],
        "mercer": ["Mercer", "Mercer Consulting", "美世", "美世咨询"],
        "mckinsey": ["McKinsey", "McKinsey People & Organizational Performance", "麦肯锡"],
    }
    return list(dict.fromkeys(base + known.get(target.lower(), [])))


def generate_queries(target: str) -> tuple[list[str], list[str], list[tuple[str, str]]]:
    names = aliases(target)
    queries = []
    for name in names:
        for topic in HR_TOPICS:
            for stype in SOURCE_TYPES:
                queries.append(f"{name} {topic} {stype}")
    video_queries = [p.format(company=name) for name in names for p in VIDEO_PATTERNS]
    video_queries += [p.format(company=name) for name in names for p in VIDEO_PLATFORM_PATTERNS]
    source_card_queries = [
        (card_type, pattern.format(company=name))
        for name in names
        for card_type, patterns in SOURCE_CARD_QUERY_PATTERNS.items()
        for pattern in patterns
    ]
    return queries, video_queries, source_card_queries


def write_plan(target: str) -> None:
    base = target_dir(target)
    plan_dir = base / "research_plan"
    plan_dir.mkdir(parents=True, exist_ok=True)
    queries, video_queries, source_card_queries = generate_queries(target)

    (plan_dir / "search_queries.md").write_text(
        "# Search Queries\n\n" + "\n".join(f"- {q}" for q in queries[:500]) + "\n",
        encoding="utf-8",
    )
    (plan_dir / "video_search_queries.md").write_text(
        "# Video Search Queries\n\n" + "\n".join(f"- {q}" for q in video_queries) + "\n",
        encoding="utf-8",
    )
    (plan_dir / "source_card_search_queries.md").write_text(
        "# Source Card Search Queries\n\n"
        + "\n".join(f"- `{card_type}` {query}" for card_type, query in source_card_queries)
        + "\n",
        encoding="utf-8",
    )
    with (plan_dir / "search_queries.csv").open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["query", "query_type", "source_card_type"])
        for q in queries:
            writer.writerow([q, "matrix", ""])
        for q in video_queries:
            writer.writerow([q, "video", "video_transcript"])
        for card_type, q in source_card_queries:
            writer.writerow([q, "source_card", card_type])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    args = parser.parse_args()
    write_plan(args.target)


if __name__ == "__main__":
    main()
