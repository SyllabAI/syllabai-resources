---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r8998
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r8998
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8998
  old_site_id: Q118
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
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2009, Q1D
task: T-UGM-IMPORT-6
---

# When does $1-2+3-4+5-\cdots +(-1)^{n+1}n$ reach $100$?

## Question

The smallest possible integer \(n\) such that \[1-2+3-4+5-6+\cdots +(-1)^{n+1}n \geq 100\] is

1. \(99\),

---

1. \(101\),

---

1. \(199\),

---

1. \(300\).

## Suggestion

What is the sum of the terms of the sequence when \(n=1\)?

What about when \(n=2\)? \(n=3\)? \(n=4\)?

When will this sum reach \(100\)?

Or… what is the sum of the first \(2n\) terms of the sequence?

## Solution

**Approach 1**

What’s the result of this sum after \(n\) steps? We get the sequence

\[1, -1, 2, -2, 3, -3, \cdots.\]

When do we first reach \(100\) in this sequence?

Clearly the \(199^{th}\) term will be the first one to give at least \(100\), so the answer is (c).

**Approach 2**

Looking at \((1-2)+(3-4)+(5-6)+\cdots\), we see that the sum of the first \(2n\) terms is \(-n\).

So adding the next term, we require \((2n+1) -n = 100\), which gives \(n = 99\).

Thus \(2n+1 = 199\), so the answer is (c).
