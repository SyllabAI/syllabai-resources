---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/geometry-of-equations/between-the-lines
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- geometry-of-equations
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: between-the-lines
  station: geometry-of-equations
  station_title: Geometry of Equations
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 7172
  old_site_id: G2_RT12_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: geometry-of-equations
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: geometry-of-equations
    validation_status: SUGGESTED
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'Area between two lines given the area of one; linear-function graph reading (gradients/intercepts) is the 1.3.2 vocabulary.'
      rationale: 'Canonical UGM title: “Between the lines”'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-3
assets:
- path: https://undergroundmathematics.org/geometry-of-equations/between-the-lines/download/teacher-notes.pdf
  kind: printable
---

# Between the lines

> Excerpt: Find the area of a region between two straight lines given minimal information. This task involves the geometry and equations of straight lines.

## Warm-up

What can you say about this diagram?

Are there any questions that you would ask about the diagram?

## Problem

In the diagram below \(f(x)\) is a linear function.

The area of the green shaded region (above the \(x\)-axis) is \(12\) square units.

What is the area of the blue shaded region (below the \(x\)-axis)?

## Suggestion

Take a step back, look at the image and write down anything that you know about it (without doing any calculations).

Some things you might have written

- \(f(x)\) passes through the origin.

- \(f(x)\) is a straight line.

- \(f(x)\) could be written in the form \(ax + b\) (where \(b=0\) in this case).

- \(y=f(x)-k\) is parallel to \(y=f(x)\) (it is a vertical translation by \(k\) units downwards).

- The green region is a trapezium of ‘height’ \(6\) units.

- The blue region is a triangle of ‘base’ or ‘height’ \(6\) units.

- The combination of the green and blue shaded regions produces a parallelogram.

- The blue triangle could sit ‘on top of’ the green trapezium to create a rectangle.

- The area of the blue triangle must be less than \(12\) square units.

## Solution

There’s more than one way in which we could calculate the area of the blue triangle. For most methods that we might consider we will need to identify the value of \(y\) when \(x=2\) (let’s call this \(y_1\)) and when \(x=8\) (let’s call this \(y_2\)).

How do we know that identifying these two values, \(y_{1}\) and \(y_{2}\), is a good strategy and will provide enough information to solve the problem?

In order to identify these two values we might begin by writing down an equation involving them. This could be the area of the green trapezium which can be written as \[12 = \frac{1}{2}(y_{1} + y_{2}) \times 6.\]

Rearranging this we find that

\[\begin{equation} \label{eq:1} y_{1}+y_{2} = 4. \end{equation}\]

In order to identify the unique values of \(y_1\) and \(y_2\) we now need a second equation containing these two unknowns.

We know that

\(f(x) = ax\)

where

\(a\)

is the gradient of the line. Because this is a straight line, the gradient,

\(a\)

, will be the same when

\(x=2\)

and when

\(x=8\)

and therefore we can write

\[a=\frac{y_{1}}{2} = \frac{y_{2}}{8},\]

which can be rearranged to give

\[\begin{equation} \label{eq:2} 4y_{1} = y_{2}. \end{equation}\]

Notice that we could have obtained this second equation by considering similar triangles instead.

The purple and yellow triangles are similar and related by a linear scale factor of \(4\). Therefore \(y_{2} = 4y_{1}\).

Solving equations \(\eqref{eq:1}\) and \(\eqref{eq:2}\) simultaneously we find that \(y_{1} = \dfrac{4}{5}\) and \(y_{2} = \dfrac{16}{5}\).

Now, the area of the blue triangle can be calculated directly if we first calculate the perpendicular height of the blue triangle as \(y_2 - y_1 = \dfrac{16}{5} - \dfrac{4}{5} = \dfrac{12}{5}\). Then we can calculate the area of the blue triangle as \[\frac{1}{2} \times 6 \times \frac{12}{5} = \frac{36}{5} \textrm{ square units}.\]

Notice that the area of the blue triangle is less than \(12\) square units. Is this what you expected?

It is also worth noting that, whilst we didn’t need it in order to solve the problem, we now know that \[y = f(x) = \dfrac{2}{5} x\] and that the translated line has equation \[y = f(x) - k = \frac{2}{5}x - \frac{16}{5},\] which can also be written as \[y = \dfrac{2}{5}(x - 8).\]

**An alternative approach**

We can also solve the problem without working out the values of \(y_1\) and \(y_2\) explicitly.

Since the lines are a distance of \(k\) apart, we have \(y_2=k\). By similar triangles, as above, \(y_1=\frac14 y_2=\frac14 k\).

Therefore the green trapezium, which has ‘height’ \(6\) and parallel sides of \(k\) and \(\frac14 k\), has area \[\frac12\times 6(k+\tfrac14k)=3\times \frac54 k.\]

The blue triangle also has ‘height’ \(6\) but its base is \(k-y_1=\frac34 k\). Therefore its area is \[\frac12\times 6\times \tfrac34k=3\times \frac34 k.\]

Therefore the ratio of the green area to the blue area is \(5\) to \(3\), and so the blue area is \[\frac35\times 12=\frac{36}{5}.\]

**Reflection**

- At first sight, it may not have looked as though there was enough information to solve the problem. Why was it possible?

- How can you generalise the problem?
