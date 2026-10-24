"""Tests for the PIDA install, sync, and plugin packaging. Run from the repository root:

    python -m unittest discover -s tests -v
"""
from pathlib import Path
import json
import re
import shutil
import subprocess
import sys
import unittest
import uuid

ROOT = Path(__file__).resolve().parents[1]

try:
    from tempfile import mkdtemp
except ImportError:  # some locked-down Python installs ship without tempfile
    def mkdtemp():
        path = ROOT / ".pida-tmp" / uuid.uuid4().hex
        path.mkdir(parents=True)
        return str(path)
INSTALL = ROOT / "scripts" / "install-pida.py"
SYNC = ROOT / "scripts" / "sync-skills.py"
SKILLS = ROOT / ".agents" / "skills"


def run(*args, cwd=ROOT):
    return subprocess.run([sys.executable, *map(str, args)], cwd=cwd, capture_output=True, text=True)


def frontmatter(path):
    text = path.read_text(encoding="utf-8")
    match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", text, re.S)
    return match.group(1) if match else ""


class Install(unittest.TestCase):
    def setUp(self):
        self.target = Path(mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.target, ignore_errors=True)
        fallback = ROOT / ".pida-tmp"
        if fallback.is_dir() and not any(fallback.iterdir()):
            fallback.rmdir()

    def test_default_installs_core_and_claude(self):
        result = run(INSTALL, "--target", self.target)
        self.assertEqual(result.returncode, 0, result.stderr)
        for rel in ("AGENTS.md", "CLAUDE.md", ".claude/skills/project-audit/SKILL.md",
                    ".claude/agents/pida-auditor.md", ".agents/skills/project-audit/templates/client-matrix.md",
                    "docs/project-intelligence/client-matrix.md", "project-management/BACKLOG.md",
                    "scripts/doc-freshness.py"):
            self.assertTrue((self.target / rel).is_file(), rel)
        for rel in (".github", ".agent", ".claude-plugin", "skills", "tests", "README.md"):
            self.assertFalse((self.target / rel).exists(), rel)
        self.assertEqual(list(self.target.rglob("__pycache__")), [])

    def test_never_overwrites_existing_files(self):
        (self.target / "CLAUDE.md").write_text("our rules\n", encoding="utf-8")
        result = run(INSTALL, "--target", self.target)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual((self.target / "CLAUDE.md").read_text(encoding="utf-8"), "our rules\n")
        self.assertIn("merge: CLAUDE.md", result.stdout)

    def test_rerun_reports_up_to_date(self):
        run(INSTALL, "--target", self.target)
        result = run(INSTALL, "--target", self.target)
        self.assertIn("\n0 created,", result.stdout)
        self.assertIn(" 0 need a manual merge.", result.stdout)

    def test_dry_run_writes_nothing(self):
        result = run(INSTALL, "--target", self.target, "--tools", "all", "--dry-run")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("would create: AGENTS.md", result.stdout)
        self.assertEqual(list(self.target.iterdir()), [])

    def test_no_skills_leaves_skills_to_the_plugin(self):
        result = run(INSTALL, "--target", self.target, "--no-skills")
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertTrue((self.target / "CLAUDE.md").is_file())
        self.assertTrue((self.target / "docs/project-intelligence/README.md").is_file())
        for rel in (".agents", ".claude", "scripts/sync-skills.py"):
            self.assertFalse((self.target / rel).exists(), rel)
        self.assertIn("/pida:project-audit", result.stdout)

    def test_selected_adapters(self):
        run(INSTALL, "--target", self.target, "--tools", "copilot,antigravity,ci")
        for rel in (".github/copilot-instructions.md", ".github/skills/testing/SKILL.md",
                    ".agent/rules/pida-project-intelligence.md", ".github/workflows/pida-checks.yml"):
            self.assertTrue((self.target / rel).is_file(), rel)
        self.assertFalse((self.target / "CLAUDE.md").exists())

    def test_rejects_unknown_tool_and_kit_as_target(self):
        self.assertNotEqual(run(INSTALL, "--target", self.target, "--tools", "cursor").returncode, 0)
        self.assertNotEqual(run(INSTALL, "--target", ROOT).returncode, 0)

    def test_sync_check_passes_in_partial_install(self):
        run(INSTALL, "--target", self.target)
        result = run(self.target / "scripts" / "sync-skills.py", "--check", cwd=self.target)
        self.assertEqual(result.returncode, 0, result.stdout)
        self.assertFalse((self.target / ".github").exists())


class Packaging(unittest.TestCase):
    def test_skill_copies_in_sync(self):
        result = run(SYNC, "--check")
        self.assertEqual(result.returncode, 0, result.stdout)

    def test_skill_frontmatter(self):
        for skill_md in [*SKILLS.glob("*/SKILL.md"), *(ROOT / "skills").glob("*/SKILL.md")]:
            fm = frontmatter(skill_md)
            self.assertIn(f"name: {skill_md.parent.name}", fm, skill_md)
            self.assertRegex(fm, r"description: \S", skill_md)

    def test_plugin_manifest(self):
        plugin = json.loads((ROOT / ".claude-plugin" / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(plugin["name"], "pida")
        for rel in [*plugin["skills"], *plugin["agents"]]:
            self.assertTrue(rel.startswith("./"), rel)
            self.assertNotIn("..", rel)
            self.assertTrue((ROOT / rel).exists(), rel)
        agents = sorted(Path(a).name for a in plugin["agents"])
        self.assertEqual(agents, sorted(p.name for p in (ROOT / ".claude" / "agents").glob("*.md")))

    def test_marketplace_manifest(self):
        market = json.loads((ROOT / ".claude-plugin" / "marketplace.json").read_text(encoding="utf-8"))
        self.assertEqual(market["name"], "pida")
        self.assertEqual(market["plugins"][0]["name"], "pida")
        self.assertEqual(market["plugins"][0]["source"], "./")

    def test_readme_install_commands_match_manifests(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        self.assertIn("/plugin marketplace add mm-kishanp/PIDA_Multi_Agent_Project_Intelligence_Starter_Kit", readme)
        self.assertIn("/plugin install pida@pida", readme)
        self.assertIn("/pida:pida-setup", readme)


if __name__ == "__main__":
    unittest.main()
