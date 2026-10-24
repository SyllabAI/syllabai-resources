---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r6790
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r6790
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6790
  old_site_id: "Q156"
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
      evidence: "remainder theorem MCQ: the remainder on dividing 1+3x+5x²+…+99x⁴⁹ by x−1 is p(1)=1+3+…+99, summed as an arithmetic progression"
      rationale: "Canonical UGM title: If we divide by $x-1$, the remainder is?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, 2008, Q1D"
  task: T-UGM-IMPORT-9
---

# If we divide by $x-1$, the remainder is?

## Question

When \[1 + 3x + 5x^2 + 7x^3 + \dots + 99x^{49}\] is divided by \(x-1\) the remainder is

1. \(2000\),

---

1. \(2500\),

---

1. \(3000\),

---

1. \(3500\).

## Solution

The remainder theorem tells us that when a polynomial \(p(x)\) is divided by \(x-1\) then the remainder is \(p(1)\), which in this case is \[1 + 3 + 5 + 7 + \dots + 99.\] This is an arithmetic progression, and so sums to \[\frac{1}{2}\times 50(1+99) = 2500\] and the answer is (b).
