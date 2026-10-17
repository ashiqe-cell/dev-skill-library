#!/usr/bin/env python3
"""Safely copy one curated skill to an agent's user-level skills directory."""

from __future__ import annotations

import argparse
import json
import shutil
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TARGETS = {"codex": ".codex/skills", "claude": ".claude/skills", "agents": ".agents/skills"}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--skill", required=True, help="Exact skill package name")
    parser.add_argument("--target", required=True, choices=sorted(TARGETS))
    parser.add_argument("--home", type=Path, default=Path.home(), help="User home directory, useful for isolated installs")
    parser.add_argument("--apply", action="store_true", help="Write files. Omit for a dry run")
    args = parser.parse_args()

    package = (ROOT / "skills" / args.skill).resolve()
    skills_root = (ROOT / "skills").resolve()
    if skills_root not in package.parents or not (package / "SKILL.md").is_file():
        print(f"Unknown or invalid skill package: {args.skill}", file=sys.stderr)
        return 2
    try:
        metadata = json.loads((package / "skill.json").read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"Cannot read package metadata: {exc}", file=sys.stderr)
        return 2
    if metadata.get("name") != args.skill:
        print("Package metadata name does not match the requested skill", file=sys.stderr)
        return 2

    destination_root = (args.home.expanduser().resolve() / TARGETS[args.target]).resolve()
    destination = destination_root / args.skill
    if destination_root not in destination.parents:
        print("Invalid destination path", file=sys.stderr)
        return 2
    if destination.exists():
        print(f"Refusing to overwrite existing installation: {destination}", file=sys.stderr)
        return 3
    action = "Install" if args.apply else "Would install"
    print(f"{action} {args.skill} {metadata['version']} for {args.target} at {destination}")
    if not args.apply:
        print("Dry run only. Add --apply to copy the package.")
        return 0
    destination_root.mkdir(parents=True, exist_ok=True)
    shutil.copytree(package, destination, ignore=shutil.ignore_patterns("__pycache__", "*.pyc"))
    print("Installation complete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
