---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r8620
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r8620
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8620
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: 'x = (3-2t)^2, y = t^2 - 2t: dy/dx in terms of t, the stationary point, and the normal
        at t = 2 - the exact CIE 3.4.3 parametric exercise'
      rationale: 'Canonical UGM title: Can we find the equation of the normal to the curve when $t = 2$?'
      validation_status: SUGGESTED
    title: find and use the first derivative of a function e.g. which is defined parametrically or implicitly.
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Can we find the equation of the normal to the curve when $t = 2$?

## Question

A curve is represented parametrically by the equations

\[\begin{equation*} x = (3-2t)^2, \quad y = t^2 - 2t. \end{equation*}\]

Find

1. \(dy/dx\) in terms of \(t\),

---

1. the co-ordinates of the stationary point of the curve,

---

1. the equation of the normal at the point where \(t = 2\).

## Solution

We can write

\[\begin{equation*} \frac{dy}{dx} = \frac{\frac{dy}{dt}}{\frac{dx}{dt}}. \end{equation*}\]

We have that (by the

Chain Rule

)

\[\begin{equation*} \frac{dx}{dt} = 2(3-2t)(-2) = 4(2t-3), \quad \frac{dy}{dt} = 2t - 2 \end{equation*}\]

and therefore

\[\begin{equation*} \frac{dy}{dx} = \frac{2t - 2}{4(2t-3)} = \frac{t-1}{2(2t-3)}. \end{equation*}\]

The stationary point of the curve occurs when \(\dfrac{dy}{dx} = 0\), i.e. when \(t = 1\).

As \(x = (3-2t)^2\) and \(y = t^2 - 2t\), the co-ordinates of the stationary point are \((1,-1)\).

When

\(t = 2\)

, the gradient of the curve is

\[\begin{equation*} \frac{dy}{dx} = \frac{2-1}{2(2 \times 2 - 3)} = \frac{1}{2}. \end{equation*}\]

The gradient of the normal to the curve at this point is the negative of the reciprocal of this, i.e. \(-2\).

Thus, the equation of the normal is \(y = -2x + c\), for some constant \(c\), where we require that the original curve crosses the normal at \(t=2\).

When \(t=2\), the curve has \(x\)-coordinate \((3 - 2 \times 2)^2 = 1\) and \(y\)-coordinate \(2^2 - 2 \times 2 = 0\).

So, substituting these values into the equation for the normal, we require \(c\) to be such that \(0 = - 2 \times 1 + c\), i.e. \(c = 2\).

Consequently, the equation of the normal is \(y = -2x + 2\).
