param(
  [Parameter(Mandatory=$true)][string]$Url,
  [Parameter(Mandatory=$true)][string]$OutputDir,
  [string]$Langs = "en-orig,en,en-US,en-GB,zh-Hans,zh-Hant,zh,zh-CN,zh-TW"
)

New-Item -ItemType Directory -Force -Path $OutputDir | Out-Null

$yt = Get-Command yt-dlp -ErrorAction SilentlyContinue
if (-not $yt) {
  $candidates = Get-ChildItem -Path "$env:LOCALAPPDATA\Microsoft\WinGet" -Recurse -Filter yt-dlp.exe -ErrorAction SilentlyContinue
  if ($candidates.Count -gt 0) { $yt = $candidates[0] }
}

if (-not $yt) {
  Write-Error "yt-dlp not found. Install with: winget install yt-dlp.yt-dlp"
  exit 1
}

& $yt.Source --list-subs --no-download $Url

& $yt.Source `
  --skip-download `
  --write-subs `
  --write-auto-subs `
  --sub-langs $Langs `
  --sub-format "srt/vtt/best" `
  -o "$OutputDir/%(upload_date)s_%(title).120s_%(id)s.%(ext)s" `
  $Url
