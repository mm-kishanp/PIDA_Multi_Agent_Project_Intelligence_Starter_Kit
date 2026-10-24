---
name: security-review
description: Evidence-based security review of this repository or a change - authentication, authorization and IDOR, tenant isolation, injection, XSS, CSRF, SSRF, secrets handling, sensitive data in logs, dependencies and supply chain, configuration, and infrastructure permissions - with severity-rated findings. Maintains docs/project-intelligence/security-review.md and feeds risks and backlog tasks.
---

# Security review

Use for a whole-repository baseline, a focused area (such as auth or file upload), or the current diff. This is a code and configuration review, not a penetration test. Never attack real environments.

## Shared PIDA resources

In the skills folder: `project-audit/reference/knowledge-base-guide.md`, `project-audit/reference/discovery-checklist.md` (section 5), and `project-audit/templates/security-review.md`.

## Before you start

1. Read `AGENTS.md` / `CLAUDE.md`, any `SECURITY.md`, `project-overview.md`, `architecture.md` (trust boundaries), `api-catalog.md`, `data-model.md` (sensitive fields, tenancy), `integrations.md`, and `security-review.md`.
2. If `security-review.md` is missing or still a template, create it from the template. If the API catalog or data model is missing, enumerate entry points and sensitive data yourself for the scope under review.

## Method

Trace from **sources** (HTTP input, headers, cookies, files, messages, webhooks, environment) to **sinks** (database queries, shell commands, file paths, templates and HTML, outbound URLs, deserializers, logs, responses). For each control, verify its implementation and its configuration. Never assume a control exists because a library is installed.

## Checklist

| Area | Verify |
|---|---|
| Authentication | Scheme and provider; token validation (signature, issuer, audience, expiry); session and cookie flags; password and MFA handling; account recovery |
| Authorization | Every route and handler has an explicit policy; anonymous endpoints are intentional; object-level checks prevent IDOR; admin functions are protected |
| Tenant isolation | Tenant or ownership scope on every read, write, export, report, job, and cache key; no tenant ID trusted from client input without a check |
| Injection | Parameterized queries; no shell, eval, or template construction from input; path traversal in file operations; LDAP and NoSQL injection |
| Web | Output encoding and XSS; CSRF protection for cookie-authenticated state changes; CORS policy; security headers; open redirects |
| SSRF and outbound | User-influenced URLs restricted; webhook signature verification; TLS verification enabled |
| Files and deserialization | Upload type and size limits, storage location, scanning; unsafe deserialization or XML external entities |
| Secrets | No secrets in source, config, tests, docs, CI files, or Git history (report location only); secret-store usage; rotation |
| Sensitive data | Personal or financial data in logs, errors, analytics, or URLs; encryption at rest and in transit where required; retention and deletion |
| Crypto | No home-made crypto; modern algorithms; secure randomness for tokens |
| Dependencies and supply chain | Lockfiles committed; known-vulnerable or abandoned packages (use the ecosystem's audit tool if available offline or already configured); pinned CI actions and images; least-privilege CI tokens |
| Infrastructure and config | Debug modes off in production config; public storage or network exposure in IaC; overly broad IAM roles; default credentials |
| Rate limiting and abuse | Login, signup, password reset, and expensive endpoints |

## Severity

| Severity | Meaning |
|---|---|
| Critical | Exploitable without special access; leads to data breach, account takeover, cross-tenant access, or remote code execution |
| High | Exploitable with some preconditions, or a broken control on a sensitive path |
| Medium | Defense-in-depth gap or a vulnerability with limited impact |
| Low | Hardening or hygiene issue |

Classify each finding as a **verified defect** (the code path is demonstrated) or a **concern** (needs confirmation), and state the confidence.

## If you find a secret

Report the file and line, never the value. Recommend rotation and removal from history. Do not copy it into docs, tickets, or chat.

## Output

1. Update `security-review.md`: scope, surfaces table (every row with a status), findings (`SEC-NNN`, severity, evidence `path:line`, classification, recommended fix, linked task), and areas not reviewed.
2. Add `Proposed` fix tasks to `BACKLOG.md` (Critical and High as P0/P1) and risks to `RISKS.md`.
3. Report: scope, counts by severity, the top findings with failure scenarios, what was not reviewed, and recommended next actions. Fix issues only when asked and within scope.
