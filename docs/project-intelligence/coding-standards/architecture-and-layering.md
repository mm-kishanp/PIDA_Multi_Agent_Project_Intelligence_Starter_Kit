# Architecture and Layering

Last reviewed: YYYY-MM-DD

- Evidence scope: [Sub-projects and files sampled for this topic; how many; what was not sampled]
- Status: Consistent / Mostly consistent / Inconsistent / Not applicable / Not assessed
- Back to: [overview.md](overview.md)

How code is split into layers and modules, which way dependencies point, and where each kind of logic lives. Component-level architecture is in `architecture.md`; this page covers the code-level rules.

## Standard for this project
| Rule | Source (documented: path / inferred from dominant pattern) | Enforced by (formatter, linter rule, analyzer, CI, review, nothing) |
|---|---|---|
| [Rule] | [Verified: path / Inferred: N of M sampled files follow it] | |

## Checks
| Check | Result (Follows / Partly / Does not / Not applicable) | Evidence |
|---|---|---|
| Layers or modules are identifiable and named consistently | | |
| Dependencies point one way (for example UI/API → application → domain ← infrastructure); no reverse or circular references | | |
| Business logic lives in the domain/service layer, not in controllers, UI components, or data-access code | | |
| Data-access types (ORM entities, rows) do not leak into API responses or UI; DTOs/view models are used at boundaries | | |
| Dependency injection is used through a composition root; no service-locator or `new` of infrastructure inside business logic | | |
| Cross-cutting concerns (auth, validation, logging, caching) are applied consistently (middleware, filters, decorators) | | |
| Shared code lives in a shared module, not copied between sub-projects | | |

## How the code does it today
[Plain description of the current practice, with 2–3 good examples to copy (paths and symbols).]

## Deviations
| Where | What differs from the standard | Severity (High / Medium / Low) | Evidence |
|---|---|---|---|

## Recommended changes
| Change | Code or standard | Why | Effort (S / M / L) | Priority | Task |
|---|---|---|---|---|---|

Significant deviations also go to `review-findings.md` (as `RF-NNN`) or `tech-debt.md` (as `TD-NNN`), and actionable changes to `BACKLOG.md`.
