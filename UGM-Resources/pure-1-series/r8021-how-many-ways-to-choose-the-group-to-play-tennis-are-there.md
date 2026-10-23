---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r8021
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r8021
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8021
  old_site_id: null
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
  exam_reference: UCLES O level Additional Mathematics 2, 1970, Q4(i)
task: T-UGM-IMPORT-6
---

# How many ways to choose the group to play tennis are there?

## Question

There are \(10\) people who are going to spend the afternoon in \(2\) groups, one group to go to the theatre and the other to play tennis. In how many ways can the group for tennis be selected if there must be at least \(4\) people in each group?

## Solution

If there must be at least \(4\) people in each group, then the number of people in the group for tennis must be \(4\), \(5\), or \(6\).

There are

\[\begin{equation*} \binom{10}{k} = \frac{10!}{k!(10-k)!} \end{equation*}\]

ways of choosing

\(k\)

people from a group of

\(10\)

, and so there are

\[\begin{align*} \binom{10}{4} + \binom{10}{5} + \binom{10}{6} &= \frac{10!}{4!6!} + \frac{10!}{5!5!} + \frac{10!}{6!4!} \\ &= 2 \times \frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} + \frac{10 \times 9 \times 8 \times 7 \times 6}{5 \times 4 \times 3 \times 2 \times 1} \\ &= 2 \times \frac{10 \times 3 \times 1 \times 7}{1 \times 1 \times 1 \times 1} + \frac{1 \times 3 \times 2 \times 7 \times 6}{1 \times 1 \times 1 \times 1 \times 1} \\ &= 420 + 252 \\ &= 672 \end{align*}\]

ways of choosing the groups.

You may disagree with this. If you think a group of \(5\) going off to play tennis is a bit daft then of course you would get fewer combinations. \[\binom{10}{4} + \binom{10}{6} = \frac{10!}{4!6!} + \frac{10!}{6!4!} = 2 \times \frac{10 \times 9 \times 8 \times 7}{4 \times 3 \times 2 \times 1} = 420\]
