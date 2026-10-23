---
created: 2026-10-24T04:45:46 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/r5549
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/review-question
resource_identity:
  ugm_id: r5549
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5549
  old_site_id: None
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-meets-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-meets-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.8.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-8 cross-map (cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd)"
      evidence: "evaluates a definite integral of a piecewise-linear f composed with x^2-1 by reducing to the integral of x^2 over [-1,1] — definite integration of x^2 after composition"
      rationale: "Canonical UGM title: \"If we know $f(x)$, can we find $\\int_{-1}^1 f(x^2-1) \\:dx$?\""
      validation_status: SUGGESTED
    title: "evaluate definite integrals"
  mapped_date: '2026-10-24'
  mapper: cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-8
---

# If we know $f(x)$, can we find $\int_{-1}^1 f(x^2-1) \:dx$?

## Question

A graph of the function \(y=f(x)\) is sketched on the axes below;

The value of \(\displaystyle\int_{-1}^1 f(x^2-1) \:dx\) equals (a) \(\dfrac{1}{4}\qquad\) (b) \(\dfrac{1}{3}\quad \quad\) (c) \(\dfrac{3}{5}\quad \quad\) (d) \(\dfrac{2}{3}\).

## Suggestion

Can we write down an equation for \(f(x)\) for each distinct interval?

Can we then write down what \(f(x^2-1)\) is?

If the values of \(x\) run from \(-1\) to \(1\), what values does \(x^2 -1\) run through?

## Solution

A graph of the function \(y=f(x)\) is sketched on the axes below;

The value of \(\displaystyle\int_{-1}^1 f(x^2-1) \:dx\) equals (a) \(\dfrac{1}{4}\qquad\) (b) \(\dfrac{1}{3}\qquad\) (c) \(\dfrac{3}{5}\qquad\) (d) \(\dfrac{2}{3}\).

We can write the function as \[f(x) = \begin{cases} x+1, & -1 \le x \le 0; \\ 1-x, & 0 \le x \le 1; \\ 0, & \text{otherwise.} \end{cases}\]

By substituting we can say, \[f(x^2-1) = \begin{cases} x^2-1+1 = x^2, & -1 \le x^2-1 \le 0; \\ 1-x^2+1 = 2-x^2, & 0 \le x^2-1 \le 1; \\ \qquad 0, & \text{otherwise.} \end{cases}\]

The first of these intervals can be rewritten, \[-1 \le x^2-1 \le 0 \quad\implies\quad 0\le x^2\le 1 \quad\implies\quad -1\le x \le 1.\] We only need to integrate over this interval, so we do not need to worry about the second interval.

So we have \[\int_{-1}^1 f(x^2-1) \:dx = \int_{-1}^1 x^2 \:dx = \left[\frac{x^3}{3}\right]_{-1}^1 = \dfrac{2}{3}\] and the answer is (d).

There are two intervals that we are interested in, $-1 \leq x \leq 0$, and $0 \leq x \leq 1$ (everywhere else the function $f(x)$ is zero). The inequality $-1 \leq x \leq 0$ becomes on squaring $1 \geq x^2 \geq 0$, and so $0 \geq x^2 - 1 \geq -1$. The inequality $0 \leq x \leq 1$ becomes on squaring $0 \leq x^2 \leq 1$, and so $-1 \leq x^2 -1 \leq 0$. These intervals are the same, so we can simply focus on what happens to $f(x^2-1)$ for $x$ on the interval $[-1, 0]$. On this domain, $f(x) = 1+x$, and so $f(x^2-1) = 1+x^2-1 = x^2$. Thus $$\int_{-1}^1 f(x^2-1) \:dx = \int_{-1}^1 x^2 \:dx = \left[\frac{x^3}{3}\right]_{-1}^1 = \dfrac{2}{3}$$ and so the answer is (d). <cm-chalk> An alternative approach could be to draw up a table. <cm-table> <cm-tr> <cm-td>$x$</cm-td><cm-td>-2</cm-td><cm-td>-1.5</cm-td><cm-td>-1</cm-td><cm-td>-0.5</cm-td><cm-td>0</cm-td><cm-td>0.5</cm-td><cm-td>1</cm-td><cm-td>1.5</cm-td><cm-td>2</cm-td> </cm-tr> <cm-tr> <cm-td>$x^2-1$</cm-td><cm-td>3</cm-td><cm-td>1.25</cm-td><cm-td>0</cm-td><cm-td>-0.75</cm-td><cm-td>-1</cm-td><cm-td>-0.75</cm-td><cm-td>0</cm-td><cm-td>1.25</cm-td><cm-td>3</cm-td> </cm-tr> <cm-tr> <cm-td>$f(x^2-1)$</cm-td><cm-td>0</cm-td><cm-td>0</cm-td><cm-td>1</cm-td><cm-td>0.25</cm-td><cm-td>0</cm-td><cm-td>0.25</cm-td><cm-td>1</cm-td><cm-td>0</cm-td><cm-td>0</cm-td> </cm-tr> </cm-table> Plotting these points strongly suggests we are interested in the area under $y = x^2$ between $-1$ and $1$. </cm-chalk>
