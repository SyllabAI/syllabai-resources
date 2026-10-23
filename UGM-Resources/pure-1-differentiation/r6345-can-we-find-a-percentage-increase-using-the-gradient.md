---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r6345
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r6345
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6345
  old_site_id: Q4003
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
      evidence: percentage increase in y=3x-2x^2 via the derivative — small-increment rates work (17p/7%)
      rationale: 'Canonical UGM title: "Can we find a percentage increase using the gradient?"; exam
        provenance: UCLES AO level Additional Mathematics 1, 1978, Q7'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES AO level Additional Mathematics 1, 1978, Q7
task: T-UGM-IMPORT-7
---

# Can we find a percentage increase using the gradient?

## Question

The function \(y\) is defined by \(y=3x-2x^2\). Write down its derivative and show that, when \(x=5\), a small increase in \(x\) of \(p\%\) causes an increase in the magnitude of \(y\) of approximately \(\dfrac{17p}{7}\%\).

## Suggestion

The function \(y\) is defined by \(y=3x-2x^2\). Write down its derivative and show that, when \(x=5\), a small increase in \(x\) of \(p\%\) causes an increase in the magnitude of \(y\) of approximately \(17p/7\%\).

Suppose \(y = f(x)\), and that \((x,y)\) is on this curve. We now increase \(x\) by a small amount \(\delta x\), which increases \(y\) by a small amount \(\delta y\) (\(y\) could decrease, in which case \(\delta y\) would be negative).

Can you see why \(y'\) evaluated at \(x\) is roughly \(\dfrac{\delta y}{\delta x}\)? A diagram might help…

## Solution

The function \(y\) is defined by \(y=3x-2x^2\). Write down its derivative and show that, when \(x=5\), a small increase in \(x\) of \(p\%\) causes an increase in the magnitude of \(y\) of approximately \(17p/7\%\).

The derivative of \(y=3x-2x^2\) is \(y'=\dfrac{dy}{dx}=3-4x\), so when \(x = 5, y = -35\) and \(y'=-17\).

We now approximate the curve with the tangent to the curve at \(x=5,\) which is justified if we are close to \((5,-35)\).

Suppose that \((x + \delta x, y + \delta y)\) is on the curve. Then we can express the percentage increase in \(x\) by \[\frac{\delta x}{x}\times 100=p,\] and similarly the percentage increase in \(y\) by \[\frac{\delta y}{y} \times 100 = q.\] Dividing these, we get \(\dfrac{\delta y}{\delta x} \dfrac{x}{y} = \dfrac{q}{p}\). Now if \(\delta x\) and \(\delta y\) are small, \(\dfrac{\delta y}{\delta x} \approx \dfrac{dy}{dx}\), so at \(x = 5, \dfrac{q}{p} \approx -17 \times \dfrac{5}{-35}\).

This gives us that \(q = \dfrac{17p}{7}\), and therefore the magnitude of \(y\) increases by approximately \(\dfrac{17p}{7}\) per cent.
