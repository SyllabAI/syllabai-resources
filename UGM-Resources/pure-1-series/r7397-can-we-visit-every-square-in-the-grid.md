---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r7397
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r7397
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7397
  old_site_id: Q180
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2009, Q5
task: T-UGM-IMPORT-6
---

# Can we visit every square in the grid?

## Question

Given an \(n\times n\) grid of squares, where \(n>1\), a *tour* is a path drawn within the grid such that:

- along its way the path moves, horizontally or vertically, from the centre of one square to the centre of an adjacent square;

- the path starts and finishes in the same square;

- the path visits the centre of every other square just once.

For example, below is a tour drawn in a \(6\times6\) grid of squares which starts and finishes in the top-left square.

For parts (i)-(iv) it is assumed that \(n\) is *even*.

1. With the aid of a diagram, show how a tour, which starts and finishes in the top-left square, can be drawn in any \(n\times n\) grid.

---

1. Is a tour still possible if the start/finish point is changed to the centre of a different square? Justify your answer.

Suppose now that a robot is programmed to move along a tour of an \(n\times n\) grid. The robot understands two commands.

- command \(R\) which turns the robot clockwise through a right angle;

- command \(F\) which moves the robot forward to the centre of the next square.

The robot has a program, a list of commands, which it performs in the given order to complete a tour; say that, in total, command \(R\) appears \(r\) times in the program and command \(F\) appears \(f\) times.

1. Initially the robot is in the top-left square pointing to the right. Assuming the first command is an \(F\), what is the value of \(f\)? Explain also why \(r+1\) is a multiple of \(4\).

---

1. Must the results of part (iii) still hold if the robot starts and finishes at the centre of a different square? Explain your reasoning.

---

1. Show that a tour of an \(n \times n\) grid is not possible when \(n\) is odd.

## Solution

Given an \(n\times n\) grid of squares, where \(n>1\), a *tour* is a path drawn within the grid such that:

- along its way the path moves, horizontally of vertically, from the centre of one square to the centre of an adjacent square;

- the path starts and finishes in the same square;

- the path visits the centre of every other square just once.

For example, below is a tour drawn in a \(6\times6\) grid of squares which starts and finishes in the top-left square.

For parts (i)–(iv) it is assumed that \(n\) is *even*.

1. With the aid of a diagram, show how a tour, which starts and finishes in the top-left square, can be drawn in any \(n\times n\) grid.

From the top-left corner we go to the right until we reach the end of the row, go one square down and then left until we reach the second column.

We then go down another square and continue this pattern until we reach the bottom row. As the number of rows is even we will complete the bottom row at its left hand end. We now go up the left hand column to return to the top-left square.

An example of this algorithm for \(n=8\) is shown below.

Yes. Following the same path as above, a tour starting from a different square is still possible.

It starts from that square and repeats the path until reaching the top-left corner, and continues until reaching the starting point.

Since the tour passes through every square, then this is possible for any square.

Suppose now that a robot is programmed to move along a tour of an \(n \times n\) grid. The robot understands two commands.

- command \(R\) which turns the robot clockwise through a right angle;

- command \(F\) which moves the robot forward to the centre of the next square.

The robot has a program, a list of commands, which it performs in the given order to complete a tour; say that, in total, command \(R\) appears \(r\) times in the program and command \(F\) appears \(f\) times.

1. Initially the robot is in the top-left square pointing to the right. Assuming the first command is an \(F\), what is the value of \(f\)? Explain also why \(r+1\) is a multiple of \(4\).

The robot must visit each square exactly once, and each command \(F\) makes the robot move to a new square. It starts in a square so will have visited each square in the grid after \(n^2-1\) \(F\) commands, but to complete the tour it must make one more move back into the starting square. Therefore, \(f=n^2\).

The robot starts by moving East and its tour must finish by moving North from the square below the start. It will have turned clockwise through three right angles plus some number of complete turns. Therefore, \(r\) is \(3\) plus a multiple of \(4\). Hence \(r+1\) is a multiple of \(4\).

Regardless of where it starts, the robot must still visit each square once, so we still have \(f=n^2\), but \(r\) might be different.

For instance, if we start part way along the first row, the robot could start and finish facing East, in which case it will have made a whole number of full turns.

In this case, \(r\) is a multiple of four.

In order to be back at the starting point, the robot has to move the same number of squares up and down, and the same number of squares left and right.

Therefore the number of squares has to be even.

But, when \(n\) is odd the number of squares, \(n^2\), will be an odd number.

So if \(n\) is odd, the robot cannot get back to the original square.
