from __future__ import annotations

import csv
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PYTHON = sys.executable


class LibraryTests(unittest.TestCase):
    def test_installed_demo_is_offline_and_portable(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            result = self.run_installer("--skill", "web-vuln-auditor", "--target", "codex", "--home", temp, "--apply")
            self.assertEqual(result.returncode, 0, result.stderr)
            scripts = Path(temp) / ".codex/skills/web-vuln-auditor/scripts"
            code = (
                "import sys, socket; from unittest.mock import patch; "
                "sys.path.insert(0, sys.argv[1]); import demo; "
                "guard=patch.object(socket, 'socket', side_effect=AssertionError('Network forbidden')); "
                "guard.start(); report=demo.build_demo(); "
                "assert report.status_code == 200; assert report.findings; "
                "assert not report.csp_analysis['present']; "
                "assert 'SYNTHETIC OFFLINE' in report.notes[0]; "
                "assert report.target == 'https://demo.example'; guard.stop()"
            )
            run = subprocess.run([PYTHON, "-c", code, str(scripts)], cwd=temp, capture_output=True, text=True)
            self.assertEqual(run.returncode, 0, run.stderr)

    def run_installer(self, *args: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [PYTHON, str(ROOT / "scripts" / "install_skill.py"), *args],
            cwd=ROOT,
            text=True,
            capture_output=True,
            check=False,
        )

    def test_catalog_matches_package_manifest(self) -> None:
        with (ROOT / "catalog" / "skills.csv").open(encoding="utf-8-sig", newline="") as handle:
            rows = list(csv.DictReader(handle))
        for row in rows:
            metadata = json.loads((ROOT / row["package_path"] / "skill.json").read_text(encoding="utf-8"))
            self.assertEqual(metadata["name"], row["name"])
            self.assertEqual(metadata["version"], row["version"])

    def test_dry_run_does_not_create_files(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            result = self.run_installer("--skill", "web-vuln-auditor", "--target", "codex", "--home", temp)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertFalse((Path(temp) / ".codex" / "skills" / "web-vuln-auditor").exists())

    def test_apply_copies_package(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            result = self.run_installer("--skill", "web-vuln-auditor", "--target", "claude", "--home", temp, "--apply")
            self.assertEqual(result.returncode, 0, result.stderr)
            installed = Path(temp) / ".claude" / "skills" / "web-vuln-auditor"
            self.assertTrue((installed / "SKILL.md").is_file())
            self.assertTrue((installed / "scripts" / "audit_site.py").is_file())

    def test_existing_install_is_not_overwritten(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            destination = Path(temp) / ".agents" / "skills" / "web-vuln-auditor"
            destination.mkdir(parents=True)
            marker = destination / "keep.txt"
            marker.write_text("preserve", encoding="utf-8")
            result = self.run_installer("--skill", "web-vuln-auditor", "--target", "agents", "--home", temp, "--apply")
            self.assertEqual(result.returncode, 3)
            self.assertEqual(marker.read_text(encoding="utf-8"), "preserve")

    def test_unknown_skill_is_rejected(self) -> None:
        result = self.run_installer("--skill", "../../outside", "--target", "codex")
        self.assertEqual(result.returncode, 2)

    def test_auditor_rejects_loopback_targets(self) -> None:
        with tempfile.TemporaryDirectory() as temp:
            output = Path(temp) / "report.md"
            result = subprocess.run(
                [PYTHON, str(ROOT / "skills" / "web-vuln-auditor" / "scripts" / "audit_site.py"), "http://127.0.0.1", "--output", str(output)],
                cwd=ROOT,
                text=True,
                capture_output=True,
                check=False,
            )
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("private, reserved, or local IP addresses", output.read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
