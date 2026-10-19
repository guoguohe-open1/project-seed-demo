from __future__ import annotations

import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "bootstrap.py"


class BootstrapTests(unittest.TestCase):
    def run_bootstrap(self, target: Path, *extra: str) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            [sys.executable, str(SCRIPT), "--target", str(target), "--name", "Demo Project", *extra],
            capture_output=True,
            text=True,
            check=False,
        )

    def test_generates_agent_evaluation_project(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "generated"
            result = self.run_bootstrap(target, "--description", "A demo", "--profile", "agent-evaluation")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((target / "AGENTS.md").is_file())
            self.assertTrue((target / "docs/CONTRACTS.md").is_file())
            self.assertTrue((target / "docs/changes/templates/FEATURE.md").is_file())
            brief = (target / "docs/PROJECT_BRIEF.md").read_text(encoding="utf-8")
            profile = (target / "docs/PROJECT_PROFILE.md").read_text(encoding="utf-8")
            readme = (target / "README.md").read_text(encoding="utf-8")
            self.assertIn("Demo Project", brief)
            self.assertIn("Agent Evaluation & Simulation", brief)
            self.assertIn("observable evidence", profile)
            self.assertNotIn("{{PROJECT_NAME}}", readme)

    def test_refuses_non_empty_target_without_overwriting(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "existing"
            target.mkdir()
            sentinel = target / "keep.txt"
            sentinel.write_text("preserve", encoding="utf-8")
            result = self.run_bootstrap(target)
            self.assertEqual(result.returncode, 2)
            self.assertEqual(sentinel.read_text(encoding="utf-8"), "preserve")
            self.assertFalse((target / "AGENTS.md").exists())

    def test_allows_existing_empty_target(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "empty"
            target.mkdir()
            result = self.run_bootstrap(target, "--profile", "rag-system")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue((target / "docs/PROJECT_PROFILE.md").is_file())

    def test_dry_run_does_not_write_files(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "dry-run"
            result = self.run_bootstrap(target, "--dry-run")
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertIn("Would create", result.stdout)
            self.assertFalse(target.exists())


if __name__ == "__main__":
    unittest.main()
