---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r7035
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r7035
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7035
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Rational inequality reduces to a quadratic inequality (critical values).
      rationale: 'Canonical UGM title: “Can we solve $12/(x-3) < x+1$?”; exam provenance: UCLES 1980 Q2'
      validation_status: SUGGESTED
    title: solve quadratic equations, and quadratic By factorising, completing the square and using the
      inequalities, in one unknown formula.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1980 Q2
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/r7035/images/img-7035.svg
  kind: figure
- path: https://undergroundmathematics.org/quadratics/r7035/images/img-7035b.svg
  kind: figure
---

# Can we solve $12/(x-3) < x+1$?

## Question

1. Find the solution set for \(x\) given that the following three relations for \(x\), \(y\), where \(x, y \in \mathbb{R}\), are simultaneously true: \[\begin{equation*} y < x + 1, \quad y + 6x < 20, \quad x = 5y - 7. \end{equation*}\]
2. Find the solution set of the inequality \[\begin{equation*} \frac{12}{x-3} < x + 1, \quad (x \in \mathbb{R}, x \ne 3). \end{equation*}\]

## Suggestion

We might get some useful insight into what is happening here by drawing a sketch.

Again, a sketch might be helpful here, to help check that our answer is sensible. Remember that \(x-3\) might be positive or negative.

## Solution

It helps to sketch a diagram; here, the regions included by the inequalities are shaded.

> [figure: the two inequalities and one line sketched on a single diagram — `https://undergroundmathematics.org/quadratics/r7035/images/img-7035.svg`] (image not included in the text import; path of record).

From the sketch, we can see that the solution set for \(x\) consists of the \(x\)-coordinates of points lying on the line between \(A\) and \(B\).

We can find the coordinates of \(A\) by solving the simultaneous equations \[y=x+1\quad\text{and}\quad x=5y-7.\] Substituting the second equation into the first gives \[y=5y-6\] so that \(y=\frac64=\frac32\). Thus \(x=y-1=\frac12\), and \(A\) has coordinates \((\frac12, \frac32)\).

Likewise, the coordinates of \(B\) are found by solving \[y+6x=20\quad\text{and}\quad x=5y-7.\] Again, substitution gives \[y+30y-42=20\] which yields \(y=2\) and hence \(x=3\), so \(B\) has coordinates \((3,2)\).

Thus the solution set for \(x\) is \(\frac{1}{2} < x < 3\).

1. Find the solution set of the inequality \[\begin{equation*} \frac{12}{x-3} < x+1, \quad (x \in \mathbb{R}, x \ne 3). \end{equation*}\]

We might be tempted to multiply through by \(x-3\), but then we have to worry about its sign, and whether or not we need to change the direction of the inequality.

A sketch might again help us to follow what is happening.

> [figure: the two equations y equals 12 over x minus 3 and y equals x plus 1 sketched on a single diagram — `https://undergroundmathematics.org/quadratics/r7035/images/img-7035b.svg`] (image not included in the text import; path of record).

So \(\dfrac{12}{x-3}<x+1\) when we are between \(A\) and \(x=3\) and when we are to the right of \(B\).

We can find the \(x\)-coordinates of \(A\) and \(B\) by solving the equation \[\dfrac{12}{x-3}=x+1.\] Multiplying both sides by \(x-3\) gives \(12=(x+1)(x-3)\), which rearranges to \(x^2-2x-15=0\).

We can factorise this to get \((x-5)(x+3)=0\), so \(A\) has \(x\)-coordinate \(-3\) and \(B\) has \(x\)-coordinate \(5\).

Thus the solution set is \(-3<x<3\) or \(x>5\).

An alternative approach is to manipulate the inequality directly. But we cannot simply multiply by

\(x-3\)

, as this may be positive or negative. Instead, we can rearrange the inequality to get zero on one side, by subtracting one side from the other:

\[\begin{align*} &&x+1&>\frac{12}{x-3}\\ \iff&& x+1-\frac{12}{x-3}&>0\\ \iff&& \frac{(x+1)(x-3)-12}{x-3}&>0\\ \iff&& \frac{(x+3)(x-5)}{x-3}&>0. \end{align*}\]

Now the expression on the left changes sign at \(x = -3\), \(x = 3\) and \(x = 5\), and so we can make a table showing the sign of the expression:

|  | \(x<-3\) | \(-3<x<3\) | \(3<x<5\) | \(x>5\) |
| --- | --- | --- | --- | --- |
| \(x+3\) | \(-\) | \(+\) | \(+\) | \(+\) |
| \(x-5\) | \(-\) | \(-\) | \(-\) | \(+\) |
| \(x-3\) | \(-\) | \(-\) | \(+\) | \(+\) |
| \(\dfrac{(x+3)(x-5)}{x-3}\) | \(-\) | \(+\) | \(-\) | \(+\) |

Thus the solution set (where the expression is positive) is \(-3<x<3\) or \(x>5\).

Another technique is to multiply both sides of the inequality by \((x-3)^2\), as this is never negative; the resulting inequality can be solved in essentially the same way as we have done here.
