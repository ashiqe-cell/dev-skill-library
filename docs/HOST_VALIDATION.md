# Host validation and evidence

Checked 17 October 2026.

| Check | Result | Scope |
|---|---|---|
| GitHub CI for restructuring commit 4cde4df | Passed | Windows and Linux, Python 3.10 and 3.12 |
| Local installer and installed demo | Passed | Temporary home, unrelated working directory, sockets blocked |
| Community skills CLI discovery | One package found | Discovery only, not an agent execution test |
| Codex CLI session | Not run | Command-line executable unavailable in the current environment |
| Claude Code session | Not run | Command-line executable unavailable in the current environment |

The current Codex task ran the repository tools. That does not prove automatic skill discovery and execution in a separate host session.

## Reproduce a host smoke test

1. Record the host and Python versions.
2. Install the package using the documented route, without replacing existing work.
3. Start a fresh task in an unrelated directory.
4. Ask: "Use web-vuln-auditor to run its synthetic offline demo. Do not contact a website. Explain which findings are observations and which require verification."
5. Confirm the agent resolves the installed scripts, runs the demo, identifies synthetic data and avoids claiming real vulnerabilities.
6. Record the prompt, setup, result and limitations with private paths removed. Do not publish customer audit output.

This procedure is ready for both hosts. Their end-to-end results remain pending until executed.
