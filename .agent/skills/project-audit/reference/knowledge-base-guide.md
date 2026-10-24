# Knowledge base guide

This guide defines which files PIDA creates, where they go, which skill owns them, and the minimum standard each must meet. Every PIDA skill follows it.

## File map

Templates are in this skill's `templates/` folder. Paths in the **Target** column are relative to the repository root.

| Template | Target | Owner skills |
|---|---|---|
| `project-intelligence-README.md` | `docs/project-intelligence/README.md` | project-audit |
| `project.md` | `docs/project-intelligence/project.md` | project-audit, project-docs |
| `sub-project.md` | `docs/project-intelligence/projects/<slug>/project.md`, one per sub-project when the repository has more than one | project-audit, project-docs, project-implement |
| `project-overview.md` | `docs/project-intelligence/project-overview.md` | project-audit, project-docs |
| `repository-map.md` | `docs/project-intelligence/repository-map.md` | project-audit |
| `feature-inventory.md` | `docs/project-intelligence/feature-inventory.md` | project-audit, project-docs, project-implement |
| `feature.md` | `docs/project-intelligence/features/FEAT-NNN-<slug>.md`, one page per feature in the inventory | project-audit, project-docs, project-implement |
| `requirements.md` | `docs/project-intelligence/requirements.md` | project-docs, project-plan |
| `architecture.md` | `docs/project-intelligence/architecture.md` | architecture |
| `data-model.md` | `docs/project-intelligence/data-model.md` | database-development |
| `api-catalog.md` | `docs/project-intelligence/api-catalog.md` | api-development |
| `integrations.md` | `docs/project-intelligence/integrations.md` | architecture, api-development |
| `client-matrix.md` | `docs/project-intelligence/client-matrix.md` | project-audit, project-docs, project-implement (any skill that learns client facts) |
| `security-review.md` | `docs/project-intelligence/security-review.md` | security-review |
| `quality-and-deployment.md` | `docs/project-intelligence/quality-and-deployment.md` | testing, deployment |
| `deployment.md` | `docs/project-intelligence/deployment.md` | deployment, project-audit |
| `debugging.md` | `docs/project-intelligence/debugging.md` | project-audit, project-docs, testing |
| `coding-standards/overview.md` and the eight topic pages in `coding-standards/` | `docs/project-intelligence/coding-standards/` (same file names) | project-audit, project-review, project-docs |
| `code-review-guide.md` | `docs/project-intelligence/code-review-guide.md` | project-audit, project-review |
| `review-findings.md` | `docs/project-intelligence/review-findings.md` | project-audit, project-review, project-implement |
| `tech-debt.md` | `docs/project-intelligence/tech-debt.md` | project-audit, architecture, project-review, project-implement |
| `seo-guide.md` | `docs/project-intelligence/seo-guide.md` | project-audit, project-docs |
| `aeo-guide.md` | `docs/project-intelligence/aeo-guide.md` | project-audit, project-docs |
| `open-questions.md` | `docs/project-intelligence/open-questions.md` | all skills |
| `analysis-log.md` | `docs/project-intelligence/analysis-log.md` | project-audit, project-refresh, project-docs |
| `project-management/BACKLOG.md` | `project-management/BACKLOG.md` | project-plan (project-audit seeds it) |
| `project-management/RISKS.md` | `project-management/RISKS.md` | all skills |
| `project-management/DECISIONS.md` | `project-management/DECISIONS.md` | architecture, project-plan |
| `project-management/PROGRESS.md` | `project-management/PROGRESS.md` | project-implement, project-status |

Any skill that needs a page that does not exist yet creates it from the template, fills the sections it has evidence for, and marks the rest `Unknown — not yet audited`.

## Creation rules

