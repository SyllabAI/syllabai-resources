---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r5059
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r5059
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5059
  old_site_id: Q4029
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Solve and interpret a quadratic inequality (1962 UCLES).
      rationale: 'Canonical UGM title: “When is $12x^2+7x-10$ negative?”; exam provenance: UCLES 1962
        Q7(ii),Q7(iii)'
      validation_status: SUGGESTED
    title: solve quadratic equations, and quadratic By factorising, completing the square and using the
      inequalities, in one unknown formula.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1962 Q7(ii),Q7(iii)
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/r5059/images/img-5059-1.png
  kind: figure
---

# When is $12x^2+7x-10$ negative?

## Question

1. Find the range of values of \(x\) for which the expression \(12x^2+7x-10\) is negative.
2. Find the range of values of \(c\) for which the expression \(x^2+4x+c\) is always positive.

## Suggestion

If a quadratic is always positive, what can be said about its roots?

## Solution

This is the same as asking: when is the curve \(y = 12x^2+7x-10\) below the \(x\)-axis?

Let’s start by finding when \(y = 0\). We can use the [quadratic formula](https://undergroundmathematics.org/glossary/quadratic-equation-solution) here, giving the roots as \[\frac{-7 \pm \sqrt{49 + 480}}{24} = -\dfrac{5}{4}\ \text{and}\ \dfrac{2}{3}.\]

(We could factorise here, but the factorisation \((3x-2)(4x+5)\) could take us a while to spot.)

The coefficient of \(x^2\) is positive here, so the curve is ‘vertex-down’. We have enough information now to sketch the curve.

> [figure: the parabola discussed above — `https://undergroundmathematics.org/quadratics/r5059/images/img-5059-1.png`] (image not included in the text import; path of record).

So the expression \(12x^2+7x-10\) is negative for \(-\dfrac{5}{4}<x<\dfrac{2}{3}\).

We note that since the coefficient of \(x^2\) is positive, \(x^2+4x+c\) will always be positive for some values of \(x\), and the curve \(y=x^2+4x+c\) is ‘vertex-down’.

So the question is the same as asking: which values of \(c\) mean that the curve \(y = x^2+4x+c\) is always above the \(x\)-axis?

This means there are no roots for \(y = 0\), and so the [discriminant](https://undergroundmathematics.org/glossary/discriminant) must be negative.

So we have \(4^2-4c < 0\), or \(c > 4\).

Hence the expression is always positive if and only if \(c > 4\).

Alternatively we could complete the square here. The expression \(x^2+4x+c\) can be written \((x+2)^2 + c-4\), which is always positive if and only if \(c>4\).
