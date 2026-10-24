---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r9366
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r9366
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9366
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
  - code: 3.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "10a^2=b^3 with log_10 a = log_10 b + 1 - 'taking logs to base 10' solves the indicial system; a and b expressed as powers of 10"
      rationale: "Canonical UGM title: Can we find $a$ and $b$ as powers of $10$?"
      validation_status: SUGGESTED
    title: "use logarithms to solve equations and e.g. inequalities in which the unknown appears in indices"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "O&C O level Additional Mathematics 1, QP R826, 1975, Q2(ii)"
  task: T-UGM-IMPORT-10
---

# Can we find $a$ and $b$ as powers of $10$?

## Question

## Solution

**Approach 1:**

We have that \(10a^2 = b^3\). Taking logs to base \(10\) gives \(\log_{10}10 + 2\log_{10}a=3\log_{10}b.\)

But we know that \(\log_{10} a = \log_{10}b + 1\), and so \(1+2(\log_{10}b + 1)=3\log_{10}b.\)

This gives \(\log_{10}b = 3\), and so \(b = 10^3\), and \(a = 10^4\).

**Approach 2:**

We have

\[\begin{align*} \log_{10} a &= \log_{10} b+1\\ \implies \log_{10} a &= \log_{10} b + \log_{10} 10\\ \implies \log_{10} a &= \log_{10} (10b)\\ \implies a &= 10b. \end{align*}\]

Using the other equation, we find \[100b^2 = \frac{b^3}{10},\] and so \(b=0\) or \(b=1000\).

However \(\log_{10} 0\) is not defined, and hence \(b=0\) is not a solution.

Thus \(b=10^3\), which leads to \(a=\pm 10^4\). Again, \(\log_{10}a\) appears in the question so \(a\) cannot be negative.

So we have \(b=10^3\) and \(a=10^4\).
