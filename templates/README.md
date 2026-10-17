# Contribute a task, with evidence

Start from `SKILL.md.template`, rename it only inside your new `skills/<name>/` package, and add `README.md`, `skill.json`, and a license you have authority to grant. The template is deliberately not named `SKILL.md`, so discovery tools do not install it as a working skill.

Use the maintained package's manifest as the schema example. Set your own name, version, maintainer, classification, source repository and immutable revision. Update `catalog/skills.csv` in the same pull request.

Acceptance checklist:

- A concrete recurring developer problem and an example request.
- Explicit inputs, outputs, limitations and failure recovery.
- Commands resolve relative to the installed package, not the original checkout.
- A reproducible example with synthetic or publishable data.
- Tests for meaningful behavior and failure cases.
- Original or correctly attributed content with per-package licensing.
- No private reports, credentials, customer records or unsupported success claims.

See [contributing](../CONTRIBUTING.md) for the review process.
