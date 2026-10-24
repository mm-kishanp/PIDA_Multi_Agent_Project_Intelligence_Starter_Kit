# Multi-agent setup

PIDA uses a shared core plus platform-native adapters. No repository can guarantee identical behavior across every agentic tool; instruction discovery, skill activation, subagents, hooks, permissions, and context limits differ by product and version.

## Shared source of truth
- `AGENTS.md`: tool-neutral repository operating contract.
- `.agents/skills/<skill>/SKILL.md`: portable skill source.
- `docs/project-intelligence/`: verified project knowledge.
- `project-management/`: task and progress state.

## Platform adapters included
- Claude Code: `CLAUDE.md` and `.claude/skills/`.
- GitHub Copilot: `.github/copilot-instructions.md`, `.github/instructions/`, `.github/skills/`.
- Google Antigravity: `.agent/rules/` and `.agent/skills/` adapter files.
- Codex and other compatible tools: `AGENTS.md` and `.agents/skills/` where supported.
- VS Code and other tools may support only a subset depending on harness, version, and configuration.

## How to install
1. Back up or commit current work.
2. Merge the package into the target repository; never blindly overwrite existing instructions, skills, or settings.
3. Keep `AGENTS.md` as the shared operating contract.
4. When modifying a shared skill, update `.agents/skills/<name>/SKILL.md` and sync copies to platform-specific skill directories that your team uses. This package initially duplicates skill files to maximize native discovery; use the included sync helper to keep them aligned.
5. Verify each platform's official current documentation and test skill discovery in that platform. Do not assume the presence of a file means the tool loaded it.
6. Run `/project-audit` in Claude Code or ask the active agent to "Run the PIDA project audit workflow from the relevant project skill."

## Safe synchronization
Use `python scripts/sync-skills.py` to copy the portable `.agents/skills/` skills, including supporting files such as templates, into `.claude/skills/`, `.github/skills/`, and `.agent/skills/`. It overwrites only files that exist in the source skill and never deletes; files present only in a native copy are reported and left alone. Review Git diff after running.

`python scripts/sync-skills.py --check` reports drift without writing and exits 1 if any copy is missing or differs. The optional `.github/workflows/pida-checks.yml` runs it on pull requests that touch skills.

## Capability differences
Shared instructions and skills travel well. The subagents in `.claude/agents/` are Claude Code only; the skills mention them as optional and fall back to sequential work elsewhere. Hooks, permissions, subagent definitions, slash commands, MCP setup, IDE integrations, and autonomous execution policies are platform-specific. Configure those natively and retain safe approval boundaries.
