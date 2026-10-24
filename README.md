# Project Intelligence & Development Agent (PIDA)

PIDA is a set of instructions, skills, and subagents you drop into an existing repository. It turns an AI coding agent (Claude Code, GitHub Copilot, Google Antigravity, Codex, and similar tools) into a disciplined project analyst and developer that:

1. **learns the project from the code**: what it does, for whom, its stack, architecture, data, APIs, integrations, security surfaces, tests, and clients;
2. **writes that knowledge down** in `docs/project-intelligence/`, with every claim labelled Verified, Inferred, or Unknown and linked to source paths;
3. **plans work** as a backlog of small tasks with acceptance criteria and test plans;
4. **implements tasks** following your conventions, with tests, verification, and documentation updates;
5. **keeps the knowledge current** and lets any later session pick up exactly where the last one stopped.

PIDA is plain Markdown skills plus a few standard-library Python and shell helpers. No server, no signup, no API key, nothing to connect. Install it as a Claude Code plugin, or let the installer copy it into your repository for any agent.

---

## Contents

- [Step 1: Install](#step-1-install)
- [Step 2: Quick start](#step-2-quick-start)
- [How it works](#how-it-works)
- [Commands](#commands)
- [Specialist skills](#specialist-skills)
- [Everyday workflows](#everyday-workflows)
- [Client-specific code and client lists](#client-specific-code-and-client-lists)
- [What PIDA writes](#what-pida-writes)
- [Using PIDA with other agents](#using-pida-with-other-agents)
- [Helper scripts](#helper-scripts)
- [Customizing PIDA](#customizing-pida)
- [Safety and autonomy](#safety-and-autonomy)
- [Troubleshooting](#troubleshooting)
- [Package layout](#package-layout)

---

## Step 1: Install

Commit or back up your work first, then pick one option. None of them overwrites a file you already have.

### Option A: ask Claude

Open Claude Code at the root of your repository and paste:

```text
https://github.com/mm-kishanp/PIDA_Multi_Agent_Project_Intelligence_Starter_Kit

install PIDA into this repository
```

Claude follows the [agent install steps](#agent-install-steps) below: it clones the kit to a temporary folder, runs the installer, merges any instruction files you already have, and cleans up. Add "for Copilot too" or "for Antigravity too" if your team uses those tools.

### Option B: Claude Code plugin

Installs the PIDA skills and subagents once, for every repository you open:

```text
/plugin marketplace add mm-kishanp/PIDA_Multi_Agent_Project_Intelligence_Starter_Kit
/plugin install pida@pida
```

Then, once in each repository, add the per-repository files (`AGENTS.md`, `CLAUDE.md`, and the knowledge-base templates):

```text
/pida:pida-setup
```

Claude Code namespaces plugin skills, so as a plugin the commands are `/pida:project-audit`, `/pida:project-plan`, and so on. Get new versions with `/plugin marketplace update pida`. If the repository is private, everyone who installs needs read access to it on GitHub.

### Option C: installer script

Works for every agent and needs only Python 3.8 or newer (nothing to pip install):

```bash
git clone https://github.com/mm-kishanp/PIDA_Multi_Agent_Project_Intelligence_Starter_Kit.git pida-kit
python pida-kit/scripts/install-pida.py --target /path/to/your-repo --tools claude
```

| `--tools` value | Adds | Always added (core) |
|---|---|---|
| `claude` (default) | `CLAUDE.md`, `.claude/skills/`, `.claude/agents/` | `AGENTS.md`, `.agents/skills/`, `docs/project-intelligence/`, `project-management/`, `scripts/` helpers |
| `copilot` | `.github/copilot-instructions.md`, `.github/instructions/`, `.github/skills/` | |
| `antigravity` | `.agent/rules/`, `.agent/skills/` | |
| `codex` | nothing extra (Codex reads `AGENTS.md` and `.agents/skills/`) | |
| `ci` | `.github/workflows/pida-checks.yml` (skill drift check) | |
| `all` | everything above | |

Combine them with commas (`--tools claude,copilot`). Add `--dry-run` to preview. A file that already exists is never overwritten; the installer lists it as `merge` so you can fold PIDA's content into yours by hand, or ask your agent: *"Merge the PIDA versions of these files into ours without losing any of our rules."*

### Option D: personal skills only

Plain `/project-audit` in every repository, with no files added to any repository:

```bash
git clone https://github.com/mm-kishanp/PIDA_Multi_Agent_Project_Intelligence_Starter_Kit.git pida-kit
cp -r pida-kit/.agents/skills/* ~/.claude/skills/
cp pida-kit/.claude/agents/*.md ~/.claude/agents/
```

The skills work on their own and create the knowledge base when you run them, but the always-on rules in `CLAUDE.md` and `AGENTS.md` are missing, so use A, B, or C for team repositories.

### After installing

1. **Check it loaded.** Start the agent at the repository root (`claude` for Claude Code) and type `/project-` (or `/pida:` with the plugin). The seven PIDA commands should be listed. Restart the session if they are not.
2. **Commit the PIDA files** so teammates get them on their next pull.

### Agent install steps

For an AI agent asked to "install PIDA" from a link to this repository:

1. Confirm you are at the root of the user's repository (`git rev-parse --show-toplevel`) and note uncommitted changes. Do not install into this kit itself.
2. Clone the kit to a temporary directory outside the repository: `git clone --depth 1 https://github.com/mm-kishanp/PIDA_Multi_Agent_Project_Intelligence_Starter_Kit.git <tmp>/pida-kit`.
3. Choose `--tools`: `claude` by default; add `copilot` or `antigravity` only if the user asked, or confirm first if the repository already has `.github/copilot-instructions.md` or `.agent/`.
4. Preview with `python <tmp>/pida-kit/scripts/install-pida.py --target . --tools <tools> --dry-run`, then run it without `--dry-run`. Use `python3` or `py` if `python` is not found.
5. For every file reported as `merge`, merge the kit's version into the user's file without removing or weakening any existing rule, and show the diff.
6. Delete the temporary clone. Do not commit or push.
7. Report what was created and merged, and suggest `/project-audit` as the next step.

Detailed setup notes: [PIDA-SETUP.md](PIDA-SETUP.md). Multi-tool notes: [MULTI-AGENT-SETUP.md](MULTI-AGENT-SETUP.md).

---

## Step 2: Quick start

```text
/project-audit
```

Takes a few minutes to much longer depending on repository size. When it finishes:

1. Read the audit report and `docs/project-intelligence/open-questions.md`, and answer the questions only you can answer.
2. Read `project.md` (and the `projects/` pages if your repository has several apps or services) and skim `feature-inventory.md` to confirm PIDA understood the project.
3. Plan your next piece of work:

   ```text
   /project-plan add CSV export to the monthly report
   ```

4. Implement the first task it proposes:

   ```text
   /project-implement PIDA-001
   ```

5. Review before opening a pull request:

   ```text
   /project-review PIDA-001
   ```

6. In every later session, start with:

   ```text
   /project-status
   ```

Do not start with a broad instruction such as "rewrite everything". Audit first, review the baseline, then work task by task.

---

## How it works

```text
            ┌────────────────────┐
            │  /project-audit    │  learn the repo, write the knowledge base
            └─────────┬──────────┘
                      ▼
 docs/project-intelligence/   ◄── read by every later command
 project-management/          ◄── backlog, risks, decisions, progress
                      │
     ┌────────────────┼──────────────────┬─────────────────┐
     ▼                ▼                  ▼                 ▼
/project-plan   /project-implement  /project-review   /project-status
 goal → tasks    task → code+tests   diff → findings   where are we?
                      │
                      ▼
               /project-refresh   keep the docs in step with the code
```

Three ideas run through everything:

- **Evidence over claims.** A README, ticket, or TODO is a lead, not proof. A feature is `Implemented` only when its code path is traced and tested.
- **Knowledge lives in the repo.** The agent's understanding is saved as reviewable Markdown next to the code, so it survives across sessions, people, and tools.
- **Safe autonomy.** Routine local work proceeds without prompts. Destructive, shared, or external actions always need your approval.

---

## Commands

These workflows run only when you invoke them. In Claude Code they are slash commands (with the `pida:` prefix when installed as a plugin: `/pida:project-audit`). In other tools, ask by name, for example *"Run the PIDA project-plan workflow for: add CSV export."*

| Command | Use it when | Input | Main output |
|---|---|---|---|
| `/project-audit` | First time in a repo, or the docs are badly stale | Optional scope (`only the billing service`) and client list | Every page in `docs/project-intelligence/`, a seeded backlog, risks, decisions |
| `/project-docs` | Document a feature or area, or fill pages still marked Unknown | Scope (`the billing feature`, `api-catalog`) | Updated knowledge pages |
| `/project-plan` | Before any non-trivial change | A goal, bug, or milestone | Requirements plus `PIDA-NNN` tasks in `BACKLOG.md` |
| `/project-implement` | Build one task end to end | Task ID (`PIDA-012`) or a specific change | Code, tests, verification results, updated docs and status |
| `/project-review` | Before marking Done or opening a PR | Optional task ID, branch, or commit range | Severity-ranked findings and acceptance-criteria check |
| `/project-status` | Start of a session or after a break | — | Where things stand, mismatches, the exact next step |
| `/project-refresh` | After big changes, before a release, or on a schedule | Optional pages, folders, or `since <date>` | Stale pages re-verified and updated |

---

## Specialist skills

The agent uses these automatically when a request matches, and you can also ask for them directly (in Claude Code: `/security-review`, `/testing`, and so on).

| Skill | Covers | Maintains |
|---|---|---|
| `api-development` | REST, GraphQL, gRPC, webhooks, events: validation, auth, errors, versioning, contract tests | `api-catalog.md` |
| `architecture` | Current architecture, or designing a change with options, trade-offs, and an ADR | `architecture.md`, `integrations.md`, `DECISIONS.md` |
| `database-development` | Schema, migrations, queries, indexes, tenancy, sensitive data, rollback plans | `data-model.md` |
| `deployment` | CI/CD, environments, config and secret references, containers, IaC, release and rollback | `quality-and-deployment.md` |
| `security-review` | Authn/authz, IDOR, tenant isolation, injection, XSS/CSRF/SSRF, secrets, dependencies | `security-review.md` |
| `testing` | Real quality gates, risk-based test design, writing and running tests | quality gates and test evidence |

In Claude Code, three subagents help in the background: `pida-auditor` audits areas of large repos in parallel, `pida-reviewer` gives an independent review of a diff, and `pida-test-runner` runs your project's checks and reports exact results. None of them edits files.

---

## Everyday workflows

**Fix a bug**

```text
/project-plan fix: invoices are duplicated when the payment webhook retries
/project-implement PIDA-014
/project-review PIDA-014
```

**Small, well-defined change (no planning needed)**

```text
/project-implement add a "last login" column to the admin users table
```

PIDA creates a lightweight task record for it automatically.

**Understand an area before touching it**

```text
/project-docs the notifications module
```

**Security pass before a release**

```text
Run a security review of the authentication and payment flows.
/project-refresh
```

**Resume interrupted work**

```text
/project-status
continue with the next step
```

**Audit only part of a large repository**

```text
/project-audit only services/billing and services/invoicing
```

Other areas are marked `Not inspected` so nobody mistakes the result for a full audit.

---

## Client-specific code and client lists

If your codebase serves several clients (customers, tenants, brands, or partners) and behavior differs between them, PIDA tracks that in `docs/project-intelligence/client-matrix.md`:

- every client and its key in the code;
- how the running code works out which client it is serving (subdomain, header, login claim, config, build flag);
- where client-specific code, configuration, and feature flags live;
- a **feature × client matrix**: Enabled, Disabled, or Customized for each client.

**Give PIDA your client list whenever you have one.** It is saved in the same session, even outside an audit:

```text
/project-audit Our clients are Acme (code ACM), Globex (GLX) and Initech (INI).
Acme and Globex use SSO; Initech uses password login. Only Globex has the export feature.
```

Facts you state are recorded as `Inferred (user-stated)` until PIDA finds the code that confirms them. Clients you named that aren't in the code, and clients in the code that you didn't name, go into `open-questions.md`. When implementing, PIDA works out which clients a change reaches, keeps other clients' behavior unchanged when a task targets one client, and reports "clients affected" at the end.

PIDA stores client **names, codes, and behavior only**, never contacts, contract terms, pricing, credentials, or customer data. If client names are confidential, say so and it will use the codes from the source instead.

---

## What PIDA writes

```text
docs/project-intelligence/
  README.md                  index and scope of the knowledge base
  project.md                 plain-language explanation of the project: start here
  projects/<name>/project.md one page per sub-project (app, service, library, worker), when there are several
  project-overview.md        technical summary: glossary, stack, runtime components, how to run it
  repository-map.md          where everything lives
  feature-inventory.md       every capability: status, clients, evidence, tests
  requirements.md            goals, roles, functional and non-functional requirements
  architecture.md            components, key flows (Mermaid), trust boundaries, debt
  data-model.md              stores, entities, relationships, migrations
  api-catalog.md             endpoints, events, contracts, auth
  integrations.md            external systems
  client-matrix.md           clients and what works for which client
  security-review.md         security surfaces and findings
  quality-and-deployment.md  local setup, quality gates, CI checks
  deployment.md              deployment strategy and how it is deployed: environments, pipelines, release, rollback
  debugging.md               how to debug each part of the project, logs, test data, common problems
  coding-standards/          how the code follows its standards and what to change, one page per topic:
    overview.md                scorecard, how the code is implemented, top recommended changes
    architecture-and-layering.md, async-await.md, code-structure-and-duplication.md,
    commenting-and-documentation.md, constants-and-magic-values.md,
    error-handling-and-security.md, logging.md, naming-and-code-hygiene.md
  code-review-guide.md       how reviews work here and the review checklist
  review-findings.md         RF-NNN findings from audits and reviews, with status
  tech-debt.md               TD-NNN technical debt register and hotspots
  seo-guide.md               search-engine readiness of public pages (or Not applicable)
  aeo-guide.md               readiness for AI assistants and answer engines (or Not applicable)
  open-questions.md          unknowns that need an answer
  analysis-log.md            history of audits and refreshes
  features/FEAT-NNN-*.md     one page per feature: behavior, entry points, data, clients, tests, gaps
project-management/
  BACKLOG.md                 PIDA-NNN tasks with acceptance criteria and test plans
  RISKS.md                   R-NNN risks with likelihood, impact, mitigation
  DECISIONS.md               ADR-NNN decisions, including pre-existing choices
  PROGRESS.md                current goal, work done, checks run, exact next step
```

How to read it:

- **Verified** means backed by a cited file, test, or config. **Inferred** gives a reason and a confidence level. **Unknown** says what was checked and how to find out.
- Feature status is one of `Implemented`, `Partial`, `Planned`, `Deprecated`, or `Unknown`.
- Task status is one of `Proposed`, `Ready`, `In Progress`, `Blocked`, `In Review`, `Done`, or `Deferred`. `Done` requires passing verification.
- IDs are stable and never reused: `FEAT`, `FR`/`NFR`, `CLIENT`, `INT`, `RF` (review findings), `TD` (tech debt), `SEC`, `Q`, `R`, `ADR`, `PIDA`.
- Every `/project-audit` creates or re-reviews all of these pages, including the coding standards, deployment, debugging, and SEO/AEO guides, and re-checks open findings and debt.

Commit these files. They are meant to be reviewed in pull requests like code. If your repository already has equivalents (an `ARCHITECTURE.md`, ADR folder, OpenAPI spec, or issue tracker), PIDA links to them instead of duplicating them.

The pages shipped in this kit are blank templates (dates show `YYYY-MM-DD`). The audit fills them in.

---

## Using PIDA with other agents

| Tool | Reads | How to run a workflow |
|---|---|---|
| Claude Code | `CLAUDE.md`, `.claude/skills/`, `.claude/agents/` | Slash commands: `/project-audit` |
| GitHub Copilot | `.github/copilot-instructions.md`, `.github/instructions/`, `.github/skills/` | *"Run the PIDA project-audit skill."* |
| Google Antigravity | `.agent/rules/`, `.agent/skills/` | *"Run the PIDA project-audit skill."* |
| Codex and other `AGENTS.md` tools | `AGENTS.md`, `.agents/skills/` | *"Follow .agents/skills/project-audit/SKILL.md."* |

Every tool shares the same knowledge base and backlog, so you can audit with one tool and implement with another. Subagents, hooks, slash commands, and permission settings are tool-specific. Without subagents, the skills fall back to working sequentially. Test skill discovery in each tool rather than assuming it loaded.

---

## Helper scripts

All optional and read-only unless noted.

| Command | What it does |
|---|---|
| `bash scripts/repo-inventory.sh` | Prints Git status, top-level entries, and manifest paths. Never reads file contents. |
| `python scripts/doc-freshness.py` | Lists knowledge pages with missing or placeholder review dates, pages older than 90 days (`--max-age-days N`), and cited paths that no longer exist. `--strict` exits 1 on issues. |
| `python scripts/install-pida.py --target <repo>` | **Writes to the target.** Installs PIDA without overwriting existing files. See [Option C](#option-c-installer-script). Lives in the kit only; it is not copied into your repository. |
| `python scripts/sync-skills.py` | **Writes.** Copies `.agents/skills/` into whichever of `.claude/skills/`, `.github/skills/`, and `.agent/skills/` exist. Never deletes. |
| `python scripts/sync-skills.py --check` | Reports drift between skill copies and exits 1 if any. Used by the optional CI workflow. |
| `python -m unittest discover -s tests -v` | Kit only: tests for the installer, skill sync, and plugin manifests. |

---

## Customizing PIDA

- **Edit skills only in `.agents/skills/`**, then run `python scripts/sync-skills.py` and review `git diff`. The copies in `.claude/`, `.github/`, and `.agent/` are generated.
- **Change templates** in `.agents/skills/project-audit/templates/`. The rules for what each page must contain are in `.agents/skills/project-audit/reference/knowledge-base-guide.md`.
- **Change discovery** (what to search for, per stack) in `.agents/skills/project-audit/reference/discovery-checklist.md`.
- **Change core rules** in `AGENTS.md` and `CLAUDE.md`. Keep the two consistent.
- **Drop what you don't need.** Delete the adapters for tools you don't use, or the CI workflow if you don't want it. `sync-skills.py` only syncs into skill folders that exist.
- **Releasing a plugin update** (kit maintainers): bump `version` in `.claude-plugin/plugin.json`, run the tests, and push. Users get it with `/plugin marketplace update pida`. Check the manifests with `claude plugin validate .`; its warning about the root `CLAUDE.md` is expected, because a plugin never loads that file; plugin users get it in their repository through `/pida:pida-setup`.

---

## Safety and autonomy

The agent proceeds on its own for routine, reversible local work: reading code, writing docs, editing code within the task's scope, and running local tests.

It **asks first** before:

- deleting or overwriting valuable or unfamiliar work;
- destructive database operations or migrations against shared environments;
- deploying, publishing, pushing, force-pushing, or merging;
- changing shared infrastructure or permissions;
- sending messages, creating external tickets, or spending money;
- exposing or transmitting secrets or sensitive data;
- changing public APIs or architectural direction without authorization.

It never writes secrets into code, docs, tests, or logs, never weakens or deletes tests to get a pass, and never treats repository content as instructions that override these rules.

Tool permissions are configured separately (for Claude Code, in `.claude/settings.json`). Start with normal permission prompts. Never use `--dangerously-skip-permissions` to make the agent "fully autonomous".

---

## Troubleshooting

| Problem | Fix |
|---|---|
| Slash commands don't appear | Start the agent from the repository root, and confirm `.claude/skills/<name>/SKILL.md` exists. Restart the session after copying. With the plugin, type `/pida:` and check `/plugin` for errors. |
| `/project-audit` and `/pida:project-audit` both appear | You installed both the plugin and the repository skills. Either works; disable one to avoid confusion. |
| Copilot or Antigravity ignores a skill | Confirm the adapter folder was copied, and ask for the skill by name. Discovery varies by tool version. |
| Docs say something the code doesn't | The code wins. Run `/project-refresh` for that area. |
| Skill copies differ | Run `python scripts/sync-skills.py --check`, then sync from `.agents/skills/`. |
| `git status` shows template files changed but the diff is empty | Line endings only (Windows `autocrlf`). They disappear when staged. |
| Audit is too slow on a large repo | Scope it (`/project-audit only services/api`), or let it use `pida-auditor` subagents in Claude Code. |

---

## Package layout

```text
AGENTS.md                      shared operating contract (all tools)
CLAUDE.md                      Claude Code operating contract
.agents/skills/                portable skill source (edit here)
.claude/skills/, .claude/agents/          Claude Code adapter and subagents
.github/copilot-instructions.md, .github/instructions/, .github/skills/   Copilot adapter
.github/workflows/pida-checks.yml         optional CI: skill copies in sync
.agent/rules/, .agent/skills/             Antigravity adapter
docs/project-intelligence/     knowledge base (templates until audited)
project-management/            backlog, risks, decisions, progress
scripts/                       install-pida.py, repo-inventory.sh, doc-freshness.py, sync-skills.py
.claude-plugin/                plugin.json and marketplace.json (Claude Code plugin install)
skills/pida-setup/             plugin-only skill: /pida:pida-setup
tests/                         tests for the installer, sync, and manifests
PIDA-SETUP.md                  setup and operating guide
MULTI-AGENT-SETUP.md           multi-tool notes
.gitignore.pida-example        optional ignore entries for local scratch files
```

PIDA follows the `CLAUDE.md` and `.claude/skills/<name>/SKILL.md` conventions of Claude Code. Check the current syntax against the official documentation for your installed version.
