---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r6993
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r6993
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6993
  old_site_id: Q83
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
  exam_reference: Oxford University Mathematics Aptitude Test, None, Q1E
task: T-UGM-IMPORT-6
---

# When is $6 \times 7 = 42$ a counter-example?

## Question

The fact that \[6 \times 7 = 42,\] is a counter-example to which of the following statements?

1. the product of any two odd integers is odd;

---

1. if the product of two integers is not a multiple of \(4\) then the integers are not consecutive;

---

1. if the product of two integers is a multiple of \(4\) then the integers are not consecutive;

---

1. any even integer can be written as the product of two even integers.

## Solution

In order to be a [counter-example](https://undergroundmathematics.org/glossary/counterexample) to this statement, a fact would have to involve two odd integers whose product is even.

Since \(6\) is not an odd integer, the fact is not a counter-example to this statement.

In fact, the statement is true, so there *are no* counter-examples.

The number \(42\) is not a multiple of \(4\), but it is the product of two consecutive integers, \(6\) and \(7\), so we have a counter-example, and the statement is not true.

Since \(42\) is not a multiple of \(4\), the fact that \(6 \times 7 = 42\) has no bearing on the truth of this statement.

The statement, however, is clearly false — try \(4 \times 5\).

This statement is clearly false, but to provide a counter-example we would have to show that every factorisation of some even integer includes an odd number.

The fact \(6 \times 7 = 42\) alone is not enough.

But if we listed all the factorisations of \(42\), that’s \[1 \times 42, 2 \times 21, 3 \times 14, 6 \times 7,\] and noted that \(42\) is never the product of two even numbers, this *would* be a counter-example to the statement.

Thus the answer is (b).
