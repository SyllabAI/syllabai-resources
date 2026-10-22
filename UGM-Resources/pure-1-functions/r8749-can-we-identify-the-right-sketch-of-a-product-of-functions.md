---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r8749
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r8749
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8749
  old_site_id: Q214
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-functions
    validation_status: SUGGESTED
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) 2007 Q['Q1G']
task: T-UGM-IMPORT-2
---

# Can we identify the right sketch of a product of functions?

## Question

On which of the axes below is a sketch of the graph \[y = 2^{-x} \sin^2 (x^2)?\]

| > [figure: Graph going up and down, never negative, with increasing frequency. Tends towards 0 as x tends to infinity. Starts at origin. — `https://undergroundmathematics.org/combining-functions/r8749/images/img-a.png`] (image not included in the text import; path of record). | > [figure: Graph going up and down, crossing the x axis often, with increasing frequency. Tends towards 0 as x tends to infinity. Starts at origin. — `https://undergroundmathematics.org/combining-functions/r8749/images/img-b.png`] (image not included in the text import; path of record). |
| --- | --- |
| > [figure: Graph going up and down, never negative, with constant frequency. Tends towards 0 as x tends to infinity. Starts at origin. — `https://undergroundmathematics.org/combining-functions/r8749/images/img-c.png`] (image not included in the text import; path of record). | > [figure: Graph going up and down, never negative, with increasing frequency. Tends towards 0 as x tends to infinity. Starts at (0,0.5). — `https://undergroundmathematics.org/combining-functions/r8749/images/img-d.png`] (image not included in the text import; path of record). |

## Suggestion

When are the functions \(2^{-x}\) and \(\sin^2 (x^2)\) positive, and when are they negative??

What is the \(y\) coordinate of the graph in the question when \(x=0\)?

When does the graph in the question meet the \(x\)-axis?

## Solution

- Both \(2^{-x}\) and \(\sin^2(x^2)\) are functions that are never negative, so \(y\geq0\), which discounts b.
- At \(x=0\), \(2^{-x} = 1\) and \(\sin^2 (x^2)=0\), so \(y(0)=0\), which discounts d.
- Finally, the graph meets the \(x\)-axis when \(\sin^2 (x^2) = 0\), which occurs when \(\sin (x^2)=0\), so at  \[x = \sqrt{\pi}, \sqrt{2\pi}, \sqrt{3\pi}, \ldots.\]  These are not evenly spaced as in c. These values get closer together as \(x\) increases, as in a.

Hence the answer is (a).
