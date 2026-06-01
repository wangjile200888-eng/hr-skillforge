# HR Nuwa Skill MVP

HR版女娲 Skill 生成器：把咨询公司、标杆公司或HR软件公司的公开资料蒸馏成可安装的 HR 方法论 `SKILL.md`。

## Quick Start

```powershell
cd D:\AI-Workspace\hr-nuwa-skill
python scripts/run_pipeline.py --target "Mercer" --type consulting_company --mode mvp
```

第一次运行会创建：

```text
output/generated-skills/{target_slug}/
```

然后把你搜集到的网页、PDF、视频、transcript、手工资料填入 `sources.csv`，再次运行 pipeline。

MVP 不自动绕过登录、验证码、会员或私密视频限制。

## Optional: Install anysearch-skill

当需要最大化搜索量时，可以把 GitHub 上的 `anysearch-skill` 安装到 Codex 技能目录，作为搜索增强层：

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

安装后建议重启 Codex，再继续运行 HR Nuwa。

## Example: Hay Group / Korn Ferry Hay

`examples/hay/` contains a distilled Hay-style HR consulting skill as a reference case:

- `examples/hay/SKILL.md`: distilled Hay/Korn Ferry Hay-style expert skill.
- `examples/hay/distillation-report.md`: source expansion and distillation summary.
- `examples/hay/quality-report.md`: quality gate result.
- `examples/hay/sources.csv`: curated source index.

The full local run also produced large fetched web/PDF/transcript caches under `output/`. These runtime caches are intentionally excluded from Git because they are large and should be regenerated or stored separately when needed.