1. **Look for an equivalent first.** If the repository already has `ARCHITECTURE.md`, `docs/adr/`, an OpenAPI spec, an issue tracker, or similar, link to it from the PIDA page instead of copying it. Record the mapping in `docs/project-intelligence/README.md`. If the repository already keeps knowledge in a different folder, use that folder and tell the user.
2. **Create folders as needed**: `docs/project-intelligence/`, `docs/project-intelligence/features/`, `docs/project-intelligence/coding-standards/`, `docs/project-intelligence/projects/<slug>/` (only when the repository has more than one sub-project), and `project-management/`.
3. **Start from the template.** Keep its headings in order; add sections the project needs; delete sections only if they are irrelevant and say why in the scope line.
4. **Fill every placeholder.** A finished section is one of:
   - evidence-backed content labelled Verified / Inferred / Unknown with source paths;
   - `Not applicable — <evidence>` (for example `Not applicable — no HTTP server; the project is a CLI (cmd/tool/main.go)`);
   - `Unknown — checked <what>; next step: <how to find out>`, with a matching `Q-NNN` in `open-questions.md` if it matters.
   Never leave `[...]` placeholders, `YYYY-MM-DD`, or template example rows such as `FEAT-001 | [Name]`.
5. **Date and scope.** Set `Last reviewed:` to today's date (ISO `YYYY-MM-DD`) and state the evidence scope, including what was not inspected.
6. **Update, don't overwrite.** When a page already has real content, verify and edit it in place. Keep history in `analysis-log.md` and `DECISIONS.md`; never erase backlog, risk, or decision history.
7. **Create every page in the file map during an audit**, even when the answer is short. A one-line `Not applicable` page tells later readers the area was checked.
8. **No secrets or production data**, ever. Record variable names and secret locations only.

## Client information

`client-matrix.md` records which clients the codebase serves and what works for which client. Every skill keeps it current:

1. **Capture user-provided client lists.** Whenever the user names clients (in a request, a pasted list, a file, or a remark such as "client X uses SSO, client Y doesn't"), record each one in `client-matrix.md` in the same session: add a row to *Client list sources* and *Clients* labelled `Provided by user, <date>`, and record any stated behavior as `Inferred (user-stated)` until code confirms it. Create the page from the template if it does not exist. Do not wait for an audit.
2. **Verify against code.** For each client, find how it is selected at runtime and which code paths, configuration keys, flags, and integrations differ. Promote a user-stated fact to Verified only with a cited path. When the code contradicts the user's statement, record both and add a `Q-NNN`.
3. **Reconcile lists.** Clients found in code or config but missing from the user's list, and listed clients with no trace in code, both go to `open-questions.md`.
4. **Keep the matrix in step with features.** When a feature's availability or behavior differs by client, fill its row in *Feature availability by client* and the *Clients* column of `feature-inventory.md`.
5. **Names and codes only.** Never store client contacts, contract terms, pricing, credentials, or customer records. If the user marks client names as confidential, use the codes found in source instead.

## Project pages

Every repository gets `project.md`, a plain-language explanation of the project for anyone joining it, including non-developers. `project-overview.md` is the technical summary and links to it. Do not repeat between the two: users, capabilities, and the problem solved belong in `project.md`; stack, runtime, glossary, and run commands belong in `project-overview.md`.

When the repository contains more than one **sub-project**, each also gets `projects/<slug>/project.md`, created from `sub-project.md`, and `project.md` lists them all with links.

1. **What counts as a sub-project.** A unit that is built, run, deployed, or published on its own and usually has its own manifest or entry point: a web app, API, worker, function app, mobile app, CLI, shared library or package, or a separately deployed infrastructure stack. Examples: each project in a `.sln`, each package in a workspace or monorepo, each service folder with its own Dockerfile or pipeline.
2. **What does not.** Test projects (document them under the sub-project they test), generated or vendored code, and plain folders inside one deployable unit.
3. **Slug.** The sub-project's name in lowercase kebab-case (`projects/billing-api/project.md`).
4. **Single-project repositories** get only `project.md`; its *How it is organized* section says `Single project — <evidence>` and no `projects/` folder is created.
5. **Large repositories.** With more sub-projects than can be documented well in one run (roughly more than 15), write pages for deployable applications and services first, then shared libraries, then the rest, and list the ones still without a page under *Project pages remaining* in `PROGRESS.md`.
6. **Keep them current.** A change to a sub-project's purpose, entry point, dependencies, interfaces, configuration, or deployment updates its page in the same change. A new sub-project gets a new page and a row in `project.md`.

