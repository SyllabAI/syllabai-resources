---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/big-trig
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: big-trig
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 5795
  old_site_id: G5_RT12_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: trigonometry-triangles-to-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: trigonometry-triangles-to-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: 'compare sin(cos x) and cos(sin x): range and behaviour reasoning over sine and cosine
        for angles of any size'
      rationale: 'Canonical UGM title: “Big trig”; exam provenance: Based on this'
      validation_status: SUGGESTED
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Based on this
task: T-UGM-IMPORT-5
assets:
- path: https://undergroundmathematics.org/trigonometry-triangles-to-functions/big-trig/download/teacher-notes.pdf
  kind: printable
---

# Big trig

> Excerpt: This provides an opportunity for students to consider how the sine and cosine functions behave in a "which is bigger?" context. Working on this problem could help to reinforce students' understanding of the behaviour of trigonometric functions and the problem can be attempted in a variety of different ways.

## Problem

Which is larger: \(\sin(\cos x)\) or \(\cos(\sin x)\)?

Does it depend on \(x\)?

## Suggestion

- What are the minimum and maximum values of \(\sin x\) and \(\cos x\)?

- Where are \(\sin x\) and \(\cos x\) positive or negative?

- Where are \(\sin x\) and \(\cos x\) increasing or decreasing?

## Things you might consider

Let’s start by thinking about what we know about the behaviour of \(\sin x\) and \(\cos x.\)

