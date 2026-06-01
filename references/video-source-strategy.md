# Video Source Strategy

Video is a first-class source for HR SkillForge. It captures how consultants explain frameworks, answer follow-up questions, sequence cases, and translate abstract models into management actions.

## Video Search Terms

English:

```text
{company} HR webinar
{company} organization design webinar
{company} talent strategy interview
{company} leadership development podcast
{company} performance management video
{company} people analytics webinar
{company} CHRO interview
{company} HR transformation conference
{company} keynote organization capability
{company} human capital trends webinar
{company} total rewards webinar
{company} sales incentive webinar
```

Chinese:

```text
{公司名} 人力资源 视频
{公司名} 组织能力 访谈
{公司名} 绩效管理 直播
{公司名} 人才管理 论坛
{公司名} 组织发展 公开课
{公司名} CHRO 访谈
{公司名} 干部管理 演讲
{公司名} 薪酬绩效 视频
{公司名} 销售激励 直播
```

## Platforms

| Platform | Value | MVP handling |
|---|---|---|
| Official website transcript | Highest-quality official video/audio text | Fetch as web/transcript source |
| Official webinar pages | Methodology explanation and Q&A | Fetch page; record replay/transcript |
| Official podcast pages | Expert discussion, leadership/HR opinions | Fetch show notes/transcript |
| YouTube | Global consulting webinars, podcasts, conference clips | `yt-dlp`; if blocked, record pending |
| Bilibili | Chinese forums, public classes, translated consulting videos | `yt-dlp` where possible; otherwise manual transcript |
| Vimeo | Conference and consulting event replays | `yt-dlp` where possible |
| LinkedIn Events / Video | Consultant talks and webinar announcements | Manual/source card; no login bypass |
| Apple Podcasts / Spotify | Expert interviews and official podcasts | Prefer transcript/show notes pages |
| 小宇宙 / 喜马拉雅 | Chinese HR interviews and courses | Manual/source card; transcript if provided |
| SHRM / Gartner / HR Tech / WorldatWork / CIPD / ATD | HR conference replays and expert sessions | Fetch public agenda/replay/transcript |
| Thinkers50 / TED / business schools | Leadership and organization talks | Fetch public transcript/video pages |

## Processing Order

```text
public video URL
-> yt-dlp --list-subs
-> download manual subtitles
-> fallback to automatic subtitles
-> clean transcript
-> source card
-> 02-video-transcripts.md
```

If no subtitles exist and the user provides authorized local audio/video, use transcription. MVP records unsupported items in `pending_transcription.md`.

## Fallback Rule

Do not stop at YouTube failure. If YouTube subtitles cannot be collected because of login, bot checks, or missing captions, immediately expand to:

1. official transcript / webinar / podcast pages
2. Bilibili and Vimeo
3. conference websites
4. podcast platforms and show notes
5. business-school public lectures
6. Chinese video/course platforms

Every failed video attempt must still be recorded with title, URL, platform, failure reason, and next suggested channel.

## Compliance

Do not bypass login, CAPTCHA, paywalls, member-only access, private video restrictions, or platform anti-abuse controls. If blocked, record the URL and reason.
