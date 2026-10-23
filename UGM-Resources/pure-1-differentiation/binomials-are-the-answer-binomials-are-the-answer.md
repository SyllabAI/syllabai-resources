---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/binomials-are-the-answer
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/investigation
- level/introducing
resource_identity:
  ugm_id: binomials-are-the-answer
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 7
  resource_type_label: Investigation
  level: Introducing
  ref: 7692
  old_site_id: C2_RT1_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: gradients of chords (3,9)->(3.5,12.25)->(3.1,9.61)->... then the general gradient of
        y=x^n via the binomial expansion — the derivation-of-record from chord limits to the power rule
        (lane-6 sweep routing pre-identified it for 1.7)
      rationale: 'Canonical UGM title: "Binomials are the answer!"'
      validation_status: SUGGESTED
      primaryPick: true
    title: understand the gradient of a curve at a point as the limit of the gradients of a suitable
      sequence of chords, and use the notations d y , and d y f ′ ( x ) , f ″( x ) , 2 for first and
      second derivatives
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/calculus-of-powers/binomials-are-the-answer/download/teacher-notes.pdf
  kind: printable
---

# Binomials are the answer!

> Excerpt: Starting with quadratics and cubics, students explore gradients of chords, leading to gradients of tangents to curves and finally a general result for the gradient of $y=x^n$.

## Introduction

