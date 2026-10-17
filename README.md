# Dev Skill Library

**Practical, reviewable skills for coding agents.**

[![Validate](https://github.com/ashiqe-cell/dev-skill-library/actions/workflows/validate.yml/badge.svg)](https://github.com/ashiqe-cell/dev-skill-library/actions/workflows/validate.yml)
[![License](https://img.shields.io/badge/catalog%20license-MIT-2f6f55)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-1-9b4c35)](#skill-catalog)
[![Contributions](https://img.shields.io/badge/contributions-welcome-d99a36)](CONTRIBUTING.md)

Dev Skill Library is a curated, versioned home for reusable agent skills. Each package has clear ownership, provenance, licensing, install instructions, and automated validation. The goal is to make good workflows portable across Codex, Claude, and compatible tools without copying unreviewed material into every project.

## Start here

Browse the [skill catalog](#skill-catalog), then read the skill's `SKILL.md` and package README before using it. Skills are instructions and tools, not a guarantee of a particular result. Review scope and permissions before running any tool that touches a live system.

### Install a skill

Requires Python 3.10 or later. Preview the installation first:

```powershell
python scripts/install_skill.py --skill web-vuln-auditor --target codex
```

Apply it after reviewing the destination:

```powershell
python scripts/install_skill.py --skill web-vuln-auditor --target codex --apply
```

The installer supports `codex`, `claude`, and `agents`. It copies only one named skill, defaults to a dry run, and refuses to overwrite an existing installation. See [installation details](docs/INSTALLATION.md).

## Skill catalog

| Skill | What it does | License | Version | Package |
|---|---|---|---|---|
| [Web Vulnerability Auditor](skills/web-vuln-auditor/) | Passive review of public websites for browser-visible security, privacy, configuration, and SEO risks | MIT | 0.2.0 | [Open](skills/web-vuln-auditor/) |

Want a skill added? Open a [skill request](https://github.com/ashiqe-cell/dev-skill-library/issues/new?template=skill_request.yml). Third-party skills are not copied into this catalog without compatible licensing, attribution, and a clear maintenance plan.

## How this library stays dependable

- **Provenance first:** every package records who maintains it, where it came from, the source revision, and its license.
- **Small packages:** each skill has its own metadata, instructions, license, and supporting files.
- **Safe installation:** dry run by default, explicit skill selection, no silent overwrites.
- **Automated checks:** CI checks metadata, package layout, documentation conventions, and installer behavior on every pull request.
- **Reviewable updates:** version history and change notes make skill changes visible to maintainers and users.

Read the [architecture](docs/ARCHITECTURE.md), [provenance policy](docs/PROVENANCE.md), and [release process](docs/RELEASING.md) for the full model.

## Contribute

Bug reports, tested improvements, and new skills are welcome. Start with [CONTRIBUTING.md](CONTRIBUTING.md), follow the package template, and include evidence that a proposed workflow works. Please star the repository if it saves you time or helps your team. Stars help other developers discover it, while useful issues and pull requests help improve it.

## Repository map

```text
skills/                 Curated, installable skill packages
catalog/                Machine-readable catalog and local inventory snapshot
scripts/                Validation and safe installation utilities
tests/                  Installer and catalog tests
docs/                   Architecture, provenance, installation, release guidance
.github/workflows/      Continuous integration
```

The files under `catalog/installed-skills.*` are a names-only snapshot from one developer machine. They are for discovery, not a claim that those skills are owned by this project.
