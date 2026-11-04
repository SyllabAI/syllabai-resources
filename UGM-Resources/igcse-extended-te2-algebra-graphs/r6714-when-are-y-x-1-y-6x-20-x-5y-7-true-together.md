---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r6714
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r6714
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6714
  old_site_id: Q74
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: polynomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: polynomials
    validation_status: SUGGESTED
  spec_points:
  - code: E2.6.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: When are y<x+1, y+6x<20, x=5y-7 true together — linear inequalities solved and interpreted;
        E2.6.2 register.
      rationale: 'Canonical UGM title: “When are  $y < x+1, y+6x < 20, x = 5y-7$ true together?”; exam
        provenance: UCLES A level Mathematics B 2, QP 9202/2, 1980, Q2

        Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
        Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

        All rights reserved

        .'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: 'UCLES A level Mathematics B 2, QP 9202/2, 1980, Q2

    Question reproduced by kind permission of Cambridge Assessment Group Archives. The question remains
    Copyright University of Cambridge Local Examinations Syndicate (“UCLES”),

    All rights reserved

    .'
task: T-UGM-IMPORT-19
assets:
- path: https://undergroundmathematics.org/polynomials/r6714/images/lines.png
  kind: figure
- path: https://undergroundmathematics.org/polynomials/r6714/images/quadratic.png
  kind: figure
- path: https://undergroundmathematics.org/polynomials/r6714/images/cubic.png
  kind: figure
- path: https://undergroundmathematics.org/polynomials/r6714/images/intersection.png
  kind: figure
---

# When are  $y < x+1, y+6x < 20, x = 5y-7$ true together?

## Question

1. Find the solution set for \(x\) given that the following three relations for \(x\), \(y\), where \(x\), \(y\in \mathbb{R}\), are simultaneously true: \[y < x+1, \quad y+6x < 20, \quad x = 5y-7.\]
2. Find the solution set of the inequality \[\frac{12}{x-3} < x+1, \quad (x\in \mathbb{R}, \ x \neq 3).\]

## Suggestion

Could we sketch the lines \(y=x+1\), \(y+6x=20\) and \(x=5y-7\)?

How else could we write the inequality?

Could we draw a sketch?

## Solution

A diagram of the three lines helps us visualise the problem.

> [figure: The lines given above (where any inequality signs are replaced by equals signs). Two of the lines are positive gradient, and one is of negative gradient. — `https://undergroundmathematics.org/polynomials/r6714/images/lines.png`] (image not included in the text import; path of record).

The region where y < x + 1 is the half-plane below the blue line. The blue line itself is not in the region.

The region where y + 6x < 20 is the half-plane below the yellow line. The yellow line itself is not in the region.

So we can see the portion of the red line that lies in the region where both inequalities are satisfied.

We need to find the x-values that points on this portion of red line can take.

Rearranging \(x=5y-7\) gives us \[y=\frac{x+7}{5}.\]

Substituting this into the inequalities gives \[\frac{x+7}{5}<x+1 \quad \text{and}\quad \frac{x+7}{5}+6x<20,\] from which we get \[x+7<5x+5 \quad \text{and}\quad x+7+30x<100.\] Solving these gives us \(\dfrac{1}{2}<x\) and \(x<3\) respectively. Therefore the solution set for \(x\) is \(\dfrac{1}{2} < x < 3\).

Alternatively, we could find the point of intersection of the blue line with the red line, and of the yellow line with the red line.

### Approach 1

It’s tempting to multiply both sides by \(x-3\) to give \(12 < (x+1)(x-3)\), but \(x-3\) might be negative, and so multiplying by \(x-3\) could change the direction of the inequality.

So we split the problem up into two cases: \(x-3>0\) and \(x-3<0\).

#### Case 1: \(x-3>0\)

Since \(x-3>0\), we can multiply by \(x-3\) without changing the direction of the inequality to get \(12 < (x+1)(x-3)\).

