---
name: testing
description: Discover this repository's real quality gates (test frameworks, commands, CI checks, coverage, lint and type checks), design risk-based tests, write tests that follow existing conventions, run them, and report exact results. Maintains the quality gates section of docs/project-intelligence/quality-and-deployment.md and test evidence in the feature inventory.
---

# Testing

Use when adding tests for a change or bug, assessing coverage of a feature or area, setting up the test plan for a task, or verifying a change.

## Shared PIDA resources

In the skills folder: `project-audit/reference/knowledge-base-guide.md`, `project-audit/reference/discovery-checklist.md` (sections 6–7), and `project-audit/templates/quality-and-deployment.md`.

## Before you start

1. Read `AGENTS.md` / `CLAUDE.md`, `repository-map.md`, `quality-and-deployment.md`, and `feature-inventory.md`.
2. If `quality-and-deployment.md` is missing or still a template, create it from the template and fill the quality gates section from the discovery in step 1 below.

## 1. Discover the quality gates

- Test frameworks and runners per project or package; test folder layout and naming; shared fixtures, factories, builders, mocks, and test databases or containers.
- Exact commands from CI first, then package scripts, Makefiles, or task runners. CI is the real gate.
- Coverage tooling and thresholds; lint, format, and type-check commands; pre-commit hooks.
- Environment needs: services, environment variable **names**, seed data. Never use production services or credentials.

Record each gate in `quality-and-deployment.md` with its command, where it is enforced, and whether you ran it.

## 2. Design tests by risk

Pick the cheapest test that proves the behavior:

| Test type | Use for |
|---|---|
| Unit | Pure logic, calculations, validation, mapping |
| Integration | Data access, queries, migrations, framework wiring, external clients with fakes |
| API / contract | Routes, status codes, auth, serialization, published contracts and events |
| UI / end to end | Critical user journeys only |
| Migration | Up/down, data preservation, backfills |
| Security | Authorization, tenant isolation, input validation |
| Performance | Only when there is a stated requirement or a known hotspot |

For each behavior cover the normal path, boundaries (empty, max, off-by-one), invalid input, failure of dependencies (timeouts, errors), authorization (unauthenticated, forbidden, other tenant), and concurrency or idempotency where relevant. For a bug, write a failing test that reproduces it first, then fix.

## 3. Write tests

- Follow the existing structure, naming, assertion style, and fixtures; put tests where similar tests live.
- Make tests deterministic: control time, randomness, ordering, and network; avoid sleeps; isolate data.
- Assert on behavior, not implementation details. One reason to fail per test where practical.
- No real secrets or production data in tests or fixtures.

## 4. Run and report

1. Run the focused tests first, then the broader relevant suite, then lint, type, and build checks if code changed. Where subagents are supported (Claude Code: `pida-test-runner`), you may delegate the runs.
2. For failures, determine whether they are caused by the change, pre-existing (check on the base commit if cheap), environmental, or flaky. Never delete, skip, or weaken a test to get a pass. Report flaky tests as risks.
3. A passing build is not proof of runtime behavior. Say what remains unverified.

## 5. Update records

- Feature rows and feature pages: list the tests that prove each feature and the gaps.
- `quality-and-deployment.md`: gates and the last result, with the date.
- `BACKLOG.md`: `Proposed` tasks for critical paths without tests. `RISKS.md`: flaky or missing gates.

## Report

Gates discovered; tests added or changed and what each proves; exact commands with Pass/Fail and counts; failures with assessment; what remains unverified.
