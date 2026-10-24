---
name: project-implement
description: Implement one backlog task (or a clearly specified change) end to end in this repository - code, tests, migrations, configuration examples, and documentation - following existing conventions, verifying with the project's real quality gates, and updating the backlog, knowledge base, and progress records. Use with a task ID such as PIDA-012.
disable-model-invocation: true
---

# Task implementation

Input: a task ID from `project-management/BACKLOG.md`, or a specific change. If no task exists, create a lightweight task record first, with scope, acceptance criteria, and a test plan.

## Shared PIDA resources

In the skills folder: `project-audit/reference/knowledge-base-guide.md` (which page records what), `project-audit/reference/discovery-checklist.md`, and `project-audit/templates/`.

## Before you start

1. Run `git status --short --branch`. Note uncommitted changes that are not yours and leave them alone.
2. Read `AGENTS.md` / `CLAUDE.md` and nested instructions near the code, then `project.md`, the page of each sub-project you will touch, `project-overview.md`, `repository-map.md`, `quality-and-deployment.md`, and the knowledge pages relevant to the task (feature, API, data model, security, and `client-matrix.md` when the code serves several clients), the `coding-standards/` pages, and open items in `review-findings.md` and `tech-debt.md` for the files you will touch.
3. If the knowledge base or `project-management/` is missing, create them from the templates. At minimum fill `repository-map.md` and `quality-and-deployment.md` for the affected area, because you need the conventions and test commands. Recommend `/project-audit` for full coverage.
4. Validate the docs against current code. When they disagree, the code wins: note the drift and fix the docs in step 10.

## Workflow

1. **Confirm the task**: acceptance criteria, dependencies (are they `Done`?), and out-of-scope items. If a critical ambiguity affects data loss, security, compatibility, or major product behavior, ask one focused question. Otherwise proceed with a documented assumption.
2. **Start**: set the task to `In Progress` and write the plan (files to change, tests to add, commands to run) into `PROGRESS.md`.
3. **Trace** callers, data flows, permissions, tenant boundaries, configuration, error handling, logging, and backward compatibility for every symbol you will change. Identify which clients the change affects: client-specific branches, per-client config or flags, and client-specific folders (discovery checklist section 10). A change to shared code reaches every client unless gated. If the task targets one client, keep other clients' behavior unchanged and say how you verified that. When the client scope is unclear and the change alters behavior, ask.
4. **Implement** the smallest complete change:
   - follow the `coding-standards/` pages and existing patterns for layering, async, structure, comments, constants, error handling, logging, naming, and formatting; do not copy a pattern listed there as a deviation;
   - preserve public API and schema compatibility unless the task explicitly changes it;
   - write migrations to be reversible or document the rollback;
   - add new configuration as variable names with placeholders in example files, never real values;
   - add no new dependency unless needed; explain it in the report and in `DECISIONS.md` if significant.
5. **Test**: add or update tests for the normal path, failure and validation cases, boundaries, authorization or tenant isolation, and each affected client variant where relevant. Follow the testing skill. Never delete, skip, or weaken a test to get a pass.
6. **Verify**: run the focused tests first, then the relevant lint, type, build, and broader test commands from `quality-and-deployment.md` or CI. Record exact commands and outcomes. Where subagents are supported (Claude Code: `pida-test-runner`), you may delegate the runs.
7. **Review your diff** (`git diff`, `git status`): accidental files, debug code, secrets, unrelated refactors, generated artifacts, formatting churn, API or schema risks. For risky changes, consider an independent review (`pida-reviewer` or the project-review skill).
8. **Check acceptance**: mark each `AC-n` as met, with evidence.
9. **Set status**: `Done` only when every acceptance criterion is met and the required verification passed. Otherwise use `In Review` (complete but not fully verified) or `Blocked` (with the reason).
10. **Update the documentation affected by the change**:

| If you changed… | Update |
|---|---|
| user-visible behavior | `feature-inventory.md` (status, evidence, tests), the feature's page in `features/` (create it if missing; a new feature gets a new `FEAT-NNN` row and page), `requirements.md` |
| a sub-project's purpose, entry point, dependencies, interfaces, configuration, or deployment; or added a sub-project | its `projects/<slug>/project.md` (create it for a new sub-project) and the sub-project list in `project.md` |
| routes, contracts, events | `api-catalog.md` |
| schema, migrations, entities | `data-model.md` |
| external calls or webhooks | `integrations.md` |
| client-specific code, config, or flags, or learned which client has what | `client-matrix.md`, the `Clients` column of `feature-inventory.md` |
| auth, permissions, secrets handling | `security-review.md` |
| build, test, CI checks, local setup | `quality-and-deployment.md` |
| pipelines, environments, release, rollback, infrastructure | `deployment.md` |
| how to run, debug, or seed the project locally | `debugging.md` |
| fixed a review finding or paid down debt; or noticed new debt | `review-findings.md` (status, evidence) and `tech-debt.md` |
| a convention the team agreed to change | the matching `coding-standards/` page and `DECISIONS.md` |
| public pages, meta tags, structured data, `robots.txt`, sitemaps | `seo-guide.md`, `aeo-guide.md` |
| component boundaries or a significant choice | `architecture.md`, `DECISIONS.md` |
| anything uncertain or risky | `open-questions.md`, `RISKS.md` |

11. **Record** in `PROGRESS.md`: completed work, files changed with reasons, commands and results, blockers, and exact next steps.

## Boundaries

Do not push, merge, deploy, change shared infrastructure, run migrations against shared databases, or perform destructive data operations without explicit approval.

## Report

Behavior delivered; clients affected (or "all" / "single-client"); files changed; tests added; commands run with Pass/Fail; acceptance criteria status; docs and backlog updated; known gaps, risks, and manual follow-up.
