---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/r7586
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/review-question
resource_identity:
  ugm_id: r7586
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 7586
  old_site_id: Q58
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-of-powers
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-of-powers
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: OP+OQ minimum for the line y=c-mx through R(a,b) — differentiate a + ma + b/m
      rationale: 'Canonical UGM title: "Given the line $PRQ$, when is $OP + OQ$ a minimum?"; exam provenance:
        UCLES STEP Mathematics I, 2012, Q1'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  - code: 1.7.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: OP+OQ minimum for the line y=c-mx through R(a,b) — differentiate a + ma + b/m
      rationale: 'Canonical UGM title: "Given the line $PRQ$, when is $OP + OQ$ a minimum?"; exam provenance:
        UCLES STEP Mathematics I, 2012, Q1'
      validation_status: SUGGESTED
    title: locate stationary points and determine their nature, and use information about stationary
      points in sketching graphs.
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES STEP Mathematics I, 2012, Q1
task: T-UGM-IMPORT-7
interactive:
- src: //www.geogebratube.org/material/iframe/id/fQRUBj5w/width/600/height/450/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Given the line $PRQ$, when is $OP + OQ$ a minimum?

## Question

The line \(L\) has equation \(y=c-mx\), with \(m>0\) and \(c>0\). It passes through the point \(R(a,b)\) and cuts the axes at the points \(P(p,0)\) and \(Q(0,q)\), where \(a\), \(b\), \(p\) and \(q\) are all positive. Find \(p\) and \(q\) in terms of \(a\), \(b\) and \(m\).

As \(L\) varies with \(R\) remaining fixed, show that the minimum value of the sum of the distances of \(P\) and \(Q\) from the origin is \((a^{\frac{1}{2}}+b^{\frac{1}{2}})^2\), and find in a similar form the minimum distance between \(P\) and \(Q\). (You may assume that any stationary values of these distances are minima.)

## Suggestion

Could we draw a diagram to help us visualise the problem?

As \(L\) varies with \(R\) remaining fixed, show that the minimum value of the sum of the distances of \(P\) and \(Q\) from the origin is \((a^{\frac{1}{2}}+b^{\frac{1}{2}})^2\)…

How could we find a minimum? What is varying here? Could we differentiate with respect to that?

## Solution

The equation of a line with gradient \(-m\), passing through the point \(R(a,b)\) is \[y-b=-m(x-a).\] We can rearrange this and compare it with the given equation for \(L\) to find that \[c= ma+b.\] Therefore we find that \(q=ma+b\) and \(p=\dfrac{ma+b}{m}\).

As \(L\) varies with \(R\) remaining fixed, show that the minimum value of the sum of the distances of \(P\) and \(Q\) from the origin is \((a^{\frac{1}{2}}+b^{\frac{1}{2}})^2\)…

Use the applet to explore the behaviour as

\(m\)

varies. Drag

\(R\)

to different locations and vary

\(m\)

to see how the values of

\(OP+OQ\)

and

\(PQ\)

change.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/fQRUBj5w/width/600/height/450/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/fQRUBj5w)

Let the sum of the distances of \(P\) and \(Q\) from the origin be \(D\). Then \[D = (ma+b) + \left(\frac{ma+b}{m}\right) = ma+\frac{b}{m}+a+b.\] Since \(a\) and \(b\) are fixed, by varying \(L\) we are effectively just varying \(m\). Therefore, we want to minimise \(D\) with respect to \(m\).

Now differentiating, we have \[\frac{dD}{d m}=a-\frac{b}{m^2}.\] We get a stationary point when \(\dfrac{dD}{dm}=0\). That gives \[a=\frac{b}{m^2} \Longleftrightarrow m=\pm \sqrt{\frac{b}{a}}.\] We are told that \(m>0\), so we choose the positive root \(m=\sqrt{\frac{b}{a}}\).

This value must be a minimum value as there is only one stationary value, and by considering our expression for \(D\), we can see that as \(m\rightarrow 0, \, D\) will become very large, and the same will happen as \(m\rightarrow\infty\).

To find the minimum value, we substitute back into the expression for

\(D\)

:

\[\begin{align*} D &= a+b+a\sqrt{\frac{b}{a}}+b\sqrt{\frac{a}{b}}\\ &= a+b+2a^{\frac{1}{2}}b^{\frac{1}{2}}\\ &= (a^{\frac{1}{2}}+b^{\frac{1}{2}})^2 \end{align*}\]

as required.

… and find in a similar form the minimum distance between \(P\) and \(Q\).

The distance \(PQ = \sqrt{p^2+q^2}\).

It’s helpful for us to note that the minimum value of \(\sqrt{p^2+q^2}\) coincides with the minimum value of \(p^2+q^2\), so we can make our lives a little easier by concentrating on minimising \[PQ^2 = p^2 + q^2 = \left(\frac{ma+b}{m}\right)^2 + (ma+b)^2\] rather than \(\sqrt{p^2+q^2}\).

\[\begin{align*} PQ^2 &=\left(\frac{ma+b}{m}\right)^2 + (ma+b)^2 \\ &= \left(a+\frac{b}{m}\right)^2 + (ma + b)^2 \\ &=a^2 + 2\frac{ab}{m} + \frac{b^2}{m^2} + a^2m^2 + 2abm+ b^2\\ \end{align*}\]

Differentiating \(PQ^2\) with respect to \(m\) gives

\[\frac{d}{dm}(PQ^2) =-\frac{2ab}{m^2}-\frac{2b^2}{m^3} + 2a^2m + 2ab\]

The stationary points occur when

\[\begin{align*} -\frac{2ab}{m^2}-\frac{2b^2}{m^3} + 2a^2m + 2ab &= 0 \\ \iff \quad -\frac{b}{m^3}(am+b)+a(am+b)&=0 \\ \iff \quad \qquad (am + b)\left(a - \frac{b}{m^3}\right)&=0. \end{align*}\]

The two (real) roots of this equation are

\[\begin{align*} m&=-\frac{b}{a}\\ m^3&=\frac{b}{a} \quad \iff m=\sqrt[3]{\frac{b}{a}}. \end{align*}\]

The first of these is not a valid root, as

\(m>0\)

, so substituting the second back into the expression for

\(PQ^2\)

we find

\[\begin{align*} p^2+q^2&=\left(1+\frac{1}{m^2}\right)(ma+b)^2\\ &=(1+a^{\frac{2}{3}}b^{-\frac{2}{3}})(a^{\frac{2}{3}}b^{\frac{1}{3}}+b)^2\\ &=b^{-\frac{2}{3}}(b^{\frac{2}{3}}+a^{\frac{2}{3}})(b^{\frac{1}{3}})^2(a^{\frac{2}{3}}+b^{\frac{2}{3}})^2\\ &=(a^{\frac{2}{3}}+b^{\frac{2}{3}})^3. \end{align*}\]

Thus the minimum value of \(PQ= \sqrt{p^2+q^2}\) as \(L\) varies is \[(a^{\frac{2}{3}}+b^{\frac{2}{3}})^{\frac{3}{2}}.\]

As before, this value must be a minimum value as there is only one legitimate stationary value, and we can create arbitrarily large \(PQ\) by taking \(m\rightarrow 0\) or \(m\rightarrow\infty\).
