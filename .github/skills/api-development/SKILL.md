---
name: api-development
description: Design, implement, document, or analyze this repository's APIs and messaging contracts - REST/HTTP routes, GraphQL, gRPC, webhooks, and event producers/consumers - covering routing, validation, authentication, authorization, error format, versioning, compatibility, and contract tests, and keeping docs/project-intelligence/api-catalog.md current.
---

# API development

Use when adding or changing an endpoint, event, or webhook, when documenting the existing API surface, or when assessing a contract change.

## Shared PIDA resources

In the skills folder: `project-audit/reference/knowledge-base-guide.md`, `project-audit/reference/discovery-checklist.md` (section 4 for route discovery), and `project-audit/templates/api-catalog.md` and `integrations.md`.

## Before you start

1. Read `AGENTS.md` / `CLAUDE.md`, `project-overview.md`, `repository-map.md`, `api-catalog.md`, and `security-review.md` in `docs/project-intelligence/`.
2. If `api-catalog.md` is missing or still a template, create it from the template and fill it for the area you touch, or for the whole API when documenting. Create `docs/project-intelligence/` if needed.

## 1. Learn the project's API conventions

Find and cite the existing patterns before writing anything:
- **Style and framework**: REST, GraphQL, gRPC, server actions, or message-based; the framework and its routing mechanism.
- **Contract source of truth**: code-first (annotations, decorators) or spec-first (OpenAPI, GraphQL SDL, `.proto`, AsyncAPI). Note where generated clients come from.
- **Routing and naming**: URL shapes, pluralization, casing, versioning (path, header, or none).
- **Validation**: library or attributes used, and where validation runs.
- **Auth**: the authentication scheme, how endpoints declare authorization (attributes, policies, guards, middleware), anonymous endpoints, and how tenant or ownership scoping is applied.
- **Errors**: response shape (for example RFC 7807 problem details or a custom envelope), status-code conventions, and the global exception handler.
- **Pagination, filtering, sorting**, idempotency keys, rate limiting, caching headers, and CORS.
- **Events**: broker, topic naming, payload schema and versioning, delivery guarantees, retries, dead-letter handling, consumer idempotency.
- **Tests**: how API, integration, or contract tests are written, and the fixtures and helpers they use.

## 2. Design a change

For each endpoint or event, define:
- purpose and the calling client(s);
- method and route, or topic, and operation name;
- request schema with validation rules, and response schema with status codes for success, validation failure (400/422), unauthenticated (401), forbidden (403), not found (404), conflict (409), and server error;
- required permission and tenant or ownership rule;
- side effects (writes, events, emails, external calls) and idempotency;
- pagination and limits for collections;
- compatibility impact.

**Compatibility rules.** Adding optional fields, new endpoints, or new event types is normally safe. Removing or renaming fields or routes, changing types or meaning, tightening validation, or changing auth requirements are breaking. They need explicit user approval, a versioning or deprecation plan, and a `DECISIONS.md` entry.

## 3. Implement

1. Follow the existing layering (controller/handler → service → data access) and the patterns found in section 1.
2. Validate input at the boundary, and enforce authorization and tenant scope on every data access, not only at the route.
3. Return the project's standard error shape. Never leak stack traces, internal identifiers, or secrets.
4. Update the spec file or regenerate clients if the project is spec-first or ships clients.
5. Log and trace using existing conventions, without logging sensitive payloads.

## 4. Test

Cover the success path, validation failures, unauthenticated and forbidden access, cross-tenant access attempts, not found, conflicts, and idempotent retries. Add contract or schema tests where the project has them. For events, test serialization, consumer idempotency, and failure or retry handling. Run the tests with the commands in `quality-and-deployment.md`.

## 5. Document

- Update `api-catalog.md`: one row per endpoint or event with method, route or topic, purpose, auth, request and response contract, side effects, and evidence. Group large APIs by resource with counts, and detail the critical endpoints.
- Update `integrations.md` for webhooks or external consumers, `feature-inventory.md` for user-visible capability, and `security-review.md` if the auth surface changed.
- Record breaking-change decisions in `DECISIONS.md`.

## Report

Endpoints or events added or changed; compatibility assessment; tests and commands run with results; docs updated; open questions.
