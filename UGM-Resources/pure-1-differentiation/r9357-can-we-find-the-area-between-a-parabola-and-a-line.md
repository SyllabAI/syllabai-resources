---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r9357
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r9357
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9357
  old_site_id: Q98
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
  exam_reference: Oxford University Mathematics Aptitude Test, None, Q1A
task: T-UGM-IMPORT-7
---

# Can we find the area between a parabola and a line?

## Question

The area of the region bounded by the curves \(y = x^2\) and \(y = x + 2\) equals

1. \(\frac{7}{3}\),

---

1. \(\frac{7}{2}\),

---

1. \(\frac{9}{2}\),

---

1. \(\frac{11}{2}\).

## Suggestion

Draw a sketch! Where do the curves intersect?

## Solution

The curves intersect when \(x^2 = x + 2\), or \((x - 2)(x + 1) = 0\), so the points of intersection are at \(x = 2\) and \(x = -1\).

From our sketch we can see that \(x + 2 \geq x^2\) in the region \(-1 \leq x \leq 2\), so
 \[\text{Area enclosed} = \left( \text{Area below } \; y = x + 2 \right) - \left(\text{Area below } \; y = x^2 \right) .\]

The area below \(y=x^2\) is calculated by integration, and the area below \(y=x+2\) can be found using the formula for the area of a trapezium. We have \[\text{Area below } \; y = x + 2 \; = 3 \times \frac{1+4}{2}=\frac{15}{2}, \text{while}\] \[\text{Area below } \; y = x^2 \; = \int\limits_{-1}^2 x^2 \; dx=\left[\frac{1}{3} x^3\right] _{-1}^2=\frac{8}{3}-\frac{-1}{3}=3.\]

So the area we seek is \[\frac{15}{2}-3=\frac{9}{2}\]

and the answer is (c).

You could also calculate the area under the straight line \(y=x+2\) using the integral \(\int\limits_{-1}^2 x+2 \; dx\).
