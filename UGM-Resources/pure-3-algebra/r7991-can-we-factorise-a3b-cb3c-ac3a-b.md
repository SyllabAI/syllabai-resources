---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r7991
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r7991
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7991
  old_site_id: "Q204"
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
      evidence: "(a−b) shown to be a factor of a³(b−c)+b³(c−a)+c³(a−b) by the factor theorem in a, then complete factorisation; part (i) uses the integer-index binomial only as technique"
      rationale: "Canonical UGM title: Can we factorise $a^3(b-c)+b^3(c-a)+c^3(a-b)$?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Mathematics 1, QP 180, 1955, Q1"
  task: T-UGM-IMPORT-9
---

# Can we factorise $a^3(b-c)+b^3(c-a)+c^3(a-b)$?

## Question

1. Prove that \[\frac{1}{(2-\sqrt{3})^3}+\frac{1}{(2+\sqrt{3})^3}=52.\]

---

1. Show that \((a-b)\) is a factor of \[a^3(b-c)+b^3(c-a)+c^3(a-b)\] and hence factorise the expression completely.

## Suggestion

Could we write these two fractions as a single fraction?

What happens if we expand \((a+b)^3 + (a-b)^3?\)

## Solution

We first write the left hand side as a single fraction, \[\frac{1}{(2-\sqrt{3})^3}+\frac{1}{(2+\sqrt{3})^3}=\frac{(2+\sqrt{3})^3 +(2-\sqrt{3})^3}{(2-\sqrt{3})^3(2+\sqrt{3})^3},\] What is the denominator? We have \[(2-\sqrt{3})^3(2+\sqrt{3})^3= \bigl((2-\sqrt{3})(2+\sqrt{3})\bigr)^3=(4-3)^3=1^3=1.\]

So our fraction becomes \[(2+\sqrt{3})^3+(2-\sqrt{3})^3.\]

We can use the binomial theorem to write

\[\begin{align*} (a+b)^3 &= a^3 + 3a^2b + 3ab^2 + b^3\\ (a-b)^3 &= a^3 - 3a^2b + 3ab^2 - b^3, \end{align*}\]

so that we have \((a+b)^3+(a-b)^3 = 2a^3 +6ab^2.\) Thus \[(2+\sqrt{3})^3 +(2-\sqrt{3})^3 = 2\times 2^3+6\times 2 \times 3 = 52,\] as required.

Let’s define \(Q(a,b,c)= a^3(b-c)+b^3(c-a)+c^3(a-b).\)

We can show that \((a-b)\) is a factor of this expression using the [Factor Theorem](https://undergroundmathematics.org/glossary/factor-theorem).

This says that \((x-p)\) divides the polynomial \(P(x)\) if and only if \(P(p) = 0\).

So if we regard \(Q\) as a polynomial in \(a\), then \((a-b)\) will divide \(Q(a,b,c)\) if and only if \(Q(b,b,c)=0\).

Now \(Q(b,b,c)=b^3(b-c)+b^3(c-b)+c^3(b-b)=0\), so \((a-b)\) is a factor of \(Q(a,b,c)\).

…and hence factorise the expression completely.

Notice that our expression is such that \(Q(a,b,c)= Q(c,a,b) = Q(b,c,a)\) (we say that \(Q(a,b,c)\) is symmetrical in \(a\), \(b\) and \(c\)).

Because of this symmetry, we know that if \((a-b)\) is a factor of \(Q(a,b,c)\), then \((b-c)\) and \((c-a)\) are also.

So \(Q(a,b,c)=(a-b)(b-c)(c-a)R(a,b,c)\), where \(R\) is a symmetrical polynomial in \(a\), \(b\) and \(c\).

Now \(Q(a,b,c)\) is of degree \(4\), while \((a-b)(b-c)(c-a)\) is of degree \(3\), so \(R(a,b,c)\) must be of degree \(1\) in \(a, b\) and \(c\).

The only symmetrical polynomial of degree \(1\) is of the form \(R(a,b,c)=k(a+b+c)\) where \(k\) is a constant. So we have \(Q(a,b,c)=(a-b)(b-c)(c-a)k(a+b+c).\)

To find the value of \(k\), we compare the coefficients of one of the terms. The coefficient of \(a^3b\) in \(Q(a,b,c)\) is \(1\), so \(a \times b \times (-a) \times ka = a^3b\), and so \(k = -1\).

Thus \(Q(a,b,c) = -(a-b)(b-c)(c-a)(a+b+c)\), and this is our factorisation.
