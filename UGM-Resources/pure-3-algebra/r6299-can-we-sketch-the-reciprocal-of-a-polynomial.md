---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r6299
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r6299
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6299
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
  - code: 3.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "factor theorem with a value table finds the root x=2 of x³−3x−2, then complete factorisation (x−2)(x+1)²; the reciprocal-curve sketch reads the double root"
      rationale: "Canonical UGM title: Can we sketch the reciprocal of a polynomial?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Pure Mathematics 1, QP 9210/1, 1980, Q4"
  task: T-UGM-IMPORT-9
---

# Can we sketch the reciprocal of a polynomial?

## Question

Express \(x^3 - 3x - 2\) as the product of three linear factors.

Show that \(x^3 - 3x - 2\) may also be expressed in the form \((x-1)^2(x+p) + q\), where \(p\) and \(q\) are constants to be found. Hence, or otherwise, show that the curve whose equation is \(y = x^3 - 3x - 2\) has a minimum point where \(x = 1\).

Sketch the curve whose equation is

\[\begin{equation*} y = \frac{1}{x^3 - 3x - 2}, \end{equation*}\]

indicating clearly all its asymptotes. Hence obtain the number of real roots of the equation

\[\begin{equation*} (x+1)(x^3 - 3x - 2) = 1. \end{equation*}\]

## Solution

By the [factor theorem](https://undergroundmathematics.org/glossary/factor-theorem), a polynomial \(f(x)\) has a linear factor \((x-a)\) if and only if \(f(a) = 0\).

If we let \(f(x) = x^3 - 3x - 2\), we have

| \(x\) | \(0\) | \(1\) | \(2\) |
|---|---|---|---|
| \(f(x)\) | \(-2\) | \(-4\) | \(0\) |

So \((x-2)\) is a factor of \(f(x) = x^3 - 3x - 2\), and \(f(x) = (x-2)(x^2+ax+1)\).

Since \(f(x)\) has no \(x^2\) term, \(a = 2\), and \(f(x)\) can be factorised completely as \[f(x) = (x-2)(x+1)^2,\] which is the product of three linear factors.

By expanding and collecting powers of

\(x\)

, we see that

\[\begin{align*} (x-1)^2(x+p) + q &= (x^2 - 2x + 1)(x+p) + q \\ &= x^3 + px^2 - 2x^2 - 2px + x + p + q \\ &= x^3 + (p-2)x^2 + (1-2p)x + p + q. \end{align*}\]

Can we write for all

\(x\)

\[\begin{equation*} x^3 - 3x - 2 = x^3 + (p-2)x^2 + (1-2p)x + p + q \end{equation*}\]

for some \(p\) and \(q\)?

By equating coefficients, we need

\(p\)

and

\(q\)

that satisfy

\[\begin{align*} 0 &= p - 2, \\ -3 &= 1 - 2p, \\ -2 &= p + q \end{align*}\]

simultaneously. The first gives us

\(p = 2\)

, as does the second, and the third becomes

\(q = -4\)

. So we can write down the identity

\[\begin{equation*} x^3 - 3x - 2 = (x-1)^2(x+2) - 4. \end{equation*}\]

We know \(f(x) = (x-1)^2(x+2) - 4\). When \(x = 1\), \(f(x) = -4\).

When \(x =1 + \alpha\), where \(\alpha\) is small and positive, then \(f(x) = \alpha^2(3+\alpha)-4 > -4\).

When \(x = 1 - \alpha\), then \(f(x) = \alpha^2(3-\alpha)-4 > -4\). Thus \(y = f(x)\) has a minimum at \(x = 1\).

Or else we can differentiate. If \(y = f(x) = x^3 -3x -2\), then \(y' = 3x^2-3 = 0\) when \(x = 1\).

We have \(y'' = 6x = 6\) when \(x = 1\), which is positive, so we have a minimum.

We know

\[\begin{equation*} y = \frac{1}{x^3 - 3x - 2} = \frac{1}{(x-2)(x+1)^2} = \frac{1}{(x-1)^2(x+2) - 4}. \end{equation*}\]

In sketching the graph, we will ask four questions:

1. what are the intercepts?

When \(x = 0\), \(y = -\dfrac{1}{2}\). This is the \(y\)-intercept of the curve. There are no \(x\)-intercepts, since the numerator of \(y\) can never equal zero.

1. what is the asymptotic behaviour?

There are two vertical asymptotes (corresponding to the roots of the denominator) at \(x = -1\) and \(x = 2\).

Since the denominator of \(y\) tends towards \(\pm \infty\) as \(x\) tends towards \(\pm \infty\), and as the numerator is constant, we can see \(y \to 0\) as \(x \to \pm \infty\). Thus there is one horizontal asymptote, \(y = 0\).

1. where is \(y\) positive and negative?

The sign of \(y\) depends wholly on the sign of \((x-2)\), since \((x+1)^2\) is never negative, and so \(y > 0\) if \(x > 2\) and \(y < 0\) if \(x < 2\) (provided that \(x \ne -1\)).

1. are there any turning points?

Finally, the denominator has a local minimum at \(x = 1\), and so its reciprocal \(y\) must have a local maximum at \(x = 1\).

We can now sketch \(y\):

We can rewrite this equation as

\[\begin{equation*} x+1 = \frac{1}{x^3 - 3x - 2}. \end{equation*}\]

(Clearly \(x^3 - 3x - 2\) cannot be zero, since in this case the equation is not satisfied.) A real solution to this equation corresponds precisely to an intersection between the line \(y = x+1\) and the curve \(y = \dfrac{1}{x^3 - 3x - 2}\).

Thus we have this sketch of the line and the curve. There are two intersections, and hence there are two real roots to the equation.
