---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r9138
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r9138
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9138
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
  spec_points:
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: quadratic through (1,0) and (2,0) with gradient 2 at (2,0) — gradient conditions are
        the 1.7.3 step; the area computation carries a recorded 1.8 bearing
      rationale: 'Canonical UGM title: "Can we find the area enclosed by this quadratic and the $x$-axis?";
        exam provenance: UCLES O level Additional Mathematics 2, 1963, Q4'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Additional Mathematics 2, 1963, Q4
task: T-UGM-IMPORT-7
---

# Can we find the area enclosed by this quadratic and the $x$-axis?

## Question

The curve \(y=ax^2+bx+c\) passes through the points \((1,0)\) and \((2,0)\) and its gradient at the point \((2,0)\) is \(2\). Find the numerical value of the area included between the curve and the axis of \(x\).

## Solution

Since the curve passes through

\((1,0)\)

and

\((2,0)\)

we have

\[\begin{align*} ax^2+bx+c &= a(x-1)(x-2) \\ &= ax^2 -3ax +2a \end{align*}\]

Equating coefficients we find that

\[\begin{align} b&=-3a \label{eq:b} \\ \text{and }c&=2a \label{eq:c} \end{align}\]

We also know the gradient of the curve is \(2\) at \(x=2\). Differentiating, \[\frac{dy}{dx}=2ax+b,\] and so we have that \[4a+b=2.\] Substituting \(\eqref{eq:b}\) and \(\eqref{eq:c}\), we have \[a=2,\quad b=-6,\quad c=4.\] So the curve has the equation \(y=2x^2-6x+4\).

The area between the curve and the axis is found by integrating between the two roots at \(x=1\) and \(x=2\). Since the curve is below the axis this will give us a negative result whose numerical value is the area. \[\int_1^2 2x^2-6x+4 \, dx = \left[\frac{2x^3}{3}-3x^2+4x\right]^2_1=\frac{16}{3}-12+8-\frac{2}{3}+3-4=\frac{14}{3}-5=-\frac{1}{3}\] Thus the required area is \(\tfrac{1}{3}\).
