---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/frightening-function
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/food-for-thought
- level/introducing
resource_identity:
  ugm_id: frightening-function
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Introducing
  ref: 7040
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
  - code: 3.1.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "telescoping via partial-fraction splitting of 1/((x−k)(x−k−1)) terms; Taking it further decomposes three denominators of the (ax+b)(cx+d) type"
      rationale: "Canonical UGM title: Frightening function"
      validation_status: SUGGESTED
    title: "recall an appropriate form for expressing rational functions in partial fractions, and carry out the decomposition, in cases where the denominator is no more complicated than ( ax + b )( cx + d )( ex + f ), ( ax + b )( cx + d )², ( ax + b )( cx² + d )"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-9
---

# Frightening function

> Excerpt: Students have to decide how to manipulate algebraic fractions in order to simplify a frightening looking function. This can be used as an introduction to partial fractions.

## Problem

Simplify the function

\[f(x) = \dfrac{(x-1)-(x-2)}{(x-1)(x-2)} + \dfrac{(x-2)-(x-3)}{(x-2)(x-3)} + \dfrac{(x-3)-(x-4)}{(x-3)(x-4)} + \dfrac{(x-4)-(x-5)}{(x-4)(x-5)}.\]

Taking it further

Is it possible to split each of the following fractions up into the sum of two fractions?

- \(\dfrac{1}{(x-2)(x-3)}\)

- \(\dfrac{7}{(x-1)(x-8)}\)

- \(\dfrac{1}{(x-2)(x-8)}\)

## Suggestion

Think about the following questions. Some may be more helpful than others.

- Can a common denominator be found?

- What happens if we simplify the numerator? What might the next step be?

- Look at the individual fractions, e.g. \(\dfrac{(x-1)-(x-2)}{(x-1)(x-2)}\). Can it be split into simpler fractions?

How does the fraction \(\dfrac{(x-2)-(x-3)}{(x-2)(x-3)}\) help?

Do you think all these fractions can be written in the form \(\dfrac{A}{(x-p)} + \dfrac{B}{(x-q)}\)?

## Solution

We will explore the possible starting points given in the suggestion:

**Common denominator**

When we add fractions we need a common denominator. In this case it would be \((x-1)(x-2)(x-3)(x-4)(x-5).\) The first term would become \[\dfrac{\big((x-1)-(x-2)\big)(x-3)(x-4)(x-5)}{(x-1)(x-2)(x-3)(x-4)(x-5)}.\]

Writing out the whole function would be very long, so we will introduce notation that will help us write \(f(x)\) in a shorter way, and should make it easier to spot any structure or symmetry that occurs. \[(x - a_1)(x-a_2)...(x-a_n) = [a_1a_2...a_n]\] So \((x-1)(x-2)(x-3)\) would be written \([123]\).

\[f(x) = \dfrac{([1]-[2])[345] + ([2]-[3])[145] + ([3]-[4])[125] + ([4]-[5])[123]}{[12345]}\]

Possible next steps

Multiplying out the brackets gives us

\[f(x) = \dfrac{[1345]-[2345]+[1245]-[1345]+[1235]-[1245]+[1234]-[1235]}{[12345]},\]

which has terms in the numerator that cancel, leaving us with

\[f(x) = \dfrac{[1234]-[2345]}{[12345]}.\]

Did you spot that the terms were going to cancel before expanding the brackets?

Written in our ordinary algebraic notation we have \[\dfrac{(x-1)(x-2)(x-3)(x-4) - (x-2)(x-3)(x-4)(x-5)}{(x-1)(x-2)(x-3)(x-4)(x-5)},\] so we can simplify the common factors leaving us with \[f(x) = \dfrac{(x-1)-(x-5)}{(x-1)(x-5)} \text{ or } f(x) = \dfrac{4}{(x-1)(x-5)}.\]

**Simplifying the numerator**

It turns out that the numerator for each fraction simplifies to \(1\). This seems helpful but then we are left with \[f(x) = \dfrac{1}{(x-1)(x-2)} + \dfrac{1}{(x-2)(x-3)} + \dfrac{1}{(x-3)(x-4)} + \dfrac{1}{(x-4)(x-5)}.\] Where might we go from here?

Possible next steps

It seems sensible to think about creating a common denominator for the terms as we did above. Written in our new notation we can write \[f(x) = \dfrac{[345]+[145]+[125]+[123]}{[12345]}.\]

