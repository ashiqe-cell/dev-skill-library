# Dev Skill Library

A shared, version-controlled home for the development skills used across Ashiq's coding projects and AI assistants.

## Purpose

Keep reusable workflows discoverable, maintainable, and consistent across Codex, Claude, and other compatible agent tools. Each skill lives once in this library; projects and assistants can install or link selected skills from here.

## Structure

- `skills/` — canonical skill folders, each with its own `SKILL.md` and any supporting scripts, templates, or examples.
- `catalog/` — live inventory, provenance, compatibility, and installation notes.
- `README.md` — library overview and contribution rules.

## Current installed-skill inventory

The live inventory in `catalog/installed-skills.csv` is generated from the current user-level Codex, Claude, and agent skill folders. These entries point to their installed locations; they are not copied into this repository. Review ownership and license before promoting an installed skill into `skills/`.

To refresh the inventory in PowerShell, run:

```powershell
$roots = @(
  @{ Tool = 'Codex'; Path = "$env:USERPROFILE\.codex\skills" },
  @{ Tool = 'Claude'; Path = "$env:USERPROFILE\.claude\skills" },
  @{ Tool = 'Agents'; Path = "$env:USERPROFILE\.agents\skills" }
)
$rows = foreach ($root in $roots) {
  Get-ChildItem -LiteralPath $root.Path -Directory -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $skillFile = Join-Path $_.FullName 'SKILL.md'
    if (Test-Path -LiteralPath $skillFile) {
      [pscustomobject]@{ tool = $root.Tool; name = $_.Name; path = $_.FullName; skill_md = $skillFile }
    }
  }
}
$rows | Export-Csv -LiteralPath "$env:USERPROFILE\Dev Skill Library\catalog\installed-skills.csv" -NoTypeInformation -Encoding utf8
```

`catalog\refresh-inventory.ps1` runs this refresh and also writes a Markdown summary.

## Adding a skill

1. Create a folder under `skills/` using a short, lowercase, hyphenated name.
2. Add a `SKILL.md` with a clear name, purpose, trigger conditions, workflow, and output expectations.
3. Record its source and license in `catalog/skills.csv`.
4. Mark it `company-authored`, `adapted`, or `third-party`; retain upstream attribution and license for adapted or third-party work.
5. Test it in a representative project before making it a default for all projects.

## Rules

- Never copy credentials, customer data, or project secrets into this library.
- Keep project-specific instructions in each project's own `AGENTS.md`.
- Pin external skills to a version or commit and review upstream changes before updating.
- Do not overwrite assistant-managed skill directories automatically; install explicitly through the target tool's supported mechanism.
- Prefer portable instructions and declare tool or platform requirements.

