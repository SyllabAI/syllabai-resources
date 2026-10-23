---
created: 2026-10-23T16:39:11 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/r8658
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/review-question
resource_identity:
  ugm_id: r8658
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8658
  old_site_id: Q142
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
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: Oxford University Mathematics Aptitude Test, Specimen 1, Q4
task: T-UGM-IMPORT-5
interactive:
- src: //www.geogebratube.org/material/iframe/id/BcAFHM9w/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Can we find the area of a pedal triangle?

## Question

A triangle \(ABC\) has sides \(BC\), \(CA\), and \(AB\) of lengths \(a\), \(b\) and \(c\) respectively, and angles at \(A\), \(B\) and \(C\) are \(\alpha\), \(\beta\) and \(\gamma\) where \(0 \leq \alpha ,\beta ,\gamma \leq \frac{1}{2}\pi\).

1. Show that the area of \(ABC\) equals \(\frac{1}{2}bc\sin\alpha\). Deduce the sine rule \[\frac{a}{\sin\alpha} = \frac{b}{\sin\beta} = \frac{c}{\sin\gamma}.\]

---

1. The points \(P\), \(Q\) and \(R\) are respectively the feet of the perpendiculars from \(A\) to \(BC\), \(B\) to \(CA\), and \(C\) to \(AB\) as shown. Prove that \[\text{Area of $PQR$} = (1 - \cos^2 \alpha - \cos^2 \beta - \cos^2 \gamma) \times (\text{Area of $ABC$}).\]

---

1. For what triangles \(ABC\), with angles \(\alpha\), \(\beta\), \(\gamma\) as above, does the equation \[\cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma =1\] hold?

## Suggestion

A triangle \(ABC\) has sides \(BC\), \(CA\), and \(AB\) of lengths \(a\), \(b\) and \(c\) respectively, and angles at \(A\), \(B\) and \(C\) are \(\alpha\), \(\beta\) and \(\gamma\) where \(0 \leq \alpha ,\beta ,\gamma \leq \frac{1}{2}\pi\).

…

1. The points \(P\), \(Q\) and \(R\) are respectively the feet of the perpendiculars from \(A\) to \(BC\), \(B\) to \(CA\), and \(C\) to \(AB\) as shown. Prove that \[\text{Area of $PQR$} = (1 - \cos^2 \alpha - \cos^2 \beta - \cos^2 \gamma) \times (\text{Area of $ABC$}).\]

---

1. For what triangles \(ABC\), with angles \(\alpha\), \(\beta\), \(\gamma\) as above, does the equation \[\cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma =1\] hold?

Use this applet to explore the behaviour for different triangles \(ABC\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/BcAFHM9w/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/BcAFHM9w)

The blue triangle \(PQR\) is called a “pedal triangle” because it is formed from the *feet* of perpendiculars.

Remember that in the question, the angles at \(A\), \(B\) and \(C\) cannot be obtuse.

When does the blue triangle disappear?

## Solution

A triangle \(ABC\) has sides \(BC\), \(CA\), and \(AB\) of sides \(a\), \(b\) and \(c\) respectively, and angles at \(A\), \(B\) and \(C\) are \(\alpha\), \(\beta\) and \(\gamma\) where \(0 \leq \alpha ,\beta ,\gamma \leq \frac{1}{2}\pi\).

1. Show that the area of \(ABC\) equals \(\frac{1}{2}bc\sin\alpha\).

We take \(AB\) as the base, which has length \(c\), and \(CR\) as the height, which has length \(AC \sin(\angle CAR) = b \sin\alpha\). Then the triangle has area \[\frac{1}{2} \times \text{base} \times \text{height} = \frac{1}{2}cb \sin\alpha.\]

By choosing a different side as the base of the triangle and using the same method, we see that the area is also given by \[\text{Area}(ABC) = \frac{1}{2}bc\sin\alpha = \frac{1}{2}ac\sin\beta = \frac{1}{2}ab\sin\gamma.\] If we divide through by \(\frac{1}{2}abc\), and then take the reciprocals of the equations, we get the sine rule \[\frac{a}{\sin\alpha} = \frac{b}{\sin\beta} = \frac{c}{\sin\gamma}.\]

It’s going to become very tedious writing the word “area” repeatedly in our equations. So we’ll use the notation \([ABC]\) to mean the area of triangle \(ABC\).

We have \([PQR]=[ABC]-[AQR]-[BRP]-[CPQ].\)

Consider the triangle \(AQR\). Using our formula from the first part, we have \[[AQR] = \frac{1}{2}AQ \times AR\times\sin\alpha.\] But we know \([ABC]=\dfrac{1}{2}bc\sin\alpha\), and so \[\sin \alpha = 2\dfrac{[ABC]}{bc}.\] Substituting, we get \[[AQR] = \frac{AQ \times AR}{b \times c} \times [ABC].\]

But if we look at the right-angled triangles \(RAC\) and \(BAQ\), we see that \[\cos\alpha = \dfrac{AR}{b}=\dfrac{AQ}{c},\]

and substituting gives \[[AQR] = \cos^2\alpha \times [ABC].\]

Similarly, \[[BPR] = \cos^2\beta \times [ABC],\] and \[[CQP] = \cos^2\gamma \times [ABC].\]

So finally

\[\begin{align*} {}[PQR] &{}= [ABC] - [AQR] - [BPR] - [CQP]\\ &{}= (1 - \cos^2\alpha - \cos^2\beta - \cos^2\gamma) \times [ABC]. \end{align*}\]

1. For what triangles \(ABC\), with angles \(\alpha , \beta , \gamma\) as above, does the equation \[\cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma =1\] hold?

If \(\cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma =1\), then the area of the triangle \(PQR\) is zero.

This can only happen when two of \(P\), \(Q\) and \(R\) coincide - at the right angle of the triangle.

So this equation holds only if the triangle \(ABC\) is right-angled.

In fact, it is easy to see that we have an if and only if relationship here: \(\cos^2 \alpha + \cos^2 \beta + \cos^2 \gamma =1\) if and only if the triangle \(ABC\) is right-angled.
