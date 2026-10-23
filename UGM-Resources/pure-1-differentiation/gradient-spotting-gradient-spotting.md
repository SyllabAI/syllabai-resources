---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-of-powers/gradient-spotting
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-of-powers
- type/building-blocks
- level/introducing
resource_identity:
  ugm_id: gradient-spotting
  station: calculus-of-powers
  station_title: Calculus of Powers
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Introducing
  ref: 6979
  old_site_id: null
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
      evidence: applet pattern-hunt for the gradient of ax^2+bx+c and of cubics — inducing the power
        rule with each coefficient's contribution to the gradient
      rationale: 'Canonical UGM title: "Gradient spotting"'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/calculus-of-powers/gradient-spotting/download/teacher-notes.pdf
  kind: printable
interactive:
- src: //www.geogebratube.org/material/iframe/id/CHRwAg7n/width/652/height/673/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
- src: //www.geogebratube.org/material/iframe/id/vMdq5UMB/width/654/height/673/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Gradient spotting

> Excerpt: Students use an applet to look for patterns in the gradients of quadratics and cubics, with the aim of understanding the contribution of each coefficient to the gradient and thus producing a rule for finding the gradient function (derivative) of these polynomials.

## Investigating quadratics

- In the upper half of this applet, the graph of \(y=f(x)\) is drawn, where \(f(x)=ax^2+bx+c\). You can change the values of the coefficients \(a\), \(b\) and \(c\) by moving the sliders or typing in values.

- The points \((x,f(x))\) are shown in green for \(x=-4\), \(-3\), …, \(4\) (though some of these may be beyond the visible part of the graph).

- Part of the tangent to the graph of \(y=f(x)\) is drawn in orange at each of these points.

- The gradients of these tangents have been calculated; they are shown in the spreadsheet on the right hand side, and are also plotted on the graph in the lower half of the applet.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/CHRwAg7n/width/652/height/673/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/CHRwAg7n)

The big question: Can you find a relationship between the equation of the quadratic and its gradient at \(x\)?

For each of the following questions, describe what you think will happen before you try it out on the interactivity. Then reflect on your ideas: did the actual behaviour surprise you? And can you explain the observed behaviour? (You might want to start with very simple values for \(a\), \(b\) and \(c\).)

- What happens to the gradients as you change \(c\)?

- What happens to the gradients as you change \(a\)?

- What happens to the gradients as you change \(b\)?

Given what you have discovered, can you use it to predict what the gradients will be for some or all of the following quadratics? Test your predictions!

- \(y=2x^2\)

- \(y=x^2+x\)

- \(y=2x^2+x\)

- \(y=2x^2+x-3\)

- \(y=-3x^2\)

- \(y=x^2-x\)

- \(y=3x^2-2x+1\)

Now predict the gradients for some other quadratics and test your results until you are confident that you have found a way of predicting the gradient function for any quadratic.

## Investigating cubics

Here is an applet very similar to that in the [first section](https://undergroundmathematics.org/calculus-of-powers/gradient-spotting/), only this time it is for cubic graphs \(y=f(x)\) where \(f(x)=ax^3+bx^2+cx+d\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/vMdq5UMB/width/654/height/673/border/888888/rc/false/ai/false/sdz/true/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/vMdq5UMB)

Again, the big question: Can you find a relationship between the equation of the cubic and its gradient at \(x\)?

As with the quadratic case, for each of the following questions, describe what you think will happen before you try it out on the interactivity. Then reflect on your ideas: did the actual behaviour surprise you? And can you explain the observed behaviour?

- What happens to the gradients as you change \(d\)?

- What happens to the gradients as you change \(a\)?

- What happens to the gradients as you change \(c\)?

- What happens to the gradients as you change \(b\)?

Given what you have discovered, can you use it to predict what the gradients will be for some or all of the following cubics? Test your predictions!

- \(y=2x^3\)

- \(y=x^3+x\)

- \(y=x^3-x^2\)

- \(y=2x^3+x^2\)

- \(y=2x^3-x^2+3x\)

- \(y=-x^3+2x^2-3x+4\)

Now predict the gradients for some other cubics and test your results until you are confident that you have found a way of predicting the gradient function for any cubic.

Can you predict what the gradient will be for quartics (equations of the form \(y=ax^4+bx^3+\cdots\)) or [polynomials](https://undergroundmathematics.org/glossary/polynomial) of higher [degree](https://undergroundmathematics.org/glossary/degree-of-a-polynomial)?

## Things you might have noticed

**Quadratic gradients**

- As we change \(c\), the curve just translates up or down, so the gradient at a given \(x\)-value does not change.

- The graph of the gradients is a straight line, and its gradient changes as we change \(a\). The gradient function of \(y=x^2\) is \(2x\), as we discovered in [Zooming in](https://undergroundmathematics.org/introducing-calculus/zooming-in). If we stretch this function in the \(y\)-direction by a factor of \(2\), by setting \(a=2\), we double the gradients, giving a gradient function of \(4x\). Does the same sort of thing happen for other values of \(a\)? Does changing \(b\) affect the gradient of the gradient function line?

- Changing \(b\) translates the gradient function. If we add \(1\) to \(b\), then the gradient function increases by \(1\). This makes some sense: \(b=1\) (with \(a=c=0\)) gives the function \(y=x\), which has gradient \(1\) everywhere. So if we add \(x\) to our function, it seems reasonable that the gradient should increase by \(1\). For example, when we go from \(y=3x\) to \(y=3x+x=4x\), the gradient increases from \(3\) to \(4\).

Putting these together, to find the gradient of the quadratic function \(f(x)=ax^2+bx+c\), we can start with \(x^2\), stretch it by a factor of \(a\) to get \(ax^2\) (which has what gradient function?), then add on \(bx\) (which does what to the gradient function?) and then finally add \(c\). This will give us the final gradient function.

**Cubic gradients**

Following on from the above ideas, we can predict what will happen for a cubic: starting with \(x^3\), which appears to have a quadratic gradient function (which quadratic exactly?), we stretch it to obtain \(ax^3\), and this stretches the gradient function. We then add on extra terms, whose behaviour we now understand from exploring quadratics: first we add on \(bx^2\), then \(cx\) and finally \(d\).

Using this idea, we should be able to predict the gradient function of any cubic \(f(x)=ax^3+bx^2+cx+d\).

Can you predict what the gradient will be for quartics (equations of the form \(y=ax^4+bx^3+\cdots\)) or polynomials of higher degree?

Some patterns definitely seem to be emerging here! What would you expect the gradient function of \(x^4\) to be?
