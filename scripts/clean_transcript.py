from __future__ import annotations

import argparse
import re
from pathlib import Path


TIMESTAMP_PATTERNS = [
    r"\d{2}:\d{2}:\d{2}[,.]\d{3}\s+-->\s+\d{2}:\d{2}:\d{2}[,.]\d{3}",
    r"\d{2}:\d{2}\.\d{3}\s+-->\s+\d{2}:\d{2}\.\d{3}",
]


def clean_subtitle_text(text: str) -> str:
    cleaned = []
    prev = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            continue
        if line.upper().startswith("WEBVTT") or line.upper().startswith("KIND:") or line.upper().startswith("LANGUAGE:"):
            continue
        if line.isdigit():
            continue
        if any(re.search(pattern, line) for pattern in TIMESTAMP_PATTERNS):
            continue
        line = re.sub(r"<[^>]+>", "", line)
        line = line.replace("&nbsp;", " ")
        line = re.sub(r"\s+", " ", line).strip()
        if line and line != prev:
            cleaned.append(line)
            prev = line
    return "\n".join(cleaned)


def clean_path(path: Path, output_dir: Path | None = None) -> Path:
    output_dir = output_dir or path.parent
    output_dir.mkdir(parents=True, exist_ok=True)
    out = output_dir / f"{path.stem}.transcript.txt"
    out.write_text(clean_subtitle_text(path.read_text(encoding="utf-8", errors="ignore")), encoding="utf-8")
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input", required=True)
    parser.add_argument("--output-dir")
    args = parser.parse_args()
    path = Path(args.input)
    out_dir = Path(args.output_dir) if args.output_dir else None
    if path.is_dir():
        for file in path.rglob("*"):
            if file.suffix.lower() in {".srt", ".vtt"}:
                print(clean_path(file, out_dir))
    else:
        print(clean_path(path, out_dir))


if __name__ == "__main__":
    main()

