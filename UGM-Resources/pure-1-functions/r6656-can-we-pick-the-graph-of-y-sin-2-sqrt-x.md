---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r6656
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r6656
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6656
  old_site_id: null
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
  exam_reference: Oxford (MAT) 2010 Q['Q1D']
task: T-UGM-IMPORT-2
---

# Can we pick the graph of $y=\sin^2{\sqrt{x}}$?

## Question

The graph of \(y=\sin^2{\sqrt{x}}\) is drawn in

| > [figure: Function oscillating between positive and negative with constant amplitude, frequency. — `https://undergroundmathematics.org/combining-functions/r6656/images/img-6656a.png`] (image not included in the text import; path of record). | > [figure: Positive function, starting at 0, increasing quickly to a maximum, then curving back down to 0, and increasing again to the same maximum, this time more slowly. — `https://undergroundmathematics.org/combining-functions/r6656/images/img-6656b.png`] (image not included in the text import; path of record). |
| --- | --- |
| > [figure: Positive function, increasing to a maximum, then going back to 0, then increasing again to a larger maximum, then down again. — `https://undergroundmathematics.org/combining-functions/r6656/images/img-6656c.png`] (image not included in the text import; path of record). | > [figure: Positive function oscillating with constant amplitude, frequency. — `https://undergroundmathematics.org/combining-functions/r6656/images/img-6656d.png`] (image not included in the text import; path of record). |

## Solution

The function \(y=\sin^2{\sqrt{x}}\) is positive for any positive \(x\), so it cannot be (a).

The local maximum of \(y=\sin^2{\sqrt{x}}\) is \(1\) for \(\sqrt{x} = \left(\dfrac{\pi}{2}\right), \left(\dfrac{3\pi}{2}\right), \left(\dfrac{5\pi}{2}\right) ...\), so it cannot be (c) as its first two local maxima are of different values.

And the frequency of our function is not constant, as it is in the case of \(\sin x\). We can see this by looking at the \(x\) values of the first few maxima: \[x = \dfrac{\pi^2}{4}, \dfrac{9\pi^2}{4}, \dfrac{25\pi^2}{4}...\]

These are not equally separated, so it cannot be (d).

Which means the correct answer is (b).
