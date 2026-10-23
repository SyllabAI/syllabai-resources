---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/how-high-am-i
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
  ugm_id: how-high-am-i
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 8159
  old_site_id: G3_RT12_2
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
      evidence: Ferris-wheel rider height as a cosine/sine model of the turned angle — graph use in context
      rationale: 'Canonical UGM title: “How high am I?”'
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
- path: https://undergroundmathematics.org/trigonometry-triangles-to-functions/how-high-am-i/download/teacher-notes.pdf
  kind: printable
---

# How high am I?

> Excerpt: This offers an opportunity to apply some basic trigonometry to a situation that students start by visualising. Asking students to explain why their solutions work for all angles from $0$ to $2\pi$ could help to make links with graphs of trigonometric functions and how these relate to the original situation.

## Problem

How does an angular change on a Ferris wheel affect the height of a rider above the ground level?

After looking at this resource you may like to take a look at [Proving the half-angle formulae](https://undergroundmathematics.org/trigonometry-compound-angles/proving-half-angle-formulae) and [Inspecting identities](https://undergroundmathematics.org/trigonometry-compound-angles/inspecting-identities) in which you may notice the appearance of similar expressions.

## Suggestion

Try to draw a diagram to represent the situation. You might find that two diagrams are useful, one to show the initial situation and one to show the situation after the ride has moved a little.

Keep it simple, label what you know and what you want to find.

## Solution

We need to select a starting point - an initial position for the rider. It makes sense to choose this to be at the bottom of the wheel, where the rider first gets on. Once the wheel starts moving the rider will begin to move around the circumference of a circle. After some time the rider will have moved through an angle, \(\theta\), relative to the starting position and will be a height, \(h\), above the ‘ground’ (we are assuming that at the starting position the rider has a height of \(0\)).

We can now add to our initial diagram, labelling the radius of the Ferris wheel, \(r\), and the angle through which the rider has turned, \(\theta\).

We are interested in finding the vertical height of the rider at this position. Notice that we can construct a right-angled triangle as shown in the following diagram.

Using trigonometry we can show that the length \(a\) is equal to \(r\cos \theta.\)

Then the vertical height of the rider above their starting position (the ground), \(h\), is \[r-r\cos \theta = r(1-\cos\theta).\]

It makes sense to check this result. We know that when \(\theta=0\), \(h\) should equal \(0\) and that when \(\theta=\pi\), \(h\) should equal \(2r\). Substituting \(\theta=0\) into our formula for the height gives \[h=r(1-\cos 0) = r(1 - 1) = 0,\] as required.

Similarly, substituting \(\theta=\pi\) into the formula for the height gives \[h=r(1-\cos \pi)=r(1-(-1)) = 2r.\]

We found this formula by considering the acute value of \(\theta\) in my original diagram. We have confirmed that the formula returns expected results for two specific values of \(\theta\) but it’s worth thinking a little further about why it works for all values of \(\theta\).

Consider the following two diagrams:

|  |  |
|---|---|

Can you use these diagrams to explain why the formula \(h=r(1-\cos\theta)\) also works for obtuse and reflex values of \(\theta\)?

Thinking graphically

One way of approaching this would be to consider the graphical representation of the formula that we have found.

How does each diagram relate to this graph? Does this help to explain why the formula works for all values of \(\theta\)?

Thinking algebraically

| If we had considered this diagram in the first place we may have decided that the height of the rider above the ground is given by \[h = r(1+\cos (\pi - \theta)).\] Is this formula equivalent to the original, \[h = r(1-\cos \theta)?\] |  |
|---|---|
