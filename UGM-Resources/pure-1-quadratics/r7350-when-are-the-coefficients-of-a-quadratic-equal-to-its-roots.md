---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r7350
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r7350
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7350
  old_site_id: Q35
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points:
  - code: 1.1.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Coefficients equal to roots — root/condition reasoning (UKMT).
      rationale: 'Canonical UGM title: “When are the coefficients of a quadratic equal to its roots?”;
        exam provenance: UKMT 2011 Q15'
      validation_status: SUGGESTED
    title: find the discriminant of a quadratic polynomial ax + bx + c and use the discriminant ‘repeated
      root’ is included.
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UKMT 2011 Q15
task: T-UGM-IMPORT-1
interactive:
- src: //www.geogebratube.org/material/iframe/id/XCBPHeKs/width/600/height/500/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When are the coefficients of a quadratic equal to its roots?

## Question

The equation \(x^2+ax+b=0\), where \(a\) and \(b\) are different, has solutions \(x=a\) and \(x=b\). How many such equations are there?

## Suggestion

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/XCBPHeKs/width/600/height/500/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/XCBPHeKs)

Here the blue curve is \(y = x^2 + ax+b\), while the red curve is \(y = (x-a)(x-b)\).

Can you adjust \(a\) and \(b\) so that the roots of the two curves are the same?

In this case, what can we say about the two curves?

## Solution

As \(x=a\) and \(x=b\) are the solutions to the equation \(x^2+ax+b=0\), we have \[x^2+ax+b\equiv(x-a)(x-b).\]

Expanding gives \[x^2+ax+b\equiv x^2+(-a-b)x+ab\]

Comparing coefficients of these two quadratics, we see that we require \(a=-a-b\) and \(b=ab\).

From the first condition we deduce \(a=-b/2\). Substituting this into the second condition gives \[b=-\frac{b^2}{2},\] which has solutions \(b=0\) and \(b=-2\).

As \(a\) and \(b\) are assumed to be different, we cannot use \(b=0\) because this corresponds to \(a=0\).

For \(b=-2\) we get \(a=1\), which is different from \(b\).

Alternatively, we could have started with the second condition, \(b=ab\). Rearranging this as \(ab-b=0\) and factorising to \(b(a-1)=0\) shows that \(a=1\) or \(b=0\), and we obtain the same solutions (\(a=b=0\) or \(a=1\), \(b=-2\)) again.

As yet a third approach, we could have substituted \(x=a\) and \(x=b\) into the original equation to obtain \(a^2+a^2+b=0\) and \(b^2+ab+b=0\); the first gives \(b=-2a^2\) and the second gives \(b(a+b+1)=0\). From the second equation, we obtain \(b=0\) and hence \(a=0\), or \(b=-a-1\). Substituting the latter into \(b=-2a^2\) gives \(2a^2-a-1=0\) or \((2a+1)(a-1)=0\), so \(a=1\) or \(a=-\frac12\). If \(a=1\), then \(b=-2\), as before. If \(a=-\frac12\), then \(b=-\frac12\), so \(a=b\).

This is strange: we have obtained a third possible solution using this approach, which did not appear in either of the first two approaches. (Though we have to reject it anyway, as \(a=b\), it is still odd that we have found a further solution.)

What’s going on here?  *JGF illustration: * Here we sketch the two curves $2x^2+y=0$ (in red), and $y^2+xy+y=0$ (in blue). Does this shed any light on our quandary? <cm-image url="images/img-7350-1.png" alt-text="the graphs 2x^2+y = 0 and y^2+xy+y=0 together." />

Since the solutions to \(x^2+x-2=0\) are indeed \(x=1\) and \(x=-2\), there is exactly one equation that meets the conditions.

What happens if we go up to a cubic?

If \(x^3 + ax^2 + bx + c = 0\) has the roots \(a\), \(b\) and \(c\), what equations are possible?

Can we come up with a general result for higher powers?

**Challenge**
