---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r8775
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r8775
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8775
  old_site_id: Q3050
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Form a quadratic from given data/conditions.
      rationale: 'Canonical UGM title: “Can we fit a quadratic to this given data?”; exam provenance:
        UCLES 1967 Q1'
      validation_status: SUGGESTED
    title: solve quadratic equations, and quadratic By factorising, completing the square and using the
      inequalities, in one unknown formula.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1967 Q1
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/r8775/images/data-plot-labelled.png
  kind: figure
- path: https://undergroundmathematics.org/quadratics/r8775/images/plot-with-line-labelled.png
  kind: figure
---

# Can we fit a quadratic to this given data?

## Question

| \(x\vphantom{4}\) | \(4\) | \(7\) | \(10\) | \(13\) |
| --- | --- | --- | --- | --- |
| \(\smash{y}\vphantom{4}\) | \(96\) | \(133\) | \(160\) | \(117\) |

In the above table the values of \(y\) were calculated from a formula \(y = Ax^2 + Bx\), where \(A\) and \(B\) are constants. One of the values of \(y\), however, has been deliberately misprinted.

Plot the values of \(y/x\) against those of \(x\), and

1. find which value of \(y\) has been misprinted and give the correct value,
2. estimate the numerical values of \(A\) and \(B\).

## Suggestion

In the above table the values of \(y\) were calculated from a formula \(y = Ax^2 + Bx\), where \(A\) and \(B\) are constants. One of the values of \(y\), however, has been deliberately misprinted.

Plot the values of \(y/x\) against those of \(x\), …

Why does the question ask us to use \(y/x\) rather than \(y\)?

## Solution

| \(x\vphantom{4}\) | \(4\) | \(7\) | \(10\) | \(13\) |
| --- | --- | --- | --- | --- |
| \(\smash{y}\vphantom{4}\) | \(96\) | \(133\) | \(160\) | \(117\) |

In the above table the values of \(y\) were calculated from a formula \(y = Ax^2 + Bx\), where \(A\) and \(B\) are constants. One of the values of \(y\), however, has been deliberately misprinted.

 Plot the values of

\(y/x\)

 against those of

\(x\)

…

We have the following calculated data:

| \(x\vphantom{4}\) | \(4\) | \(7\) | \(10\) | \(13\) |
| --- | --- | --- | --- | --- |
| \(\smash{y/x}\vphantom{4}\) | \(24\) | \(19\) | \(16\) | \(9\) |

The data are plotted below.

> [figure: A plot of $y/x$ against $x$. — `https://undergroundmathematics.org/quadratics/r8775/images/data-plot-labelled.png`] (image not included in the text import; path of record).

If \(y = Ax^2 + Bx\), then \(y/x = Ax + B\).

This is the equation of a straight line, so, given the information in the question, we should expect to find a line through three of the four points plotted above. This is in fact the case!

> [figure: A plot of $y/x$ against $x$, together with an added line. — `https://undergroundmathematics.org/quadratics/r8775/images/plot-with-line-labelled.png`] (image not included in the text import; path of record).

From the plot above, the incorrect value of \(y\) is the one corresponding to \(x=10\), namely \(160\).

Since the correct value of \(y/x\) must lie on the line, this value is \(14\), and so the correct value of \(y\) is \(14\times10=140\).

The equation of the blue line is \(y/x = Ax + B\), so we can find the value of \(A\) by finding the gradient of the line and the value of \(B\) by finding its \(y\)-intercept.

The gradient of the line in the plot above is (from looking at the points where \(x=4\) and \(x=13\)) \[ \frac{\Delta y}{\Delta x} = \frac{9 - 24}{13 - 4} = -\frac{15}{9} = -\frac{5}{3} \] so \(A = -\dfrac{5}{3}\). Taking the point with \(x=4\), \(y/x=24\), we have \[24=-\frac{5}{3}\times 4+B\] so \(B=\dfrac{92}{3}=30\frac{2}{3}\).

If we were doing this problem using real-world data rather than calculated figures, we would not use our data points to find the equation of the line (and hence \(A\) and \(B\), but would instead use points on the line itself. In this case, though, these are the same thing.
