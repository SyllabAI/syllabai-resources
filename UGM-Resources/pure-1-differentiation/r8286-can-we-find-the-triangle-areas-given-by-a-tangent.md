---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r8286
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r8286
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8286
  old_site_id: Q1031
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
      evidence: tangent to xy=c^2 at (ct,c/t) via dy/dx=-c^2/x^2 — rational-index power rule plus tangent
        construction with area links
      rationale: 'Canonical UGM title: "Can we find the triangle areas given by a tangent?"; exam provenance:
        UCLES A level Mathematics 2, 1954, Q4'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: tangent to xy=c^2 at (ct,c/t) via dy/dx=-c^2/x^2 — rational-index power rule plus tangent
        construction with area links
      rationale: 'Canonical UGM title: "Can we find the triangle areas given by a tangent?"; exam provenance:
        UCLES A level Mathematics 2, 1954, Q4'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics 2, 1954, Q4
task: T-UGM-IMPORT-7
---

# Can we find the triangle areas given by a tangent?

## Question

Find the equation of the tangent to the rectangular hyperbola \(xy=c^2\) at the point \(P(ct,c/t)\).

The tangent at \(P\) meets the axes of \(x\) and \(y\) at \(L\) and \(M\) respectively. \(O\) is the centre of the hyperbola and \(POQ\) is a diameter. The straight line \(MQ\) meets the axis of \(x\) in \(T\). Prove that

1. the area of triangle \(MOL\) is \(2c^2\),

---

1. the area of triangle \(QOT\) is \(c^2/3\).

## Suggestion

A well drawn diagram will help us a lot in this question!

What is the gradient at any point on the curve \(xy=c^2\)?

Can we use the equation of the tangent at \(P\) to find \(L\) and \(M\)?

What are the coordinates of \(Q\) if \(POQ\) is a diameter?

Note that a diameter of a hyperbola is any straight line passing through its centre. We can assume here that \(Q\) is the point on the hyperbola opposite \(P\).  Note; $AOB$ is a diameter of a hyperbola if and only if the straight line segment $AOB$ has rotational symmetry of order $2$ about $O$.

## Solution

Differentiating the curve \(y=\dfrac{c^2}{x}\) we find

\[\dfrac{dy}{dx}=-\dfrac{c^2}{x^2}.\]

So the gradient at \(P = (ct,c/t)\) is \(-\dfrac{1}{t^2}\).

Thus the equation of the tangent here is

\[\begin{align*} y-\dfrac{c}{t} &= -\dfrac{1}{t^2}(x-ct) \\ \Longrightarrow y &= -\dfrac{x}{t^2}+\frac{2c}{t} = \dfrac{2ct-x}{t^2} \end{align*}\]

1. Prove that the area of the triangle \(MOL\) is \(2c^2\)

The \(x\)-intercept of the tangent: \[0=\dfrac{2ct-x}{t^2}\quad \Longrightarrow \quad x=2ct,\] so \(L\) is \((2ct,0)\).

The \(y\)-intercept of the tangent: \[y=\dfrac{2ct}{t^2}=\dfrac{2c}{t},\] so \(M\) is \((0,\dfrac{2c}{t}).\)

So using area = \(\dfrac{1}{2} \times \,\text{base}\, \times\, \text{height}\), the area of triangle \(MOL\) is \[\dfrac{1}{2}\times 2ct \times \dfrac{2c}{t}=2c^2.\]

1. Prove that the area of the triangle \(QOT\) is \(c^2/3\).

The coordinates of point \(Q\) are \((-ct,-c/t)\) since it is the reflection of \(P\) in \(O\).

The line joining \(Q = (-ct,-c/t)\) and \(M = (0,2c/t)\) has gradient \[\dfrac{\dfrac{2c}{t}+\dfrac{c}{t}}{ct}=\dfrac{3}{t^2}.\] Therefore the equation of the line \(QM\) is \[y-\dfrac{2c}{t}={3}{t^2}x.\] The \(x\)-intercept is then \[x=-\dfrac{2c}{t}\times\dfrac{t^2}{3}=-\dfrac{2ct}{3}.\]

Thus triangle \(QOT\) has base \(\dfrac{2ct}{3}\) and height \(\dfrac{c}{t}\) so its area is \[\dfrac{1}{2}\times \dfrac{2ct}{3}\times\dfrac{c}{t}=\dfrac{c^2}{3}.\]
