---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r6138
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r6138
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6138
  old_site_id: Q155
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
      evidence: 'sin^2x + 3sinx cosx + 2cos^2x = 0 solution count: divide by cos^2x, use tan x = sin x/cos
        x, solve the quadratic in tan'
      rationale: 'Canonical UGM title: “How many solutions does $\sin^2x+3\sin x\cos x+2\cos^2 x=0$ have?”;
        exam provenance: Oxford University Mathematics Aptitude Test, 2010, Q1C'
      validation_status: SUGGESTED
    title: use the identities / tan i and cos i sin i + cos i / 1
  - code: 1.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: 'sin^2x + 3sinx cosx + 2cos^2x = 0 solution count: divide by cos^2x, use tan x = sin x/cos
        x, solve the quadratic in tan'
      rationale: 'Canonical UGM title: “How many solutions does $\sin^2x+3\sin x\cos x+2\cos^2 x=0$ have?”;
        exam provenance: Oxford University Mathematics Aptitude Test, 2010, Q1C'
      validation_status: SUGGESTED
      primaryPick: true
    title: find all the solutions of simple trigonometrical equations lying in a specified interval (general
      forms of solution are not included).
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2010, Q1C
task: T-UGM-IMPORT-5
---

# How many solutions does $\sin^2x+3\sin x\cos x+2\cos^2 x=0$ have?

## Question

In the range \(0\leq x<2\pi\), the equation \[\sin^2x+3\sin x\cos x+2\cos^2 x=0\] has

1. \(1\) solution,

---

1. \(2\) solutions,

---

1. \(3\) solutions,

---

1. \(4\) solutions.

## Solution

If \(\cos x = 0, \sin x \neq 0\), so the equation does not hold. Thus we are free to divide by \(\cos^2x\), since it must be non-zero, giving \[\tan^2x + 3\tan x + 2=0,\]

which factorises into \[(\tan x +1)(\tan x +2 ) = 0.\]

So our solutions will be those for \(\tan x = -1, \tan x = -2.\)

Since \(y=\tan x\) has a period of \(\pi\), there will therefore be four solutions in total, which means the answer is (d).
