---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r6414
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r6414
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6414
  old_site_id: "Q217"
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
      evidence: "a^x > cb^y taken to logs: 'x log a > log c + y log b' (base > 1 so log is increasing) - finitely many positive integer solutions classified by a,b against 1"
      rationale: "Canonical UGM title: When does this inequality have a finite number of integer solutions?"
      validation_status: SUGGESTED
    title: "use logarithms to solve equations and e.g. inequalities in which the unknown appears in indices"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, 2010, Q1J"
  task: T-UGM-IMPORT-10
---

# When does this inequality have a finite number of integer solutions?

## Question

*[Choose the one correct answer and explain your reasoning.]*

Let \(a\), \(b\), \(c\) be positive numbers. There are *finitely* many *positive whole* numbers \(x\), \(y\) which satisfy the inequality \[a^x > cb^y\] if

1. \(a>1\) or \(b<1\).

---

1. \(a<1\) or \(b<1\).

---

1. \(a<1\) and \(b<1\).

---

1. \(a<1\) and \(b>1\).

## Suggestion

It’s important to notice that the question refers to a *finite* number of solutions…

Can we use logarithms to rewrite the inequality?

## Solution

Taking logarithms of both sides we have \[a^x > cb^y \quad\iff\quad \log(a^x)> \log(cb^y)\] (so long as the base of the logarithm is greater than one, as \(\log x\) is then an increasing function).

This can be rewritten as

\[\begin{align*} x\log a &> \log c+y\log b\\ \iff\quad y\log b &< x\log a - \log c \end{align*}\]

The corresponding equation is of a straight line in the \(x-y\) plane. To find the gradient of this line we want to divide through by \(\log b\) but we must be careful as this could be negative.

We have either \[\text{Case 1: }\quad y < x\frac{\log a}{\log b} - \frac{\log c}{\log b},\quad\text{if } \log b > 0\] or \[\text{Case 2: }\quad y > x\frac{\log a}{\log b} - \frac{\log c}{\log b},\quad\text{if } \log b < 0.\]

To have a finite number of positive solutions the inequality must correspond to the region *below* a straight line with negative gradient.

Case 2 is a region *above* a line, so we need only consider case 1, \(\log b > 0\). We also require the gradient of the line, \(\dfrac{\log a}{\log b}\), to be negative.

Hence, \(\log b > 0\) and \(\log a < 0\). In other words, \(b > 1\) and \(a < 1\).

So the answer is (d).

Why does it not matter whether the \(y\)-intercept of the straight line is positive or negative?

Three possible straight lines
