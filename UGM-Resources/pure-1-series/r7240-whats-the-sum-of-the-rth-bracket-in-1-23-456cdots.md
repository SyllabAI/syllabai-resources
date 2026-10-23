---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r7240
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r7240
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7240
  old_site_id: Q2010
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
  exam_reference: UCLES A level Mathematics A 1, 1975, Q3
task: T-UGM-IMPORT-6
---

# What's the sum of the $r^{th}$ bracket in $(1), (2,3), (4,5,6),\cdots$?

## Question

The positive integers are bracketed as follows: \[(1), (2,3), (4,5,6),\dotsc ,\] where there are \(r\) integers in the \(r^{th}\) bracket.

Find expressions for the first and last integers in the \(r^{th}\) bracket.

Find the sum of all the integers in the first 20 brackets.

Prove that the sum of the integers in the \(r^{th}\) bracket is \(\frac{1}{2}r(r^2+1)\).

*You may assume that the sum of the first \(n\) positive integers is \(\frac{1}{2} n (n+1)\).*

## Suggestion

Can we find a pattern for the starting terms in the brackets? For the finishing terms?

Prove that the sum of the integers in the \(r^{th}\) bracket is \(\dfrac{1}{2}r(r^2+1)\).

Can we use the values for the first and the last integers in the \(r^{th}\) bracket from the first part?

## Solution

Let’s look at the sequence \(u_1, u_2, u_3, \cdots\) formed by the first term in each bracket. This is \[1,2,4,7,11,\cdots\] where the \(r^{th}\) term \(u_r\) is given by \(1+1+2+3+\cdots+(r-1)\).

Using the formula for \(1 + 2 + 3 + \cdots\) given in the questions, we can write this as \[1+ \dfrac{r(r-1)}{2} = \dfrac{r^2-r+2}{2}.\]

*Check: when \(r = 4, \dfrac{r^2-r+2}{2} = 7.\)*

Thus \(u_r = \dfrac{r^2-r+2}{2}\).

The last term in the \(r^{th}\) bracket must be \[\dfrac{r^2-r+2}{2} + r - 1 = \dfrac{r(r+1)}{2}.\]

*Check: when \(r = 3, \dfrac{9+3}{2} = 6\).*

We know the last integer of the \(20^{th}\) bracket is \(\dfrac{20(21)}{2} = 210\).

So to find the sum of the first 20 brackets, we just need to add all positive integers up to \(210\).

This gives us \[\frac{1}{2} {210} (210+1) = 22\, 155.\]

Prove that the sum of the integers in the \(r^{th}\) bracket is \(\dfrac{1}{2}r(r^2+1)\).

The \(r^{th}\) bracket starts with \(\dfrac{r^2-r+2}{2}\) and ends with \(\dfrac{r(r+1)}{2}\).

This is an arithmetic series with \(a = \dfrac{r^2-r+2}{2}, n = r\) and \(d = 1\).

Thus the sum of the terms is \[n\dfrac{1}{2} \text{(first term + last term)} = \dfrac{r}{2}\left(\dfrac{r^2-r+2}{2} + \dfrac{r(r+1)}{2}\right) = \dfrac{r(r^2+1)}{2}.\]
