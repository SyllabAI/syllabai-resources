---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-compound-angles/r8525
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-compound-angles
- type/review-question
resource_identity:
  ugm_id: r8525
  station: trigonometry-compound-angles
  station_title: 'Trigonometry: Compound Angles'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8525
  old_site_id: Q96
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-compound-angles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-compound-angles
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics Scholarship paper, QP 183, 1954, Q3
task: T-UGM-IMPORT-5
---

# Can we prove $\sin a \sin b \leq \sin^2\frac{1}{2}(a+b)$?

## Question

Prove that, for all values of \(a\) and \(b\), \[\sin a \sin b \le \sin^2\frac{1}{2}(a+b).\]

Show further that, if \(a\), \(b\), \(c\) and \(d\) all lie between \(0\) and \(\pi\), then \[\sin a \sin b \sin c \sin d \leq \left( \sin\frac{1}{4}(a+b+c+d)\right)^4;\] and, by writing \(d=\frac{1}{3}(a+b+c)\), deduce that \[\sin a \sin b \sin c \le \left( \sin\frac{1}{3}(a+b+c)\right)^3.\]

Show precisely where the restrictions on \(a\), \(b\), \(c\) and \(d\) are used in the proof of the last two inequalities.

## Suggestion

Can we find an identity for \(\sin a \sin b\)?

If \(0 \leq a \leq \pi\), what does that tell us about \(\sin a\)?

Handy fact: if \(0 \leq a \leq b\), and \(0 \leq c \leq d\), then \(0 \leq ac \leq bd\).

… and, by writing \(d=\frac{1}{3}(a+b+c)\), deduce that \[\sin a \sin b \sin c \le \left( \sin\frac{1}{3}(a+b+c)\right)^3.\]

Let’s think about the case \(0 < a, b, c, d < \pi\) separately to the cases where \(a = b = c = 0\) and \(a = b = c = \pi.\)

For the first case, what do you know about \(\sin \frac{1}{3}(a+b+c)\)?

## Solution

We know that \[\cos (x+y) = \cos x\cos y-\sin x\sin y \quad \text{and} \quad \cos (x-y) = \cos x\cos y+\sin x\sin y.\]

Thus \[\sin x\sin y = \dfrac{1}{2}(\cos (x-y)-\cos (x+y)).\]

This means \[\sin \left(\dfrac{a+b}{2}\right)\sin \left(\dfrac{a+b}{2}\right) = \dfrac{1}{2}(1-\cos (a+b)).\]

We also have \[\sin a\sin b = \dfrac{1}{2}(\cos (a-b)-\cos (a+b)).\]

Since \(\cos(a-b) \leq 1\), on comparing the last two equations we see \(\sin a\sin b \leq \sin^2 \left(\dfrac{a+b}{2}\right)\).

If \(0 \leq a, b, c, d \leq \pi,\) then

\[0 \leq \sin a, \sin b, \sin c, \sin d \leq 1.\]

Therefore

\[0 \leq \sin a \sin b \leq \sin^2{\frac{1}{2}(a+b)}\]

and

\[0 \leq \sin c \sin d \leq \sin^2{\frac{1}{2}(a+b)}.\]

Because the left hand side of each inequality is greater than or equal to zero, we can multiply the inequalities to get

\[\begin{equation} \sin a \sin b \sin c \sin d \leq \sin^2{\frac{1}{2}(a+b)} \sin^2{\frac{1}{2}(c+d)}. \label{eq:1} \end{equation}\]

Using the inequality from a), we also have

\[\begin{align} \sin{\frac{1}{2}(a+b)} \sin{\frac{1}{2}(c+d)} &\leq \sin^2{\frac{1}{2}\bigl[\frac{1}{2}(a+b)+\frac{1}{2}(c+d)\bigr]} \notag \\ \quad &= \sin^2{\frac{1}{4}(a + b + c +d)}. \label{eq:2} \end{align}\]

We know

\[0 \leq \frac{1}{2}(a+ b), \frac{1}{2}(c+d) \leq \pi,\]

and so

\[0 \leq \sin \frac{1}{2}(a+b) \sin \frac{1}{2}(c+d),\]

which means we can square \(\eqref{eq:2}\) to get

\[\begin{equation} \sin^2{\frac{1}{2}(a+b)} \sin^2 \frac{1}{2}(c+d) \leq \sin^4{\frac{1}{4}(a+b+c+d)}. \label{eq:3} \end{equation}\]

Combining \(\eqref{eq:1}\) and \(\eqref{eq:3}\) we get

\[\begin{align*} \sin a \sin b \sin c \sin d &\leq \sin^4\frac{1}{4}(a+b+c+d) \\ & \quad = \bigl(\sin \frac{1}{4}(a+b+c+d)\bigr)^4, \end{align*}\]

as required.

… and, by writing \(d=\frac{1}{3}(a+b+c)\), deduce that \[\sin a \sin b \sin c \le \left( \sin\frac{1}{3}(a+b+c)\right)^3.\]

Setting \(d = \frac{1}{3}(a+b+c),\) we see that

\[a + b + c + d = \frac{4}{3}(a+b+c),\]

and we can deduce that

\[\begin{equation} \sin a \sin b \sin c \sin \frac{1}{3}(a+b+c) \leq \bigl(\sin \frac{1}{3}(a+b+c)\bigr)^4. \label{eq:4} \end{equation}\]

From \(0 \leq a, b, c \leq \pi\), we deduce that \(0 \leq \frac{1}{3}(a+b+c) \leq \pi\) and, except in the cases \(a,b,c=0\) and \(a,b,c=\pi\), we have the strict inequality \(0 < \frac{1}{3}(a+b+c) < \pi\), and so

\[\sin \frac{1}{3}(a+b+c) > 0.\]

Given this, we can divide \(\eqref{eq:4}\) by \(\sin \frac{1}{3}(a+b+c)\) to get

\[\sin a \sin b \sin c \leq \bigl(\sin \frac{1}{3}(a+b+c)\bigr)^3,\]

as required.

The final task is to consider the cases \(a = b = c = 0\) and \(a = b = c = \pi.\) In both of these cases, both sides of the inequality are \(0\) (as \(\sin 0 = \sin \pi = 0\)), and so the inequality still holds.
