---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r6340
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r6340
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6340
  old_site_id: Q2016
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
  exam_reference: UCLES A level Mathematics 1, 1952, Q2
task: T-UGM-IMPORT-6
---

# Can we find a good rational approximation for $\sqrt{5}$?

## Question

Prove that, if \(x\) is so small that its cube and higher powers can be neglected, \[\sqrt{\frac{1+x}{1-x}} = 1 + x + \frac{x^2}{2}.\] By taking \(x = \dfrac{1}{9}\), prove that \(\sqrt{5}\) is approximately equal to \(\dfrac{181}{81}\).

## Suggestion

Can we rewrite the left-hand side as a product of functions that we *do* know how to expand?

## Solution

The [binomial theorem](https://undergroundmathematics.org/glossary/binomial-theorem) says that, if \(r\) is any real number and \(\big|x\big| < 1\), then \[(1+x)^r = 1 + rx + \frac{r(r-1)}{2!} x^2 + \frac{r(r-1)(r-2)}{3!} x^3 + \dotsb.\] Since \(x\) is close enough to zero so that its cube and higher powers can be neglected, this can be shortened to say that \[(1+x)^r \approx 1 + rx + \frac{r(r-1)}{2!} x^2.\]

Now, as we can write

\[ \sqrt{\frac{1+x}{1-x}} = (1+x)^{1/2} \times (1-x)^{-1/2} \]

we can therefore use the binomial theorem to say that

\[\begin{align*} \sqrt{\frac{1+x}{1-x}} &\approx \left( 1 + \tfrac{1}{2}x + \frac{\tfrac{1}{2}\left( -\tfrac{1}{2} \right)}{2!}x^2 \right) \times \left( 1 + \left(-\tfrac{1}{2}\right)(-x) + \frac{-\tfrac{1}{2}\left( -\tfrac{3}{2} \right)}{2!}(-x)^2 \right) \\ &= \left( 1 + \tfrac{1}{2}x - \tfrac{1}{8}x^2 \right) \times \left( 1 + \tfrac{1}{2}x + \tfrac{3}{8}x^2 \right) \\ &\approx 1 + \left( \tfrac{1}{2} + \tfrac{1}{2} \right) x + \left( \tfrac{3}{8} + \tfrac{1}{4} - \tfrac{1}{8} \right) x^2\\ &= 1 + x + \frac{x^2}{2}, \end{align*}\]

as required.

Since \(x = \dfrac{1}{9}\) is close to zero, the expansion that we proved in the first part of the question is reasonable.

The left-hand side becomes \[\sqrt{\frac{1+x}{1-x}} = \sqrt{\frac{10/9}{8/9}} = \sqrt{\frac{10}{8}} = \sqrt{\frac{5}{4}} = \frac{\sqrt{5}}{2}\] while the right-hand side becomes \[1 + x + \frac{x^2}{2} = 1 + \frac{1}{9} + \frac{1}{162} = \frac{162 + 18 + 1}{162} = \frac{181}{162}.\] That is, \[\frac{\sqrt{5}}{2} \approx \frac{181}{162}\] so on multiplying through by \(2\), \[\sqrt{5} \approx \frac{181}{81}\] as we were aiming to show.

In fact, \(\left| \dfrac{181}{81} - \sqrt{5} \, \right| \approx 0.0015\). The approximation is good!

It is, however, far from being the “best” fraction approximation for

\(\sqrt{5}\)

using small denominators. We have

\[\begin{align*} \left| \dfrac{38}{17} - \sqrt{5} \, \right| &\approx 0.0008,\\ \left| \dfrac{161}{72} - \sqrt{5} \, \right| &\approx 0.00004, \end{align*}\]

which are far better. These are found from the [continued fraction](https://undergroundmathematics.org/glossary/continued-fraction) expansion of \(\sqrt{5}\).
