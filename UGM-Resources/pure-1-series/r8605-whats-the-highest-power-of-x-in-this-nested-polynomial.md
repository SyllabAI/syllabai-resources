---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r8605
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r8605
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8605
  old_site_id: Q137
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: counting-and-binomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: counting-and-binomials
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2008, Q1E
task: T-UGM-IMPORT-6
---

# What's the highest power of $x$ in this nested polynomial?

## Question

The highest power of \(x\) in \[\left\{\left[(2x^6+7)^3+(3x^8-12)^4\right]^5 + \left[(3x^5-12x^2)^5+(x^7+6)^4\right]^6\right\}^3\] is

1. \(x^{424}\),

---

1. \(x^{450}\),

---

1. \(x^{500}\),

---

1. \(x^{504}\).

## Suggestion

What is the highest power of \(x\) in \((2x^6+7)^3\)? Can we do the same for the other terms?

## Solution

The highest power of \(x\) in \((2x^6 + 7)^3\) is \(x^{18}\), and in \((3x^8 - 12)^4\) is \(x^{32}\), so in the first square bracket the highest power is \((x^{32})^5 = x^{160}\).

Similarly, the highest power of \(x\) in \((3x^5 - 12x^2)^5\) is \(x^{25}\), and in \((x^7 + 6)^4\) is \(x^{28}\), so in the second square bracket the highest power is \((x^{28})^6 = x^{168}\).

So overall, the highest power of \(x\) in the expansion is \((x^{168})^3 = x^{504}\), and the answer is (d).
