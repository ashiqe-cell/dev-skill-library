# Catalog files

- `library.json` describes the catalog schema and supported installation targets.
- `skills.csv` indexes the curated packages and records version, classification, maintainer, source revision, license, and package path.
- `installed-skills.csv` and `installed-skills.md` are a names-only snapshot from one machine. They are not package entries and do not imply ownership.

The validator checks package manifests against `skills.csv`. Add a new package under `../skills/<name>/` and update the catalog row in the same change.
