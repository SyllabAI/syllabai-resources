---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r8411
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r8411
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8411
  old_site_id: Q147
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Greatest value of (3sin^2(10x+11)-7)^2 by inner->outer bounding — composite-range technique;
        the inner bounds come from P1 1.5.4.
      rationale: 'Canonical UGM title: “When does this trig function have its maximum value?”; exam provenance:
        Oxford (MAT) 2007 Q[''Q1B'']'
      validation_status: SUGGESTED
    title: identify the range of a given function in simple cases, and find the composition of two given
      functions condition that a composite function
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) 2007 Q['Q1B']
task: T-UGM-IMPORT-2
---

# When does this trig function have its maximum value?

## Question

The greatest value which the function \[f(x)=(3\sin^2(10x+11)-7)^2\] takes, as \(x\) varies over all real values, equals

1. \(-9\),
2. \(16\),
3. \(49\),
4. \(100\).

## Solution

We know that \(\sin(10x+11)\) takes values between \(-1\) and \(1\).

So \(\sin^2(10x+11)\) takes values between \(0\) and \(1\)

So \(3\sin^2(10x+11)\) takes values between \(0\) and \(3\)

So \(3\sin^2(10x+11)-7\) takes values between \(-7\) and \(-4\)

So \(f(x)\) takes values between \(49\) and \(16\), and the greatest value which \(f(x)\) takes is \(49\).

The answer is c.
