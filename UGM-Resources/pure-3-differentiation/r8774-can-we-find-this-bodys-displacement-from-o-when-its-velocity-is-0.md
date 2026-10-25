---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/product-rule/r8774
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- product-rule
- type/review-question
resource_identity:
  ugm_id: r8774
  station: product-rule
  station_title: Product Rule & Integration by Parts
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8774
  old_site_id: Q4058
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: product-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: product-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: acceleration as d/dt of v = (2t-1)/(4(2t+1)) by the quotient rule (a = 1/(2t+2)^2) - the
        quotient-rule computation is the tested skill in kinematics clothing; the displacement part is
        an integral (3.5 bearing)
      rationale: 'Canonical UGM title: Can we find this body''s displacement from $O$ when its velocity
        is $0$?'
      validation_status: SUGGESTED
    title: differentiate products and quotients e.g.
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Can we find this body's displacement from $O$ when its velocity is $0$?

## Question

A body moves in a straight line so that at time \(\quantity{t}{sec.}\) its velocity \(\quantity{v}{ft./sec.}\) is given by the formula\[v= \frac{2t-1}{4(2t+1)}.\]

Find:

1. the displacement of the body, measured from its position when \(t=0\), at the instant when its velocity is zero;

---

1. the acceleration of the body at this instant.

[The numerical answer to (i) is required correct to two significant figures.]

## Suggestion

Find:

1. the displacement of the body, measured from its position when \(t=0\), at the instant when its velocity is zero;

[The numerical answer to (i) is required correct to two significant figures.]

Could we find the displacement by integrating the velocity?

Find:

1. the acceleration of the body at this instant.

Could we find the acceleration by differentiating the velocity?

## Solution

A body moves in a straight line so that at time \(\quantity{t}{sec.}\) its velocity \(\quantity{v}{ft./sec.}\) is given by the formula\[v= \frac{2t-1}{4(2t+1)}.\]

Find:

1. the displacement of the body, measured from its position when \(t=0\), at the instant when its velocity is zero;

[The numerical answer to (i) is required correct to two significant figures.]

The velocity is the rate of change of displacement. So to calculate the displacement away from its initial position at a given time, we need to integrate the velocity as a function of time.

Clearly if \(v = 0\), then \(t = 0.5\). We have \[v = \dfrac{1}{4}\left( \dfrac{2t-1}{2t+1} \right) = \dfrac{1}{4}\left( \dfrac{(2t+1)-2}{2t+1} \right) = \dfrac{1}{4}\left( 1 -\dfrac{2}{2t+1} \right).\]

Thus \[d = \dfrac{1}{4} \int v \:d t = \dfrac{1}{4}\left( t - \ln{\big\vert 2t+1\big\vert} + c \right) = \dfrac{t}{4} - \dfrac{\ln{\big\vert 2t+1\big\vert}}{4} + c'.\]

If \(d = 0\) when \(t = 0\), then \(c' = 0\), so at \(t = 0.5,\)

\[d = \dfrac{1}{8} - \dfrac{\ln{2}}{4} \approx \quantity{-0.048}{ft}.\]

Find: (ii) the acceleration of the body at this instant.

The acceleration \(a\) of a body at time \(t\) is found by differentiating the expression for its the velocity.

So here we have \(a = \dfrac{d}{dt} \dfrac{2t-1}{4(2t+1)}\). Using the [quotient rule](https://undergroundmathematics.org/glossary/quotient-rule), we have

\[\begin{align*} a &= \dfrac{4(2t+1)\times 2 -(2t-1)\times 8 }{16(2t+2)^2}\\ &=\dfrac{16t+8 -16t+8}{16(2t+2)^2}\\ &=\dfrac{1}{(2t+2)^2} \end{align*}\]

Putting \(t = 0.5\) gives us \[a= \quantity{0.25}{ft./sec.^2}\]
