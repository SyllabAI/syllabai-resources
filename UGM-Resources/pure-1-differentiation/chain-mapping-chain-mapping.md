---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/chain-mapping
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/building-blocks
- level/introducing
resource_identity:
  ugm_id: chain-mapping
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Introducing
  ref: 9648
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: mapping-diagram derivation of the chain rule (local scalings multiply); the worked examples
        extend beyond the P1 linear-inner scope (recorded)
      rationale: 'Canonical UGM title: "Chain mapping"; exam provenance: , None'
      validation_status: SUGGESTED
    title: use the derivative of x (for any rational n ), together with constant multiples, sums and
      differences of functions, and of composite functions using the chain rule
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: ', None'
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/chain-rule/chain-mapping/assets/mapping-diagrams-composite-2.pdf
  kind: printable
- path: https://undergroundmathematics.org/chain-rule/chain-mapping/assets/mapping-diagrams-composite.pdf
  kind: printable
- path: https://undergroundmathematics.org/chain-rule/chain-mapping/download/teacher-notes.pdf
  kind: printable
interactive:
- src: //www.geogebratube.org/material/iframe/id/R8RFvC2q/width/600/height/493/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Chain mapping

> Excerpt: Students are led to an understanding of what the chain rule means and why it works, using mapping diagrams.  It builds on two earlier mapping diagrams resources.

## Warm-up

