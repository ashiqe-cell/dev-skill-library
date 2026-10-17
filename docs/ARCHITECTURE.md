# Architecture

The library separates package contents, catalog metadata, local inventory, and tooling so that maintainers can review each concern independently.

## Package contract

Every installable skill lives in `skills/<name>/` and contains:

- `SKILL.md`: agent-facing instructions with matching `name` and `description` frontmatter.
- `skill.json`: display metadata, version, ownership, provenance, license, entrypoint, and supported targets.
- `LICENSE`: the package license, retained from the origin when adapted or imported.
- `README.md`: human-facing scope, setup, examples, limitations, and attribution.
- Optional scripts, fixtures, and assets required by that skill.

The root `catalog/library.json` declares the catalog format. `catalog/skills.csv` is the reviewable index and must agree with every package manifest. Installed-skill inventory files are a separate names-only machine snapshot and do not imply ownership.

## Validation and installation

`scripts/validate_library.py` checks metadata consistency, package structure, safe paths, version formats, and README punctuation rules. `scripts/install_skill.py` copies one package to one assistant's user skill directory. Installation is dry-run by default; it refuses path traversal and overwrites.

CI runs validation and tests on pull requests and pushes to `main`. See [installation](INSTALLATION.md) for usage and [releases](RELEASING.md) for version policy.
