from __future__ import annotations

import csv
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
OUTPUT_ROOT = ROOT / "output" / "generated-skills"

RESEARCH_FILES = [
    "01-official-methodology.md",
    "02-video-transcripts.md",
    "03-case-practices.md",
    "04-tools-and-frameworks.md",
    "05-external-views.md",
    "06-timeline.md",
    "07-china-localization.md",
]

SOURCE_FIELDS = [
    "target_name",
    "target_type",
    "source_id",
    "source_type",
    "title",
    "url_or_path",
    "language",
    "date",
    "source_tier",
    "tags",
    "notes",
]


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    value = re.sub(r"-+", "-", value).strip("-")
    return value or "target"


def target_dir(target: str) -> Path:
    return OUTPUT_ROOT / slugify(target)


def ensure_target_dirs(base: Path) -> None:
    for rel in [
        "sources/web",
        "sources/pdf",
        "sources/videos",
        "sources/transcripts",
        "sources/manual",
        "references/research",
        "source-cards/web",
        "source-cards/pdf",
        "source-cards/video",
        "source-cards/manual",
        "research_plan",
        "logs",
    ]:
        (base / rel).mkdir(parents=True, exist_ok=True)


def read_sources(path: Path) -> list[dict[str, str]]:
    if not path.exists():
        return []
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def write_sources_template(path: Path, target_name: str, target_type: str) -> None:
    if path.exists():
        return
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=SOURCE_FIELDS)
        writer.writeheader()
        writer.writerow(
            {
                "target_name": target_name,
                "target_type": target_type,
                "source_id": "manual_001",
                "source_type": "manual",
                "title": "Replace with your first source",
                "url_or_path": "",
                "language": "zh",
                "date": "",
                "source_tier": "user_provided",
                "tags": "organization;talent",
                "notes": "Delete or replace this example row.",
            }
        )


def append_log(base: Path, message: str) -> None:
    log_path = base / "logs" / "pipeline.log"
    log_path.parent.mkdir(parents=True, exist_ok=True)
    with log_path.open("a", encoding="utf-8") as f:
        f.write(message.rstrip() + "\n")

