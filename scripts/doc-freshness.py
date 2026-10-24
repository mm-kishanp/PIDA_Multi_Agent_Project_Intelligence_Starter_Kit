#!/usr/bin/env python3
"""Report drift in PIDA project-intelligence docs. Read-only.

For each Markdown page in docs/project-intelligence/ (or --docs-dir), including
subfolders such as features/, reports:
- a missing or placeholder `Last reviewed:` date;
- a review date older than --max-age-days (default 90);
- cited repository paths that no longer exist (Markdown links, and `code spans`
  containing a slash).

Output is a list of leads for /project-refresh, not proof of drift.
Exits 0 unless --strict is given and issues were found.
"""
from datetime import date
from pathlib import Path
import argparse
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
# Pages without a single review date: the index and the append-only log.
UNDATED = {"README.md", "analysis-log.md"}

DATE_RE = re.compile(r"Last reviewed:\s*(\S+)", re.IGNORECASE)
FENCE_RE = re.compile(r"^(```|~~~).*?^\1", re.MULTILINE | re.DOTALL)
LINK_RE = re.compile(r"\]\(([^)\s]+)\)")
CODE_RE = re.compile(r"`([^`\s]+)`")
SLASH_COMMAND_RE = re.compile(r"^/[\w:-]+$")  # `/project-audit`, `/pida:project-docs`
LOCATION_SUFFIX_RE = re.compile(r"(#L?\d+(-L?\d+)?|:\d+(-\d+)?)$")
PLACEHOLDER_CHARS = set("<>[]{}*$|=")


def review_date_issue(text, today, max_age):
    match = DATE_RE.search(text)
    if not match:
        return "no `Last reviewed:` date"
    try:
        reviewed = date.fromisoformat(match.group(1))
    except ValueError:
        return f"placeholder or invalid review date ({match.group(1)})"
    age = (today - reviewed).days
    if age > max_age:
        return f"last reviewed {reviewed} ({age} days ago; threshold {max_age})"
    return None


def cited_paths(text):
    """Yield (line number, path) for links and path-like code spans."""
    text = FENCE_RE.sub(lambda m: "\n" * m.group(0).count("\n"), text)
    for lineno, line in enumerate(text.splitlines(), start=1):
        candidates = LINK_RE.findall(line) + [
            c for c in CODE_RE.findall(line) if "/" in c and not SLASH_COMMAND_RE.match(c)
        ]
        for raw in candidates:
            if "://" in raw or raw.startswith(("#", "mailto:", "-")) or PLACEHOLDER_CHARS & set(raw):
                continue
            path = LOCATION_SUFFIX_RE.sub("", raw).split("#")[0]
            path = path.removeprefix("./").lstrip("/")
            if path:
                yield lineno, path


def missing_paths(page, text):
    issues = []
    for lineno, path in cited_paths(text):
        if not ((ROOT / path).exists() or (page.parent / path).exists()):
            issues.append(f"missing path (line {lineno}): {path}")
    return issues


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--docs-dir", default="docs/project-intelligence", help="absolute, or relative to repository root")
    parser.add_argument("--max-age-days", type=int, default=90)
    parser.add_argument("--strict", action="store_true", help="exit 1 if any issue is found")
    args = parser.parse_args()

    docs_dir = (ROOT / args.docs_dir).resolve()
    if not docs_dir.is_dir():
        raise SystemExit(f"Docs directory not found: {args.docs_dir}")

    today = date.today()
    pages = sorted(docs_dir.rglob("*.md"))
    flagged = 0
    for page in pages:
        text = page.read_text(encoding="utf-8", errors="replace")
        issues = []
        if page.name not in UNDATED:
            issue = review_date_issue(text, today, args.max_age_days)
            if issue:
                issues.append(issue)
        issues += missing_paths(page, text)
        if issues:
            flagged += 1
            try:
                shown = page.relative_to(ROOT).as_posix()
            except ValueError:
                shown = page.as_posix()
            print(shown)
            for issue in issues:
                print(f"  - {issue}")

    print(f"{len(pages)} page(s) checked, {flagged} with issues.")
    return 1 if args.strict and flagged else 0


if __name__ == "__main__":
    sys.exit(main())
