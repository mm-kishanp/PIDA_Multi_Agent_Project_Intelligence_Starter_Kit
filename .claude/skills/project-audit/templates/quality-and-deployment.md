# Quality and Deployment

Last reviewed: YYYY-MM-DD

Local setup and the quality gates that every change must pass. Delivery details live in `deployment.md`.

## Local development
| Step | Command | Verified? | Notes |
|---|---|---|---|
| Install | [Command] | Yes/No | [Prerequisites; placeholders for secrets] |
| Run | | | |

## Quality gates
| Gate | Command | Enforced where (local/CI/pre-commit) | Last result | Evidence |
|---|---|---|---|---|
| Unit tests | | | [Pass/Fail/Not run — date] | |
| Lint / format | | | | |
| Type check / build | | | | |
| Security / dependency scan | | | | |

## CI pipelines (quality checks)
| Pipeline | Trigger | Checks it runs | Blocks merge? | Evidence |
|---|---|---|---|---|

## Deployment and debugging
How the project is deployed (strategy, environments, release, rollback, observability) is in `deployment.md`. How to debug it is in `debugging.md`.

## Gaps
- [Missing gate, untested path, or manual step — impact]

Record a check result only when the command was actually run. Use placeholders for all secret values.
