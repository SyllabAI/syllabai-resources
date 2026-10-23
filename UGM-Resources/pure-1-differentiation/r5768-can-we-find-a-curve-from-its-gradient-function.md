---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r5768
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r5768
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5768
  old_site_id: Q3044
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
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: curve from gradient 4x-3 with minimum value -1/8 — the decisive step is locating the
        stationary point (the reverse-of-differentiation wrapper carries a recorded 1.8 bearing)
      rationale: 'Canonical UGM title: "Can we find a curve from its gradient function?"; exam provenance:
        UCLES O level Additional Mathematics 2, 1968, Q3'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Additional Mathematics 2, 1968, Q3
task: T-UGM-IMPORT-7
---

# Can we find a curve from its gradient function?

## Question

A function, \(y\), of \(x\) has gradient \(4x - 3\) at the point \((x,y)\) and the minimum value of the function is \(-\tfrac{1}{8}\). Express \(y\) in terms of \(x\) and sketch the graph of \(y\) against \(x\).

## Solution

A function, \(y\), of \(x\) has gradient \(4x - 3\) at the point \((x,y)\) and the minimum value of the function is \(-\tfrac{1}{8}\). Express \(y\) in terms of \(x\)…

The first part of the question tells us that

\[ \frac{dy}{dx} = 4x - 3. \]

so we know that

\[\begin{equation}\label{eq:indefinite-eq-for-y} y = \int \frac{dy}{dx} \:dx = 2x^2 - 3x + c \end{equation}\]

for some constant \(c\). (This is a consequence of the [fundamental theorem of calculus](https://undergroundmathematics.org/glossary/fundamental-theorem-of-calculus).)

The curve is a parabola and since the coefficient of \(x^2\) is positive we know its single stationary point is a minimum. We are also given that the \(y\)-value at the minimum is \(-\dfrac{1}{8}\).

This minimum occurs where

\(\dfrac{dy}{dx} = 0 \implies x = \dfrac{3}{4}\)

. Substituting into equation

\(\eqref{eq:indefinite-eq-for-y}\)

, we have that

\[\begin{align*} -\frac{1}{8} = 2 \left( \frac{3}{4} \right)^2 - 3 \cdot \frac{3}{4} + c &\implies c = -\frac{1}{8} - \frac{9}{8} + \frac{9}{4} \\ &\implies c = 1. \end{align*}\]

So we know that the equation of the curve is \(y = 2x^2 - 3x + 1\).

…and sketch the graph of \(y\) against \(x\).

We can factorise the expression for \(y\) as \[y = 2x^2 - 3x + 1 = (2x - 1)(x - 1).\] We thus have that the equation \(y = 0\) has two roots, at \(x = \dfrac{1}{2}\) and \(1\). The graph has a minimum at the point \(\left( \dfrac{3}{4}, -\dfrac{1}{8} \right)\), and finally, the \(y\)-intercept of the function is \(1\).
