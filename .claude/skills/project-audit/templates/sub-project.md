# [Sub-project name]

Last reviewed: YYYY-MM-DD

- Type: Web app / API / Worker / Function / Library / CLI / Mobile app / Infrastructure
- Location: `[path]`
- Status: Active / Maintenance / Deprecated / Unknown
- Confidence: High / Medium / Low
- Part of: [project.md](../../project.md)

## What it is
[2–4 plain sentences: what this sub-project does, for whom or for which other sub-projects, and why it is separate.]

## Responsibilities
- [What it owns: business areas, data, jobs, screens]

## Features
| Feature | Role in this sub-project (owns / contributes / consumes) | Page |
|---|---|---|
| FEAT-NNN [Name] | [Role] | [../../features/FEAT-NNN-slug.md] |

## How it starts and runs
| Item | Value | Evidence |
|---|---|---|
| Entry point | [file / symbol] | |
| Runtime / framework | [name and version from manifest] | |
| Build | [command; Verified or Documented] | |
| Run locally | [command; Verified or Documented] | |
| Tests | [location, framework, command] | |
| Deployed as | [container, function, package, app store, not deployed] | |

## Dependencies
| Depends on | Kind (sub-project / package / data store / external system) | Why | Evidence |
|---|---|---|---|

**Used by:** [Sub-projects or external consumers that depend on this one.]

## Interfaces
- **Exposes:** [Routes, events, CLI commands, or public package API; link `api-catalog.md`]
- **Consumes:** [Other sub-projects' APIs, queues, integrations (`INT-NNN`)]

## Data
[Stores and main entities it reads or writes, tenant/ownership rules, sensitive fields; link `data-model.md`. `Not applicable — <evidence>` if it holds no data.]

## Configuration
[Variable and key names only, never values; where they are read; per-client configuration (link `client-matrix.md`).]

## Ownership and conventions
[CODEOWNERS entries, team, layering or naming conventions specific to this sub-project.]

## Risks and gaps
- [Missing tests, TODOs, deprecated dependencies, unclear behavior → PIDA-NNN / Q-NNN / R-NNN]
