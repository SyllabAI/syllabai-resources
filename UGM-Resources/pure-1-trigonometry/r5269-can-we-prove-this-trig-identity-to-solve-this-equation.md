---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r5269
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r5269
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5269
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
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: prove sinA/(1+cosA) + (1+cosA)/sinA = 2/sinA using sin^2+cos^2=1, then solve the resulting
        equation in 0°–360°
      rationale: 'Canonical UGM title: “Can we prove this trig identity to solve this equation?”; exam
        provenance: O&C O level Additional Mathematics 1, 1967, Q3'
      validation_status: SUGGESTED
      primaryPick: true
    title: use the identities / tan i and cos i sin i + cos i / 1
  - code: 1.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: prove sinA/(1+cosA) + (1+cosA)/sinA = 2/sinA using sin^2+cos^2=1, then solve the resulting
        equation in 0°–360°
      rationale: 'Canonical UGM title: “Can we prove this trig identity to solve this equation?”; exam
        provenance: O&C O level Additional Mathematics 1, 1967, Q3'
      validation_status: SUGGESTED
    title: find all the solutions of simple trigonometrical equations lying in a specified interval (general
      forms of solution are not included).
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: O&C O level Additional Mathematics 1, 1967, Q3
task: T-UGM-IMPORT-5
---

# Can we prove this trig identity to solve this equation?

## Question

1. Prove that \[\frac{\sin A}{1 + \cos A} + \frac{1 + \cos A}{\sin A} = \frac{2}{\sin A}\] for all values of \(A\).

---

1. Find the values of \(x\) between \(0^\circ\) and \(360^\circ\) if \[\frac{\sin x}{1 + \cos x} + \frac{1 + \cos x}{\sin x} = 1 + 3 \sin x.\]

## Solution

We will begin by writing the left-hand side as a single fraction.

\[\begin{align*} \frac{\sin A}{1 + \cos A} + \frac{1 + \cos A}{\sin A} &= \frac{\sin^2 A + (1 + \cos A)^2}{(1 + \cos A)\sin A} \\ &= \frac{\sin^2 A + 1 + 2 \cos A + \cos^2 A}{(1 + \cos A)\sin A}. \end{align*}\]

For any

\(A\)

, we have the trigonometric identity

\[ \sin^2 A + \cos^2 A = 1 \]

and so we can write

\[\begin{align*} \frac{\sin^2 A + 1 + 2 \cos A + \cos^2 A}{(1 + \cos A)\sin A} &= \frac{2 + 2 \cos A}{(1 + \cos A)\sin A} \\ &= \frac{2(1 + \cos A)}{(1 + \cos A)\sin A} \\ &= \frac{2}{\sin A} \end{align*}\]

as we had hoped to show.

From the previous part of the question, \(x\) satisfies \[\frac{\sin x}{1 + \cos x} + \frac{1 + \cos x}{\sin x} = 1 + 3 \sin x.\] exactly when \[\frac{2}{\sin x} = 1 + 3 \sin x.\] Since this never holds when \(\sin x = 0\), we can multiply through by \(\sin x\) and rearrange to produce \[3 \sin^2 x + \sin x - 2 = 0.\] This is a quadratic equation in \(\sin x\); we can factorise it as \[(3 \sin x - 2)(\sin x + 1) = 0.\] Thus \(x\) satisfies the original equation given in the question exactly when \[\sin x = -1 \quad\text{or}\quad \sin x = \frac{2}{3}.\]

The unique solution to the first of these possibilities with \(0^\circ \le x \le 360^\circ\) is \(x = 270^\circ\).

The second possibility gives two solutions with \(0^\circ \le x \le 360^\circ\).

We have \(\sin^{-1} \left( \dfrac{2}{3} \right)\), which lies between \(0^\circ\) and \(90^\circ\), and \(180^\circ - \sin^{-1} \left( \dfrac{2}{3} \right)\), which lies between \(90^\circ\) and \(180^\circ\).

So there are three possible solutions in total, \(41.8^\circ, 138.2^\circ\), and \(270^\circ\).
