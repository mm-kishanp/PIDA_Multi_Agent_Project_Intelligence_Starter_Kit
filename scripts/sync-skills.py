#!/usr/bin/env python3
"""Sync PIDA skills from .agents/skills to supported native skill folders.

Copies every file in each skill directory present in .agents/skills (SKILL.md,
templates, and other supporting files). Does not delete files or touch
unrelated skill names. Review git diff after running.

Use --check to report drift without writing anything. It exits 1 when a copy
is missing or differs from the source, so it can run in CI.
"""
from pathlib import Path
import argparse
import filecmp
import shutil
import sys

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / ".agents" / "skills"
TARGETS = [ROOT / ".claude" / "skills", ROOT / ".github" / "skills", ROOT / ".agent" / "skills"]


def skill_dirs():
    return sorted(p for p in SOURCE.iterdir() if p.is_dir() and (p / "SKILL.md").is_file())


def files_in(directory):
    return sorted(f.relative_to(directory) for f in directory.rglob("*") if f.is_file())


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--check", action="store_true", help="report drift without writing; exit 1 if any")
    args = parser.parse_args()

    if not SOURCE.is_dir():
        raise SystemExit("Missing .agents/skills; nothing synced.")

    skills = skill_dirs()
    drift = []
    extras = []
    copied = 0
    for skill_dir in skills:
        source_files = files_in(skill_dir)
        for target_root in TARGETS:
            target_dir = target_root / skill_dir.name
            for rel in source_files:
                src, dst = skill_dir / rel, target_dir / rel
                if dst.is_file() and filecmp.cmp(src, dst, shallow=False):
                    continue
                if args.check:
                    drift.append((dst, "differs" if dst.exists() else "missing"))
                else:
                    dst.parent.mkdir(parents=True, exist_ok=True)
                    shutil.copy2(src, dst)
                    copied += 1
            if target_dir.is_dir():
                extras += [target_dir / rel for rel in files_in(target_dir) if rel not in source_files]

    for path in extras:
        print(f"note: {path.relative_to(ROOT).as_posix()} is not in .agents/skills (left untouched)")

    if args.check:
        for path, reason in drift:
            print(f"drift: {path.relative_to(ROOT).as_posix()} ({reason})")
        if drift:
            print(f"{len(drift)} skill file(s) out of sync. Run `python scripts/sync-skills.py`.")
            return 1
        print(f"All {len(skills)} skills in sync across {len(TARGETS)} native skill roots.")
        return 0

    print(f"Synced {copied} changed file(s) for {len(skills)} skills across {len(TARGETS)} native skill roots.")
    print("Review `git diff` before committing.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
