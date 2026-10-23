---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r9770
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r9770
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9770
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-triangles-to-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-triangles-to-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.5.4
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: 'half-disc regions with −cosθ ≤ x ≤ sinθ: area comparison powered by (sinθ−cosθ)^2; the
        rational sketch rides 1.2 and the optimisation extension 1.7 — recorded'
      rationale: 'Canonical UGM title: “As $\theta$ varies, what''s the largest this ratio of areas can
        be?”; exam provenance: Oxford University Mathematics Aptitude Test, 2013, Q4'
      validation_status: SUGGESTED
    title: use the identities / tan i and cos i sin i + cos i / 1
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2013, Q4
task: T-UGM-IMPORT-5
---

# As $\theta$ varies, what's the largest this ratio of areas can be?

## Question

1. Let \(a > 0\). Sketch the graph of \[y=\dfrac{a+x}{a-x} \quad \text{for} \quad -a < x < a.\]

---

1. Let \(0 < \theta < \dfrac{\pi}{2}\). In the diagram below is the half-disc given by \(x^2 + y^2 \leq 1\) and \(y \geq 0\). The shaded region \(A\) consists of those points with \(-\cos \theta \leq x \leq \sin \theta\). The region \(B\) is the remainder of the half-disc. Find the area of \(A\).

---

1. Assuming *only* that \(\sin^2\theta + \cos^2\theta = 1\), show that \(\sin\theta\cos\theta \leq \dfrac{1}{2}\).

---

1. What is the largest \(\dfrac{\text{area of } A}{\text{area of } B}\) can be, as \(\theta\) varies?

## Suggestion

Are there any noticeable features of this function over this interval?

Can we divide the area \(A\) into regions where we can easily calculate the areas?

Would it help to consider \((\sin\theta-\cos\theta)^2\)?

How does our work for (i) help us here?

## Solution

Now \(y=\dfrac{a+x}{a-x} = \dfrac{2a-(a-x)}{a-x} = \dfrac{2a}{a-x}-1\), so as \(x\) increases from \(-a\) towards \(a, y\) increases from \(0\) towards \(\infty\). Also \((0,1)\) is on the curve.

If we use calculus, \(\dfrac{dy}{dx} = \dfrac{2a}{(a-x)^2} > 0\), and so this function is always increasing (with a discontinuity at \(x = a\)).

We can see from the diagram that A consists of a quarter of the circle with two additional congruent triangles.

Thus the area \(A = \dfrac{\pi}{4}+2\left[\dfrac{1}{2}\sin\theta\cos\theta\right] = \dfrac{\pi}{4}+\sin\theta\cos\theta\).

We know that \(0\leq (\sin\theta-\cos\theta)^2 = \sin^2\theta + \cos^2\theta - 2\sin\theta\cos\theta.\)

Thus \(2\sin\theta\cos\theta \leq \sin^2\theta + \cos^2\theta = 1 \implies \sin\theta\cos\theta \leq \dfrac{1}{2}.\)

We know \(\dfrac{\text{area of } A}{\text{area of } B} = \dfrac{\dfrac{\pi}{4}+\sin\theta\cos\theta}{\dfrac{\pi}{2}-\left(\dfrac{\pi}{4}+\sin\theta\cos\theta\right)}= \dfrac{\dfrac{\pi}{4}+\sin\theta\cos\theta}{\dfrac{\pi}{4}-\sin\theta\cos\theta}\).

Now from part (i), we know that \(\dfrac{\dfrac{\pi}{4}+\sin\theta\cos\theta}{\dfrac{\pi}{4}-\sin\theta\cos\theta}\) increases as \(\sin\theta\cos\theta\) increases.

But the maximum value \(\sin\theta\cos\theta\) can take is \(\dfrac{1}{2}\), and so the maximum value of \(\dfrac{\dfrac{\pi}{4}+\sin\theta\cos\theta}{\dfrac{\pi}{4}-\sin\theta\cos\theta}\) is \(\dfrac{\dfrac{\pi}{4}+\dfrac{1}{2}}{\dfrac{\pi}{4}-\dfrac{1}{2}} = \dfrac{\pi+2}{\pi-2}\).
