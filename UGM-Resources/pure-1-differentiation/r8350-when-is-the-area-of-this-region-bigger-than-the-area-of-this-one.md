---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r8350
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r8350
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8350
  old_site_id: null
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2016, Q1H
task: T-UGM-IMPORT-7
---

# When is the area of this region bigger than the area of this one?

## Question

Consider two functions \[f(x) = a - x^2,\] \[g(x) = x^4 - a.\]

For precisely which values of \(a > 0\) is the area of the region bounded by the \(x\)-axis and the curve \(y = f(x)\) bigger than the area of the region bounded by the \(x\)-axis and curve \(y = g(x)\)?

1. all values of \(a\),

---

1. \(a > 1\),

---

1. \(a > \dfrac{6}{5}\),

---

1. \(a > \left(\dfrac{4}{3}\right)^{3/2}\),

---

1. \(a > \left(\dfrac{6}{5}\right)^4\).

## Suggestion

Drawing a diagram might help to visualise what is happening here.

Can we use calculus to find the areas mentioned?

What do we know about areas below the \(x\)-axis?

## Solution

The area of the region bounded by the \(x\)-axis and the curve \(y = f(x)\) is \[\int_{-a^{1/2}}^{a^{1/2}} a - x^2 \:dx = \left[ax-\dfrac{x^3}{3}\right]_{-a^{1/2}}^{a^{1/2}} = \dfrac{4a^{3/2}}{3}.\]

On the other hand the area of the region bounded by the \(x\)-axis and the curve \(y = g(x)\) is \[-\int_{-a^{1/4}}^{a^{1/4}} x^4 - a \:dx = -\left[\dfrac{x^5}{5}-ax\right]_{-a^{1/4}}^{a^{1/4}} = \dfrac{8a^{5/4}}{5}.\]

Since \(5/4<3/2\) it follows that when \(a\) is small, \(\dfrac{8a^{5/4}}{5} > \dfrac{4a^{3/2}}{3}\), but when \(a\) is large, \(\dfrac{8a^{5/4}}{5} < \dfrac{4a^{3/2}}{3}\).

So when are these two areas equal? When \[\dfrac{8a^{5/4}}{5} = \dfrac{4a^{3/2}}{3} \iff a^{1/4}=\dfrac{6}{5} \iff a = \left(\dfrac{6}{5}\right)^4,\] and so the answer is (e).
