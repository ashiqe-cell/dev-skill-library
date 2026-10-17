# Release process

Use semantic versioning for each skill package independently.

- **Patch:** documentation correction or backward-compatible bug fix.
- **Minor:** backward-compatible capability or instruction addition.
- **Major:** breaking behavior, scope, interface, or permission change.

Before release:

1. Update the package `version` in `skill.json` and the matching catalog row.
2. Record provenance updates and meaningful behavior changes in `CHANGELOG.md`.
3. Run `python scripts/validate_library.py` and `python -m unittest discover -s tests`.
4. Review the diff for secrets, machine-specific paths, generated reports, and license changes.
5. Merge only after CI passes, then tag the library release. Package versions remain authoritative for individual skills.
