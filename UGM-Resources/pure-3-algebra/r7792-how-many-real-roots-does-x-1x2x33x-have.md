---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/r7792
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/review-question
resource_identity:
  ugm_id: r7792
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7792
  old_site_id: "Q70"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 3.1.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "Express 3x/((x−1)(x+2)) in partial fractions is asked outright (cover-up and coefficient comparison both shown), then used to differentiate and sketch the curve"
      rationale: "Canonical UGM title: How many real roots does $(x-1)(x+2)(x+3)=3x$ have?"
      validation_status: SUGGESTED
    title: "recall an appropriate form for expressing rational functions in partial fractions, and carry out the decomposition, in cases where the denominator is no more complicated than ( ax + b )( cx + d )( ex + f ), ( ax + b )( cx + d )², ( ax + b )( cx² + d )"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Mathematics A 1 and Pure Mathematics 1, QP 9200/1 and 9208/1, 1984, Q11"
  task: T-UGM-IMPORT-9
---

# How many real roots does $(x-1)(x+2)(x+3)=3x$ have?

## Question

Express \(\dfrac{3x}{(x-1)(x+2)}\) in partial fractions.

Show that \(\dfrac{dy}{dx}\) is negative at all points on the graph of \[y=\frac{3x}{(x-1)(x+2)}.\]

Sketch this graph, showing the two asymptotes parallel to the \(y\)-axis and the asymptote perpendicular to the \(y\)-axis.

By sketching on the same diagram a second graph (the equation of which should be stated), or otherwise, find the number of real roots of the equation \[(x-1)(x+2)(x+3)=3x.\]

## Suggestion

How does using partial fractions help us to differentiate the expression?

Things to look out for when curve sketching:

- asymptotes;

- intercepts;

- stationary points and their nature;

- behaviour as \(x\rightarrow \pm \infty\).

Can we make this look something like the graph we’ve just sketched?

Could we make the roots of the equation into the intersections between the original graph and the new graph?

## Solution

Let \[\frac{3x}{(x-1)(x+2)} = \frac{A}{x-1} + \frac{B}{x+2}\]

Then by multiplying through by \((x-1)(x+2)\), we have \[3x = A(x+2) + B(x-1).\]

If we let

\(x = 1\)

, then our equation becomes

\[\begin{align*} 3 = 3A, \\ \text{so} \qquad A = 1. \end{align*}\]

If we now choose to use

\(x = -2\)

, then we have

\[\begin{align*} -6 = -3B, \\ \text{so} \qquad B = 2. \end{align*}\]

Alternatively, we can compare coefficients.

Comparing coefficients

We first need to expand the terms on the right hand side of the equation:

\[\begin{align*} 3x = Ax + 2A + Bx - 1B, \\ \text{so} \qquad 3x = (A + B)x + (2A - B). \end{align*}\]

Looking at the constant terms on each side of the equation, we see that \(2A - B = 0\), and looking at the terms in \(x\) on each side, we find \(3 = A + B\).

Adding these two equations gives \(A = 1\), and from there \(B = 2\).

So we have \[\frac{3x}{(x-1)(x+2)} = \frac{1}{x-1} + \frac{2}{x+2}.\]

We differentiate the partial fractions to obtain \[\frac{dy}{dx} = -\frac{1}{(x-1)^2} - \frac{2}{(x+2)^2}.\]

We can see that this must be negative at all points, because each term is negative.

The gradient is not defined at \(x = 1, -2\).

When \(x = 0\), \(y = 0\). There are no other points where the curve crosses the axes.

The two asymptotes parallel to the \(y\)-axis are \(x=1\) and \(x=-2\).

We have determined that \(\dfrac{dy}{dx}\) is always negative, and so it cannot equal \(0\), and thus there are no stationary points.

We also observe that as \(x\rightarrow \pm \infty\), \(y\rightarrow 0\).

We can now confidently sketch the graph:

We observe that the equation can be rearranged to \[x+3=\frac{3x}{(x-1)(x+2)},\] which suggests sketching the graph \(y=x+3\) onto the original graph.

There are three points of intersection for the two graphs, so there are three real roots for the equation \((x-1)(x+2)(x+3)=3x\).
