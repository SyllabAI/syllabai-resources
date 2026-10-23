---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r9837
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r9837
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9837
  old_site_id: Q130
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
      evidence: 7sin x + 2cos^2x = 5 solution count via sin^2+cos^2=1
      rationale: 'Canonical UGM title: “How many solutions does $7\sin x +2\cos ^2 x =5$ have?”; exam
        provenance: Oxford University Mathematics Aptitude Test, 2007, Q1C'
      validation_status: SUGGESTED
    title: use the identities / tan i and cos i sin i + cos i / 1
  - code: 1.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: 7sin x + 2cos^2x = 5 solution count via sin^2+cos^2=1
      rationale: 'Canonical UGM title: “How many solutions does $7\sin x +2\cos ^2 x =5$ have?”; exam
        provenance: Oxford University Mathematics Aptitude Test, 2007, Q1C'
      validation_status: SUGGESTED
    title: find all the solutions of simple trigonometrical equations lying in a specified interval (general
      forms of solution are not included).
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2007, Q1C
task: T-UGM-IMPORT-5
---

# How many solutions does $7\sin x +2\cos ^2 x =5$ have?

## Question

The number of solutions \(x\) to the equation \[7\sin x +2\cos ^2 x =5,\] in the range \(0\le x<2\pi\), is

1. \(1\),

---

1. \(2\),

---

1. \(3\),

---

1. \(4\).

## Solution

Using the identity

\(\sin^2 x+ \cos^2 x=1\)

we can rewrite the given equation. We have

\[\begin{align*} & 7\sin x +2\cos ^2 x =5\\ \iff & 7\sin x+ 2(1-\sin ^2x) =5\\ \iff & 2\sin ^2x -7\sin x +3 =0\\ \iff & (2\sin x -1)(\sin x-3)=0. \end{align*}\]

So we must have \(\sin x=3\), which has no solutions for real \(x\), or \(2\sin x=1\), that is, \(\sin x=\dfrac{1}{2}\). This has two solutions in the relevant range (namely \(\dfrac{\pi}{6}\) and \(\dfrac{5\pi}{6}\)).

So the answer is (b).
