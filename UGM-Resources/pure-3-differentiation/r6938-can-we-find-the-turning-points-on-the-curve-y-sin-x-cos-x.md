---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/r6938
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/review-question
resource_identity:
  ugm_id: r6938
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6938
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-trig-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-trig-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: turning points of y = sin x + cos x on (0, 2pi) via dy/dx = cos x - sin x = 0 - the canonical
        3.4.1 use of the standard derivatives, with the R-form of 3.3.2 as the recorded alternative (flips
        the lane-11 non-overlap row of record routed 'P3 3.4 Differentiation')
      rationale: 'Canonical UGM title: Can we find the turning points on the curve $y = \sin x + \cos
        x$?'
      validation_status: SUGGESTED
    title: use the derivatives of e , ln x , sin x , cos x , tan x , tan x , together with constant multiples,
      sums, differences and composites
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Can we find the turning points on the curve $y = \sin x + \cos x$?

## Question

Find the coordinates of the turning points on the curve \(y = \sin x + \cos x\) for \(0 < x < 2\pi.\)

## Solution

**Method 1; using calculus**

The turning points of the curve occur where the gradient is zero.

It is possible for the gradient of the curve to be zero and for this *not* to be a turning point, if we have a point of inflection. A sketch of the graph indicates that we do not have any points of inflection.

Differentiating, we have \(\dfrac{dy}{dx} = \cos x - \sin x\). This is zero if and only if \(\sin x = \cos x\). This equation is the same as \(\tan x = 1\).

We divided by \(\cos x\). This cannot be zero because then \(\sin x\) would be non-zero, so this would not be a solution to the equation.

Thus the solutions we seek in the range are \(x = \dfrac{\pi}{4}\) and \(\dfrac{5\pi}{4}\).

By substituting we find the coordinates of the turning points are a maximum at \(\left(\dfrac{\pi}{4}, \sqrt{2}\right)\) and a minimum at \(\left(\dfrac{5\pi}{4}, -\sqrt{2}\right)\).

**Method 2; using trigonometry**

There is an alternative method that does not use calculus but relies on the trigonometric identity \[\sin(x+\alpha) = \sin x \cos \alpha + \cos x \sin \alpha.\]

This holds for all real values of \(x\) and \(\alpha\).

So we can say that for some value of \(R\) and \(\alpha\) \[R\sin(x+\alpha) = R\sin x \cos \alpha + R\cos x \sin \alpha = \sin x + \cos x.\] Comparing coefficients on the right hand side, we want \(R\cos \alpha =1\), \(R\sin \alpha = 1\).

Squaring and adding these equations gives us \(R^2 = 2 \implies R = \sqrt{2}\), and dividing the two equations gives us \(\tan \alpha = 1 \implies \alpha = \dfrac{\pi}{4}\).

So \[\sin x + \cos x = \sqrt{2}\sin\left(x+\dfrac{\pi}{4}\right),\] and the turning points of the curve are where \(\sin\left(x+\dfrac{\pi}{4}\right)\) is \(1\) or \(-1\).

This happens when \(x = \dfrac{\pi}{4}\) (a maximum) or when \(x = \dfrac{5\pi}{4}\) (a minimum), and the full coordinates of the turning points are as before.

In this case, using calculus gives an easiest solution, but there are some questions that can more sensibly be tackled using the second method.
