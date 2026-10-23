---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r8168
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r8168
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8168
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
  exam_reference: Oxford University Mathematics Aptitude Test, 2014, Q1H
task: T-UGM-IMPORT-6
---

# Given this definition of $F(n)$, can we find the value of $F(6000)$?

## Question

The function

\(F(n)\)

is defined for all positive integers as follows;

\(F(1)=0\)

, and for all

\(n \geq 2\)

,

\[\begin{align*} &F(n) = F(n-1) + 2 \quad\quad\quad\quad \text{if $2$ divides $n$ but $3$ does not divide $n$};\\ &F(n) = F(n-1) + 3 \quad\quad\quad\quad \text{if $3$ divides $n$ but $2$ does not divide $n$};\\ &F(n) = F(n-1) + 4 \quad\quad\quad\quad \text{if $2$ and $3$ both divide $n$};\\ &F(n) = F(n-1) \quad\quad\quad\quad\quad\quad \text{if neither $2$ nor $3$ divides $n$}. \end{align*}\]

The value of \(F(6000)\) equals

\[(a)\quad 9827,\quad(b)\quad 10121,\quad(c)\quad 11000,\quad(d)\quad 12300,\quad(e)\quad 12352.\]

## Suggestion

Can we use the rules to evaluate \(F(n)\) for small \(n\)?

Can we find any pattern in the sequence given by the amounts we add on each time? Might this sequence be periodic?

## Solution

We know \(F(1) = 0\), and using the rules, \(F(2) = 2, F(3)=5, F(4) = 7, F(5) = 7, F(6) = 11\).

Thus as \(n\) travels from \(1\) to \(6\), we add on \(11\) to \(F(n)\).

But now the pattern repeats for \(7\) through to \(12\); we add on \(0\), then \(2\), then \(3\), then \(2\), then \(0\), then \(4\), which is \(11\).

This pattern will repeat for every \(6k+1, 6k+2, 6k+3, 6k+4, 6k+5, 6(k+1)\).

Thus we can split the numbers from \(1\) to \(6000\) into \(1000\) blocks of six, and the total added will be \(11000 = F(6000)\), and so the answer is (c).
