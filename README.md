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
  <a href="#effect-examples--效果示例">Examples / 效果示例</a> ·
  <a href="#local-commands--本地运行命令">Local Commands / 本地命令</a> ·
  <a href="#technical-implementation--技术实现">Implementation / 技术实现</a>
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

## Technical Implementation / 技术实现

**1. Evidence-First Search Engine / 证据优先的搜索引擎**

Search is designed as a multi-layer evidence acquisition system, not a simple keyword lookup.  
搜索不是简单关键词检索，而是一个多层证据采集系统。

```text
Search method / 搜索方法:
Company aliases x HR topics x source types x time ranges x languages
公司别名 x HR主题 x 资料类型 x 时间范围 x 语言

Source-card search / 证据卡搜索:
official_methodology, diagnostic_question, tool_template,
case_practice, video_transcript, external_boundary, china_localization

Search terms / 搜索词:
white paper, report, PDF, case study, webinar, podcast, transcript,
framework, toolkit, maturity model, diagnostic, leadership, rewards,
组织能力, 绩效管理, 薪酬激励, 领导力, 诊断表, 工具, 案例, 字幕

Search tools / 搜索工具:
query matrix, anysearch-skill, browser search, official-site crawl,
yt-dlp subtitles, manual sources

Search scope / 搜索范围:
official websites, PDFs, reports, YouTube, Bilibili, Vimeo, podcasts,
LinkedIn Events, SHRM, Gartner HR, HR Tech, WorldatWork, CIPD, ATD,
Thinkers50, TED, business-school lectures, Chinese HR platforms

Search preference / 搜索偏好:
official sources > video transcripts > tools/templates > cases >
external critique > Chinese localization > generic summaries
官方来源 > 视频字幕 > 工具模板 > 案例实践 > 外部评价 > 中国落地 > 泛泛摘要
```

**2. Distillation Architecture / 方法论蒸馏架构**

HR SkillForge turns raw evidence into an executable expert Skill through a layered distillation pipeline.  
HR SkillForge 通过分层蒸馏管线，把原始证据转成可执行的专家 Skill。

```text
Raw sources / 原始资料
-> source cards / 证据卡
-> evidence scoring / 证据评分
-> seven research layers / 七类研究层
-> mental models / 心智模型
-> tool layer / 工具层
-> diagnostic workflow / 诊断流程
-> deliverables / 交付物
-> anti-patterns / 反模式
-> uncertainty boundary / 不确定性边界
-> company-specific SKILL.md / 公司专属 Skill
```

The seven research layers are built to prevent shallow summarization.  
七类研究层用于避免“浅层总结”：

```text
official methodology      官方方法论
video transcripts         视频字幕
case practices            案例实践
tools and frameworks      工具框架
external views            外部评价
timeline                  时间线
China localization        中国落地
```

The final Skill must contain not only concepts, but also tools: diagnostic canvases, evidence sheets, matrices, workflows, governance mechanisms, and delivery templates.  
最终 Skill 不只保留概念，还必须沉淀工具：诊断画布、证据表、矩阵、工作流、治理机制和交付模板。

**3. Runtime Evidence Recall / 运行时证据回看**

Generated Skills are not allowed to answer only from memory. For complex problems, they should consult the original distillation materials before making strong claims.  
生成后的 Skill 不能只凭“蒸馏后的印象”回答复杂问题，而要在强判断前回看原始蒸馏材料。

```text
Runtime recall / 运行时回看:
sources.csv
distillation report
source cards
web / PDF / transcript files
quality report

Answer boundary / 回答边界:
Evidence-supported       资料支持
Synthesized judgment     综合判断
Professional inference   专业推断
```

This turns a generated Skill from a writing style into a traceable expert system: it knows where its claims came from, what is inferred, and what still needs verification.  
这让生成后的 Skill 不只是“回答风格”，而是一个可追溯的专家系统：它知道判断来自哪里、哪些是推断、哪些还需要继续验证。
