<div align="center">
  <img src="assets/dev-skill-library-icon.png" alt="Dev Skill Library icon" width="104">
  <br><br>
  <img src="assets/library-hero.svg" alt="Dev Skill Library: thoughtful skills for capable coding agents" width="100%">
  <br>
  <a href="https://github.com/ashiqe-cell/dev-skill-library/actions/workflows/validate.yml"><img src="https://github.com/ashiqe-cell/dev-skill-library/actions/workflows/validate.yml/badge.svg" alt="Build status"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-2c684f?style=flat-square" alt="MIT license"></a>
  <a href="skills/"><img src="https://img.shields.io/badge/curated%20skills-1-cb5b42?style=flat-square" alt="One curated skill"></a>
  <a href="CONTRIBUTING.md"><img src="https://img.shields.io/badge/contributions-open-d5a441?style=flat-square" alt="Contributions welcome"></a>
</div>

<div align="center">
  <h3>Stop rebuilding the same developer workflow.</h3>
  <p>Package a useful task once. Reuse it across coding agents with clear sources, safe setup, and repeatable steps.</p>
  <p><a href="#the-problem">See the problem and solution</a> · <a href="#install-across-coding-agents">Try a skill</a> · <a href="CONTRIBUTING.md">Contribute</a></p>
</div>

---

## The problem

Developers are using more coding agents, but useful workflows often live in scattered prompts, personal folders, or tool-specific setups. Teams repeat the same investigations, get inconsistent steps, and have little context about who wrote a shared skill or what its scripts will do.

## The solution

Dev Skill Library packages repeatable developer work as portable, reviewable skills. Each package explains its scope, records ownership and source, and includes the files needed to use it. A preview-first installer and automated checks make it easier to adopt and maintain.

| Common pain | What the library changes |
|:--|:--|
| Recreate the same task instructions for each agent | Keep the workflow once in a portable `SKILL.md` package |
| Unsure whether a skill is safe or legally reusable | Show scope, maintainer, license, and source revision beside it |
| Setup differs across machines and tools | Offer repeatable installation with a dry run and overwrite protection |
| Skill updates can silently change behavior | Validate package metadata and run checks in CI |

### A concrete example: first-pass website security review

The Web Vulnerability Auditor gives a developer a repeatable way to review a public site for visible security and privacy signals, such as headers, cookies, exposed configuration, script patterns, tracking, and SEO spam. It creates a report with observations that a person can verify and act on.

```text
Public website URL
       ↓
Run the documented, passive audit
       ↓
Review evidence and risk indicators
       ↓
Prioritize fixes and verify them
```

This is a first-pass aid, not a penetration test or a guarantee that a site is secure. [See the skill and its limits.](skills/web-vuln-auditor/)

## Install across coding agents

Use the community skills CLI to install this package for Codex, Claude Code, Cursor, GitHub Copilot, and other supported agents:

```bash
npx skills add ashiqe-cell/dev-skill-library --skill web-vuln-auditor -g
```

Find the project on [skills.sh](https://skills.sh), or search from your terminal with `npx skills find web-vuln-auditor`. The CLI supports multiple coding agents. Continued real-world use and maintenance help developers discover and trust the package.

Prefer a manual, preview-first install? Use the library installer:

```bash
python scripts/install_skill.py --skill web-vuln-auditor --target codex
python scripts/install_skill.py --skill web-vuln-auditor --target codex --apply
```

The installer requires Python 3.10 or later and refuses to overwrite an existing installation. [See all options.](docs/INSTALLATION.md) For public marketplace publishing routes, see [distribution guide](docs/DISTRIBUTION.md).

## Catalog

<table>
  <thead>
    <tr><th align="left">Skill</th><th align="left">Use it for</th><th align="left">Version</th><th align="left">License</th></tr>
  </thead>
  <tbody>
    <tr>
      <td><a href="skills/web-vuln-auditor/"><strong>Web Vulnerability Auditor</strong></a></td>
      <td>Passive first-pass reviews of public websites for security, privacy, configuration, and SEO spam indicators</td>
      <td><code>0.2.0</code></td>
      <td><a href="skills/web-vuln-auditor/LICENSE">MIT</a></td>
    </tr>
  </tbody>
</table>

> Findings are indicators for human review. The auditor is not an exploit scanner, penetration test, or compliance certification.

### Add a skill you need

Tell us the recurring task and the developer workflow it should improve. [Open a skill request](https://github.com/ashiqe-cell/dev-skill-library/issues/new?template=skill_request.yml).

## Designed for trust

**Attribution is part of the package.** Company-authored, adapted, and third-party skills are labeled distinctly. Source revisions and license files travel with the code.

**Installation is deliberate.** The default is a dry run. The installer accepts an exact package name, blocks path traversal, and stops if a destination already exists.

**Quality is checked continuously.** GitHub Actions validates package metadata and runs the installer tests for every pull request and push to `main`.

Learn more in the [architecture](docs/ARCHITECTURE.md), [provenance policy](docs/PROVENANCE.md), and [release guide](docs/RELEASING.md).

## Contribute

Have a correction, a tested workflow, or a package worth sharing? Start with the [contribution guide](CONTRIBUTING.md), then open an issue or pull request. We review ownership, licensing, safety, and behavior before adding a package.

If this library is useful to you, a GitHub star helps other developers find it. Sharing a reproducible issue or a thoughtful contribution helps make it better.

## Project map

```text
skills/                 Curated agent skill packages
catalog/                Package index and names-only local inventory
scripts/                Validation and preview-first installer
tests/                  Catalog, install, and safety checks
docs/                   Architecture, provenance, install, and release guides
.github/workflows/      Continuous integration
```

The installed-skill files are a names-only snapshot from one machine. They are useful for discovery and do not claim ownership of those skills.

<div align="center">
  <sub>Built for useful workflows, transparent origins, and better agent tooling.</sub>
</div>
