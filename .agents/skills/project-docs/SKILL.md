---
name: project-docs
description: Create or update the PIDA knowledge base (project overview, requirements, feature inventory and feature pages, architecture, data model, API catalog, integrations, security, quality and deployment) from repository evidence. Creates any missing folders and pages from templates. Use after an audit, after behavior changes, or when asked to document a feature, area, or the whole project.
disable-model-invocation: true
---

# Project documentation

Keeps `docs/project-intelligence/` accurate, complete, and traceable to source. Input: a scope from the user, such as "the whole knowledge base", "the billing feature", "api-catalog", or "everything changed in the last sprint". With no scope, complete every page that is missing, still a template, or marked `Unknown — not yet audited`.

## Shared PIDA resources

In the skills folder (for example `.claude/skills/` or `.agents/skills/`):
- `project-audit/reference/knowledge-base-guide.md`: file map, fill rules, IDs, feature status rules, minimum standard per page. **Read it first.**
- `project-audit/reference/discovery-checklist.md`: how to find evidence per stack.
- `project-audit/templates/`: page templates, including `feature.md`.

## Before you start

1. Read `AGENTS.md` / `CLAUDE.md`, then `docs/project-intelligence/README.md`, `project-overview.md`, and `repository-map.md`.
2. If the knowledge base is missing or still templates, create `docs/project-intelligence/` and the pages in scope from the templates. If `project-overview.md` and `repository-map.md` are not filled, fill them first using the discovery checklist, because every other page depends on them. Recommend `/project-audit` when the scope is the whole project and no audit has run.
3. Find existing authoritative docs (ADRs, OpenAPI specs, wiki exports, READMEs). Link to them rather than copying.

## Workflow

1. **Plan**: list the pages to create or update, and why each is in scope (missing, template, stale, or affected by a change).
2. **Gather evidence** per page from source, tests, schemas, migrations, API specs, CI, and deployment files. Docs and tickets are leads, not proof.
3. **Write** each page to the minimum standard in the guide:
   - fill every section with labelled content, `Not applicable — <evidence>`, or `Unknown — checked <what>; next step: <how>`;
   - cite paths and symbols for Verified claims; give reasons and confidence for Inferred claims;
   - set `Last reviewed:` to today and state the evidence scope.
4. **Cross-link**: feature rows → feature pages, APIs, data entities, and tests; requirements → features; risks and questions → their IDs.
5. **Record**: append an `analysis-log.md` entry; add new unknowns to `open-questions.md` and new risks to `project-management/RISKS.md`.
6. **Check** using the final checks in the guide, then report.

## Page-specific guidance

- **Project overview**: start with what the project is, for whom, and why, in plain language. Include the domain glossary and verified run commands. A new team member should understand the project from this page alone.
- **Feature documentation**: for each feature document user outcome, users and permissions, entry points, main flow and error cases (Given/When/Then), data touched, integrations and side effects, configuration and flags, tests, and gaps. Use one inventory row for simple features. Create `features/FEAT-NNN-<slug>.md` from `feature.md` for complex or critical features, and link it from the inventory.
- **Requirements**: separate business goals, roles, functional requirements, non-functional requirements, and constraints. Requirements reverse-engineered from code are `Inferred` until a person confirms them.
- **Architecture**: describe current state only, unless asked for a proposal. Use Mermaid for 2–5 key flows. Follow the architecture skill for depth.
- **API catalog**: method, route or topic, auth, request and response schema, status codes, validation, side effects, evidence. Follow the api-development skill for depth.
- **Data model**: stores, entities, keys, relationships, constraints, indexes, tenancy, migrations, retention, sensitive fields. Follow the database-development skill for depth.
- **Client matrix**: list every client from the user and from code, how each is selected at runtime, the client-specific code locations, and Enabled / Disabled / Customized per feature. User-stated facts stay `Inferred (user-stated)` until a cited path confirms them. Follow *Client information* in the guide and checklist section 10.
- **Quality and deployment**: include only commands that were discovered in config or verified by running. Say which.

## Rules

- Never claim a feature is implemented from docs alone, and never claim the docs are exhaustive when scope was partial.
- Update pages in place; do not erase history in logs, decisions, or the backlog.
- No secrets, tokens, connection strings, or production data. Use placeholders and variable names.

## Report

Pages created, pages updated, sections still Unknown and why, new questions and risks, and suggested follow-up.
