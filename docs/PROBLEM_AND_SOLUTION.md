# Problem and solution

## Problem

Developers are adopting multiple AI coding agents, but repeatable workflows are fragmented across chat history, personal prompt files, repositories, and tool-specific instructions. Teams rebuild the same steps, see inconsistent results, and cannot easily judge the ownership, safety, or license of a skill shared by someone else.

## Solution

Dev Skill Library turns repeatable developer tasks into portable, reviewable Agent Skills packages. It combines:

- A standard `SKILL.md` workflow that compatible agents can read.
- A package manifest, maintainer, license, and pinned source revision.
- Supporting scripts, examples, and clear usage limits.
- A dry-run installer that refuses silent overwrites.
- Catalog validation and automated tests in CI.

The library does not guarantee that every skill is correct or safe for every environment. Users should review a package before they install or run it.

## Example user problem

**Before:** A developer needs a quick review of a public website. They assemble checks from old notes, manually inspect headers and scripts, and may miss a useful signal. A teammate repeats the work with a different checklist.

**With the Web Vulnerability Auditor:** The developer installs one documented package, runs a passive review against an authorized public URL, then verifies the evidence and prioritizes fixes. The procedure is repeatable across supported agents.

## Value to measure

Track whether the library reduces setup time and repeated work, whether users can complete a skill's intended task, and how often findings are verified as useful. For the current web-audit package, useful measures include time to first report, share of findings confirmed by a human, false-positive rate, and whether teams rerun the check after remediation.
