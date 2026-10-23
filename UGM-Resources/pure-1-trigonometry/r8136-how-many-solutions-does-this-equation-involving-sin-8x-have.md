---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r8136
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r8136
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8136
  old_site_id: Q162
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
      evidence: (3+cos x)^2 = 4 − 2sin^8x solution count via sin^2+cos^2=1 and range bounds (sin^8 depth
        recorded)
      rationale: 'Canonical UGM title: “How many solutions does this equation involving $\sin^8x$ have?”;
        exam provenance: Oxford University Mathematics Aptitude Test, 2008, Q1J'
      validation_status: SUGGESTED
    title: use the identities / tan i and cos i sin i + cos i / 1
  - code: 1.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: (3+cos x)^2 = 4 − 2sin^8x solution count via sin^2+cos^2=1 and range bounds (sin^8 depth
        recorded)
      rationale: 'Canonical UGM title: “How many solutions does this equation involving $\sin^8x$ have?”;
        exam provenance: Oxford University Mathematics Aptitude Test, 2008, Q1J'
      validation_status: SUGGESTED
    title: find all the solutions of simple trigonometrical equations lying in a specified interval (general
      forms of solution are not included).
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2008, Q1J
task: T-UGM-IMPORT-5
---

# How many solutions does this equation involving $\sin^8x$ have?

## Question

In the range \(0 \leq x < 2\pi\) the equation \[(3 + \cos x)^2 = 4 - 2\sin^8x\] has

1. \(0\) solutions,

---

1. \(1\) solution,

---

1. \(2\) solutions,

---

1. \(3\) solutions.

## Suggestion

What is the range of values that the left hand side can take?

## Solution

The quickest way to see this is to notice that \[(3+\cos x)^2 \geq (3-1)^2 = 4\] and \[4 - 2\sin^8x \leq 4.\] So there can only be solutions when these hold with equality, i.e. when \(\cos x = -1\) and \(\sin x = 0\). In the range \(0 \leq x < 2\pi\) this only occurs at \(x = \pi\), so the answer is (b).
