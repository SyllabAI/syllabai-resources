---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/discussing-distance
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/problem-requiring-decisions
- level/introducing
resource_identity:
  ugm_id: discussing-distance
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 6
  resource_type_label: Problem requiring decisions
  level: Introducing
  ref: 7371
  old_site_id: C1_RT2_5
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: introducing-calculus
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: introducing-calculus
    validation_status: SUGGESTED
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/introducing-calculus/discussing-distance/download/teacher-notes.pdf
  kind: printable
---

# Discussing distance

> Excerpt: This resource asks students to decide what two unlabelled graphs represent. It goes on to ask students to think carefully about the difference between graphing distance and graphing displacement. Are the graphs always different?

## Problem

The two graphs below depict the same journey along a straight road.

- What’s the same and what’s different about the graphs?

- What do you think the labels on the each of the axes would be?

Suggestion

- What sort of things do we measure when taking a journey? Which axis are these likely to go on?

- If you walk to school, and then home again, how far have you walked and how far have you moved from your starting point?

## Solution

Initial ideas might have been a distance-time graph and a speed-time graph. If this were true, would it be possible for them to represent the same journey? How would a constant speed be represented on each?

If we think only about distance, we should notice that the two graphs cannot both be distance-time graphs. Distance can only go on increasing; you cannot undo the distance you have travelled. The left hand graph is a distance-time graph, but the right hand graph is something else, in this case a displacement-time graph.

Displacement explanation

If you walk \(\quantity{1.5}{km}\) to school every day then, when you have walked home, you have covered a distance of at least \(\quantity{3}{km}\) by the end of the day. However, if you talk about displacement, then by the end of the day you are back at your starting point, so your displacement is \(0\).

Distance is how much ground you have covered in your travels, whereas displacement looks at how far you are from your starting point.

If we compare the graphs, then from \(0\) to \(10\) on the \(x\) axis, our graphs are identical. After this, they differ.

- What do you think changes in the journey after this point?

- What do you notice about the gradients of the same section on each graph?

To use the same graphs to explore further graphical representations of journeys, go to [Speed vs velocity](https://undergroundmathematics.org/introducing-calculus/speed-vs-velocity).

## Thinking about journeys

The journey described by our graphs was along a straight road. This is a very simplistic and unlikely journey in the real world.

For each of the situations below, can you sketch a distance-time graph and a displacement-time graph?

- Do the graphs look the same?

- Are they both possible to draw?

**Situation one**

You walk straight to school travelling at a constant speed of \(\quantity{0.5}{m\,s^{-1}}\).

Discussion points

We didn’t state where we were measuring displacement from. The graph above shows the displacement measured from ‘home’. If instead displacement was measured from ‘school’, how would the displacement graph change?

- Would the distance graph also change?

- How many dimensions is our journey taking place in?

**Situation two**

You walk straight along the road from home to school and at the end of the first road you take a \(90^{\circ}\) turn left. You travel at a constant speed of \(\quantity{0.5}{m\,s^{-1}}\).

At faster speeds we would expect to slow down when we approach and turn a corner. Here we are making the assumption that the constant speed of \(\quantity{0.5}{m\,s^{-1}}\) is maintained.

Discussion points

While the distance-time graph is easy to draw (and is the same as above), the displacement-time graph may have caused a few more problems. Remember, we defined displacement as how far you are from the starting point (assuming displacement is being measured from there) so, while you might be moving at \(\quantity{0.5}{m\,s^{-1}}\), you are not moving away from the starting point at this speed.

When the distance travelled is \(\quantity{125}{m}\), the displacement seems to be \[\sqrt{100^2+25^2}\approx \quantity{103}{m}.\]

Does our answer of \(103\) m make sense?

In Situation one, we were travelling in one dimension, so we had forward (positive displacement) and backward (negative displacement). If I told you that you were \(103\) m away from your starting point in a two dimensional world, would you be able to tell me where you were?

We need extra information. Displacement is a [vector](https://undergroundmathematics.org/glossary/vector) quantity which tells us both the distance from the starting point and the direction. In one dimension, the direction could be either positive or negative, but in two dimensions that is not enough.

We might give an angle along with our distance. For example, \(103\)m at an angle of \(14.04^{\circ}\), although we would have to know where our angle is being measured from and in which direction.

Or we might use our two dimensions as separate directions, at right angles to one another, that can be positive or negative. (This should sound familiar!) We could write the displacement as \(\begin{pmatrix} 100 \\ 25 \end{pmatrix}\). Where have you seen something like this before?

Either way, this represents our displacement at a single point, and not the displacement throughout the journey. That displacement cannot meaningfully be sketched on a displacement-time graph.

Representing a simple journey in two dimensions can become complicated when we think about displacement, rather than distance travelled. Does the same happen with speed and velocity? These questions are considered in [Speed vs velocity](https://undergroundmathematics.org/introducing-calculus/speed-vs-velocity).
