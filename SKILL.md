---
name: hr-skillforge
description: HR SkillForge / HR methodology distiller. Distill public evidence from consulting firms, benchmark companies, and HR software companies into installable company-specific HR methodology Skills. Emphasizes English target normalization, full-strategy distillation by default, anysearch-enhanced discovery, public video/audio/transcript handling, source cards, evidence scoring, seven research layers, quality gates, and explicit evidence boundaries.
metadata:
  short-description: HR SkillForge / HR 方法论 Skill 锻造器
---

# HR SkillForge / HR 方法论 Skill 锻造器

This Skill forges company-specific HR methodology Skills from public evidence about consulting firms, benchmark companies, and HR software companies. It does not write company profiles; it generates reusable `SKILL.md` files that help users solve real HR, organization, talent, performance, rewards, leadership, culture, people analytics, and change-management problems.

本 Skill 用于把咨询公司、标杆公司或 HR 软件公司的公开资料，蒸馏成可安装、可调用的 company-specific HR 方法论 Skill。目标不是写公司介绍，而是生成能解决真实 HR / 组织 / 人才 / 绩效 / 薪酬激励 / 领导力 / 变革问题的 `SKILL.md`。

## Operating Defaults / 运行默认规则

- Default to full-strategy distillation, not MVP or fast mode. Use the richest practical search depth, full source-card coverage, video/audio expansion, quality gates, and a practical installable `SKILL.md` unless the user explicitly asks for a quick probe.
- Before searching, normalize the distillation target into an English search name. If the user provides Chinese, translated, abbreviated, or ambiguous names, remind the user that the target is being searched as its English/public name and include the Chinese name as an alias rather than the primary search key.
- For international targets, do not rely on Chinese target names as the primary query string. Chinese names can create encoding issues, irrelevant search results, and weak official-source recall.
- Examples: `麦肯锡` -> primary search target `McKinsey`; aliases `麦肯锡`, `McKinsey & Company`, `McKinsey People & Organizational Performance`. `美世` -> `Mercer`. `光辉合益` / `Hay` -> `Korn Ferry Hay Group` or the best public English brand.
- When running scripts, prefer `--mode full --depth standard` as the default. Escalate to `--depth deep` when the target is important, official sources are sparse, or the user asks for a complete playbook.
- Default all user-facing outputs to bilingual Chinese and English. This includes generated `SKILL.md`, distillation reports, evidence summaries, quality notes, warnings, usage instructions, and final answers unless the user explicitly requests one language only.

中文规则：默认做“全攻略蒸馏”，不要默认做 fast/MVP。蒸馏对象必须先确认英文公开名称；如果用户输入中文公司名或中文方法论名，要提醒使用者“将按英文公开名称搜索，中文作为别名补充”，再开始搜索和生成。所有面向使用者的输出默认中英文双语，除非用户明确要求只用一种语言。

## Core Principles / 核心原则

- Input is a company, institution, product, or method source; output is an installable Skill, not a research report.
- Use public sources, user-authorized sources, and compliant video/audio/subtitle/transcript sources only.
- Video, webinar, interview, podcast, and transcript sources are high-weight and must not be silently skipped.
- Every source should become a source card; every core judgment should be traceable to evidence or explicitly marked as professional inference.
- If evidence is insufficient, generate a `Light Version`; do not fabricate a complete methodology.
- Do not bypass login, CAPTCHA, membership, private-video restrictions, paywalls, or platform controls.
- For current facts, regulations, labor-market data, compensation data, product details, or recent news, refresh public sources before answering.

## Default Workflow / 默认工作流

```text
target_name + target_type
-> normalize to English/public search name and aliases
-> init target directory
-> create or read sources.csv
-> check search provider availability, especially anysearch
-> generate query matrix, source-card search plan, and video/audio search plan
-> run source-card-driven search, with anysearch preferred when available
-> fetch web pages, PDFs, transcripts, video/audio pages, and manual files
-> capture subtitles/transcripts only when compliant and authorized
-> clean transcripts
-> create source cards with evidence score
-> merge into seven research files
-> build company-specific SKILL.md
-> quality_check -> quality-report.md
-> if possible, run a second distillation pass to improve practicality and bilingual usability
```

## Seven Research Agents / 七类研究文件

| Agent | Output | Focus |
|---|---|---|
| Official Methodology / 官方方法论 | `01-official-methodology.md` | Official frameworks, definitions, capability pages, reports, named models |
| Video Transcripts / 视频音频与字幕 | `02-video-transcripts.md` | Consultant explanations, webinars, podcasts, Q&A wording, real explanation sequence |
| Case Practices / 案例实践 | `03-case-practices.md` | Implementation paths, project playbooks, client cases, management actions |
| Tools and Frameworks / 工具框架 | `04-tools-and-frameworks.md` | Diagnostic tables, models, scorecards, checklists, SOPs, templates |
| External Views / 外部评价 | `05-external-views.md` | Limitations, controversy, blind spots, boundaries, third-party checks |
| Timeline / 时间线 | `06-timeline.md` | Recent changes, trends, outdated risks, new reports |
| China Localization / 中国落地 | `07-china-localization.md` | Chinese sources, China contexts, local management language and conversion |

