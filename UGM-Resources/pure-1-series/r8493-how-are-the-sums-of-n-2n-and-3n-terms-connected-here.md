---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/r8493
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/review-question
resource_identity:
  ugm_id: r8493
  station: sequences
  station_title: Sequences
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8493
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: sequences
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: sequences
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: S_3=3(S_2-S_1) for an AP; sum of 1+3x/(1+2x^2)+... and the |r|<1 condition for a sum
        to infinity
      rationale: 'Canonical UGM title: "How are the sums of $n$, $2n$ and $3n$ terms connected here?";
        exam provenance: UCLES O level Mathematics C, 1953, Q9'
      validation_status: SUGGESTED
    title: use the formulae for the n th term and for the Including knowledge that numbers sum of the
      first n terms to solve problems involving arithmetic or geometric progressions equivalent).
  - code: 1.6.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: S_3=3(S_2-S_1) for an AP; sum of 1+3x/(1+2x^2)+... and the |r|<1 condition for a sum
        to infinity
      rationale: 'Canonical UGM title: "How are the sums of $n$, $2n$ and $3n$ terms connected here?";
        exam provenance: UCLES O level Mathematics C, 1953, Q9'
      validation_status: SUGGESTED
    title: 'Questions may involve more than one progression. geometric progression, and the formula
      for the sum to infinity of a convergent geometric progression.: • use the condition for the convergence
      of a'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Mathematics C, 1953, Q9
task: T-UGM-IMPORT-6
---

# How are the sums of $n$, $2n$ and $3n$ terms connected here?

## Question

1. If \(S_1\), \(S_2\) and \(S_3\) are the sums of \(n\), \(2n\) and \(3n\) terms of an arithmetic progression, show that \(S_3=3(S_2-S_1)\).

---

1. Find the sum of \(n\) terms of the series \[1+\frac{3x}{(1+2x^2)}+\frac{9x^2}{(1+2x^2)^2}+\frac{27x^3}{(1+2x^2)^3}+....\] For what values of \(x\) does this series have a sum to infinity?

## Suggestion

Is there a formula for the sum of the first \(n\) terms of an arithmetic progression that we could use?

What kind of series is this? When does this kind of series have a sum to infinity?

## Solution

Let our arithmetic progression be \(u_1, u_2, u_3, ...\), or alternatively \(a, a+d, a + 2d, ...\).

If we now take the sum over the first \(n\) values, we find \[\sum_{m=1}^{n} u_m = \dfrac{n}{2}(2a+(n-1)d).\]

This is the formula we need. So for our sequence,

\[\begin{align*} S_1&=\dfrac {n}{2}(2a + (n-1)d),\\ S_2&=n(2a + (2n-1)d),\\ S_3&=\dfrac{3n}{2}(2a + (3n-1)d). \end{align*}\]

Thus \(3(S_2-S_1) = 3n\left[2a+2nd-d-\left(a+\dfrac{nd}{2}-\dfrac{d}{2}\right)\right] = 3n\left[a+\dfrac{3nd}{2}-\dfrac{d}{2}\right] = \dfrac{3n}{2}(2a+(3n-1)d)= S_3\).

This is a geometric series, with first term \(a = 1\), and with common ratio \(r = \dfrac{3x}{1+2x^2}\).

The formula for the sum of the first \(n\) terms of a geometric progression is

\[S_n = \dfrac{a(r^n-1)}{r-1} = \dfrac{a(1-r^n)}{1-r}.\]

So here we have \[S_n=\frac{\left(\dfrac{3x}{1+2x^2}\right)^n-1}{\dfrac{3x}{1+2x^2}-1}=\frac{\dfrac{(3x)^n-(1+2x^2)^n}{(1+2x^2)^n}}{\dfrac{3x-(1+2x^2)}{1+2x^2}}= \frac{(3x)^n -(1+2x^2)^n}{(1+2x^2)^{n-1}(1-2x)(x-1)}.\]

A geometric series diverges if and only if \(\big \vert r \big \vert \geq 1.\) So when is \(\big|\dfrac{3x}{1+2x^2}\big| \ge 1\) true?

Note that \(1 + 2x^2 > 0\) for all real values of \(x\), so we need to solve \(\big|3x\big| \geq 1+2x^2\).

Let’s look at the case \(x>0\); this gives us \(2x^2-3x+1\geq 0\) to solve, which is true if and only if \((2x-1)(x-1) \geq 0\), or \(\frac{1}{2}\le x \le 1\).

Now looking at the case \(x<0\); we need to solve \(2x^2+3x+1\geq 0\), which is true if and only if \((2x+1)(x+1) \geq 0\), or \(-1 \leq x \leq -\frac{1}{2}\).

Hence we find the series to diverge for \(\frac{1}{2}\le \big \vert x \big \vert \le 1\), and it will converge for all other values of \(x\).
