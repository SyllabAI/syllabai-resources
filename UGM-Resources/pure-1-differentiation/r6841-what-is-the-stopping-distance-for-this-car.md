---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/r6841
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/review-question
resource_identity:
  ugm_id: r6841
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6841
  old_site_id: null
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
  exam_reference: UCLES O level Mechanics, 1960, Q6
task: T-UGM-IMPORT-7
---

# What is the stopping distance for this car?

## Question

A car is travelling at \(\quantity{30}{mph}\) when the driver needs to make an emergency stop. It takes him \(\quantity{0.7}{seconds}\) to apply the brake and the car comes to rest with uniform retardation in a further \(\quantity{2}{seconds}\). How far has the car travelled since the emergency arose?

With the same time taken to apply the brake and the same retardation, what would have been the stopping distance if the car had originally been travelling at \(\quantity{40}{mph}\)?

[Give your answer in yards, where \(\quantity{1}{mile}=\quantity{1760}{yards}\)]

## Solution

We can calculate the distance the car has travelled by drawing a velocity-time graph and calculating the area underneath.

The vertical axis of our graph is the velocity in miles per hour which we need to convert into yards per second. We can convert miles per hour into miles per second by dividing by \(3600\) and then multiply by \(1760\) to get our answer in yards per second. \[\frac{30}{3600}\times1760 = \frac{44}{3}\] We can calculate the area of the rectangle which is the thinking distance, \[0.7\times\frac{44}{3}\approx10.3.\] The area of the triangle is the braking distance, \[\frac{1}{2}\times\frac{44}{3}\times2\approx14.7.\] We can now add our areas together to get our total stopping distance \[10.3+14.7=25.0\] Therefore, since the emergency arose, the car has travelled \(\quantity{25}{yards}\).

You could also complete this question by using the constant acceleration formulae.

We can use the same method for this situation as the only change is the initial velocity. We can work out our new velocity in yards per second as before, \[\frac{40}{3600}\times1760 = \frac{176}{9}.\] We can calculate the area of the rectangle, \[0.7\times\frac{176}{9}\approx13.7.\] Our old and new triangles both have the same gradient and are therefore similar, so we can use the lengths of the previous triangle to work out the lengths of the new triangle. We know that the scale factor between the triangles is \(\frac{4}{3}\) therefore the length of the base is now \[\frac{4}{3}\times2=\frac{8}{3}\] and the area of the triangle is \[\frac{1}{2}\times\frac{8}{3}\times\frac{176}{9}\approx26.1.\] We can now add our areas to get the total distance \[13.7+26.1=39.8.\] Therefore the stopping distance if the driver was travelling at \(\quantity{40}{mph}\) would have been \(\quantity{40}{yards}\).

Notice that this is more than \(\frac{4}{3}\) of the \(\quantity{30}{mph}\) stopping distance. Why is that?
