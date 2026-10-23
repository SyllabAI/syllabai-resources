---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/two-way-calculus
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/many-ways-problem
- level/developing
resource_identity:
  ugm_id: two-way-calculus
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 5564
  old_site_id: C3_RT6_2
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'two-way table: generate functions with prescribed stationary points, local extrema
        and increasing/decreasing ranges — differentiation central (the inflection clause is extension,
        recorded)'
      rationale: 'Canonical UGM title: "Two-way calculus"'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'two-way table: generate functions with prescribed stationary points, local extrema
        and increasing/decreasing ranges — differentiation central (the inflection clause is extension,
        recorded)'
      rationale: 'Canonical UGM title: "Two-way calculus"'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/calculus-meets-functions/two-way-calculus-teacher-support/assets/twowaycalculus-studentwork.pdf
  kind: printable
- path: https://undergroundmathematics.org/calculus-meets-functions/two-way-calculus/download/teacher-notes.pdf
  kind: printable
---

# Two-way calculus

> Excerpt: Students generate examples and identify common features by linking together stationary points, increasing and decreasing behaviour, integration and differentiation. For detailed notes on this resource, please see [Two-way calculus - teacher support](/calculus-meets-functions/two-way-calculus-teacher-support).

## Problem

Each column and row heading in the following table is a property that a function may or may not have. A function can appear in a cell if it has the properties in the corresponding row and column.

We have omitted some headings, and some entries in cells. Can you complete the table?

**You might find it helpful to draw some sketches.** You could use graph-sketching software such as [Desmos](https://www.desmos.com/calculator) to help you, but try to do the sketching by hand before reaching for a computer or calculator!

Make sure that you can explain why each function has the desired properties.

|  | The curve is \(\ldots\) creasing for \(x>1\) | Has a local \(\ldots\) imum with \(y\) -coordinate \(1\) |  |
|---|---|---|---|
| Has a stationary point at \((1,1)\) | \[y=x^3+3x^2-9x+6\] |  | \[y=3x^4-4x^3+2\] |
|  |  | \[y=2x^3+9x^2+1\] | \[y=1-\dfrac{1}{4}x^4-x^3\] |
| Has an \(\,\,\ldots \,\,\) number of stationary points |  |  | \[y=x^5-x^3+5\] |

- Can you complete the table using a different function in every cell?

- On the other hand, can you complete the table with a smaller number of functions?

- Did you have any choice about the column and row headings?

## Things you might try

Have you tried sketching the functions we have been given?

If we want…

A stationary point on the curve

If we want a curve given by \(y=f(x)\) to have a stationary point at \((a,b)\) where \(a\) and \(b\) are real numbers, we want \(f'(a)=0\) and \(f(a)=b\).

An odd number of stationary points

How many stationary points can a quadratic or cubic have?

What about a degree \(4\) or \(5\) polynomial?

Local minimum or maximum

If we want a curve to have a local minimum or local maximum, what could the curve “look like”?

If \(g(x)\) is a function with a local maximum at \(x=2\), can we use this information to create a function that has a local minimum at \(x=2\)?

## A possible solution

|  | The curve is increasing for \(x>1\) | Has a local minimum with \(y\) -coordinate \(1\) | Has a point of inflection when \(x=0\) |
|---|---|---|---|
| Has a stationary point at \((1,1)\) | \[y=x^3+3x^2-9x+6\] | \[y=(x-1)^2+1\] | \[y=3x^4-4x^3+2\] |
| Has a local maximum when \(x=-3\) | \[y=x^3+3x^2-9x+6\] | \[y=2x^3+9x^2+1\] | \[y=1-\dfrac{1}{4}x^4-x^3\] |
| Has an odd number of stationary points | \[y=7(x-1)^2+1\] | \[y=(x+4)^2+1\] | \[y=x^5-x^3+5\] |
