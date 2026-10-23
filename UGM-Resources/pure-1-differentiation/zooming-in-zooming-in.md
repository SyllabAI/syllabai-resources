---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/zooming-in
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/scaffolded-task
- level/introducing
resource_identity:
  ugm_id: zooming-in
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 3
  resource_type_label: Scaffolded task
  level: Introducing
  ref: 6920
  old_site_id: C1_RT1_2
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
  - code: 1.7.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: 'zoom-in construction on y=x^2: local linearity, chord gradients collected to a formula
        for the gradient function — the limit-of-gradients-of-chords construct of 1.7.1 (lane-6 sweep
        routing pre-identified this resource for 1.7)'
      rationale: 'Canonical UGM title: "Zooming in"'
      validation_status: SUGGESTED
    title: understand the gradient of a curve at a point as the limit of the gradients of a suitable
      sequence of chords, and use the notations d y , and d y f ′ ( x ) , f ″( x ) , 2 for first and
      second derivatives
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/introducing-calculus/zooming-in/download/teacher-notes.pdf
  kind: printable
interactive:
- src: //www.geogebratube.org/material/iframe/id/R89wFrDq/width/429/height/518/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
- src: //www.geogebratube.org/material/iframe/id/X8qK6jS8/width/810/height/493/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Zooming in

> Excerpt: This problem develops the idea that the gradient of a curve can be understood by zooming in to the graph. The collected results at the end can lead to a formula for the gradient function (derivative) of $x^2$.

## Activity

- What happens if we “zoom in” to a graph?

- What happens if we “zoom in” to a point on the graph of \(y=x^2\)?

In this activity, we are going to zoom in to different points on the graph of \(y=x^2\) to explore what happens when we do so.

This activity is best done in groups of three or four to share the workload. You will need graph paper.

There are four graph-drawing tasks, A, B, C and D. If you have four people in your group, take one task each; if you have only three, then share tasks A, B and C between you, and only do task D if you have time.

Your teacher may give you a value for \(b\), otherwise you can choose your own value for \(b\) from the choices \(-2\), \(-1.5\), \(-1\), \(-0.5\), \(0\), \(0.5\), \(1\), \(1.5\) and \(2\). **Everyone in the group should use the same value of \(b\).** You can work on the tasks simultaneously, and then compare your results at the end.

**Task A**

Complete the table of values of the function \(y=x^2\) and use this to draw a graph of \(y=x^2\) on graph paper for values of \(x\) between \(-3\) and \(3\).

Use a scale of \(\quantity{2}{cm}\) (one big square) per unit **on each axis**.

| \(x\) | \(y=x^2\) |
|---|---|
| \(-3\) |  |
| \(-2.5\) |  |
| \(-2\) |  |
| \(-1.5\) |  |
| \(-1\) |  |
| \(-0.5\) |  |
| \(0\) |  |
| \(0.5\) |  |
| \(1\) |  |
| \(1.5\) |  |
| \(2\) |  |
| \(2.5\) |  |
| \(3\) |  |

When you have drawn the graph, draw a box on it between \(x=b–0.1\) and \(x=b+0.1\) to show where the graph for task B is.

**Task B**

Complete the table of values of the function \(y=x^2\) and use this to draw a graph of \(y=x^2\) on graph paper for values of \(x\) between \(x=b-0.1\) and \(x=b+0.1\).

Use a scale of \(\quantity{2}{cm}\) (one big square) per \(0.1\) unit **on each axis**.

| \(x\) | \(x\) | \(y=x^2\) |
|---|---|---|
| \(b-0.1\phantom{00}\) |  |  |
| \(b-0.075\) |  |  |
| \(b-0.05\phantom{0}\) |  |  |
| \(b-0.025\) |  |  |
| \(b\phantom{{}+0.000}\) |  |  |
| \(b+0.025\) |  |  |
| \(b+0.05\phantom{0}\) |  |  |
| \(b+0.075\) |  |  |
| \(b+0.1\phantom{00}\) |  |  |

