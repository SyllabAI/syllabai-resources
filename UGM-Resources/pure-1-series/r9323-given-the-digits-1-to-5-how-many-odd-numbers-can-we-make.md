---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r9323
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r9323
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9323
  old_site_id: Q3046
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
  exam_reference: UCLES O level Additional Mathematics 1, 1968, Q1
task: T-UGM-IMPORT-6
---

# Given the digits $1$ to $5$, how many odd numbers can we make?

## Question

The digits \(1\), \(2\), \(3\), \(4\), \(5\) are written down at random to form a five-digit number.

*Note; no digit may be repeated!*

Find:

1. how many such numbers are possible,

---

1. the chance that the last digit is odd,

---

1. how many of the numbers are divisible by 4.

## Suggestion

Can we think of a rule to check whether or not a number is divisible by \(4\)?

Does looking at the last digit work?

## Solution

We have five ways to choose the first digit, and once we’ve done that, four ways of choosing the second, and so on…

So there are \(5! = 120\) possible numbers.

The last digit must be one of \(1, 3\) and \(5\). Once we have chosen this, there are \(4!\) ways to choose the first four digits.

Thus there are \(3 \times 4! = 72\) possible numbers that are odd and the chance that a number is odd is \(\dfrac{72}{120}=\dfrac{3}{5}.\)

Could we have just stated this anyway as \(3\) of our digits were odd?

1. how many of the numbers are divisible by \(4\).

Any five-digit positive integer can be written as \(100a + b\) for positive integers \(100 \le a < 1000\) and \(0 \le b < 100\).

Then we only need to check \(b\) for divisibility by \(4\) because \(100a + b = 4\left(25a + \frac{b}{4}\right)\) which is an integer if \(b\) is a multiple of \(4\).

So the general rule for checking whether or not \(4\) goes into a number is this; does \(4\) go into the final two digits?

If so, then the number is a multiple of \(4\), and not otherwise. (That’s how we check for leap years and the next Summer Olympics.)

The only pairs of digits that could end our number and which are divisible by \(4\) are \(12\), \(24\), \(32\) and \(52\).

Thus, there are \(3! \times 4 = 24\) such numbers.
