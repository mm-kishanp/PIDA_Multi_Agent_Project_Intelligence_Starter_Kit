# Async and Await

Last reviewed: YYYY-MM-DD

- Evidence scope: [Sub-projects and files sampled for this topic; how many; what was not sampled]
- Status: Consistent / Mostly consistent / Inconsistent / Not applicable / Not assessed
- Back to: [overview.md](overview.md)

How asynchronous code is written: async all the way, cancellation, concurrency, and the absence of blocking calls. Write `Not applicable — <evidence>` when the languages in use have no async model.

## Standard for this project
| Rule | Source (documented: path / inferred from dominant pattern) | Enforced by (formatter, linter rule, analyzer, CI, review, nothing) |
|---|---|---|
| [Rule] | [Verified: path / Inferred: N of M sampled files follow it] | |

## Checks
| Check | Result (Follows / Partly / Does not / Not applicable) | Evidence |
|---|---|---|
| Async is used end to end on I/O paths (HTTP, database, file, queue); no sync-over-async (`.Result`, `.Wait()`, `GetAwaiter().GetResult()`, blocking futures) | | |
| No async-over-sync wrappers that only hide blocking work | | |
| Every promise/task is awaited or deliberately handled; no unobserved fire-and-forget; no `async void` outside event handlers | | |
| Cancellation tokens / abort signals are accepted and passed through long-running calls | | |
| Library code follows the platform's context guidance (for example `ConfigureAwait(false)` in .NET libraries) | | |
| Parallel work uses the right primitive (`Task.WhenAll`, `Promise.all`, `asyncio.gather`) with bounded concurrency | | |
| Timeouts are set on outbound calls; retries do not stack unboundedly | | |

## How the code does it today
[Plain description of the current practice, with 2–3 good examples to copy (paths and symbols).]

## Deviations
| Where | What differs from the standard | Severity (High / Medium / Low) | Evidence |
|---|---|---|---|

## Recommended changes
| Change | Code or standard | Why | Effort (S / M / L) | Priority | Task |
|---|---|---|---|---|---|

Significant deviations also go to `review-findings.md` (as `RF-NNN`) or `tech-debt.md` (as `TD-NNN`), and actionable changes to `BACKLOG.md`.
