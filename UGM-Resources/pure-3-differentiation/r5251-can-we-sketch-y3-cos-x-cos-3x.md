---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r5251
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r5251
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5251
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
  - code: 3.4.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: d/dx (3 cos x - cos 3x) = 6 sin x cos 2x proved by the chain rule on cos 3x plus the product-to-sum
        identity, then the increasing ranges and the sketch (flips the lane-11 non-overlap row of record
        routed 'P3 3.4 Differentiation')
      rationale: 'Canonical UGM title: Can we sketch $y=3 \cos x - \cos 3x$?'
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

# Can we sketch $y=3 \cos x - \cos 3x$?

## Question

Prove that

\[\begin{equation*} \frac{d}{dx} (3 \cos x - \cos 3x)= 6 \sin x \cos 2x. \end{equation*}\]

For what two ranges of values of

\(x\)

between

\(0\)

and

\(\pi\)

is

\[\begin{equation*} 3 \cos x - \cos 3x \end{equation*}\]

an increasing function of \(x\)?

Draw a rough sketch-graph of \(y = 3 \cos x - \cos 3x\) for values of \(x\) from \(0\) to \(\pi\), indicating clearly any maximum or minimum points.

## Solution

Using the

chain rule

or by thinking about horizontal scaling, we have that

\[\begin{equation*} \frac{d}{dx} \cos 3x = - 3 \sin 3x. \end{equation*}\]

By the

compound angle formula

,

\[\begin{align*} \sin 3x = \sin(x + 2x) &= \sin x \cos 2x + \sin 2x \cos x \\ &= \sin x \cos 2x + 2 \sin x \cos^2 x \\ &= \sin x \cos 2x + \sin x (1 + \cos 2x) \\ &= 2 \sin x \cos 2x + \sin x \end{align*}\]

so that

\[\begin{align*} \frac{d}{dx} \left( 3 \cos x - \cos 3x \right) &= - 3 \sin x + 3 \sin 3x \\ &= - 3 \sin x + 6 \sin x \cos 2x + 3 \sin x \\ &= 6 \sin x \cos 2x. \end{align*}\]

Alternatively, we can use the standard formula, \(\sin P-\sin Q = 2\cos\left(\dfrac{P+Q}{2}\right)\sin\left(\dfrac{P-Q}{2}\right)\).

A function is increasing exactly when its derivative is positive, so we are looking for those ranges of values of

\(x\)

such that

\[\begin{equation*} \frac{d}{dx} \left( 3 \cos x - \cos 3x \right) > 0 \end{equation*}\]

which, from the above, is equivalent to the inequality

\[\begin{equation*} \sin x \cos 2x > 0. \end{equation*}\]

This holds exactly when \(\sin x\) and \(\cos 2x\) have the same sign. We know that \(\sin x\) is positive when \(0 < x < \pi\), so the required inequality can only hold when \(\cos 2x > 0\). We know that:

- \(\cos 2x > 0\) when \(0 < x < \pi/4\),

- \(\cos 2x < 0\) when \(\pi/4 < x < 3\pi/4\), and

- \(\cos 2x > 0\) when \(3\pi/4 < x < \pi\).

The regions are therefore \(0< x < \pi/4\) and \(3\pi/4 < x < \pi\).

From the above, we know that \(y\) is

- equal to \(2\) when \(x = 0\);

- increasing in the region \(0 < x < \pi/4\);

- stationary when \(x = \pi/4\);

- decreasing in the region \(\pi/4 < x < 3\pi/4\);

- stationary when \(x = 3\pi/4\);

- increasing when \(3\pi/4 < x < \pi\); and

- equal to \(-2\) when \(x = \pi\).

The only aspects left to consider are the location of the

\(x\)

-intercept in the decreasing phase and the value of the function at the stationary points. Symmetry suggests that the

\(x\)

-intercept might be at

\(x=\frac{\pi}{2}\)

so we start by trying that.

\[\begin{align*} \text{At }x=\frac{\pi}{2},\quad y &= 3 \cos \frac{\pi}{2} - \cos \frac{3\pi}{2} = 0,\\ \text{At }x=\frac{\pi}{4},\quad y &= 3 \cos \frac{\pi}{4} - \cos \frac{3\pi}{4} = \frac{3\sqrt{2}}{2} + \frac{\sqrt{2}}{2} = 2\sqrt{2},\\ \text{At }x=\frac{3\pi}{4},\quad y &= 3 \cos \frac{3\pi}{4} - \cos \frac{9\pi}{4} = -\frac{3\sqrt{2}}{2} - \frac{\sqrt{2}}{2} = -2\sqrt{2}. \end{align*}\]

We also have rotational symmetry about \(\left(\dfrac{\pi}{2},0\right)\), as \(y(x) = -y\left(\pi - x \right)\) for any \(0 < x < \dfrac{\pi}{2}\). We thus have the following sketch graph.
