# [Project name]

Last reviewed: YYYY-MM-DD

- Evidence scope: [What was inspected to write this page; what was not]
- Confidence: [High / Medium / Low]

This page explains the project in plain language for anyone joining it: developers, testers, product owners, and stakeholders. Technical details live in `project-overview.md` and the pages it links to.

## What it is
[3–5 plain sentences, no jargon: what the system does, for whom, and why it exists. Label Verified / Inferred and cite sources.]

## The problem it solves
[The need or pain point behind the project, and what users did before or would do without it. Usually Inferred; say why.]

## Who uses it
| User / role | What they want to achieve | Main workflows | Evidence |
|---|---|---|---|
| [Role] | [Goal] | [Workflow → FEAT-NNN] | [Auth config, routes, UI] |

## What it does
- [Capability in plain words — FEAT-NNN — Implemented / Partial / Planned]

## How people use it
[A short walk-through of one or two typical journeys, start to finish, in plain words. Link the features involved.]

## How it is organized
| Sub-project | What it is | Type (web app / API / worker / library / CLI / mobile / infrastructure) | Location | Page |
|---|---|---|---|---|
| [Name] | [One line] | [Type] | [path] | [projects/<slug>/project.md] |

[For a single-project repository write `Single project — <evidence>` instead of the table. Add a Mermaid diagram of how the sub-projects talk to each other when there are more than two.]

## Clients
[Who the project serves and whether behavior differs per client, in one or two sentences; details in `client-matrix.md`. `Not applicable — <evidence>` when there is one client.]

## Current state
[Plain-language summary of maturity: in production or not, how actively it changes, what is unfinished, and the biggest known risks (link R-NNN).]

## Where to go next
- Technical summary, stack, and how to run it: `project-overview.md`
- Where the code lives: `repository-map.md`
- Every feature and its status: `feature-inventory.md`
- Open questions: `open-questions.md`
