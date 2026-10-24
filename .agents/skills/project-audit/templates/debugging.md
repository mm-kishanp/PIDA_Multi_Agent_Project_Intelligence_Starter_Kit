# Debugging Guide

Last reviewed: YYYY-MM-DD

- Evidence scope: [IDE launch configs, compose files, README sections, logging config, scripts inspected; commands Verified (run) or Documented (read)]

How to run the project under a debugger, find what went wrong, and fix common problems. Commands use placeholders for every secret.

## Prerequisites
[Runtimes and versions, tools, local services (databases, queues, emulators), and how to start them (for example `docker compose up <services>`).]

## Debug each sub-project
| Sub-project | How to start in debug mode | IDE configuration | Ports / URLs | Evidence |
|---|---|---|---|---|
| [Name] | [Command or IDE profile] | [VS Code launch.json, launchSettings.json, JetBrains run configurations, none] | [Local URL] | |

## Attach to a running process or container
[How to attach the debugger to a running process, container, or emulator, if the project supports it. `Not applicable — <evidence>` otherwise.]

## Local configuration for debugging
[Variable names needed locally, example files (`.env.example`, `appsettings.Development.json`), feature flags to turn on, how to point at local services. Never real values.]

## Test data
[Seed scripts, fixtures, test accounts (described, never real credentials), how to reset local data.]

## Logs
- Where logs go locally:
- How to raise the log level:
- How to find one request's logs (correlation or trace ID):

## Debugging tests
[How to run one test or one file under the debugger for each test framework.]

## Background jobs, queues, and scheduled tasks
[How to trigger a job manually, inspect a queue locally, and step through a consumer.]

## Diagnosing deployed environments
[Read-only ways to investigate a problem outside local: log queries, traces, dashboards, health endpoints. Never change production data to debug.]

## Common problems
| Symptom | Likely cause | Fix | Evidence |
|---|---|---|---|

## Useful tools and commands
- [Tool or command — what it is for]
