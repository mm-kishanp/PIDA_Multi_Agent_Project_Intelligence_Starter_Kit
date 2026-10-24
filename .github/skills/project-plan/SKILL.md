---
name: project-plan
description: Turn a feature request, business requirement, bug, or milestone into an evidence-based plan for this repository - clarified requirements, design approach, and a sequenced backlog of small verifiable tasks with acceptance criteria, test plans, risks, and estimates. Creates project-management/ and requirement pages if missing. Use before implementing anything non-trivial.
disable-model-invocation: true
---

# Project planning

Input: the user's goal, such as "add CSV export to reports", "fix duplicate invoices", or "prepare the v2 release". The output is a plan grounded in how this project actually works, written to the backlog so `/project-implement <task ID>` can execute it.

## Shared PIDA resources

In the skills folder: `project-audit/reference/knowledge-base-guide.md` (file map, fill rules, IDs), `project-audit/reference/discovery-checklist.md`, and `project-audit/templates/` (including `templates/project-management/`).

## Before you start

1. Read `AGENTS.md` / `CLAUDE.md`, `project-overview.md`, `repository-map.md`, `feature-inventory.md`, `requirements.md`, `architecture.md`, and `client-matrix.md` in `docs/project-intelligence/`, plus `project-management/BACKLOG.md`, `RISKS.md`, and `DECISIONS.md`.
2. If any are missing or still templates, discover the area the goal touches using the checklist. Create `project-management/` and its four files from the templates (removing example entries), and create the knowledge pages you need for this plan, filled for that area. Recommend `/project-audit` if the project has never been audited.
3. Check the backlog for existing tasks that overlap the goal. Extend or reference them; do not duplicate.

## Workflow

1. **Understand the goal**: who benefits, the observable outcome, and measurable success criteria. Write them as `BR-NNN` / `FR-NNN` / `NFR-NNN` entries in `requirements.md`, using Given/When/Then for functional behavior.
2. **Map the current state**: inspect the related code, existing features, conventions, data model, APIs, permissions, configuration, and tests. Cite paths. Note what can be reused. Establish the client scope: which clients want this, which must not be affected, and how existing client-specific behavior (checklist section 10) constrains the design. If the user names clients, record them in `client-matrix.md`.
3. **Resolve ambiguity**:
   - Ask one focused question when an answer would change data handling, security, compatibility, or major product behavior.
   - Otherwise record an explicit assumption in the plan and in `open-questions.md`, and continue.
4. **Choose an approach**: the smallest design consistent with existing patterns. When there is a real choice (new dependency, new service, schema redesign, public API change), compare 2–3 options and record the choice as a `Proposed` ADR in `DECISIONS.md`. Changes to public APIs or architectural direction need user approval.
5. **Break down the work** into tasks that can each be implemented and verified on their own, typically a few hours to a day. Cover as relevant: schema and migrations (with backfill and rollback), backend logic, API contract, UI, authorization, tenant isolation, configuration, observability, accessibility, performance, tests, documentation, and deployment steps.
6. **Write each task** in `BACKLOG.md` using the template fields:
   - stable `PIDA-NNN` ID, continuing from the highest existing number; never invent external tracker IDs;
   - status (`Ready` if unblocked, `Proposed` if it needs confirmation), priority P0–P3, outcome, scope and out-of-scope;
   - dependencies, likely files and components (evidence-backed paths);
   - client scope (`All`, specific `CLIENT-NNN`, or `Not applicable`) when the code serves several clients;
   - acceptance criteria as observable results (`AC-1`, `AC-2`, …);
   - test plan naming the test types and the exact commands from `quality-and-deployment.md`;
   - risks, and an estimate range with assumptions and confidence.
7. **Sequence**: order by dependency first, then risk (do the riskiest unknowns early), then value. Identify the first `Ready` task.
8. **Record risks** in `RISKS.md` and update `PROGRESS.md` with the goal, the plan summary, and the next step. Preserve all prior history.

## Rules

- Plan only what the goal needs; avoid speculative abstractions and unrelated refactors. List adjacent improvements as separate `Proposed` tasks if worth keeping.
- Estimates are planning ranges, not commitments.
- Do not mark anything `Done` while planning.

## Report

Goal and success criteria; key findings about the current state; chosen approach and any decision needing approval; task list (ID, title, priority, status, dependencies); top risks; assumptions and open questions; the recommended first task and the command to start it (`/project-implement PIDA-NNN`).
