---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r6577
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r6577
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6577
  old_site_id: "Q1065"
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
      evidence: "remainder-theorem evaluations f(±2), factor theorem on the zero remainder → complete factorisation of the cubic, then exact divisibility by the quadratic x²+x−6 via its linear factors"
      rationale: "Canonical UGM title: Can we factorise $6x^3+5x^2-17x-6$ completely?"
      validation_status: SUGGESTED
    title: "divide a polynomial, of degree not exceeding 4, by a linear or quadratic polynomial, and identify the quotient and remainder (which may be zero)"
  - code: 3.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "remainder-theorem evaluations f(±2), factor theorem on the zero remainder → complete factorisation of the cubic, then exact divisibility by the quadratic x²+x−6 via its linear factors"
      rationale: "Canonical UGM title: Can we factorise $6x^3+5x^2-17x-6$ completely?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES AO level Additional Mathematics 2, QP 8175/2, 1984, Q12"
  task: T-UGM-IMPORT-9
---

# Can we factorise $6x^3+5x^2-17x-6$ completely?

## Question

1. Given that \(f(x)=6x^3+5x^2-17x-6\),  find the remainder when \(f(x)\) is divided by \(x-2\), find the remainder when \(f(x)\) is divided by \(x+2\), factorise \(f(x)\) completely.

---

1. Given that the expression \(ax^3-x^2+bx+18\) is exactly divisible by \(x^2+x-6\), find the value of \(a\) and \(b\).

## Suggestion

Would it help us to recall the [remainder theorem](https://undergroundmathematics.org/glossary/remainder-theorem)?

\(\qquad\) iii. factorise \(f(x)\) completely.

Can we find a remainder that is zero? What does this tell us about the roots of \(f(x)\)?

Would it help to try to factorise \(x^2+x-6\)?

## Solution

The remainder theorem tells us that if \(f(c)=r\) for some polynomial \(f(x)\), then \(r\) is the remainder when \(f(x)\) is divided by \(x-c\).

In our case, \(c\) is \(2\) for the first part, and \(-2\) for the second.

We can now substitute these values into \(f(x)\), giving

\[\begin{align*} f(+2)&=28,\\ f(-2)&=0. \end{align*}\]

Therefore the remainder when \(f(x)\) is divided by \(x-2\) is \(28\), and the remainder on dividing by \(x+2\) is \(0\).

\(\qquad\) (iii) factorise \(f(x)\) completely.

Since the remainder of \(f(x)\) divided by \(x+2\) is zero, we know \(x+2\) is a factor of \(f(x)\).

Check the [factor theorem](https://undergroundmathematics.org/glossary/factor-theorem) if you need to…

We now know that \(f(x)\) is of the form \((x+2)(ax^2+bx+c)\), where \(a\), \(b\) and \(c\) are constants to be found. This means \[f(x) = 6x^3 + 5x^2 - 17x - 6 = (x+2)(ax^2+bx+c).\]

We can find \(a\), \(b\) and \(c\) by considering the coefficients of the different powers of \(x\).

The only cubic term on the right hand side is \(ax^3\), so we can see by comparing it with the left hand side that \(a = 6\).

The constant term is \(2c\), which must equal \(-6\), and so \(c = -3\).

There’ll be two square terms in the expansion of the right hand side, namely

\(12x^2\)

and

\(bx^2\)

. Therefore

\[\begin{align*} 12 + b &= 5 \\ \implies b &= -7. \end{align*}\]

We can check this by looking at the linear terms; on the right hand side, we get

\(2bx\)

and

\(-3x\)

, so

\[\begin{align*} 2b - 3 &= -17 \\ \implies 2b &= -14 \\ \implies b &= -7, \quad \text{as above}. \end{align*}\]

Therefore we can write \(f(x) = (x + 2)(6x^2 - 7x - 3)\).

The quadratic bracket here can be factorised by inspection, or by using the quadratic formula if we’re stuck. We find that \[f(x) = (x + 2)(3x + 1)(2x - 3).\]

Or we could use polynomial division…

We could also have found the quadratic \(6x^2 - 7x - 3\) by using polynomial division. \[\begin{array}{r} 6x^2\phantom{1}{}-7x-3 \cmlongdivbr x+2 \cmlongdiv{6x^3\phantom{1}{}+5x^2-17x-6} \cmlongdivbr \underline{6x^3+12x^2}\phantom{{}-17x-6} \cmlongdivbr \phantom{6x^3}{}-7x^2-17x\phantom{{}-6} \cmlongdivbr \phantom{6x^3}{}\underline{{}-7x^2-14x}\phantom{{}-6} \cmlongdivbr \phantom{6x^3+5x^2}{}-3x-6 \cmlongdivbr \phantom{6x^3+5x^2}\underline{{}-3x-6} \cmlongdivbr \phantom{6x^3+5x^2-17x+{}}0 \cmlongdivbr \end{array}\]

Although the question doesn’t ask for this, click below for a plot of \(y=f(x)\), with the three roots indicated.

Show Plot

Let’s factorise; \(x^2 + x - 6 = (x + 3)(x - 2)\).

So we know that \((x-2)\) and \((x+3)\) are factors of the above cubic expression, and so if we substitute in \(x=2\) or \(x=-3\) to this cubic, the result has to be zero.

This leads to the following pair of equations:

\[\begin{align} 8a+2b+14&=0 \quad \implies \quad 4a + b + 7 = 0 \label{eq:I}\\ -27a-3b+9&=0 \quad \implies \quad -9a - b + 3 = 0. \label{eq:II} \end{align}\]

We can solve these by adding them together:

\[\begin{align*} -5a + 10 &= 0 \\ \implies a &= 2, \end{align*}\]

and substituting into

\(\eqref{eq:I}\)

, we find

\[\begin{align*} 4 \times 2 + b + 7 &= 0 \\ \implies b &= -15. \end{align*}\]

We can check this by substituting both \(a\) and \(b\) into \(\eqref{eq:II}\): \[-9 \times 2 - (-15) + 3 = 0.\]

We therefore find \(a= 2\), \(b = 15\), and that the full cubic function is \(2x^3-x^2-15x+18\).
