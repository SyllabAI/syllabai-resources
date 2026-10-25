---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r6806
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r6806
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6806
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: exp-and-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: exp-and-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "part (c) evaluates 2/(5(2+5log_b c)) + 1/(5+2log_c b) through the identity 1/(a+y)+1/(a+z)=1/a with log_b c · log_c b = 1 - the reciprocal relation read off the definition of the logarithm"
      rationale: "Canonical UGM title: If $yz=a^2$, can we prove that $1/(a+y) + 1/(a+z) = 1/a$?"
      validation_status: SUGGESTED
    title: "understand the relationship between logarithms and indices, and use the laws of logarithms (excluding change of base)"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "UCLES A level Mathematics 1 and Pure Mathematics 1, QP 417/1 and 447/1, 1963, Q1"
  task: T-UGM-IMPORT-10
---

# If $yz=a^2$, can we prove that $1/(a+y) + 1/(a+z) = 1/a$?

## Question

If \(yz=a^2\) prove that \[\frac{1}{a+y} + \frac{1}{a+z} = \frac{1}{a}.\]

By using this result, or otherwise, find the numerical values of

1. \(\dfrac{1}{1+x^k} + \dfrac{1}{1+x^{-k}}\);

---

1. \(\dfrac{1}{7+\sqrt{62}-\sqrt{13}} + \dfrac{1}{7+\sqrt{62}+\sqrt{13}}\);

---

1. \(\dfrac{2}{5(2+5\log_b c)} + \dfrac{1}{5+2\log_c b}\);

## Solution

Solving \(yz=a^2\) for \(y\), we obtain

\[y=\dfrac{a^2}{z},\]

which we can substitute into the left-hand side of the given expression. This leads us to

\[\begin{align*} \frac{1}{a+y} + \frac{1}{a+z} &= \frac{1}{a+\dfrac{a^2}{z}} + \frac{1}{a+z}\\ &=\dfrac{z}{az+a^2} + \dfrac{a}{a(a+z)}\\ &=\dfrac{a+z}{a(a+z)}=\dfrac{1}{a}, \end{align*}\]

as required.

Comparing this expression with the one above leads to setting \(a=1\), \(x^k=y\) and \(x^{-k}=z\). These values clearly fulfil \(yz=a^2\), and hence give us

\[\frac{1}{1+x^k} + \frac{1}{1+x^{-k}} = 1.\]

We have \((\sqrt{62}-\sqrt{13})(\sqrt{62}+\sqrt{13})=62-13=49=7^2\), which means we can we take \(a=7\), \(y=\sqrt{62}-\sqrt{13}\) and \(z=\sqrt{62}+\sqrt{13}\).

Thus \[\frac{1}{7+\sqrt{62}-\sqrt{13}} + \frac{1}{7+\sqrt{62}+\sqrt{13}}=\frac{1}{7}.\]

We can write this as

\[\frac{1}{5+\dfrac{25}{2}\log_b c} + \frac{1}{5+2\log_c b}.\]

This looks rather like the expression at the start of the question, so let us try \(a=5\), \(y=\dfrac{25}{2}\log_b c\) and \(z=2\log_c b\). Then \[yz=\dfrac{25}{2}\log_b c\times2\log_c b = 25\log_b c\times\log_c b = 25 = a^2 .\]

We have used the law of logarithms for changing bases which states that \[\log_a b=\log_a c\times \log_c b .\]

So we can state that \[\frac{2}{5(2+5\log_b c)} + \frac{1}{5+2\log_c b}=\frac{1}{5}.\]
