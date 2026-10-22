---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/r9709
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/review-question
resource_identity:
  ugm_id: r9709
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9709
  old_site_id: Q122
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: geometry-of-equations
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: geometry-of-equations
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'Largest x satisfying three linear inequalities — vertex exploration of a feasible region; the optimisation framing is LP-flavoured (recorded medium).'
      rationale: 'Canonical UGM title: “What is the largest $x$ to satisfy these three inequalities?”; exam provenance: Oxford (MAT) None Q1D'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford (MAT) None Q1D
task: T-UGM-IMPORT-3
---

# What is the largest $x$ to satisfy these three inequalities?

## Question

The numbers

\(x\)

and

\(y\)

satisfy the following inequalities

\[\begin{align*} 2x+3y &\le 23, \\ x+2 &\le 3y, \\ 3y+1 &\le 4x. \end{align*}\]

The largest possible value of \(x\) is

1. \(6\),

---

1. \(7\),

---

1. \(8\),

---

1. \(9\).

## Suggestion

Can we draw a diagram? Where are all the inequalities satisfied?

Or would working purely algebraically be more useful?

Where in this region does the largest value of \(x\) occur?

## Solution

**A graphical approach**

First, we sketch the three lines

\[\begin{align*} 2x+3y &= 23, \\ x+2 &= 3y\quad\text{and}\\ 3y+1 &=4x, \end{align*}\]

by rearranging them in the form \(y=mx+c\) first.

Then thinking about which side of each of the lines is satisfied by the inequalities, we see that the central triangular region is the one satisfied by all three inequalities.

We can see from the graph that the largest possible value of \(x\) is where the lines \(2x+3y=23\) and \(x+2=3y\) intersect, which is at the point \((7,3)\).

So the answer is (b).

**An algebraic approach**

We want to find the largest possible value of \(x\), so we aim to eliminate \(y\).

- First attempt: The third inequality rearranges to give \(3y\le 4x-1\). We cannot substitute this into the first inequality, as the directions of the inequalities are not compatible. If we substitute it into the second inequality, though, we obtain \(x+2\le 4x-1\), so \(3x\ge3\), or \(x\ge1\), which is not so helpful.

- Second attempt: The first inequality rearranges to give \(3y\le 23-2x\). Combining this with the second inequality gives \[x+2\le 3y\le 23-2x\] so \(3x\le 21\) or \(x\le7\). If \(x=7\), the second inequality gives \(9\le 3y\), so we could try \(y=3\). This pair of values satisfies all three inequalities, so the greatest possible value of \(x\) is \(7\), and the answer is (b).
