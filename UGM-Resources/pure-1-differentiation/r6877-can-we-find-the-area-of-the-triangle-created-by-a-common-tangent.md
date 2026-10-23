---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r6877
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r6877
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6877
  old_site_id: Q3051
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
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: prove y^2=16x and y=x^2+3 touch at (1,4) via equal gradients (y=4x^(1/2) power rule)
        then the unit-area tangent triangle
      rationale: 'Canonical UGM title: "Can we find the area of the triangle created by a common tangent?";
        exam provenance: UCLES O level Additional Mathematics 2, 1967, Q2'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: prove y^2=16x and y=x^2+3 touch at (1,4) via equal gradients (y=4x^(1/2) power rule)
        then the unit-area tangent triangle
      rationale: 'Canonical UGM title: "Can we find the area of the triangle created by a common tangent?";
        exam provenance: UCLES O level Additional Mathematics 2, 1967, Q2'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Additional Mathematics 2, 1967, Q2
task: T-UGM-IMPORT-7
---

# Can we find the area of the triangle created by a common tangent?

## Question

Prove that the curves \(y^2 = 16x\) and \(y = x^2 + 3\) touch at the point \((1,4)\). Prove also that the common tangent at this point forms with the axes a triangle of unit area.

## Suggestion

The important word here is *touch*.

Suppose two curves both go though a point \(P\). What can we say about the tangent to each curve at \(P\) if the curves touch at \(P\)?

## Solution

To show that the two curves touch one another at \((1,4)\), we’ll show that

1. this point lies on both curves, and that

---

1. their gradients are equal at this point.

For the curve \(y = x^2 + 3\), since \(4 = 1^2 + 3\), the point \((1,4)\) lies on the curve.

We also have that \(y' = 2x \implies y'(1) = 2\).

For the curve defined by \(y^2 = 16x\), we have that \(4^2 = 16 \times 1\), and so the point \((1, 4)\) lies on this curve too.

If

\(y^2 = 16x\)

, then

\(y = 4\sqrt{x}=4x^{\frac{1}{2}}\)

, so

\[\begin{align*} \frac{dy}{dx} &= 4\times\frac{1}{2}\times x^{-\frac{1}{2}} \\ &=\frac{2}{\sqrt{x}} \end{align*}\]

which gives that \(y'(1)=2\).

Thus at \((1,4), y' = 2\) for both curves, and they do indeed kiss at \((1,4)\).

Alternatively, the curves intersect when \((x^2+3)^2=16x\), or \(x^4+6x^2-16x+9=0\).

This factorises to \((x-1)^2(x^2+2x+9)=0\) (we are looking for a double factor of \((x-1)\), since the question tells us to expect a touching at \(x = 1\)).

Thus there is a double root at \(x = 1\), and so the curves touch at \((1,4)\).

We might note the extra information that \(x^2+2x+9=0\) has no roots, since its discriminant is negative, so \((1,4)\) is the only place these curves coincide.

The tangent of the two curves at \((1,4)\) is of the form \(y = mx + c\), where \(m\) is the gradient of both curves at this point, and \(c\) is such that \((1,4)\) lies on the line.

We know that \(m = 2\). As \(c\) satisfies \(4 = m \times 1 + c\), we have \(c = 4 - 2 \times 1 = 2\). So the tangent is \(y = 2x + 2.\)

This intersects the axes at \((-1,0)\) and \((0,2)\), and so the area of the required triangle is \[\frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2} \times 1 \times 2 = 1.\]
