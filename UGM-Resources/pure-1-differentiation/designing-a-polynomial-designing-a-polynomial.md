---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/power-series/designing-a-polynomial
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- power-series
- type/investigation
- level/developing
resource_identity:
  ugm_id: designing-a-polynomial
  station: power-series
  station_title: Power Series
  resource_type_id: 7
  resource_type_label: Investigation
  level: Developing
  ref: 9355
  old_site_id: C8_RT1_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: power-series
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: power-series
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: design p(x) with p(x)=p'(x) — term-by-term power-rule differentiation with coefficient
        matching (the exponential-series connection is the bigger picture)
      rationale: 'Canonical UGM title: "Designing a polynomial"'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/power-series/designing-a-polynomial/download/teacher-notes.pdf
  kind: printable
---

# Designing a polynomial

## Problem

Can we design a polynomial in \(x\), \(p(x)\), such that \(p(x)=p'(x)\)?

Prompting questions

1. What is the simplest polynomial in \(x\) you can think of and what is its derivative?

---

1. What powers of \(x\) do you want the polynomial to include and what does this mean for the derivative?

You may want to use [Desmos](https://www.desmos.com/calculator) to plot the function \(p(x)\) as you construct it.

## Things you might have tried

To tackle this question we could look at the prompting questions.

The simplest polynomial in \(x\) could be \(p(x)=\text{constant}\). If this were the case then \(p'(x)=0\), so if the constant equals zero then we would have a solution. This solution does seem a silly one, can we find another?

We could choose \(p(x)=c+x\), where \(c\) is a constant. What would \(c\) need to be to make \(p'(x)\) have the same constant term as \(p(x)\) in this case?

Answer

If we could choose \(p(x)=c+x\), where \(c\) is a constant then this would give \(p'(x)=1\). Thus, if we choose \(c\) to be \(1\) we would have \(p(x)\) and \(p'(x)\) agreeing as far as the \(x^0\) (constant) term (but they disagree beyond that).

If we choose to include an \(x^2\) term in our polynomial \(p(x)\), then \(p'(x)\) would include an \(x\) term. From part (a), if we choose \(p(x)=1+x\) then we have \(p(x)\) agreeing with \(p'(x)\) as far as the \(x^0\) term. So if we include \(\dfrac{x^2}{2}\) in \(p(x)\), we would then get \[p(x)=1+x+\frac{x^2}{2}\] and \[p'(x)=1+x,\] so that \(p(x)\) and \(p'(x)\) agree as far as the \(x^1\) term (but not beyond).

How could we continue this?

What do the polynomials you find look like when plotted, \(y=p(x)\)?

You may want to use [Desmos](https://www.desmos.com/calculator) to plot the function \(p(x)\) as you construct it.
