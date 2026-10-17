#!/usr/bin/env python3
"""Validate package metadata and repository conventions using only the stdlib."""

from __future__ import annotations

import csv
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
VERSION_RE = re.compile(r"^\d+\.\d+\.\d+$")
ALLOWED_CLASSIFICATIONS = {"company-authored", "adapted", "third-party"}


def fail(errors: list[str], message: str) -> None:
    errors.append(message)


def main() -> int:
    errors: list[str] = []
    catalog_path = ROOT / "catalog" / "skills.csv"
    try:
        with catalog_path.open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
    except (OSError, csv.Error) as exc:
        print(f"Cannot read {catalog_path}: {exc}", file=sys.stderr)
        return 1

    catalog_names: set[str] = set()
    for row in rows:
        name = row.get("name", "")
        if name in catalog_names:
            fail(errors, f"Duplicate catalog entry: {name}")
        catalog_names.add(name)
        if not NAME_RE.fullmatch(name):
            fail(errors, f"Invalid skill name: {name!r}")
        package = (ROOT / row.get("package_path", "")).resolve()
        if ROOT not in package.parents:
            fail(errors, f"Package path escapes repository: {name}")
            continue
        manifest_path = package / "skill.json"
        skill_path = package / "SKILL.md"
        readme_path = package / "README.md"
        license_path = package / "LICENSE"
        for required in (manifest_path, skill_path, readme_path, license_path):
            if not required.is_file():
                fail(errors, f"{name}: missing {required.relative_to(ROOT)}")
        if not manifest_path.is_file() or not skill_path.is_file():
            continue
        try:
            metadata = json.loads(manifest_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError) as exc:
            fail(errors, f"{name}: invalid skill.json: {exc}")
            continue
        if metadata.get("name") != name:
            fail(errors, f"{name}: skill.json name does not match catalog")
        if metadata.get("version") != row.get("version"):
            fail(errors, f"{name}: version differs between manifest and catalog")
        if not VERSION_RE.fullmatch(metadata.get("version", "")):
            fail(errors, f"{name}: version must use MAJOR.MINOR.PATCH")
        if metadata.get("classification") not in ALLOWED_CLASSIFICATIONS:
            fail(errors, f"{name}: invalid classification")
        if metadata.get("license") != row.get("license"):
            fail(errors, f"{name}: license differs between manifest and catalog")
        if not metadata.get("source", {}).get("repository") or not metadata.get("source", {}).get("revision"):
            fail(errors, f"{name}: source repository and immutable revision are required")
        body = skill_path.read_text(encoding="utf-8")
        frontmatter = re.match(r"\A---\s*\n(.*?)\n---\s*\n", body, re.DOTALL)
        if not frontmatter:
            fail(errors, f"{name}: SKILL.md needs YAML frontmatter")
        else:
            front = frontmatter.group(1)
            if not re.search(rf"^name:\s*{re.escape(name)}\s*$", front, re.MULTILINE):
                fail(errors, f"{name}: SKILL.md name differs from manifest")
            if not re.search(r"^description:\s*\S", front, re.MULTILINE):
                fail(errors, f"{name}: SKILL.md description is required")
        for file_path in (skill_path, readme_path):
            if file_path.is_file() and "\u2014" in file_path.read_text(encoding="utf-8"):
                fail(errors, f"{name}: remove em dash from {file_path.relative_to(ROOT)}")
        entrypoint = metadata.get("entrypoint", "")
        entry_path = (package / entrypoint).resolve()
        if package not in entry_path.parents or not entry_path.is_file():
            fail(errors, f"{name}: invalid or missing entrypoint")

    package_dirs = {p.name for p in (ROOT / "skills").iterdir() if p.is_dir() and not p.name.startswith(".")}
    if package_dirs != catalog_names:
        fail(errors, f"Catalog/package mismatch: catalog={sorted(catalog_names)}, packages={sorted(package_dirs)}")

    if errors:
        print("Library validation failed:")
        for error in errors:
            print(f"- {error}")
        return 1
    print(f"Validated {len(rows)} skill package(s).")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
