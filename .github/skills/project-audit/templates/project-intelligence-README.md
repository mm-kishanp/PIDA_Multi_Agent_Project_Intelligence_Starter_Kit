# Project Intelligence

This directory is the evidence-based knowledge base maintained by PIDA.

## Rules
- Verify content against current code before relying on it.
- Label material findings `Verified`, `Inferred`, or `Unknown`.
- Include source paths and symbols/lines where practical.
- Record scan scope and exclusions.
- Do not store credentials, tokens, production data, or other secrets.
- Link to existing authoritative documentation rather than duplicating it.
- Refresh relevant pages after code, schema, dependency, API, or deployment changes. `python scripts/doc-freshness.py` lists pages with stale or placeholder review dates and cited paths that no longer exist.
- Blank templates for every page live in the templates folder of the `project-audit` skill (source: `.agents/skills/project-audit/templates/`).

## Suggested documents
- `project-overview.md`
- `repository-map.md`
- `feature-inventory.md`
- `requirements.md`
- `architecture.md`
- `data-model.md`
- `api-catalog.md`
- `integrations.md`
- `security-review.md`
- `quality-and-deployment.md`
- `open-questions.md`
- `analysis-log.md`
