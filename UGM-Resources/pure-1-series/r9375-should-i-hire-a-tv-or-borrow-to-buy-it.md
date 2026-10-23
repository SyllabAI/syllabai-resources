---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r9375
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r9375
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9375
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
      evidence: TV-hire payments form a GP (r=4/5) — total over 8 years vs compound-interest debt —
        applied GP modelling
      rationale: 'Canonical UGM title: "Should I hire a TV or borrow to buy it?"; exam provenance: O&C
        O level MEI Additional Mathematics 1, 1974, Q9'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: O&C O level MEI Additional Mathematics 1, 1974, Q9
task: T-UGM-IMPORT-6
---

# Should I hire a TV or borrow to buy it?

## Question

A colour television set is hired for \(£80\) in the first year. In each subsequent year the charge is four-fifth of the charge in the previous year. Write down the first four terms of a geometric progression of payments made in successive years, without working them out individually. Calculate the total paid over 8 years by the hirer to the nearest \(£\).

If instead he had borrowed \(£200\) to buy the set outright and this debt had accumulated at \(10\%\) compound interest, what total sum to the nearest \(£\) would be owing after 8 years?

## Suggestion

How can we sum the terms of a geomtric progression? Is there a formula we can use?

Can we write down how much is owed at the end of year 1? At the end of year 2?

## Solution

For simplicity we drop all units as we work and keep in mind that costs are in \(£\) and times in years.

The first four payments are \(80, 80 \times \dfrac{4}{5}, 80 \times \left(\dfrac{4}{5}\right)^2, 80 \times \left(\dfrac{4}{5}\right)^3.\)

These form the first four terms of a geometric progression, with \(a = 80,\) and \(r = \dfrac{4}{5}.\)

The sum of the first \(n\) terms of a geometric progression is \(S_n = \dfrac{a(1-r^n)}{1-r}\).

We need \(S_8 = \dfrac{80(1-0.8^8)}{1-0.8} = £333\) (to the nearest pound).

At the start, he owes \(200\). After one year, he owes \(200 \times 1.1\) (an increase of \(10\) per cent). After \(n\) years, he owes \(200 \times 1.1^n.\)

Thus after eight years, he owes \(200 \times 1.1^8 = £429\) (to the nearest pound).

The question doesn’t tell us that the hirer owns the set after eight years, so which option is the best value is moot!
