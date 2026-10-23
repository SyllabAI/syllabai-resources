---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r5995
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r5995
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5995
  old_site_id: null
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
  exam_reference: UCLES A level Pure Mathematics 1, 1979, Q1(a)
task: T-UGM-IMPORT-6
---

# If $x_2 = 1/(1 - x_1), x_3 = 1/(1 - x_2)$, can we show $x_1x_2x_3+1=0$?

## Question

It is given that

\[\begin{equation*} x_2 = \frac{1}{1 - x_1}, \quad x_3 = \frac{1}{1 - x_2}, \quad x_4 = \frac{1}{1 - x_3}, \quad\text{where $x_1 \ne 0$ or $1$.} \end{equation*}\]

Prove that (i) \(x_1x_2x_3 + 1 = 0\), (ii) \(x_4 = x_1\).

## Solution

As \(x_1\) neither equals \(0\) nor \(1\), it follows that \(x_2\), \(x_3\), and \(x_4\) likewise neither equal \(0\) nor \(1\).

We can write

\[\begin{align*} x_1x_2x_3 = \dfrac{x_1}{1 - x_1} \dfrac{1}{1 - x_2} &= \dfrac{x_1}{1 - x_1} \dfrac{1}{1 - \dfrac{1}{1 - x_1}} \\ &= \dfrac{x_1}{1 - x_1} \dfrac{1 - x_1}{(1 - x_1) - 1} \\ &= \dfrac{x_1}{1 - x_1} \dfrac{1 - x_1}{-x_1} \\ &= -1. \end{align*}\]

from which the result immediately follows.

For the second part, note that what we have just proved for \(x_1 x_2 x_3\) applies similarly to \(x_2 x_3 x_4\). So we also have \(x_2 x_3 x_4 = -1\).

Then

\[x_2 x_3 x_4 = x_1 x_2 x_3,\]

so dividing both sides by \(x_2 x_3\) yields

\[x_4 = x_1.\]

If \(f(x) = \dfrac{1}{1 - x}\), then we have shown \(f^3(x) = x\).

We might wonder, if \(f(x) = \dfrac{p(x)}{q(x)}\), where \(p\) and \(q\) are polynomials with rational coefficients, and \(f^n(x) = x\) for (almost ) all \(x\), what are the possible values for \(n\)?

These beautiful periodic creatures are called Lyness cycles, after Robert Cranston Lyness.
