# Code Review Guide

Last reviewed: YYYY-MM-DD

- Evidence scope: [PR templates, CODEOWNERS, CI required checks, CONTRIBUTING, branch rules visible in the repository; what could not be seen (hosting settings)]

How changes are reviewed in this project and what a reviewer checks. `/project-review` and the `pida-reviewer` subagent use this page.

## How reviews work here
| Item | Current practice | Evidence |
|---|---|---|
| Pull request template | [Path or "none"] | |
| Code owners / required reviewers | [CODEOWNERS entries or "none found"] | |
| Required checks before merge | [CI jobs that gate merges] | |
| Branch protection and approvals | [Usually Unknown from the repository — ask] | |
| Branch and commit conventions | [Naming, conventional commits, squash/merge] | |
| Review tooling | [Bots, linters in PRs, coverage comments] | |

## Review checklist
Check every change against these, linking the standard it comes from:

- **Correctness**: acceptance criteria met; edge cases and error paths handled.
- **Architecture and layering**: logic in the right layer; dependency direction respected. [coding-standards/architecture-and-layering.md](coding-standards/architecture-and-layering.md)
- **Async**: no blocking calls; cancellation passed; nothing left unawaited. [coding-standards/async-await.md](coding-standards/async-await.md)
- **Structure and duplication**: no copy-paste; reuses existing helpers. [coding-standards/code-structure-and-duplication.md](coding-standards/code-structure-and-duplication.md)
- **Comments and docs**: public APIs documented; no commented-out code. [coding-standards/commenting-and-documentation.md](coding-standards/commenting-and-documentation.md)
- **Constants**: no magic values or hardcoded client/environment values. [coding-standards/constants-and-magic-values.md](coding-standards/constants-and-magic-values.md)
- **Errors and security**: validation, authorization, no leaked internals, no secrets. [coding-standards/error-handling-and-security.md](coding-standards/error-handling-and-security.md)
- **Logging**: structured, right level, no sensitive data. [coding-standards/logging.md](coding-standards/logging.md)
- **Naming and hygiene**: conventions, formatting, no warnings or debug code. [coding-standards/naming-and-code-hygiene.md](coding-standards/naming-and-code-hygiene.md)
- **Tests**: new behavior covered for normal, failure, boundary, and authorization cases; no test weakened.
- **Clients**: which clients the change reaches (`client-matrix.md`).
- **Docs**: feature pages, sub-project pages, API catalog, and data model updated.

## What blocks a merge
| Severity | Meaning | Blocks merge? |
|---|---|---|
| Critical | Security breach, data loss, or outage likely | Yes |
| High | Wrong main-flow behavior, broken compatibility, significant security weakness | Yes |
| Medium | Edge-case bug, missing important test, reliability or performance risk | Team decision |
| Low | Maintainability, minor convention, documentation | No; fix or log |

[Adjust to the team's actual rules if documented.]

## Recurring review themes
[Patterns that keep appearing in `review-findings.md`, and the standard or tooling change that would stop them.]
