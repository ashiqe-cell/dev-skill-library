# Installed skill inventory refresh
$ErrorActionPreference = 'Stop'

$libraryRoot = Split-Path -Parent $PSScriptRoot
$roots = @(
    @{ Tool = 'Codex'; Path = Join-Path $env:USERPROFILE '.codex\skills' },
    @{ Tool = 'Claude'; Path = Join-Path $env:USERPROFILE '.claude\skills' },
    @{ Tool = 'Agents'; Path = Join-Path $env:USERPROFILE '.agents\skills' }
)

$rows = foreach ($root in $roots) {
    if (Test-Path -LiteralPath $root.Path) {
        Get-ChildItem -LiteralPath $root.Path -Directory -Force | ForEach-Object {
            if (Test-Path -LiteralPath (Join-Path $_.FullName 'SKILL.md')) {
                [pscustomobject]@{
                    tool = $root.Tool
                    name = $_.Name
                    source = 'user-level installation'
                }
            }
        }
    }
}

$rows | Sort-Object tool, name | Export-Csv -LiteralPath (Join-Path $PSScriptRoot 'installed-skills.csv') -NoTypeInformation -Encoding utf8
$counts = $rows | Group-Object tool | Sort-Object Name
$lines = @(
    '# Installed skills inventory',
    '',
    "Generated: $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss zzz')",
    '',
    'This inventory lists skill names and assistant source only. It does not copy skill contents or claim ownership.',
    '',
    '| Assistant | Skills found |',
    '|---|---:|'
)
foreach ($count in $counts) { $lines += "| $($count.Name) | $($count.Count) |" }
$lines += ''
$lines += 'See `installed-skills.csv` for the skill names and assistant source.'
$lines | Set-Content -LiteralPath (Join-Path $PSScriptRoot 'installed-skills.md') -Encoding utf8
Write-Host "Indexed $($rows.Count) installed skills (names only)."
