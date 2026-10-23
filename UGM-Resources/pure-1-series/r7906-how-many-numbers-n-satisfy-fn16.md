---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r7906
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r7906
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7906
  old_site_id: Q169
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2010, Q1G
task: T-UGM-IMPORT-6
---

# How many numbers $n$ satisfy $f(n)=16$?

## Question

The function \(f\), defined for whole positive numbers, satisfies \(f(1)=1\) and also the rules \[f(2n)=2f(n),\] \[f(2n+1)=4f(n),\] for all values of \(n\). How many numbers \(n\) satisfy \(f(n)=16\)?

1. \(3\),

---

1. \(4\),

---

1. \(5\),

---

1. \(6\).

## Solution

To begin with, we could calculate the first few terms: \(f(1)=1\), \(f(2)=2\), \(f(3)=2\), \(f(4)=4\). Is there a pattern? Not an obvious one.

It’s a help to ask how 16 factorises. We can do this using only the factors of \(2\) and \(4\) in \(5\) different ways, where the order matters, namely

1. \(2\times 2\times 2\times 2\),

---

1. \(4\times 2\times 2\),

---

1. \(2\times 4\times 2\),

---

1. \(2\times 2\times 4\) and

---

1. \(4\times 4\).

To which values of \(n\) do these correspond?

1. corresponds to applying the first rule, namely \(f(2n)=2f(n)\), four times, giving \(n=2\times 2\times 2\times 2\times 1=16\) (the sequence of \(n\) values is \(1-2-4-8-16\)).

---

1. corresponds to applying the second rule once, followed by the first one twice, giving \(n=2(2\times2\times1)+1=9\) (the sequence is \(1-2-4-9\)).

---

1. corresponds to applying the first rule, the second rule, and then the first one again, giving \(n=2[2(2\times1)+1)]=10\) (the sequence is \(1-2-5-10\)).

---

1. corresponds to applying the first one twice, followed by the second one once, giving \(n=2\times2\times[2(1)+1]=12\) (the sequence is \(1-3-6-12\)).

---

1. corresponds to applying the second rule twice, giving \(n=2[2(1)+1]+1=7\) (the sequence is \(1-3-7\)).

Therefore we can have \(f(n)=16\) for \(5\) different values of \(n\), and the answer is (c).

Alternatively, we can find \(f(n)\) for \(n = 1\) to \(16\), and notice that \(f(n) \geq 16\) for \(n = 8\) to \(16\).

This means that \(f(n) > 16\) for \(n = 17\) to \(32\), since applying the first rule to one of these numbers \(n\) gives \(f(n)\) to be at least \(32\), and applying the second rule gives \(f(n)\) to be at least \(64\).

We can extend this argument naturally to show \(f(n) > 16\) for all \(n > 16\), and so there are just five values of \(n\) where \(f(n) = 16\). The answer is (c).
