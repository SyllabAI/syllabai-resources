---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/power-series/r7436
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- power-series
- type/review-question
resource_identity:
  ugm_id: r7436
  station: power-series
  station_title: Power Series
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7436
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: power-series
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: power-series
    validation_status: SUGGESTED
  spec_points:
  - code: 3.1.6
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "(1+x)^{3/2}+(1−2x)^{3/4} expanded to x³ by the real-index binomial series with the |x|<1 validity condition stated"
      rationale: "Canonical UGM title: Can we expand $(1+x)^{3/2} + (1-2x)^{3/4}$ as far as the term in $x^3$?"
      validation_status: SUGGESTED
    title: "use the expansion of (1 + x)ⁿ, where n is a rational number and | x | < 1"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES O level Additional Mathematics 2, QP 420/2, 1967, Q5(i)"
  task: T-UGM-IMPORT-9
---

# Can we expand $(1+x)^{3/2} + (1-2x)^{3/4}$ as far as the term in $x^3$?

## Question

Use the binomial theorem to expand

\[\begin{equation*} (1+x)^\frac{3}{2} + (1-2x)^\frac{3}{4} \end{equation*}\]

as far as the term in \(x^3\).

## Solution

The

binomial theorem

says that, if

\(|x| < 1\)

, then

\[\begin{equation*} (1+x)^r = 1 + rx + \frac{r(r-1)}{2!} x^2 + \frac{r(r-1)(r-2)}{3!} x^3 + \dotsb \end{equation*}\]

and so to expand

\[\begin{equation*} (1+x)^\frac{3}{2} + (1-2x)^\frac{3}{4} \end{equation*}\]

as far as the term in \(x^3\), we can

1. separately expand \((1+x)^\frac{3}{2}\) and \((1-2x)^\frac{3}{4}\) up to \(x^3\) and

---

1. collect the terms.

Thus

\[\begin{align*} (1+x)^\frac{3}{2} &= 1 + \frac{3}{2}x + \frac{\frac{3}{2} \times \frac{1}{2}}{2!} x^2 + \frac{\frac{3}{2} \times \frac{1}{2} \times \left(- \frac{1}{2} \right)}{3!} x^3 + \ldots\\ &= 1 + \frac{3}{2} x + \frac{3}{8} x^2 - \frac{3}{48} x^3 + \ldots, \end{align*}\]

and

\[\begin{align*} (1-2x)^\frac{3}{4} &= 1 + \frac{3}{4} (-2x) + \frac{\frac{3}{4} \times \left( -\frac{1}{4} \right)}{2!} (-2x)^2 + \frac{\frac{3}{4} \times \left( -\frac{1}{4} \right) \times \left( -\frac{5}{4} \right)}{3!} (-2x)^3 + \ldots\\ &= 1 - \frac{3}{2} x - \frac{3}{8} x^2 - \frac{15}{48} x^3 + \ldots, \end{align*}\]

and therefore

\[\begin{align*} (1+x)^\frac{3}{2} + (1-2x)^\frac{3}{4} &= \left( 1 + \frac{3}{2} x + \frac{3}{8} x^2 - \frac{3}{48} x^3 \right) + \left( 1 - \frac{3}{2} x - \frac{3}{8} x^2 - \frac{15}{48} x^3 \right)+ \ldots \\ &= 2 - \frac{18}{48} x^3 + \ldots \\ &= 2 - \frac{3}{8} x^3 + \ldots \end{align*}\]
