---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r7444
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r7444
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7444
  old_site_id: Q3021
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Additional Mathematics 1, 1977, Q3
task: T-UGM-IMPORT-7
---

# Can we find the area inside a straight line, a parabola and the x-axis?

## Question

The figure shows the curve \(y = x^2\) and the straight line \(2x + y = 15\). Find

1. the co-ordinates of \(P\) and \(Q\),

---

1. the area of the shaded region.

## Suggestion

The figure shows the curve \(y = x^2\) and the straight line \(2x + y = 15\). Find […] the area of the shaded region.

Is there a way of viewing the region differently?

A further suggestion

Could we, perhaps, view it as the sum of two simpler regions?

## Solution

The figure given in the question is the following.

The point \(P\) is the point in the first quadrant at which the curve \(y = x^2\) and line \(y = 15 - 2x\) cross. That is, it is the point whose \(x\)-coordinate is positive and such that \[x^2 = 15 - 2x.\] This equation can be rearranged to become \[x^2 + 2x - 15 = 0\] which, by inspection, factorises: \[(x + 5)(x - 3) = 0.\] Thus, the \(x\)-coordinate of \(P\) is \(3\), and so the coordinates of \(P\) are \((3,9)\) since, in particular, \(P\) lies on the curve \(y = x^2\).

The point \(Q\) is the \(x\)-intercept of the line, so the \(x\)-coordinate of \(Q\) is the value of \(x\) such that \[15 - 2x = 0.\] Thus, \(x = \tfrac{15}{2}\), and so the coordinates of \(Q\) are \(\left( \tfrac{15}{2}, 0 \right)\).

The key to this question is to break the region into two pieces, as the following diagram shows.

The shaded area is therefore the sum of the area of region \(A\) and the area of region \(B\), which are separated by the dotted line segment in the image. This dotted line segment is part of the line \(x = 3\), since the \(x\)-coordinate of the point \(P\) is \(3\).

The area of region \(A\) can be calculated by integration: \[\text{area of $A$} = \int_0^3 x^2 \:dx = \left[ \frac{x^3}{3} \right]_0^3 = \frac{3^3}{3} - 0 = 9.\]

On the other hand, region \(B\) is a (right-angled) triangle whose base has length \[\frac{15}{2} - 3 = \frac{9}{2}\] (which corresponds to the \(x\)-coordinate of \(P\) being subtracted from the \(x\)-coordinate of \(Q\)) and whose height has length \(9\), which corresponds to the \(y\)-coordinate of \(P\). Thus, \[\text{area of $B$} = \frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times \frac{9}{2} \times 9 = \frac{81}{4}.\]

Therefore, \[\text{area of shaded region} = \text{area of $A$} + \text{area of $B$} = 9 + \frac{81}{4} = \frac{117}{4}.\]
