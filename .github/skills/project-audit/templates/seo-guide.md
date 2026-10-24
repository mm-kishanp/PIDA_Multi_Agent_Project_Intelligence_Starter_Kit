# SEO Guide

Last reviewed: YYYY-MM-DD

- Evidence scope: [Front-end sub-projects, page templates, routing, head/meta handling, static files inspected]
- Applicability: [Applies — public web pages that should be found in search engines / `Not applicable — <evidence>` (for example internal tool behind login, API only, mobile app, CLI)]

How well the project's public pages can be found and understood by search engines, and what to change. If the project has no public web pages, write `Not applicable — <evidence>` above and stop.

## Rendering
| Sub-project / site | Rendering (static, server-rendered, client-only SPA, hybrid) | Framework | Evidence |
|---|---|---|---|

Client-only rendering hides content from crawlers that do not run JavaScript; note it as a finding where it affects public pages.

## Checks
| Check | Result (Follows / Partly / Does not / Not applicable) | Evidence |
|---|---|---|
| Unique `<title>` and meta description per page, set from page content | | |
| Canonical URLs | | |
| `robots.txt` present and correct; non-production environments not indexable | | |
| `sitemap.xml` generated and kept current | | |
| Clean, stable, readable URLs; redirects for moved pages; real 404 status | | |
| One `<h1>` per page and a logical heading order | | |
| Images have meaningful `alt` text, sizes, and modern formats | | |
| Structured data (JSON-LD, schema.org) for the main content types | | |
| Open Graph and social card tags | | |
| Language and `hreflang` for multilingual sites | | |
| Performance: Core Web Vitals risks (large bundles, unoptimized images, layout shift, render-blocking resources) | | |
| Mobile-friendly, responsive layout | | |
| Internal linking and navigation crawlable (real links, not only script handlers) | | |

## Findings
| Where | Issue | Impact | Severity | Evidence |
|---|---|---|---|---|

## Recommended changes
| Change | Why | Effort | Priority | Task |
|---|---|---|---|---|

Ranking results and traffic are not visible from the code; record measured data only if the user provides it.
