<h1 align="center">HR SkillForge / HR 方法论锻造器</h1>

<p align="center"><em>「把公开资料，锻造成可调用的 HR 专家」</em></p>
<p align="center"><em>"Forge public evidence into usable HR expertise."</em></p>

<p align="center">
  <img alt="License" src="https://img.shields.io/badge/License-MIT-yellow">
  <img alt="Skill" src="https://img.shields.io/badge/Codex-Skill-7B2FF7">
  <img alt="HR" src="https://img.shields.io/badge/Domain-HR%20%7C%20Organization-blue">
  <img alt="Evidence" src="https://img.shields.io/badge/Evidence-Source%20Cards-green">
  <img alt="Bilingual" src="https://img.shields.io/badge/Docs-English%20%2F%20中文-orange">
</p>

<p align="center"><strong>HR SkillForge helps HRDs, consultants, OD professionals, and founders distill consulting-firm and benchmark-company know-how into practical Skills.</strong></p>
<p align="center"><strong>HR SkillForge 帮助 HRD、咨询顾问、组织发展从业者和创业者，把咨询公司与标杆企业的方法论蒸馏成可直接使用的 Skill。</strong></p>

<p align="center">
  <a href="examples/hay/SKILL.md">View Hay Example / 查看 Hay 案例</a> ·
  <a href="#how-to-use--如何使用">How to Use / 使用方法</a> ·
  <a href="#1-search-method--搜索方法">Search / 搜索方法</a> ·
  <a href="#2-distillation-framework--蒸馏框架">Framework / 蒸馏框架</a> ·
  <a href="#3-runtime-use--蒸馏后运用方法">Runtime Use / 运用方法</a>
</p>

## How To Use / 如何使用

You only need to give it a target company or methodology source. HR SkillForge then guides evidence search, source-card extraction, methodology distillation, and runtime use.  
你只需要输入一个目标公司或方法论来源。HR SkillForge 会引导完成资料搜索、证据卡抽取、方法论蒸馏和后续应用。

For example / 例如：

```text
Distill Hay Group into an HR consulting expert Skill.
把 Hay Group 蒸馏成一个 HR 咨询专家 Skill。

Distill Mercer into a total rewards and organization design Skill.
把 Mercer 蒸馏成一个总回报与组织设计 Skill。

Distill a benchmark company into a performance-management Skill.
把某家标杆企业蒸馏成绩效管理 Skill。
```

The generated Skill is then used like a specialist advisor. It should answer real HR problems with its distilled tools, while checking the original source cards and evidence files before making strong claims.  
生成后的 Skill 会像一个专门领域顾问一样使用。它要用蒸馏出的工具帮助用户解决真实 HR 问题，同时在给出强判断前回看原始 source cards 和证据文件。

Main outputs / 主要输出：

```text
company-specific SKILL.md          公司专属 Skill
source cards                       证据卡
distillation report                蒸馏报告
quality report                     质量报告
evidence-backed tool layer         有证据支撑的工具层
```

Local run commands are available in [Local Commands / 本地运行命令](#local-commands--本地运行命令).  
本地运行命令见 [Local Commands / 本地运行命令](#local-commands--本地运行命令)。

## Effect Examples / 效果示例

```text
User / 用户
> 我们集团岗位职级很乱，老员工、头衔、薪酬、绩效都搅在一起。怎么从0到1重建？

Hay Skill / Hay 方法论 Skill
> 先不要直接定级，也不要先调薪。
> Hay-style 的第一步是把四件事拆开：
> Job / 岗位：这个岗位本身创造多大价值？
> Person / 人：任职者是否胜任？
> Performance / 绩效：今年结果如何？
> Pay / 薪酬：薪酬在市场和内部区间里处于什么位置？
>
> 你的问题不是“职级表不够细”，而是岗位价值、个人贡献和薪酬治理混在一起。
> 先选20-30个标杆岗位，用 Know-How、Problem Solving、Accountability 做证据访谈；
> 再建岗位族、职级矩阵和薪酬带。个人薪酬放到最后，用绩效和市场数据校准。
```

```text
User / 用户
> 销售团队绩效不好，老板想加大考核和末位淘汰。

Hay Skill / Hay 方法论 Skill
> 先判断这是绩效问题，还是组织气候问题。
> 如果目标不清、授权不足、反馈很少、跨部门支持弱，加大考核只会放大焦虑。
>
> 我会先做 Leadership Style and Climate Audit：
> 1. 销售目标是否被翻译成可控行为？
> 2. 主管是 coaching，还是只在月底追责？
> 3. 资源、价格、交付、线索质量是否支持销售完成目标？
> 4. 绩效差异来自能力、区域、客户结构，还是管理方式？
>
> 如果气候问题没解决，末位淘汰不是绩效工具，而是信任消耗器。
```

```text
User / 用户
> 我们想学习 Hay 的岗位价值评估，能不能直接给每个岗位打分？

Hay Skill / Hay 方法论 Skill
> 不能直接伪造 Hay 官方分数。
> 正式岗位评估需要授权工具、训练过的评估者、岗位访谈和评审校准。
>
> 但可以先做一个合规的 Work Value Diagnostic：
> - 这个岗位需要什么 Know-How？
> - 它解决的问题复杂度在哪里？
> - 它对结果承担什么 Accountability？
> - 它和相邻岗位的价值差异是什么？
>
> 输出不是官方点值，而是岗位价值证据表、岗位轮廓判断和是否需要正式评估的建议。
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

## Local Commands / 本地运行命令

Clone and install / 克隆并安装：

```powershell
git clone https://github.com/wangjile200888-eng/hr-skillforge.git
cd hr-skillforge
pip install -r requirements.txt
```

Create a target and generate search plans / 创建目标并生成搜索计划：

```powershell
python scripts/init_target.py --target "Hay" --type consulting_company
python scripts/search_sources.py --target "Hay"
```

Fill `sources.csv`, then run the pipeline / 填写 `sources.csv` 后运行流程：

```powershell
python scripts/run_pipeline.py --target "Hay" --type consulting_company --mode mvp
```

Generated output / 生成结果：

```text
output/generated-skills/hay/SKILL.md
```

## Technical Innovations / 技术创新

**1. Search as Evidence Hunting / 搜索不是找网页，是找证据**

HR SkillForge does not only search keywords. It searches for missing source cards: official methodology, diagnostic questions, tools, cases, video transcripts, external boundaries, and China localization.  
HR SkillForge 不只是搜关键词，而是按“缺哪类证据卡”去搜：官方方法论、诊断问题、工具模板、案例实践、视频字幕、外部边界、中国落地。

**2. Distillation as Skill Building / 蒸馏不是总结，是造一个能工作的 Skill**

It turns source cards into mental models, tool layers, workflows, deliverables, anti-patterns, and uncertainty boundaries. The output is a usable expert Skill, not a prettier research note.  
它把 source cards 转成心智模型、工具层、工作流、交付物、反模式和不确定性边界。输出不是更漂亮的研究笔记，而是一个能工作的专家 Skill。

**3. Runtime With Source Recall / 使用时不凭印象，会回看蒸馏材料**

When answering real questions, the generated Skill should consult its original sources, source cards, transcripts, and quality report before making strong claims.  
真正解决问题时，生成的 Skill 不只调用“蒸馏后的印象”，还会回看原始资料、source cards、视频转写和质量报告，再给出判断。
