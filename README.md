<div align="center">
  <img src="assets/dev-skill-library-icon.png" alt="Dev Skill Library" width="96">
  <h1>Dev Skill Library</h1>
  <p><strong>Stop rebuilding the same developer workflow.</strong></p>
  <p>Reusable agent instructions, runnable tools, and examples you can inspect.</p>
  <a href="https://github.com/ashiqe-cell/dev-skill-library/actions/workflows/validate.yml"><img src="https://github.com/ashiqe-cell/dev-skill-library/actions/workflows/validate.yml/badge.svg" alt="Validation status"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2c684f" alt="MIT"></a>
  <p><a href="#try-it">Try it</a> · <a href="#choose-a-task">Choose a task</a> · <a href="docs/README.md">Documentation</a> · <a href="CONTRIBUTING.md">Contribute</a></p>
</div>

## The problem we solve

Useful agent workflows get lost in chat history or copied between projects. The next developer repeats the setup, misses a step, or cannot tell where a script came from.

This library keeps instructions, tools, examples, and provenance together in versioned packages. Start with one concrete task: a first-pass website review that produces evidence and remediation suggestions.

**Available now: one maintained skill.** More packages must earn their place through a real use case and reproducible checks. See the [roadmap](docs/ROADMAP.md).

## Try it

Discover the package before installing:

```bash
npx skills add ashiqe-cell/dev-skill-library --list
npx skills add ashiqe-cell/dev-skill-library --skill web-vuln-auditor -g
```

Then ask your agent, replacing the placeholder with a public website you are authorized to assess:

> Use web-vuln-auditor to review <authorized-public-url>. Show the evidence, suggested fixes, and limitations. Distinguish observations from confirmed vulnerabilities.

You receive a Markdown or JSON report covering visible headers, cookies, scripts, configuration and tracking signals. This is a first-pass review aid, not a penetration test or security certification.

**Want to see the output without contacting a website?** Run the [offline walkthrough](examples/web-audit/README.md):

```bash
git clone https://github.com/ashiqe-cell/dev-skill-library.git
cd dev-skill-library
python skills/web-vuln-auditor/scripts/demo.py
```

Python 3.10+ is required. No Python packages are needed. The demo uses synthetic responses and writes only to your terminal.

## Choose a task

| Your problem | Package | Output | Evidence |
|---|---|---|---|
| I need a repeatable first review of a public website | [Web Vulnerability Auditor](skills/web-vuln-auditor/) v0.3.0 | Findings, evidence and remediation in Markdown or JSON | [Offline example](examples/web-audit/README.md), [tests](tests/test_library.py), [source and license](skills/web-vuln-auditor/README.md#package-provenance) |

The [catalog](catalog/skills.csv) contains maintained packages only. Historical names from other installations are [archived separately](archive/local-inventory/).

## Installation and compatibility

For a preview-first local install, run these from the cloned repository:

```bash
python scripts/install_skill.py --skill web-vuln-auditor --target codex
python scripts/install_skill.py --skill web-vuln-auditor --target codex --apply
```

The installer refuses to overwrite an existing package. Targets are `codex`, `claude`, and `agents`. See [installation and recovery](docs/INSTALLATION.md).

| Route | Verification scope |
|---|---|
| Community skills CLI | Remote discovery tested; one skill found. Host support follows that CLI. |
| Local Python installer | Isolated copy, dry run, overwrite protection and installed execution tests. |
| Agent execution | Instructions are portable; end-to-end runs in every host have not been verified. |
| Marketplace listings | No marketplace approval or directory indexing is claimed. |

## What makes a package worth sharing?

- A specific developer problem and example request.
- Runnable steps that work outside the original checkout.
- Evidence, limitations and failure recovery.
- A license and recorded source revision.
- Meaningful tests and a reproducible example.

[Contribute a workflow](CONTRIBUTING.md) using the [package template](templates/README.md), or [request a missing task](https://github.com/ashiqe-cell/dev-skill-library/issues/new?template=skill_request.yml).

## Project map

```text
skills/       Maintained, self-contained packages
catalog/      Machine-readable package index
examples/     Guided, reproducible walkthroughs
templates/    Contribution starter, not an installable skill
scripts/      Installer and validation
tests/        Behavioral checks
docs/         Guides, roadmap and source-backed research
archive/      Historical inventory, excluded from the catalog
```

Read the [documentation hub](docs/README.md), [research behind the structure](docs/research/REPOSITORY_BENCHMARK.md), and [next milestones](docs/ROADMAP.md).

If a workflow helped, share what you used it for. Reproducible feedback and contributions make this library better; a star helps others discover it.
