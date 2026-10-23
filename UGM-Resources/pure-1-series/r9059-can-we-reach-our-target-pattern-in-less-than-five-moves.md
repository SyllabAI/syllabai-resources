---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r9059
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r9059
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9059
  old_site_id: Q1057
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
  exam_reference: Oxford University Mathematics Aptitude Test, None, Q7
task: T-UGM-IMPORT-6
---

# Can we reach our target pattern in less than five moves?

## Question

The game of *Oxflip* is for one player and involves circular counters, which are white on one side and black on the other, placed in a grid. During a game, the counters are flipped over (changing between black and white side uppermost) following certain rules.

Given a particular size of grid and a set starting pattern of whites and blacks, the aim of the game is to reach a certain target pattern. Each “move” of the game is to flip over either a whole row or a whole column of counters (so one whole row or column has all its blacks swapped to whites and vice versa). For example, in a game played in a three-by-three square grid, if you are given the starting and target patterns

a sequence of three moves to achieve the target is:

There are many other sequences of moves which also have the same result.

1. Consider the two-by-two version of the game with starting pattern    Draw the eight different target patterns (including the starting pattern) that it is possible to obtain. What are the possible numbers of white counters that may be present in these target patterns?

1. In the four-by-four version of the game, starting with pattern    explain why it is impossible to reach a pattern with only one white counter. [*Hint: don’t try to write out every possible combination of moves.*]

---

1. In the five-by-five game, explain why any sequence of moves which begins    and ends with an all-white pattern, must involve an odd number of moves. What is the least number of moves needed? Give reasons for your answer.

## Suggestion

When a row or a column is flipped, what happens to the number of whites in that row or column?

Again, when a row or a column is flipped, what happens to the number of whites in that row or column?

Can we see how to get to an all-white board? Can we show that it can’t be done in fewer moves?

## Solution

The game of *Oxflip* is for one player and involves circular counters, which are white on one side and black on the other, placed in a grid. During a game, the counters are flipped over (changing between black and white side uppermost) following certain rules.

Given a particular size of grid and a set starting pattern of whites and blacks, the aim of the game is to reach a certain target pattern. Each “move” of the game is to flip over either a whole row or a whole column of counters (so one whole row or column has all its blacks swapped to whites and vice versa). …  For example, in a game played in a three-by-three square grid, if you are given the starting and target patterns <cm-image print-width="270" url="images/image1.png" alt-text="Pattern of 9 counters with 5 black counters being the middle counter and the four corner counters."/> a sequence of three moves to achieve the target is: <cm-image print-width="450" url="images/image2.png" alt-text="Three moves, flipping over the first row of counters so that now 4 black counters remain, flipping over the middle column so that only the bottom row of counters is now black, and flipping the bottom row to leave all counters white."/> There are many other sequences of moves which also have the same result.

1. Consider the two-by-two version of the game with starting pattern    Draw the eight different target patterns (including the starting pattern) that it is possible to obtain.

The possible numbers of white counters are \(0, 2, 4\). Every go starts with an even number of whites, and does not alter the parity (odd or evenness) of the count.

We either turn two whites to two blacks, or two blacks to two whites, or a white and a black to a white and a black.

The starting pattern has an even number of white counters.

Each time a row or column is flipped, the number of whites in that row or column goes from \(i\) to \(4-i\).

This means that if we start with an even number of white counters in the row or column, there’ll still be an even number after flipping.

And similarly, if we start with an odd number, there’ll still be an odd number afterwards. Each flip preserves the parity of the white counters.

Therefore, as we started with an even number of white counters, there can only ever be an even number of white counters, so we can never just have one counter.

When any row or column is flipped, the number of white counters goes from \(i\) to \(5-i\).

So if we start with an even number of whites in a row or column, there’ll be an odd number of whites in that row or column after flipping.

Similarly, if we start with an odd number of whites in a row or column, there’ll be an even number afterwards.

So, as we start with an even number of white counters in total, and our target contains an odd number of white counters in total, there must be an odd number of moves to reach the target.

We can easily see that it is possible to get to an all-white grid in \(5\) moves; for example, we can flip columns \(1, 3, 5\) and then flip rows \(2\) and \(4\).

As we know we need an odd number of moves, to show it can’t be done in less than \(5\) moves, we just need to show that it can’t be done in \(3\).

We can see that we cannot reach all the black counters in only \(3\) moves.

There are a maximum of \(3\) black counters in any row or column, so we can touch at most \(9\) black counters in \(3\) moves, but there are \(13\) black counters altogether.
