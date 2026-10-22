---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r9742
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r9742
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9742
  old_site_id: Q3008
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: x-axis crossings of a parameterised quadratic.
      rationale: 'Canonical UGM title: “Where does $y = px^2 + 8x + p - 6$ cross the $x$-axis?”; exam
        provenance: UCLES 1983 Q13(a)'
      validation_status: SUGGESTED
    title: find the discriminant of a quadratic polynomial ax + bx + c and use the discriminant ‘repeated
      root’ is included.
  - code: 1.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: x-axis crossings of a parameterised quadratic.
      rationale: 'Canonical UGM title: “Where does $y = px^2 + 8x + p - 6$ cross the $x$-axis?”; exam
        provenance: UCLES 1983 Q13(a)'
      validation_status: SUGGESTED
    title: solve quadratic equations, and quadratic By factorising, completing the square and using the
      inequalities, in one unknown formula.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1983 Q13(a)
task: T-UGM-IMPORT-1
---

# Where does $y = px^2 + 8x + p - 6$ cross the $x$-axis?

## Question

Find the range of values of \(p\) for which the graph of \(y = px^2 + 8x + p - 6\) crosses the \(x\)-axis. State also the values of \(p\) for which the \(x\)-axis is a tangent to the curve.

## Solution

Given a quadratic equation \(ax^2 + bx + c = 0\), its [discriminant](https://undergroundmathematics.org/glossary/discriminant) is \(d = b^2 - 4ac\).

The graph of \(y = ax^2 + bx + c\) crosses the \(x\)-axis if, and only if, \(d > 0\).

Here the discriminant is

\[\begin{align*} d &= 8^2 - 4 \times p \times (p - 6) \\ &= 64 - 4(p^2 - 6p) \\ &= 4(-p^2 + 6p + 16) \\ &= 4(8-p)(2+p). \end{align*}\]

The graph of \(d=4(8-p)(2+p)=4(-p^2+6p+16)\) is “vertex-up” (as the coefficient of \(p^2\) is negative), and is zero when \(p=-2\) or \(p=8\). Therefore \(4(8-p)(2+p)>0\) if and only if \(-2 < p < 8\).

Thus the graph crosses the \(x\)-axis if and only if \(-2<p<8\).

This happens precisely when the \(x\)-axis touches the parabola. This happens if, and only if, the discriminant is zero.

From the above, this is the case when \(p = 8\) or \(p = -2\).
