---
created: 2026-10-23T21:23:05 (UTC +06:00)
source: https://undergroundmathematics.org/sequences/square-spirals
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- sequences
- type/food-for-thought
- level/introducing
resource_identity:
  ugm_id: square-spirals
  station: sequences
  station_title: Sequences
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Introducing
  ref: 6381
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: sequences
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: sequences
    validation_status: SUGGESTED
  spec_points:
  - code: 1.6.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-6 cross-map (cross-map-series.json (P3c lane
        6) @ syllabai-experimental 82964ce4)
      evidence: 'square spirals: shaded fractions 1/4+1/16+1/64+... — a visual infinite GP sum (Introducing
        level)'
      rationale: 'Canonical UGM title: "Square spirals"'
      validation_status: SUGGESTED
      primaryPick: true
    title: 'Questions may involve more than one progression. geometric progression, and the formula
      for the sum to infinity of a convergent geometric progression.: • use the condition for the convergence
      of a'
  mapped_date: '2026-10-23'
  mapper: cross-map-series.json (P3c lane 6) @ syllabai-experimental 82964ce4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-6
assets:
- path: https://undergroundmathematics.org/sequences/square-spirals/download/teacher-notes.pdf
  kind: printable
---

# Square spirals

> Excerpt: This resource presents diagrams that offer an interesting and concrete way for students to think about infinite geometric series without needing prior knowledge of geometric sequences.

## Warm-up

What do you notice about the diagram below? What questions could you ask about it?

Things you might think about

- What shapes can you see in the diagram?

- Can you find the area of any of the shapes?

- Can you see any sequences?

- What fraction of the whole shape is each colour?

- Are you making any assumptions in your answers?

## Problem

What fraction of the large square is each shaded square? Write the total shaded area as a sum of fractions.

What fraction of the large square is each shaded triangle? Write the total shaded area as a sum of fractions.

If the area of the large squares is 1, what is the total sum of the shaded area in each case?

Can other sums of fractions be thought about in a similar way? Is it possible to draw a diagram that represents the following sums?

\[\dfrac{1}{2} + \dfrac{1}{4} + \dfrac{1}{8}+ \dfrac{1}{16}+ \dotsb\] \[\dfrac{1}{3} + \dfrac{1}{9} + \dfrac{1}{27} + \dfrac{1}{81} + \dotsb\]

What is the total of each sum?

## Solution

The fractions of each shaded square form a [geometric sequence](https://undergroundmathematics.org/glossary/geometric-sequence).

If we make the assumption that this pattern will be infinite, then the sum of the fractions will be \[\dfrac{1}{4} + \dfrac{1}{16}+ \dfrac{1}{64}+ \dfrac{1}{256} + \dotsb \text{ or } \dfrac{1}{4} + \dfrac{1}{4^2}+ \dfrac{1}{4^3}+ \dfrac{1}{4^4} + \dotsb\]

Do we know anything about the value of this sum? What must it be bigger than? What must it be smaller than?

If the area of the large square is 1, what is the total sum of the shaded area?

There are many ways the total of this sum can be found, but what do we see in the image below?

There are different ways to think about this image, but one is:

We have the same sequence appearing three times, and covering the whole of the square so \[\dfrac{1}{4} + \dfrac{1}{4^2}+ \dfrac{1}{4^3}+ \dfrac{1}{4^4} + \dotsb = \dfrac{1}{3}.\]

To start finding the fraction of each triangle we need to make some assumptions. We will assume that the diagonal lines that form the next square come from the midpoints of the larger square. There are many ways we could find the areas of triangles and the relationships between them, but we will think about similar triangles.

Why are the two triangles similar? What is the length scale factor from the smaller to the larger one? What about the area scale factor?

The larger triangle has sides that are double the length of the smaller triangle, and since they are similar, the area is four times as big.

The two triangles together give \(\dfrac{1}{4}\) of the square. Since the bigger triangle is \(\dfrac{4}{5}\) of \(\dfrac{1}{4}\), it’s \(\dfrac{1}{5}\) of the whole square.

What is the area of the smaller square?

If the area of the large square is 1, what is the total sum of the shaded area in each case?

Each square is \(\dfrac{1}{5}\) of the area of the previous square, so each triangle is \(\dfrac{1}{5}\) of the area of the previous triangle. If the area of the large square is \(1\), the total shaded area is therefore \[\dfrac{1}{5} + \dfrac{1}{5^2} + \dfrac{1}{5^3} + \dfrac{1}{5^4}+ \dotsb \text{ or } \dfrac{1}{5} + \dfrac{1}{25} + \dfrac{1}{125} + \dfrac{1}{625}+ \dotsb.\]

If we think about the image from the warm-up then we see that this sum is equal to \(\dfrac{1}{4}\).

Here are suggestions for each sum.

|  |  |
|---|---|

Using the diagrams we can see the total of the sums. \[\dfrac{1}{2} + \dfrac{1}{4} + \dfrac{1}{8}+ \dfrac{1}{16}+ \dotsb = 1\] \[\dfrac{1}{3} + \dfrac{1}{9} + \dfrac{1}{27} + \dfrac{1}{81} + \dotsb = \dfrac{1}{2}\]

From above we have: \[\dfrac{1}{4} + \dfrac{1}{16}+ \dfrac{1}{64}+ \dfrac{1}{256} + \dotsb = \dfrac{1}{3}\] \[\dfrac{1}{5} + \dfrac{1}{25} + \dfrac{1}{125} + \dfrac{1}{625}+ \dotsb = \dfrac{1}{4}\]

Can you use these infinite sums to find the total of others? For example, can you find the total sum of \(\dfrac{1}{2} + \dfrac{1}{10} + \dfrac{1}{50} + \dfrac{1}{250} + \dotsb\)?

Is it possible that other sums of fractions will sum to the same totals? For example, can you find another infinite sum that equals \(\dfrac{1}{4}\)?
