# anysearch Search Provider

anysearch-skill is an optional search enhancement layer for HR SkillForge. Use it when the user asks to maximize source collection, run broad search, batch query many combinations, or connect to the GitHub anysearch skill.

## Role

anysearch helps with:

- broad web search
- batch search across the query matrix
- video page discovery
- PDF and report discovery
- full-text extraction where supported
- exporting candidates into `sources.csv`

It does not replace:

- evidence scoring
- source cards
- video subtitle download
- transcript cleaning
- quality report
- final methodology distillation

## Installation Check

```powershell
Test-Path "$env:USERPROFILE\.codex\skills\anysearch\SKILL.md"
```

If the result is `True`, read that `SKILL.md` and follow its local instructions.

## Install From GitHub

Explain to the user that this downloads the public GitHub repository into the local Codex skills folder.

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

If GitHub changes the default branch or directory name, use the repository's latest installation instructions.

## Optional API Key

```powershell
$env:ANYSEARCH_API_KEY = "your_api_key_here"
```

Without an API key, anonymous usage may work but has lower quota and less reliability.

## Smoke Test

Try Python first:

```powershell
python "$env:USERPROFILE\.codex\skills\anysearch\scripts\anysearch_cli.py" doc
```

If Python is unavailable, try Node or PowerShell:

```powershell
node "$env:USERPROFILE\.codex\skills\anysearch\scripts\anysearch_cli.js" doc
powershell -ExecutionPolicy Bypass -File "$env:USERPROFILE\.codex\skills\anysearch\scripts\anysearch_cli.ps1" doc
```

After installation, restart Codex so the new skill can be discovered automatically.

## HR SkillForge Usage Pattern

1. Generate `research_plan/search_queries.csv`.
2. Run anysearch against source-card-driven query groups first:
   - official methodology card
   - diagnostic question card
   - tool/template card
   - case practice card
   - video/transcript card
   - external boundary card
   - China localization card
3. Then run anysearch against the broad query matrix:
   - official methodology
   - video/webinar/transcript
   - case study
   - tools/frameworks
   - China localization
4. Export candidate results into `sources.csv`.
5. Mark each row with source type: `web`, `pdf`, `video`, `transcript`, `podcast`, or `manual`.
6. Preserve `source_card_type` when possible, so the pipeline can tell which evidence gap the source was meant to fill.
7. Continue the normal HR SkillForge pipeline.

## Source Card Search Method

Use source cards as search briefs. Each card type becomes a query family:

| Card Type | anysearch Query Intent |
|---|---|
| `official_methodology` | official definitions, named models, white papers |
| `diagnostic_question` | diagnostic questions, maturity models, assessments |
| `tool_template` | scorecards, templates, checklists, toolkits |
| `case_practice` | client stories, implementation cases, operating steps |
| `video_transcript` | webinars, podcasts, interviews, captions, transcripts |
| `external_boundary` | criticism, limitations, analyst views, practitioner reviews |
| `china_localization` | Chinese cases, Chinese terms, local adaptation |

If a card type has fewer than three usable sources, run another anysearch round using extracted names: methodology names, consultant names, report titles, conference names, client cases, and Chinese/English synonyms.

## Quality Rule

Search volume is useful only when it increases usable evidence. Prioritize sources that contain:

- consultant explanation
- methodology definitions
- practical tools
- case implementation details
- transcripts or captions
- recent updates
- independent criticism or boundary conditions
