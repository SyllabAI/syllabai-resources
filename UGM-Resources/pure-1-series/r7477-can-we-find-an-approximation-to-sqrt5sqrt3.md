---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r7477
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r7477
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7477
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: counting-and-binomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: counting-and-binomials
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics B 1, 1973, Q5
task: T-UGM-IMPORT-6
---

# Can we find an approximation to $\sqrt{5}+\sqrt{3}$?

## Question

If

\(\dfrac{b}{a}\)

is small enough for powers of

\(\dfrac{b}{a}\)

higher than the third to be neglected, show that

\[\begin{equation*} (a+b)^\frac{1}{2} - (a-b)^\frac{1}{2} = a^\frac{1}{2} \left( \frac{b}{a} + \frac{b^3}{8a^3} \right). \end{equation*}\]

Use this result to deduce a rational approximation to \(\sqrt 5 - \sqrt 3\).

Deduce, or obtain otherwise, a rational approximation to \(\sqrt 5 + \sqrt 3\).

## Solution

If \(a > 0\), we can write \[(a+b)^\frac{1}{2} = \sqrt{a} \left( 1 + \frac{b}{a} \right)^{1/2}.\]

The

binomial theorem

says that, if

\(\big |x \big| < 1\)

,

\[\begin{equation*} (1+x)^\alpha = 1 + \alpha x + \frac{\alpha(\alpha-1)}{2!} x^2 + \frac{\alpha(\alpha-1)(\alpha-2)}{3!} x^3 + \dotsb \end{equation*}\]

and so, if

\(\dfrac{b}{a}\)

is small enough,

\[\begin{align*} (a+b)^\frac{1}{2} &= \sqrt{a} \left( 1 + \frac{b}{a} \right)^{1/2} \\ &= \sqrt{a} \left( 1 + \frac{1}{2} \frac{b}{a} + \frac{\frac{1}{2} \times \left(-\frac{1}{2} \right)}{2!} \left( \frac{b}{a} \right)^2 + \frac{\frac{1}{2} \times \left( -\frac{1}{2} \right) \times \left( -\frac{3}{2} \right)}{3!} \left( \frac{b}{a} \right)^3 + \dotsb \right) \\ &\approx \sqrt{a} \left( 1 + \frac{b}{2a} - \frac{b^2}{8a^2} + \frac{b^3}{16a^3} \right). \end{align*}\]

Similarly, assuming that

\(a > 0\)

and

\(\dfrac{b}{a}\)

is small enough we will get the same result as above replacing

\(b\)

with

\(-b\)

,

\[\begin{align*} (a-b)^\frac{1}{2} &\approx \sqrt{a} \left( 1 + \frac{-b}{2a} - \frac{(-b)^2}{8a^2} + \frac{(-b)^3}{16a^3} \right)\\ &= \sqrt{a} \left( 1 - \frac{b}{2a} - \frac{b^2}{8a^2} - \frac{b^3}{16a^3} \right). \end{align*}\]

As a result,

\[\begin{align*} (a+b)^\frac{1}{2} - (a-b)^\frac{1}{2} &\approx \sqrt{a} \left( \left( 1 + \frac{b}{2a} - \frac{b^2}{8a^2} + \frac{b^3}{16a^3} \right) - \left( 1 - \frac{b}{2a} - \frac{b^2}{8a^2} - \frac{b^3}{16a^3} \right) \right) \\ &= \sqrt{a} \left( \frac{b}{a} + \frac{b^3}{8a^3} \right). \end{align*}\]

Let’s put \(a + b = 5\) and \(a - b = 3\). Now adding gives \(2a = 8 \implies a = 4, b = 1\). Thus \(a > 0\) and \(\dfrac{b}{a}\) is suitably small.

From our work above,

\[\begin{align*} \sqrt 5 - \sqrt 3 = (a+b)^\frac{1}{2} - (a-b)^\frac{1}{2} &\approx \sqrt{a} \left( \frac{b}{a} + \frac{b^3}{8a^3} \right) \\ &= \sqrt{4} \left( \frac{1}{4} + \frac{1}{8 \times 64} \right) \\ &= \frac{1}{2} + \frac{1}{256} \\ &= \frac{129}{256}\\ & \approx 0.5039... \end{align*}\]

The approximation is an accurate one: \(\sqrt 5 - \sqrt 3= 0.5040...\)

We have

\((\sqrt 5 + \sqrt 3)(\sqrt 5 - \sqrt 3) = 2.\)

Thus

\(\sqrt 5 + \sqrt 3 \approx 2 \times \dfrac{256}{129} = \dfrac{512}{129} = 3.9690...\)

Again, the approximation is a good one: \(\sqrt 5 + \sqrt 3 = 3.9681...\)
