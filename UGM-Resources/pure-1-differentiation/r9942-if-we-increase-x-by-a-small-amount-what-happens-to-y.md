---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r9942
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r9942
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9942
  old_site_id: Q3019
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
      evidence: dy/dx of 4x^3-7x^2 at (2,4), then the small increment dx that raises y from 4 to 4.05
        — power rule plus small-increment application
      rationale: 'Canonical UGM title: "If we increase $x$ by a small amount, what happens to $y$?";
        exam provenance: UCLES O level Additional Mathematics 2, 1977, Q6'
      validation_status: SUGGESTED
      primaryPick: true
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: dy/dx of 4x^3-7x^2 at (2,4), then the small increment dx that raises y from 4 to 4.05
        — power rule plus small-increment application
      rationale: 'Canonical UGM title: "If we increase $x$ by a small amount, what happens to $y$?";
        exam provenance: UCLES O level Additional Mathematics 2, 1977, Q6'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Additional Mathematics 2, 1977, Q6
task: T-UGM-IMPORT-7
---

# If we increase $x$ by a small amount, what happens to $y$?

## Question

Given that \(y = 4x^3 - 7x^2\), find the value of \(dy/dx\) at the point \((2,4)\).

Hence find the approximate increase in \(x\) which will cause \(y\) to increase from \(4\) to \(4.05\).

## Suggestion

Suppose \(y = f(x)\), and that \((x,y)\) is on this curve. We now increase \(x\) by a small amount \(\delta x\), which increases \(y\) by a small amount \(\delta y\) (\(y\) could decrease, in which case \(\delta y\) would be negative).

Can you see why \(y'\) evaluated at \(x\) is roughly \(\dfrac{\delta y}{\delta x}\)? A diagram might help…

## Solution

We know that the derivative of \(x^n\) is \(nx^{n-1}\). Using this, we have that \[\frac{dy}{dx} = y' = 4 \times 3x^2 - 7 \times 2x = 12x^2 - 14x.\] So we have that the value of \(\dfrac{dy}{dx}\) at the point \((2,4)\) is \[y'(2) = 12 \times 2^2 - 14 \times 2 = 48 - 28 = 20.\]

Consider the following graph of a curve \(y = f(x)\).

The slope of the tangent is close to the slope of the chord; that is, to use the notation in the figure,

\[ \frac{\delta y}{\delta x} \approx \frac{dy}{dx} \quad\text{when $\delta x$ is small.} \]

So if the

\(x\)

-coordinate of the leftmost point in this figure is denoted by

\(x_0\)

, then

\[\begin{equation}\label{eq:approximation-to-derivative} \frac{f(x_0+\delta x) - f(x_0)}{\delta x} \approx f'(x_0) \quad\text{when $\delta x$ is small}. \end{equation}\]

In fact, the *definition* of \(f'(x_0)\) is the value towards which \[\frac{f(x_0+\delta x) - f(x_0)}{\delta x}\] tends as \(\delta x\) tends towards zero.

In our case:

- \(f(x) = 4x^3 - 7x^2\),

- \(x_0 = 2\),

- \(f(x_0) = 4\), and

- \(f'(x_0) = 20\).

If we choose \(\delta x\) so that \(f(x_0 + \delta x) = 4.05\), then, from \(\eqref{eq:approximation-to-derivative}\), we would have \[\frac{4.05 - 4}{\delta x} = \frac{f(x_0+\delta x) - f(x_0)}{\delta x} \approx f'(x_0) = 20,\] and so, by rearranging, \[\delta x \approx \frac{4.05 - 4}{20} = \frac{1/20}{20} = \frac{1}{400} = 0.0025.\]

If we use our calculators, we find that \[f(2.0025) - f(2) = 0.05010\ldots,\] and so our approximation is a good one!
