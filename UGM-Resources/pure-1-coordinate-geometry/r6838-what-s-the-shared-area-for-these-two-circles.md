---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r6838
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r6838
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6838
  old_site_id: None
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: circles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: circles
    validation_status: SUGGESTED
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule 3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1982 Q6
task: T-UGM-IMPORT-3
assets:
- path: https://undergroundmathematics.org/circles/r6838/download/teacher-notes.pdf
  kind: printable
---

# What's the shared area for these two circles?

## Question

Two coplanar circles, each of radius \(\quantity{5}{cm}\), have their centres \(\quantity{6}{cm}\) apart. Calculate the area of the region common to the interiors of both the circles, giving your answer in \(\mathrm{cm}^2\) correct to two significant figures.

## Suggestion

What diagram could you draw to represent the problem? Label all the lengths you know.

Which areas of shapes can you find?

## Solution

To calculate the shaded area, we’ll compute the area of the circle sector \(ACE\), before subtracting the area of the triangle \(ACD\), and then multiplying by \(4\).

The length \(AD\) must be \(3\), and so by Pythagoras, the length of \(CD\) must be \(4\). Thus \(\angle CAD\) is \(\arctan \dfrac{4}{3}\).

Thus the area of the sector \(ACE\) (working in radians) is \(0.5 \times 5^2 \times \arctan \dfrac{4}{3}\), while the area of triangle \(ACD\) is \(0.5 \times 4 \times 3 = 6\).

So the shaded area is \(4(12.5 \arctan \dfrac{4}{3}-6) = 22.36\dots\), which is \(\quantity{22}{cm^2}\) when given to two significant figures.
