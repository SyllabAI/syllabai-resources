---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/r6983
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/review-question
resource_identity:
  ugm_id: r6983
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6983
  old_site_id: Q101
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
  - code: E2.4.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: When is this product of powers an integer — fractional/negative index evaluation; E2.4.1
        register.
      rationale: 'Canonical UGM title: “When is this product of powers an integer?”; exam provenance:
        Oxford University Mathematics Aptitude Test, 2007, Q1A

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
  exam_reference: 'Oxford University Mathematics Aptitude Test, 2007, Q1A

    Question reproduced by kind permission of The University of Oxford. The question remains Copyright
    The University of Oxford,

    All rights reserved

    .'
task: T-UGM-IMPORT-19
---

# When is this product of powers an integer?

## Question

*[Choose the one correct answer and explain your reasoning.]*

Let \(r\) and \(s\) be integers. Then \[\frac{6^{r+s}\times12^{r-s}}{8^r\times9^{r+2s}}\] is an integer if

1. \(r+s\le 0\),
2. \(s \le 0\),
3. \(r\le 0\),
4. \(r\ge s\).

## Suggestion

Maybe we could break \(6, 12, 8\) and \(9\) down into their prime factors to rewrite the expression?

## Solution

We have \(6 = 2 \times 3, 12 = 2^2 \times 3, 8 = 2^3\), and \(9 = 3^2\).

If we separate the powers of \(2\) and \(3\), we have \[\frac{6^{r+s}\times12^{r-s}}{8^r\times9^{r+2s}}= \frac{(2\times3)^{r+s}\times(2^2\times3)^{r-s}}{(2^3)^r\times(3^2)^{r+2s}}\] \[= 2^{r+s+2r-2s-3r} \times3^{r+s+r-s-2r-4s}\] \[=2^{-s}\times 3^{-4s}.\]

This is an integer precisely when \(s\le 0\).

So the answer is (b).
