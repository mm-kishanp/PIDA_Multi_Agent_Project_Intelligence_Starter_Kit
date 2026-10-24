# Client Matrix

Last reviewed: YYYY-MM-DD

Scope: [Which code, configuration, and client lists were inspected; what was not.]

Use this page when the codebase serves more than one client (customer, tenant, brand, partner, or deployment) and behavior differs between them. If every client gets identical behavior, write `Not applicable — <evidence>` and stop.

## Client list sources
| Source | Type (user-provided / config / code / database seed / docs) | Date captured | Notes |
|---|---|---|---|
| [e.g. "User message"] | user-provided | YYYY-MM-DD | [Names as given] |

A client list given by the user is recorded as-is and labelled `Provided by user, <date>`. It is authoritative for *which clients exist*; behavior per client still needs code evidence.

## Clients
| ID | Client name | Code / key in source | Status (Active / Onboarding / Inactive / Unknown) | Environments / deployments | Source | Evidence |
|---|---|---|---|---|---|---|
| CLIENT-001 | [Name] | [`clientCode`, tenant ID name, folder name] | Unknown | [Where it runs] | [user-provided / code] | [paths] |

Record names and codes only. No contacts, contract terms, pricing, credentials, or customer data.

## How client-specific behavior is implemented
| Mechanism | Where | How a client is selected at runtime | Evidence |
|---|---|---|---|
| [Per-client config file, feature flag, tenant setting row, `if/switch` on client code, per-client folder/module, theme/branding, build variant, separate deployment, DB schema per client] | [path] | [header, subdomain, login claim, env var, build flag] | [path:line] |

## Client-specific code locations
| Location | Client(s) | What it changes | Classification | Evidence |
|---|---|---|---|---|
| [path or symbol] | CLIENT-001 | [Behavior difference] | Verified / Inferred / Unknown | [path:line] |

Flag hardcoded client names, IDs, or codes in business logic here; they are a common source of regressions.

## Feature availability by client
Rows are `FEAT-NNN` from `feature-inventory.md`. List only features whose availability or behavior differs between clients; note "all other features: same for every client" below the table if verified.

| Feature | CLIENT-001 | CLIENT-002 | Evidence / notes |
|---|---|---|---|
| FEAT-001 [Name] | Enabled / Disabled / Customized / Unknown | | [flag name, config key, path] |

- **Enabled**: standard behavior is reachable for this client.
- **Disabled**: switched off or unreachable for this client.
- **Customized**: client-specific variation; describe it in the next section.
- **Unknown**: no evidence either way.

## Customizations per client
### CLIENT-001 — [Name]
- **Customizations**: [What differs and where — paths, flags, config keys]
- **Integrations**: [`INT-NNN` used only or differently by this client]
- **Configuration**: [Variable/key names only, never values]
- **Tests**: [Tests that exercise this client's path, or "none found"]
- **Known issues / gaps**: [`PIDA-NNN`, `Q-NNN`, `R-NNN`]

## Risks and gaps
| Item | Clients affected | Evidence | Suggested action |
|---|---|---|---|
| [Untested client branch, hardcoded ID, divergent copy of shared code] | | | |
