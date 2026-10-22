---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r9617
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r9617
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9617
  old_site_id: None
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
  exam_reference: Oxford (MAT) 2012 Q1D
task: T-UGM-IMPORT-3
---

# Which of these graphs shows the area $A(c)$ as $c$ varies?

## Question

Shown below is a diagram of the square with vertices \((0, 0), (0, 1), (1, 1), (1, 0)\) and the line \(y = x+c\). The shaded region is the region of the square which lies below the line; this shaded region has area \(A(c)\).

Which of the following graphs shows \(A(c)\) as \(c\) varies?

## Suggestion

What values of \(c\) give a positive area?

When will the area be growing quickly and when slowly?

Which of the graphs given are in line with this?

Alternatively; can we come up with an explicit formula for \(A(c)\), one that tells us what \(A(c)\) is terms of \(c\)?

Could we consider the two cases \(-1 \leq c \leq 0\) and \(0 \leq c \leq 1\) separately?

What shape would the graph of such a formula be?

## Solution

The area \(A(c)\) is first positive once \(c\) becomes greater than \(−1\), which is when the line \(y = x + c\) first touches the square.

As \(c\) increases, the area increases more and more quickly (as more of the line \(y = x + c\) lies within the square) until \(c = 0\) (when \(y = x\) is a diagonal of the square).

The area then increases more and more slowly until \(c = 1,\) at which point \(A(c)\) reaches its maximum value.

The graph with this shape is (a).

Algebraically, looking at the areas of triangles, when \(-1 \leq c \leq 0\), we have \[A(c) = \dfrac{1}{2}(1+c)^2,\] and when \(0 \leq c \leq 1\), we have \[A(c) = 1-\dfrac{1}{2}(1-c)^2 = c+\dfrac{1}{2} -\dfrac{c^2}{2}.\]

Thus for \(-1 \leq c \leq 0\), we have part of a vertex-down parabola, while for \(0 \leq c \leq 1\), we have part of a vertex-up parabola.

The only possible answer is (a).
