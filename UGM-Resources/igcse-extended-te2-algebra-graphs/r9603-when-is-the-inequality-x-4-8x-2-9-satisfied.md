---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/r9603
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/review-question
resource_identity:
  ugm_id: r9603
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9603
  old_site_id: null
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: thinking-about-algebra
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-algebra
    validation_status: SUGGESTED
  spec_points:
  - code: E2.6.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: When is x^4<8x^2+9 satisfied — a quadratic inequality in x^2; E2.6.2 register at stretch.
      rationale: 'Canonical UGM title: “When is the inequality  $x^4<8x^2+9$ satisfied?”; exam provenance:
        Oxford University Mathematics Aptitude Test, 2014, Q1A

        Question reproduced by kind permission of The University of Oxford. The question remains Copyright
        The University of Oxford,

        All rights reserved

        .'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: 'Oxford University Mathematics Aptitude Test, 2014, Q1A

    Question reproduced by kind permission of The University of Oxford. The question remains Copyright
    The University of Oxford,

    All rights reserved

    .'
task: T-UGM-IMPORT-19
---

# When is the inequality  $x^4<8x^2+9$ satisfied?

## Question

The inequality \[x^4<8x^2+9\] is satisfied precisely when \[\text{(a)}-3<x<3 \quad \text{(b)} \quad 0<x<4 \quad \text{(c)} \quad 1<x<3 \quad \text{(d)}-1<x<9 \quad \text{(e)}-3<x<-1.\]

## Suggestion

Could we take all of the terms to one side, and then factorise?

## Solution

We have

\[\begin{align*} x^4<8x^2+9 \\ \iff x^4-8x^2-9&<0 \\ \iff (x^2+1)(x^2-9)&<0 \\ \iff (x^2+1)(x+3)(x-3)&<0. \end{align*}\]

Now \(x^2 + 1\) is always positive, so we are interested in when \((x+3)(x-3)\) is negative.

When \(x < -3\), both brackets are negative, and when \(x > 3\), both brackets are positive.

In between these values, one bracket is negative and one is positive, and so \((x+3)(x-3)\) is negative.

Thus the answer is (a).
