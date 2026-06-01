# HR SkillForge / HR 方法论锻造器

Forge company-specific HR expertise from public evidence.  
从公开证据中锻造可调用的公司级 HR 方法论专家。

HR SkillForge turns public materials from consulting firms, benchmark companies, and HR software companies into usable company-specific HR methodology Skills. It is not a company-profile writer; it is designed to help users solve real problems in organization design, talent, performance, compensation, incentives, leadership, and HR transformation.  
HR SkillForge 把咨询公司、标杆企业或 HR 软件公司的公开资料，锻造成可调用的 HR 方法论 Skill。重点不是写公司介绍，而是形成一个能帮助用户解决组织、人才、绩效、薪酬、激励、领导力和 HR 转型问题的专家型 Skill。

## Quick Start / 使用方法

Clone the repository and install dependencies.  
克隆仓库并安装依赖：

```powershell
git clone https://github.com/wangjile200888-eng/hr-skillforge.git
cd hr-skillforge
pip install -r requirements.txt
```

Create a target workspace and generate the first search plan.  
创建目标项目并生成第一轮搜索计划：

```powershell
python scripts/init_target.py --target "Hay" --type consulting_company
python scripts/search_sources.py --target "Hay"
```

Review the generated query files, search and collect sources, then fill `sources.csv`.  
查看生成的搜索文件，搜集资料，并填写 `sources.csv`：

```text
output/generated-skills/hay/research_plan/search_queries.csv
output/generated-skills/hay/research_plan/source_card_search_queries.md
output/generated-skills/hay/research_plan/video_search_queries.md
output/generated-skills/hay/sources.csv
```

For larger search coverage, optionally install `anysearch-skill` and use it to batch search the source-card queries.  
如果需要扩大搜索量，可以安装 `anysearch-skill`，用它批量执行 source-card 查询：

```powershell
$SkillRoot = "$env:USERPROFILE\.codex\skills"
$TempDir = Join-Path $env:TEMP "anysearch-skill-install"
New-Item -ItemType Directory -Force -Path $SkillRoot, $TempDir | Out-Null
Invoke-WebRequest -Uri "https://github.com/anysearch-ai/anysearch-skill/archive/refs/heads/main.zip" -OutFile (Join-Path $TempDir "anysearch-skill.zip")
Expand-Archive -Path (Join-Path $TempDir "anysearch-skill.zip") -DestinationPath $TempDir -Force
Remove-Item -Recurse -Force (Join-Path $SkillRoot "anysearch") -ErrorAction SilentlyContinue
Move-Item -Path (Join-Path $TempDir "anysearch-skill-main") -Destination (Join-Path $SkillRoot "anysearch")
```

Run the pipeline after `sources.csv` is ready.  
`sources.csv` 准备好后，运行完整流程：

```powershell
python scripts/run_pipeline.py --target "Hay" --type consulting_company --mode mvp
```

The generated Skill will appear here.  
生成后的 Skill 会出现在：

```text
output/generated-skills/hay/SKILL.md
```

Check the Hay example if you want to see a completed case first.  
如果想先看完整案例，可以查看：

```text
examples/hay/SKILL.md
examples/hay/distillation-report.md
examples/hay/sources.csv
```

## 1. Search Method / 搜索方法

Search combines broad coverage with evidence-card gap filling.  
搜索采用“广覆盖 + 证据卡补洞”的方式。

The first layer is a query matrix.  
第一层是 query matrix：

```text
Company Alias x HR Topic x Source Type x Time Range x Language
公司别名 x HR主题 x 资料类型 x 时间范围 x 语言
```

It covers English names, Chinese names, former names, sub-brands, signature methodologies, and HR topics such as organization design, talent strategy, performance management, compensation and rewards, leadership, and HR digital transformation.  
它会同时覆盖英文名、中文名、旧名称、子品牌、代表性方法论名称，以及组织设计、人才战略、绩效管理、薪酬激励、领导力、HR 数字化等主题。

The second layer is source-card-driven search. Define the evidence cards needed for the final Skill first, then search around evidence gaps.  
第二层是 source-card-driven search。先定义最终蒸馏需要哪些证据卡，再围绕证据缺口搜索：

```text
official_methodology      官方方法论
diagnostic_question       诊断问题
tool_template             工具模板
case_practice             案例实践
video_transcript          视频/字幕/转写
external_boundary         外部评价与边界
china_localization        中国落地
```

When search volume is insufficient, HR SkillForge can install and use the GitHub `anysearch-skill` to run batch searches across web pages, PDFs, video pages, podcast pages, and full-text content. Search results are not treated as conclusions; they must enter `sources.csv`, then pass through fetching, source cards, evidence scoring, and quality checks.  
当搜索量不足时，可以安装并调用 GitHub 上的 `anysearch-skill`，用它批量搜索网页、PDF、视频页、播客页和全文内容。搜索结果不会直接进入结论，必须先进入 `sources.csv`，再经过抓取、source card、证据评分和质量检查。

