---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/r9586
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/review-question
resource_identity:
  ugm_id: r9586
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9586
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
  exam_reference: UCLES O level Additional Mathematics 2, 1977, Q17
task: T-UGM-IMPORT-7
---

# What is the acceleration of this particle?

## Question

A body is travelling along a straight line with constant acceleration \(\quantity{a}{m\,s^{-2}}\). The body passes a fixed point \(O\) on the line with velocity \(\quantity{u}{m\,s^{-1}}\). Between \(\quantity{4}{s}\) and \(\quantity{5}{s}\) after passing \(O\) the body travels \(\quantity{10}{m}\). Between \(\quantity{6}{s}\) and \(\quantity{7}{s}\) after passing \(O\) the body travels \(\quantity{12}{m}\).

Calculate the values of \(u\) and \(a\).

## Solution

We are given distances at various times so the most useful equation of motion is going to be \[s=ut+\frac{1}{2}at^2.\]

We can use the equation to find the displacements at \(\quantity{5}{s}\) and \(\quantity{4}{s}\). \[s_5=5u+\frac{25}{2}a\] \[s_4=4u+\frac{16}{2}a\] Subtracting gives us the distance travelled in this period which we are told is \(10\). We can do the same for the period \(\quantity{6}{s}\) to \(\quantity{7}{s}\). \[10=u+\frac{25-16}{2}a=u+4.5a\] \[12=u+\frac{49-36}{2}a=u+6.5a\] We now can subtract these equations and solve for \(a\), \[-2=-2a\] \[a=1\] and substitute this value into one of the above equations to find \(u\). \[10=u+4.5\] \[u=5.5\]

Alternatively, we could use a graphical approach to visually achieve the same solution. If we draw a velocity-time graph, the area underneath is the distance travelled.

From the information we are given, the difference between the two shaded areas is \(\quantity{2}{m}\). In the period of time between \(\quantity{4}{s}\) and \(\quantity{6}{s}\) the velocity increases by \(2a\). So the difference between the shaded areas is a rectangle of base \(1\) and height \(2a\). Since we know this difference is \(2\) we have \[2a\times1=2\] \[a=1\]

Can you also deduce the value of \(u\) from this diagram?
