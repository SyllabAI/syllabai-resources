---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r9928
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r9928
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9928
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
  spec_points:
  - code: 1.6.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: x^3-1/x^3 and x^5-1/x^5 in terms of u=x-1/x by expanding (x-1/x)^3 and (x-1/x)^5 with
        the binomial theorem
      rationale: 'Canonical UGM title: "If $x - 1/x = u$, what''s $x^3 - 1/x^3$?"; exam provenance:
        UCLES A level Mathematics A 1, 1978, Q3(a)'
      validation_status: SUGGESTED
    title: use the expansion of ( a + b ) , where n is a positive integer
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES A level Mathematics A 1, 1978, Q3(a)
task: T-UGM-IMPORT-6
---

# If $x - 1/x = u$, what's $x^3 - 1/x^3$?

## Question

If \(x - \dfrac{1}{x} = u\), express \(x^3 - \dfrac{1}{x^3}\) and \(x^5 - \dfrac{1}{x^5}\) in terms of \(u\).

## Suggestion

What happens if we square \(u\)?

## Solution

We can begin by applying the

binomial theorem

to see that

\[\begin{align*} \left( x - \frac{1}{x} \right)^3 &= x^3 - 3x + \frac{3}{x} - \frac{1}{x^3} \\ &= x^3 - \frac{1}{x^3} - 3\left( x - \frac{1}{x} \right) \end{align*}\]

which implies that

\[\begin{equation*} x^3 - \frac{1}{x^3} = \left( x - \frac{1}{x} \right)^3 + 3 \left( x - \frac{1}{x} \right) = u^3 + 3u. \end{equation*}\]

We can do a similar thing again:

\[\begin{align*} \left( x - \frac{1}{x} \right)^5 &= x^5 - 5x^3 + 10x - \frac{10}{x} + \frac{5}{x^3} - \frac{1}{x^5} \\ &= x^5 - \frac{1}{x^5} - 5\left( x^3 - \frac{1}{x^3} \right) + 10 \left( x - \frac{1}{x} \right) \end{align*}\]

This implies that

\[\begin{align*} x^5 - \frac{1}{x^5} &= \left( x - \frac{1}{x} \right)^5 + 5 \left( x^3 - \frac{1}{x^3} \right) - 10 \left( x - \frac{1}{x} \right) \\ &= u^5 + 5(u^3 + 3u) - 10u \\ &= u^5 + 5u^3 + 5u. \end{align*}\]

If we extend this idea, we can write \(x^7-\dfrac{1}{x^7}\), \(x^9-\dfrac{1}{x^9}\) and so on as polynomials in \(u\). Are there any patterns that you can find to the polynomials which result?
