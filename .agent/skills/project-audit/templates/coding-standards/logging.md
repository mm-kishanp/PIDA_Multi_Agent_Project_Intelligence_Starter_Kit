# Logging

Last reviewed: YYYY-MM-DD

- Evidence scope: [Sub-projects and files sampled for this topic; how many; what was not sampled]
- Status: Consistent / Mostly consistent / Inconsistent / Not applicable / Not assessed
- Back to: [overview.md](overview.md)

How the code logs: framework, structure, levels, correlation, and sensitive data.

## Standard for this project
| Rule | Source (documented: path / inferred from dominant pattern) | Enforced by (formatter, linter rule, analyzer, CI, review, nothing) |
|---|---|---|
| [Rule] | [Verified: path / Inferred: N of M sampled files follow it] | |

## Checks
| Check | Result (Follows / Partly / Does not / Not applicable) | Evidence |
|---|---|---|
| One logging framework/abstraction is used throughout (no stray `print`/`console.log` in production code) | | |
| Logs are structured (named properties) rather than string-concatenated | | |
| Levels are used consistently (debug/info/warning/error); errors are logged once, with context and the exception | | |
| A correlation or trace ID flows through requests, jobs, and outbound calls | | |
| No sensitive data in logs: credentials, tokens, personal data, payment data (record locations only) | | |
| Log volume is reasonable on hot paths; no logging inside tight loops | | |
| Log configuration (levels, sinks) comes from configuration per environment | | |

## How the code does it today
[Plain description of the current practice, with 2–3 good examples to copy (paths and symbols).]

## Deviations
| Where | What differs from the standard | Severity (High / Medium / Low) | Evidence |
|---|---|---|---|

## Recommended changes
| Change | Code or standard | Why | Effort (S / M / L) | Priority | Task |
|---|---|---|---|---|---|

Significant deviations also go to `review-findings.md` (as `RF-NNN`) or `tech-debt.md` (as `TD-NNN`), and actionable changes to `BACKLOG.md`.
