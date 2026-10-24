# Error Handling and Security

Last reviewed: YYYY-MM-DD

- Evidence scope: [Sub-projects and files sampled for this topic; how many; what was not sampled]
- Status: Consistent / Mostly consistent / Inconsistent / Not applicable / Not assessed
- Back to: [overview.md](overview.md)

How errors are raised, handled, and returned, and the secure-coding practices visible in the code. Security findings at system level are in `security-review.md`; this page covers coding practice.

## Standard for this project
| Rule | Source (documented: path / inferred from dominant pattern) | Enforced by (formatter, linter rule, analyzer, CI, review, nothing) |
|---|---|---|
| [Rule] | [Verified: path / Inferred: N of M sampled files follow it] | |

## Checks
| Check | Result (Follows / Partly / Does not / Not applicable) | Evidence |
|---|---|---|
| A global error handler or middleware turns unhandled errors into a consistent response | | |
| Exceptions are not swallowed (empty catch, catch-and-ignore, catch-all returning success) | | |
| Errors returned to callers do not leak stack traces, SQL, internal paths, or secrets | | |
| Expected failures use the project's error pattern (result types, typed exceptions, error codes) consistently | | |
| Input is validated at every boundary (API, message consumer, file import) with one validation approach | | |
| Queries are parameterized; no string-built SQL, shell commands, or file paths from user input | | |
| Authorization is checked in code paths that access data, including ownership and tenant checks | | |
| Secrets come from the secret store or configuration, never from code | | |

## How the code does it today
[Plain description of the current practice, with 2–3 good examples to copy (paths and symbols).]

## Deviations
| Where | What differs from the standard | Severity (High / Medium / Low) | Evidence |
|---|---|---|---|

## Recommended changes
| Change | Code or standard | Why | Effort (S / M / L) | Priority | Task |
|---|---|---|---|---|---|

Significant deviations also go to `review-findings.md` (as `RF-NNN`) or `tech-debt.md` (as `TD-NNN`), and actionable changes to `BACKLOG.md`.