## Coding standards, reviews, and technical debt

The `coding-standards/` pages describe how the code is written today, the standard the project should hold to, where the code deviates, and what to change. They guide implementation and review.

1. **Find documented standards first**: `.editorconfig`, formatter and linter configs, analyzer rule sets, CONTRIBUTING, style guides, ADRs. A rule backed by one of these is Verified, with its path.
2. **Otherwise infer from the dominant pattern.** Sample representative files from each sub-project and layer (typically 3–5 per layer, plus the most-changed files from Git history) and state the sample on each page. A rule followed by most of the sample is `Inferred: N of M sampled files follow it` until the team confirms it. Never present an inferred rule as the team's policy.
3. **Every page answers four things**: the standard, how the code does it today (with good examples to copy), deviations (with `path:line` and severity), and recommended changes (to the code or to the standard itself, with effort and priority).
4. **Recommendations are proposals.** Do not change code during an audit. Put actionable changes in `BACKLOG.md` as `Proposed` tasks; a change to the standard itself becomes a `Proposed` ADR in `DECISIONS.md` until accepted.
5. **Findings and debt.** A concrete defect or deviation worth tracking goes to `review-findings.md` as `RF-NNN`. A long-lived structural problem (layering violations, duplication, outdated dependencies, untested critical paths, manual deployment steps) goes to `tech-debt.md` as `TD-NNN`. Link both ways to tasks.
6. **Keep them current.** `/project-review` appends findings and checks changes against the standards and `code-review-guide.md`. `/project-implement` follows the standards and updates the status of findings and debt it resolves. Every re-audit re-checks open findings and debt items and marks them Fixed or Paid down only with evidence.
7. Write `Not applicable — <evidence>` on a topic page that cannot apply (for example `async-await.md` in a language with no async model).

## Deployment, debugging, SEO, and AEO

- **`deployment.md`** explains the deployment strategy in plain language and then the detail: what is deployed, environments, pipelines, infrastructure, configuration names, migrations, release, rollback, post-deploy verification, observability, and manual steps. `quality-and-deployment.md` keeps local setup, quality gates, and CI checks, and links to it.
- **`debugging.md`** tells a developer how to run each sub-project under a debugger, attach to a running process, configure local services and test data, find logs, debug tests and background jobs, investigate deployed environments read-only, and fix common problems. Mark each command Verified (run) or Documented (read).
- **`seo-guide.md` and `aeo-guide.md`** apply only when the project serves public web pages or content. Otherwise write `Not applicable — <evidence>` in the Applicability line (for example an internal tool behind sign-in, an API, a CLI, or a mobile app). Whether to allow AI crawlers is a business decision: record the current state and ask; never change it unprompted.

## Feature pages

Every feature in `feature-inventory.md` gets its own page, `features/FEAT-NNN-<slug>.md`, created from `feature.md`. `<slug>` is the feature name in lowercase kebab-case (`FEAT-007-csv-export.md`).

1. **Link both ways.** The inventory's `Page` column links to the page; the page names its inventory row. Keep status, clients, and confidence identical in both places.
2. **Depth follows the feature.** A simple or `Planned` feature can have a short page: outcome, status, evidence, and gaps, with the remaining sections marked `Not applicable — <reason>` or `Unknown — <what was checked>`. Critical features (authentication, payments, data deletion, tenant access, core business flows) get every section filled.
3. **Large inventories.** When there are too many features to document well in one run (roughly more than 40), write pages in this order: critical features, then `Implemented` and `Partial`, then the rest. List the features still without a page under *Feature pages remaining* in `PROGRESS.md` so the next `/project-docs` run continues from there. Never create empty placeholder pages to hit a count.
4. **Keep them current.** Any skill that changes a feature's behavior, status, tests, or client availability updates its page in the same change, and creates the page if it is missing.

## IDs

