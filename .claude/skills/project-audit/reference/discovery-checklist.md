# Discovery checklist

Use this checklist to understand a repository from evidence. Every step is read-only. Commands are given for POSIX shells and PowerShell; use whichever the environment provides.

## 1. Preflight

| Goal | POSIX | PowerShell |
|---|---|---|
| Repository root | `git rev-parse --show-toplevel` | same |
| Working-tree state | `git status --short --branch` | same |
| Recent history | `git log --oneline -20` | same |
| Activity and authorship | `git log --since="6 months ago" --format="%ad %an" --date=short \| head` | `git log --since="6 months ago" --format="%ad %an" --date=short \| Select-Object -First 10` |
| Tracked file count | `git ls-files \| wc -l` | `(git ls-files).Count` |
| Files per top-level folder | `git ls-files \| cut -d/ -f1 \| sort \| uniq -c \| sort -rn` | `git ls-files \| % { ($_ -split '/')[0] } \| Group-Object \| Sort-Object Count -Descending` |
| Most changed areas (6 months) | `git log --since="6 months ago" --name-only --format= \| cut -d/ -f1-2 \| sort \| uniq -c \| sort -rn \| head -20` | `git log --since="6 months ago" --name-only --format= \| ? { $_ } \| % { ($_ -split '/')[0..1] -join '/' } \| Group-Object \| Sort-Object Count -Descending \| Select-Object -First 20` |
| Releases | `git tag --sort=-creatordate \| head` | `git tag --sort=-creatordate \| Select-Object -First 10` |

If the folder is not a Git repository, record that and list files while excluding the folders in section 8.

Also check whether PIDA files already exist and whether they are still templates: a page containing `YYYY-MM-DD` or bracketed placeholders such as `[Name]` has not been filled.

## 2. Read first

Read these when present, root first, then nested copies near the code you will touch:
- Agent instructions: `CLAUDE.md`, `AGENTS.md`, `.github/copilot-instructions.md`, `.github/instructions/`, `.cursor/rules/`, `.windsurfrules`, `.agent/rules/`.
- Project docs: `README*`, `CONTRIBUTING*`, `SECURITY*`, `CODEOWNERS`, `CHANGELOG*`, `LICENSE`, `docs/`, ADR folders (`docs/adr/`, `adr/`, `architecture/`), wiki exports.
- Conventions: `.editorconfig`, formatter and linter configs.

Extract the stated purpose, audience, domain terms, setup steps, and feature claims. Treat feature claims as hypotheses to verify, not facts.

## 3. Stack signals

| File | Indicates | Look next at |
|---|---|---|
| `package.json`, `package-lock.json`, `pnpm-lock.yaml`, `yarn.lock`, `bun.lockb` | Node.js / JavaScript / TypeScript; lockfile names the package manager | `scripts`, `workspaces`, `main`/`bin`, framework dependencies (Next.js, React, Vue, Angular, Svelte, Express, NestJS, Fastify), `tsconfig.json` |
| `*.sln`, `*.csproj`, `Directory.Build.props`, `global.json` | .NET | `Program.cs`, `Startup.cs`, `TargetFramework`, `PackageReference`, appsettings **key names** |
| `pyproject.toml`, `requirements*.txt`, `setup.py`, `Pipfile`, `poetry.lock`, `uv.lock` | Python | Django (`manage.py`, `settings.py`), FastAPI/Flask app objects, `console_scripts` |
| `go.mod`, `go.work` | Go | `cmd/*/main.go`, `internal/` |
| `Cargo.toml` | Rust | `src/main.rs`, `[[bin]]`, workspace members |
| `pom.xml`, `build.gradle(.kts)`, `settings.gradle` | JVM (Java/Kotlin) | `@SpringBootApplication`, `application.yml` key names |
| `Gemfile` | Ruby / Rails | `config/routes.rb`, `db/schema.rb`, `app/jobs` |
| `composer.json` | PHP / Laravel / Symfony | `routes/`, `database/migrations`, `config/` |
| `pubspec.yaml`, `Package.swift`, `*.xcodeproj`, Android `build.gradle` | Mobile | app entry, navigation, API client |
| `Dockerfile`, `compose.yaml`, `docker-compose*.yml` | Containers | base images, exposed ports, environment variable names, service list |
| `*.tf`, `*.bicep`, ARM JSON, `Pulumi.*`, `cdk.json`, `serverless.yml`, Kubernetes manifests, `Chart.yaml` | Infrastructure as code | resources, environments, secret references |
| `.github/workflows/`, `azure-pipelines.yml`, `.gitlab-ci.yml`, `Jenkinsfile`, `.circleci/`, `bitbucket-pipelines.yml` | CI/CD | exact build, test, lint, and deploy commands; triggers; environments |
| `nx.json`, `turbo.json`, `lerna.json`, `pnpm-workspace.yaml` | Monorepo | project list and dependency graph |

Record versions from manifests, not from memory.

## 4. Entry points and runtime units

- **Web / API**: route registrations and controllers (`app.get(`, `router.`, `@app.route`, `urls.py`, `routes.rb`, `[Http*]`, `@GetMapping`, `MapGet`), OpenAPI/Swagger files, GraphQL schemas, `.proto` files.
- **Frontend**: router configuration, `pages/` or `app/` directories, navigation menus, state stores, API client modules.
- **Workers and jobs**: hosted/background services, cron definitions, Celery/Sidekiq/Hangfire/BullMQ, queue consumers, Azure Functions, AWS Lambda handlers.
- **CLI**: `bin` entries, `console_scripts`, `cmd/` packages.
- **Composition root**: dependency-injection registration, middleware pipeline, configuration loading.

