---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r9207
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r9207
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9207
  old_site_id: Q212
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
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: coefficients of x^-12 and x^2 in (x^4-1/x^2)^5 (x-1/x)^6 by expanding both brackets
        — binomial expansion with negative powers of the variable
      rationale: 'Canonical UGM title: "Can we find the coefficients of $x^{−12}$ and $x^2$ in this
        expansion?"; exam provenance: UCLES STEP Mathematics I, 2000, Q2'
      validation_status: SUGGESTED
    title: use the expansion of ( a + b ) , where n is a positive integer
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES STEP Mathematics I, 2000, Q2
task: T-UGM-IMPORT-6
---

# Can we find the coefficients of $x^{−12}$ and $x^2$ in this expansion?

## Question

Show that the coefficient of \(x^{−12}\) in the expansion of \[\left(x^4-\frac{1}{x^2}\right)^5\left(x-\frac{1}{x}\right)^6\] is \(−15\), and calculate the coefficient of \(x^2\).

Hence, or otherwise, calculate the coefficients of \(x^4\) and \(x^{38}\) in the expansion of \[(x^2 − 1)^{11}(x^4 + x^2 + 1)^5.\]

## Suggestion

Could we expand each of the brackets?

What contribution do we need from each of the bracketed terms to get \(x^{-12}\) or \(x^2\) terms?

How are the two parts related? Could we rewrite this new expression to make it look like the first part?

What happens if we mulitply \((x^4+x^2+1)\) by \((x^2-1)\)?

## Solution

Show that the coefficient of \(x^{−12}\) in the expansion of \[\left(x^4-\frac{1}{x^2}\right)^5\left(x-\frac{1}{x}\right)^6\] is \(−15\), and calculate the coefficient of \(x^2\).

Using the binomial expansion on each bracket, we have

\[\begin{align} \left(x^4-\frac{1}{x^2}\right)^5 &\left(x-\frac{1}{x}\right)^6\notag \\ =\left(x^{20}-5x^{14}+10x^8-10x^2+5x^{-4}-x^{-10}\right) &\left(x^{6}-6x^{4}+15x^2-20+15x^{-2}-6x^{-4}+x^{-6}\right).\label{eq:expansion} \end{align}\]

The only way we can get an \(x^{-12}\) term on multiplying out is from the \(x^{-10}\) term in the first bracket multiplied by the \(x^{-2}\) term in the second bracket.

Thus the coefficient of \(x^{-12}\) in the full expansion is \((-1)\times15 = -15\).

There are three ways we can get an \(x^{2}\) term on multiplying out: \(x^{8} \times x^{-6}\), \(x^{2} \times x^{0}\) and \(x^{-4} \times x^{6}\).

Thus the coefficient of \(x^{2}\) in the full expansion is \(10 + 200 + 5 = 215\).

Hence, or otherwise, calculate the coefficients of \(x^4\) and \(x^{38}\) in the expansion of \[(x^2 − 1)^{11}(x^4 + x^2 + 1)^5.\]

We can note first that

\[\begin{align*} \left(x^4-\frac{1}{x^2}\right)^5\left(x-\frac{1}{x}\right)^6 &= \left(\frac{x^6-1}{x^2}\right)^5\left(\frac{x^2-1}{x}\right)^6\\ &= \dfrac{(x^6-1)^5(x^2-1)^6}{x^{16}}. \end{align*}\]

Secondly, we can note that \[(x^4+x^2+1)(x^2-1) = x^6 - 1.\]

Thus

\[\begin{align*} (x^2-1)^{11}(x^4+x^2+1)^5 &= (x^2-1)^{6}(x^2-1)^{5}(x^4+x^2+1)^5\\ &=(x^2-1)^{6}(x^6-1)^{5}\\ &=\dfrac{x^{16}(x^2-1)^{6}(x^6-1)^{5}}{x^{16}}\\ &= x^{16}\left(x^4-\frac{1}{x^2}\right)^5\left(x-\frac{1}{x}\right)^6. \end{align*}\]

So to find the coefficient of \(x^4\) in \((x^2-1)^{11}(x^4+x^2+1)^5\) is to find the coefficient of \(x^{-12}\) in the expansion \(\eqref{eq:expansion}\) of \(\left(x^4-\dfrac{1}{x^2}\right)^5\left(x-\dfrac{1}{x}\right)^6\).

We already know this to be \(-15\).

And to find the coefficient of \(x^{38}\) in \((x^2-1)^{11}(x^4+x^2+1)^5\) is to find the coefficient of \(x^{22}\) in the expansion \(\eqref{eq:expansion}\). This comes from \(x^{20}\) in the first bracket and \(x^2\) in the second, giving a coefficient of \(15\).
