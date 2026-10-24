---
name: architecture
description: Document this repository's current architecture (components, dependencies, runtime flows, data and trust boundaries, deployment units, integrations) or design an architectural change with options, trade-offs, and an ADR, using the actual technology stack. Maintains docs/project-intelligence/architecture.md, integrations.md, and project-management/DECISIONS.md.
---

# Architecture

Two modes:
- **Current state**: explain how the system is built today.
- **Change design**: propose how to build something new or restructure something existing.

Ask which mode applies if the request is unclear, or do current state first, since every proposal starts from it.

## Shared PIDA resources

In the skills folder: `project-audit/reference/knowledge-base-guide.md`, `project-audit/reference/discovery-checklist.md` (sections 3–5), and `project-audit/templates/architecture.md`, `integrations.md`, and `project-management/DECISIONS.md`.

## Before you start

1. Read `AGENTS.md` / `CLAUDE.md`, `project-overview.md`, `repository-map.md`, `architecture.md`, `integrations.md`, `data-model.md`, and `DECISIONS.md`, plus any existing ADR folder.
2. If they are missing or still templates, create them from the templates. Fill `repository-map.md` and the stack section of `project-overview.md` first, using the discovery checklist.

## Current-state mode

1. **Runtime units**: every deployable or runnable unit (web app, API, worker, function, job, CLI, mobile app), its entry point, and how it is deployed.
2. **Components and boundaries**: modules or projects, their responsibilities, and dependency direction. Use project references, imports, and DI registrations as evidence. Flag cycles and layer violations.
3. **Key flows**: trace 2–5 important flows end to end (entry → validation → authorization → logic → persistence → side effects → response) and draw each as a Mermaid `sequenceDiagram` or `flowchart`. Mark inferred edges as inferred.
4. **System context**: a Mermaid `flowchart` with users, the system's runtime units, data stores, and external systems.
5. **Data and trust boundaries**: where authentication happens, where authorization and tenant scope are enforced, what crosses the network, and where secrets come from.
6. **Cross-cutting concerns**: configuration, error handling, logging and telemetry, caching, background processing, feature flags.
7. **Constraints and debt**: compatibility, performance, regulatory, and operational constraints; technical debt with evidence, impact, and suggested action, recorded in `tech-debt.md` as `TD-NNN` (debt items worth doing become `Proposed` backlog tasks). Code-level layering rules belong in `coding-standards/architecture-and-layering.md`.
8. **Decisions**: link existing ADRs. Record major pre-existing choices as `Accepted (pre-existing, inferred from code)` in `DECISIONS.md`.
9. Write `architecture.md` and `integrations.md` following the guide's standard.

## Change-design mode

1. State the problem, goals, non-goals, and constraints: functional need, scale, latency, consistency, security, cost, team skills, deadlines.
2. Describe the current state of the affected area, with evidence.
3. Generate 2–3 viable options. Always include the smallest change that fits existing patterns.
4. Compare them on fit with existing architecture, complexity, risk, performance, security, operability, cost, migration effort, and reversibility.
5. Recommend one option, and give the migration path (incremental steps, expand/contract for data, feature flags), the rollback plan, and validation (tests, metrics).
6. Record an ADR in `DECISIONS.md` with status `Proposed`: context, decision, alternatives, consequences, evidence, revisit trigger. New services, new infrastructure, new major dependencies, or public contract changes need user approval before moving to `Accepted`.
7. Hand off implementation as backlog tasks (see the project-plan skill).

## Rules

- Discover the stack; never assume .NET, Node, AWS, Azure, React, or any other technology.
- Prefer the smallest change consistent with established patterns; avoid speculative abstractions, new layers, or new services without a concrete need.
- Separate current state from proposals clearly in every document.
- Diagrams must match the code; a diagram of an imagined system is worse than none.

## Report

Mode; key findings or the recommendation; diagrams added; decisions recorded and their status; risks; follow-up tasks.
