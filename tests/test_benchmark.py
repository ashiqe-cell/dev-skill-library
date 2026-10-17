import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("benchmark_auditor", ROOT / "scripts/benchmark_auditor.py")
benchmark = importlib.util.module_from_spec(spec)
spec.loader.exec_module(benchmark)


class BenchmarkTests(unittest.TestCase):
    def test_labeled_cases(self):
        cases = json.loads((ROOT / "benchmarks/web-audit/cases.json").read_text())
        for result in benchmark.evaluate(cases):
            with self.subTest(case=result["case"]):
                self.assertTrue(result["passed"], result)

    def test_harness_detects_missed_and_unexpected_findings(self):
        case = {"name": "intentional-mismatch", "analyzer": "cookies",
                "headers": {"Set-Cookie": "session=fixture"},
                "expected_titles": ["deliberately absent finding"]}
        result = benchmark.evaluate([case])[0]
        self.assertFalse(result["passed"])
        self.assertEqual(result["missed"], ["deliberately absent finding"])
        self.assertEqual(result["unexpected"], ["Cookie session is missing recommended flags"])


if __name__ == "__main__":
    unittest.main()
