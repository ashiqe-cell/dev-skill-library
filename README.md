# Dev Skill Library

A shared, version-controlled catalog for reusable coding skills across Codex, Claude, and compatible agent tools.

## Layout

- `skills/` — canonical skill folders, each with `SKILL.md` and any supporting files.
- `catalog/skills.csv` — ownership, source, license, and status for skills we choose to maintain here.
- `catalog/installed-skills.csv` — names of skills detected in local assistant installations, without machine-specific file paths.
- `catalog/refresh-inventory.ps1` — refreshes the local installed-skill inventory.

## Skill ownership and contributions

Before adding a skill, identify it as `company-authored`, `adapted`, or `third-party`. Keep upstream attribution and license files for adapted and third-party work. Pin external dependencies to a version or commit and review changes before updating them.

For a canonical skill, create `skills/<short-hyphenated-name>/SKILL.md` and record its source and license in `catalog/skills.csv`. Test it in a representative project before making it a shared default.

## Refresh the local inventory

Run this from PowerShell on a machine with Codex, Claude, or agent skills installed:

```powershell
& "$env:USERPROFILE\Dev Skill Library\catalog\refresh-inventory.ps1"
```

The inventory stores skill names and assistant source only. It does not copy installed skill content or claim ownership. The generated inventory is machine-specific; review it before committing changes.

## Safety and maintenance

- Keep credentials, customer data, and project secrets out of this repository.
- Keep project-specific instructions in each project's own `AGENTS.md`.
- Do not overwrite assistant-managed skill directories automatically; install selected skills through each tool's supported mechanism.
- Prefer portable instructions and declare tool or platform requirements.
