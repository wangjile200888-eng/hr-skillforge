from __future__ import annotations

import argparse
from pathlib import Path

from utils import RESEARCH_FILES, target_dir


def bucket_for(card_text: str, path: Path) -> str:
    text = card_text.lower()
    name = path.as_posix().lower()
    if "/video/" in name or "source type: video" in text or "source type: transcript" in text:
        return "02-video-transcripts.md"
    if "case" in text or "案例" in text:
        return "03-case-practices.md"
    if any(k in text for k in ["tool", "framework", "model", "diagnostic", "template", "工具", "模型", "诊断"]):
        return "04-tools-and-frameworks.md"
    if any(k in text for k in ["third_party", "news", "external", "critique", "媒体", "评价"]):
        return "05-external-views.md"
    if any(k in text for k in ["2026", "2025", "2024", "latest", "最新"]):
        return "06-timeline.md"
    if any(k in text for k in ["china", "chinese", "中国", "本土", "中文"]):
        return "07-china-localization.md"
    return "01-official-methodology.md"


def run(target: str) -> None:
    base = target_dir(target)
    research_dir = base / "references" / "research"
    buckets = {name: [] for name in RESEARCH_FILES}
    cards = list((base / "source-cards").rglob("*.md"))
    for card in cards:
        text = card.read_text(encoding="utf-8", errors="ignore")
        buckets[bucket_for(text, card)].append((card, text))

    for name, items in buckets.items():
        lines = [f"# {name.removesuffix('.md')}\n"]
        if not items:
            lines.append("\n_No evidence yet._\n")
        for card, text in items:
            lines.append(f"\n## {card.stem}\n\n")
            lines.append(text)
            lines.append("\n")
        (research_dir / name).write_text("".join(lines), encoding="utf-8")

    summary = [
        "# Research Summary\n",
        f"- Source cards: {len(cards)}",
        f"- Video cards: {len(list((base / 'source-cards' / 'video').glob('*.md')))}",
        f"- Research files: {len(RESEARCH_FILES)}",
        "",
    ]
    (base / "references" / "research-summary.md").write_text("\n".join(summary), encoding="utf-8")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    args = parser.parse_args()
    run(args.target)


if __name__ == "__main__":
    main()

