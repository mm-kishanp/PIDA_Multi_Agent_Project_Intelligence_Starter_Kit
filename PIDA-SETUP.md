# PIDA setup and operating guide

## 1. Install

Copy/merge these files into the target repository. Preserve existing `CLAUDE.md`, `.claude/settings.json`, skills, hooks, and commands. If a target file already exists, merge the content manually or ask Claude Code to integrate without losing existing rules.

Start Claude Code at the repository root:
```bash
claude
```

Check installation if needed:
```bash
claude doctor
```

Official references:
- Claude Code setup: https://docs.anthropic.com/en/docs/claude-code/getting-started
- Claude Code memory / `CLAUDE.md`: https://docs.anthropic.com/en/docs/claude-code/memory
- Claude Code skills: https://docs.anthropic.com/en/docs/claude-code/skills
- CLI usage: https://docs.anthropic.com/en/docs/claude-code/cli-usage

## 2. First-run sequence

1. `/project-audit` — read-only discovery and evidence-based baseline.
2. Review `docs/project-intelligence/open-questions.md` and the audit report.
3. `/project-docs` — create/update the project knowledge base using verified findings.
4. `/project-plan <goal>` — create a backlog for the next feature or milestone.
5. `/project-implement <task ID>` — implement a specific task end-to-end.
6. `/project-review` — review the diff, tests, security, and documentation consistency.
7. `/project-status` — at the start of each later session, reconcile progress records with Git and get the next step.
8. `/project-refresh` — after significant changes or before a release, find and fix stale knowledge pages (`python scripts/doc-freshness.py` lists candidates).

In Claude Code, the audit, review, and implement workflows can delegate to the subagents in `.claude/agents/` (`pida-auditor`, `pida-reviewer`, `pida-test-runner`). They are limited to read and shell tools and instructed not to edit files; review their tool lists against your own permission policy.

Do not begin with a broad instruction like "rewrite everything". Start with audit and review the baseline.

## 3. Suggested team workflow

- At the start of a feature: audit relevant code, update requirements and backlog.
- During implementation: work on one coherent task or tightly related task group.
- Before completion: run relevant tests, inspect `git diff`, update docs and task status.
- At milestones/releases: refresh architecture, integrations, deployment, security and known limitations.
- After major dependency or architecture changes: re-run the audit for impacted areas.

## 4. Existing repository handling

If an equivalent document already exists, treat it as authoritative until checked. Link rather than duplicate. Preserve existing naming, folders, build system, and conventions. Do not relocate application files merely to match this template.

## 5. Permissions and autonomy

Claude Code permissions are configured separately from these instructions. Start with normal permission prompts and a narrow allowlist for safe read-only commands if desired. Do not enable broad write or shell permissions without evaluating the risk. Never use permission bypass flags to make the agent "fully autonomous."

## 6. Completion criteria

A project audit is complete only when its scope, evidence, exclusions, stack, architecture, feature status, test commands, gaps, and open questions are recorded. It is not proof that every line of a large repository was understood.

A task is complete only when acceptance criteria are met, relevant checks are run, docs are updated, and remaining risks are reported.


## Multi-agent support

See `MULTI-AGENT-SETUP.md` for shared instructions, platform adapters, skill synchronization, and capability differences. Do not assume hooks, permissions, subagents, slash commands, or all skill features are portable. Validate the native configuration with the actual tool and version.
