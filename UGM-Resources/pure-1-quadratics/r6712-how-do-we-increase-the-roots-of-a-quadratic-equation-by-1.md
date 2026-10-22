---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r6712
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r6712
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6712
  old_site_id: Q4032
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: 'Shift roots by 1: substitution y = x - 1, expansion and comparison.'
      rationale: 'Canonical UGM title: “How do we increase the roots of a quadratic equation by $1$?”;
        exam provenance: UCLES 1962 Q7(i)'
      validation_status: SUGGESTED
    title: solve quadratic equations, and quadratic By factorising, completing the square and using the
      inequalities, in one unknown formula.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1962 Q7(i)
task: T-UGM-IMPORT-1
---

# How do we increase the roots of a quadratic equation by $1$?

## Question

If \(\alpha\) and \(\beta\) are the roots of the equation \[2x^2+3x+2 = 0,\] find the equation whose roots are \(\alpha+1\) and \(\beta+1\).

## Suggestion

Can we solve this problem without computing \(\alpha\) and \(\beta\) explicitly?

## Solution

If \(y = f(x)\) has roots \(\alpha\) and \(\beta\), then we can find a function with roots \(\alpha+1\) and \(\beta+1\) by translating this \(1\) unit to the right.

Thus \(y = f(x-1)\) will have roots \(\alpha + 1\), \(\beta + 1\).

So the equation we seek is \(2(x-1)^2 +3(x-1) +2 =0\), or \(2x^2-x+1=0\).

It is interesting to note that this works, even though the roots of the original equation are [complex](https://undergroundmathematics.org/glossary/complex)!
