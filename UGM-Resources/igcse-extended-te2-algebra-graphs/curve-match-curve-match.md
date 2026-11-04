---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-functions/curve-match
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-functions
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: curve-match
  station: thinking-about-functions
  station_title: Thinking about Functions
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 6285
  old_site_id: F1_RT12_2
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: thinking-about-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-functions
    validation_status: SUGGESTED
  spec_points:
  - code: E2.11.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: Graphs of powers of x and related functions matched to equations — E2.11.1 form-recognition
        register.
      rationale: 'Canonical UGM title: “Curve match”; exam provenance: Based on this

        NRICH resource

        , used with permission. The NRICH resource remains Copyright University of Cambridge,

        All rights reserved

        .'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: 'Based on this

    NRICH resource

    , used with permission. The NRICH resource remains Copyright University of Cambridge,

    All rights reserved

    .'
task: T-UGM-IMPORT-19
assets:
- path: https://undergroundmathematics.org/thinking-about-functions/curve-match/images/diagram.png
  kind: figure
---

# Curve match

> Excerpt: This offers an exploration of the graphs of powers of $x$ and related functions.  By comparing the graphs with each other, students are asked to match a set of graphs to their equations.

## Problem

The following five functions have been plotted accurately on the axes below.

- \(y=\sqrt{x}\)
- \(y=x^2\)
- \(y=x\)
- \(y=\dfrac{x^2+x}{2}\)
- \(y=2\sqrt{x}-x\)

> [figure: Graphs of all 5 functions, all of which pass through the origin and (1,1), but each with different curvatures in between. — `https://undergroundmathematics.org/thinking-about-functions/curve-match/images/diagram.png`] (image not included in the text import; path of record).

Can you label each curve?

Imagine that you wish to plot a route between \((0,0)\) and \((1,1)\). Can you find a function that does this without intersecting any of the existing curves, except at the end points?

What other curves can you plot that intersect the existing curves only at the end points?

## Solution

We know that \(y = x\) is a straight line, passing through both the origin and \((1,1)\), so this is the middle ‘curve’.

For \(x\) between \(0\) and \(1\), we know that \(x^2 < x\), so the curve \(y = x^2\) must lie below the straight line. Similarly, for these \(x\) we have \(\sqrt{x} > x\) and so the curve \(y = \sqrt{x}\) lies above the straight line.

Now \(y = \dfrac{x^2 + x}{2}\) is the average of \(x^2\) and \(x\), so must lie between the two. So working down from \(y = x\) (the straight line in the middle) we first reach \(y = \dfrac{x^2 + x}{2}\) and then \(y = x^2\).

Since \(\sqrt{x} > x\), we have \(2\sqrt{x} - x > \sqrt{x}\). So working up from \(y = x\) we first reach \(y = \sqrt{x}\) and then \(y = 2\sqrt{x} - x.\)

To summarise, from top to bottom we have \(y = 2\sqrt{x} - x\), then \(y = \sqrt{x}\), then \(y = x\), then \(y = \dfrac{x^2 + x}{2}\), and finally \(y = x^2\) at the bottom.

---

There are many curves that we could choose.

One way to generate many examples would be to take averages of two or more of the above curves, in just the same way that we took the average of \(x\) and \(x^2\) to get a new curve. We might need to be a bit careful in our choice of curves in order to ensure that the new curve does not intersect any of the existing curves other than at the end points.

We could pick a polynomial such as \(y = x^3\); we can check that this intersects the existing curves only at \(x = 0\) and \(x = 1\).
