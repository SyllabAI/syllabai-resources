---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r5602
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r5602
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5602
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
  exam_reference: UCLES A level Mathematics B Special paper, 1979, Q3
task: T-UGM-IMPORT-6
---

# Can we show  $L  < \int_1^r \frac{1}{x} \:dx <  R$?

## Question

Show, graphically or otherwise, that if

\(r\)

is an integer greater than

\(1\)

, then

\[\begin{equation*} L = \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \dotsb + \frac{1}{r} < \int_1^r \frac{1}{x} \:dx < 1 + \frac{1}{2} + \frac{1}{3} + \dotsb + \frac{1}{r-1} = R. \end{equation*}\]

Determine whether \(\frac{1}{2}(L+R)\) underestimates or overestimates the value of the integral.

## Solution

Consider the following graph.

The first red column in this image has area

\(\dfrac{1}{2}\)

, the second

\(\dfrac{1}{3}\)

, etc., and every such column lies under the curve

\(y = \frac{1}{x}\)

; thus, for every

\(r\)

,

\[\begin{equation*} L = \frac{1}{2} + \frac{1}{3} + \frac{1}{4} + \dotsb + \frac{1}{r} < \int_1^r \frac{1}{x} \:dx \end{equation*}\]

Similarly, we can consider another graph.

The first red column in this image has area

\(1\)

, the second

\(\dfrac{1}{2}\)

, etc., and the curve falls under the red horizontal line segments; thus, for every

\(r\)

,

\[\begin{equation*} \int_1^r \frac{1}{x} \:dx < 1 + \frac{1}{2} + \frac{1}{3} + \dotsb + \frac{1}{r-1} = R. \end{equation*}\]

The series \(1 + \frac{1}{2} + \frac{1}{3} + \dotsb\) is called the harmonic series. Can you use the inequality above to decide whether this series converges or diverges? You may wish to look at [Harmonious proofs](https://undergroundmathematics.org/sequences/harmonious-proofs) to explore this idea further.

Consider the red shaded area in the following graph.

This area is, in fact,

\(\dfrac{L+R}{2}\)

. Since the red broken line always lies above the blue line, the shaded area will always be greater than the integral, and so

\[\begin{equation*} \frac{L+R}{2} > \int_1^r \frac{1}{x} \:dx \end{equation*}\]

for every \(r\); that is, it’s an overestimate.

It turns out that the error

\[\begin{equation*} \sum_{n=1}^{r-1} \frac{1}{n} - \int_1^r \frac{1}{x} \:dx = \sum_{n=1}^{r-1} \frac{1}{n} - \log r \end{equation*}\]

converges as \(r \to \infty\) to a positive constant, \(\gamma\), called the Euler–Mascheroni constant. This appears in a number of surprising places in mathematics, but it remains mysterious; for example, it’s unknown whether it’s irrational or not (although it almost certainly is).
