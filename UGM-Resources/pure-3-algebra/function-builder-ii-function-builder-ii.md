---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/function-builder-ii
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/building-blocks
- level/developing
resource_identity:
  ugm_id: function-builder-ii
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Developing
  ref: 9446
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: polynomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: polynomials
    validation_status: SUGGESTED
  spec_points:
  - code: 3.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "algebraic long division of x²−5x+8 by x+1 (quotient x−6, remainder 14) identifies the behaviour of b(x)/a(x) for the graph-matching grid"
      rationale: "Canonical UGM title: Function builder II"
      validation_status: SUGGESTED
    title: "divide a polynomial, of degree not exceeding 4, by a linear or quadratic polynomial, and identify the quotient and remainder (which may be zero)"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-9
---

# Function builder II

> Excerpt: Students combine functions by taking reciprocals and by dividing and find the sketches of the results to fill the cells of a grid. This task builds understanding of the properties of functions and practises visualisation and sketching of graphs of rational functions.

## Problem

The function \[a(x)=x+1\] can be combined in a number of ways with each of the functions \[b(x)=2x-1, \quad b(x)=x^2-5x+8, \quad b(x)=x^2-5x-6\] to create a set of new functions. Can you find the correct one of graphs M to X to go in each cell of the grid below?

The graphs are available as [cards to print out](https://undergroundmathematics.org/polynomials/function-builder-ii/components/cards.pdf), along with a [large format grid](https://undergroundmathematics.org/polynomials/function-builder-ii/components/printable-table.pdf).

| \(a(x)=\) \(x+1\) | \(\dfrac{1}{b(x)}\) | \(\dfrac{a(x)}{b(x)}\) | \(\dfrac{b(x)}{a(x)}\) |
|---|---|---|---|
| \(b(x)=\) \(2x-1\) |  |  |  |
| \(b(x)=\) \(x^2-5x+8\) |  |  |  |
| \(b(x)=\) \(x^2-5x-6\) |  |  |  |

## Solution

In order to match up the graphs with their equations, we need to identify some of the features of each curve, such as

- the location of vertical asymptotes,

- where it crosses the \(x\) and \(y\)-axes,

- whether the function is positive or negative for ranges of \(x\) values,

- its behaviour as \(x\) becomes very large in positive and negative directions.

To find some of these features, it can be helpful to rearrange the algebra or to consider the effect of simple graph transformations. Here are a few examples of things you might have thought of.

**Finding \(\frac{a(x)}{b(x)}\) for \(b(x)=2x-1\)**

We want to identify the graph of \(y=\dfrac{x+1}{2x-1}\).

We can see that it will have an \(x\)-intercept at \((-1,0)\) and a \(y\)-intercept at \((0,-1)\). It will also have a vertical asymptote at \(x=\frac{1}{2}\). As \(x\) increases from just less than \(\frac{1}{2}\) to just more than \(\frac{1}{2}\), the denominator goes from negative to positive so our graph will do the same at the asymptote.

When \(x\) is very large, either positive or negative, we have \(y\approx\dfrac{x}{2x}=\dfrac{1}{2}\).

The shape of the curve is not immediately obvious, but we can do some rearranging of the algebra. \[y=\frac{x+1}{2x-1}=\frac{\frac{1}{2}(2x-1)+\frac{3}{2}}{2x-1} = \frac{1}{2}+\frac{3}{2}\frac{1}{2x-1} = \frac{1}{2} +\frac{3}{4}\frac{1}{(x-1/2)}\] So now we can see that our function is a hyperbola, \(\frac{1}{x}\), that has been translated horizontally by \(\frac{1}{2}\), scaled vertically by \(\frac{3}{4}\) and then translated up by \(\frac{1}{2}\).

This confirms that as \(x\to\pm\infty\), \(y\to\frac{1}{2}\) and the correct graph is (M).

**Finding \(\frac{1}{b(x)}\) for \(b(x)=x^2-5x+8\)**

It is helpful to first explore the features of the quadratic, \(b(x)\). It doesn’t factorise easily, so let’s try completing the square. \[x^2-5x+8 = \left(x-\tfrac{5}{2}\right)^2 + 8-\tfrac{25}{4} = \left(x-\tfrac{5}{2}\right)^2 + \tfrac{7}{4}\] So we have that

- \(b(x)\) is a parabola with a minimum at \(\left(\frac{5}{2},\frac{7}{4}\right)\), so \(y=\frac{1}{b(x)}\) has a maximum at \(\left(\frac{5}{2},\frac{4}{7}\right)\);

- \(b(x)\) is always positive, so \(y=\frac{1}{b(x)}\) is also always positive;

- \(b(x)\) has no zeros, so \(y=\frac{1}{b(x)}\) has no vertical asymptotes;

- as \(x\to\pm\infty\), \(\frac{1}{b(x)}\to 0\).

The correct graph is (S).

**Finding \(\frac{b(x)}{a(x)}\) for \(b(x)=x^2-5x+8\)**

We want to find \(y=\dfrac{x^2-5x+8}{x+1}\). We discovered above that the quadratic numerator has no zeros, so this curve does not cross the \(x\)-axis.

It has a \(y\)-intercept at \(8\), and a vertical asymptote at \(x=-1\).

Let’s see what happens if we do an algebraic division.

Using long division, \[\begin{array}{rll} \phantom{x^2+5}x-6 & \text{ r }14 \cmlongdivbr x+1 \cmlongdiv{x^2-5x+8} \cmlongdivbr \underline{x^2+\phantom{0}x}\phantom{{}+8} && \hbox{[$x \times (x+1)$]} \cmlongdivbr \phantom{x^2}{}-6x+8 && \hbox{[subtract...]} \cmlongdivbr \phantom{x^2}\underline{{}-6x-6} && \hbox{[$-6(x+1)$]} \cmlongdivbr \phantom{x^2-5x+{}}14 && \hbox{[remainder]} \cmlongdivbr \end{array}\]

or using a grid method, \[\begin{array}{r|rr} & \phantom{0}x\phantom{x^2}-6 \\ \hline x & x^2-6x & 14 \\ +1 & x\phantom{x^2}-6 \end{array}\]

The remainder of \(14\) tells us that \(x^2-5x+8=(x+1)(x-6)+14\).

So we have \(y=x-6 +\frac{14}{x+1}\) and the curve is a hyperbola added to a straight line of gradient \(1\). This gives the perhaps surprising result that as \(x\to\pm\infty\), \(y\to x-6\).

The correct graph is (U).

**Finding the third row graphs**

The quadratic in the third row, \(b(x)=x^2-5x-6\), looks very similar to that in the second row. However, this one factorises such that \(b(x)\) has zeros at \(x=-1\) and \(x=6\). This gives rise to some vertical asymptotes, but also allows some cancelling to occur in the algebraic fractions.

Here is a completed grid

| \(a(x)=x+1\) | \(\dfrac{1}{b(x)}\) | \(\dfrac{a(x)}{b(x)}\) | \(\dfrac{b(x)}{a(x)}\) |
|---|---|---|---|
| \(b(x)=2x-1\) | Graph P, \(y=\dfrac{1}{2x-1}\) | Graph M, \(y=\dfrac{x+1}{2x-1}\) | Graph N, \(y=\dfrac{2x-1}{x+1}\) |
| \(b(x)=\) \(x^2-5x+8\) | Graph S, \(y=\dfrac{1}{x^2-5x+8}\) | Graph Q, \(y=\dfrac{x+1}{x^2-5x+8}\) | Graph U, \(y=\dfrac{x^2-5x+8}{x+1}\) |
| \(b(x)=\) \(x^2-5x-6\) | Graph V, \(y=\dfrac{1}{(x+1)(x-6)}\) | Graph T, \(y=\dfrac{1}{x-6}, x\ne-1\) | Graph X, \(y=x-6, x\ne-1\) |
