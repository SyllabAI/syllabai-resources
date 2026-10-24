---
created: 2026-10-25T01:37:17 (UTC +06:00)
source: https://undergroundmathematics.org/polynomials/r5276
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- polynomials
- type/review-question
resource_identity:
  ugm_id: r5276
  station: polynomials
  station_title: Polynomials & Rational Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5276
  old_site_id: "Q242"
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
  - code: 3.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "remainder of p_n(x)/p_{n−1}(x) by long division (Approach 1) and by the remainder theorem at the root of p_{n−1} (Approach 2); linear-by-linear division with quotient n/(n−1)"
      rationale: "Canonical UGM title: What is the remainder when $p_n (x)$ is divided by $p_{n-1} (x)$?"
      validation_status: SUGGESTED
    title: "divide a polynomial, of degree not exceeding 4, by a linear or quadratic polynomial, and identify the quotient and remainder (which may be zero)"
  - code: 3.1.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-9 cross-map (cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb)"
      evidence: "remainder of p_n(x)/p_{n−1}(x) by long division (Approach 1) and by the remainder theorem at the root of p_{n−1} (Approach 2); linear-by-linear division with quotient n/(n−1)"
      rationale: "Canonical UGM title: What is the remainder when $p_n (x)$ is divided by $p_{n-1} (x)$?"
      validation_status: SUGGESTED
    title: "use the factor theorem and the remainder theorem"
  mapped_date: '2026-10-25'
  mapper: cross-map-algebra.json (P3c lane 9) @ syllabai-experimental 3098d8eb
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, 2013, Q1G"
  task: T-UGM-IMPORT-9
---

# What is the remainder when $p_n (x)$ is divided by $p_{n-1} (x)$?

## Question

Let \(n \ge 2\) be an integer and \(p_n (x)\) be the polynomial \[p_n (x) = (x-1) + (x-2) + \cdots + (x-n).\] What is the remainder when \(p_n (x)\) is divided by \(p_{n-1} (x)\)?

1. \(\dfrac{n}{2}\);

---

1. \(\dfrac{n+1}{2}\);

---

1. \(\dfrac{n^2+n}{2}\);

---

1. \(\dfrac{-n}{2}\).

## Suggestion

The terms in \(p_n (x)\) follow a sequence - can we sum this?

What value of \(x\) makes \(p_{n-1}(x)\) zero?

## Solution

We can use the formula for the sum of an arithmetic progression to calculate \[p_n(x) = nx - \frac{n(n+1)}{2}\] and \[p_{n-1}(x) = (n-1)x - \frac{n(n-1)}{2}.\]

**Approach 1**

We can carry out long division, by noting that the

\(x\)

term of

\(p_{n-1}(x)\)

divides

\(\dfrac{n}{n-1}\)

times into the

\(x\)

term of

\(p_n(x)\)

, so that the remainder is

\[\begin{align*} p_n(x) - \dfrac{n}{n-1}p_{n-1}(x) &{}= \left(nx - \dfrac{n(n+1)}{2}\right) - \dfrac{n}{n-1} \left((n-1)x - \dfrac{n(n-1)}{2}\right)\\ &{}= -\dfrac{n(n+1)}{2} + \dfrac{n^2}{2}\\ &{}= \dfrac{-n}{2}, \end{align*}\]

and the answer is (d).

**Approach 2**

We can use the Remainder Theorem. We have that \[p_{n-1}(x)=(n-1)\bigl(x-\tfrac{1}{2}n\bigr),\] and so \(p_{n-1}(x) =0\) when \(x = \dfrac{n}{2}\) (we can ignore the \(n-1\) factor as it will not change the remainder).

So the remainder is equal to \(p_n\left(\dfrac{n}{2}\right) = -\dfrac{n}{2}\), as before.

The answer is (d).
