---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r9749
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r9749
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9749
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
  exam_reference: UCLES A level Mathematics 1, 1960, Q2(ii)
task: T-UGM-IMPORT-6
---

# In how many ways can we organise a mixed doubles tennis match?

## Question

A game of tennis, in which one boy and one girl are matched against a similar pair, is to be made up from \(5\) boys and \(3\) girls. In how many ways can this be done? In how many of the games will a specified boy be playing? In how many of the games will he be opposing a second specified boy?

## Solution

There are five ways to choose the first boy.

Once he’s chosen, there are four possible boys left to play against him.

We have three possibilities for the first girl, and two for the second girl.

Thus we appear to have \(5 \times 4 \times 3 \times 2 = 120\) possible matches.

But we must note that the match in which boy \(A\) and girl \(A\) play against boy \(B\) and girl \(B\) is the same as the match where boy \(B\) and girl \(B\) play against boy \(A\) and girl \(A\).

So we counted each match twice above, and therefore we have \(\dfrac{120}{2} = 60\) different ways to organise these matches.

If boy \(A\) is the specified one, then there are four boys left who can play against him.

As before, there are three possibilities for the first girl, and two for the second one.

Note that in this case we don’t count any matches twice, since we’ve chosen the specified boy first. So there are \(4 \times 3 \times 2 = 24\) such matches.

Let’s say boy \(A\) is the first boy, and \(B\) is the second boy.

There are now three possibilities for the first girl, and two for the second. Again, we do not count any match twice here, so there are \(3 \times 2 = 6\) such matches.