When you have drawn the graph, draw a box on it between \(x=b–0.01\) and \(x=b+0.01\) to show where the graph for task C is.

**Task C**

Complete the table of values of the function \(y=x^2\) and use this to draw a graph of \(y=x^2\) on graph paper for values of \(x\) between \(x=b-0.01\) and \(x=b+0.01\).

Use a scale of \(\quantity{2}{cm}\) (one big square) per \(0.01\) unit **on each axis**.

| \(x\) | \(x\) | \(y=x^2\) |
|---|---|---|
| \(b-0.01\phantom{00}\) |  |  |
| \(b-0.0075\) |  |  |
| \(b-0.005\phantom{0}\) |  |  |
| \(b-0.0025\) |  |  |
| \(b\phantom{{}+0.0000}\) |  |  |
| \(b+0.0025\) |  |  |
| \(b+0.005\phantom{0}\) |  |  |
| \(b+0.0075\) |  |  |
| \(b+0.01\phantom{00}\) |  |  |

If there are four people in your group, then when you have drawn the graph, draw a box on it between \(x=b–0.001\) and \(x=b+0.001\) to show where the graph for task D is.

**Task D**

Complete the table of values of the function \(y=x^2\) and use this to draw a graph of \(y=x^2\) on graph paper for values of \(x\) between \(x=b-0.001\) and \(x=b+0.001\).

Use a scale of \(\quantity{2}{cm}\) (one big square) per \(0.001\) unit **on each axis**.

| \(x\) | \(x\) | \(y=x^2\) |
|---|---|---|
| \(b-0.001\phantom{00}\) |  |  |
| \(b-0.00075\) |  |  |
| \(b-0.0005\phantom{0}\) |  |  |
| \(b-0.00025\) |  |  |
| \(b\phantom{{}+0.00000}\) |  |  |
| \(b+0.00025\) |  |  |
| \(b+0.0005\phantom{0}\) |  |  |
| \(b+0.00075\) |  |  |
| \(b+0.001\phantom{00}\) |  |  |

**Questions**

- Line up the graphs, so that you can see the progression as you zoom in on the point where \(x=b\). What do you notice?

- How do your graphs compare with those of other groups (who are using different values of \(b\))?

- What do you think might happen if we had started with a different curve instead of \(y=x^2\)?

## Things you might have noticed

This interactivity shows what you might have drawn. You can select the value of \(b\) and then zoom in to the graph at that point.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/R89wFrDq/width/429/height/518/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/R89wFrDq)

You have probably noticed that the graph looks like a straight line when you zoom in far enough.

- What is the gradient of the straight line you end up with?

- Comparing your results with those of other groups or with the interactivity, how does the gradient depend on the value of \(b\) you are using?

- Does every graph look like a straight line when you zoom in far enough?

You can explore this more generally with the [interactive graph](https://undergroundmathematics.org/introducing-calculus/zooming-in/interactive-graph) we have provided.

After thinking about this problem, you might like to think about [tangents](https://undergroundmathematics.org/introducing-calculus/a-tangent-is) or how you might develop these ideas to work out gradient functions for [powers of \(x\)](https://undergroundmathematics.org/calculus-of-powers/binomials-are-the-answer).

You might also want to think about how this approach relates to the algebraic point of view explored in [Binomials are the answer](https://undergroundmathematics.org/calculus-of-powers/binomials-are-the-answer): the derivative there is found as the limit of the gradients of chords, using the algebraic expression \(\dfrac{(x+h)^2-x^2}{(x+h)-x}\).

## Interactive graph

This interactivity offers the ability to explore the effect of zooming in on the graph of a function of your choice. You can also show a second point and the chord between them by clicking “Show triangle”.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/X8qK6jS8/width/810/height/493/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/X8qK6jS8)
