# Rebuild plan and acceptance criteria

## Phase 1: Make the current package useful and understandable

Implemented in this restructure:

- Problem-led README with one honest task entry and complete setup commands.
- Documentation hub, source-backed comparison and archived machine inventory.
- Offline demo through the real report pipeline, without live requests.
- Portable installed instructions and exclusion of generated reports from installs.
- Contribution template that discovery tools cannot mistake for a working package.
- Behavioral tests and Windows/Linux validation matrix.

## Phase 2: Validate actual adoption

Completed: nine labeled synthetic header/cookie cases with missed and unexpected finding checks, a tested benchmark harness, and a [host verification record](HOST_VALIDATION.md). The previous Windows/Linux CI matrix passed. See [benchmark scope and known limitations](../benchmarks/web-audit/README.md).

Still pending:

- Run the same authorized task in Codex and Claude Code and record host versions, setup and output limitations.
- Ask early users where installation or report interpretation fails; make feedback optional and do not add telemetry by default.
- Expand the fixture benchmark to policy alternatives and independently reviewed labels before making detection-quality claims.
- Publish a versioned release after the expanded CI checks pass and release notes are reviewed.

Acceptance: reproducible host instructions, documented failures, and a benchmark that exposes false positives as well as detections.

## Phase 3: Grow by problem coverage

Proposed candidates, not available skills: API contract review, migration readiness review and accessibility triage. Choose based on actual requests rather than keyword counts. Each needs ownership review, boundaries, examples and behavioral tests before entering the maintained catalog.

Acceptance: every new package solves a distinct task and works from its installed directory. No copied license-restricted collections or untested bulk imports.

## Phase 4: Distribution

Prepare a short demo, a task-focused release announcement and host-specific setup guides. Submit to relevant directories only after their current rules are checked and the owner authorizes submission. Do not imply listing approval before it exists.

Track voluntary successful-use reports, actionable issues, repeat contributors and releases. Stars are a secondary discovery signal; no growth target is guaranteed.