In [Mapping a function](https://undergroundmathematics.org/thinking-about-functions/mapping-a-function), we explored mapping diagrams for linear functions. What happens if we now compose two functions?

- How could we draw a mapping diagram to show the composition of the function \(f(x)=\frac{3}{2}x\) with the function \(g(x)=2x\) to get the function \(h(x)=g(f(x))\)?

- We described linear functions as scalings. How are the scalings represented by the three functions \(f\), \(g\) and \(h\) related to each other?

## Warm-up ideas

In [Mapping a function](https://undergroundmathematics.org/thinking-about-functions/mapping-a-function), we explored mapping diagrams for linear functions. What happens if we now compose two functions?

- How could we draw a mapping diagram to show the composition of the function \(f(x)=\frac{3}{2}x\) with the function \(g(x)=2x\) to get the function \(h(x)=g(f(x))\)?

We can represent this composite by using three numberlines, with arrows from the left to middle one representing \(f(x)\), and then arrows from the middle to the right representing \(g(x)\), like this:

Here, we have centred the left-hand numberline on \(2\); the numberlines are centred in such a way that the arrow starting from \(2\) is horizontal, as before.

We can then show the composite function \(h(x)=g(f(x))\) by joining the starts to the ends of the arrow chains, like this:

This shows how the function \(h\) takes values from the left-hand numberline to values on the right-hand numberline.

As in Mapping a function, we can also extend the arrows beyond the numberlines. For clarity, we only do this for the composite function \(h\):

The lines all meet in a point, showing that \(h(x)\) is a scaling with a scale factor of \(3\). (This is the scaling factor from the left-hand to right-hand numberline.) As \(h(x)=g(f(x))=g\bigl(\frac{3}{2}x\bigr)=3x\), this is to be expected.

We can also check that the formula we worked out in [Mapping a function](https://undergroundmathematics.org/thinking-about-functions/mapping-a-function/noticed) for the location of the focal point gives us the expected location: that formula gives the location as \(\frac{1}{1-3}=-\frac{1}{2}\) times the distance between the numberlines. This matches what we see in the diagram, because the numberlines of interest here are the left-hand and right-hand ones.

- We described linear functions as scalings. How are the scalings represented by the three functions \(f\), \(g\) and \(h\) related to each other?

\(f(x)=\frac{3}{2}x\) is a scaling with scale factor \(\frac{3}{2}\) and \(g(x)=2x\) is a scaling with scale factor \(2\). The composite function \(h(x)=3x\) is a scaling with scale factor \(3\).

In general, if we compose a scaling with scale factor \(s\) together with a scaling with scale factor \(t\), we will get a scaling with scale factor \(st\). In our particular case, we have \(\frac{3}{2}\times 2=3\).

Here, we used linear functions with no constant term and centred our mapping diagram on \(0\). Would we have obtained the same results if we had started with the functions \(f(x)=\frac{3}{2}x+4\) and \(g(x)=2x-3\), still with \(h(x)=g(f(x))\), and centred our mapping diagram on \(7\) (as input value)?

## Problem

In [Mapping a derivative](https://undergroundmathematics.org/introducing-calculus/mapping-a-derivative), we saw that we can think of a derivative as a local scaling. What happens if we now want to find the derivative of a composite of two functions?

- What does the mapping diagram of the composite \(h(x)=g(f(x))\) look like if \(f(x)=x^2+3\) and \(g(x)=\sqrt{x}\) (so that \(h(x)=\sqrt{x^2+3}\)), and we centre our mapping diagram at \(1\) on the input numberline?

- How does the diagram change as we zoom in?

- What does this tell us about the derivative \(h'(1)\)?

- Generalising this, given any composite function \(h(x)=g(f(x))\), how can we find \(h'(a)\) for a given \(a\)?

You can download blank composite mapping diagrams with [one on a page](https://undergroundmathematics.org/chain-rule/chain-mapping/assets/mapping-diagrams-composite.pdf) or [two on a page](https://undergroundmathematics.org/chain-rule/chain-mapping/assets/mapping-diagrams-composite-2.pdf), or you can use the [interactivity](https://undergroundmathematics.org/chain-rule/chain-mapping/interactivity) to explore this.

## Things you might have noticed

If we draw the mapping diagram at a scale of \(1\) unit per tick mark, we obtain the following, where the non-linear behaviour of \(f\) is clear, though that of \(g\) is less so:

We can now draw the composite arrows and extend them into lines:

We see that the green lines fail to meet at a point. If we zoom in, things now look very different:

What is going on here?

- The composite function \(h(x)\) appears to be a local scaling, as all of the lines meet at a point. From the diagram, the scale factor appears to be \(\frac{1}{2}\).

- The function \(f(x)=x^2+3\) is locally a scaling with scale factor \(2\). We can see this either by looking at the mapping diagram carefully, or by noting that the derivative of \(f(x)\) is \(f'(x)=2x\), so that the scale factor at \(x=1\) is \(f'(1)=2\).

- The function \(g(x)=\sqrt{x}\) is also locally a scaling when we zoom in. The scale factor is a little harder to make out reliably from the diagram, but we can use what we know about differentiation to calculate it. We have \(g'(x)=\dfrac{1}{2\sqrt{x}}\). The function \(g\) is centred on \(x=f(1)=4\) in this diagram, so the local scale factor is \(g'(f(1))=g'(4)=\dfrac{1}{2\sqrt{4}}=\dfrac{1}{4}\).

- Composing these, we obtain a local scaling with scale factor \(2\times\frac{1}{4}=\frac{1}{2}\), multiplying the scale factors as we saw in the [Warm-up](https://undergroundmathematics.org/chain-rule/chain-mapping/) section. This calculated composite scale factor agrees with what we observed about the function \(h(x)\).

So we conclude that \(h'(1)=\frac{1}{2}\).

Here is a somewhat generic sketch of a composite mapping diagram for \(h(x)=g(f(x))\), where we have shown the arrows and lines for \(h(x)\) but not for the individual functions \(f(x)\) or \(g(x)\):

The function \(f(x)\) gives a local scaling with scale factor \(f'(a)\), the derivative of \(f\) at \(a\).

The function \(g(x)\) is centred on \(f(a)\), so it gives rise to a local scaling with scale factor \(g'(f(a))\), the derivative of \(g\) at \(f(a)\).

Since \(h(x)\) is locally the composition of these two scalings, we see that \(h'(a)\) is also a local scaling. The scale factor of the composition is the product of the scale factors of \(f\) and \(g\), so \(h'(a)=f'(a)\times g'(f(a))\).

This is the *chain rule*, which can therefore be written: \[\text{if $h(x)=g(f(x))$, then $h'(x)=g'(f(x)).f'(x)$.}\]

There is another common way of writing the chain rule, which we can get by setting \(u=f(x)\) and \(y=h(x)\), so that \(y=g(f(x))=g(u)\). We then have \(f'(x)=\dfrac{du}{dx}\) and \(g'(f(x))=g'(u)\), which we can write as \(\dfrac{dy}{du}\). Substituting this into the previous version then gives us: \[\dfrac{dy}{dx}=\dfrac{dy}{du}\times \dfrac{du}{dx}.\]

## Interactivity

To enter the function \(x^2\) into this applet, type x^2. To enter \(\sqrt{x}\), type sqrt(x).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/R8RFvC2q/width/600/height/493/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/R8RFvC2q)
