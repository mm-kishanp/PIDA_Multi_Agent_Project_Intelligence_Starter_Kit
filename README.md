# Project Intelligence & Development Agent (PIDA)

A repository-local operating framework for Claude Code that analyzes an existing software project, builds evidence-based project knowledge, plans implementation work, implements scoped tasks, and keeps documentation current.

## Install into an existing repository

1. Back up or commit your current work.
2. Copy the contents of this package into the repository root. If `CLAUDE.md` or `.claude/` already exists, merge carefully; never overwrite existing project instructions blindly.
3. Start Claude Code from the repository root.
4. Run `/project-audit` first. It works out what the project is (purpose, users, features, stack, architecture, data, APIs, integrations, security surfaces, quality gates) and creates and fills every page in `docs/project-intelligence/` plus the four files in `project-management/`. Review its findings before asking for implementation. Every other skill also creates the pages it needs if they are missing.
5. Run `/project-plan <feature or goal>` to produce an actionable backlog.
6. Run `/project-implement <task ID>` to implement a specific task with tests and documentation updates.
7. Start later sessions with `/project-status`; run `/project-refresh` periodically to keep the knowledge base current.

## Included

- `CLAUDE.md`: core operating contract and workflow.
- `.claude/skills/`: specialist workflows and slash commands.
- `.claude/agents/`: read-only subagents (`pida-auditor`, `pida-reviewer`) and a `pida-test-runner` for parallel audits, independent reviews, and verification.
- `docs/project-intelligence/`: generated knowledge and templates (canonical copies in the `project-audit` skill's `templates/`).
- `project-management/`: backlog, decisions, risks, progress tracking.
- `scripts/`: optional helpers — `repo-inventory.sh` (read-only inventory), `doc-freshness.py` (read-only doc drift report), `sync-skills.py` (skill sync and `--check`).
- `.github/workflows/pida-checks.yml`: optional CI check that skill copies stay in sync.
- `PIDA-SETUP.md`: installation, first run, and maintenance guide.

## Safety and autonomy

The agent can autonomously read the repository, create or edit local documentation, implement scoped changes, and run appropriate local checks. It must ask first before destructive or irreversible actions, production changes, external communications, publishing, force pushes, deleting branches, dropping data, or modifying shared infrastructure. It must not use `--dangerously-skip-permissions` as a substitute for a safe setup.

## Compatibility

This package uses Claude Code's `CLAUDE.md` project instructions and `.claude/skills/<skill-name>/SKILL.md` skill layout. Confirm current syntax against the official documentation for your installed version. It does not require MCP servers or third-party integrations.


## Multi-agent support

PIDA now uses a shared `AGENTS.md` operating contract and portable Agent Skills, with native adapters for Claude Code, GitHub Copilot, Google Antigravity, and compatible tools. See `MULTI-AGENT-SETUP.md`. Tool discovery differs, so test each platform rather than assuming identical behavior.

- Shared instructions: `AGENTS.md`
- Portable skill source: `.agents/skills/`
- Claude Code adapter: `CLAUDE.md`, `.claude/skills/`
- Copilot adapter: `.github/copilot-instructions.md`, `.github/instructions/`, `.github/skills/`
- Antigravity adapter: `.agent/rules/`, `.agent/skills/`
- Skill sync helper: `python scripts/sync-skills.py`
