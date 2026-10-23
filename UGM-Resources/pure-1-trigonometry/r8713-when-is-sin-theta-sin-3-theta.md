---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r8713
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r8713
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8713
  old_site_id: Q1083
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-compound-angles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-compound-angles
    validation_status: SUGGESTED
  spec_points:
  - code: 1.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: 'sinθ > sin 3θ: sketch both curves on 0–2π (solution suggested); triple-angle alternative
        rides P3 — recorded'
      rationale: 'Canonical UGM title: “When is $\sin\theta > \sin 3\theta$?”; exam provenance: UCLES
        A level Pure Mathematics 3, QP 447/3, 1963, Q1(ii)'
      validation_status: SUGGESTED
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  - code: 1.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: 'sinθ > sin 3θ: sketch both curves on 0–2π (solution suggested); triple-angle alternative
        rides P3 — recorded'
      rationale: 'Canonical UGM title: “When is $\sin\theta > \sin 3\theta$?”; exam provenance: UCLES
        A level Pure Mathematics 3, QP 447/3, 1963, Q1(ii)'
      validation_status: SUGGESTED
    title: find all the solutions of simple trigonometrical equations lying in a specified interval (general
      forms of solution are not included).
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Pure Mathematics 3, QP 447/3, 1963, Q1(ii)
task: T-UGM-IMPORT-5
---

# When is $\sin\theta > \sin 3\theta$?

## Question

Determine for what range of values of \(\theta\) between \(0\) and \(2\pi\) \[\sin\theta > \sin 3\theta.\]

## Suggestion

Could we sketch the two curves \(y = \sin \theta\) and \(y = \sin(3\theta)\)?

If \(\sin A=\sin B\), what can we say about \(A\) and \(B\)?

Alternatively, can we express \(\sin 3\theta\) in terms of \(\sin\theta\)?

## Solution

The best thing to do is sketch the two curves \(y=\sin\theta\) and \(y=\sin 3\theta\).

So we get intersections when \[\sin \theta=\sin 3 \theta.\]

Now \[\sin A= \sin B \iff A = B + 2n\pi \quad \text{OR} \quad A= \pi - B + 2n\pi,\] where \(n\) is a whole number.

So here we have \[\theta = 3\theta + 2n\pi \implies \theta = -n\pi \quad \text{OR} \quad \theta = \pi - 3\theta + 2n\pi \implies \theta = \dfrac{(2n+1)\pi}{4}.\]

So the intersection points for \(y = \sin \theta\) and \(y = \sin (3\theta)\) in the given range are \(0, \dfrac{\pi}{4},\dfrac{3\pi}{4},\pi,\dfrac{5\pi}{4},\dfrac{7\pi}{4}, 2\pi.\)

Now looking back at our sketch, we can pinpoint the ranges where

\(\sin\theta > \sin 3 \theta\)

as

\[\begin{align*} \frac{\pi}{4} &< \theta < \frac{3\pi}{4} \\ \pi &< \theta < \frac{5\pi}{4} \\ \frac{7\pi}{4} &< \theta < 2\pi. \end{align*}\]

Alternatively, we could say

\[\sin 3 \theta = \sin (\theta + 2\theta)=\sin\theta\cos (2\theta) +\sin (2 \theta) \cos \theta.\]

That is, we have the equation

\[\begin{align*} \sin \theta &= \sin\theta(1-2\sin^2 \theta) +2\sin \theta \cos^2 \theta \\ &= \sin \theta - 2\sin^3\theta + 2\sin\theta(1-\sin^2 \theta)\\ &= 3\sin\theta - 4\sin^3\theta. \end{align*}\]

Thus we want to solve \[\sin \theta (2\sin^2 \theta -1) =0.\] The first part of the equation, \(\sin\theta = 0\), gives the solutions \(\theta = 0,\pi,2\pi\).

The second part of the equation, \(2\sin^2 \theta -1 =0\), can be rearranged to \(\sin\theta = \pm \dfrac{1}{\sqrt{2}}\), and so gives the solutions \(\theta = \dfrac{\pi}{4},\,\dfrac{3\pi}{4},\,\dfrac{5\pi}{4},\,\dfrac{7\pi}{4}\) in this range.
