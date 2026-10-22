---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r5754
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r5754
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5754
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
  exam_reference: UCLES 1979 Q6
task: T-UGM-IMPORT-3
---

# What is the locus of these points fixed to a rod?

## Question

The ends \(A\) and \(B\) of a rod of fixed length move on the positive \(x\) and \(y\) axes respectively. \(C\) is a point on \(AB\), and \(CD\) is perpendicular to \(AB\), as shown in the figure. The lengths of \(AC\), \(BC\) and \(CD\) are \(a\), \(b\) and \(c\) respectively.

1. Find parametric equations for the locus of \(C\).

---

1. Find parametric equations for the locus of \(D\).

---

1. If \(c^2=ab\) show that the locus of \(D\) consists of part of a straight line and find the coordinates of the extremities of this locus.

---

1. Sketch the loci of \(C\) and \(D\) for the case \(a=4\), \(b=9\), \(c=6\).

## Solution

In the question the rod is moving attached to the axes, so one aspect which changes is the angle that it makes with the horizontal (angle \(OAC\)). We can then annotate our original diagram to help in writing our parametric equations.

Let \(\alpha\) be the acute angle the rod makes with the \(x\)-axis. We can mark in other angles \(\alpha\) on our diagram as shown.

It is possible to use a different variable as the parameter, for instance the \(x\)-coordinate of \(C\). The final result would be the same.

Now using triangle

\(CYB\)

and

\(CAX\)

we can write the parametric equations for

\(C\)

.

\[\begin{align*} x &= b \cos \alpha \\ y &= a \sin \alpha \\ \end{align*}\]

To get the equations for

\(D\)

we need to add sides from triangle

\(CED\)

.

\[\begin{align} x &= b \cos \alpha+ c \sin \alpha \label{eq:1}\\ y &= a \sin \alpha+ c \cos \alpha \label{eq:2} \end{align}\]

We are told to consider when \(c^2=ab\). Using the parametric equations for \(D\) with this information we can find a relationship between \(x\) and \(y\). Multiplying \(\eqref{eq:1}\) by \(a\) and \(\eqref{eq:2}\) by \(b\) we can create equations with a matching term so that subtraction eliminates them. \[ax-cy=ab\cos \alpha - c^2 \cos \alpha\] Since we know that \(c^2=ab\) this reduces to \(ax-cy=0\) which is a straight line through the origin with gradient \(\frac {a}{c}\).

If you used other ways of eliminating \(\alpha\) from these equations you may have got \(y=\frac{c}{b}x\) or \(y=\sqrt{\frac{a}{b}}x\) or \(y=\left ( \frac{c-a}{b-c} \right )x\). Can you show that these are all equivalent?

The extremities of the locus will be when

\(\alpha\)

is either

\(0\)

(the rod is lying flat) or

\(90 ^\circ\)

(the rod is vertical) these are the points

\((b,c)\)

and

\((c,a)\)

respectively.

The parametric equations for the locus of \(C\) tell us this is (one quarter of) an ellipse with semi-minor axis \(a\) and semi-major axis \(b\). (If we don’t recognise this we can rearrange for \(\sin \alpha\) and \(\cos \alpha\) and use the Pythagorean identity to eliminate \(\alpha\).)

We can now sketch these two loci:
