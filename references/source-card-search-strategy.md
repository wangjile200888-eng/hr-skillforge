# Source Card Driven Search

Source cards should drive search, not only summarize collected sources. Before searching, define the evidence cards the final Skill needs, then use anysearch or browser search to fill each card type.

## Why

Keyword matrix search finds many pages, but it can miss the exact evidence needed for distillation. Source-card-driven search turns every missing field into a search target.

## Evidence Card Types

| Card Type | What To Find | Typical Source |
|---|---|---|
| `official_methodology` | definitions, official frameworks, named models | official site, white paper, PDF |
| `diagnostic_question` | diagnostic questions, maturity model, assessment logic | toolkit, assessment page, webinar |
| `tool_template` | scorecard, checklist, worksheet, framework, SOP | toolkit, PDF, slide deck |
| `case_practice` | implementation steps, client cases, project actions | case study, customer story |
| `video_transcript` | consultant explanation, Q&A, speaking sequence | YouTube, Vimeo, podcast, webinar transcript |
| `external_boundary` | limitations, critique, failure modes, external views | analyst, academic, media, practitioner review |
| `china_localization` | Chinese cases, translated concepts, local adaptation | Chinese web, forums, public courses |

## Query Logic

For every target alias, generate queries by card type:

```text
{company} official methodology HR organization framework
{company} diagnostic questions organization capability
{company} tool template framework HR
{company} case study HR transformation organization design
{company} webinar transcript HR organization
{company} criticism limitation review HR methodology
{company} China HR case organization performance
```

Also generate Chinese queries:

```text
{公司名} 官方 方法论 组织 人才 绩效 薪酬
{公司名} 诊断 问题 组织能力 人才管理
{公司名} 工具 模板 评分卡 诊断表
{公司名} 案例 实践 组织变革 人才 绩效
{公司名} 视频 字幕 访谈 直播 回放
{公司名} 局限 评价 争议 方法论
{公司名} 中国 企业 案例 组织 人才 绩效 薪酬
```

## anysearch Usage

When anysearch is installed, run the source-card query set before or alongside the broad matrix. For each result, capture:

- query
- card type
- title
- URL
- source type
- language
- date if visible
- why it may fill the card
- whether full text or transcript was captured

Export candidates into `sources.csv`. Keep `source_card_type` where possible so later extraction knows what evidence gap the source was meant to fill.

## Search Expansion Rule

If a source card type has fewer than three usable sources, expand with:

1. target alias or former company name
2. named methodology from collected sources
3. consultant / author name
4. conference or webinar title
5. equivalent Chinese and English terms
6. PDF, transcript, webinar, toolkit, scorecard modifiers

## Distillation Rule

Do not allow a source card type to stay empty silently. Mark it as:

- `filled`: enough evidence to distill
- `thin`: limited evidence, usable with caution
- `empty`: no evidence, must not fabricate

The final Skill should include the strongest filled cards and explicitly state uncertainty for thin or empty cards.
