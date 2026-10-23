---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r7399
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r7399
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7399
  old_site_id: Q154
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2008, Q1I
task: T-UGM-IMPORT-6
---

# What do we get if we add the digits of the integers from 1 to 99?

## Question

The function \(S(n)\) is defined for positive integers \(n\) by \[S(n) = \text{sum of the digits of }n.\] For example, \(S(723) = 7+2+3=12\). The sum \[S(1) + S(2) + S(3) + \dots + S(99)\] equals

1. \(746\),

---

1. \(862\),

---

1. \(900\),

---

1. \(924\).

## Suggestion

Could we lay out the \(S\) values in a table?

How often does the digit \(1\) appear in the numbers from \(1\) to \(99\)?

What about the other digits?

## Solution

**Approach 1**

We can lay out the digits we have to add in a table and then add up each column.

| \(0+0\) | \(0+1\) | \(0+2\) | \(0+3\) | \(\dots\) | \(0+9\) |
|---|---|---|---|---|---|
| \(1+0\) | \(1+1\) | \(1+2\) | \(1+3\) | \(\dots\) | \(1+9\) |
| \(2+0\) | \(2+1\) | \(2+2\) | \(2+3\) | \(\dots\) | \(2+9\) |
| \(\dots\) | \(\dots\) | \(\dots\) | \(\dots\) | \(\dots\) | \(\dots\) |
| \(9+0\) | \(9+1\) | \(9+2\) | \(9+3\) | \(\dots\) | \(9+9\) |
| \(1+2+\dots+9=45\) | \(45+10\times1\) | \(45+10\times2\) | \(45+10\times3\) | \(\dots\) | \(45+10\times9\) |

Adding up the column totals we have \[45\times10 + 10\times1 + 10\times2 +\dots+10\times9 = 45\times10+10\times45 = 900\] so the answer is (c).

**Approach 2**

Since zeroes do not contribute to the sum, we can rewrite this as \[S(1) + S(2) + S(3) + \dots + S(99) = S(00) + S(01) + \dots + S(99).\]

Then in the \(100\) two-digit numbers \(00, \dots, 99\), each digit \(0,\dots ,9\) appears \(20\) times (\(10\) times as the first digit, \(10\) times as the second).

So \[S(1) + S(2) + S(3) + \dots + S(99) = 20 \times (0 + 1 + \dots + 9) = 20 \times 10 \times \frac{(0 + 9)}{2} = 900,\] and the answer is (c).
