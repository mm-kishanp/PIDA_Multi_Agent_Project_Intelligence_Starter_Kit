---
name: deployment
description: Analyze or change how this repository is built, configured, and delivered - CI/CD pipelines, environments, configuration and secrets references, containers, infrastructure as code, release and rollback, and observability - and produce release checklists. Maintains docs/project-intelligence/deployment.md (strategy and delivery) and the CI section of quality-and-deployment.md. Never deploys or changes shared infrastructure without approval.
---

# Deployment and delivery

Use to document the delivery path, change a pipeline, Dockerfile, or IaC, prepare a release, or plan a rollback.

## Shared PIDA resources

In the skills folder: `project-audit/reference/knowledge-base-guide.md`, `project-audit/reference/discovery-checklist.md` (sections 3 and 6), and `project-audit/templates/deployment.md` and `quality-and-deployment.md`.

## Before you start

1. Read `AGENTS.md` / `CLAUDE.md`, `project-overview.md`, `repository-map.md`, `deployment.md`, `quality-and-deployment.md`, `architecture.md`, and `security-review.md`.
2. If `deployment.md` or `quality-and-deployment.md` is missing or still a template, create it from the template and fill it from the evidence below.

## 1. Discover the delivery path

Find and cite:
- **CI/CD**: pipeline files, triggers (push, PR, tag, schedule, manual), jobs and stages, the exact build, test, lint, scan, package, and deploy commands, required checks, and approvals or environment protections;
- **Artifacts**: container images (Dockerfile base images, multi-stage builds, exposed ports, run user), packages, bundles; registries; versioning and tagging scheme;
- **Environments**: names (dev, test, staging, production), how each is deployed, and promotion between them;
- **Infrastructure as code**: tool, modules or stacks, state location (path only), the resources that matter (compute, data, networking, identity);
- **Configuration**: configuration sources per environment and required variable **names**; secret stores (Key Vault, Secrets Manager, Vault, CI secrets), recorded by name and location only;
- **Database migrations in delivery**: when and how they run;
- **Release and rollback**: tagging, changelog, feature flags, blue-green or canary, the rollback procedure and how data changes affect it;
- **Observability**: logging, metrics, tracing, health checks, alerts, dashboards.

Mark anything not verifiable from the repository (portal settings, manual steps) as Unknown and add it to `open-questions.md`.

## 2. Document

Fill `deployment.md`: the deployment strategy in plain words, a flow diagram, what is deployed per sub-project, environments and configuration names, pipelines, infrastructure, migrations, release, rollback, post-deploy verification, observability, manual steps, and recommended improvements. Keep local development, quality gates, and CI checks in `quality-and-deployment.md`. Record delivery debt (manual steps, no rollback, unpinned images) in `tech-debt.md`. Add delivery risks (manual steps, no rollback, unpinned images, secrets in pipeline files, missing gates) to `RISKS.md` and actionable fixes to `BACKLOG.md`.

## 3. Change pipelines, containers, or IaC

1. Follow the existing structure and conventions; change the smallest thing needed.
2. Validate locally where tools allow: YAML or schema lint, `docker build`, `terraform fmt` and `terraform validate`, `bicep build`, `helm lint`, or the platform's dry-run or `plan` against a non-production target. Report the commands and results.
3. Pin versions of actions, base images, and providers consistently with the repository's practice.
4. Keep secrets in the secret store; reference them by name; never echo them in logs.
5. Keep least privilege for pipeline identities and tokens.
6. Explain the effect on each environment and how to roll the change back.

## 4. Release checklist (when preparing a release)

- Scope: tasks `Done` since the last release, from `BACKLOG.md` and Git history.
- Quality gates green on the release commit, with evidence.
- Migrations reviewed for locks, backfill, and rollback; run order relative to the code deployment.
- Configuration and secret changes per environment.
- Feature flags and their default states.
- Rollback plan and trigger conditions.
- Post-deploy verification: health checks, smoke tests, metrics to watch.
- Release notes drafted from completed tasks and `DECISIONS.md`.

## Boundaries

Ask before deploying, triggering production pipelines, applying IaC to shared environments, changing permissions or secrets, publishing packages or images, pushing tags, or merging. Planning, linting, and local builds are fine.

## Report

What was found or changed, validation commands and results, environment impact, rollback, docs updated, risks, and the approvals needed.
