---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r9599
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r9599
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9599
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
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: '100 cm wire into an equilateral triangle and a square: show the total-area formula
        then find the least area — canonical CIE P1 optimisation'
      rationale: 'Canonical UGM title: "What can we say about the combined area of these two shapes?";
        exam provenance: UCLES O level Additional Mathematics 1, 1987, Q10'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: '100 cm wire into an equilateral triangle and a square: show the total-area formula
        then find the least area — canonical CIE P1 optimisation'
      rationale: 'Canonical UGM title: "What can we say about the combined area of these two shapes?";
        exam provenance: UCLES O level Additional Mathematics 1, 1987, Q10'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Additional Mathematics 1, 1987, Q10
task: T-UGM-IMPORT-7
---

# What can we say about the combined area of these two shapes?

## Question

A piece of wire, \(100\) cm in length, is divided into two parts. One part is bent to form an equilateral triangle of side \(x\) cm and the other is bent to form a square of side \(y\) cm.

Express \(y\) in terms of \(x\) and hence show that \(\quantity{A}{cm^2}\), the total area enclosed by the two shapes, is such that \[A=\frac{\sqrt{3}x^2}{4}+\frac{(100-3x)^2}{16}.\] Calculate the value of \(x\) for which \(A\) has a stationary value. Determine whether this value of \(x\) makes \(A\) a maximum or a minimum.

## Solution

A piece of wire, \(100\) cm in length, is divided into two parts. One part is bent to form an equilateral triangle of side \(x\) cm and the other is bent to form a square of side \(y\) cm.

Express \(y\) in terms of \(x\)…

The perimeter of the two shapes will add up to \(100\). Hence we must have that \[3x+4y=100,\] since \(x\) is the side length of an equilateral triangle and \(y\) is the side length of a square. Rearranging this equation tells us that \[y=\frac{100-3x}{4}.\]

…hence show that \(\quantity{A}{cm^2}\), the total area enclosed by the two shapes, is such that \[A=\frac{\sqrt{3}x^2}{4}+\frac{(100-3x)^2}{16}.\]

Since the angles in an equilateral triangle are \(60^\circ\), we have that the area of the equilateral triangle is \[\frac{1}{2}x^2\sin 60=\frac{\sqrt{3}}{4}x^2.\] The area of the square is \[y^2=\frac{(100-3x)^2}{16}.\] Therefore \[A=\frac{\sqrt{3}}{4}x^2+\frac{(100-3x)^2}{16}\] as required.

Expanding the bracket and differentiating we have

\[\begin{align*} A &= \frac{\sqrt{3}}{4}x^2 + \frac{10\,000}{16} - \frac{600x}{16} + \frac{9x^2}{16} \\ \frac{dA}{dx} &= \frac{\sqrt{3}}{2}x - \frac{600}{16} + \frac{9x}{8} \\ &=\frac{4\sqrt{3}+9}{8}x-\frac{300}{8}. \end{align*}\]

At the stationary value this is zero, \[x=\frac{300}{4\sqrt{3}+9}\approx 18.8,\] which gives \(y \approx 10.9\), and \(A \approx 126.4\).

\(A\) is a quadratic function of \(x\) so it has only one stationary value. The coefficient of \(x^2\) is positive so the stationary point must be a minimum.

Alternatively, we could evaluate the second derivative \[\frac{d^2A}{dx^2}=\frac{4\sqrt{3}+9}{8}>0,\] for all \(x\), and so the stationary point must be a minimum.
