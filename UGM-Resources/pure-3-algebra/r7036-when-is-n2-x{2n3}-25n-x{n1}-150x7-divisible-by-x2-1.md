---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r7036
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r7036
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7036
  old_site_id: "Q1054"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: polynomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: polynomials
    validation_status: SUGGESTED
  spec_points:
  - code: 3.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "x²−1 is a factor iff the polynomial vanishes at x=±1 (factor theorem applied twice), with the parity case-split settling n=10/15"
      rationale: "Canonical UGM title: When is $n^2 x^{2n+3} - 25n x^{n+1} + 150x^7$ divisible by $x^2-1$?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, 2009, Q1I"
  task: T-UGM-IMPORT-9
---

# When is $n^2 x^{2n+3} - 25n x^{n+1} + 150x^7$ divisible by $x^2-1$?

## Question

The polynomial

\[n^2 x^{2n+3} - 25n x^{n+1} + 150x^7\]

has \(x^2 - 1\) as a factor

1. for no values of \(n\),

---

1. for \(n=10\) only,

---

1. for \(n=15\) only,

---

1. for \(n=10\) and \(n=15\) only.

## Suggestion

Given that \(x^2-1\) is a factor, what linear factors of the polynomial do we know?

Can we now use the factor theorem on the polynomial twice?

We may need to be more careful with one factor than the other…

## Solution

We can factorise \(x^2 -1\) as

\[x^2 -1 = (x+1)(x-1),\]

so for the polynomial

\[n^2 x^{2n+3} - 25n x^{n+1} + 150x^7\]

to have \(x^2-1\) as a factor, the value of the polynomial when \(x=\pm1\) must be \(0\) (from the [factor theorem](https://undergroundmathematics.org/glossary/factor-theorem)).

When \(x=+1\), we need

\[n^2 - 25n + 150=0,\]

which can be factorised as

\[(n-10)(n-15)=0,\]

so \(n=10\) or \(n=15\).

When \(x=-1\), we need

\[0 = \begin{cases} -n^2 + 25n - 150 & n \textrm{ even} \\ -n^2 - 25n - 150 & n \textrm{ odd}, \\ \end{cases}\]

which can be factorised as

\[0 = \begin{cases} -(n-10)(n-15) & n \textrm{ even} \\ -(n+10)(n+15) & n \textrm{ odd}, \\ \end{cases}\]

which gives

\[\begin{cases} n=10 & n \textrm{ even } [n \neq 15 \text{ because } n \text{ must be even]} \\ n=-15 & n \textrm{ odd } [n \neq -10 \text{ because } n \text{ must be odd]}. \\ \end{cases}\]

So for both \(x=+1\) and \(x=-1\) to be solutions of the polynomial, we must have \(n=10\).

So the answer is (b).

Alternatively we could say, when \(x = -1\) we have \(n^2+25n(-1)^{n+1} +150 =0\).

Subtracting this from \(n^2 - 25n + 150=0,\) we get \(25n((-1)^{n+1}+1)=0\), and so \(n\) must be even.

So \(n\) must be \(10\) or \(15\), and also even, so the only possibility is \(n = 10\). The answer is (b).
