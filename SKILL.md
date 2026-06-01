---
name: hr-skillforge
description: HR SkillForge / HR 方法论锻造器。Distill public evidence from consulting firms, benchmark companies, and HR software companies into installable company-specific HR methodology Skills. 用于把咨询公司、HR咨询公司、标杆公司或HR软件公司的公开资料蒸馏成可安装的 company-specific HR/组织/人才/绩效/激励方法论 SKILL.md。Emphasizes multi-source search, public video subtitles, source cards, evidence scoring, research layers, quality gates, and Light Version boundaries. 强调多源公开资料、公开视频字幕、source cards、证据评分、七类研究文件、质量检查和 Light Version 边界。
metadata:
  short-description: HR SkillForge / HR方法论Skill锻造器
---

# HR SkillForge / HR 方法论锻造器

This Skill forges company-specific HR methodology Skills from public evidence about consulting firms, benchmark companies, and HR software companies. It does not write company profiles; it generates reusable `SKILL.md` files that help users solve real HR, organization, talent, performance, rewards, leadership, and change-management problems.  
本 Skill 是“HR咨询公司 / 标杆公司方法论 Skill 锻造器”。目标不是总结公司介绍，而是生成一个可复制使用的 company-specific `SKILL.md`，让用户能用目标公司的公开方法论视角解决 HR、组织、人才、绩效、激励、领导力和变革管理问题。

## Core Principles / 核心原则

- Input is a company or institution name; output is an installable Skill, not a research report. / 输入是公司或机构名称，输出是可安装 Skill，不是研究报告。
- Use public sources, user-authorized sources, and compliant video subtitles/transcripts. / 必须使用公开资料、用户授权资料和合规可处理的视频字幕。
- Video, webinar, interview, and podcast transcripts are high-weight sources and must not be skipped. / 视频、Webinar、访谈、播客 transcript 是高权重资料源，不能省略。
- Every source should become a source card, and every core judgment should be traceable. / 所有资料都要生成 source card，所有核心判断都要能追溯来源。
- If evidence is insufficient, generate a `Light Version`; do not fabricate a complete methodology. / 资料不足时生成 `Light Version`，不能硬编完整方法论。
- Do not bypass login, CAPTCHA, membership, private-video restrictions, or platform controls. / 不绕过登录、验证码、会员、私密视频或平台风控。

## Default Workflow / 默认工作流

```text
target_name + target_type / 目标名称 + 目标类型
-> init target directory / 初始化目标目录
-> create or read sources.csv / 创建或读取来源清单
-> check search provider availability, optionally install anysearch-skill / 检查搜索工具，必要时安装 anysearch-skill
-> generate query matrix, source-card search plan, and video search plan / 生成关键词矩阵、证据卡搜索计划和视频搜索计划
-> fetch web pages, PDFs, transcripts, video subtitles, manual files / 抓取网页、PDF、转写、视频字幕和手工资料
-> clean transcripts / 清洗转写文本
-> create source cards with evidence score / 生成带证据评分的 source cards
-> merge into 7 research files / 合并为七类研究文件
-> build company-specific SKILL.md / 生成公司专属 SKILL.md
-> quality_check -> quality-report.md / 质量检查并生成质量报告
```

## Seven Research Agents / 七类 Research Agent

| Agent | Output | Focus / 重点 |
|---|---|---|
| Official Methodology / 官方方法论 | `01-official-methodology.md` | Official frameworks, definitions, formal methodologies / 官方框架、概念定义、正式方法论 |
| Video Transcripts / 视频字幕 | `02-video-transcripts.md` | Consultant explanations, Q&A wording, real explanation sequence / 顾问解释框架、问答口径、真实表达顺序 |
| Case Practices / 案例实践 | `03-case-practices.md` | Implementation paths, project playbooks, management actions / 落地路径、项目打法、管理动作 |
| Tools and Frameworks / 工具模板 | `04-tools-and-frameworks.md` | Diagnostic tables, models, scorecards, SOPs / 诊断表、模型、评分卡、SOP |
| External Views / 外部评价 | `05-external-views.md` | Limitations, controversy, blind spots, boundaries / 局限、争议、盲点、适用边界 |
| Timeline / 时间线 | `06-timeline.md` | Recent changes, trends, outdated risks / 最近两年变化、趋势、过时风险 |
| China Localization / 中国落地 | `07-china-localization.md` | Chinese sources, China contexts, localization conversion / 中文资料、中国企业场景、本土化转换 |

