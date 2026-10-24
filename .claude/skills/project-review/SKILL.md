---
name: project-review
description: Review the current changes (working tree, a branch, or a commit range) in this repository for correctness against acceptance criteria, regression risk, security, test quality, API and schema compatibility, and documentation drift, using the project's own conventions and knowledge base. Use before marking a task Done or before opening a pull request.
disable-model-invocation: true
---

# Project review

Review the actual diff, not an imagined implementation. Input: optional task ID, branch, or commit range. Default scope: all uncommitted changes, plus commits on the current branch not yet on its base branch.

## Shared PIDA resources

In the skills folder: `project-audit/reference/knowledge-base-guide.md` and `project-audit/templates/`.

## Before you start

1. Determine the scope: `git status --short`, `git diff`, `git diff --staged`, and `git log --oneline <base>..HEAD` with `git diff <base>...HEAD`. Include untracked files relevant to the change.
2. Read `AGENTS.md` / `CLAUDE.md`, the task in `BACKLOG.md` (acceptance criteria and test plan), and the knowledge pages for the touched area: `repository-map.md`, `architecture.md`, `security-review.md`, `api-catalog.md`, `data-model.md`, `quality-and-deployment.md`.
3. If those pages are missing or still templates, learn the conventions directly from the surrounding code and tests. Note in the report that the knowledge base needs `/project-audit`. Do not block the review on it.

## What to check

| Area | Questions |
|---|---|
| Correctness | Does each acceptance criterion hold? Are edge cases, empty and large inputs, and error paths handled? Any off-by-one, null, race, or ordering issue? |
| Conventions | Does it follow the project's existing structure, naming, error handling, logging, and dependency patterns? |
| Security | Authentication and authorization on new paths; tenant and ownership checks on every data access; input validation; injection (SQL, command, template, path); SSRF; unsafe deserialization; secrets in code, config, or logs; sensitive data in logs or errors |
| Compatibility | Public API, event, and schema changes; migration safety (locks, backfill, rollback); configuration changes and defaults; feature flags |
| Client impact | Which clients the change reaches (check `client-matrix.md` and client-specific code); does a change meant for one client leak to others through shared code; are client branches, per-client config, and flags updated consistently; new hardcoded client IDs; tests for each affected client variant |
| Reliability | Retries, idempotency, timeouts, transactions, concurrency, resource cleanup, observability for new failure modes |
| Performance | N+1 queries, unbounded queries or loops, missing indexes, large payloads, work on hot paths |
| Tests | New behavior covered for normal, failure, boundary, and authorization cases; tests deterministic; no test deleted, skipped, or weakened |
| Diff hygiene | Unrelated refactors, debug code, generated or build artifacts, formatting churn, accidental files, other people's uncommitted changes |
| Documentation | Feature status, API catalog, data model, client matrix, task status, and decisions consistent with the change |

## Independent review

Where subagents are supported (Claude Code: `pida-reviewer`), delegate an independent pass with the diff scope and the acceptance criteria, not your conclusions. Merge its findings with yours and verify each before reporting.

## Verification

Run the relevant checks from `quality-and-deployment.md` or CI (focused tests, lint, type check, build), or use `pida-test-runner`. Report the exact commands and outcomes. Never state a check passed unless it ran and was conclusive.

## Severity

| Severity | Meaning |
|---|---|
| Critical | Security breach, data loss or corruption, or production outage likely |
| High | Wrong behavior for a main flow, broken compatibility, or a significant security weakness |
| Medium | Edge-case bug, missing important test, reliability or performance risk |
| Low | Maintainability, minor convention, or documentation issue |

## Output

1. Scope reviewed (files and commits) and anything not reviewed.
2. Findings ordered by severity. Each has `path:line`, the issue, a concrete failure scenario, **verified defect** or **concern**, and a suggested fix.
3. Acceptance criteria: Met / Not met / Cannot verify, with evidence.
4. Checks run, with results.
5. Documentation drift found.

Report findings first. Fix in-scope issues only if asked, or when the user's request included fixing; ask before expanding scope. Record out-of-scope findings as `Proposed` tasks in `BACKLOG.md` and significant risks in `RISKS.md`.
