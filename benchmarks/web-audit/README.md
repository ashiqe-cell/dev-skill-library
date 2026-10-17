# Synthetic detection benchmark

From the repository root:

```bash
python scripts/benchmark_auditor.py
```

Nine labeled cases cover complete headers, header-name casing, missing CSP, unsafe inline policy, short HSTS, protected and unprotected session cookies, multiple cookies and no cookie header. Expected finding titles are stored independently in `cases.json`. The runner reports both missed and unexpected findings and fails on either. Socket creation is blocked during evaluation.

These fixtures test the header and cookie rules only. They do not validate live transport, browser behavior, exploitable vulnerabilities, consent handling or every parser. A passing result is not a real-world precision or recall claim.

## Interpretation limits

- A missing header does not establish exploitability. Report severity still needs human review.
- CSP frame-ancestors can provide framing protection without X-Frame-Options; the current rule may still flag the missing header.
- Some cookies legitimately need JavaScript access. A missing HttpOnly flag may be intentional. The preferences-cookie fixture records the current rule output, not a vulnerability label.
- CSP parsing is heuristic and cannot establish that a policy is effective in a browser.
- HSTS deployment duration depends on operational readiness. A short duration can be intentional.

Future cases should include policy alternatives, malformed inputs and independently reviewed labels before expanding accuracy claims. Do not silently change expected labels to hide a regression.
