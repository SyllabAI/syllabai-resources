---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r6246
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r6246
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6246
  old_site_id: Q82
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
      evidence: Quadratic formula with literal coefficients.
      rationale: 'Canonical UGM title: “Can we solve $nx^2+2x\sqrt{pn^2+q}+rn+s=0$?”; exam provenance:
        UCLES 1999 Q2'
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
  exam_reference: UCLES 1999 Q2
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/r6246/images/q82sketch1.png
  kind: figure
- path: https://undergroundmathematics.org/quadratics/r6246/images/q82negquad.png
  kind: figure
- path: https://undergroundmathematics.org/quadratics/r6246/images/q82sketch2.png
  kind: figure
---

# Can we solve $nx^2+2x\sqrt{pn^2+q}+rn+s=0$?

## Question

Consider the quadratic equation

\[\begin{equation*} nx^2+2x\sqrt{pn^2+q}+rn+s=0, \tag{$*$} \label{eq:star} \end{equation*}\]

where \(p>0\), \(p\ne r\) and \(n=1\), \(2\), \(3\), \(\dots\).

1. For the case where \(p=3\), \(q=50\), \(r=2\), \(s=15\), find the set of values of \(n\) for which equation \(\eqref{eq:star}\) has no real roots.
2. Prove that if \(p<r\) and \(4q(p-r)>s^2\), then \(\eqref{eq:star}\) has no real roots for any value of \(n\).
3. If \(n=1\), \(p-r=1\) and \(q=s^2/8\), show that \(\eqref{eq:star}\) has real roots if, and only if, \(s\le 4-2\sqrt{2}\) or \(s\ge 4+2\sqrt{2}\).

## Solution

where \(p>0\), \(p\ne r\) and \(n=1\), \(2\), \(3\), \(\dots\).

1. For the case where \(p=3\), \(q=50\), \(r=2\), \(s=15\), find the set of values of \(n\) for which equation \(\eqref{eq:starrepeat}\) has no real roots.

 Consider the quadratic equation

\[\begin{equation*} nx^2+2x\sqrt{pn^2+q}+rn+s=0, \tag{$*$} \label{eq:starrepeat} \end{equation*}\]

Let’s first substitute in the values we are given. We want to know for which

\(n\)

the equation

\[\begin{equation} nx^2+2x\sqrt{3n^2+50}+2n+15=0 \label{eq:1} \end{equation}\]

has no real roots.

We therefore want to determine the values of

\(n\)

for which the

is negative, that is,

\(n\)

such that

\[\begin{align*} &4(3n^2+50)-4n(2n+15) <0\\ \iff\quad & (3n^2+50)-n(2n+15) <0\\ \iff\quad & n^2 -15n +50 <0\\ \iff\quad & (n-5)(n-10) <0.\\ \end{align*}\]

We can now sketch the graph of \(y = (n-5)(n-10)\).

> [figure: Graph of y =  n squared minus 15 n + 50, an vertex-down parabola with x-intercepts at 5 and 10 — `https://undergroundmathematics.org/quadratics/r6246/images/q82sketch1.png`] (image not included in the text import; path of record).

We can therefore see that \(n^2-15n+50<0\) when \(5<n<10\).

Since \(n\) is a positive integer, we deduce that the equation \(\eqref{eq:1}\) has no real roots when \(n=6\), \(7\), \(8\) or \(9\).

1. Prove that if \(p < r\) and \(4q(p-r) > s^2\), then \(\eqref{eq:starrepeat}\) has no real roots for any value of \(n\).

In order for \(\eqref{eq:starrepeat}\) to have no real roots for a particular value of \(n\), its discriminant must be negative for that value of \(n\).

In order for \(\eqref{eq:starrepeat}\) to have no real roots for *any* value of \(n\), its discriminant must therefore be negative for all values of \(n\).

The discriminant of

\(\eqref{eq:starrepeat}\)

is

\[4(pn^2+q)-4n(rn+s)=4(p-r)n^2-4sn+4q,\]

so we want to show that

\[4(p-r)n^2-4sn+4q<0\]

for all values of

\(n\)

, or equivalently,

\[\begin{equation} (p-r)n^2-sn+q<0 \label{eq:2} \end{equation}\]

for all \(n\). But this is a quadratic inequality in \(n\), and we want to show that it holds for all values of \(n\). (Actually, we only need to show that it is true for positive integer values of \(n\). If, though, we can show that it is true for all real values of \(n\), this will be stronger than we need and so we will be done.)

First note that \(p<r\) (which we are given) means that the leading coefficient of this quadratic is negative, so we know this quadratic is “vertex-up”:

> [figure: Graph of a vertex-up parabola — `https://undergroundmathematics.org/quadratics/r6246/images/q82negquad.png`] (image not included in the text import; path of record).

*A general quadratic where the coefficient of \(x^2\) is negative*

In order for this quadratic to be negative for all real \(n\), it must have no real roots.

The discriminant of the quadratic in \(\eqref{eq:2}\) is \[s^2-4(p-r)q,\] which is negative, as we are told in the question. So in this case, \(\eqref{eq:starrepeat}\) has no real roots for any value of \(n\).

1. If \(n=1\), \(p-r=1\) and \(q=s^2/8\), show that \(\eqref{eq:starrepeat}\) has real roots if, and only if, \(s\le 4-2\sqrt{2}\) or \(s\ge 4+2\sqrt{2}\).

From part (ii), we know that the discriminant of

\(\eqref{eq:starrepeat}\)

is

\[4(p-r)n^2-4sn+4q,\]

which when we’ve substituted in the values given in the question takes the form

\[4-4s+4\frac{s^2}{8},\]

and we want to find the range of values for which this is greater than or equal to

\(0\)

. So we solve

\[\begin{align*} \frac{s^2}{2}-4s+4&\ge 0 \\ \iff\quad s^2-8s+8&\ge0 \\ \end{align*}\]

We find the roots of this quadratic by completing the square:

\[\begin{align*} &s^2-8s+8=0 \\ \iff\quad &(s-4)^2-16+8=0 \\ \iff\quad &(s-4)^2=8 \\ \iff\quad &s-4=\pm2\sqrt{2}\\ \iff\quad &s=4\pm 2\sqrt{2}. \end{align*}\]

(Alternatively, we could have used the [quadratic formula](https://undergroundmathematics.org/glossary/quadratic-equation-solution) for this.)

Sketching the graph of \(y=s^2-8s+8\), we see that it is non-negative if and only if \[s\ge 4+2\sqrt{2} \text{ or } s\le 4-2\sqrt{2}.\]

> [figure: Graph of y = s squared minus 8 s + 8, an upward facing parabola with x-intercepts at 4 minus 2 root 2 and 4 + 2 root 2 — `https://undergroundmathematics.org/quadratics/r6246/images/q82sketch2.png`] (image not included in the text import; path of record).
