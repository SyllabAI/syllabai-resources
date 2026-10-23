---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r7374
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r7374
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7374
  old_site_id: Q123
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
      evidence: the graph of all points with sin y = sin x — solution-set structure as a picture
      rationale: 'Canonical UGM title: “Which points in the $x$-$y$ plane satisfy $\sin y=\sin x$?”; exam
        provenance: Oxford University Mathematics Aptitude Test, 2009, Q1G'
      validation_status: SUGGESTED
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  - code: 1.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: the graph of all points with sin y = sin x — solution-set structure as a picture
      rationale: 'Canonical UGM title: “Which points in the $x$-$y$ plane satisfy $\sin y=\sin x$?”; exam
        provenance: Oxford University Mathematics Aptitude Test, 2009, Q1G'
      validation_status: SUGGESTED
    title: find all the solutions of simple trigonometrical equations lying in a specified interval (general
      forms of solution are not included).
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2009, Q1G
task: T-UGM-IMPORT-5
---

# Which points in the $x$-$y$ plane satisfy $\sin y=\sin x$?

## Question

The graph of all those points \((x, y)\) in the \(xy\)-plane which satisfy the equation \(\sin(y) = \sin(x)\) is drawn in

|  |  |
|---|---|
|  |  |

## Solution

Firstly, we know that the equation is trivially true when \(x=y\), and so we can rule out graphs (b) and (d) as the line \(y=x\) is missing.

Secondly, we know \(y = \pi - x\) is a solution to the equation, and this line does not appear in (d), which means that by elimination, (c) is the answer.

A fuller answer might run as follows: we know that for all values of \(x\), \[\sin(x)=\sin(\pi-x)\] and \[\sin(x)=\sin(x + 2n\pi),\] where \(n\) is an integer.

Thus if \(\sin(y) = \sin(x)\) then \[y = x + 2n\pi,\] OR \[y = \pi - x + 2n\pi = -x +(2n-1)\pi.\]

So the solution is given by the lines \[\cdots, y=x-2\pi, y = x, y = x+2\pi, y = x + 4\pi, \cdots,\] together with the lines \[\cdots, y = -x-\pi, y=-x+\pi, y=-x+3\pi, \cdots.\]

These are the lines shown in (c).