In the solution for [A tangent is…](https://undergroundmathematics.org/introducing-calculus/a-tangent-is/solution) we had the following,

When we “zoom in” to a point on a curve, it often looks like a straight line. If so, then we can draw that straight line. If we then zoom out again, we will discover that we have drawn the tangent to the curve at that point. This is what a tangent is.

How can we use this to find the gradient of the tangent line?

How do we find the gradient of a straight line?

## Quadratic and cubic

**Looking at the quadratic \(y=x^2\)**

Figure 1

How can we find the gradient of the line through the points with coordinates \((3,9)\) and \((3.5,12.25)\)?

How can we find the gradient of the line through the points with coordinates \((3,9)\) and \((3.1,9.61)\)?

How can we find the gradient of the line through the points with coordinates \((3,9)\) and \((3.01,9.0601)\)?

Answer

To find the gradient of the line going through the points \((x_1,y_1)\), \((x_2,y_2)\) we look at the change in the \(y\)-coordinate divided by the change in the \(x\)-coordinate:

\[\frac{y_2-y_1}{x_2-x_1}.\]

So for each of the pairs of points we have:

1. \(\dfrac{12.25-9}{3.5-3}=6.5\).

---

1. \(\dfrac{9.61-9}{3.1-3}=6.1\).

---

1. \(\dfrac{9.0601-9}{3.01-3}=6.01\).

Can we make any suggestions on what is happening?

What could we suggest the gradient of the tangent line at \((3,9)\) to the curve \(y=x^2\) is?

How can we generalise this for any point \((x,x^2)\)?

Can you use a spreadsheet to investigate what the tangent line gradient will be for \(x=2\), \(x=4\) etc…?

An algebraic point of view

How can we find the gradient of the line through the points with coordinates \((x,x^2)\) and \((x+h,(x+h)^2)\)?

We can apply the same thoughts when we had numbers,

\[\frac{y_2-y_1}{x_2-x_1}=\frac{(x+h)^2-x^2}{x+h-x}=\frac{(x+h)^2-x^2}{h}.\]

We can expand and simplify this expression,

\[\frac{(x+h)^2-x^2}{h}=\frac{x^2+2hx+h^2-x^2}{h}=\frac{2hx+h^2}{h}=2x+h.\]

So, the gradient of the line through the points \((x,x^2)\) and \((x+h,(x+h)^2)\) is \(2x+h\).

As we move the point \((x+h,(x+h)^2)\) closer and closer to \((x,x^2)\), we are making \(h\) smaller and smaller, finally making \(h\) zero. This gives the gradient of the line that *touches* the curve \(y=x^2\) at the point \((x,x^2)\) as \(2x\).

**Looking at the cubic \(y=x^3\)**

Can you use a spreadsheet to investigate what the tangent line gradient will be for \(x=1\), \(x=2\), \(x=3\) etc… on the cubic curve \(y=x^3\)?

If we take \(x=2\), we have the point \((2,8)\) and we can choose a second *close* point on the curve \(y=x^3\), \((2.01,9.261)\). This would give a gradient of

\[\frac{y_2-y_1}{x_2-x_1}=\frac{9.261-8}{2.1-2}=12.61.\]

How can we generalise this for any point \((x,x^3)\)?

An algebraic point of view

How can we find the gradient of the line through the points with coordinates \((x,x^3)\) and \((x+h,(x+h)^3)\)?

We can apply the same thoughts when we had for the curve \(y=x^2\).

\[\frac{y_2-y_1}{x_2-x_1}=\frac{(x+h)^3-x^3}{x+h-x}=\frac{(x+h)^3-x^3}{h}.\]

We can expand and simplify this expression:

\[\frac{(x+h)^3-x^3}{h}=\frac{x^3+3hx^2+3h^2x+h^3-x^3}{h}=\frac{3hx^2+3h^2x+h^3}{h}=3x^2+3hx+h^2.\]

So, the gradient of the line through the points \((x,x^3)\) and \((x+h,(x+h)^3)\) is \(3x^2+3hx+h\).

As we move the point \((x+h,(x+h)^3)\) closer and closer to \((x,x^3)\), we are making \(h\) smaller and smaller, finally making \(h\) zero. This gives the gradient of the line that *touches* the curve \(y=x^3\) at the point \((x,x^3)\) as \(3x^2\).

## Generalising to $x^n$

How can we find the gradient for any tangent line to a function \(y=x^n\), where \(n\) is a positive integer?

An algebraic point of view

In [Quadratic and cubic](https://undergroundmathematics.org/calculus-of-powers/binomials-are-the-answer/quadratic-and-cubic) we were given a power of \(x\), \(f(x)=x^2\) or \(x^3\), and we took the point \((3,f(3))\) and another point \((3+h,f(3+h))\) and found the gradient of the line through these two points for \(h\) a very small number.

If we did this here, what would be the gradient of the line through \((3,f(3))\) and \((3+h,f(3+h))\), for smaller and smaller values of \(h\)?

How can we generalise this for any point on the curve \(y=x^n\)?

## Solution for $x^n$

We could adapt what we did for the quadratic and cubic curves in order to generalise: how can we find the gradient of the line through the points with coordinates \((x,x^n)\) and \((x+h,(x+h)^n)\)? Where \(h\) is a very very small positive number.

We can then calculate the gradient of the line going through the points \((x,x^n)\) and \((x+h,(x+h)^n)\),

\[\frac{y_2-y_1}{x_2-x_1}=\frac{(x+h)^n-x^n}{x+h-x}=\frac{(x+h)^n-x^n}{h}.\]

We would like to expand and simplify this expression, but \((x+h)^n\) is not so simple to expand when we don’t have a specific value for \(n\).

However, \(x+h\) is a binomial. We have a way to expand \((x+h)^n\), The Binomial Theorem, for \(n\) a positive integer:

\[(x+h)^n={\binom n 0}x^nh^0+{\binom n 1}x^{n-1}h+{\binom n 2}x^{n-1}h^2+ \dots + {\binom n {n-1}}xh^{n-1}+{\binom n n}x^{0}h^n.\]

The binomial coefficients \({\dbinom n k}\) are given by \(\dfrac{n!}{k!(n-k)!}\).

We can now think about how to expand,

\[\frac{(x+h)^n-x^n}{h}.\]

The numerator is,

\[{\binom n 0}x^nh^0+{\binom n 1}x^{n-1}h+{\binom n 2}x^{n-1}h^2+ \dots + {\binom n {n-1}}xh^{n-1}+{\binom n n}x^{0}h^n-x^n\]

which simplifies to,

\[{\binom n 1}x^{n-1}h+{\binom n 2}x^{n-1}h^2+ \dots + {\binom n {n-1}}xh^{n-1}+{\binom n n}x^{0}h^n.\]

The denominator simplifies to \(h\).

So, the gradient of the line through the points \((x,x^n)\) and \((x+h,(x+h)^n)\) is

\[{\binom n 1}x^{n-1}+{\binom n 2}x^{n-1}h+ \dots + {\binom n {n-1}}xh^{n-2}+{\binom n n}h^{n-1}.\]

As we move the point \((x+h,(x+h)^n)\) closer and closer to \((x,x^n)\), we are making \(h\) smaller and smaller, finally making \(h\) zero. This gives the gradient of the line that *touches* the curve \(y=x^n\) at the point \((x,x^n)\) as \({\binom n 1}x^{n-1}\), for \(n\) a positive integer.

The binomial coefficient \(\dbinom{n}{1}\) is given by \(\dfrac{n!}{1!(n-1)!}=\dfrac{n\times (n-1) \times \dots \times 1}{(n-1)\times (n-2) \times \dots \times 1}=n\).

This gives the gradient of the line that *touches* the curve \(y=x^n\) at the point \((x,x^n)\) as \(nx^{n-1}\), for \(n\) a positive integer.
