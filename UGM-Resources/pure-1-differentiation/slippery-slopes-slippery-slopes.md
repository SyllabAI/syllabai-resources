---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-meets-functions/slippery-slopes
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-meets-functions
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: slippery-slopes
  station: calculus-meets-functions
  station_title: Calculus meets Functions
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 8481
  old_site_id: C3_RT12_1
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
  - code: 1.7.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: gradients of f(x), f(x)-8, 3f(x), 3f(x)+8 at matched points — constant-multiple/sum
        derivative structure read graphically
      rationale: 'Canonical UGM title: "Slippery slopes"'
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
- path: https://undergroundmathematics.org/calculus-meets-functions/slippery-slopes/download/teacher-notes.pdf
  kind: printable
---

# Slippery slopes

> Excerpt: Students are presented with graphs of related (but unknown) functions and asked to determine the gradients of these graphs at certain points.

## Problem

Here are the graphs of four functions. The equations of the graphs are \[y=f(x) \quad y=f(x)-8 \quad y=3f(x) \quad \text{and} \quad y=3f(x)+8.\]

- The \(x\)-coordinates of \(A\), \(B\), \(C\) and \(D\) are all the same. What can you deduce about the gradients of the curves at \(A\), \(B\), \(C\) and \(D\)?

- The gradient of the tangent at \(D\) is \(\tfrac{1}{4}\). What are the gradients of the tangents at \(A\), \(B\) and \(C\)?

Here are the graphs of another four functions. The equations of these graphs are \[y=f(x)\quad y=f(x+20)-8 \quad y=3f(x-25) \quad \text{and} \quad y=-3f(x)+10.\]

- The \(x\)-coordinates of points \(E\), \(F\), \(G\) and \(H\) are \(-15\), \(5\), \(5\) and \(30\) respectively. What can you deduce about these points?

- The gradient of the tangent at \(E\) is \(-\tfrac{1}{4}.\) What are the gradients of the tangents at \(F\), \(G\) and \(H\)?

## Solution

Which graph is which?

In order to sort out which curve is which, we can consider these questions.

- Which graphs could be translations of each other?

- Which graphs could be stretches of each other parallel to the \(y\)-axis?

- What do the slopes of the tangents at \(A\), \(B\), \(C\) and \(D\) tell us?

By answering these questions we can deduce that the graphs through \(A\) and \(B\) must be \(y=3f(x)+8\) and \(y=3f(x)\) respectively and the graphs through \(C\) and \(D\) must be \(y=f(x)\) and \(y=f(x)-8\) respectively.

Gradients of tangents

Since the graphs through \(C\) and \(D\) are translations of each other parallel to the \(y\)-axis, and \(C\) and \(D\) have the same \(x\)-coordinate, the tangent at \(C\) is parallel to the tangent at \(D.\) Therefore the gradient of the tangent at \(C\) is \(\tfrac{1}{4}.\)

We know the equations of the graphs, so we know that the values of the functions whose graphs pass through \(A\) and \(B\) are changing three times as rapidly as the values of the functions whose graphs pass through \(C\) and \(D.\) Therefore the gradient of the tangents at \(A\) and \(B\) is \(\tfrac{3}{4}\).

Here are the graphs of another four functions. The equations of these graphs are \[y=f(x)\quad y=f(x+20)-8 \quad y=3f(x-25) \quad \text{and} \quad y=-3f(x)+10.\]

- The \(x\)-coordinates of points \(E\), \(F\), \(G\) and \(H\) are \(-15\), \(5\), \(5\) and \(30\) respectively. What can we say about these points?

- The gradient of the tangent at \(E\) is \(-\tfrac{1}{4}.\) What are the gradients of the tangents at \(F\), \(G\) and \(H\)?

The transformations of these curves look a bit more complicated than those in the first set of functions, but we can use similar ideas to work out which curve is which and find the coordinates of points \(E\), \(F\), \(G\) and \(H\).

Which graph is which?

From the equations we can see that \(y=f(x)\) and \(y=f(x+20)-8\) are translations of each other, so these must be the graphs through points \(E\) and \(G.\) As \(y=f(x+20)-8\) is a translation of \(y=f(x)\) in the negative \(x\) and \(y\) directions, \(y=f(x+20)-8\) must be the graph through \(E.\)

Of the remaining equations, only \(y=-3f(x)+10\) involves a reflection of \(y=f(x)\) in the \(x\)-axis. To use this information, let’s consider the behaviour of the functions shown as \(x\) increases:

- the functions shown by the graphs through \(G\) and \(H\) increase, then decrease, then increase again

- the function shown by the graph through \(F\) decreases, then increases, then decreases again.

Therefore the equation of the graph through \(H\) is \(y=3f(x-25)\) and the equation of the graph through \(F\) is \(y=-3f(x)+10.\)

We can also see that the local maximum of the graph through \(H\) is higher than (and occurs to the right of) the local maximum of the graph through \(G.\) This gives us a different way to see that the equation of the graph though \(H\) is \(y=3f(x-25).\)

Relationship between points

We now know that \(G\) lies on \(y=f(x)\) and has coordinates \((5,0).\) Since the \(x\)-coordinate of \(E\) is \(20\) less than the \(x\)-coordinate of \(G\), and the graph through \(E\) is a translation of the graph through \(G\) by \(-20\) parallel to the \(x\)-axis, we know that \(E\) and \(G\) are corresponding points on the two graphs. Therefore the coordinates of \(E\) are \((-15,-8).\)

Thinking about the transformations of \(y=f(x)\) that produce the other graphs, we can see that \(F\) and \(H\) are both points corresponding to \(G\) under these transformations. Therefore the coordinates of \(F\) are \((5,10)\) and the coordinates of \(H\) are \((30,0).\)

Gradients of tangents

Since we know that \(G\) and \(E\) are corresponding points on translations of graphs, the tangent at \(G\) must be parallel to the tangent at \(E\), i.e. the gradient of the tangent at \(G\) is \(-\tfrac{1}{4}.\)

The graph through \(H\) is obtained from the graph through \(G\) by a translation parallel to the \(x\)-axis, followed by a stretch of scale factor \(3\) parallel to the \(y\)-axis. The translation doesn’t affect the gradient of the tangent, but the stretch means that the rate of change of the transformed function is three times the rate of change of the original function. Therefore the gradient of the tangent at \(H\) is \(-\tfrac{3}{4}.\)

Finally, to transform the graph through \(G\) into the graph through \(F\), we can reflect in the \(x\)-axis, stretch by scale factor \(3\) parallel to the \(y\)-axis, and then translate. The reflection and stretch mean that the rate of change of the transformed function is three times the rate of change of the original function, but this change is in the opposite direction, i.e. the transformed function decreases where the original function increases and vice versa. Therefore the gradient of the tangent at \(F\) is \(\tfrac{3}{4}.\)

We have used the idea that when a graph is translated, the tangents at corresponding points have the same gradient. It is important to note that this is not the same as saying that translations do not affect gradient functions.

Can you think of an example where the translation doesn’t affect the gradient function, and an example where it does?