For each unit record: how it starts, configuration source, what it depends on, and how it is deployed.

## 5. Cross-cutting concerns (search hints)

| Concern | Search for |
|---|---|
| Authentication | `jwt`, `oauth`, `openid`, `passport`, `AddAuthentication`, `@login_required`, `session`, identity provider SDKs |
| Authorization | `Authorize`, `AllowAnonymous`, `policy`, `role`, `permission`, `can(`, `@PreAuthorize`, guards, middleware |
| Tenancy / ownership | `tenant`, `TenantId`, `organization_id`, `account_id`, `owner_id`, global query filters, row-level security |
| Persistence | ORM context/models (EF Core `DbContext`, `schema.prisma`, TypeORM, Sequelize, SQLAlchemy, Django models, ActiveRecord, Hibernate, GORM), migration folders, raw SQL |
| Client-specific behavior | see section 10 |
| Integrations | HTTP client factories, SDK imports (payments, email, SMS, storage, cloud), message brokers, webhook handlers |
| Configuration | `process.env`, `os.environ`, `IConfiguration`, `GetEnvironmentVariable`, `.env.example`, feature-flag SDKs |
| Errors and logging | global exception handlers, logger setup, OpenTelemetry/APM, log statements near sensitive data |
| Incomplete work | `TODO`, `FIXME`, `HACK`, `NotImplemented`, `throw new Error("not implemented")`, `pass  # TODO`, disabled flags |

## 6. Tests and quality gates

- Test locations and frameworks: Jest, Vitest, Mocha, Playwright, Cypress, pytest, unittest, xUnit, NUnit, MSTest, `go test`, `cargo test`, JUnit, RSpec, PHPUnit.
- Rough counts per area (number of test files), coverage configuration and thresholds.
- Lint/format/type tools: ESLint, Prettier, Ruff, Black, mypy, `dotnet format`, golangci-lint, Clippy, `tsc`.
- Pre-commit hooks: `.husky/`, `.pre-commit-config.yaml`, `lefthook.yml`.
- The CI file is the real quality gate: copy the exact commands it runs.

During an audit, record commands as **Documented** (read from config) unless you actually ran them.

## 7. Map test coverage to features

For each important feature, find tests that exercise its entry point. Absence of tests on a critical path (authentication, payments, data deletion, tenant access) is a finding for the backlog and risk register.

## 8. Exclusions

Do not read the contents of:
- dependency and build output: `node_modules/`, `vendor/`, `bin/`, `obj/`, `dist/`, `build/`, `out/`, `target/`, `.next/`, `.nuxt/`, `coverage/`, `__pycache__/`, `.venv/`, `venv/`, `.gradle/`;
- minified bundles, binaries, images, archives, large data files (sample a fixture only if needed);
- generated code (note it as generated, read its generator config instead).

Never open files likely to contain secret values: `.env` (`.env.example` and `.env.sample` are fine), `*.pem`, `*.key`, `*.pfx`, `id_rsa*`, `secrets.*`, environment-specific settings with connection strings, Terraform state. Derive variable **names** from example files and from code that reads configuration.

## 9. Size strategy

| Tracked files | Approach |
|---|---|
| Under ~500 | Single pass over all non-excluded areas. |
| ~500–5,000 | Phase by top-level area; log progress in `analysis-log.md` and `PROGRESS.md` after each area. |
| Over ~5,000 or monorepo | Audit area by area, in parallel subagents where supported; sample representative modules and state the sampling explicitly. |

## 10. Client-specific code

Find out whether the codebase serves several clients (customers, tenants, brands, partners, or deployments) with different behavior, and record it in `client-matrix.md`.

1. **Start from the user's list.** If the user named clients, search for each name, abbreviation, and likely code (case-insensitive, also in kebab, snake, and Pascal case). Every hit is a lead to a client-specific path.
2. **Search for the selection mechanism** — how the running code knows which client it is serving:

   | Mechanism | Search for |
   |---|---|
   | Client identifiers | `client`, `customer`, `tenant`, `brand`, `partner`, `org`, `ClientId`, `ClientCode`, `customerKey`, `tenantKey`, `X-Client`, `X-Tenant` |
   | Per-client folders and files | `clients/`, `customers/`, `tenants/`, `overrides/`, `custom/`, `brands/`, `themes/`, `whitelabel/`, file names containing a client name or code |
   | Per-client configuration | `appsettings.<Name>.json`, `config/<name>.*`, `.env.<name>.example`, Helm values or Terraform workspaces per client, tenant settings tables and seed data |
   | Feature flags and toggles | flag SDKs (LaunchDarkly, Unleash, Flagsmith, Azure App Configuration), `isEnabledFor`, `featureFor`, flags keyed by tenant or client |
   | Conditionals in code | `if (client ==`, `switch (tenant`, `case "<code>"`, comparisons against hardcoded IDs, GUIDs, or domains |
   | Build and deploy variants | build flavors, conditional-compilation symbols, separate pipelines, Dockerfiles, or app IDs per client |
   | Branding and content | per-client logos, CSS themes, translation or copy overrides, email templates |

3. **For each client**, record: its key in source; how it is selected at runtime (subdomain, header, login claim, environment variable, build flag, database row); the features it has Enabled, Disabled, or Customized; its client-only integrations and configuration key names; and the tests that exercise its path.
4. **Flag risks**: hardcoded client IDs in business logic, copy-pasted per-client variants of shared code, client branches without tests, and clients in the user's list with no trace in code (or the reverse).
5. Per-client values in configuration may be secrets. Record key names only.