There don’t seem to be any terms that cancel in the numerator, or any common factors that would allow the fraction to be simplified.

What happens if we create a common denominator for a pair of fractions instead? E.g. \(\dfrac{1}{(x-1)(x-2)} + \dfrac{1}{(x-2)(x-3)}.\)

**Simplifying terms**

Each term can be split into two fractions, e.g. \[\dfrac{(x-1) - (x-2)}{(x-1)(x-2)} = \dfrac{(x-1)}{(x-1)(x-2)} - \dfrac{(x-2)}{(x-1)(x-2)},\] which gives us fractions with common factors that can be simplified.

\[\begin{align*} f(x) &= \dfrac{(x-1)}{(x-1)(x-2)} - \dfrac{(x-2)}{(x-1)(x-2)} + \cdots + \dfrac{(x-4)}{(x-4)(x-5)}- \dfrac{(x-5)}{(x-4)(x-5)} \\ &= \dfrac{1}{(x-2)} - \dfrac{1}{(x-1)} + \dfrac{1}{(x-3)} - \dfrac{1}{(x-2)}+ \dfrac{1}{(x-4)} - \dfrac{1}{(x-3)}+ \dfrac{1}{(x-5)}- \dfrac{1}{(x-4)} \end{align*}\]

We can see that many of the terms appear twice, in fact most terms have a pair with which they will cancel. We call this a telescoping sum. This leaves us with

\[f(x) = \dfrac{1}{x-5} - \dfrac{1}{x-1}.\]

This method is based around the idea of splitting a fraction up into the sum of simpler fractions which is called [partial fraction decomposition](https://undergroundmathematics.org/glossary/partial-fractions).

We ended up with \(f(x)\) written in two different forms, let’s call them \(f_1\) and \(f_2\): \[f_1(x) = \dfrac{1}{x-5} - \dfrac{1}{x-1} \text{ and } f_2(x) = \dfrac{4}{(x-1)(x-5)}.\]

- How would we show that \(f_1\) can be rewritten as \(f_2\)?

- Starting with \(f_2\), how would we show it can be rewritten as \(f_1\)?

Depending on the approach taken to simplify \(f(x)\), we may have already noticed that \(\dfrac{1}{(x-2)(x-3)} = \dfrac{(x-2)-(x-3)}{(x-2)(x-3)}.\)

Therefore we can use the simplifying terms approach from above and split this into two fractions:

\[\begin{align*} \dfrac{1}{(x-2)(x-3)} &= \dfrac{(x-2)-(x-3)}{(x-2)(x-3)} \\ &= \dfrac{(x-2)}{(x-2)(x-3)} - \dfrac{(x-3)}{(x-2)(x-3)} \\ &= \dfrac{1}{(x-3)} - \dfrac{1}{(x-2)} \end{align*}\]

How are the examples below different from this? How are they the same?

This is the same in that

\((x-1) - (x-8) = 7\)

and so the same technique can be applied to split the fraction in two.

\[\begin{align*} \dfrac{7}{(x-1)(x-8)} &= \dfrac{(x-1)-(x-8)}{(x-1)(x-8)} \\ &= \dfrac{1}{(x-8)} - \dfrac{1}{(x-1)} \end{align*}\]

This is different in that we can’t just rewrite the numerator in terms of the brackets that appear in the denominator. Or can we? What if we have multiples of each bracket? \[\dfrac{1}{(x-2)(x-8)} = \dfrac{A(x-2) - B(x-8)}{(x-2)(x-8)}\]

This would give us \(Ax - 2A - Bx + 8B = 1\) and so we can write down two equations, \(A-B = 0\) and \(-2A + 8B = 1\), which solve to give \(A = \frac{1}{6}\) and \(B = \frac{1}{6}\).

\[\dfrac{1}{(x-2)(x-8)}= \dfrac{1/6}{(x-8)} - \dfrac{1/6}{(x-2)}\]

Could we have worked this out in a different way if we thought about what \(\dfrac{6}{(x-2)(x-8)}\) could be rewritten as?

Is it possible to write all fractions in the form \(\dfrac{p}{(x-q)(x-r)}\) as \(\dfrac{A}{(x-q)} + \dfrac{B}{(x-r)},\) where \(p, q, r, A\) and \(B\) are constants? What happens if \(q = r\)?
