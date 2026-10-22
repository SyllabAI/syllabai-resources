---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/function-builder-i
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/fluency-exercise
- level/developing
resource_identity:
  ugm_id: function-builder-i
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 8
  resource_type_label: Fluency exercise
  level: Developing
  ref: 8608
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-functions
    validation_status: SUGGESTED
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-2
---

# Function builder I

> Excerpt: This task is designed to build understanding of the properties of functions and their graphs. Students see how those properties affect the outcome of combining pairs of functions by adding, subtracting and multiplying, in order to fill the cells of a grid with an appropriate sketch.

## Problem

The function \[a(x)=x+1\] can be combined in a number of ways with each of the functions \[b(x)=2x-1, \quad b(x)=x^2-5x+8, \quad b(x)=x^2-5x-6\] to create a set of new functions. What functions are created by adding, subtracting and multiplying? Can you sketch them in the cells of the grid below?

You might prefer to choose from the graphs A to L which are provided as [cards to print out](https://undergroundmathematics.org/combining-functions/function-builder-i/components/cards.pdf).

| \(a(x)=\) \(x+1\) | \(a(x)+b(x)\) | \(a(x)-b(x)\) | \(a(x)\times b(x)\) |
| --- | --- | --- | --- |
| \(b(x)=\) \(2x-1\) | > [figure: graph of a plus b — `https://undergroundmathematics.org/combining-functions/function-builder-i/images/a-plus-b1.png`] (image not included in the text import; path of record). \(y=3x\) |  |  |
| \(b(x)=\) \(x^2-5x+8\) |  |  |  |
| \(b(x)=\) \(x^2-5x-6\) |  |  |  |

## Solution

### Top row, \(b(x)=2x-1\)

Here, \(a(x)\) and \(b(x)\) are both straight line functions. Adding and subtracting them will create other straight line functions and the correct ones can be found by checking their axis intercepts.

**Multiplying** two straight line functions will usually create a quadratic function.

In this case, the result is \(y=(x+1)(2x-1)\) which is an upward facing parabola with \(x\)-intercepts at \(-1\) and \(+\frac12\). So it must be graph K.

Can you find an example of straight line functions that do *not* create a quadratic when multiplied?

### Middle row, \(b(x)=x^2-5x+8\)

**Adding**, we get \(y = (x+1)+(x^2-5x+8) = x^2-4x+9\). This is an upward facing parabola, so it could be either I, J or K. It has a \(y\)-intercept of \(9\) so it must be graph I.

To check, we can see that it does not factorise, but we could write it in completed square form, \[y=(x-2)^2+5\] which shows that its vertex is at \((2,5)\) and it does not cross the \(x\)-axis.

**Subtracting**, we get \(y=-x^2+6x-7\). This is downward facing with \(y\)-intercept of \(-7\) so it could be graph F or G.

Completing the square, \(y = -(x-3)^2+2\), so its vertex is at \((3,2)\) and it therefore crosses the \(x\)-axis. It must be graph F.

When we **multiply** a straight line function by a quadratic we expect to get a cubic function. Here, \(y=(x+1)(x^2-5x+8)\). We can see that this meets the \(x\)-axis at \(x=-1\) and that it has a \(y\)-intercept of \(8\). All three of graphs D, H and L meet the \(x\)-axis at some negative value of \(x\), but only H has a positive \(y\)-intercept. So this must be graph H.

Note that multiplying out the two brackets here would not be particularly helpful.

To check our choice of graph H, we could note that the graph has no other \(x\)-intercepts. What does this tell us about the quadratic factor, \((x^2-5x+8)\)?

### Bottom row, \(b(x)=x^2-5x-6\)

, we get a quadratic that factorises.

\[\begin{align*} y&=x^2-4x-5\\ &=(x-5)(x+1) \end{align*}\]

It has \(x\)-intercepts at \(-1\) and \(5\) and \(y\)-intercept at \(-5\), so it must be graph J.

, we get

\[\begin{align*} y&=-x^2+6x+7\\ &=-(x-7)(x+1) \end{align*}\]

This is downward facing with \(x\)-intercepts at \(-1\) and \(7\) and \(y\)-intercept at \(7\), so it must be graph E.

, we get another cubic. This time we can factorise it further.

\[\begin{align*} y&=(x+1)(x^2-5x-6)\\ &=(x+1)(x-6)(x+1) \end{align*}\]

It has a repeated root at \(x=-1\) and another root at \(x=6\) so it must be graph D.

| \(a(x)=x+1\) | \(a(x)+b(x)\) | \(a(x)-b(x)\) | \(a(x)\times b(x)\) |
| --- | --- | --- | --- |
| \(b(x)=2x-1\) | > [figure: graph of a plus b — `https://undergroundmathematics.org/combining-functions/function-builder-i/images/a-plus-b1.png`] (image not included in the text import; path of record). Graph C, \(y=3x\) | > [figure: graph of a minus b — `https://undergroundmathematics.org/combining-functions/function-builder-i/images/a-minus-b1.png`] (image not included in the text import; path of record). Graph A, \(y=-x+2\) | > [figure: graph of a times b — `https://undergroundmathematics.org/combining-functions/function-builder-i/images/a-times-b1.png`] (image not included in the text import; path of record). Graph K, \(y=(x+1)(2x-1)\) |
| \(b(x)=\) \(x^2-5x+8\) | > [figure: graph of a plus b — `https://undergroundmathematics.org/combining-functions/function-builder-i/images/a-plus-b2.png`] (image not included in the text import; path of record). Graph I, \(y=x^2-4x+9\) | > [figure: graph of a minus b — `https://undergroundmathematics.org/combining-functions/function-builder-i/images/a-minus-b2.png`] (image not included in the text import; path of record). Graph F, \(y=-x^2+6x-7\) | > [figure: graph of a times b — `https://undergroundmathematics.org/combining-functions/function-builder-i/images/a-times-b2.png`] (image not included in the text import; path of record). Graph H, \(y=(x+1)(x^2-5x+8)\) |
| \(b(x)=\) \(x^2-5x-6\) | > [figure: graph of a plus b — `https://undergroundmathematics.org/combining-functions/function-builder-i/images/a-plus-b3.png`] (image not included in the text import; path of record). Graph J, \(y=x^2-4x-5\) | > [figure: graph of a minus b — `https://undergroundmathematics.org/combining-functions/function-builder-i/images/a-minus-b3.png`] (image not included in the text import; path of record). Graph E, \(y=-x^2+6x+7\) | > [figure: graph of a times b — `https://undergroundmathematics.org/combining-functions/function-builder-i/images/a-times-b3.png`] (image not included in the text import; path of record). Graph D, \(y=(x+1)^2(x-6)\) |

**Here is a completed grid**