Use stable, never-reused IDs: `FEAT-NNN` (features), `BR-NNN` (business goals), `FR-NNN` / `NFR-NNN` (requirements), `INT-NNN` (integrations), `CLIENT-NNN` (clients), `RF-NNN` (review findings), `TD-NNN` (technical debt), `SEC-NNN` (security findings), `Q-NNN` (open questions), `R-NNN` (risks), `ADR-NNN` (decisions), `PIDA-NNN` (backlog tasks). Continue from the highest existing number.

## Minimum standard per page

| Page | Must answer | Main evidence |
|---|---|---|
| project | What the project is, for whom, and why, in plain language a non-developer understands; the problem it solves; users and their workflows; capabilities linked to FEAT IDs; a typical journey; every sub-project with a link to its page (or `Single project`); clients; current state; links onward | README, domain models, routes and UI, auth config, feature inventory, manifests, Git history |
| `projects/<slug>/project` | One page per sub-project: what it is and why it is separate, responsibilities, features it owns or uses, entry point, runtime, build/run/test commands, deployment, dependencies and dependents, interfaces exposed and consumed, data, configuration names, ownership, risks | The sub-project's manifest, entry point, composition root, references to other sub-projects, tests, pipeline |
| project-overview | One-line summary linking to `project.md`; domain glossary; stack with versions; runtime components linked to sub-project pages; how to run it locally; maturity and activity | README, manifests, entry points, domain models, Git history |
| repository-map | Purpose of every top-level folder; entry points; manifests; test locations and commands; generated and excluded areas; conventions. A newcomer can find where to change any feature. | File tree, manifests, CODEOWNERS |
| feature-inventory | One row per user-facing capability and significant internal capability (jobs, imports, admin tools), with status, clients, a link to its feature page, evidence, tests, gaps | Routes, screens, navigation, CLI commands, jobs, permission definitions, tests; README claims only as leads |
| features/FEAT-NNN-* | One page per inventory feature: user outcome, users and permissions, entry points, main flow and error cases as Given/When/Then, data touched, integrations and side effects, configuration and flags, client availability, tests, gaps. Depth per *Feature pages* | The feature's traced code path, tests, config, and client-specific code |
| requirements | Business goals (usually Inferred), roles and permissions, functional requirements for key features as Given/When/Then, non-functional requirements visible in config (timeouts, limits, caching, retention), constraints | Auth config, feature behavior, configuration, docs |
| architecture | Components and responsibilities, dependency direction, 2–5 key flows as Mermaid diagrams, trust boundaries, constraints, architectural risks (debt goes to `tech-debt.md`) | Composition root, module references, traced flows |
| data-model | Every data store; entities with keys, relationships, sensitive fields, and tenant/ownership rules; migration mechanism and latest migration; Mermaid `erDiagram` when there are more than three entities | ORM models, schema files, migrations |
| api-catalog | Every externally reachable endpoint, event, or contract with auth; for more than ~50, group by resource with counts and detail the critical ones | Route registrations, controllers, OpenAPI/GraphQL/proto files, consumers |
| integrations | Every external system, direction, auth method, config names, failure handling | HTTP clients, SDKs, webhooks, queues |
| client-matrix | Every known client (from the user and from code) with its key in source; how a client is selected at runtime; every client-specific code location; which features are Enabled / Disabled / Customized per client; per-client customizations, integrations, config key names, and tests; or `Not applicable — <evidence>` for single-client code | User-provided lists, per-client config and folders, feature flags, tenant settings, client-code conditionals, seeds, deployment variants |
| security-review | Every surface row filled with a status; findings with severity and evidence; areas not reviewed | Auth middleware, policies, data access, config, dependencies, CI |
| quality-and-deployment | Local setup, quality gates with exact commands and whether they were run, CI checks and whether they block merges, gaps; links to `deployment.md` and `debugging.md` | CI files, manifests, package scripts, hooks |
| deployment | Plain-language deployment strategy and a flow diagram; what is deployed per sub-project; environments; pipelines; infrastructure; configuration and secret names; migrations; release; rollback; post-deploy verification; observability; manual steps; recommended improvements | Pipeline files, Dockerfiles, IaC, release scripts, deployment docs |
| debugging | How to debug each sub-project locally, attach, configure local services and test data, find logs, debug tests and jobs, diagnose deployed environments read-only, common problems | IDE launch configs, compose files, README, logging config, scripts |
| `coding-standards/overview` | Standard sources and enforcement; how the code is implemented; scorecard for the eight topics; top recommended changes; proposed changes to the standards | Config files, sampled code, topic pages |
| `coding-standards/<topic>` | Standard (documented or inferred, with enforcement), check results, current practice with examples, deviations with severity, recommended changes; or `Not applicable` | Sampled code per sub-project and layer, linter and analyzer configs |
| code-review-guide | How reviews work here (PR template, code owners, required checks, conventions), review checklist linked to the standards, what blocks a merge, recurring themes | PR templates, CODEOWNERS, CI, CONTRIBUTING, review findings |
| review-findings | Every finding from audits and reviews with ID, source, severity, location, status, and task; summary counts | Audit and review runs |
| tech-debt | Summary, hotspots, debt register with type, evidence, impact, effort, priority, status, task; paid-down log | Code, Git history, TODO/FIXME counts, manifests, findings |
| seo-guide | Applicability; rendering per site; check results; findings; recommended changes; or `Not applicable` | Front-end code, page templates, head/meta handling, static files |
| aeo-guide | Applicability; AI crawler access; check results; findings; recommended changes; or `Not applicable` | Front-end code, structured data, `robots.txt`, static files |
| open-questions | Every Unknown that affects behavior, security, data, or delivery | All pages |
| analysis-log | One entry per audit/refresh run: trigger, scope, checks run, documents updated, next steps | This run |
| BACKLOG | Remove the template example; actionable gaps as `Proposed` tasks with evidence and acceptance criteria | Findings |
| RISKS | Remove the template example; risks with likelihood, impact, evidence, mitigation | Findings |
| DECISIONS | Remove the template example; link existing ADRs; record major pre-existing choices (framework, data store, auth provider, hosting) as `Accepted (pre-existing, inferred from code)` with evidence | Manifests, code, existing ADRs |
| PROGRESS | Current goal, what was done, files changed, checks run, next exact steps | This run |

