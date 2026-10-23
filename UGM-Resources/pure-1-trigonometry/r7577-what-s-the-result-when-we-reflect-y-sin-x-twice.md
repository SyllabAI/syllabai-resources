---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r7577
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r7577
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7577
  old_site_id: Q226
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
      evidence: reflect y = sin x in x = π then in y = 2 — the result is y = cos x; transformations of
        trig graphs
      rationale: 'Canonical UGM title: “What''s the result when we reflect $y=\sin x$ twice?”; exam provenance:
        Oxford University Mathematics Aptitude Test, 2013, Q1B'
      validation_status: SUGGESTED
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, 2013, Q1B
task: T-UGM-IMPORT-5
---

# What's the result when we reflect $y=\sin x$ twice?

## Question

The graph of \(y=\sin x\) is reflected first in the line \(x= \pi\) and then in the line \(y=2\). The resulting graph has equation

1. \(y=\cos x\);

---

1. \(y=2+\sin x\);

---

1. \(y=4+\sin x\);

---

1. \(y=2-\cos x\).

## Suggestion

Have you drawn a sketch?

## Solution

**Approach 1: Sketching graphs**

Here is a sketch of \(y=\sin x\), with \(x=\pi\) shown.

This is what the reflection looks like, with \(y=2\) marked.

This is what the graph looks like once it has been reflected the second time.

It passes through \(4\) on the \(y\)-axis and is clearly a vertical translation of \(y=\sin x\), so the answer must be (c).

Another way to look at it…

Suppose we have two reflections whose mirror lines are not parallel.

If we do one followed by the other, this is equivalent to a rotation about the point where the mirror lines meet.

*You could pick some reflections and convince yourself of this.*

So here our two reflections are equivalent to a rotation through \(180^\circ\) around \((\pi, 2)\), which takes \(y = \sin x\) to \(y = \sin x + 4\). The answer is (c).

**Approach 2: Algebraic transformations**

If we reflect \(y = f(x)\) in \(x = a\), we get the curve \(y = f(-x+2a)\).

If we reflect \(y = f(x)\) in \(y = a\), we get the curve \(y = -f(x)+2a\).

When reflected in the line \(x=\pi\), the graph of \(y=\sin x\) becomes \[y=\sin(2\pi -x)=\sin(-x)=-\sin x.\]

When reflected in the line \(y=2\), the graph of \(y=-\sin x\) becomes \[y= 4-(-\sin x)=4+\sin x.\]

The answer is (c).
