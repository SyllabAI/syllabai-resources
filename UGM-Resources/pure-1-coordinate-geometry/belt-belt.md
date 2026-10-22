---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/belt
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: belt
  station: circles
  station_title: Circles
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 8393
  old_site_id: G4_RT12_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: circles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: circles
    validation_status: SUGGESTED
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule 3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-3
assets:
- path: https://undergroundmathematics.org/circles/belt/download/teacher-notes.pdf
  kind: printable
---

# Belt

> Excerpt: This resource brings together a range of geometric and algebraic ideas associated with circles.

## Problem

A piece of thin wire of length \(L\) binds together two cylindrical welding rods, of radii \(R\) and \(r\), by passing all the way around them both.

Find \(L\) in terms of \(R\) and \(r\).

## Suggestion

What are the types of shape that the wire takes?

Look at

Two cylindrical welding rods with part of the wire drawn in

Can you see any way of drawing in an extra line to make a right-angled triangle with two side lengths you know? Does the angle of this triangle help you to work out what the lengths of the other parts will be?

## Solution

We can see from the picture that the wire is made up of two arcs of circles joined by two straight lines.

Let’s find the lengths of the straight lines first.

The straight part of the wire runs along two lines that are tangent to both circles. Drawing in radii of the circles that are perpendicular to this tangent line and the straight line joining the centres of the two circles, we have the following picture:

The two cylindrical welding rods with part of the wire and some other helpful lines drawn in

We have also drawn in an extra line of the same length of those we want to find, but further down, creating a triangle.

A close-up of the triangle we found

We can use this to find the length of \(x\), as well as the value of \(\theta\). Notice that the bottom triangle is a reflection of the top triangle, so that both line segments have the same length. (And we are assuming that \(R>r\).)

Using [Pythagoras’s Theorem](https://undergroundmathematics.org/glossary/pythagoras-theorem), we find that \[x=\sqrt{(R+r)^2-(R-r)^2}=\sqrt{4Rr}=2\sqrt{Rr},\] and using trigonometry we have that \[\sin\theta=\frac{R-r}{R+r},\] and so \[\theta=\sin^{-1}\left(\frac{R-r}{R+r}\right).\]

Now let’s find the lengths of the arcs.

The two cylindrical welding rods with the arced part of the wire marked

We know the angles of the arcs from our earlier drawing. The red angle (on the left) is the whole circle without two times the third (unmarked) angle in our triangle (which we know must be \(\pi/2-\theta\)), and so the red angle must be \[2\pi-2\left(\frac{\pi}{2}-\theta\right)=\pi+2\theta.\]

The blue angle (on the right) is the whole circle minus two times \(\theta\) minus two right angles, and so must be \[2\pi-2\theta-2\frac{\pi}{2}=\pi-2\theta.\]

So the length of the red (left) arc is \[\frac{\pi+2\theta}{2\pi}2\pi R=\pi R+2\theta R=\pi R +2 R \sin^{-1}\left(\frac{R-r}{R+r}\right),\] and the blue (right) arc has length \[\frac{\pi-2\theta}{2\pi}2\pi r=\pi r-2\theta r= \pi r- 2r \sin^{-1}\left(\frac{R-r}{R+r}\right).\]

So the total length of the wire is \[2\{\text{length of straight line}\}+\{\text{length of blue arc}\}+\{\text{length of red arc}\},\] which is \[4\sqrt{Rr}+\pi(R+r)+2(R-r)\sin^{-1}\left(\frac{R-r}{R+r}\right).\]
