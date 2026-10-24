# Naming and Code Hygiene

Last reviewed: YYYY-MM-DD

- Evidence scope: [Sub-projects and files sampled for this topic; how many; what was not sampled]
- Status: Consistent / Mostly consistent / Inconsistent / Not applicable / Not assessed
- Back to: [overview.md](overview.md)

Naming conventions and day-to-day hygiene: formatting, warnings, unused code, and consistency with the domain glossary.

## Standard for this project
| Rule | Source (documented: path / inferred from dominant pattern) | Enforced by (formatter, linter rule, analyzer, CI, review, nothing) |
|---|---|---|
| [Rule] | [Verified: path / Inferred: N of M sampled files follow it] | |

## Checks
| Check | Result (Follows / Partly / Does not / Not applicable) | Evidence |
|---|---|---|
| Naming follows the language convention consistently (casing for types, members, files, constants) | | |
| Names are meaningful and use the domain terms in the glossary (`project-overview.md`), one term per concept | | |
| File names match the type or component they contain | | |
| A formatter is configured and the code is formatted with it | | |
| No unused imports, variables, parameters, or private members | | |
| Compiler/linter warnings are low; suppressions are rare and justified inline | | |
| No leftover debug code (temporary logging, debugger statements, test-only flags) | | |

## How the code does it today
[Plain description of the current practice, with 2–3 good examples to copy (paths and symbols).]

## Deviations
| Where | What differs from the standard | Severity (High / Medium / Low) | Evidence |
|---|---|---|---|

## Recommended changes
| Change | Code or standard | Why | Effort (S / M / L) | Priority | Task |
|---|---|---|---|---|---|

Significant deviations also go to `review-findings.md` (as `RF-NNN`) or `tech-debt.md` (as `TD-NNN`), and actionable changes to `BACKLOG.md`.
