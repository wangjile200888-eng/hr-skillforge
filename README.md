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
  <a href="#technical-innovations--技术创新">Innovation / 技术创新</a>
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
