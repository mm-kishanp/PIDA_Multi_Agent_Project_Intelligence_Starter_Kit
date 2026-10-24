# Coding Standards: Overview

Last reviewed: YYYY-MM-DD

- Evidence scope: [Sub-projects, folders, and number of files sampled per topic; what was not sampled]
- Standard sources found: [`.editorconfig`, linter/analyzer configs, formatter config, CONTRIBUTING, style guides, ADRs; or "none: standards below are inferred from the dominant patterns in the code"]
- Enforcement found: [Formatter, linters, analyzers, pre-commit hooks, CI checks, required reviews; with paths]

This folder records how the code is written today, the standard the project should hold to, where the code deviates, and the changes recommended. Standards drawn from documented configuration are **Verified**; standards inferred from the dominant pattern in the code are **Inferred** until the team confirms them.

## How the code is implemented
[4–8 sentences on the overall implementation approach: architecture style, layering, dependency injection, data access pattern, error-handling and logging approach, async model, test style. Cite representative files. Details are in the topic pages.]

## Scorecard
| Topic | Status | Documented or inferred | Enforced by | Top issue | Page |
|---|---|---|---|---|---|
| Architecture and layering | Consistent / Mostly consistent / Inconsistent / Not applicable / Not assessed | | | | [architecture-and-layering.md](architecture-and-layering.md) |
| Async and await | | | | | [async-await.md](async-await.md) |
| Code structure and duplication | | | | | [code-structure-and-duplication.md](code-structure-and-duplication.md) |
| Commenting and documentation | | | | | [commenting-and-documentation.md](commenting-and-documentation.md) |
| Constants and magic values | | | | | [constants-and-magic-values.md](constants-and-magic-values.md) |
| Error handling and security | | | | | [error-handling-and-security.md](error-handling-and-security.md) |
| Logging | | | | | [logging.md](logging.md) |
| Naming and code hygiene | | | | | [naming-and-code-hygiene.md](naming-and-code-hygiene.md) |

## Top recommended changes
| # | Change | Topic | Why it matters | Effort | Priority | Task |
|---|---|---|---|---|---|---|
| 1 | [Change to the code, or to the standard itself] | | | S / M / L | P0–P3 | PIDA-NNN |

## Changes to the standards themselves
[Rules the team should adopt, document, or enforce: for example, add a formatter, turn on an analyzer rule, write down a convention that is followed but undocumented. These are proposals until the team accepts them; record accepted ones in `DECISIONS.md`.]

## Related
- Code review checklist: `code-review-guide.md`
- Findings from audits and reviews: `review-findings.md`
- Technical debt: `tech-debt.md`