- Both \(\sin x\) and \(\cos x\) have period \(2\pi\) so \(\sin(\cos x)\) and \(\cos(\sin x)\) will be periodic. The period of each function can’t be more than \(2\pi\) so we only need to consider what happens for \(x\) in the [interval](https://undergroundmathematics.org/glossary/interval-notation) \([0,2\pi].\)

- \(\sin x\) and \(\cos x\) vary between \(-1\) and \(1.\) What does this tell us about the minimum and maximum values of \(\sin(\cos x)\) and \(\cos(\sin x)\)?

- For \(x\) in \(\big[0,\tfrac{\pi}{2}\big]\) and \(\big[\tfrac{3\pi}{2},2\pi\big]\) \(\sin x\) increases and for \(x\) in \(\big[\tfrac{\pi}{2},\tfrac{3\pi}{2}\big]\) it decreases. Where does \(\cos x\) decrease or increase between \(0\) and \(2\pi\)?

- We know that \(\cos x\) is an even function and \(\sin x\) is an odd function, i.e. \(\cos (-x) = \cos x\) and \(\sin(-x)=-\sin x.\)

**Special points**

We’ll consider some multiples of \(\tfrac{\pi}{2}\) to get a sense of how the two functions behave. You may find it helpful to start marking some points on a sketch graph as you read.

- When \(x=0, \pi, 2\pi\) the value of \(\cos(\sin x)\) is \(1\), which must be the maximum value of the function. This means the period of \(\cos(\sin x)\) could be \(\pi.\)

- \(\sin(\cos 2\pi)=\sin(\cos 0) = \sin 1.\) The value \(\sin 1\) must be positive, but as \(\sin x\) does not reach \(1\) until \(x=\tfrac{\pi}{2}\), \(\sin(\cos 0) <1.\) Similarly \(\sin (\cos \pi)=\sin (-1) = -\sin 1 >-1.\)

- \(\sin \tfrac{\pi}{2}=1\), so \(\cos (\sin \tfrac{\pi}{2})=\cos 1\), which is positive, but less than \(1.\) Also, \(\cos (\sin \tfrac{3\pi}{2})=\cos 1\) because of the period of \(\cos (\sin x).\)

- \(\cos x=0\) when \(x=\tfrac{\pi}{2}\) and \(x=\tfrac{3\pi}{2}\) so \(\sin(\cos x)=0\) at these points.

This means that \(\cos(\sin x) >\sin(\cos x)\) at \(0,\tfrac{\pi}{2},\pi,\tfrac{3\pi}{2}\) and \(2\pi.\) The values of \(\cos 1\) and \(\sin 1\) seem to be important. Without using a calculator or graphing software, how could you decide which of these values is bigger?

**Behaviour between special points**

Positive and negative

As \(\cos x\) is negative between \(\tfrac{\pi}{2}\) and \(\tfrac{3\pi}{2}\) and \(\sin x\) is negative for \(x\) between \(-1\) and \(0\) the value of the function \(\sin (\cos x)\) must be negative for \(x\) between \(\tfrac{\pi}{2}\) and \(\tfrac{3\pi}{2}.\)

What does the same reasoning tell us about \(\cos(\sin x)\)?

Symmetry

As

\(\cos x\)

is an even function and

\(\sin x\)

is odd,

\(\cos (\sin (-x))=\cos (-\sin x)=\cos (\sin x)\)

and

\(\sin (\cos (-x))=\sin (\cos x)\)

, so both functions are even. As well as telling us that the

\(y\)

-axis is a line of symmetry of the graphs of

\(y=\sin (\cos x)\)

and

\(y=\cos (\sin x)\)

, this also shows that these graphs are symmetric about the line

\(x=\pi.\)

(For example,

\(\sin (\cos (\pi-x))=\sin (\cos (x-\pi)).\)

) This helps because we are interested in what happens between

\(0\)

and

\(2\pi.\)

Increasing and decreasing behaviour

For \(x\) between \(0\) and \(\tfrac{\pi}{2}\), \(\sin x\) increases from \(0\) to \(1\) and \(\cos x\) decreases, so \(\cos(\sin x)\) decreases from \(1\) to \(\cos 1\). On \(\big[\tfrac{\pi}{2},\pi\big]\), \(\sin x\) decreases from \(1\) to \(0\) and \(\cos x\) decreases from \(0\) to \(-1\). This means that \(\cos(\sin x)\) *increases* from \(\cos 1\) to \(1\) and therefore has a minimum when \(x=\tfrac{\pi}{2}.\) What happens between \(\pi\) and \(2\pi\)?

These ideas, can be used to show that \(\cos(\sin x)\) has a period of \(\pi\) and its range is \([\cos 1,1]\) whereas \(\sin(\cos x)\) has period \(2\pi\) and its range is \([-\sin 1, \sin 1].\)

For all the points considered, \(\cos(\sin x) >\sin(\cos x)\) and we now know a lot about the graphs \(y=\cos (\sin x)\) and \(y=\sin (\cos x).\) It seems reasonable to conjecture that \(\cos(\sin x) >\sin(\cos x)\) for all \(x\), but to convince ourselves that this is true, we need to show that the graphs do not cross anywhere.

Do the graphs of \(y=\cos(\sin x)\) and \(y=\sin(\cos x)\) ever cross?

The graphs can’t cross between \(\tfrac{\pi}{2}\) and \(\tfrac{3\pi}{2}\) because \(\sin(\cos x)\) is negative here, but what about between \(0\) and \(\tfrac{\pi}{2}\) or between \(\tfrac{3\pi}{2}\) and \(2\pi\)?

We want to know whether \[\cos (\sin x) = \sin (\cos x)\] has any solutions for \(x\) in \(\left[0, \tfrac{\pi}{2}\right].\) Now, if \(\cos a = \sin b\) then \(a=\tfrac{\pi}{2}-b\), so \(a+b=\tfrac{\pi}{2}\), or in our case \(\sin x+ \cos x = \tfrac{\pi}{2}.\)

The diagram shows part of a circle of radius \(1\) and an angle \(x\) between \(0\) and \(\tfrac{\pi}{2}.\) The length of arc \(APB\) is \(\tfrac{\pi}{2},\) but \(\sin x\) is smaller than the length of arc \(AP\) and \(\cos x\) is smaller than the length of arc \(PB.\)

Therefore \[\sin x + \cos x < \tfrac{\pi}{2}\] so \(\cos (\sin x) = \sin (\cos x)\) does not have any solutions in \([0, \tfrac{\pi}{2}]\). The symmetry of the graphs about \(x=\pi\), means that there aren’t any solutions in \([\tfrac{3\pi}{2},2\pi]\) either. Therefore \(\cos (\sin x)\) is larger than \(\sin (\cos x)\) for all real \(x.\)

Another approach is to use the inequality \(\sin \theta < \theta\) for positive \(\theta.\) To see how this inequality arises, consider the diagram below. This shows the chord \(AB\) of a circle subtending an angle \(\theta\) at the centre of the circle, where \(0<\theta < \pi.\)

If we compare the areas of the triangle \(OAB\) and the minor sector \(OAB,\) we get \(\tfrac{1}{2}r^2 \sin \theta < \tfrac{1}{2}r^2 \theta\) and therefore \(\sin \theta < \theta\).

We can combine this inequality with the increasing and decreasing behaviour of \(\sin x\) and \(\cos x\) on \(\big[ 0, \tfrac{\pi}{2}\big]\) to show that \[\sin (\cos x) < \cos x \quad \text{and} \quad \cos (\sin x) > \cos x\]

Therefore \(\cos x\) is always sandwiched between \(\sin (\cos x)\) and \(\cos (\sin x)\) for \(x\) between \(0\) and \(\tfrac{\pi}{2}.\) As above, the symmetry of the graphs completes the proof that \(\cos (\sin x)\) is larger than \(\sin (\cos x)\) for all real \(x.\)

Graph
