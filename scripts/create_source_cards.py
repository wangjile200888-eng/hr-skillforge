from __future__ import annotations

import argparse
from pathlib import Path

from evidence_score import score_source
from utils import read_sources, target_dir


def find_local_content(row: dict[str, str], base: Path) -> tuple[str, str]:
    source_id = row["source_id"]
    source_type = row.get("source_type", "")
    candidates = []
    if source_type == "web":
        candidates.append(base / "sources" / "web" / f"{source_id}.md")
    elif source_type == "manual":
        path = row.get("url_or_path", "")
        if path:
            candidates.append(Path(path))
        candidates.append(base / "sources" / "manual" / f"{source_id}.md")
    elif source_type in {"video", "transcript"}:
        candidates.extend((base / "sources" / "transcripts").glob(f"*{source_id}*"))
        candidates.extend((base / "sources" / "videos").glob(f"*{source_id}*"))
    elif source_type == "pdf":
        candidates.append(base / "sources" / "pdf" / f"{source_id}.md")

    for path in candidates:
        if path.exists() and path.is_file():
            return str(path), path.read_text(encoding="utf-8", errors="ignore")
    return "", ""


def card_dir(source_type: str) -> str:
    if source_type in {"video", "transcript"}:
        return "video"
    if source_type == "pdf":
        return "pdf"
    if source_type == "manual":
        return "manual"
    return "web"


def make_card(row: dict[str, str], base: Path) -> Path:
    local_path, content = find_local_content(row, base)
    score, level = score_source(row, content)
    source_id = row["source_id"]
    out = base / "source-cards" / card_dir(row.get("source_type", "")) / f"{source_id}.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    summary = " ".join(content.split()[:80]) if content else row.get("notes", "")
    text = f"""# Source Card: {source_id}

## Metadata

- Target: {row.get('target_name','')}
- Target Type: {row.get('target_type','')}
- Source ID: {source_id}
- Source Type: {row.get('source_type','')}
- Source Tier: {row.get('source_tier','')}
- Title: {row.get('title','')}
- URL or Path: {row.get('url_or_path','')}
- Date: {row.get('date','')}
- Language: {row.get('language','')}
- Evidence Score: {score}
- Evidence Level: {level}
- Tags: {row.get('tags','')}
- Local Path: {local_path}

## Short Summary

{summary}

## Key Evidence

1. TBD
2. TBD
3. TBD

## Extractable HR Patterns

- HR / Organization Methodology:
- Diagnostic Question:
- Tool / Template:
- Management Action:
- Applicable Scenario:
- Limitation:

## Notes

{row.get('notes','')}
"""
    out.write_text(text, encoding="utf-8")
    return out


def run(target: str) -> None:
    base = target_dir(target)
    rows = [r for r in read_sources(base / "sources.csv") if r.get("source_id") and r.get("source_id") != "manual_001"]
    for row in rows:
        print(make_card(row, base))


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    args = parser.parse_args()
    run(args.target)


if __name__ == "__main__":
    main()

