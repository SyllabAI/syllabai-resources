---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/sum-estimating
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/scaffolded-task
- level/developing
resource_identity:
  ugm_id: sum-estimating
  station: sequences
  station_title: Sequences
  resource_type_id: 3
  resource_type_label: Scaffolded task
  level: Developing
  ref: 9016
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
task: T-UGM-IMPORT-6
assets:
- path: https://undergroundmathematics.org/sequences/sum-estimating/download/teacher-notes.pdf
  kind: printable
---

# Sum estimating

> Excerpt: This problem explores the links between integration and summation. Often when introducing integration we use sums to approximate integrals. Here the idea is turned on its head and students are asked to approximate the value of the sum of $r^2$ using integrals.

## Warm-up

Can you convince yourself that \(n^2 ≤ \displaystyle\sum_{r=1}^{n} r^2 ≤ n^3\)?

Suggestion

Think about representing the sum of the first \(n\) square numbers as bars of width \(1\) and height \(r^2\).

A convincing argument

\[\displaystyle\sum_{r=1}^{n} r^2 = 1+4+9+16+\cdots+n^2\]

Written in this form we see that \(n^2 ≤ 1+4+9+\cdots+n^2\).

We might also have seen this from the diagram above as the last bar has an area of \(n^2\).

When is \(n^2 = \displaystyle\sum_{r=1}^{n} r^2\) and when is \(n^2 < \displaystyle\sum_{r=1}^{n} r^2\)?

The second half of the inequality can also be determined from this diagram. The sum of the square numbers is enclosed by a rectangle made up of the axes, the dotted line, and the last bar. This rectangle has an area of \(n^3\) and so \(\displaystyle\sum_{r=1}^{n} r^2 ≤ n^3\)

Putting this together gives us \(n^2 ≤ \displaystyle\sum_{r=1}^{n} r^2 ≤ n^3\).

## Problem

In the [Warm-up](https://undergroundmathematics.org/sequences/sum-estimating/) we saw that \(n^2\) and \(n^3\) can be used as lower and upper bounds for the value of \(\displaystyle\sum_{r=1}^{n} r^2\): \[n^2 ≤ \displaystyle\sum_{r=1}^{n} r^2 ≤ n^3\]

We can use the diagrams below to find a different way to bound \(\displaystyle\sum_{r=1}^{n} r^2\).

|  |  |
|---|---|

- Which of the areas represented in the two diagrams is bigger?

- Does this result generalise?

Use this information to provide either an upper or lower bound for \(\displaystyle\sum_{r=1}^{n} r^2\).

- Can you find a function which bounds the graphical representation of \(\displaystyle\sum_{r=1}^{n} r^2\) on the other side?

Suggestion

Use this function to provide a second bound for \(\displaystyle\sum_{r=1}^{n} r^2\).

## Solution

The first diagram is a representation of the sum of the first \(8\) square numbers, where each bar has width \(1\) and height \(r^2\). The second diagram has a shaded area which can represented by the integral \(\int_0^8 x^2 \, dx\).

Which of these areas is bigger? We could numerically compute the areas but a simple way to compare them is to draw the two images on the same axes.

We can see that \(\int_0^8 x^2 \, dx < \sum_{r=1}^{8} r^2\), but we can also generalise this result from the diagram and say that

\[\int_0^n x^2 \, dx < \sum_{r=1}^{n} r^2.\]

Use this information to provide either an upper or lower bound for the value of \(\displaystyle\sum_{r=1}^{n} r^2\).

Calculating the value of the integral, we have \(\int_0^n x^2 \, dx = \frac{1}{3}n^3\), so we can provide a lower bound for \(\sum_{r=1}^{n} r^2\),

\[\dfrac{1}{3}n^3 < \sum_{r=1}^n r^2.\]

How does what we’ve done here, using an integral to estimate a summation, compare to what you’ve done before using integrals and sums?

Can you find a function that bounds the graphical representation of \(\displaystyle\sum_{r=1}^{n} r^2\) on the other side?

Use this function to provide a second bound for \(\displaystyle\sum_{r=1}^{n} r^2\).

Now we know that we are looking to find an upper bound. We can find a function that gives an overestimate of the area by using a transformation of \(y = x^2\).

Therefore the integral \(\int_0^n (x+1)^2 \, dx\) provides an upper bound to \(\sum_{r=1}^{n} r^2\). It evaluates to \(\int_0^n (x+1)^2 \, dx = \frac{1}{3}n^3 + n^2 + n\), so we have the following bounds for \(\sum_1^n r^2\):

\[\dfrac{1}{3}n^3 < \sum_1^n r^2 < \dfrac{1}{3}n^3 + n^2 + n.\]

Our result shows that \(\sum_1^n r^2 \approx \frac{1}{3}n^3\). Does this seem reasonable? Why might we have expected this result?

There is more than one way we can approximate an upper bound for \(\sum_1^n r^2\). A different approach involves the following diagram.

We can use this to write the inequality \[\displaystyle\sum_0^{n-1} r^2 < \dfrac{1}{3}n^3.\]

If we add \(n^2\) to both sides of the inequality we get \[\displaystyle\sum_0^{n-1} r^2 + n^2 < \dfrac{1}{3}n^3 + n^2,\]

which can be simplified to

\[\displaystyle\sum_0^{n} r^2 < \dfrac{1}{3}n^3 + n^2.\]

How does this compare to the upper bound found above? Does it matter that the limits are slightly different?

To find the exact value of \(\sum_1^n r^2\) you might like to try the review question [R6143](https://undergroundmathematics.org/sequences/r6143).
