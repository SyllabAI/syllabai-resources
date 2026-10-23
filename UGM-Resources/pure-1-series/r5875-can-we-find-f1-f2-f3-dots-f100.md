---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r5875
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r5875
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5875
  old_site_id: Q244
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2013, Q1I
task: T-UGM-IMPORT-6
---

# Can we find $F(1) + F(2) + F(3) + \dots + F(100)$?

## Question

The function \(F(k)\) is defined for positive integers by \(F(1)=1\), \(F(2)=1\), \(F(3)=-1\) and by the identities \[F(2k)=F(k), \qquad F(2k+1)=F(k)\] for \(k \ge 2\). The sum \[F(1) + F(2) + F(3) + \dots + F(100)\] equals

1. \(-15\);

---

1. \(28\);

---

1. \(64\);

---

1. \(81\).

## Solution

It is easiest here to think of \(F(1)\), \(F(2)\), … as a sequence.

The recursion rules \(F(2k) = F(k)\) and \(F(2k+1) = F(k)\) mean that the \(k\)th value gets repeated at the consecutive positions \(2k\) and \(2k+1\). Given the starting values, this means the values of \(F(k)\), when listed in sequence, are \[1,1,-1,\underbrace{1,1}_{\times 2},\underbrace{-1,-1}_{\times 2}, \underbrace{1,1,1,1}_{\times 4},\underbrace{-1,-1,-1,-1}_{\times 4}, \underbrace{1,1,1,1,1,1,1,1}_{\times 8},-1,-1,\dots\] (where the numbers underneath indicate how many repeated numbers appear in the block).

The strings of \(-1\)s end at positions \(3\), \(7\), \(15\), \(31\), …, so if the first \(3\) or first \(7\) or first \(15\) or … terms are added, the sum will be equal to \(1\), as all \(+1\)s and \(-1\)s will cancel out except the first \(1\).

Continuing in this manner, we find that the sum of the first \(127\) terms is equal to \(1\). The last \(32\) terms, and in particular \(F(101)\) to \(F(127)\), are all \(-1\)s. So \[F(1)+F(2)+F(3)+\dots +F(100)+ \underbrace{F(101) + \dots + F(127)}_{\text{all $-1$s}} = 1\] giving \[F(1)+F(2)+F(3)+\dots +F(100) = 1-(-27)=28.\]

Alternatively, the sum of the first \(63\) terms is \(1\), the next \(32\) terms (up to \(F(95)\)) are \(+1\), and the final \(5\) terms are \(-1\), so the total is \(1+32-5=28\).

Hence the answer is (b).
