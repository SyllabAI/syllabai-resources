---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r6164
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r6164
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6164
  old_site_id: None
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
  exam_reference: O&C (Oxford & Cambridge SEG) 1967 Q6
task: T-UGM-IMPORT-3
---

# What's the area of this square if it sits in this sector?

## Question

\(ABCD\) is a square lying symmetrically inside a sector of a circle whose radius is \(\quantity{1}{in.}\), the angle of the sector being \(60^\circ\). \(A\) and \(B\) lie on the straight boundaries, \(C\) and \(D\) on the curved boundary. Calculate:

1. the length of the arc \(CD\),

---

1. the area \(ABCD\),

---

1. the area of the minor segment of the circle cut off by the chord \(CD\).

[Answers to (i) and (iii) may be left in terms of \(\pi\).]

## Solution

We have \(\angle OAB = \angle OBA\), and \(\angle AOB = 60^\circ\), so the triangle \(ABO\) is equilateral. Now consider the triangle \(ADO\). It is isosceles, with sides \(a, a\) and \(1\).

We have \(\angle OAD\) is \(150^\circ\), so we can say \(2a \sin 75 = 1\), and so \(a = \dfrac{1}{2 \sin 75} (\approx 0.5176...).\)

Now

\(\angle DOA = 15^\circ = \angle COB\)

, since triangles

\(DOA\)

and

\(COB\)

are isosceles. Thus

\(\angle DOC = 30^\circ\)

, and so

\[\begin{align*} \text{length of the arc $CD$} &= \frac{\angle DOC}{360^\circ} \times \text{circumference of the circle} \\ &= \frac{30^\circ}{360^\circ} \times 2\pi \\ &= \quantity{\frac{\pi}{6}}{in.} \end{align*}\]

This is simply \(a^2\), which is \(\left(\dfrac{1}{2 \sin 75}\right)^2 = \quantity{0.268(3sf)}{sq.in.}\)

We are not asked to find this exactly, but this is not hard to do. We have \(\sin 75 = \sin30\cos45+\sin45\cos30 = \dfrac{\sqrt{2}+\sqrt{6}}{4}.\)

So \(\left(\dfrac{1}{2 \sin 75}\right)^2 = \left(\dfrac{2}{\sqrt{2}+\sqrt{6}}\right)^2 = \dfrac{1}{2+\sqrt{3}} = 2-\sqrt{3} = \quantity{0.268(3sf)}{sq.in.}\)

We need the area of the sector \(DOC\), and then subtract from this the area of the triangle \(DOC\).

Thus we have \(\pi \times 1^2 \times \dfrac{30}{360} - 0.5 \times 1 \times 1 \times \sin 30 = \quantity{\dfrac{\pi}{12} - \dfrac{1}{4}}{sq.in.}\)

Can you find any other ways of doing this question?
