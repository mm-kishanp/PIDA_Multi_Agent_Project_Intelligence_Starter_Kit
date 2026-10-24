# Technical Debt

Last reviewed: YYYY-MM-DD

- Evidence scope: [Areas inspected; TODO/FIXME counts; Git hotspots used; what was not inspected]

## Summary
[3–5 sentences: where the debt concentrates, what it costs the team today (slower changes, bugs, outages, onboarding), and the few items worth paying down first.]

## Hotspots
| Area / path | Why it is a hotspot (change frequency, size, defects, TODO density) | Related debt | Evidence |
|---|---|---|---|

## Debt register
| ID | Area | Debt | Type | Evidence | Impact | Effort (S / M / L) | Priority | Status | Task |
|---|---|---|---|---|---|---|---|---|---|
| TD-001 | [Sub-project or module] | [What is wrong] | Design / Code / Test / Dependency / Infrastructure / Documentation / Security | [paths, counts, versions] | [What it costs, concretely] | | P0–P3 | Open / Planned / Paid down / Accepted | PIDA-NNN |

Types:
- **Design**: wrong boundaries, layering violations, tight coupling.
- **Code**: duplication, very large classes or functions, dead code, magic values.
- **Test**: missing tests on critical paths, flaky or slow suites.
- **Dependency**: outdated, unsupported, or vulnerable packages and runtimes (versions from manifests).
- **Infrastructure**: manual deployment steps, no rollback, unpinned images.
- **Documentation**: missing or wrong docs that slow people down.
- **Security**: weaknesses that are not yet exploitable findings (those go in `security-review.md`).

## Paid down
| ID | Date | How | Evidence |
|---|---|---|---|
