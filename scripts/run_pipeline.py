from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path

from init_target import init_target
from utils import append_log, read_sources, target_dir


SCRIPT_DIR = Path(__file__).resolve().parent


def call(script: str, *args: str) -> None:
    cmd = [sys.executable, str(SCRIPT_DIR / script), *args]
    subprocess.run(cmd, check=False)


def process_video_sources(target: str) -> None:
    base = target_dir(target)
    rows = [r for r in read_sources(base / "sources.csv") if r.get("source_type") == "video" and r.get("url_or_path")]
    ps1 = SCRIPT_DIR / "fetch_video_subtitles.ps1"
    for row in rows:
        out_dir = base / "sources" / "videos" / row["source_id"]
        cmd = [
            "powershell",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(ps1),
            "-Url",
            row["url_or_path"],
            "-OutputDir",
            str(out_dir),
        ]
        result = subprocess.run(cmd, check=False)
        if result.returncode != 0:
            append_log(base, f"VIDEO_ERROR {row['source_id']} {row['url_or_path']}")
            pending = base / "pending_transcription.md"
            with pending.open("a", encoding="utf-8") as f:
                f.write(f"- {row['source_id']}: {row.get('title','')} | {row['url_or_path']} | subtitle fetch failed\n")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    parser.add_argument("--type", default="auto", dest="target_type")
    parser.add_argument("--mode", default="mvp")
    args = parser.parse_args()

    base = init_target(args.target, args.target_type)
    call("search_sources.py", "--target", args.target)
    call("fetch_web_pages.py", "--target", args.target)
    process_video_sources(args.target)
    call("clean_transcript.py", "--input", str(base / "sources" / "videos"), "--output-dir", str(base / "sources" / "transcripts"))
    call("create_source_cards.py", "--target", args.target)
    call("merge_research.py", "--target", args.target)
    call("build_skill.py", "--target", args.target, "--type", args.target_type)
    call("quality_check.py", "--target", args.target, "--type", args.target_type)
    print(base)


if __name__ == "__main__":
    main()

