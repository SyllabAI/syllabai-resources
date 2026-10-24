---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r6431
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r6431
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6431
  old_site_id: "Q68"
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
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "rational-root search on 3x³+14x²+2x−4 (factor-theorem candidate testing) completes the cubic left by the squared surd equation"
      rationale: "Canonical UGM title: Can we solve  $\\sqrt{4x+13}-\\sqrt{x+1}=\\sqrt{12-x}?$"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Mathematics Scholarship paper, QP 183, 1954, Q1"
  task: T-UGM-IMPORT-9
---

# Can we solve  $\sqrt{4x+13}-\sqrt{x+1}=\sqrt{12-x}?$

## Question

1. Solve \[\sqrt{4x+13}-\sqrt{x+1}=\sqrt{12-x}.\]

---

1. One root of the equation \[3x^3+14x^2+2x-4=0\] is rational. Obtain this root and complete the solution of the equation.

## Suggestion

How could we get rid of the square roots?

Squaring both sides of this will still leave a square root, but could we rearrange and square again?

If we do this, will our solutions all be valid?

What does the question mean by ‘rational’?

We could write this root as \(\dfrac{a}{b}\), where the fraction is in lowest terms. What happens if we substitute this into the cubic and simplify?

Since \(a\) and \(b\) have no common factors, what does this tell us?

Can you find any ways to minimise the number of possibilities for \(a\) and \(b\) that need checking? Can we then check all the possibilities?

## Solution

Squaring both sides of the equation gives us

\[\begin{align*} &(4x+13)+(x+1)-2\sqrt{(4x+13)(x+1)} = 12-x\\ \Longrightarrow\quad& 5x+14-12+x = 2\sqrt{(4x+13)(x+1)}\\ \Longrightarrow\quad& 3x+1 = \sqrt{(4x+13)(x+1)}. \end{align*}\]

Squaring again implies that

\[\begin{align*} &9x^2+6x+1 = (4x+13)(x+1)=4x^2+17x+13 \\ \Longrightarrow\quad& 5x^2-11x-12 = 0 \\ \Longrightarrow\quad& (5x+4)(x-3) = 0 \end{align*}\]

and so \(x = -\dfrac{4}{5}\) or \(x = 3\).

We know now that these are the only two possibilities for a solution. There is a problem, however; squaring may have intrduced false roots.

For example, if we have \(x=\sqrt{x+2}\), then squaring gives \(x^2 = x+2\), and so \((x-2)(x+1)=0\), and \(x = 2\) or \(-1\).

But \(2\) works in our original equation, while \(-1\) does not. So \(-1\) is a false root, and \(2\) is the only true solution.

So we need to check whether or not the possible solutions above satisfy our original equation.

If \(x = -\dfrac{4}{5}\), then the left-hand side is \[\sqrt{4\left(-\dfrac{4}{5}\right)+13}-\sqrt{-\dfrac{4}{5} + 1} = \sqrt{\dfrac{49}{5}}-\sqrt{\dfrac{1}{5}}=\dfrac{1}{\sqrt{5}}(7-1)=\dfrac{6}{\sqrt{5}},\] while the right-hand side is \[\sqrt{12+\dfrac{4}{5}}=\sqrt{\dfrac{64}{5}}=\dfrac{8}{\sqrt{5}},\] which are not equal. Thus \(x=-\dfrac{4}{5}\) is not a solution.

If \(x=3\), then the left-hand side is \[\sqrt{4\times 3+13}-\sqrt{3 + 1}=5-2=3\] while the right-hand side is \[\sqrt{12-3}=\sqrt{9}=3.\] Thus \(x=3\) is the only solution to the original equation.

1. One root of the equation \(3x^3+14x^2+2x-4=0\) is rational. Obtain this root and complete the solution of the equation.

Let \(f(x)=3x^3+14x^2+2x-4\). Assume the given rational root is \(\dfrac{a}{b}\), where the highest common factor of \(a\) and \(b\) is \(1\) and, without loss of generality, \(b>0\).

Substituting this solution into \(f(x)=0\) and multiplying through by \(b^3\) we find \[3a^3+14a^2b+2ab^2-4b^3=0.\] Note that this means \(b\) divides \(3a^3\) (since it divides every other term) and so \(b\) is \(1\) or \(3\) (since it cannot share a factor with \(a\)).

Now \(2\) divides \(14a^2b+2ab^2-4b^3\), and so \(2\) divides \(3a^3\), and thus \(2\) divides \(a\), say \(a = 2c\). This gives us \[6c^3 + 14c^2b + cb^3 - b^3 = 0,\] and so \(c\) divides \(b^3\). But \(c\) and \(b\) have no common factor, and so \(c\) must be \(\pm 1\), and \(a\) must be \(\pm 2\).

So the only possible rational roots for the equation are \(\dfrac{2}{3}, -\dfrac{2}{3}, 2\) or \(-2\).

It is easy to check that \(-\dfrac{2}{3}\) is the only one to satisfy the equation. Thus \(x=-\dfrac{2}{3}\) is the rational root. Factorising the cubic we find \[3x^3 + 14x^2 + 2x - 4 = (3x+2)(x^2+4x-2)=0.\] So either \(x = -\dfrac{2}{3}\), or \(x^2+4x-2=0\) and so \[x=\dfrac{-4\pm\sqrt{16-4\times(-2)}}{2}=-2\pm\sqrt{6}.\]
