---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r8468
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r8468
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8468
  old_site_id: "Q3011"
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
      evidence: "remainder theorem squared relation (a²−3)²=f(−a) reduced to 9a²+2a−7=0 and factorised"
      rationale: "Canonical UGM title: If two remainders are related can we find $a$?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES AO level Additional Mathematics 2, QP 8175/2, 1980, Q12(a)"
  task: T-UGM-IMPORT-9
---

# If two remainders are related can we find $a$?

## Question

The remainder when \(x^4 + 3x^2 - 2x + 2\) is divided by \(x + a\) is the square of the remainder when \(x^2 - 3\) is divided by \(x + a\). Calculate the possible values of \(a\).

## Solution

The remainder theorem tells us that if a polynomial \(p(x)\) is divided by \(x-a\), the remainder is \(p(a)\).

So on dividing \(x^2 - 3\) by \(x + a\), we have a remainder of \(a^2-3\).

We also have that if \(f(x) = x^4 + 3x^2 - 2x + 2\) is divided by \(x + a\), the remainder is \(f(-a)=a^4 + 3a^2 + 2a + 2\).

Thus the question tells us that \((a^2-3)^2 = a^4 + 3a^2 + 2a + 2 \implies 9a^2+2a-7=0.\)

Factorising, we have that \((a+1)(9a-7) = 0\), and so the possible values for \(a\) are \(-1\) and \(\dfrac{7}{9}\).
