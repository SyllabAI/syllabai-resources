---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r6546
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r6546
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6546
  old_site_id: "Q105"
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
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "show a+b+c is a factor of a³+b³+c³−3abc and find the other factor — the factor theorem with the c=−a−b substitution inside the AM-GM deduction"
      rationale: "Canonical UGM title: Can we prove the Arithmetic and Geometric Mean Inequality?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Pure Mathematics 1, QP 9210/1, 1980, Q3"
  task: T-UGM-IMPORT-9
---

# Can we prove the Arithmetic and Geometric Mean Inequality?

## Question

1. Prove that, if \(a\) and \(b\) are real, \[\frac{1}{2}(a^2+b^2)\geq ab.\]

---

1. Deduce that, if \(a\),\(b\) and \(c\) are real, \[a^2+b^2+c^2\geq ab+bc+ca.\]

---

1. Show that \(a+b+c\) is a factor of \(a^3+b^3+c^3-3abc\) and find the other factor of this expression.

---

1. Deduce that, if \(p\), \(q\) and \(r\) are positive, \[\frac{1}{3}(p+q+r)\geq (pqr)^{\frac{1}{3}}.\]

## Suggestion

What happens if we bring everything to the left-hand side and try to factorise?

Can we use the first part of the question here?

Could we use earlier parts to help? Would putting \(p = a^3, q = b^3, r = c^3\) be more convenient?

## Solution

The inequality holds if and only if \(a^2+b^2\geq 2ab\), which is true if and only if \(a^2- 2ab +b^2\geq 0.\)

This is true, since \(a^2-2ab+b^2=(a-b)^2,\) and any square is either zero or positive. Hence \[\frac{1}{2}(a^2+b^2)\geq ab.\]

This is called the *arithmetic mean-geometric mean inequality*, or the *AM-GM inequality*, for two variables.

The quantity \(\frac{1}{2}(x + y)\) is the *arithmetic mean* of \(x\) and \(y\), and (if \(x\) and \(y\) are positive) \(\sqrt{xy}\) is the *geometric mean* of \(x\) and \(y\).

So we have established that the arithmetic mean is always greater than or equal to the geometric mean.

This inequality is extremely useful for solving many mathematics problems.

We can use the result in (i) three times for

\(a\)

and

\(b\)

,

\(b\)

and

\(c\)

and

\(c\)

and

\(a\)

, namely

\[\begin{align*} \frac{1}{2}(a^2+b^2) &\geq ab, \\ \frac{1}{2}(b^2+c^2) &\geq bc, \\ \frac{1}{2}(c^2+a^2) &\geq ca. \end{align*}\]

By adding them up we get \[\frac{1}{2}(a^2+b^2)+\frac{1}{2}(b^2+c^2)+\frac{1}{2}(c^2+a^2)\geq ab+bc+ca,\] which implies \[a^2+b^2+c^2\geq ab+bc+ca.\]

We can use the Factor Theorem here.

The Factor Theorem says that the polynomial \(f(x)\) has a factor \(x-p\) if and only if \(f(p)=0\).

Let’s put \(f(a) = a^3+b^3+c^3-3abc\), so \(f(a)\) is a degree \(3\) polynomial in \(a\). Thus \(a+b+c\) will be a factor of \(f(a)\) if and only if \(f(-b-c) = 0\).

Now \[f(-b-c) = (-b-c)^3+b^3+c^3 -3(-b-c)bc\] \[= -b^3-3b^2c-3bc^2-c^3+b^3+c^3+3b^c+3c^2b =0.\]

So \(a+b+c\) does divide \(a^3+b^3+c^3-3abc\).

We need the other factor, which must include \(a^2 + b^2 + c^2\), because we need to create \(a^3 + b^3 + c^3\).

Let’s say that \((a+b+c)(a^2+b^2+c^2+g)=a^3+b^3+c^3-3abc\), where \(g\) is a polynomial in \(a, b\) and \(c\).

So \[a^3+b^3+c^3+ab^2+ac^2+ba^2+ca^2+cb^2 +(a+b+c)g = a^3+b^3+c^3-3abc\],

which is true if and only if

\[ab^2+ac^2+ba^2+ca^2+cb^2 +3abc +(a+b+c)g =0,\] or \[(ab+bc+ca)(a+b+c) + (a+b+c)g=0.\]

So \(g = -(ab+bc+ca)\), and \[a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2+-ab-bc-ca).\]

Let \(a=p^{\frac{1}{3}}\), \(b=q^{\frac{1}{3}}\) and \(c=r^{\frac{1}{3}}\).

Then in terms of \(a\), \(b\) and \(c\), we have to prove that \[a^3+b^3+c^3\geq 3abc.\]

By (iii) we know that \[a^3+b^3+c^3-3abc=(a+b+c)(a^2+b^2+c^2-ab-bc-ca)\] and this is greater or equal to \(0\) since, by (ii), \(a^2+b^2+c^2- ab-bc-ca\geq 0\), and \(a+b+c\geq 0\), as \(a\), \(b\) and \(c\) are positive.

Therefore, \[a^3+b^3+c^3-3abc\geq 0,\] which implies \[a^3+b^3+c^3\geq 3abc.\]

Hence, \[\frac{1}{3}(p+q+r)\geq (pqr)^{\frac{1}{3}}.\]

This is the arithmetic mean-geometric mean (AM-GM) inequality for three variables: again, the arithmetic mean is always greater than or equal to the geometric mean.

What happens if we try to generalise to more variables?
