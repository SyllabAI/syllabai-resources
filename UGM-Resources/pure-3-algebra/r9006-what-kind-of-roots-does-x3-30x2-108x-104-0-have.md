---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r9006
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r9006
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9006
  old_site_id: "Q99"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: polynomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: polynomials
    validation_status: SUGGESTED
  spec_points:
  - code: 3.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "small-integer root search by the factor theorem factorises x³−30x²+108x−104=(x−2)²(x−26) — repeated-root MCQ"
      rationale: "Canonical UGM title: What kind of roots does $x^3 - 30x^2 + 108x - 104 = 0$ have?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, Specimen 1, Q1D"
  task: T-UGM-IMPORT-9
---

# What kind of roots does $x^3 - 30x^2 + 108x - 104 = 0$ have?

## Question

The equation \(x^3 - 30x^2 + 108x - 104 = 0\) has

1. no real roots;

---

1. exactly one real root;

---

1. three distinct real roots;

---

1. a repeated root.

## Suggestion

What does the Factor Theorem tell us? Could we try using small integers to find one factor?

## Solution

Let \(f(x) = x^3 - 30x^2 + 108x - 104\).

By searching for small integer solutions, we find that \[f(2) = 8 - 120 + 216 - 104 = 0,\] so \((x - 2)\) is a factor of \(f(x)\). Then we can factorise completely to find \[f(x) = (x - 2)(x^2 - 28x + 52) = (x - 2)(x - 2)(x - 26),\] so \(f(x)\) has a repeated root and the answer is (d).
