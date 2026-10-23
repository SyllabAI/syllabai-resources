---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r7391
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r7391
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7391
  old_site_id: Q4001
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
      evidence: gradient 17 at P on y=3x^2+5x-12, then gradients at the x-intercepts — plain power-rule
        fluency with a quadratic solve
      rationale: 'Canonical UGM title: "What is the gradient of this curve at its $x$-intercepts?";
        exam provenance: UCLES AO level Certificate in Additional Mathematics 1, 1989, Q2'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: gradient 17 at P on y=3x^2+5x-12, then gradients at the x-intercepts — plain power-rule
        fluency with a quadratic solve
      rationale: 'Canonical UGM title: "What is the gradient of this curve at its $x$-intercepts?";
        exam provenance: UCLES AO level Certificate in Additional Mathematics 1, 1989, Q2'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES AO level Certificate in Additional Mathematics 1, 1989, Q2
task: T-UGM-IMPORT-7
---

# What is the gradient of this curve at its $x$-intercepts?

## Question

The gradient of the curve \(y=3x^2+5x-12\) is \(17\) at the point \(P\). Calculate the coordinates of \(P\).

The curve cuts the \(x\)-axis at \(Q\) and \(R\). Find the gradient of the curve at \(Q\) and at \(R\).

## Solution

The gradient of the curve is given by \[\frac{dy}{dx}=6x+5.\] We must find the value of \(x\) for which \[6x+5=17.\] Subtracting \(5\) from both sides, we see that \[6x=12,\] and therefore \[x=2.\] Therefore \(P=(2, 3\times 2^2+5\times 2-12)=(2,10)\).

We must first find \(Q\) and \(R\) by finding the roots of \(y=3x^2+5x-12=0\). By inspection, we can see that \[3x^2+5x-12=(3x-4)(x+3),\] and so \[Q=(-3,0),\quad R=(\frac{4}{3},0).\]

Evaluating \(\dfrac{dy}{dx}\) at these points, we find that at Q, \[\frac{dy}{dx}=6\times -3+5=-13,\] and at R, \[\frac{dy}{dx}=6\times \frac{4}{3}+5=13.\] So the gradient of the curve at \(Q\) is \(-13\), and at \(R\) is \(13\).

Why do the two gradients differ only in their sign?
