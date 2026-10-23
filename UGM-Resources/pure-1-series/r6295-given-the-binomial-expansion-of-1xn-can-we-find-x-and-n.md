---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r6295
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r6295
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6295
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
  exam_reference: UCLES O level Additional Mathematics 1, 1971, Q7(i)
task: T-UGM-IMPORT-6
---

# Given the binomial expansion of $(1+x)^n$, can we find $x$ and $n$?

## Question

The binomial expansion of \((1+x)^n\) is

\[1-\dfrac{1}{2}\times \dfrac{1}{3} + \dfrac{\frac{1}{2}\times\frac{3}{2}}{1\times 2}\left(\dfrac{1}{3}\right)^2- \dfrac{\frac{1}{2}\times\frac{3}{2}\times\frac{5}{2}}{1\times 2\times 3}\left(\dfrac{1}{3}\right)^3+...\]

Determine the values of \(x\) and \(n\).

## Suggestion

The binomial expansion of \((1+x)^n\) is

\[1-\dfrac{2}{3}\times \dfrac{1}{3} + \dfrac{\frac{1}{2}\times\frac{3}{2}}{1\times 2}\left(\dfrac{1}{3}\right)^2- \dfrac{\frac{1}{2}\times\frac{3}{2}\times\frac{5}{2}}{1\times 2\times 3}\left(\dfrac{1}{3}\right)^3+...\]

Determine the values of \(x\) and \(n\).

Could we write out the expansion of \((1+x)^n\) and compare the terms with what we are given?

## Solution

We can write down the binomial expansion of \((1+x)^n\) as

\[1+\dfrac{n}{1!}x + \dfrac{n(n-1)}{2!}x^2+ \dfrac{n(n-1)(n-2)}{3!}x^3+...\]

This is true for all real values of \(n\), although there are conditions on \(x\).

If \(n\) is a positive integer, the expansion terminates, while if \(n\) is negative or not an integer (or both), we have an infinite series that is valid if and only if \(\big \vert x \big \vert < 1\).

We can now compare this with the series we are given. The increasing powers of \(\dfrac{1}{3}\) strongly suggest that \(x = \dfrac{1}{3}\).

What can we now say about \(n\)? If we look at the \(x^2\) term, we need \(\dfrac{1}{2}\times\dfrac{3}{2} = n(n-1)\). The only ways this can happen are if \(n = -\dfrac{1}{2}\) or \(n = \dfrac{3}{2}\).

The \(x^3\) term tells us \(-\dfrac{1}{2}\times\dfrac{3}{2}\times\dfrac{5}{2} = n(n-1)(n-2)\), which must mean \(n = -\dfrac{1}{2}\).

We can easily check that this provides the other terms of the series successfully.

Thus \(x = \dfrac{1}{3}, n = -\dfrac{1}{2}\).
