---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/r5777
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/review-question
resource_identity:
  ugm_id: r5777
  station: circles
  station_title: Circles
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5777
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
  spec_points:
  - code: 1.3.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-3 cross-map (cross-map-coordinate-geometry.json (P3c lane 3) @
        syllabai-experimental cb947595)
      evidence: 'centre and radius of the inscribed circle — the equation-of-circle form is 1.3.2; the incentre construction rides triangle-centre geometry (recorded medium).'
      rationale: 'Canonical UGM title: “Can we find the equation of the inscribed circle of the triangle $ABC$?”; exam provenance: UCLES 1985 Q13'
      validation_status: SUGGESTED
    title: interpret and use any of the forms y = mx + c , y – y = m ( x – x ) , ax + by + c = 0 in solving
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1985 Q13
task: T-UGM-IMPORT-3
---

# Can we find the equation of the inscribed circle of the triangle $ABC$?

## Question

> (this panel carries no extractable text — image/interactive content; not part of the text import).

## Suggestion

We will certainly need some clear and accurate diagrams with everything we know marked in.

Do we have any information as to where the circumcentre will lie? The incentre?

Can we find the coordinates of any key points? The lengths of any key sides?

## Solution

By symmetry, we can see that the equation of the line is \(y = x\).

Find, by an algebraic method,

1. the equation of the circle through the points \(A, B\) and \(C\)…

We are asked for the equation of the circumcircle (the circle that passes through each of the triangle’s vertices) of the triangle, which always exists.

Again by the symmetry of the triangle, the circumcentre (the centre of the circumcircle) must lie on \(y = x\), let’s say at \((m, m)\).

The circumcentre must be the same distance from \(A\) as from \(B\), so

\[(7-m)^2+(7-m)^2 = (6-m)^2 + (0-m)^2 \implies -28m +98= 36 -12m \implies m = \dfrac{31}{8}.\]

So the equation we seek is \(\left(x-\dfrac{31}{8}\right)^2+\left(y-\dfrac{31}{8}\right)^2 = r^2.\)

Putting \((0,6)\) into this equation gives \(r^2 = \dfrac{625}{32}\), and so finally we have our equation;

\[\left(x-\dfrac{31}{8}\right)^2+\left(y-\dfrac{31}{8}\right)^2 = \dfrac{625}{32}.\]

The question doesn’t specify the form in which to leave the equation, so we can leave it with brackets.

If we wish to remove the fractions, we reach \((8x-31)^2+(8y-31)^2=1250\).

Again by the symmetry of the triangle, the centre of the inscribed circle must lie on \(y = x\), let’s say at \((n, n)\).

It’s easy to calculate the various lengths on the diagram. We know \(D\) is \((3, 3)\), and so \(OD = DC= CE\) is \(3\sqrt{2}\) (by symmetry). But we know \(AC\) is \(5\sqrt{2}\), and so \(CA\) is \(2\sqrt{2}\).

We have from the diagram that \(p^2 = (3\sqrt{2})^2 + s^2\), while \(q^2 = (2\sqrt{2})^2 +s^2\).

Subtracting these equations gives us that \(10 = p^2-q^2 = (n-6)^2+(n-0)^2-(7-n)^2-(7-n)^2\).

Multiplying out and solving for \(n\) here gives us that \(n = \dfrac{9}{2}\).

So the equation of the inscribed circle is \(\left(x-\dfrac{9}{2}\right)^2+\left(y-\dfrac{9}{2}\right)^2 = s^2\).

We can see from the diagram that \(q + s = AD = 4\sqrt{2}\), and thus \(s = 4\sqrt{2} - \sqrt{\dfrac{25}{2}} = \dfrac{3}{2}\sqrt{2}\).

So finally, the inscribed circle has equation \(\left(x-\dfrac{9}{2}\right)^2+\left(y-\dfrac{9}{2}\right)^2 = \dfrac{9}{2}\).
