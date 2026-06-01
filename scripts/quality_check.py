from __future__ import annotations

import argparse
from pathlib import Path

from utils import RESEARCH_FILES, read_sources, target_dir


FULL_THRESHOLDS = {
    "consulting_company": (50, 8, 25, 10),
    "hr_software_company": (40, 5, 15, 8),
    "benchmark_company": (40, 5, 15, 8),
    "auto": (20, 2, 8, 5),
}

USABLE_THRESHOLDS = {
    "consulting_company": (20, 5, 10, 5),
    "hr_software_company": (18, 4, 8, 4),
    "benchmark_company": (20, 4, 8, 5),
    "auto": (12, 2, 5, 3),
}


def run(target: str, target_type: str) -> Path:
    base = target_dir(target)
    rows = [r for r in read_sources(base / "sources.csv") if r.get("source_id") and r.get("source_id") != "manual_001"]
    total_req, video_req, official_req, recent_req = FULL_THRESHOLDS.get(target_type, FULL_THRESHOLDS["auto"])
    usable_total, usable_video, usable_official, usable_recent = USABLE_THRESHOLDS.get(target_type, USABLE_THRESHOLDS["auto"])
    videos = [r for r in rows if r.get("source_type") in {"video", "transcript"}]
    official = [r for r in rows if "official" in (r.get("source_tier") or "")]
    recent = []
    for r in rows:
        try:
            if r.get("date") and int(r["date"][:4]) >= 2024:
                recent.append(r)
        except ValueError:
            pass
    cards = list((base / "source-cards").rglob("*.md"))
    research_ok = all((base / "references" / "research" / name).exists() for name in RESEARCH_FILES)
    skill_exists = (base / "SKILL.md").exists()
    full = len(rows) >= total_req and len(videos) >= video_req and len(official) >= official_req and len(recent) >= recent_req
    usable = len(rows) >= usable_total and len(videos) >= usable_video and len(official) >= usable_official and len(recent) >= usable_recent
    version = "Full Version" if full else ("Usable Candidate" if usable else "Light Version")

    report = f"""# Quality Report: {target}

## Summary

- Target type: {target_type}
- Version: {version}
- Sources: {len(rows)} / {total_req}
- Video or transcript sources: {len(videos)} / {video_req}
- Official sources: {len(official)} / {official_req}
- Recent sources: {len(recent)} / {recent_req}
- Usable Candidate threshold: sources {len(rows)} / {usable_total}, videos {len(videos)} / {usable_video}, official {len(official)} / {usable_official}, recent {len(recent)} / {usable_recent}
- Source cards: {len(cards)}
- Research files complete: {research_ok}
- SKILL.md exists: {skill_exists}

## Required Follow-up

{"- Add more video/webinar/podcast transcript sources for Full Version.\n" if len(videos) < video_req else ""}
{"- Add more official reports/articles/cases for Full Version.\n" if len(official) < official_req else ""}
{"- Add more recent sources from 2024-2026 for Full Version.\n" if len(recent) < recent_req else ""}
{"- Add source cards by running create_source_cards.py.\n" if len(cards) < len(rows) else ""}

## Boundary

If this report says Light Version, the generated Skill must not present its models as fully validated.
If this report says Usable Candidate, the generated Skill may be used, but must label model confidence.
"""
    out = base / "quality-report.md"
    out.write_text(report, encoding="utf-8")
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    parser.add_argument("--type", default="auto", dest="target_type")
    args = parser.parse_args()
    print(run(args.target, args.target_type))


if __name__ == "__main__":
    main()
