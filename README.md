# HR Skill Distiller

把咨询公司、标杆企业或 HR 软件公司的公开资料，蒸馏成可调用的 company-specific HR 方法论 Skill。重点不是写公司介绍，而是形成一个能帮助用户解决组织、人才、绩效、薪酬、激励、领导力和 HR 转型问题的专家型 Skill。

## 1. 搜索方法

搜索采用“广覆盖 + 证据卡补洞”的方式。

第一层是 query matrix：

```text
Company Alias x HR Topic x Source Type x Time Range x Language
```

会同时覆盖英文名、中文名、旧名称、子品牌、代表性方法论名称，以及组织设计、人才战略、绩效管理、薪酬激励、领导力、HR 数字化等主题。

第二层是 source-card-driven search。先定义最终蒸馏需要哪些证据卡，再围绕证据缺口搜索：

```text
official_methodology
diagnostic_question
tool_template
case_practice
video_transcript
external_boundary
china_localization
```

当搜索量不足时，可以安装并调用 GitHub 上的 `anysearch-skill`，用它批量搜索网页、PDF、视频页、播客页和全文内容。搜索结果不会直接进入结论，必须先进入 `sources.csv`，再经过抓取、source card、证据评分和质量检查。

视频和字幕是高权重来源。搜索会扩展到 YouTube、Bilibili、Vimeo、官网 webinar、podcast transcript、LinkedIn Events、Apple Podcasts、Spotify、小宇宙、喜马拉雅、SHRM、Gartner HR、HR Tech、WorldatWork、CIPD、ATD、Thinkers50、TED 和商学院公开课。

## 2. 蒸馏框架

蒸馏目标是生成一个可使用的 `SKILL.md`，而不是资料摘要。

核心流程：

```text
target name
-> generate search plan
-> collect web / PDF / video transcript / podcast / manual sources
-> create source cards
-> score evidence quality
-> merge into research layers
-> extract mental models, tools, workflows, anti-patterns
-> build company-specific SKILL.md
-> quality report
```

研究层分为七类：

```text
01 official methodology
02 video transcripts
03 case practices
04 tools and frameworks
05 external views
06 timeline
07 China localization
```

每条资料会被整理成 source card，提取：

```text
HR / organization methodology
diagnostic question
tool / template
management action
applicable scenario
limitation
China localization implication
evidence level
source confidence
```

最终 Skill 必须包含：

```text
role and boundary
applicable scenarios
core mental models
tool layer
diagnostic workflow
evidence checklist
deliverables
anti-patterns
localization guidance
source and uncertainty boundary
```

如果资料不足，输出 Light Version 或 Usable Candidate，不硬编完整方法论。

## 3. 蒸馏后运用方法

生成后的 Skill 不是静态文章，而是解决问题时使用的专家工作流。

使用 Skill 回答复杂问题时，必须先回看原始资料：

```text
sources.csv
distillation report
source cards
web/PDF/transcript files
quality report
```

回答要区分三类内容：

```text
Evidence-supported: 原始资料直接支持
Synthesized judgment: 多个资料交叉归纳
Professional inference: 基于方法论推演，但资料没有直接说明
```

输出通常包括：

```text
core judgment
problem decomposition
evidence consulted
recommended tools
solution design
implementation steps
governance mechanism
risks and anti-patterns
evidence boundary
```

`examples/hay/` 提供了一个 Hay Group / Korn Ferry Hay-style HR 咨询专家案例，展示如何从公开资料蒸馏出岗位价值评估、工作架构、薪酬绩效治理、领导力气候和人才评估工具层。
