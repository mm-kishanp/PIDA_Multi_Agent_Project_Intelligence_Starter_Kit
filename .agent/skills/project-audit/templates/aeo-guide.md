# AEO Guide

Last reviewed: YYYY-MM-DD

- Evidence scope: [Front-end sub-projects, content templates, structured data, `robots.txt`, static files inspected]
- Applicability: [Applies — public content that should be cited by AI assistants and answer engines / `Not applicable — <evidence>`]

Answer Engine Optimization (AEO): how well AI assistants and answer engines (chat assistants, AI search, voice assistants) can find, understand, and cite the project's public content, and what to change. It builds on `seo-guide.md`. If the project has no public content, write `Not applicable — <evidence>` above and stop.

## AI crawler access
| Item | Current state | Evidence |
|---|---|---|
| `robots.txt` rules for AI crawlers (for example GPTBot, ClaudeBot, PerplexityBot, Google-Extended) | [Allowed / blocked / not mentioned] | |
| Content available without running JavaScript | | |
| `llms.txt` (a proposed convention for a plain-text site guide aimed at language models) | [Present / absent] | |

Whether to allow AI crawlers is a business decision. Record the current state and add a `Q-NNN` if the intent is unclear; never change it without the user's decision.

## Checks
| Check | Result (Follows / Partly / Does not / Not applicable) | Evidence |
|---|---|---|
| Structured data for answerable content (FAQPage, HowTo, Product, Article, Organization, BreadcrumbList) | | |
| Question-style headings with a direct, short answer right after them | | |
| Key facts (prices, specs, hours, policies) stated in plain text, not only in images or scripts | | |
| Clear entity information: organization name, logo, contact, consistent naming across pages | | |
| Authorship, published and updated dates on content pages | | |
| Content is current; stale pages are updated or removed | | |
| Sources and references cited where claims are made | | |
| Server-rendered or static HTML for public content | | |
| Accessible text alternatives for media (transcripts, captions, alt text) | | |

## Findings
| Where | Issue | Impact | Severity | Evidence |
|---|---|---|---|---|

## Recommended changes
| Change | Why | Effort | Priority | Task |
|---|---|---|---|---|

How often assistants cite the site is not visible from the code; record measured data only if the user provides it.
