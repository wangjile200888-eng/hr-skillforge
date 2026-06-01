from __future__ import annotations

import argparse
from pathlib import Path

from utils import RESEARCH_FILES, ensure_target_dirs, target_dir, write_sources_template


def init_target(target: str, target_type: str) -> Path:
    base = target_dir(target)
    ensure_target_dirs(base)
    write_sources_template(base / "sources.csv", target, target_type)

    for name in RESEARCH_FILES:
        path = base / "references" / "research" / name
        if not path.exists():
            title = name.removesuffix(".md").replace("-", " ").title()
            path.write_text(f"# {title}\n\n_No evidence yet._\n", encoding="utf-8")

    index = base / "sources" / "index.csv"
    if not index.exists():
        index.write_text(
            "source_id,source_type,status,local_path,error\n",
            encoding="utf-8-sig",
        )
    return base


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    parser.add_argument("--type", default="auto", dest="target_type")
    args = parser.parse_args()
    print(init_target(args.target, args.target_type))


if __name__ == "__main__":
    main()

