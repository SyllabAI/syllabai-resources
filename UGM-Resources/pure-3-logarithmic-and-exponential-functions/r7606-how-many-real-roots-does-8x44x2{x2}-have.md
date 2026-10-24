---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/r7606
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/review-question
resource_identity:
  ugm_id: r7606
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7606
  old_site_id: "Q79"
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
      evidence: "8^x+4=4^x+2^{x+2} - 'the unknown x is in the exponents. Could we make a substitution?' y=2^x gives a factorable cubic; three real solutions"
      rationale: "Canonical UGM title: How many real roots does $8^x+4=4^x+2^{x+2}$ have?"
      validation_status: SUGGESTED
    title: "use logarithms to solve equations and e.g. inequalities in which the unknown appears in indices"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: "Oxford University Mathematics Aptitude Test, 2007, Q1F"
  task: T-UGM-IMPORT-10
---

# How many real roots does $8^x+4=4^x+2^{x+2}$ have?

## Question

The equation \[8^x+4=4^x+2^{x+2}\] has

1. no real solutions;

---

1. one real solution;

---

1. two real solutions;

---

1. three real solutions.

[A real solution is one that lies on the number line.]

## Suggestion

This equation looks difficult because the unknown \(x\) is in the exponents. Could we make a substitution to make it look more like a familiar type of equation?

## Solution

First set

\(y=2^x\)

. Then the equation can be rewritten as

\[\begin{align*} &y^3+4=y^2+4y\\ \iff &y^3-y^2-4y+4=0. \end{align*}\]

The left hand side can be factorised (by noticing that if we substitute

\(y=1\)

then we have a solution).

\[\begin{align*} &(y-1)(y^2-4)=0\\ \iff &(y-1)(y-2)(y+2)=0 \end{align*}\]

So the possible solutions are \(y=1\), \(y=2\), \(y=-2\). But \(y=2^x>0\) for real \(x\), so valid solutions occur when \(y=1\) or \(y=2\).

This gives the solutions \(x=0\) and \(x=1\) respectively, but since we’re only asked how many solutions there are, we don’t actually need to find them (provided we can be sure they exist!)

So the equation has two real solutions. The answer is (c).

The curve \(y=8^x+4-4^x-2^{x+2}\)
