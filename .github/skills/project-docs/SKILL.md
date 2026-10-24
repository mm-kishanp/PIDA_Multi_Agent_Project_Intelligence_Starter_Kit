---
name: project-docs
description: Create or update the PIDA knowledge base (project overview, requirements, feature inventory and feature pages, architecture, data model, API catalog, integrations, security, quality and deployment) from repository evidence. Creates any missing folders and pages from templates. Use after an audit, after behavior changes, or when asked to document a feature, area, or the whole project.
disable-model-invocation: true
---

# Project documentation

Keeps `docs/project-intelligence/` accurate, complete, and traceable to source. Input: a scope from the user, such as "the whole knowledge base", "the billing feature", "api-catalog", or "everything changed in the last sprint". With no scope, complete every page that is missing, still a template, or marked `Unknown — not yet audited`, including `project.md`, a page for every sub-project that lacks one, and a feature page for every inventory feature that lacks one (start with the lists under *Project pages remaining* and *Feature pages remaining* in `PROGRESS.md`, if any). When the scope names a feature or area, create or update the feature pages for every feature in it.

## Shared PIDA resources

In the skills folder (for example `.claude/skills/` or `.agents/skills/`):
- `project-audit/reference/knowledge-base-guide.md`: file map, fill rules, IDs, feature status rules, minimum standard per page. **Read it first.**
- `project-audit/reference/discovery-checklist.md`: how to find evidence per stack.
- `project-audit/templates/`: page templates, including `feature.md`.

## Before you start

1. Read `AGENTS.md` / `CLAUDE.md`, then `docs/project-intelligence/README.md`, `project.md`, `project-overview.md`, and `repository-map.md`.
2. If the knowledge base is missing or still templates, create `docs/project-intelligence/` and the pages in scope from the templates. If `project.md`, `project-overview.md`, and `repository-map.md` are not filled, fill them first using the discovery checklist, because every other page depends on them. Recommend `/project-audit` when the scope is the whole project and no audit has run.
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

- **Project page (`project.md`)**: the plain-language explanation of the project: what it is, the problem it solves, who uses it and how, what it does (linked to features), how it is organized into sub-projects, its clients, and its current state. Write it so a new team member, tester, or product owner understands the project from this page alone, without technical background.
- **Sub-project pages (`projects/<slug>/project.md`)**: when the repository has more than one sub-project, one page each from `sub-project.md`: what it is and why it is separate, responsibilities, features, entry point and runtime, build/run/test commands, deployment, dependencies and dependents, interfaces, data, configuration names, ownership, and risks. List every sub-project in `project.md`. Follow *Project pages* in the guide.
- **Project overview**: the technical summary. One-line description linking to `project.md`, domain glossary, stack, runtime components linked to sub-project pages, verified run commands, maturity.
- **Feature documentation**: every feature gets a row in `feature-inventory.md` **and** its own page, `features/FEAT-NNN-<slug>.md`, created from `feature.md` and linked from the row's `Page` column. On each page document the user outcome, users and permissions, entry points, main flow and error cases (Given/When/Then), data touched, integrations and side effects, configuration and flags, client availability, tests, and gaps. Simple or `Planned` features may have short pages; critical ones get every section filled. Follow *Feature pages* in the guide. When a run cannot finish every page, update *Feature pages remaining* in `PROGRESS.md`.
- **Requirements**: separate business goals, roles, functional requirements, non-functional requirements, and constraints. Requirements reverse-engineered from code are `Inferred` until a person confirms them.
- **Architecture**: describe current state only, unless asked for a proposal. Use Mermaid for 2–5 key flows. Follow the architecture skill for depth.
- **API catalog**: method, route or topic, auth, request and response schema, status codes, validation, side effects, evidence. Follow the api-development skill for depth.
- **Data model**: stores, entities, keys, relationships, constraints, indexes, tenancy, migrations, retention, sensitive fields. Follow the database-development skill for depth.
- **Client matrix**: list every client from the user and from code, how each is selected at runtime, the client-specific code locations, and Enabled / Disabled / Customized per feature. User-stated facts stay `Inferred (user-stated)` until a cited path confirms them. Follow *Client information* in the guide and checklist section 10.
- **Coding standards** (`coding-standards/`): for each of the eight topics, the standard (documented with its path, or inferred from a stated sample), check results, current practice with good examples, deviations with severity, and recommended changes; summarize in `overview.md`. Follow *Coding standards, reviews, and technical debt* in the guide and checklist section 11.
- **Code review guide, review findings, tech debt**: how reviews work and the checklist; the `RF-NNN` log with statuses; the `TD-NNN` register with hotspots. Never delete history; update statuses with evidence.
- **Deployment** (`deployment.md`): start with the strategy in plain words and a flow diagram, then the detail. **Debugging** (`debugging.md`): practical steps a developer can follow today.
- **SEO and AEO guides**: only for public web pages or content; otherwise `Not applicable — <evidence>`. Record AI-crawler policy as found; never change it.
- **Quality and deployment**: include only commands that were discovered in config or verified by running. Say which.

## Rules

- Never claim a feature is implemented from docs alone, and never claim the docs are exhaustive when scope was partial.
- Update pages in place; do not erase history in logs, decisions, or the backlog.
- No secrets, tokens, connection strings, or production data. Use placeholders and variable names.

## Report

Pages created, pages updated, sub-project and feature pages written and any still remaining, sections still Unknown and why, new questions and risks, and suggested follow-up.
