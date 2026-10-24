---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r6488
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r6488
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6488
  old_site_id: "Q3006"
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
      evidence: "common factor x−2 evaluated at x=2 in both expressions (factor theorem → simultaneous equations); same remainder under x+a and x−2a from f(−a)=f(2a)"
      rationale: "Canonical UGM title: If dividing by $x+a$ or $x-2a$ gives the same remainder, what's $a$?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES AO level Additional Mathematics 1, QP 8175/1, 1983, Q12"
  task: T-UGM-IMPORT-9
---

# If dividing by $x+a$ or $x-2a$ gives the same remainder, what's $a$?

## Question

1. The expressions \(px^4 - 5x + q\) and \(x^4 - 2x^3 - px^2 - qx - 8\) have a common factor \(x - 2\). Find the value of \(p\) and of \(q\).

---

1. The expression \(x^3 - x^2 - 2x - 3\) has the same remainder when divided by \(x + a\) and by \(x - 2a\). Find the non-zero values of \(a\) and the corresponding values of the remainder.

## Solution

1. The expressions \(px^4 - 5x + q\) and \(x^4 - 2x^3 - px^2 - qx - 8\) have a common factor \(x-2\). Find the value of \(p\) and of \(q\).

As \(x-2\) is a factor of both of these polynomials, by the [factor theorem](https://undergroundmathematics.org/glossary/factor-theorem), both expressions are zero when evaluated at \(x = 2\) .

We thus have the simultaneous equations

\[\begin{align*} p \times 2^4 - 5 \times 2 + q &= 0, \\ 2^4 - 2 \times 2^3 - p \times 2^2 - q \times 2 - 8 &= 0. \end{align*}\]

That is,

\[\begin{align*} 16p + q &= 10, \\ -4p - 2q &= 8. \end{align*}\]

The second equation becomes \(q = -4-2p\) when dividing through by \(2\). By substituting this into the first equation, we have that \[16p + (-4-2p) = 10.\] That is, \(14p = 14\) or \(p = 1\). Consequently, \(q = -4-2 = -6\).

1. The expression \(x^3 - x^2 - 2x - 3\) has the same remainder when divided by \(x+a\) and by \(x-2a\). Find the non-zero values of \(a\) and the corresponding values of the remainder.

The

remainder theorem

tells us that the expression evaluated at

\(x=-a\)

is equal to the expression evaluated at

\(x=2a\)

. This gives us

\[\begin{equation} -a^3 - a^2 + 2a - 3 = 8a^3 - 4a^2 - 4a - 3. \label{eq:1} \end{equation}\]

That is, \(a\) is such that \[9a^3 - 3a^2 - 6a = 0\] or \[3a(3a^2 - a - 2) = 0.\] Factorising, we see that \[3a^2 - a - 2 = (3a + 2)(a - 1)\] and so the non-zero values of \(a\) that satisfy \(\eqref{eq:1}\) are \(a = 1\) and \(a = -\dfrac{2}{3}\).

By substituting into either side of \(\eqref{eq:1}\), the remainder in the case when \(a=1\) is given by \[-1^3 - 1^2 + 2 \times 1 - 3 = -3,\] and the remainder in the case when \(a=-\dfrac{2}{3}\) is given by \[-\left(-\frac{2}{3}\right)^3 - \left(-\frac{2}{3}\right)^2 + 2 \times \left( -\frac{2}{3} \right) - 3 = \frac{8 - 12 - 36 - 81}{27} = -\frac{121}{27}.\]

How could we check our answers?
