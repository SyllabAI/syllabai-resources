---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/a-tangent-is
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/building-blocks
- level/introducing
resource_identity:
  ugm_id: a-tangent-is
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Introducing
  ref: 9209
  old_site_id: C1_RT2_3
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
  spec_points:
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: tangent-to-a-curve definition refinement with circle counter-examples; the zoom chord-to-tangent
        interactivity carries the 1.7.1 construct — concept building block for tangent/normal work
      rationale: 'Canonical UGM title: "A tangent is ..."'
      validation_status: SUGGESTED
    title: apply differentiation to gradients, tangents and normals, increasing and decreasing functions
      and rates of change
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/introducing-calculus/a-tangent-is/download/teacher-notes.pdf
  kind: printable
interactive:
- src: //www.geogebratube.org/material/iframe/id/X8qK6jS8/width/810/height/493/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# A tangent is ...

> Excerpt: This resource is designed to provoke discussion and to help build up a sense of what a tangent is. Students are presented with several descriptions and asked to find or sketch an example to show that the proposed definition does not work for all curves.

## Problem

Here are some suggestions of how we could define a tangent to a curve at a point.

1. “A tangent is a straight line which only meets the curve at that one point.”

---

1. “A tangent is a straight line which touches the curve at that point only.”

---

1. “A tangent is a straight line which meets the curve at that point, but the curve is all on one side of the line.”

---

1. “A tangent is a straight line which meets the curve at that point, but near that point, the curve is all on one side of the line.”

Which, if any, of these proposed definitions works for a circle?

For each one, can you find or sketch an example to show that the proposed definition does not work for all curves?

Can you come up with a better definition? (You may like to think about the [Zooming in](https://undergroundmathematics.org/introducing-calculus/zooming-in) resource when answering this question.)

## Solution

Here are some suggestions of how we could define a tangent to a curve at a point.

Which, if any, of these proposed definitions works for a circle?

For each one, can you find or sketch an example to show that the proposed definition does not work for all curves?

All four of the proposed definitions work for circles. Things only stop working when we allow other types of curves.

1. Here’s a case where it meets at more than one point:    And here’s a straight line which only meets the curve at one point, but is clearly not what we would want to call a tangent:

---

1. Here’s a case where a tangent touches the curve at more than one point:

---

1. The first example for statement 1 above shows that this doesn’t work, either.

---

1. This is better than statement 3, but the graph of \(y=x^3\) shows that this doesn’t quite work either. (This same example also shows that statement 3 does not always work.) A rough sketch looks like this; the tangent is the \(x\)-axis:

As we saw in [Zooming in](https://undergroundmathematics.org/introducing-calculus/zooming-in), when we “zoom in” to a point on a curve, it often looks like a straight line. If so, then we can draw that straight line. If we then zoom out again, we will discover that we have drawn the tangent to the curve at that point. This is what a tangent is.

Here is an example for the function \(y=x^2\) at \(x=1\):

We start with the graph of \(y=x^2\):

We zoom in to \((1,1)\) (indicated by the red box):

It looks just like a straight line! So we draw that line on the graph as well (\(y=2x-1\)), here shown in blue:

We now zoom back out:

You can explore this idea yourself using the [interactive graph](https://undergroundmathematics.org/introducing-calculus/a-tangent-is/interactive-graph) or graphing software such as [Desmos](https://www.desmos.com/calculator/).

This problem tells us that a tangent is a *local property* of a graph: the tangent at a point is dependent upon the behaviour of the graph *very near* that point. What goes on elsewhere on the graph is of no interest when finding the tangent.

The gradient of a curve at a point is similarly a local property.

Can you find a graph which does not look like a straight line when you zoom in? (This may only be at one particular point.)

Would the graph have a tangent at that point?

## Interactive graph

This interactivity offers the ability to explore the effect of zooming in on the graph of a function of your choice. You can show a second point, the chord between them and the tangent to the graph: start by clicking “Show triangle”.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/X8qK6jS8/width/810/height/493/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/X8qK6jS8)
