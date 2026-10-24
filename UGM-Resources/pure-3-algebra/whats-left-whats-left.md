---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/whats-left
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/package-of-problems
- level/developing
resource_identity:
  ugm_id: whats-left
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 8162
  old_site_id: "E3_RT7_1"
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
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "quotient/remainder degree reasoning across eight divisions p(x)/d(x) incl. quadratic divisors, with worked algebraic division and the remainder-form generalisation"
      rationale: "Canonical UGM title: What's left?"
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

# What's left?

> Excerpt: What's left? provides students with an opportunity to practise algebraic division while being asked to think about what form the remainder and quotient functions will take.

## Problem

\[\text{The answer to "$27$ divided by $4$" could be written as "$6$, remainder $3$"}\]

where \(4\) is the divisor, \(6\) is the [quotient](https://undergroundmathematics.org/glossary/quotient), and \(3\) is the remainder.

What other ways can you find to express \(\text{"$27$ divided by $4$"}\)?

Why will the remainder always be less than the divisor? Is a similar idea true in polynomial division? For example when a cubic polynomial is divided by a quadratic, what form will the remainder take?

Below is a series of expressions in the form \(\dfrac{p(x)}{d(x)}\), where \(p(x)\) and \(d(x)\) are polynomials.

What [degree](https://undergroundmathematics.org/glossary/degree-of-a-polynomial) are the quotient and remainder polynomials when \(p(x)\) is divided by \(d(x)\)?

A. \(\dfrac{3x+1}{x}\)

B. \(\dfrac{5x-2}{2x-1}\)

C. \(\dfrac{3x^2-5x+2}{x+1}\)

D. \(\dfrac{x^3-5x^2+3x+1}{x+1}\)

E. \(\dfrac{5x^2+8x+9}{x^2+x+2}\)

F. \(\dfrac{x^3-x^2-7x+1}{x^2+2x-1}\)

G. \(\dfrac{x^4-3x^3 + x + 1}{x-1}\)

H. \(\dfrac{6x^4 + 5x^3 + x^2 +10 x -3}{2x^2 + 3x - 1}\)

Can we always know what degree polynomial the quotient and the remainder will be by looking at the question?

Without any calculations, what can we say about the degree of the quotient and remainder polynomials of the following division?

I. \(\dfrac{x^9 - 5x^7 + 3x^2 - 11x + 2}{2x^5 + 4x^4 - x + 7}\)

## Suggestion

Some of the questions have divisors which are quadratic. Below are suggestions as to how methods used for algebraic division by a linear divisor can be extended to working with a quadratic.

E. \(\dfrac{5x^2+8x+9}{x^2+x+2}\)

We could rewrite \(p(x)\) so multiples of the divisor, \(d(x)\), appear.

\[\dfrac{5x^2+8x+9}{x^2+x+2} = \dfrac{5x^2+5x+10+3x-1}{x^2+x+2}\]

Why is this helpful? What might the next step be?

F. \(\dfrac{x^3-x^2-7x+1}{x^2+2x-1}\)

We could use the grid method by extending the number of rows in the grid. For more support with using the grid method you may wish to look at [Divide it up](https://undergroundmathematics.org/polynomials/divide-it-up).

|  | \(x\) | \(\ldots\) |
|---|---|---|
| \(x^2\) | \(x^3\) |  |
| \(+2x\) |  |  |
| \(-1\) |  |  |

Which cells would you fill in next?

We could also use long division:

\[\begin{array}{rll} \phantom{x^2-x^2-7}x+\ldots & \cmlongdivbr x^2+2x-1 \cmlongdiv{x^3-x^2-7x+1} \cmlongdivbr \underline{x^3+\ldots\phantom{{}+1x+8}} && [x \times (x^2+2x-1)] \cmlongdivbr \end{array}\]

## Solution

There are many different ways we could write \(\text{"$27$ divided by $4$"}\). For example, \(6\dfrac{3}{4}\), \(\dfrac{24+3}{4}\) and \(6 + \dfrac{3}{4}\).

Why will the remainder will always be less than the divisor? Is a similar idea true in polynomial division? For example when a cubic polynomial is divided by a quadratic, what form will the remainder take?

Below is a series of expressions in the form \(\dfrac{p(x)}{d(x)}\), where \(p(x)\) and \(d(x)\) are polynomials.

What degree are the quotient and remainder polynomials when \(p(x)\) is divided by \(d(x)\)?

A. \(\dfrac{3x+1}{x}\)

As the divisor is an individual term, we can split up the fraction.

\[\begin{align*} \dfrac{3x+1}{x} &= \dfrac{3x}{x}+\dfrac{1}{x}\\ &= 3 + \dfrac{1}{x} \end{align*}\]

This is a linear expression divided by a linear expression, giving a quotient of \(3\) and a remainder of \(1\), so both are polynomials of degree \(0\).

B. \(\dfrac{5x-2}{2x-1}\)

One method we could use to divide this expression would be rewriting \(p(x)\), in terms of multiples of the divisor, \(d(x)\).

The numerator would become \(\frac{5}{2}(2x-1) + \frac{1}{2}\), giving us

\[\begin{align*} \dfrac{5x-2}{2x-1} &= \dfrac{\frac{5}{2}(2x-1) + \frac{1}{2}}{2x-1}\\ &= \dfrac{5}{2} + \dfrac{\frac{1}{2}}{2x-1} \end{align*}\]

The quotient is

\(\frac{5}{2}\)

and the remainder is

\(\frac{1}{2}\)

which are both polynomials of degree

\(0\)

.

Quotients and remainders don’t have to be integers, or have integer coefficients.

C. \(\dfrac{3x^2-5x+2}{x+1}\)

We are still dividing by a linear expression, but it is no longer a single term. We will use the grid method to do the division. For a more in-depth look at this method, see [Divide it up](https://undergroundmathematics.org/polynomials/divide-it-up).

Putting the first term, \(3x^2\), in the table allows us to complete the first column.

|  | \(3x\) | \(\ldots\) |
|---|---|---|
| \(x\) | \(3x^2\) |  |
| \(+1\) | \(3x\) |  |

We need the \(x\) terms to add to \(-5x\), so we put \(-8x\) in the second column.

|  | \(3x\) | \(-8\) |
|---|---|---|
| \(x\) | \(3x^2\) | \(-8x\) |
| \(+1\) | \(3x\) | \(-8\) |

The completed grid tells us that \[\dfrac{3x^2 - 5x - 8}{x+1} = 3x-8.\]

How does this relate to the original problem \(\dfrac{3x^2-5x+2}{x+1}\)?

We can write it as

\[\begin{align*} \dfrac{3x^2-5x+2}{x+1} &= \dfrac{3x^2 - 5x -8 + 10}{x+1}\\ &= 3x-8 +\dfrac{10}{x+1}. \end{align*}\]

The quotient is \(3x - 8\) and the remainder is \(10\).

After three questions we might already have some ideas as to the structure that is appearing. It may help to think about the following questions:

- How do the questions differ? Does this explain the differences in the answers?

- Can we make any conjectures about the outcome of the next question?

D. \(\dfrac{x^3-5x^2+3x+1}{x+1}\)

We can rewrite the numerator,

\(p(x)\)

, as multiples of the divisor

\(d(x)\)

.

\[\begin{align*} \dfrac{x^3-5x^2+3x+1}{x+1} &= \dfrac{x^3+x^2 - 6x^2 - 6x + 9x+9 - 8}{x+1}\\ &= \dfrac{x^3 + x^2}{x+1} + \dfrac{-6x^2-6x}{x+1} + \dfrac{9x+9}{x+1} + \dfrac{-8}{x+1} \\ &= x^2-6x+9+\dfrac{-8}{x+1}. \end{align*}\]

The quotient is \(x^2-6x+9\) and the remainder is \(-8\).

E. \(\dfrac{5x^2+8x+9}{x^2+x+2}\)

Here we have a quadratic divisor for the first time. One of the methods in the suggestion proposed writing the fraction in this form:

\[\dfrac{5x^2+8x+9}{x^2+x+2} = \dfrac{5x^2+5x+10 +3x - 1}{x^2+x+2}.\]

Written like this we can split it into two fractions.

\[\begin{align*} \dfrac{5x^2+5x+10 +3x - 1}{x^2+x+2}&= \dfrac{5x^2+5x+10}{x^2+x+2}+\dfrac{3x-1}{x^2+x+2} \\ &= 5 + \dfrac{3x-1}{x^2+x+2} \end{align*}\]

This leaves us with a quotient of \(5\) and a remainder of \(3x-1\).

Why is the remainder a linear expression as opposed to a constant like the previous questions?

F. \(\dfrac{x^3-x^2-7x+1}{x^2+2x-1}\)

Using long division gives us,

\[\begin{array}{rll} \phantom{x^2-x^2-7}x-3 & \text{ rem }-2 \cmlongdivbr x^2+2x-1 \cmlongdiv{x^3-\phantom{2}x^2-7x+1} \cmlongdivbr \underline{x^3+2x^2-\phantom{0}x}\phantom{{}+8} && [x \times (x^2+2x-1)] \cmlongdivbr \phantom{x^3}{}-3x^2-6x+1 && \cmlongdivbr \phantom{x^3}\underline{{}-3x^2-6x+3} && [-3 \times (x^2+2x-1)] \cmlongdivbr \phantom{x^3-2x^2-7x}{}-2 && \text{[remainder]} \cmlongdivbr \end{array}\]

which means we can write

\[\dfrac{x^3-x^2-7x+1}{x^2+2x-1} = x -3 +\dfrac{-2}{x^2+2x-1}.\]

Would we always expect the remainder to be a constant when dividing a cubic by a quadratic?

G. \(\dfrac{x^4-3x^3 + x + 1}{x-1}\)

\[\begin{array}{rll} \phantom{x-1}x^3 - 2x^2 - 2x -1 \cmlongdivbr x-1 \cmlongdiv{x^4-3x^3+0x^2 + \phantom{2}x + 1} \cmlongdivbr \underline{x^4- \phantom{3}x^3}\phantom{{}+1x^2+ 1x+8} && [x^3 \times (x-1)] \cmlongdivbr \phantom{x^4}{}-2x^3+ 0x^2\phantom{{}+ 1x+8} && \cmlongdivbr \phantom{x^3}\underline{{}-2x^3+2x^2}\phantom{{}+ 1x+8} && [-2x^2\times(x-1)] \cmlongdivbr \phantom{x^4}{}-2x^2+ \phantom{2}x\phantom{{}+8} && \cmlongdivbr \phantom{x^3}\underline{{}-2x^2+2x}\phantom{{}+8} && [-2x\times(x-1)] \cmlongdivbr \phantom{x^4}{}-x+1 && \cmlongdivbr \phantom{x^3}\underline{{}-x+1} && [-1\times(x-1)] \cmlongdivbr \phantom{x^3-2x^2-7x}{}0 \cmlongdivbr \end{array}\]

What is unusual about the remainder of this problem?

H. \(\dfrac{6x^4 + 5x^3 + x^2 + 10 x -3}{2x^2 + 3x - 1}\)

Using the grid method to divide this expression gives us a completed grid of

|  | \(3x^2\) | \(-2x\) | \(5\) |
|---|---|---|---|
| \(2x^2\) | \(6x^4\) | \(-4x^3\) | \(10x^2\) |
| \(3x\) | \(9x^3\) | \(-6x^2\) | \(15x\) |
| \(-1\) | \(-3x^2\) | \(2x\) | \(-5\) |

which means we can write

\[\begin{align*} \dfrac{6x^4 + 5x^3 + x^2 + 10 x -3}{2x^2 + 3x - 1} &= \dfrac{6x^4 +5x^3+ x^2 +17x - 5 - 7x + 2}{2x^2 + 3x - 1}\\ &= 3x^2 - 2x+5 +\dfrac{-7x+2}{2x^2 + 3x - 1}. \end{align*}\]

The answers from above are summarised in the table.

| Question | Degrees of \(p(x)\) and \(d(x)\) | Degree of \(q(x)\) | Degree of \(r(x)\) |
|---|---|---|---|
| A. | \(1, 1\) | \(0\) | \(0\) |
| B. | \(1,1\) | \(0\) | \(0\) |
| C. | \(2,1\) | \(1\) | \(0\) |
| D. | \(3,1\) | \(2\) | \(0\) |
| E. | \(2,2\) | \(0\) | \(1\) |
| F. | \(3,2\) | \(1\) | \(0\) |
| G. | \(4,1\) | \(3\) | Remainder of \(0\) |
| H. | \(4,2\) | \(2\) | \(1\) |
|  | \(m,n\) |  |  |

The final row has a polynomial of degree \(m\) being divided by a polynomial of degree \(n\). Can you complete this row?

At the beginning we thought about numerical division and asked ‘Why will the remainder will always be less than the divisor?’ Are there any similarities between the remainder and divisor in algebraic division and the remainder and divisor in numerical division?

For G. we have written that the remainder is zero, rather than the degree of the polynomial. The zero polynomial has no nonzero terms so it can be said that the degree is undefined. However it is sometimes useful to define it to be \(-\infty\).

The remainder must have a degree less than the degree of the divisor, otherwise it could be divided further. In this case, the remainder must have a degree of less than 5.

Is it possible to be any more precise about the degree of the remainder?

The quotient must have degree 4. We have been writing the answers to the above questions in the form \[\dfrac{p(x)}{d(x)} = q(x) + \dfrac{r(x)}{d(x)}\] where \(q(x)\) is the quotient and \(r(x)\) is the remainder. This could also be written as \[p(x) = q(x)d(x) + r(x).\]

Since the divisor has degree 5, then the quotient must have degree 4 in order to produce a polynomial of degree 9.