This is equivalent to \(0<x^2-2x-15\), which we can rewrite as \((x-5)(x+3)>0\).

> [figure: Graph of the quadratic described. It has roots at 5 and minus 3, and is upward-facing. — `https://undergroundmathematics.org/polynomials/r6714/images/quadratic.png`] (image not included in the text import; path of record).

Sketching \(y=(x-5)(x+3)\) shows this inequality holds if \(x<-3\) or if \(x>5\).

Since we are only considering \(x>3\) though, the solution set is \(x>5\).

#### Case 2: \(x-3<0\)

Multiplying by \(x-3\) now means multiplying by a negative value, so we’ll get the same quadratic inequality, but with a different inequality sign, that is, \(0>(x-5)(x+3)\).

Referring to the sketch of \(y=(x-5)(x+3)\), this can only hold when \(-3<x<5\). As we’re only considering \(x<3\), the solution set is \(-3<x<3\).

By combining the results from the two cases, we get the solution set for \(x\) of \(-3<x<3\) or \(x>5\).

### Approach 2

Since multiplying by \(x-3\) might change the sign of the inequality, we’ll multiply by something we know is never negative.

Since we want to multiply by \(x-3\) to clear the denominator, we multiply by \((x-3)^2\ge0\).

This gives us \[12(x-3)<(x+1)(x-3)^2.\]

It’s tempting to now multiply out, but instead, we can use the shared factor of \(x-3\) to rearrange and factorise.

Rearranging and taking out

\(x-3\)

as a factor gives:

\[\begin{align*} &&(x+1)(x-3)^2-12(x-3)&>0&&\quad\\ \iff\quad&&(x-3)((x+1)(x-3)-12)&>0\\ \iff\quad&&(x-3)(x^2-2x-15)&>0\\ \iff\quad&&(x-3)(x-5)(x+3)&>0 \end{align*}\]

This is a cubic which crosses the \(x\)-axis at \(3\), \(5\) and \(-3\), looking roughly like

> [figure: Graph of the cubic described. It tends to infinity as x tends to infinity, and tends to minus infinity as x tends to minus infinity. — `https://undergroundmathematics.org/polynomials/r6714/images/cubic.png`] (image not included in the text import; path of record).

We can see that \((x-3)(x-5)(x+3)>0\) when \(-3<x<3\) or \(x>5\).

### Approach 3

We begin by sketching the two functions \(y=\dfrac{12}{x-3}\) and \(y=x+1\) on the same axes.

The graph of \(y=\dfrac{12}{x-3}\) can be found from \(y=\dfrac{1}{x}\) via stretching in the \(y\)-direction by a factor of \(12\) and then translating by \(3\) in the \(x\)-direction.

So the graph looks like

> [figure: Graph of the curve and the line described. The line crosses the curve twice. — `https://undergroundmathematics.org/polynomials/r6714/images/intersection.png`] (image not included in the text import; path of record).

The two graphs intersect at \(A\) and \(B\), with \(x\)-coordinates \(a\) and \(b\) respectively.

It’s clear from the graph that \(\dfrac{12}{x-3} < x+1\) when the red graph is below the blue one, which occurs when \(a<x<3\) and when \(x>b\).

So it only remains to find \(a\) and \(b\), which we can do by solving the equation \[\frac{12}{x-3} = x+1.\] Multiplying by \(x-3\) and rearranging gives \[(x+1)(x-3)-12=0\] so \[x^2-2x-15=0\] which yields \((x-5)(x+3)=0\), therefore \(x=5\) or \(x=-3\).

This gives \(a=-3\) and \(b=5\), so the solution is \(-3<x<3\) or \(x>5\).

### Approach 4

We have \(\dfrac{12}{x-3}<x+1\), and so bringing everything to the LHS, \(\dfrac{12}{x-3}-x-1<0\), or \(\dfrac{(x-5)(x+3)}{3-x}<0\).

As we now allow \(x\) to move from below \(-3\) to above \(5\), we can track the sign of this rational function, which gives us the same answer as before.