## Source-Card-Driven Search / 证据卡驱动搜索

Before searching broadly, define the evidence cards the final Skill needs. Search by card type, not only by generic keywords.

Core source-card types:

- `official_methodology`: official methodologies, model definitions, white papers, capability pages.
- `diagnostic_question`: diagnostic questions, maturity models, assessment logic.
- `tool_template`: scorecards, checklists, templates, toolkits.
- `case_practice`: client cases, implementation paths, management actions.
- `video_transcript`: webinars, podcasts, interviews, subtitles, transcripts.
- `external_boundary`: external views, controversy, limitations, failure conditions.
- `china_localization`: China cases, Chinese wording, localization conversion.

If a card type has fewer than three usable sources, expand with target aliases, named methodologies, consultant names, report titles, conference names, client cases, and Chinese/English synonyms.

## Search Provider Rules / 搜索工具规则

- Prefer `anysearch` when installed. Use it for broad web search, batch query expansion, full-text extraction, video/audio page discovery, PDF discovery, and source export.
- anysearch is a discovery and extraction layer; it does not replace source cards, evidence scoring, quality gates, or video/subtitle rules.
- If anysearch returns Markdown search results, parse result titles, URLs, snippets, dates, and source types into `sources.csv`.
- If anysearch is unavailable, rate-limited, or returns low-quality results, fall back to browser/web search, official site checks, video platform search, and manual sources.

## Video / Audio / Subtitle Rules / 视频音频与字幕规则

Video and audio are not auxiliary. Formal distillation must process at least one round of video/audio/subtitle or transcript source discovery.

Priority:

```text
official transcript / podcast transcript
-> official webinar or podcast page
-> YouTube/Bilibili manual subtitles
-> YouTube/Bilibili auto subtitles
-> user-authorized local audio/video transcription
-> video/audio page metadata
-> no subtitles: record the failure and evidence gap
```

When using `yt-dlp`, download subtitles only, not video files.

```powershell
yt-dlp --list-subs "VIDEO_URL"
yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs "en-orig,en,en-US,en-GB,zh-Hans,zh-Hant,zh,zh-CN,zh-TW" --sub-format "srt/vtt/best" "VIDEO_URL"
```

If YouTube requires login or triggers anti-bot restrictions, stop automatic capture, record the item in `pending_transcription.md`, and ask the user for an authorized transcript, exported cookies file, or local file. Do not bypass platform controls.

After YouTube fails, immediately expand to:

- Official transcript / webinar / podcast pages
- Bilibili, Vimeo, LinkedIn Events
- Apple Podcasts / Spotify / Omny / podcast indexes
- SHRM, Gartner HR, HR Tech, WorldatWork, CIPD, ATD
- Thinkers50, TED/TEDx, business school public lectures

## Quality Gates / 质量门槛

Use three levels:

- `Full Version`: strong source base, broad coverage, enough official/recent/video or audio evidence.
- `Usable Candidate`: enough high-signal public sources for analysis and draft solution design, with confidence labels.
- `Light Version`: sparse or weak evidence; generate candidate hypotheses and research summary only.

For international consulting companies, aim for:

```text
Full Version: 50 total sources, 8 video/audio/transcript candidates, 25 official sources, 10 recent sources.
Usable Candidate: 20 total sources, 5 video/audio/transcript candidates, 10 official sources, 5 recent sources.
```

Even when quantitative gates are met, mark transcript gaps if subtitles or full transcripts were not actually captured.

## Scripts / 脚本默认用法

Default project root:

```text
PROJECT_ROOT/
```

Recommended full-strategy command:

```powershell
python scripts/run_pipeline.py --target "McKinsey" --type consulting_company --mode full --depth standard
```

Deep distillation when the user asks for a complete playbook:

```powershell
python scripts/run_pipeline.py --target "McKinsey" --type consulting_company --mode full --depth deep
```

Avoid using Chinese target names as the primary target for international companies. Use the English public name as `--target`, and record Chinese names as aliases or source-query variants.

## Final Skill Requirements / 最终产物要求

The generated `SKILL.md` should include:

- Bilingual Chinese and English throughout, especially headings, core conclusions, workflows, diagnostic questions, evidence boundaries, and usage instructions.
- Evidence status and quality boundary.
- Honest non-affiliation boundary.
- Company-specific method families, not generic HR advice.
- Diagnostic question sets.
- Answer workflow.
- Source-card recall rules.
- Confidence labels.
- Default output templates.
- Anti-patterns.
- China localization notes when relevant.
- Refresh rules for current data and recent trends.

## When To Read Reference Files / 何时读取参考文件

- Search strategy and query matrix: `references/research-framework.md`
- anysearch installation and usage: `references/anysearch-search-provider.md`
- Source-card-driven search: `references/source-card-search-strategy.md`
- Evidence scoring: `references/evidence-scoring.md`
- Video subtitle strategy: `references/video-source-strategy.md`
- Extraction fields and source cards: `references/extraction-framework.md`
- Quality gates: `references/quality-standard.md`