Video and subtitle sources are high-weight evidence. Search expands beyond web pages to YouTube, Bilibili, Vimeo, official webinars, podcast transcripts, LinkedIn Events, Apple Podcasts, Spotify, 小宇宙, 喜马拉雅, SHRM, Gartner HR, HR Tech, WorldatWork, CIPD, ATD, Thinkers50, TED, and business-school public lectures.  
视频和字幕是高权重来源。搜索会扩展到 YouTube、Bilibili、Vimeo、官网 webinar、podcast transcript、LinkedIn Events、Apple Podcasts、Spotify、小宇宙、喜马拉雅、SHRM、Gartner HR、HR Tech、WorldatWork、CIPD、ATD、Thinkers50、TED 和商学院公开课。

## 2. Distillation Framework / 蒸馏框架

The goal is to generate a usable `SKILL.md`, not a research summary.  
蒸馏目标是生成一个可使用的 `SKILL.md`，而不是资料摘要。

Core workflow / 核心流程：

```text
target name / 目标名称
-> generate search plan / 生成搜索计划
-> collect web, PDF, video transcript, podcast, manual sources / 收集网页、PDF、视频字幕、播客、手工资料
-> create source cards / 生成证据卡
-> score evidence quality / 证据质量评分
-> merge into research layers / 合并到研究层
-> extract mental models, tools, workflows, anti-patterns / 提炼心智模型、工具、流程、反模式
-> build company-specific SKILL.md / 生成公司专属 SKILL.md
-> quality report / 质量报告
```

Seven research layers / 七类研究层：

```text
01 official methodology      官方方法论
02 video transcripts         视频字幕与转写
03 case practices            案例实践
04 tools and frameworks      工具与框架
05 external views            外部评价
06 timeline                  时间线
07 China localization        中国落地
```

Each source is converted into a source card and used to extract structured patterns.  
每条资料会被整理成 source card，并用于提取结构化模式：

```text
HR / organization methodology     HR/组织方法论
diagnostic question               诊断问题
tool / template                   工具/模板
management action                 管理动作
applicable scenario               适用场景
limitation                        局限
China localization implication    中国落地启示
evidence level                    证据等级
source confidence                 来源可信度
```

The final Skill must include both thinking and execution layers.  
最终 Skill 必须同时包含思考层和执行层：

```text
role and boundary                 角色与边界
applicable scenarios              适用场景
core mental models                核心心智模型
tool layer                        工具层
diagnostic workflow               诊断流程
evidence checklist                证据清单
deliverables                      交付物
anti-patterns                     反模式
localization guidance             本土化指导
source and uncertainty boundary   来源与不确定性边界
```

If evidence is insufficient, the output must be marked as Light Version or Usable Candidate. It should not fabricate a complete methodology.  
如果资料不足，输出 Light Version 或 Usable Candidate，不硬编完整方法论。

## 3. Runtime Use / 蒸馏后运用方法

A generated Skill is not a static article; it is an expert workflow for solving real problems.  
生成后的 Skill 不是静态文章，而是解决问题时使用的专家工作流。

When using a Skill for complex questions, the agent must review original evidence first.  
使用 Skill 回答复杂问题时，必须先回看原始资料：

```text
sources.csv                       来源索引
distillation report               蒸馏报告
source cards                      证据卡
web / PDF / transcript files      网页/PDF/字幕转写文件
quality report                    质量报告
```

Answers must separate three types of content.  
回答要区分三类内容：

```text
Evidence-supported: source-backed claims
资料支持：原始资料直接支持

Synthesized judgment: cross-source synthesis
综合判断：多个资料交叉归纳

Professional inference: methodology-based reasoning beyond direct evidence
专业推断：基于方法论推演，但资料没有直接说明
```

Typical output structure / 常见输出结构：

```text
core judgment                     核心判断
problem decomposition             问题拆解
evidence consulted                已回看的证据
recommended tools                 推荐工具
solution design                   方案设计
implementation steps              实施步骤
governance mechanism              治理机制
risks and anti-patterns           风险与反模式
evidence boundary                 证据边界
```

`examples/hay/` contains a Hay Group / Korn Ferry Hay-style HR consulting expert case. It shows how public evidence can be distilled into job evaluation, work architecture, pay and performance governance, leadership climate, and talent assessment tools.  
`examples/hay/` 提供了一个 Hay Group / Korn Ferry Hay-style HR 咨询专家案例，展示如何从公开资料蒸馏出岗位价值评估、工作架构、薪酬绩效治理、领导力气候和人才评估工具层。