## Feature status rules

| Status | Required evidence |
|---|---|
| Implemented | Entry point is registered and reachable, the code path is traced end to end, and tests or other runtime evidence exist |
| Partial | Some layers are missing, the path contains TODO/not-implemented code, it is behind a disabled flag, or it is incomplete and untested |
| Planned | Only docs, tickets, TODOs, stubs, or UI placeholders exist |
| Deprecated | Marked obsolete, unreachable, or flagged off with removal notes |
| Unknown | Not enough evidence to decide |

## Final checks before reporting

1. Run `python scripts/doc-freshness.py` if the script exists; resolve placeholder dates and missing paths in pages you wrote.
2. Search the files you wrote for leftover placeholders: `YYYY-MM-DD`, `[Name]`, `[Purpose]`, `[Path`, `FEAT-001 | [`, `PIDA-001 — [`.
3. Search the files you wrote for secret-like content: `password=`, `secret=`, `token=`, `AKIA`, `-----BEGIN`, `Server=`, `mongodb://`, `postgres://`. Remove any values.
4. Confirm every Verified claim cites a path, and every Inferred claim gives a reason and confidence.
5. Confirm every client the user named in this session appears in `client-matrix.md`.
6. Confirm all nine `coding-standards/` pages, `code-review-guide.md`, `review-findings.md`, `tech-debt.md`, `deployment.md`, `debugging.md`, `seo-guide.md`, and `aeo-guide.md` exist and are filled or marked `Not applicable — <evidence>`, and that every `RF-NNN` and `TD-NNN` worth acting on has a task.
7. Confirm `project.md` lists every sub-project and each has an existing `projects/<slug>/project.md`, or is listed under *Project pages remaining* in `PROGRESS.md`.
8. Confirm every inventory row links to an existing `features/FEAT-NNN-*.md` page, or is listed under *Feature pages remaining* in `PROGRESS.md`, and that every feature page matches an inventory row.
