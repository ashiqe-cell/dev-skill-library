# Repository benchmark and restructuring decisions

Observed 17 October 2026 using the GitHub REST API, repository trees and READMEs. This is a purposive sample of six popular relevant repositories, not an exhaustive ranking. Stars measure reach, not quality or proof that a README caused growth. Brand, age, audience and distribution also matter.

| Repository | Stars | Forks | Pattern to adopt |
|---|---:|---:|---|
| [obra/superpowers](https://github.com/obra/superpowers) | 300,959 | 26,870 | Explain the complete workflow and recovery paths. |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 294,523 | 24,699 | Organize around developer problems and composable tasks. |
| [anthropics/skills](https://github.com/anthropics/skills) | 181,685 | 21,522 | Keep packages self-contained with templates and per-skill terms. |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 77,278 | 9,160 | Make the first use case concrete and group discovery by task. |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 35,875 | 3,893 | Use clear categories and contribution quality criteria. |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | 32,549 | 2,842 | Show when to use each skill and how to install it. |

The [machine-readable snapshot](repository-snapshot.json) records API URLs, immutable source commits and observed root folders. Counts will change.

## Decisions for this library

| Observation | Decision | What we deliberately defer |
|---|---|---|
| Problem-based navigation is clearer than a long file list | Task catalog and a concrete first request | Empty categories and inflated skill counts |
| Runnable examples explain value | Offline report walkthrough using the real analyzer | Claims about real detection accuracy without a benchmark |
| Self-contained skills move between hosts | Resolve scripts from installed package location | Native plugin manifests before testing each host |
| Large directories distinguish links from packages | Archive machine inventory outside maintained catalog | Vendoring hundreds of unreviewed third-party skills |
| Community projects make contribution requirements explicit | Non-discoverable template and acceptance checklist | Automatic acceptance of generated packages |
| Mature projects provide troubleshooting and tests | Installation docs, behavioral tests, Windows/Linux CI | Claiming every agent is supported merely because files copy |

## What the comparisons do not prove

Superpowers provides an orchestration methodology, while VoltAgent is primarily a directory. Their scope differs from a one-package executable library. Matt Pocock also has an established audience; its growth cannot be attributed to structure alone. Anthropic's repository contains differing per-skill terms, so its contents must not be treated as uniformly reusable. No benchmark code or skill text was copied into this project.

## Positioning

Lead with a repeatable developer task, show a runnable result, explain limitations, and give a short installation path. Expand when a new package solves a distinct problem and passes the same evidence standard. Measure successful use and useful contributions alongside stars.
