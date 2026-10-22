---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r5868
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r5868
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5868
  old_site_id: Q174
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
  exam_reference: Oxford (MAT) 2008 Q['Q1G']
task: T-UGM-IMPORT-2
---

# Can we identify the right sketch graph of this reciprocal function?

## Question

Which of the graphs below is a sketch of \[y = \frac{1}{4x-x^2-5}\; ?\]

| > [figure: Graph that tends to zero as x tends to plus or minus infinity, with a maximum at a positive x value, and y positive for all x. — `https://undergroundmathematics.org/combining-functions/r5868/images/diagrama.png`] (image not included in the text import; path of record). | > [figure: Graph that tends to zero as x tends to plus or minus infinity, with a maximum at a negative x value, and y positive for all x. — `https://undergroundmathematics.org/combining-functions/r5868/images/diagramb.png`] (image not included in the text import; path of record). |
| --- | --- |
| > [figure: Graph that tends to zero as x tends to plus or minus infinity, with a minimum at a positive x value, and y negative for all x. — `https://undergroundmathematics.org/combining-functions/r5868/images/diagramc.png`] (image not included in the text import; path of record). | > [figure: Graph that tends to zero as x tends to plus or minus infinity, with a minimum at a negative x value, and y negative for all x. — `https://undergroundmathematics.org/combining-functions/r5868/images/diagramd.png`] (image not included in the text import; path of record). |

## Suggestion

Would it help to complete the square for the quadratic expression in the denominator?

## Solution

We can complete the square. We have \(4x-x^2-5 = -(x^2-4x) -5 = -((x-2)^2-4)-5 = -(x-2)^2+4-5 = -(x-2)^2-1\).

So the graph is \[y = \frac{1}{-(x-2)^2-1},\] which shows the function is always negative, and has a minimum value of \(y=-1\) at \(x=2\).

Hence the correct graph is c.
