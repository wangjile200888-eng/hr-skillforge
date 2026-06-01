from __future__ import annotations

from datetime import datetime


def score_source(row: dict[str, str], content: str = "") -> tuple[int, str]:
    score = 50
    tier = (row.get("source_tier") or "").lower()
    source_type = (row.get("source_type") or "").lower()
    title = (row.get("title") or "").lower()
    tags = (row.get("tags") or "").lower()
    date = row.get("date") or ""

    if "official" in tier:
        score += 30
    if tier in {"official_video", "official_report", "public_interview", "user_provided"}:
        score += 25
    if source_type in {"pdf", "video", "transcript"} or len(content) > 3000:
        score += 20
    if date:
        score += 10
        try:
            year = int(date[:4])
            if datetime.now().year - year <= 3:
                score += 10
        except ValueError:
            pass
    else:
        score -= 10
    if any(k in content.lower() for k in ["case", "framework", "model", "tool", "diagnostic", "案例", "模型", "工具"]):
        score += 10
    if any(k in tags + title for k in ["hr", "organization", "talent", "performance", "reward", "薪酬", "绩效", "人才", "组织"]):
        score += 10
    if tier in {"secondary_summary", "news"}:
        score -= 15
    if len(content.strip()) < 500:
        score -= 20

    score = max(0, min(100, score))
    if score >= 80:
        level = "A"
    elif score >= 60:
        level = "B"
    elif score >= 40:
        level = "C"
    else:
        level = "D"
    return score, level

