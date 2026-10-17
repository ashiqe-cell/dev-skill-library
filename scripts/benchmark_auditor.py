"""Check labeled synthetic header and cookie cases. No network or file outputs."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import socket
import sys
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "skills/web-vuln-auditor/scripts"))
import audit_site


def evaluate(cases):
    results = []
    with patch.object(socket, "socket", side_effect=AssertionError("Benchmark network access forbidden")):
        for case in cases:
            findings = []
            if case["analyzer"] == "headers":
                audit_site.analyze_headers(case["headers"], findings, "https://fixture.example")
            elif case["analyzer"] == "cookies":
                audit_site.analyze_cookies(case["headers"], findings)
            else:
                raise ValueError(f"Unknown analyzer: {case['analyzer']}")
            expected = set(case["expected_titles"])
            actual = {finding.title for finding in findings}
            results.append({
                "case": case["name"], "passed": actual == expected,
                "missed": sorted(expected - actual),
                "unexpected": sorted(actual - expected),
            })
    return results


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--cases", type=Path, default=ROOT / "benchmarks/web-audit/cases.json")
    args = parser.parse_args()
    cases = json.loads(args.cases.read_text(encoding="utf-8"))
    if not cases:
        parser.error("At least one labeled case is required")
    results = evaluate(cases)
    for item in results:
        print(f"{'PASS' if item['passed'] else 'FAIL'} {item['case']}")
        if not item["passed"]:
            print(f"  Missed: {item['missed']}; unexpected: {item['unexpected']}")
    print(f"{sum(item['passed'] for item in results)}/{len(results)} synthetic cases passed. Not a real-world accuracy score.")
    return 0 if all(item["passed"] for item in results) else 1


if __name__ == "__main__":
    raise SystemExit(main())
