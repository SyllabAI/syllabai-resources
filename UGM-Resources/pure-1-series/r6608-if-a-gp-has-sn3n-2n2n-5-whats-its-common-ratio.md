---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r6608
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r6608
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6608
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: sequences
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: sequences
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: S_n=(3^n-2^n)/2^{n-5} — find first term and common ratio — canonical GP-sum-formula
        problem
      rationale: 'Canonical UGM title: "If a GP has $S_n=(3^n - 2^n)/2^{n-5}$, what''s its common ratio?";
        exam provenance: O&C O level Additional Mathematics 2, 1967, Q1(ii)'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: O&C O level Additional Mathematics 2, 1967, Q1(ii)
task: T-UGM-IMPORT-6
---

# If a GP has $S_n=(3^n - 2^n)/2^{n-5}$, what's its common ratio?

## Question

For all values of \(n\) the sum of \(n\) terms of a geometrical progression is \(\dfrac{3^n - 2^n}{2^{n-5}}\). Find its first term and common ratio.

## Solution

A geometric progression takes the form \(a, ar, ar^2, \dotsc\), where \(a\) is the first term and \(r\) is the common ratio. We are told that, for each \(n \ge 1\), \[a + ar + \dotsb + ar^{n-1} = \frac{3^n - 2^n}{2^{n-5}}.\]

When \(n = 1\), this becomes \[a = \frac{3^1 - 2^1}{2^{1-5}} = \frac{3 - 2}{2^{-4}} = 1 \times 2^4 = 16.\]

When \(n = 2\), this becomes

\[a + ar = \frac{3^2 - 2^2}{2^{2-5}} \implies 16 + 16r = \frac{9 - 4}{2^{-3}} = 5 \times 2^3 = 40.\]

Thus the second term \(ar = 40 - 16 = 24\), which means that \(r = \dfrac{24}{16} = \dfrac{3}{2}\).
