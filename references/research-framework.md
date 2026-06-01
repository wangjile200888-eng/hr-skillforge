# Research Framework

## Target Types

| target_type | Examples | Focus |
|---|---|---|
| `consulting_company` | McKinsey, BCG, Mercer, Korn Ferry, Hay, Deloitte, PwC, 北森 | 方法论、诊断框架、工具、项目语言、适用场景 |
| `benchmark_company` | 华为、宝洁、Costco、丰田、阿里、字节 | 组织机制、人才标准、干部体系、绩效激励、文化机制 |
| `hr_software_company` | Workday, SAP SuccessFactors, Moka, 飞书人事 | 产品逻辑、数据模型、HR SaaS实践、数字化落地 |
| `auto` | 用户不确定 | 根据关键词初步判断 |

## Query Matrix

Every target should generate queries from:

```text
Company Alias x HR Topic x Source Type x Time Range x Language
```

### Company Alias

Include:

- English legal/common name
- Acronym
- Chinese name
- Former name
- Sub-brand / practice name
- Signature methodology name

### HR Topics

```text
organization capability
organization design
operating model
HR operating model
HRBP
COE
shared services
talent strategy
key roles
talent to value
leadership development
leadership model
performance management
incentive
compensation
rewards
total rewards
culture transformation
people analytics
HR digital transformation
AI in HR
组织能力
组织设计
人才战略
绩效管理
薪酬绩效
激励
领导力
干部管理
组织发展
```

### Source Types

```text
white paper
report
PDF
case study
webinar
podcast
interview
transcript
presentation
slides
framework
toolkit
maturity model
diagnostic
survey
白皮书
报告
案例
视频
访谈
直播
播客
字幕
课件
PPT
工具
模型
成熟度
诊断表
调研
```

### Time Ranges

```text
classic
last 3 years
last 12 months
2026
2025
2024
latest
new report
annual report
trend report
最新
趋势报告
年度报告
调研报告
```

## Search Channels

| Channel | MVP handling |
|---|---|
| anysearch-skill | Preferred enhanced provider when installed; use for broad web search, batch query expansion, full-text extraction, and search result export |
| Keyword Search | Generate queries for manual/browser search |
| Official Site Crawl | Read sitemap and candidate paths if official domains are provided |
| Video Search | Generate video-specific search terms; process links in `sources.csv` |
| PDF/PPT Search | Add `filetype:pdf`, `presentation`, `slides`, `PPT` |
| Chinese Localization | Always generate Chinese queries |
| JD Search | Required for benchmark companies |

## Search Provider Order

When the user wants maximum search coverage, use this order:

```text
1. anysearch-skill if installed or user agrees to install it
2. Browser / web search for current public pages
3. Official site and sitemap checks
4. Video platform search queries
5. User-provided manual sources
```

anysearch is a discovery and extraction tool. It must still feed results into `sources.csv`; do not treat search snippets as final evidence unless the full page, PDF, transcript, or video page has been captured and scored.

## Snowball Expansion

From high-quality sources extract:

- author / consultant name
- report title
- methodology name
- model name
- client case
- conference
- partner institution
- repeated keywords

If an entity appears in 3+ high-quality sources, add it to the next search round.

## Video Platform Matrix

Video search must not rely only on YouTube. Generate platform-specific queries for:

- YouTube
- Bilibili
- Vimeo
- LinkedIn Events
- Apple Podcasts / Spotify
- 小宇宙 / 喜马拉雅
- SHRM
- Gartner HR
- HR Tech Conference
- WorldatWork
- CIPD
- ATD
- Thinkers50
- TED / TEDx
- business school websites

Example platform queries:

```text
site:youtube.com {company} HR webinar
site:bilibili.com {company} 组织能力 访谈
site:vimeo.com {company} leadership development
site:podcasts.apple.com {company} HR podcast
site:shrm.org {company} webinar talent
site:worldatwork.org {company} total rewards
site:cipd.org {company} leadership
site:hbr.org {company} leadership interview
```
