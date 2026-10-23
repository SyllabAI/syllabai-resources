---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/approximating-areas
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/problem-requiring-decisions
- level/developing
resource_identity:
  ugm_id: approximating-areas
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 6
  resource_type_label: Problem requiring decisions
  level: Developing
  ref: 9188
  old_site_id: C1_RT8_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: introducing-calculus
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: introducing-calculus
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/introducing-calculus/approximating-areas/download/teacher-notes.pdf
  kind: printable
---

# Approximating areas

> Excerpt: Students are challenged to put four shaded areas in increasing order of size. This is a problem in which the concepts of area under a curve, over- and under-estimation, and the trapezium rule can be introduced.

## Problem

Consider the shaded area under each function shown on the cards.

Put the cards in order of size of the shaded area, from smallest to largest.

(a)

(b)

(c)

(d)

How did you decide which card has the smallest shaded area? What about the largest?

Check

The exact value for the area under each function, in order of increasing size, is:

| Card | Function | Area |
|---|---|---|
|  | \(f(x)=\dfrac{2}{3}x\) | \(8\) |
|  | \(f(x)=\dfrac{1}{2}x^3-4x^2+8x\) | \(\dfrac{26}{3}\) |
|  | \(f(x)=\dfrac{1}{4}x^2\) | \(\dfrac{31}{3}\) |
|  | \(f(x)=\dfrac{11}{4}\) | \(11\) |

- How close were your estimates to these exact values? Were they over or under-estimates?

- How could you have improved these estimates?

- How can you refine your methods of estimating the areas under the quadratic and cubic curves to obtain answers that are correct to \(1\) decimal place?

## Things you might have noticed

Consider the shaded area under each function shown on the cards.

Put the cards in order of size, from smallest to largest in terms of the shaded area.

If we first step back and look at the four cards as a whole we might notice a few helpful things.

- Two of the cards contain linear functions—these areas can be calculated exactly.

- The other two cards contain a quadratic and cubic function respectively. Calculating these areas exactly is possible but requires some tools that we may not yet be familiar with. We could however start by finding an estimate for the shaded areas. If we are confident that we have a good estimate this may be enough to put the cards in order.

First let’s consider the card containing the linear function \(f(x) = \dfrac{11}{4}\). This function describes a straight line parallel to the \(x\)-axis and therefore the shaded region is a rectangle of width \(4\) and height \(\dfrac{11}{4}\).

The area of this rectangle is then given by \[4 \times \frac{11}{4} = 11.\]

If we now consider the second linear function, \(f(x) = \dfrac{2}{3}x\), we can see that the shaded region is a trapezium.

- Do we currently have all of the information needed to be able to calculate the area of this trapezium? If not, how might we determine the additional information?

- Once we have calculated a value for this area, is it greater than the area of the shaded region on the previous card?

This card shows a quadratic curve. How might we estimate the area of the shaded region?

- Is there more than one way in which we could do this?

- If we chose to estimate by constructing a trapezium, like this, what would our estimate for the shaded area be? Do you think this estimate is ‘good enough’?

- Does our chosen method produce an over-estimate or an under-estimate? How do we know?

- Can we establish maximum and minimum values for the shaded area that will enable us to place this card in order, when compared to the previous two?

Now we consider the cubic curve on the final card. How might we estimate the area of the shaded region this time?

- Will we choose to take the same approach as for the quadratic curve? Why?

- Does our chosen method produce an over-estimate or an under-estimate? How do we know?

- Can we establish maximum and minimum values for the shaded area that will enable us to place this card in order, when compared to the others?

If you are interested in how the exact answers provided on the problem page were calculated, you might like to explore some of the ideas at [Calculus of Powers](https://undergroundmathematics.org/calculus-of-powers).
