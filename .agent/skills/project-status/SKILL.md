---
name: project-status
description: Report where the project stands and the exact next step by reading PROGRESS.md, the backlog, risks, decisions, the knowledge base, and Git state, and reconciling them with the working tree. Use at the start of a session, after switching context, or before resuming interrupted work.
disable-model-invocation: true
---

# Project status and resume

Gives a fresh session the context it needs in one pass. Read-only unless the user asks to resume or the records are missing.

## Shared PIDA resources

In the skills folder: `project-audit/reference/knowledge-base-guide.md` and `project-audit/templates/project-management/`.

## Workflow

1. **Repository state**: confirm the root. When Git is available run `git status --short --branch`, `git log --oneline -15`, and `git stash list`. Note uncommitted changes and do not alter them.
2. **Records**: read `project-management/PROGRESS.md`, `BACKLOG.md`, `RISKS.md`, `DECISIONS.md` (or the repository's equivalent tracker), and the opening lines of `docs/project-intelligence/project-overview.md`.
3. **If records are missing**:
   - No `project-management/` and no knowledge base: say the project has not been onboarded, give a short orientation from the README and manifests, and recommend `/project-audit`.
   - Knowledge base present but no `project-management/`: create the four files from the templates, removing example entries, and record a session-start entry in `PROGRESS.md`.
4. **Knowledge base health**: run `python scripts/doc-freshness.py` if it exists, or check `Last reviewed` dates manually. Note pages that are templates, stale, or cite missing paths.
5. **Reconcile records with reality**:
   - files under "Files changed" that no longer exist, and modified files that are not recorded;
   - tasks `In Progress` with no matching changes; tasks `Done` without recorded verification;
   - blockers or questions that later commits or decisions appear to resolve;
   - commits since the last progress update that no task explains.
   Report mismatches as findings; do not silently rewrite history.
6. **Next step**: the exact step recorded in `PROGRESS.md`. If none, the highest-priority `Ready` task whose dependencies are `Done`.
7. **Resume** only when the user asked: continue the next step with the project-implement workflow. Otherwise stop after the report.
8. Edit `PROGRESS.md` only to correct verified inaccuracies or add a session-start entry, preserving prior content.

## Report format

```text
Project: <one-line description from project-overview>
Branch / working tree: <branch, ahead/behind, uncommitted summary>
Current goal / task: <goal> / <PIDA-NNN title, status>
Tasks: Ready n · In Progress n · In Review n · Blocked n · Proposed n · Done n
In progress / blocked: <ID — title — reason>
Open high risks: <R-NNN — summary>
Decisions needed from you: <list>
Last recorded verification: <command — result — date> (as recorded, not re-run)
Knowledge base: <fresh | n pages stale/template — list>
Mismatches found: <list or none>
Next step: <exact action and command>
```
