---
name: pida-setup
description: Set up PIDA in the current repository after installing the PIDA plugin. Adds the always-on instructions (AGENTS.md, CLAUDE.md), the knowledge-base and project-management templates, and the doc helper scripts, and optionally the GitHub Copilot or Google Antigravity adapters, without overwriting existing files. Use once per repository, or when asked to "set up PIDA", "install PIDA here", or "add PIDA to this repo".
disable-model-invocation: true
---

# PIDA setup for this repository

The PIDA plugin gives you the skills (`/pida:project-audit`, `/pida:project-plan`, and the rest) and the subagents in every repository. A plugin cannot place files in a repository, so this skill adds the per-repository pieces:

- `AGENTS.md` and `CLAUDE.md`: the operating contract that loads in every session (evidence rules, safety boundaries, client tracking);
- `docs/project-intelligence/` and `project-management/`: blank templates the audit fills in;
- `scripts/doc-freshness.py` and `scripts/repo-inventory.sh`: read-only helpers the skills use when present.

The installer never overwrites an existing file.

## Steps

1. **Confirm the location.** Run `git rev-parse --show-toplevel` and `git status --short`. Work from the repository root. If the folder is not a Git repository, say so and ask before continuing. Note uncommitted changes; leave them alone.

2. **Choose adapters.** Default to Claude Code only. Add `copilot` or `antigravity` only if the user asked for them, or the repository already has `.github/copilot-instructions.md` or `.agent/` (then confirm with the user first).

3. **Preview.** Run the installer in dry-run mode (use `python3` or `py` if `python` is not found):

   ```bash
   python "${CLAUDE_PLUGIN_ROOT}/scripts/install-pida.py" --target . --tools claude --no-skills --dry-run
   ```

   Replace `claude` with a comma-separated list such as `claude,copilot` when step 2 added adapters. With Copilot or Antigravity, drop `--no-skills` so those tools get their skill copies too; Claude Code still uses the plugin's skills.

4. **Install.** Run the same command without `--dry-run`.

5. **Merge.** For each file reported as `merge` (it existed and differs), read both versions, `${CLAUDE_PLUGIN_ROOT}/<path>` and the repository's own, and merge PIDA's sections into the existing file without removing or weakening any existing rule. Show the user the resulting diff. Never replace their file wholesale.

6. **Without Python**, copy the same paths by hand from `${CLAUDE_PLUGIN_ROOT}`, skipping files that already exist: `AGENTS.md`, `CLAUDE.md`, `docs/project-intelligence/`, `project-management/`, `scripts/doc-freshness.py`, `scripts/repo-inventory.sh`.

7. **Report**: files created, files merged (with a one-line summary each), files left unchanged, and the next step:

   ```text
   /pida:project-audit
   ```

   Mention that the commands in `CLAUDE.md` and the README appear without the `pida:` prefix (`/project-audit`); with the plugin they run as `/pida:project-audit`. Suggest committing the new files so the whole team gets them.

## Rules

- Write only the files listed above and merges of files the installer reported. Do not modify application code.
- Do not commit, push, or change settings or permissions.
- Never copy secrets or environment files.
