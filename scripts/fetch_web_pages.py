from __future__ import annotations

import argparse
import csv
from pathlib import Path

import requests
from bs4 import BeautifulSoup
from markdownify import markdownify as md

from utils import append_log, read_sources, target_dir


def fetch_one(row: dict[str, str], base: Path) -> tuple[str, str, str]:
    source_id = row["source_id"]
    url = row["url_or_path"]
    out = base / "sources" / "web" / f"{source_id}.md"
    try:
        resp = requests.get(url, timeout=25, headers={"User-Agent": "Mozilla/5.0"})
        resp.raise_for_status()
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header"]):
            tag.decompose()
        title = soup.title.get_text(" ", strip=True) if soup.title else row.get("title", "")
        body = soup.find("main") or soup.find("article") or soup.body or soup
        text = md(str(body))
        out.write_text(f"# {title}\n\nSource: {url}\n\n{text}\n", encoding="utf-8")
        return source_id, str(out), ""
    except Exception as exc:
        append_log(base, f"WEB_ERROR {source_id} {url}: {exc}")
        return source_id, "", str(exc)


def run(target: str) -> None:
    base = target_dir(target)
    rows = [r for r in read_sources(base / "sources.csv") if r.get("source_type") == "web" and r.get("url_or_path")]
    index_path = base / "sources" / "index.csv"
    with index_path.open("a", encoding="utf-8-sig", newline="") as f:
        writer = csv.writer(f)
        for row in rows:
            source_id, local_path, error = fetch_one(row, base)
            writer.writerow([source_id, "web", "error" if error else "ok", local_path, error])


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--target", required=True)
    args = parser.parse_args()
    run(args.target)


if __name__ == "__main__":
    main()

