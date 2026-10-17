# Contributing

Issues and pull requests are welcome. Start with a focused change that can be reviewed and tested.

## Propose a skill

1. Open an issue describing the user problem, intended users, and why an agent skill is the right solution.
2. State whether the work is company-authored, adapted, or third-party.
3. Include the source URL, exact revision, license, maintainer, and any required dependencies.
4. Use the package layout in [Architecture](docs/ARCHITECTURE.md). Keep instructions safe, specific, and testable.
5. Add or update catalog metadata, tests, and changelog entries.
6. Run the validator and tests locally, then submit the pull request.

Do not submit secrets, customer data, generated audit reports, unlicensed copied content, or absolute machine paths. Explain how the skill handles user authorization, external side effects, and untrusted input. Maintainers may decline a package that cannot be safely or legally maintained.

## Improve the library

Bug reports should include the command, expected result, actual result, and a minimal reproduction. Feature requests should explain the workflow they improve. Keep pull requests focused and include test evidence.
