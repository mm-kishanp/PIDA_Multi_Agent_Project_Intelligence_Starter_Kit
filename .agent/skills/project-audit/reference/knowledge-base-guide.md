# Knowledge base guide

This guide defines which files PIDA creates, where they go, which skill owns them, and the minimum standard each must meet. Every PIDA skill follows it.

## File map

Templates are in this skill's `templates/` folder. Paths in the **Target** column are relative to the repository root.

| Template | Target | Owner skills |
|---|---|---|
| `project-intelligence-README.md` | `docs/project-intelligence/README.md` | project-audit |
| `project-overview.md` | `docs/project-intelligence/project-overview.md` | project-audit, project-docs |
| `repository-map.md` | `docs/project-intelligence/repository-map.md` | project-audit |
| `feature-inventory.md` | `docs/project-intelligence/feature-inventory.md` | project-audit, project-docs, project-implement |
| `feature.md` | `docs/project-intelligence/features/FEAT-NNN-<slug>.md` (only for features that need more than one inventory row) | project-docs |
| `requirements.md` | `docs/project-intelligence/requirements.md` | project-docs, project-plan |
| `architecture.md` | `docs/project-intelligence/architecture.md` | architecture |
| `data-model.md` | `docs/project-intelligence/data-model.md` | database-development |
| `api-catalog.md` | `docs/project-intelligence/api-catalog.md` | api-development |
| `integrations.md` | `docs/project-intelligence/integrations.md` | architecture, api-development |
| `client-matrix.md` | `docs/project-intelligence/client-matrix.md` | project-audit, project-docs, project-implement (any skill that learns client facts) |
| `security-review.md` | `docs/project-intelligence/security-review.md` | security-review |
| `quality-and-deployment.md` | `docs/project-intelligence/quality-and-deployment.md` | testing, deployment |
| `open-questions.md` | `docs/project-intelligence/open-questions.md` | all skills |
| `analysis-log.md` | `docs/project-intelligence/analysis-log.md` | project-audit, project-refresh, project-docs |
| `project-management/BACKLOG.md` | `project-management/BACKLOG.md` | project-plan (project-audit seeds it) |
| `project-management/RISKS.md` | `project-management/RISKS.md` | all skills |
| `project-management/DECISIONS.md` | `project-management/DECISIONS.md` | architecture, project-plan |
| `project-management/PROGRESS.md` | `project-management/PROGRESS.md` | project-implement, project-status |

Any skill that needs a page that does not exist yet creates it from the template, fills the sections it has evidence for, and marks the rest `Unknown — not yet audited`.

## Creation rules

1. **Look for an equivalent first.** If the repository already has `ARCHITECTURE.md`, `docs/adr/`, an OpenAPI spec, an issue tracker, or similar, link to it from the PIDA page instead of copying it. Record the mapping in `docs/project-intelligence/README.md`. If the repository already keeps knowledge in a different folder, use that folder and tell the user.
2. **Create folders as needed**: `docs/project-intelligence/`, `docs/project-intelligence/features/` (only when a feature page is written), and `project-management/`.
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

## IDs

Use stable, never-reused IDs: `FEAT-NNN` (features), `BR-NNN` (business goals), `FR-NNN` / `NFR-NNN` (requirements), `INT-NNN` (integrations), `CLIENT-NNN` (clients), `SEC-NNN` (security findings), `Q-NNN` (open questions), `R-NNN` (risks), `ADR-NNN` (decisions), `PIDA-NNN` (backlog tasks). Continue from the highest existing number.

## Minimum standard per page

| Page | Must answer | Main evidence |
|---|---|---|
| project-overview | What the project is, for whom, and why, in plain language; key capabilities linked to FEAT IDs; domain glossary; stack with versions; runtime components; how to run it locally; maturity and activity | README, manifests, entry points, domain models, routes and UI, Git history |
| repository-map | Purpose of every top-level folder; entry points; manifests; test locations and commands; generated and excluded areas; conventions. A newcomer can find where to change any feature. | File tree, manifests, CODEOWNERS |
| feature-inventory | One row per user-facing capability and significant internal capability (jobs, imports, admin tools), with status, evidence, tests, gaps | Routes, screens, navigation, CLI commands, jobs, permission definitions, tests; README claims only as leads |
| requirements | Business goals (usually Inferred), roles and permissions, functional requirements for key features as Given/When/Then, non-functional requirements visible in config (timeouts, limits, caching, retention), constraints | Auth config, feature behavior, configuration, docs |
| architecture | Components and responsibilities, dependency direction, 2–5 key flows as Mermaid diagrams, trust boundaries, constraints, technical debt | Composition root, module references, traced flows |
| data-model | Every data store; entities with keys, relationships, sensitive fields, and tenant/ownership rules; migration mechanism and latest migration; Mermaid `erDiagram` when there are more than three entities | ORM models, schema files, migrations |
| api-catalog | Every externally reachable endpoint, event, or contract with auth; for more than ~50, group by resource with counts and detail the critical ones | Route registrations, controllers, OpenAPI/GraphQL/proto files, consumers |
| integrations | Every external system, direction, auth method, config names, failure handling | HTTP clients, SDKs, webhooks, queues |
| client-matrix | Every known client (from the user and from code) with its key in source; how a client is selected at runtime; every client-specific code location; which features are Enabled / Disabled / Customized per client; per-client customizations, integrations, config key names, and tests; or `Not applicable — <evidence>` for single-client code | User-provided lists, per-client config and folders, feature flags, tenant settings, client-code conditionals, seeds, deployment variants |
| security-review | Every surface row filled with a status; findings with severity and evidence; areas not reviewed | Auth middleware, policies, data access, config, dependencies, CI |
| quality-and-deployment | Local setup, quality gates with exact commands and whether they were run, pipelines, environments, release and rollback, observability, gaps | CI files, manifests, IaC, Dockerfiles |
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
