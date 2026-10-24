# Code Structure and Duplication

Last reviewed: YYYY-MM-DD

- Evidence scope: [Sub-projects and files sampled for this topic; how many; what was not sampled]
- Status: Consistent / Mostly consistent / Inconsistent / Not applicable / Not assessed
- Back to: [overview.md](overview.md)

How files, classes, and functions are organized and sized, and how much logic is duplicated.

## Standard for this project
| Rule | Source (documented: path / inferred from dominant pattern) | Enforced by (formatter, linter rule, analyzer, CI, review, nothing) |
|---|---|---|
| [Rule] | [Verified: path / Inferred: N of M sampled files follow it] | |

## Checks
| Check | Result (Follows / Partly / Does not / Not applicable) | Evidence |
|---|---|---|
| Folder and file layout follows one convention per sub-project (by feature or by layer) and matches `repository-map.md` | | |
| Classes and functions have a single clear responsibility; no very large files or functions on hot paths (note the largest) | | |
| No copy-pasted logic across files, sub-projects, or per-client variants; shared helpers are reused | | |
| No dead code: unused classes, functions, endpoints, feature-flagged-off paths with no removal plan | | |
| Deep nesting and long parameter lists are rare; complex conditionals are extracted and named | | |
| Tests mirror the source structure | | |

## How the code does it today
[Plain description of the current practice, with 2–3 good examples to copy (paths and symbols).]

## Deviations
| Where | What differs from the standard | Severity (High / Medium / Low) | Evidence |
|---|---|---|---|

## Recommended changes
| Change | Code or standard | Why | Effort (S / M / L) | Priority | Task |
|---|---|---|---|---|---|

Significant deviations also go to `review-findings.md` (as `RF-NNN`) or `tech-debt.md` (as `TD-NNN`), and actionable changes to `BACKLOG.md`.
