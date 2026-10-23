---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/can-you-find-trigonometry-edition
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/many-ways-problem
- level/developing
resource_identity:
  ugm_id: can-you-find-trigonometry-edition
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 4
  resource_type_label: Many ways problem
  level: Developing
  ref: 5463
  old_site_id: G3_RT6_3
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
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: find sine/cosine/tangent graphs under constraints — stretches, reflections, translations
        of y=sin x and the behaviour that follows
      rationale: 'Canonical UGM title: “Can you find... trigonometry edition”'
      validation_status: SUGGESTED
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-5
assets:
- path: https://undergroundmathematics.org/trigonometry-triangles-to-functions/can-you-find-trigonometry-edition/download/teacher-notes.pdf
  kind: printable
---

# Can you find... trigonometry edition

> Excerpt: Students are asked to suggest graphs of trigonometric functions which satisfy certain conditions. In the first part of the problem students are asked to suggest one graph, while in the second they are asked to suggest two or three graphs which simultaneously satisfy a set of conditions.

## One graph

Think of the types of graphs you can obtain by a combination of stretches, reflections and translations of the graph \(y=\sin x\). In this resource we refer to any of these graphs as a “sine graph”.

Can you find …

1. … a sine graph which touches the lines \(y=3\) and \(y=1?\)

---

1. … a cosine graph which crosses the \(x\)-axis at \(x=1\) and \(x=-1\)?

---

1. … a tangent graph which passes through the point \(\big(\dfrac{\pi}{3},0\big)\) and for which the line \(x=\dfrac{\pi}{2}\) is an asymptote?

You can use [Desmos](https://www.desmos.com/calculator) to help you find suitable graphs, but try to sketch some graphs first.

Could you include extra conditions in parts (a), (b) or (c) so that the graphs are unique?

## More than one graph

Can you find …

1. … two sine graphs which only cross each other on the \(x\)-axis?

---

1. … a sine graph, a cosine graph and a tangent graph which all meet at certain points? What if all three graphs have to meet at the origin?

---

1. … a sine graph and a cosine graph which don’t cross each other? What if the graphs have to lie between \(y=1\) and \(y=-1\)?

---

1. … a cosine graph and a tangent graph which meet the \(x\)-axis the same number of times between \(x=-4\) and \(x=4\)? What if these points have to be the same for both graphs?

Note that by “a sine graph” we mean any curve which is obtained by some combination of stretches, reflections and translations of the graph \(y=\sin x\).

You can use [Desmos](https://www.desmos.com/calculator) to help you find suitable graphs, but try to sketch some graphs first.

## Things you might have tried

Please note that we have used radians in this discussion, but we could have used degrees. The thinking and the ideas will be the same in both cases, so do try to read this even if you have used degrees.

Can you find …

1. … two sine graphs which only cross each other on the \(x\)-axis?

Given that \(y=\sin x\) crosses the \(x\)-axis, what are the simplest transformations you could apply to it to obtain another sine graph which crosses the \(x\)-axis at the same points?

One option would be to reflect \(y=\sin x\) in the \(x\)-axis to give you the two sine graphs. Another would be to stretch it parallel to the \(y\)-axis.

1. … a sine graph, a cosine graph and a tangent graph which all meet at certain points? What if all three graphs have to meet at the origin?

One approach could be to look at where two of \(y=\sin x\), \(y=\cos x\) and \(y=\tan x\) meet and then transform the third graph so that it also passes through these points.

For example, we could note that \(y=\sin x\) and \(y=\cos x\) meet at \(\big(\tfrac{\pi}{4}, \tfrac{\sqrt{2}}{2}\big)\), but \(\tan \tfrac{\pi}{4} = 1\), so we could rescale \(y=\tan x\) to give our third graph.

If we wanted to make sure all the graphs met at the origin, we could note that \(y=\sin x\) and \(y=\tan x\) meet at integer multiples of \(\pi\), so both pass through the origin. As \(y=\cos x\) passes through \((0,1)\) we could translate this graph to ensure that it also passes through the origin. We could think of using \(y= \cos ( x \pm \tfrac{\pi}{2})\), but what would the graphs look like in each case?

1. … a sine graph and a cosine graph which don’t cross each other? What if the graphs have to lie between \(y=1\) and \(y=-1\)?

Here we should think about what “don’t cross each other” means. If we consider \(y=\cos x\) and \(y=\sin \left(x+ \tfrac{\pi}{2}\right)\), or \(y=\sin x\) and \(y=2-\sin x\) then the pairs of graphs don’t cross, but there are plenty of points in common. We will try to find graphs without any points in common. If we can’t manage to find graphs that will work, then we could allow the graphs to meet but not cross.

The graphs of \(y=\sin x\) and \(y=\cos x\) both take values between \(-1\) and \(1\). One option would be to slide one or both of the graphs parallel to the \(y\)-axis so that their values don’t overlap at all.

To solve the second part of the problem we could rescale the graphs so that they could be moved apart and still fit between the lines \(y=1\) and \(y=-1\). We could also combine this with translations parallel to the \(x\)- or \(y\)-axes so that the ranges of the functions overlap, but the graphs don’t actually cross. Here is one possible solution to illustrate this.

The graph of \(y=\tan x\) crosses the \(x\)-axis three times between \(x=-4\) and \(x=4\), whereas \(y=\cos x\) crosses the \(x\)-axis only twice in this interval. One option would be to translate the graph of \(y=\cos x\) so that it crosses the \(x\)-axis three times instead of two. Given that \(y=\sin x\) crosses the \(x\)-axis at the same points as \(y=\tan x\) and \(\sin x =\cos (x-\tfrac{\pi}{2})\), we could use \(y=\sin x\) and \(y=\tan x\) as our two graphs. A further option would be to increase the [frequency](https://undergroundmathematics.org/glossary/frequency) of the cosine wave and then slide the graph down so that it just touches the \(x\)-axis.This could also give a cosine graph which meets the \(x\)-axis at the same points as the graph of \(y=\tan x\).
