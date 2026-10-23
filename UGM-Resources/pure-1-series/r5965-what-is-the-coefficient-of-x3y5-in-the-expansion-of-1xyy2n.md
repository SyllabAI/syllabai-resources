---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/counting-and-binomials/r5965
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- counting-and-binomials
- type/review-question
resource_identity:
  ugm_id: r5965
  station: counting-and-binomials
  station_title: Counting & Binomials
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5965
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: counting-and-binomials
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: counting-and-binomials
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: coefficient of x^3 y^5 in (1+xy+y^2)^n by writing (1+y(x+y))^n and applying the binomial
        expansion twice
      rationale: 'Canonical UGM title: "What is the coefficient of $x^3y^5$ in the expansion of  $(1+xy+y^2)^n$?";
        exam provenance: Oxford University Mathematics Aptitude Test, 2014, Q1G'
      validation_status: SUGGESTED
    title: use the expansion of ( a + b ) , where n is a positive integer
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2014, Q1G
task: T-UGM-IMPORT-6
---

# What is the coefficient of $x^3y^5$ in the expansion of  $(1+xy+y^2)^n$?

## Question

Let \(n\) be a positive integer. The coefficient of \(x^3y^5\) in the expansion of

\[(1+xy+y^2)^n\]

equals

\[(a) \quad n,\quad(b) \quad 2^n,\quad(c) \quad \begin{pmatrix}n\\3\end{pmatrix} \begin{pmatrix}n\\5\end{pmatrix},\quad(d) \quad 4\begin{pmatrix}n\\4\end{pmatrix},\quad(e) \quad\begin{pmatrix}n\\8\end{pmatrix}.\]

## Suggestion

Could we write \((1+xy+y^2)^n\) as \((1+y(x+y))^n\)? What happens if we expand this with the binomial theorem now?

## Solution

We can write the expression as

\[(1+y(x+y))^n = 1 + \begin{pmatrix}n\\1\end{pmatrix}y(x+y)+\begin{pmatrix}n\\2\end{pmatrix}y^2(x+y)^2+\begin{pmatrix}n\\3\end{pmatrix}y^3(x+y)^3+\begin{pmatrix}n\\4\end{pmatrix}y^4(x+y)^4+\begin{pmatrix}n\\5\end{pmatrix}y^5(x+y)^5+...\]

The powers in \(x^3y^5\) add to 8, so the only term that interests us is \(\begin{pmatrix}n\\4\end{pmatrix}y^4(x+y)^4.\)

We need the \(x^3y\) term in \((x+y)^4\), which has coefficient \(\begin{pmatrix}4\\3\end{pmatrix} = 4\). Thus the coefficient of \(x^3y^5\) overall is \(4\begin{pmatrix}n\\4\end{pmatrix}\), and the answer is (d).
