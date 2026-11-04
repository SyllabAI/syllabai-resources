---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-functions/two-way-functions
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-functions
- type/many-ways-problem
- level/developing
resource_identity:
  ugm_id: two-way-functions
  station: thinking-about-functions
  station_title: Thinking about Functions
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 9796
  old_site_id: F1_RT6_1
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: thinking-about-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-functions
    validation_status: SUGGESTED
  spec_points:
  - code: E2.11.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: The asymptote half of the property work — E2.11.3 register.
      rationale: 'Canonical UGM title: “Two-way functions”'
      validation_status: SUGGESTED
  - code: E2.13.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: The asymptote half of the property work — E2.11.3 register.
      rationale: 'Canonical UGM title: “Two-way functions”'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-19
---

# Two-way functions

> Excerpt: This resource gives students an opportunity to explore their understanding of roots and asymptotes of functions, both by identifying properties that functions have in common and also by seeking functions that have particular properties. For detailed notes on this resource, please see [Two-way functions - teacher support](/thinking-about-functions/two-way-functions-teacher-support).

## Problem

Each column and row heading in the following table is a property that a function may or may not have. A function can appear in a cell if it has the properties in the corresponding row and column.

We have omitted some headings, and some entries in cells. Can you complete the table?

You might find it helpful to draw some sketches. You could use graph-sketching software such as [Desmos](https://www.desmos.com/calculator) to help you, but try to do the sketching by hand first, before reaching for a computer or calculator!

Make sure that you can explain why each function has the desired properties.

|  | \(y\)-axis is an asymptote |  |  | Passes through origin |
| --- | --- | --- | --- | --- |
| \(x = 1\) is a root |  | \(y = \vert x-1\vert\) | \(y = -3x+3\) |  |
| Has exactly two roots |  | \(y = x(x-2)\) |  |  |
|  | \(y = \dfrac{1}{x}\) \(\text{for }x \neq 0\) | \(y = \dfrac{1}{(x-1)^2}\) \(\text{for }x \neq 1\) | \(y = \dfrac{3}{x+1}\) \(\text{for }x \neq -1\) |  |
| \(y \to \infty\) as \(x \to \infty\) |  |  | \(y = 2+(x-1)^4\) |  |

- Can you complete the table using a different function in every cell?
- How few different functions can you use in the table?
- Did you have any choice about the column and row headings?

## Suggestion

Here are some functions that might (or might not) prove helpful when trying to complete the table. You could sketch each to see whether it has properties that you find useful. The functions are also available on [cards to cut out](https://undergroundmathematics.org/thinking-about-functions/two-way-functions/components/cards.pdf).

\(y = (x-1)^2\)

\(y = x(1-x)\)

\(y = \dfrac{1}{\vert x \vert}\) for \(x \neq 0\)

\(y = 1 + \dfrac{1}{x}\) for \(x \neq 0\)

\(y = (x-1)^2 (x+3)\)

\(y = \dfrac{x-1}{x}\) for \(x \neq 0\)

\(y = x^3\)

\(y = \dfrac{x}{(x-1)^2}\) for \(x \neq 1\)

\(y = -1 + \dfrac{1}{x^2}\) for \(x \neq 0\)

\(y = \vert x \vert\)

\(y = x(x+7)\)

\(y = \dfrac{3}{x^2}\) for \(x \neq 0\)

\(y = x + \dfrac{1}{x}\) for \(x \neq 0\)

\(y = x^2 + 3\)

\(y = x\)

\(y = \dfrac{1}{x^3}\) for \(x \neq 0\)

## Solution

Here is one possible way to complete the table.

|  | \(y\)-axis is an asymptote | Is symmetrical about \(x = 1\) | Intersects \(y\)-axis at \(3\) | Passes through origin |
| --- | --- | --- | --- | --- |
| \(x = 1\) is a root | \(y = \dfrac{x-1}{x}\) for \(x \neq 0\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph1proj.png`] (image not included in the text import; path of record). | \(y = \vert x - 1 \vert\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph5proj.png`] (image not included in the text import; path of record). | \(y = -3x + 3\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph9proj.png`] (image not included in the text import; path of record). | \(y = x(1-x)\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph13proj.png`] (image not included in the text import; path of record). |
| Has exactly two roots. | \(y = -1 + \dfrac{1}{x^2}\) for \(x \neq 0\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph2proj.png`] (image not included in the text import; path of record). | \(y = x(x-2)\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph6proj.png`] (image not included in the text import; path of record). | \(y = (x-1)^2 (x+3)\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph10proj.png`] (image not included in the text import; path of record). | \(y = x(x+7)\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph14proj.png`] (image not included in the text import; path of record). |
| \(x\)-axis is an asymptote | \(y = \dfrac{1}{x}\) for \(x \neq 0\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph3proj.png`] (image not included in the text import; path of record). | \(y = \dfrac{1}{(x-1)^2}\) for \(x \neq 1\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph7proj.png`] (image not included in the text import; path of record). | \(y = \dfrac{3}{x+1}\) for \(x \neq -1\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph11proj.png`] (image not included in the text import; path of record). | \(y = \dfrac{x}{(x-1)^2}\) for \(x \neq 1\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph15proj.png`] (image not included in the text import; path of record). |
| \(y \to \infty\) as \(x \to \infty\) | \(y = x + \dfrac{1}{x}\) for \(x \neq 0\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph4proj.png`] (image not included in the text import; path of record). | \(y = (x-1)^2\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph8proj.png`] (image not included in the text import; path of record). | \(y = 2 + (x-1)^4\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph12proj.png`] (image not included in the text import; path of record). | \(y = x\) > [figure: — `https://undergroundmathematics.org/thinking-about-functions/two-way-functions/images/graph16proj.png`] (image not included in the text import; path of record). |
