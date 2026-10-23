---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r6584
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r6584
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6584
  old_site_id: Q3017
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
  spec_points:
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: tangent to y=x^2 at P, x-intercept Q — the tangent construction is the 1.7.3 load-bearing
        step; the shaded-area computation carries a recorded 1.8 bearing
      rationale: 'Canonical UGM title: "Can we find the area inside a parabola, a tangent, and the $x$-axis?";
        exam provenance: UCLES AO level Additional Mathematics 2, 1980, Q2'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES AO level Additional Mathematics 2, 1980, Q2
task: T-UGM-IMPORT-7
---

# Can we find the area inside a parabola, a tangent, and the $x$-axis?

## Question

The figure shows part of the curve \(y = x^2\). \(PQ\) is the tangent to this curve at \(P\).

Calculate

1. the coordinates of \(Q\),

---

1. the area of the shaded region.

## Suggestion

The point \(Q\) is the \(x\)-intercept of the tangent. Can we find the equation of the tangent at P, and so find Q?

Could we view this region as the difference of two simpler regions?

## Solution

The tangent to the curve at \(P\) intersects the \(x\)-axis at \(Q\). A sensible first step would be to calculate the equation of the tangent. This takes the form \[y = mx + c\] where \(m\) is the gradient of the curve \(y = x^2\) at \(P\) and \(c\) is chosen so that the tangent line passes through \(P\).

The gradient of the curve \(y = x^2\) at \(P = (4,16)\) is given by \(y'=2x\) when \(x = 4\), so \(m=8\).

For the tangent line to pass through \(P\), \(c\) must be chosen so that the equation \[16 = 8 \times 4 + c\] is true. That is, \(c = -16\), and so the equation of the tangent is \[y = 8x - 16.\]

The \(x\)-intercept for the tangent is the value of \(x\) for which \(y = 0\) in the equation defining the tangent.

That is, to find \(Q\) we are looking for the value of \(x\) that satisfies the equation \[0 = 8x - 16.\] Hence, \(x = 2\), and so \(Q = (2,0)\).

The area we are to find can be found as the area of the light blue region minus the area of the light red region.

The area of the light blue region is given by \[\int_0^4 x^2 \:dx = \left[ \dfrac{x^3}{3} \right]_0^4 = \dfrac{4^3}{3} - \dfrac{0^3}{3} = \dfrac{64}{3}.\]

The area of the light red region is the area of a triangle, and so it equals

\[ \dfrac{1}{2} \times \text{base} \times \text{height} = \dfrac{1}{2} \times (4 - 2) \times 16 = 16. \]

Consequently, the desired area is

\[ \dfrac{64}{3} - 16 = \dfrac{16}{3}. \]

Can we generalise here? If we give the point \(P\) coordinates \((p, p^2)\), what is the required area now?
