# Commenting and Documentation

Last reviewed: YYYY-MM-DD

- Evidence scope: [Sub-projects and files sampled for this topic; how many; what was not sampled]
- Status: Consistent / Mostly consistent / Inconsistent / Not applicable / Not assessed
- Back to: [overview.md](overview.md)

How code is commented and documented: public API docs, comment quality, TODOs, and module-level READMEs.

## Standard for this project
| Rule | Source (documented: path / inferred from dominant pattern) | Enforced by (formatter, linter rule, analyzer, CI, review, nothing) |
|---|---|---|
| [Rule] | [Verified: path / Inferred: N of M sampled files follow it] | |

## Checks
| Check | Result (Follows / Partly / Does not / Not applicable) | Evidence |
|---|---|---|
| Public APIs (exported functions, public classes, endpoints) have doc comments in the language's standard form (XML docs, JSDoc/TSDoc, docstrings, KDoc, GoDoc) | | |
| Comments explain why, not what; no comments that restate the code | | |
| No commented-out code blocks | | |
| TODO/FIXME/HACK comments are rare, specific, and linked to a task (record the count) | | |
| Each sub-project or major module has a README covering purpose and how to run or use it | | |
| API documentation (OpenAPI, GraphQL schema docs) is generated or maintained alongside the code | | |

## How the code does it today
[Plain description of the current practice, with 2–3 good examples to copy (paths and symbols).]

## Deviations
| Where | What differs from the standard | Severity (High / Medium / Low) | Evidence |
|---|---|---|---|

## Recommended changes
| Change | Code or standard | Why | Effort (S / M / L) | Priority | Task |
|---|---|---|---|---|---|

Significant deviations also go to `review-findings.md` (as `RF-NNN`) or `tech-debt.md` (as `TD-NNN`), and actionable changes to `BACKLOG.md`.