## Video Subtitle Rules / 视频字幕硬规则

Video is not auxiliary. Formal distillation must process at least one round of video/subtitle sources.  
视频资料不是辅助资料。正式蒸馏必须至少处理一轮视频/字幕来源。

Priority / 优先级：

```text
official transcript / podcast transcript / 官方 transcript 或播客 transcript
-> YouTube/Bilibili manual subtitles / YouTube/Bilibili 人工字幕
-> YouTube/Bilibili auto subtitles / YouTube/Bilibili 自动字幕
-> user-authorized local audio/video transcription / 用户授权本地音视频转写
-> video page metadata / 视频页面信息
-> no subtitles, record failure / 无字幕，记录失败
```

When using `yt-dlp`, download subtitles only, not video files.  
使用 `yt-dlp` 时只下载字幕，不下载视频：

```powershell
yt-dlp --list-subs "VIDEO_URL"
yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs "en-orig,en,en-US,en-GB,zh-Hans,zh-Hant,zh,zh-CN,zh-TW" --sub-format "srt/vtt/best" "VIDEO_URL"
```

If YouTube requires login or triggers anti-bot restrictions, stop automatic capture, record the item in `pending_transcription.md`, and ask the user for an authorized transcript or local file. Do not bypass platform controls.  
如果 YouTube 要求登录或触发反机器人限制，停止自动抓取，记录到 `pending_transcription.md`，提示用户提供授权 transcript 或本地文件。不要绕过平台限制。

Do not stop distillation after YouTube fails; immediately expand to:  
YouTube 失败后不能停止蒸馏，应立即扩展到：

- 官网 transcript / webinar / podcast
- Bilibili
- Vimeo
- LinkedIn Events
- Apple Podcasts / Spotify
- 小宇宙 / 喜马拉雅
- SHRM / Gartner / HR Tech / WorldatWork / CIPD / ATD
- Thinkers50 / TED / 商学院公开课

## Search Enhancement: anysearch-skill / 搜索增强：anysearch-skill

If the user asks for broader coverage, automated search, batch retrieval, or GitHub `anysearch-skill`, use `anysearch-skill` as the search enhancement layer. It does not replace source cards, evidence scoring, or video-subtitle rules; it only expands discovery across web pages, PDFs, video pages, podcast pages, and full-text content.  
如果用户要求扩大搜索量、自动化搜索、批量检索或“调用 GitHub 上的 anysearch-skill”，优先使用 `anysearch-skill` 作为搜索增强层。它不能替代 source card、证据评分和视频字幕规则，只负责更大规模地发现网页、PDF、视频页、播客页和全文内容。

Prefer source-card-driven search: define the evidence cards first, then ask anysearch to search by card type instead of only running broad keyword searches. Core card types include:  
搜索时优先采用 source-card-driven search：先定义要填充的证据卡，再让 anysearch 按卡片类型检索，而不是只做宽泛关键词搜索。核心卡片类型包括：

- `official_methodology`: official methodologies, model definitions, white papers / 官方方法论、模型定义、白皮书。
- `diagnostic_question`: diagnostic questions, maturity models, assessment logic / 诊断问题、成熟度模型、评估逻辑。
- `tool_template`: scorecards, checklists, templates, toolkits / 评分卡、清单、模板、工具包。
- `case_practice`: client cases, implementation paths, management actions / 客户案例、实施路径、管理动作。
- `video_transcript`: webinars, podcasts, interviews, subtitles, transcripts / Webinar、播客、访谈、字幕、transcript。
- `external_boundary`: external views, controversy, limitations, failure conditions / 外部评价、争议、局限、失败条件。
- `china_localization`: China cases, Chinese wording, localization conversion / 中国案例、中文表达、本土化转换。

