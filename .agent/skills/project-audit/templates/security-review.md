# Security Review

Last reviewed: YYYY-MM-DD

Scope: [Areas inspected; areas not inspected]

This is an evidence-based repository review, not a penetration test or compliance certification.

## Security-sensitive surfaces
| Surface | Expected control | Implementation evidence | Status | Notes |
|---|---|---|---|---|
| Authentication | [Mechanism] | [Paths] | Verified / Inferred / Unknown | |
| Authorization | | | | |
| Tenant/data isolation | | | | |
| Input validation / injection | | | | |
| Secret management | [Where secrets live — names only] | | | |
| Sensitive data in logs | | | | |
| Dependencies / supply chain | [Lockfiles, CI scanning] | | | |
| Transport, CORS, headers | | | | |

## Findings
| ID | Severity | Finding | Evidence | Verified defect / Concern | Recommended action | Task |
|---|---|---|---|---|---|---|
| SEC-001 | Critical/High/Medium/Low | [Finding] | [path:line] | [Classification] | [Action] | [PIDA-xxx] |

## Not reviewed
- [Area — why]

Never record secret values, tokens, or private keys. Do not infer that a control exists without verifying its implementation and configuration.
