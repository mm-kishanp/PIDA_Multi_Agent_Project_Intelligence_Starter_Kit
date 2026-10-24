#!/usr/bin/env python3
"""Install PIDA into a target repository without overwriting anything.

Copies the shared core (AGENTS.md, portable skills, knowledge-base and
project-management templates, helper scripts) plus the adapters for the tools
you choose. A file that already exists in the target is never overwritten: it
is reported as `unchanged` when identical, or `merge` when it differs, so you
can merge it by hand (or ask your agent to).

Use --no-skills when the skills come from the Claude Code plugin instead; only
the instruction files, templates, and doc helpers are copied then.
Use --dry-run to see what would happen without writing anything.
"""
from pathlib import Path
import argparse
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]

COMPONENTS = {
    "core": [
        "AGENTS.md",
        ".agents/skills",
        "docs/project-intelligence",
        "project-management",
        "scripts/doc-freshness.py",
        "scripts/repo-inventory.sh",
        "scripts/sync-skills.py",
    ],
    "claude": ["CLAUDE.md", ".claude/skills", ".claude/agents"],
    "copilot": [".github/copilot-instructions.md", ".github/instructions", ".github/skills"],
    "antigravity": [".agent/rules", ".agent/skills"],
    "codex": [],  # reads AGENTS.md and .agents/skills from core
    "ci": [".github/workflows/pida-checks.yml"],
}
# Provided by the plugin when installed with --no-skills.
SKILL_PATHS = {
    ".agents/skills",
    ".claude/skills",
    ".claude/agents",
    ".github/skills",
    ".agent/skills",
    "scripts/sync-skills.py",
    ".github/workflows/pida-checks.yml",
}
IGNORED_PARTS = {"__pycache__"}


def selected_paths(tools, no_skills):
    paths = []
    for name in ["core", *tools]:
        for rel in COMPONENTS[name]:
            if rel not in paths and not (no_skills and rel in SKILL_PATHS):
                paths.append(rel)
    return paths


def files_under(rel):
    source = ROOT / rel
    if source.is_file():
        return [Path(rel)]
    return sorted(
        f.relative_to(ROOT)
        for f in source.rglob("*")
        if f.is_file() and not IGNORED_PARTS & set(f.parts) and f.suffix != ".pyc"
    )


def same_content(a, b):
    # Git on Windows may have rewritten line endings in the target.
    return a.read_bytes().replace(b"\r\n", b"\n") == b.read_bytes().replace(b"\r\n", b"\n")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--target", default=".", help="repository root to install into (default: current directory)")
    parser.add_argument(
        "--tools",
        default="claude",
        help="comma-separated adapters: claude, copilot, antigravity, codex, ci, or all (default: claude)",
    )
    parser.add_argument("--no-skills", action="store_true", help="skip skills and agents (they come from the plugin)")
    parser.add_argument("--dry-run", action="store_true", help="report what would be copied; write nothing")
    args = parser.parse_args()

    tools = [t.strip() for t in args.tools.split(",") if t.strip()]
    if tools == ["all"]:
        tools = [t for t in COMPONENTS if t != "core"]
    unknown = [t for t in tools if t not in COMPONENTS or t == "core"]
    if unknown:
        raise SystemExit(f"Unknown tool(s): {', '.join(unknown)}. Choose from claude, copilot, antigravity, codex, ci, all.")

    target = Path(args.target).resolve()
    if not target.is_dir():
        raise SystemExit(f"Target is not a directory: {target}")
    if target == ROOT:
        raise SystemExit("Target is the PIDA kit itself; pass --target <your repository>.")

    created, unchanged, merge = [], [], []
    for rel in selected_paths(tools, args.no_skills):
        for file_rel in files_under(rel):
            src, dst = ROOT / file_rel, target / file_rel
            shown = file_rel.as_posix()
            if dst.exists():
                (unchanged if dst.is_file() and same_content(src, dst) else merge).append(shown)
                continue
            if not args.dry_run:
                dst.parent.mkdir(parents=True, exist_ok=True)
                shutil.copy2(src, dst)
            created.append(shown)

    verb = "would create" if args.dry_run else "created"
    for path in created:
        print(f"{verb}: {path}")
    for path in merge:
        print(f"merge: {path} (already exists and differs; left untouched)")

    print()
    print(f"Target: {target}")
    print(f"Tools: core{''.join(', ' + t for t in tools)}{' (skills from plugin)' if args.no_skills else ''}")
    print(f"{len(created)} {verb}, {len(unchanged)} already up to date, {len(merge)} need a manual merge.")
    if args.dry_run:
        print("Dry run: nothing was written.")
        return 0
    if merge:
        print("Merge the files listed above by hand, or ask your agent: "
              "\"Merge the PIDA versions of these files into ours without losing any of our rules.\"")
    prefix = "/pida:" if args.no_skills else "/"
    print(f"Next: start your agent at the repository root and run {prefix}project-audit.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
