# Repository guidance

Keep reusable packages under `skills/<name>/`. Each package needs `SKILL.md`, `skill.json`, `README.md`, and `LICENSE`. Update `catalog/skills.csv` when adding or versioning packages.

Preserve ownership, license, source URL, and immutable revision for adapted or third-party work. Do not publish secrets, machine-specific paths, customer data, or generated audit reports.

Before finishing a change, run `python scripts/validate_library.py` and `python -m unittest discover -s tests -v`. Keep README and skill documentation free of em dashes.
