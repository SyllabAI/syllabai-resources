---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r5764
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r5764
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5764
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Ranges of [x] and x-[x]; sketch; solve f(x)=g(x) and fg(x)=gf(x). Floor function beyond
        P1 routine.
      rationale: 'Canonical UGM title: “Can we sketch the graph of $g \colon x \to x - [x]$?”; exam provenance:
        UCLES 1976 Q[''Q2''] [848/1]'
      validation_status: SUGGESTED
    title: identify the range of a given function in simple cases, and find the composition of two given
      functions condition that a composite function
  - code: 1.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Ranges of [x] and x-[x]; sketch; solve f(x)=g(x) and fg(x)=gf(x). Floor function beyond
        P1 routine.
      rationale: 'Canonical UGM title: “Can we sketch the graph of $g \colon x \to x - [x]$?”; exam provenance:
        UCLES 1976 Q[''Q2''] [848/1]'
      validation_status: SUGGESTED
    title: understand the terms function, domain, range, one-one function, inverse function and composition
      of functions
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1976 Q['Q2'] [848/1]
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/r5764/images/plot-labelled.png
  kind: figure
---

# Can we sketch the graph of $g \colon x \to x - [x]$?

## Question

For any real number

\(x\)

,

\([x]\)

denotes the greatest integer not exceeding

\(x\)

; e.g.

\([3.6] = 3\)

,

\([2] = 2\)

,

\([-1.4] = -2\)

, etc. Functions

\(f\)

and

\(g\)

are defined on the domain of all real numbers as follows:

\[\begin{equation*} f \colon x \to [x]; \quad g \colon x \to x - [x]. \end{equation*}\]

Find the ranges of \(f\) and \(g\), and sketch the graph of \(g\).

Determine the solution sets of the equations

1. \(f(x) = g(x),\qquad\) (ii) \(fg(x) = g\,f(x)\).

## Solution

The function \([x]\) defined here is known as the [floor function](https://undergroundmathematics.org/glossary/floor-function).

From the definition of the floor function, the output value of \(f\) will always be an integer. Since the input \(x\) can be any real number the range of \(f\) is all the integers, \(\mathbb{Z}\).

The function \(g(x)=x-[x]\) which means it subtracts the whole number part, leaving only the fractional part of the input value \(x\).

For integer values of \(x\), \([x]=x\) which means that \(g(x)=0\). So the graph of the function looks like this.

> [figure: Sketch of the graph of g — `https://undergroundmathematics.org/combining-functions/r5764/images/plot-labelled.png`] (image not included in the text import; path of record).

The range is \(0\leq g(x)<1\).

Determine the solution sets of the equations

1. \(f(x) = g(x)\)

We want to find for which values of

\(x\)

,

\[\begin{equation*} f(x) = g(x) \iff [x] = x - [x]. \end{equation*}\]

The left-hand side is always an integer, while the only integer value that the right-hand side can take is zero, which occurs whenever \(x\) is an integer.

The solution set is therefore \(x=0\).

Since the range of

\(g\)

is

\(0\leq g(x)<1\)

we have that

\[\begin{equation*} fg(x) = [g(x)] = 0. \end{equation*}\]

We also have that

\[\begin{equation*} g\,f(x) = g([x]) = [x] - [[x]] = 0. \end{equation*}\]

The equation is therefore satisfied regardless of the value of \(x\). The solution set is the real numbers, \(\mathbb{R}\).
