---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/inequalities
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/many-ways-problem
- level/developing
resource_identity:
  ugm_id: inequalities
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 7416
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
  - code: 3.1.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "Taking it further: solve |x+1|>2|x−1| by branch equations x+1=2(1−x) and x+1=2(x−1) over modulus graphs, and by squaring to (x+1)²=4(x−1)² — modulus graphs in inequality solving"
      rationale: "Canonical UGM title: Inequality sets"
      validation_status: SUGGESTED
    title: "understand the meaning of | x |, sketch the graph of y = | ax + b | and use relations such as"
  - code: 3.1.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "Taking it further: solve |x+1|>2|x−1| by branch equations x+1=2(1−x) and x+1=2(x−1) over modulus graphs, and by squaring to (x+1)²=4(x−1)² — modulus graphs in inequality solving"
      rationale: "Canonical UGM title: Inequality sets"
      validation_status: SUGGESTED
    title: "| a | = | b | ⇔ a² = b² and | x – a | < b ⇔ a – b < x < a + b when solving equations and inequalities"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-9
---

# Inequality sets

> Excerpt: This resource encourages students to think flexibly about inequalities by providing a table where they are asked to fill in the blank spaces so that each row contains a solution set, a graph and an inequality.

## Problem

Fill in the blank spaces so that each row contains:

- an inequality that needs solving

- a graph that can help solve the inequality

- a solution set of the inequality.

Example

| Solution set | Graph | Inequality |
|---|---|---|
| \(\left\{x: x≤-4\right\} \cup \left\{x: x≥-1\right\}\) |  | \(x^2 + 5x + 4 ≥0\) |

| Solution set | Graph | Inequality |
|---|---|---|
| \(\left\{x: 2<x<5\right\}\) |  |  |
| \(\left\{x: 0<x≤1\right\}\) |  |  |
|  |  | \(\dfrac{x^2+5x-6}{x^2+x-6}≥0\) |
|  |  | \(x^2 + 6x > 2x+1\) |
| \(\left\{x: x<-5\right\} \cup \left\{x:-2<x<2\right\}\) |  |  |

Do any of the blank cells have more than one possible answer?

## Solution

Fill in the blank spaces so that each row contains:

- an inequality

- a graph that can help solve the inequality

- a solution set of the inequality.

| Solution set | Graph | Inequality |
|---|---|---|
| \(\left\{x: 2<x<5\right\}\) |  |  |

One way to start might be to think about the solution set on a pair of axes, and then sketching a graph that would fit the constraints.

The graph sketched above is \(y = a(x-2)(x-5)\) where \(a>0\). For the inequality we could suggest something specific such as \((x-2)(x-5) < 0\), or we could be more general and write \(a(x-2)(x-5) < 0\).

What would happen if \(a < 0\)? How would the graph change? How would the inequality change?

| Solution set | Graph | Inequality |
|---|---|---|
| \(\left\{x: 0<x≤1\right\}\) |  |  |

Why can’t this solution set satisfy a quadratic inequality?

We want \(1\) to be included, but \(0\) is not part of the solution. What graphs can we sketch that will satisfy this constraint? Two suggestions are shown here.

| \(\dfrac{1}{x}-1≥0\) | \(\ln x ≤ 0\) |
|---|---|

Both graphs have asymptotes at the \(y\)-axis, which gives the correct solution set since the two functions don’t exist when \(x=0\).

\(y = \dfrac{1}{x^2}-1\) also has an asymptote on the \(y\)-axis and a root at \(x = 1\). Why isn’t the inequality \(\dfrac{1}{x^2}-1≥0\) a possible answer?

| Solution set | Graph | Inequality |
|---|---|---|
|  |  | \(\dfrac{x^2+5x-6}{x^2+x-6}≥0\) |

We want to know where our graph is greater than or equal to zero. To find these sections we need to know the \(x\)-intercepts and the asymptotes.

The two asymptotes can be found by finding for what values the denominator, \(x^2 + x - 6\), equals zero, which is \(x = -3\) and \(x = 2\).

The graph will cross the \(x\)-axis when \(y = 0\), which means when \(x^2 + 5x - 6 =0\). The intercepts are at \(x = -6\) and \(x = 1\).

Therefore the solution set of \(\dfrac{x^2+5x-6}{x^2+x-6}≥0\) is \(\left\{x: x≤-6\right\} \cup \left\{x:-3<x≤1\right\}\cup \left\{x: x>2\right\}\).

| Solution set | Graph | Inequality |
|---|---|---|
|  |  | \(x^2 + 6x > 2x+1\) |

There are several different graphs we could sketch to help us solve \(x^2 + 6x > 2x+1\). Two examples are shown below.

|  |  |
|---|---|

Both examples can be sketched reasonably accurately without having to do any calculations. They give us a way to approximate solutions and enable us to see what the solution set will look like, i.e. \(\left\{x: a<x<b\right\}\) or \(\left\{x: x<a\right\}\cup \left\{x: x>b\right\}\).

What other graphs could be sketched? Are they any more or less helpful than those above?

Finding the intersection points by solving \(x^2 + 6x = 2x+1\) gives us a solution set of \(\left\{x: x<-2-\sqrt{5}\right\} \cup \left\{x: x> -2 + \sqrt{5} \right\}\).

| Solution set | Graph | Inequality |
|---|---|---|
| \(\left\{x: x<-5\right\} \cup \left\{x:-2<x<2\right\}\) |  |  |

The solution set implies that we have three values where the graph switches from positive to negative. If we interpret these as roots then we could sketch a cubic.

This is the graph of \(y = a(x+5)(x+2)(x-2)\) where \(a > 0\), so the inequality will be \(a(x+5)(x+2)(x-2) ≤ 0\).

What if the three values are not all roots? If one of them is an asymptote can you still find a graph that fits the solution set?

## Taking it further

Solve the inequality \(|x+1|>2|x-1|\).

Is it possible to find the solutions without solving any equations?

Things you might have done

There are several approaches that could be taken to solve \(|x+1|>2|x-1|\). If we don’t want to solve any equations we might think about the geometry of the lines. We could start by labelling the graph with any information we know.

At the first intersection, we can create two similar triangles where the corresponding sides are length \(1\) and length \(2\).

How does the ratio of the sides help us to find the \(x\)-coordinate of the intersection point?

For the second intersection we can think about the following triangles.

|  |  |
|---|---|

We know the gradients of the lines, and that the triangles are the same height. What can we deduce about their base lengths?

If we did solve \(|x+1|>2|x-1|\) algebraically we could use the graph to look at the two intersection points and think about which branches of the modulus functions are meeting. This would give us the equations \(x+1 = 2(1-x)\) and \(x+1 = 2(x-1)\) to solve.

Alternatively, we could square both sides to get

\((x+1)^2 = 4(x-1)^2\)

. What does this look like graphically? How do the graphs of

\(y = (x+1)^2\)

and

\(y = 4(x-1)^2\)

relate to the graphs of

\(y = |x+1|\)

and

\(y = 2|x-1|\)

?
