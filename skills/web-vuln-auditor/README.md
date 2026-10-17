# Web Vulnerability Auditor

A passive, first-pass review tool for public websites. It inspects externally visible responses and page content for security, privacy, configuration, and SEO spam indicators.

## Checks

- HTTP security headers and Content Security Policy directives
- Cookie security attributes
- Publicly exposed configuration and common documentation endpoints
- Client-side script patterns and possible secret exposure indicators
- Frontend library and framework version clues
- Tracking and SEO spam signals

Findings are indicators that need human verification. This tool is not an exploit scanner, authenticated test suite, compliance certification, or substitute for a professional penetration test.

## Run

Requires Python 3.10 or later and uses the Python standard library.

```bash
python skills/web-vuln-auditor/scripts/audit_site.py https://example.com
```

See [SKILL.md](SKILL.md) for the required scope and safe-use instructions. The [sample JSON](samples/example-audit.json) shows the report structure.

## Package provenance

- Maintainer: `ashiqevm0496`
- License: MIT, see [LICENSE](LICENSE)
- Source repository: [web-vuln-auditor](https://github.com/ashiqevm0496/web-vuln-auditor)
- Imported revision: `fed0eabe8413d01c45473857bf80a816594bad30`
- Library package version: `0.2.0`

The package in this repository is maintained here as a curated copy. Updates are reviewed against the recorded source revision and tested before release.
