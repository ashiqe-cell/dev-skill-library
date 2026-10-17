# Installation

The installer supports Codex, Claude, and compatible agent skill directories on Windows, macOS, and Linux. It requires Python 3.10 or later.

## Preview

From the repository root, run:

```bash
python scripts/install_skill.py --skill web-vuln-auditor --target codex
```

No files are changed unless `--apply` is supplied. The default user directories are `~/.codex/skills`, `~/.claude/skills`, and `~/.agents/skills`.

## Install

```bash
python scripts/install_skill.py --skill web-vuln-auditor --target codex --apply
```

Choose `claude` or `agents` for a different target. Use `--home PATH` to set an alternate home directory, such as a temporary test directory. The installer refuses to overwrite an existing skill. Review and remove an old installation yourself before retrying.

Installed files are copies. To update, review the new library version, then replace the installation deliberately. No network access or telemetry is used by the installer.
