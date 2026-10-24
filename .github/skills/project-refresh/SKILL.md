---
name: project-refresh
description: Detect and fix drift in docs/project-intelligence by finding pages that are stale, still templates, cite paths that no longer exist, or cover code changed since their review date, then re-verifying only those areas against the code. Creates missing pages. Use after significant changes, before a release, or on a regular cadence.
disable-model-invocation: true
---

# Project knowledge refresh

Targeted re-verification, not a full re-audit. Input: optional scope (pages, folders, or "since <date>"). Default: all of `docs/project-intelligence/`.

## Shared PIDA resources

In the skills folder: `project-audit/reference/knowledge-base-guide.md` (minimum standard per page and fill rules), `project-audit/reference/discovery-checklist.md`, and `project-audit/templates/`.

## Workflow

1. **Preflight**: confirm the repository root and Git status; preserve user changes. Read `AGENTS.md` / `CLAUDE.md` and `docs/project-intelligence/README.md`.
2. **Missing pages**: compare the folder with the file map in the guide. Create missing pages from the templates and add them to the candidate list. Include a feature page for every inventory row without one, and flag feature pages with no matching inventory row. Likewise compare the sub-projects in the code (new or removed manifests, solution entries, workspace packages) with `project.md` and `projects/`: create pages for new sub-projects and flag pages for ones that no longer exist. If most pages are missing, recommend `/project-audit` instead and stop unless the user wants a refresh anyway.
3. **Automated leads**: run `python scripts/doc-freshness.py` (`--max-age-days N` changes the 90-day default). It lists pages with a missing or placeholder `Last reviewed` date, pages older than the threshold, and cited paths that no longer exist, including pages under `features/`. Without Python, perform the same checks manually. Treat the output as leads.
4. **Change-based leads**: for each page, list code changed since its review date, for example `git log --since=<date> --name-only --format= -- <paths the page covers>`. Use `repository-map.md` to map paths to pages. Also check for new manifests, migrations, routes, CI files, dependencies, and client-specific folders, configuration, or flags (checklist section 10) since the last review.
5. **Prioritize**: broken references and security, data model, and API pages first, then the feature inventory and feature pages, then the rest. Always re-check open `RF-NNN` findings and `TD-NNN` debt items whose files changed, and re-review `deployment.md` when pipelines, Dockerfiles, or IaC changed, the `coding-standards/` pages when linter or formatter configs changed, and the SEO/AEO guides when public pages changed.
6. **Re-verify each candidate**:
   - re-read the cited source and check every material claim;
   - correct or remove stale claims, fix moved paths, and add what is new (routes, entities, integrations, features, tests);
   - re-classify Verified / Inferred / Unknown; never upgrade to Verified without fresh evidence;
   - update feature statuses using the feature status rules.
7. **Delegate** broad scopes to read-only subagents where supported (Claude Code: `pida-auditor`, one per area), then merge and spot-check.
8. **Dates**: update `Last reviewed` only on pages actually re-verified, and state partial scope on the page.
9. **Records**: append an `analysis-log.md` entry (trigger, pages checked, pages updated, pages still stale and why). Add new questions to `open-questions.md`, new risks to `project-management/RISKS.md`, and actionable gaps as `Proposed` tasks in `BACKLOG.md`.
10. **Check**: re-run the freshness script and the final checks in the guide.

## Report

Pages created, pages updated with a one-line summary of what changed, remaining drift and why, new questions, risks, and tasks, and the recommended next refresh trigger.