If a card type has fewer than three usable sources, do not only broaden generic keywords. Continue searching around that card type with methodology names, consultant names, report titles, conference names, client cases, and Chinese/English synonyms.  
如果某类卡片少于 3 个可用来源，不要只继续扩大泛关键词；应围绕该卡片继续搜索，并加入方法论名称、顾问姓名、报告标题、会议名、客户案例、中文/英文同义词等二级线索。

First check whether it is installed.  
先检查是否已安装：

```powershell
Test-Path "$env:USERPROFILE\.codex\skills\anysearch\SKILL.md"
```

If it is not installed, explain that a public GitHub skill will be downloaded, then run:  
如果没有安装，先向用户说明将从 GitHub 下载公开 skill，然后执行：

```powershell
$SkillRoot = "$env:USERPROFILE\.codex\skills"
$TempDir = Join-Path $env:TEMP "anysearch-skill-install"
New-Item -ItemType Directory -Force -Path $SkillRoot, $TempDir | Out-Null
Invoke-WebRequest -Uri "https://github.com/anysearch-ai/anysearch-skill/archive/refs/heads/main.zip" -OutFile (Join-Path $TempDir "anysearch-skill.zip")
Expand-Archive -Path (Join-Path $TempDir "anysearch-skill.zip") -DestinationPath $TempDir -Force
Remove-Item -Recurse -Force (Join-Path $SkillRoot "anysearch") -ErrorAction SilentlyContinue
Move-Item -Path (Join-Path $TempDir "anysearch-skill-main") -Destination (Join-Path $SkillRoot "anysearch")
Test-Path (Join-Path $SkillRoot "anysearch\SKILL.md")
```

API key is optional. Anonymous use may work but has lower quota.  
可选配置 API Key。没有 Key 也可匿名使用，但额度更低：

```powershell
$env:ANYSEARCH_API_KEY = "your_api_key_here"
```

After installation, run a smoke test.  
安装后做一次入口校验：

```powershell
python "$env:USERPROFILE\.codex\skills\anysearch\scripts\anysearch_cli.py" doc
```

If Python is unavailable, use Node or PowerShell.  
如果 Python 不可用，改用 Node 或 PowerShell：

```powershell
node "$env:USERPROFILE\.codex\skills\anysearch\scripts\anysearch_cli.js" doc
powershell -ExecutionPolicy Bypass -File "$env:USERPROFILE\.codex\skills\anysearch\scripts\anysearch_cli.ps1" doc
```

After installation, restart Codex so the new skill can be discovered. If the user does not want to install it, continue with this Skill's query matrix, browser search, and manual `sources.csv` workflow.  
安装完成后建议重启 Codex，让新 skill 被自动发现。若用户不想安装，继续使用本 skill 的 query matrix、浏览器搜索和手工 `sources.csv` 流程。

## Scripts / 使用脚本

Default project root:  
项目默认路径：

```text
PROJECT_ROOT/
```

Example command / 运行示例：

```powershell
python scripts/run_pipeline.py --target "Mercer" --type consulting_company --mode mvp
```

If Python is unavailable, use the scripts as an executable specification first; run them after Python is installed.  
如果当前机器没有 Python，可以先使用脚本作为生成规范；安装 Python 后再运行。

## When To Read Reference Files / 何时读取参考文件

- Search strategy and query matrix / 搜索策略和 query matrix：read `references/research-framework.md`。
- anysearch installation and usage / anysearch 安装和使用策略：read `references/anysearch-search-provider.md`。
- Source-card-driven search / source card 反向驱动搜索：read `references/source-card-search-strategy.md`。
- Evidence scoring / 证据评分：read `references/evidence-scoring.md`。
- Video subtitle strategy / 视频字幕策略：read `references/video-source-strategy.md`。
- Extraction fields and source cards / 抽取字段和 source card：read `references/extraction-framework.md`。
- Quality gates / 质量门槛：read `references/quality-standard.md`。
