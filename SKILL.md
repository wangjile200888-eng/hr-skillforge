---
name: hr-nuwa-skill
description: HR版女娲 Skill 生成器。用于把咨询公司、HR咨询公司、标杆公司或HR软件公司的公开资料蒸馏成可安装的 company-specific HR/组织/人才/绩效/激励方法论 SKILL.md。工作流强调多源公开资料、公开视频字幕、source cards、证据评分、七类研究文件、质量检查和 Light Version 边界。适用于用户要求“蒸馏某公司HR方法论”“生成某咨询公司专家Skill”“参考视频字幕生成HR智脑”“把公开资料变成可用HR方法论Agent”等场景。
metadata:
  short-description: HR咨询/标杆公司方法论蒸馏器
---

# HR Nuwa Skill

本 Skill 是“HR咨询公司 / 标杆公司方法论蒸馏器”。目标不是总结公司介绍，而是生成一个可复制使用的 company-specific `SKILL.md`，让用户能用目标公司的公开方法论视角解决 HR、组织、人才、绩效、激励、领导力和变革管理问题。

## 核心原则

- 输入是公司或机构名称，输出是可安装 Skill，不是研究报告。
- 必须使用公开资料、用户授权资料和合规可处理的视频字幕。
- 视频 / Webinar / 访谈 / 播客 transcript 是高权重资料源，不能省略。
- 所有资料都要生成 source card，所有核心判断都要能追溯来源。
- 资料不足时生成 `Light Version`，不能硬编完整方法论。
- 不绕过登录、验证码、会员、私密视频或平台风控。

## 默认工作流

```text
target_name + target_type
-> init target directory
-> create / read sources.csv
-> check search provider availability, optionally install anysearch-skill
-> generate query matrix, source-card search plan, and video search plan
-> fetch web pages / PDFs / transcripts / video subtitles / manual files
-> clean transcripts
-> create source cards with evidence score
-> merge into 7 research files
-> build company-specific SKILL.md
-> quality_check -> quality-report.md
```

## 七类 Research Agent

| Agent | 输出文件 | 重点 |
|---|---|---|
| 官方方法论 | `01-official-methodology.md` | 官方框架、概念定义、正式方法论 |
| 视频字幕 | `02-video-transcripts.md` | 顾问解释框架、问答口径、真实表达顺序 |
| 案例实践 | `03-case-practices.md` | 落地路径、项目打法、管理动作 |
| 工具模板 | `04-tools-and-frameworks.md` | 诊断表、模型、评分卡、SOP |
| 外部评价 | `05-external-views.md` | 局限、争议、盲点、适用边界 |
| 时间线 | `06-timeline.md` | 最近两年变化、趋势、过时风险 |
| 中国落地 | `07-china-localization.md` | 中文资料、中国企业场景、本土化转换 |

## 视频字幕硬规则

视频资料不是辅助资料。正式蒸馏必须至少处理一轮视频/字幕来源。

优先级：

```text
官方 transcript / podcast transcript
-> YouTube/Bilibili 人工字幕
-> YouTube/Bilibili 自动字幕
-> 用户授权本地音视频转写
-> 视频页面信息
-> 无字幕，记录失败
```

使用 `yt-dlp` 时只下载字幕，不下载视频：

```powershell
yt-dlp --list-subs "VIDEO_URL"
yt-dlp --skip-download --write-subs --write-auto-subs --sub-langs "en-orig,en,en-US,en-GB,zh-Hans,zh-Hant,zh,zh-CN,zh-TW" --sub-format "srt/vtt/best" "VIDEO_URL"
```

如果 YouTube 要求登录或触发反机器人限制，停止自动抓取，记录到 `pending_transcription.md`，提示用户提供授权 transcript 或本地文件。不要绕过平台限制。

YouTube 失败后不能停止蒸馏，应立即扩展到：

- 官网 transcript / webinar / podcast
- Bilibili
- Vimeo
- LinkedIn Events
- Apple Podcasts / Spotify
- 小宇宙 / 喜马拉雅
- SHRM / Gartner / HR Tech / WorldatWork / CIPD / ATD
- Thinkers50 / TED / 商学院公开课

## 搜索增强：anysearch-skill

如果用户要求扩大搜索量、自动化搜索、批量检索或“调用 GitHub 上的 anysearch-skill”，优先使用 `anysearch-skill` 作为搜索增强层。它不能替代 source card、证据评分和视频字幕规则，只负责更大规模地发现网页、PDF、视频页、播客页和全文内容。

搜索时优先采用 source-card-driven search：先定义要填充的证据卡，再让 anysearch 按卡片类型检索，而不是只做宽泛关键词搜索。核心卡片类型包括：

- `official_methodology`：官方方法论、模型定义、白皮书。
- `diagnostic_question`：诊断问题、成熟度模型、评估逻辑。
- `tool_template`：评分卡、清单、模板、工具包。
- `case_practice`：客户案例、实施路径、管理动作。
- `video_transcript`：Webinar、播客、访谈、字幕、transcript。
- `external_boundary`：外部评价、争议、局限、失败条件。
- `china_localization`：中国案例、中文表达、本土化转换。

如果某类卡片少于 3 个可用来源，不要只继续扩大泛关键词；应围绕该卡片继续搜索，并加入方法论名称、顾问姓名、报告标题、会议名、客户案例、中文/英文同义词等二级线索。

先检查是否已安装：

```powershell
Test-Path "$env:USERPROFILE\.codex\skills\anysearch\SKILL.md"
```

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

可选配置 API Key。没有 Key 也可匿名使用，但额度更低：

```powershell
$env:ANYSEARCH_API_KEY = "your_api_key_here"
```

安装后做一次入口校验：

```powershell
python "$env:USERPROFILE\.codex\skills\anysearch\scripts\anysearch_cli.py" doc
```

如果 Python 不可用，改用 Node 或 PowerShell：

```powershell
node "$env:USERPROFILE\.codex\skills\anysearch\scripts\anysearch_cli.js" doc
powershell -ExecutionPolicy Bypass -File "$env:USERPROFILE\.codex\skills\anysearch\scripts\anysearch_cli.ps1" doc
```

安装完成后建议重启 Codex，让新 skill 被自动发现。若用户不想安装，继续使用本 skill 的 query matrix、浏览器搜索和手工 `sources.csv` 流程。

## 使用脚本

项目默认路径：

```text
D:/AI-Workspace/hr-nuwa-skill/
```

运行示例：

```powershell
python scripts/run_pipeline.py --target "Mercer" --type consulting_company --mode mvp
```

如果当前机器没有 Python，可以先使用脚本作为生成规范；安装 Python 后再运行。

## 何时读取参考文件

- 搜索策略和 query matrix：读取 `references/research-framework.md`。
- anysearch 安装和使用策略：读取 `references/anysearch-search-provider.md`。
- source card 反向驱动搜索：读取 `references/source-card-search-strategy.md`。
- 证据评分：读取 `references/evidence-scoring.md`。
- 视频字幕策略：读取 `references/video-source-strategy.md`。
- 抽取字段和 source card：读取 `references/extraction-framework.md`。
- 质量门槛：读取 `references/quality-standard.md`。
