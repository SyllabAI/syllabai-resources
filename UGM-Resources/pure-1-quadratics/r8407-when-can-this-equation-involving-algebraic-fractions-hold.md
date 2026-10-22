---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r8407
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r8407
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8407
  old_site_id: Q52
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
  - code: 1.1.5
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c quadratics cross-map (cross-map-quadratics.json @
        syllabai-experimental 915bfa8c)
      evidence: Algebraic-fraction equation reduced to a quadratic.
      rationale: 'Canonical UGM title: “When can this equation involving algebraic fractions hold?”; exam
        provenance: UCLES 2005 Q3'
      validation_status: SUGGESTED
    title: recognise and solve equations in x which are quadratic in some function of x . tan
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 2005 Q3
task: T-UGM-IMPORT-1
interactive:
- src: //www.geogebratube.org/material/iframe/id/VAbYspuB/width/600/height/400/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When can this equation involving algebraic fractions hold?

## Question

In this question, \(a\) and \(b\) are distinct, non-zero real numbers, and \(c\) is a real number.

1. Show that, if \(a\) and \(b\) are either both positive or both negative, then the equation \[\frac{x}{x-a}+\frac{x}{x-b}=1\] has two distinct real solutions.
2. Show that the equation \[\frac{x}{x-a}+\frac{x}{x-b}=1+c\] has exactly one real solution if \(c^2=-\dfrac{4ab}{(a-b)^2}\). Show that this equation can be written \(c^2=1-\left(\dfrac{a+b}{a-b}\right)^2\) and deduce that it can only hold if \(0 < c^2 \leq 1\).

## Suggestion

How can we handle equations which involve fractions? Does it make a difference if \(x\) is in the denominator?

This interactive applet shows the graph of \(y = \dfrac{x}{x-a}+\dfrac{x}{x-b}-1\). You can change the values of \(a\) and \(b\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/VAbYspuB/width/600/height/400/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/VAbYspuB)

The blue lines are the lines \(y=c\) which intersect the red curve exactly once.

## Solution

Clearly \(x \neq a\) and \(x \neq b\). We multiply through by \((x-a)(x-b)\) to clear the denominators, and get the equation \[x(x-b)+x(x-a)=(x-a)(x-b),\] which, after multiplying out and rearranging, becomes \[x^2=ab.\] This equation will have two distinct real roots (\(\pm\sqrt{ab}\)) as long as \(ab>0\), which happens exactly when \(a\) and \(b\) are either both positive or both negative.

---

We multiply through by \((x-a)(x-b)\) as in the first part, this time finding, for \(x\) not equal to \(a\) or \(b\), that \[x(x-b)+x(x-a) = (1+c)(x-a)(x-b).\] Expanding this gives \[x^2-bx+x^2-ax = x^2-ax-bx+ab +cx^2-acx-bcx+abc,\] which rearranges to the quadratic \[(1-c)x^2 + c(a+b)x - abc - ab = 0.\]

We know that a quadratic equation has one (repeated) real solution if and only if the [discriminant](https://undergroundmathematics.org/glossary/discriminant) is equal to zero.

So the quadratic has one real solution if and only if \[c^2(a+b)^2+4(1-c)(abc+ab)=0.\] Expanding this gives \[c^2(a^2+2ab+b^2)+4abc-4c^2ab+4ab-4abc=0,\] that is, \[c^2(a^2-2ab+b^2)+4ab=0.\] Rearranging this yields the result we desire: the equation has exactly one real solution if and only if \[c^2=-\frac{4ab}{(a-b)^2}.\]

---

Looking at the equation we have and the equation we’d like to get to, it would be good if we could prove that \[-4ab=(a-b)^2-(a+b)^2.\]

Expanding, we see that \[(a-b)^2-(a+b)^2=a^2-2ab+b^2-a^2-2ab-b^2=-4ab,\] and so \[c^2 = -\frac{4ab}{(a-b)^2} = \frac{(a-b)^2 - (a+b)^2}{(a-b)^2} = 1 - \left(\frac{a+b}{a-b}\right)^2.\]

Looking closely at the equation \[c^2=1-\left(\frac{a-b}{a+b}\right)^2,\] we see that since \[\left(\frac{a-b}{a+b}\right)^2 \geq 0,\] we must have \(c^2 \leq 1\).

Furthermore, since \(c\) is real, we must have \(c^2 \geq 0\). However, \(c^2=0\) if and only if \(4ab=0\) (using our first expression for \(c\)).
 But we were told at the beginning that \(a\) and \(b\) were both non-zero, so this cannot happen.

So \(0<c^2\le 1\).

In fact, we were also told that \(a\) and \(b\) are distinct, so we cannot have \(a-b=0\), and hence we cannot have \(c=1\) either. So \(0<c^2<1\).

A subtle point; the question is worded as “show that \(A\) can only hold if \(B\)”, where \(A\) and \(B\) are statements.

(Here \(A\) is the statement “\(c^2=-\dfrac{4ab}{(a-b)^2}\)”, while \(B\) is the statement “\(0 < c^2 \leq 1\)”.)

The statement means “if \(A\) is true, then \(B\) must also be true”. This is different from saying “\(A\) if \(B\)”, which means “if \(B\) is true, then \(A\) must also be true”. The two statements are *converses* of each other. The converse of a true result is sometimes, but not always, true, and we must take care to ensure that we know which statement we are attempting to prove.
