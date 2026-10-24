---
name: database-development
description: Safely analyze or change this repository's data layer - schema, entities and ORM models, migrations, queries, repositories, indexes, tenancy filters, sensitive data, and data lifecycle - using the project's own migration tooling, with zero-downtime patterns, rollback plans, and tests. Maintains docs/project-intelligence/data-model.md.
---

# Database development

Use when documenting the data model, adding or changing entities, writing migrations, fixing or optimizing queries, or assessing data risk. Database changes are a high-risk surface: be explicit about locks, backfills, rollback, and environments.

## Shared PIDA resources

In the skills folder: `project-audit/reference/knowledge-base-guide.md`, `project-audit/reference/discovery-checklist.md` (section 5, persistence), and `project-audit/templates/data-model.md`.

## Before you start

1. Read `AGENTS.md` / `CLAUDE.md`, `project-overview.md`, `repository-map.md`, `data-model.md`, `security-review.md`, and `quality-and-deployment.md`.
2. If `data-model.md` is missing or still a template, create it from the template and fill it, at least for the entities you touch.

## 1. Discover the data stack

Find and cite:
- data stores (relational, document, key-value, search, blob, cache) and their engine and version;
- access technology: ORM or query builder (EF Core, Prisma, TypeORM, Sequelize, SQLAlchemy, Django ORM, ActiveRecord, Hibernate/JPA, GORM, Dapper, raw SQL);
- schema source of truth: models, schema file, or SQL project;
- migration tool, folder, naming convention, latest migration, and how migrations run in CI and deployment (automatic at startup, pipeline step, or manual);
- conventions: key types, naming, soft delete, audit columns, timestamps and time zones, concurrency tokens;
- tenancy: tenant column, global query filters, row-level security, separate databases or schemas;
- sensitive fields: personal, financial, health, credentials, and any encryption or masking;
- seed data, test databases, and fixtures.

## 2. Document

In `data-model.md`, record stores, entities (key, relationships, sensitive fields, tenant or ownership rule, evidence), constraints and indexes, migration mechanism, retention and deletion behavior, and a Mermaid `erDiagram` when there are more than three entities.

## 3. Change the schema safely

1. Generate migrations with the project's tool and conventions. Do not hand-write migrations if the project generates them, and do not edit already-applied migrations.
2. Prefer zero-downtime, expand/contract patterns:
   - add new columns as nullable or with a default → backfill in batches → add constraints → switch reads and writes → remove the old column in a later release;
   - rename in steps (add, copy, switch, drop), not in place;
   - create indexes without blocking where the engine supports it (for example `CONCURRENTLY` or `ONLINE`), and assess table size and lock impact;
   - keep application code compatible with both the old and new schema during rollout.
3. Write a rollback (down migration or documented manual steps), and state what data a rollback would lose.
4. Plan large backfills as batched, resumable, idempotent jobs, not single transactions.
5. Update entities or models, repositories, seed data, and fixtures consistently.

## 4. Queries and data access

- Enforce tenant and ownership scope on every query path, including raw SQL, reports, exports, and background jobs.
- Use parameters; never build SQL from string concatenation of input.
- Watch for N+1 queries, unbounded result sets (add pagination or limits), missing indexes on filter, join, and sort columns, and long transactions.
- Use existing repository, unit-of-work, or query patterns rather than introducing new ones.

## 5. Test

Run migrations up (and down, where supported) against a local or disposable database only. Add repository or integration tests for new queries, constraints, tenant isolation, and concurrency, following the project's test database setup. Run the commands in `quality-and-deployment.md`.

## Boundaries

Never run migrations, data fixes, deletes, truncates, or schema drops against shared, staging, or production databases without explicit approval. Never copy production data into the repository, docs, tests, or logs. Never print connection strings.

## Report

Schema and query changes; migration name and rollback; lock and backfill assessment; tenant and sensitive-data impact; tests and commands run with results; `data-model.md` and other docs updated; deployment notes for operators.
