# Integrations

Last reviewed: YYYY-MM-DD

| ID | External system | Direction | Protocol/SDK | Purpose | Auth method | Config names (no values) | Failure handling | Evidence |
|---|---|---|---|---|---|---|---|---|
| INT-001 | [Service] | Inbound/Outbound | [HTTP/SDK/queue/webhook] | [Purpose] | [OAuth/API key/managed identity] | [ENV_VAR_NAME] | [Timeout/retry/circuit breaker/Unknown] | [Paths] |

For each integration, document as applicable: timeouts, retries and idempotency, rate limits, webhook signature verification, sandbox vs production endpoints, data shared and its sensitivity, contract tests or mocks, and owner if documented.

Record secret *names and locations* only. Never record values, tokens, or connection strings.
