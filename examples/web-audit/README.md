# Try an audit without a live target

Requires Python 3.10+. From a fresh checkout:

```bash
git clone https://github.com/ashiqe-cell/dev-skill-library.git
cd dev-skill-library
python skills/web-vuln-auditor/scripts/demo.py
```

The demo supplies a synthetic HTML response with no security headers to the real analysis and rendering pipeline. All subsequent endpoint requests receive synthetic 404 responses. No network requests are made and no report file is saved.

The result includes the target `https://demo.example`, a fixed fixture timestamp, missing-header findings, remediation text, and an explicit synthetic-data note. A missing header is an observation to review, not proof that the site can be exploited.

To compare behavior, inspect `skills/web-vuln-auditor/scripts/demo.py` and change its fixture headers locally. This demonstrates report mechanics, not detection accuracy against a benchmark of real vulnerabilities.

For an authorized real audit, follow the package's [scope and instructions](../../skills/web-vuln-auditor/SKILL.md). Keep real customer reports outside version control.
