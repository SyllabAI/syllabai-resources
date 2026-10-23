---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r8065
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r8065
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8065
  old_site_id: Q3052
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
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: delta y ~ (dy/dx) delta x with y=sqrt(x) gives sqrt(26) ~ 5.1 — the canonical small-increment
        review question
      rationale: 'Canonical UGM title: "What (approximately) is the square root of $26$?"; exam provenance:
        O&C O level Additional Mathematics 1, 1967, Q7(ii)'
      validation_status: SUGGESTED
      primaryPick: true
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: O&C O level Additional Mathematics 1, 1967, Q7(ii)
task: T-UGM-IMPORT-7
---

# What (approximately) is the square root of $26$?

## Question

By making use of the relation \(\delta y \approx \dfrac{dy}{dx} \times \delta x\), and without using tables, prove that \(5.1\) is an approximate value of \(\sqrt{26}\).

## Suggestion

There is a convention in maths that \(\delta y\) signifies ‘a small increase in \(y\)’.

We need to specify \(y=f(x)\). Can we think of an appropriate \(f(x)\), given that we’re trying to find \(\sqrt{26}\)?

A further suggestion

What happens if we choose \(y = \sqrt{x}\)?

A final suggestion

If we take \(y = \sqrt{x}\), what happens if we then use \(x = 25\) and \(\delta x = 1\)?

## Solution

Let’s consider the function \(y = \sqrt{x}\). We know that \(y(25) = \sqrt{25} = 5\) and that \[\frac{dy}{dx} = y' = \frac{1}{2} x^{-1/2} \implies y'(25) = \frac{1}{2\sqrt{25}} = \frac{1}{10}.\]

Now using \(\delta y \approx \dfrac{dy}{dx} \times \delta x\) at the point \(x = 25, y = 5\), with \(\delta x = 1\), we see that \(\delta y = 0.1 \times 1 \implies y + \delta y = 5.1.\)

Thus \(\sqrt{26} = \sqrt{25+1} \approx 5.1.\)

We can’t immediately say how accurate our approximation is here.

If we turn to our calculators, they tell us \(\sqrt{26} = 5.0990\!\ldots\), and so our approximation is surprisingly accurate (\(0.02\)% out).

With a problem like this, such accuracy cannot always be guaranteed!
