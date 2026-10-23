---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r9582
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r9582
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9582
  old_site_id: Q161
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: y=2x^3-6x^2+5x-7 stationary-point count via the discriminant of y'=6x^2-12x+5 — canonical
        MC
      rationale: 'Canonical UGM title: "How many stationary points does $y = 2x^3 - 6x^2 + 5x - 7$  have?";
        exam provenance: Oxford University Mathematics Aptitude Test, 2008, Q1A'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2008, Q1A
task: T-UGM-IMPORT-7
---

# How many stationary points does $y = 2x^3 - 6x^2 + 5x - 7$  have?

## Question

The function \[y = 2x^3 - 6x^2 + 5x - 7\] has

1. no stationary points;

---

1. one stationary point;

---

1. two stationary points;

---

1. three stationary points.

## Solution

Differentiating, we find \[y' = 6x^2 - 12x + 5.\]

We could find the roots, but it is quicker just to notice that the discriminant of the quadratic \(y'\) is \(12^2 - 4\times 6\times 5 = 24 > 0\).

This means the equation \(y' = 0\) has two distinct real roots, and hence the answer is (c).
