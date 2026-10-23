---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r9491
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r9491
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9491
  old_site_id: Q95
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
      evidence: '2cos^2x + 5sin x = 4 solution count: substitute cos^2x = 1 − sin^2x, solve the quadratic
        in sin'
      rationale: 'Canonical UGM title: “How many solutions does $2 \cos^2x + 5\sin x = 4$ have?”; exam
        provenance: Oxford University Mathematics Aptitude Test, Specimen 1, Q1F'
      validation_status: SUGGESTED
    title: use the identities / tan i and cos i sin i + cos i / 1
  - code: 1.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: '2cos^2x + 5sin x = 4 solution count: substitute cos^2x = 1 − sin^2x, solve the quadratic
        in sin'
      rationale: 'Canonical UGM title: “How many solutions does $2 \cos^2x + 5\sin x = 4$ have?”; exam
        provenance: Oxford University Mathematics Aptitude Test, Specimen 1, Q1F'
      validation_status: SUGGESTED
    title: find all the solutions of simple trigonometrical equations lying in a specified interval (general
      forms of solution are not included).
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, Specimen 1, Q1F
task: T-UGM-IMPORT-5
---

# How many solutions does $2 \cos^2x + 5\sin x = 4$ have?

## Question

How many values of \(x\) satisfy the equation \[2 \cos^2x + 5\sin x = 4\] in the range \(0 \leq x < 2 \pi\)?

1. \(2\),

---

1. \(4\),

---

1. \(6\),

---

1. \(8\).

## Suggestion

Can we rewrite the equation in terms of \(\sin x\) only or \(\cos x\) only?

## Solution

We have

\[\begin{align*} & 2 \cos^2x + 5\sin x = 4 \\ \iff & 2 - 2\sin^2 x + 5 \sin x = 4 \\ \iff & 2\sin^2 x - 5 \sin x + 2 = 0 \\ \iff & (2\sin x - 1)(\sin x - 2) = 0, \end{align*}\]

so \(\sin x = \frac{1}{2}\) (since \(\sin x = 2\) is impossible).

This occurs at \(x = \dfrac{\pi}{6}\) and \(x = \dfrac{5\pi}{6}\) in the given range, so there are \(2\) such values of \(x\) and the answer is (a).
