---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r5501
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r5501
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5501
  old_site_id: Q1019
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: product-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: product-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: turning points of y = x^2/(1+x^4) via the product rule on x^2 (1+x^4)^-1 giving dy/dx
        = 2x(1-x^4)/(1+x^4)^2 - stationary points at 0, +/-1 and the sketch
      rationale: 'Canonical UGM title: Can we sketch $y=x^2/(1+x^4)$?'
      validation_status: SUGGESTED
    title: differentiate products and quotients e.g.
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Can we sketch $y=x^2/(1+x^4)$?

## Question

Find the coordinates of the turning points on the curve with equation \[y=\frac{x^2}{1+x^4}.\]

Sketch the curve.

## Suggestion

What do we know about the derivative of a function at a turning point?

Do we know any rules for differentiating functions like this one?

What does the curve look like for large values of \(x\)?

## Solution

Finding the derivative

\(y'\)

using the product rule with

\(y=x^2\dfrac{1}{1+x^4}\)

:

\[\frac{dy}{dx}=\frac{2x}{1+x^4}-\frac{4x^3\times x^2}{(1+x^4)^2}=\frac{2x(1+x^4)-4x^5}{(1+x^4)^2}.\]

So when

\(y'=0\)

,

\[\begin{align*} 2x(1+x^4) - 4x^5 &= 0 \\ \Longrightarrow 2x-2x^5 &= 0 \\ \Longrightarrow x(1-x^4) &= 0 \\ \Longrightarrow x(1-x^2)(x^2+1) &=0\\ \quad \Longrightarrow \quad x=0, \,\, x=\pm 1. \end{align*}\]

Substituting back into the equation we find that the coordinates of the turning points are

\((0,0)\)

,

\((\pm 1,\dfrac{1}{2})\)

.

For large \(x\), the \(x^4\) term dominates, and so \(y \rightarrow 0 \quad \text{as} \quad |x| \rightarrow \infty\).

The only root coincides with the stationary point \((0,0)\).
