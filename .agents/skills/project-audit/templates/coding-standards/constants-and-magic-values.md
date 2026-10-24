# Constants and Magic Values

Last reviewed: YYYY-MM-DD

- Evidence scope: [Sub-projects and files sampled for this topic; how many; what was not sampled]
- Status: Consistent / Mostly consistent / Inconsistent / Not applicable / Not assessed
- Back to: [overview.md](overview.md)

How literal values are handled: named constants, enums, configuration, and the absence of hardcoded environment- or client-specific values.

## Standard for this project
| Rule | Source (documented: path / inferred from dominant pattern) | Enforced by (formatter, linter rule, analyzer, CI, review, nothing) |
|---|---|---|
| [Rule] | [Verified: path / Inferred: N of M sampled files follow it] | |

## Checks
| Check | Result (Follows / Partly / Does not / Not applicable) | Evidence |
|---|---|---|
| No unexplained numeric or string literals in business logic; values are named constants or enums | | |
| Constants live in a predictable place (per module or a shared constants file), not redefined in several files | | |
| Environment-specific values (URLs, hostnames, ports, timeouts, limits) come from configuration, not code | | |
| No hardcoded client, tenant, or user IDs, codes, or names in business logic (cross-check `client-matrix.md`) | | |
| No credentials, keys, or connection strings in code (record locations only, never values) | | |
| Status values, roles, and types use enums or constants shared with the database and API contracts | | |

## How the code does it today
[Plain description of the current practice, with 2–3 good examples to copy (paths and symbols).]

## Deviations
| Where | What differs from the standard | Severity (High / Medium / Low) | Evidence |
|---|---|---|---|

## Recommended changes
| Change | Code or standard | Why | Effort (S / M / L) | Priority | Task |
|---|---|---|---|---|---|

Significant deviations also go to `review-findings.md` (as `RF-NNN`) or `tech-debt.md` (as `TD-NNN`), and actionable changes to `BACKLOG.md`.
