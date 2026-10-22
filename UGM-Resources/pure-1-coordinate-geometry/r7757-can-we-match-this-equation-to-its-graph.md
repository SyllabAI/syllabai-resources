---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r7757
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r7757
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7757
  old_site_id: Q141
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: geometry-of-equations
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: geometry-of-equations
    validation_status: SUGGESTED
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule 3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) None Q1J
task: T-UGM-IMPORT-3
---

# Can we match this equation to its graph?

## Question

A sketch of the curve with equation \(x^2y^2(x+y)=1\) is drawn in which of the following diagrams?

| (a) |  | (b) |  |
|---|---|---|---|
| (c) |  | (d) |  |

## Solution

Firstly, we can rule out options (a) and (b) because points which satisfy \(x^2y^2(x+y)=1\) cannot have \(x=0\) or \(y=0\). Since graphs (a) and (b) both cross the axes, these cannot give the correct solution.

Now let’s rearrange the equation of the curve. We have \[x+y=\frac{1}{x^2y^2}>0\] so points on the curve must lie only in regions where \(x+y>0\), or \(y>-x\). This rules out option (d).

Hence, by process of elimination, (c) is the correct answer.

Alternatively, can we have \(x=y\:\)? We can, but only where \(x=y=2^{-1/5}>0\). Graphs (a) and (b) show no such point, while graph (d) seems to show \(4\) of them. Hence the answer must be (c). Or we can ask, can $x = y>0$? Yes - this gives $x = 2^{-1/5} = y$, which rules out (a) and (b). Can $x = y<0$? No, but (d) suggests the answer is yes, so this is ruled out too, and (c) is the answer.
