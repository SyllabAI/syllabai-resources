---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/slippery-slopes-another-derivative
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
  ugm_id: slippery-slopes-another-derivative
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Introducing
  ref: 7765
  old_site_id: C5_RT2_1
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
      evidence: derivatives of (2x+1)^-1 via translated 1/x graphs — a pre-chain-rule view of the linear-inner
        composite
      rationale: 'Canonical UGM title: "Slippery slopes... another derivative"'
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
- path: https://undergroundmathematics.org/chain-rule/slippery-slopes-another-derivative/download/teacher-notes.pdf
  kind: printable
interactive:
- src: //www.geogebratube.org/material/iframe/id/ePU8jFwR/width/600/height/396/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
- src: //www.geogebratube.org/material/iframe/id/RExfGrf4/width/624/height/407/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Slippery slopes... another derivative

> Excerpt: This resource discusses how the derivatives of functions like $(2x+1)^{-1}$ can be obtained by viewing them as translations of functions that we already know how to differentiate. This could precede work on the chain rule.

## Problem

You might find some of the ideas in [Slippery slopes](https://undergroundmathematics.org/calculus-meets-functions/slippery-slopes) helpful when thinking about this problem.

Here are the graphs of \(y=\dfrac{1}{x}\) and \(y=\dfrac{1}{x+1}\) with tangents drawn at points A and B.

What happens when you move the point A? *(Be careful when the \(x\)-coordinate of A gets close to \(-1\).)*

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/ePU8jFwR/width/600/height/396/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/ePU8jFwR)

1. How could you work out the gradient of \(y=\dfrac{1}{x+1}\) at the point \((2,\tfrac{1}{3})\)?

---

1. How can you differentiate \(\dfrac{1}{x+1}\)?

---

1. How could you adapt these approaches to work out the derivative of \(\dfrac{1}{2x+1}\)?

Suggestion for part 1

The graph of \(y=\dfrac{1}{x+1}\) is a translation of the graph of \(y=\dfrac{1}{x}\).

Suggestion for part 2

Can you generalise ideas from part 1 to find the derivative of \(\dfrac{1}{x+1}\) at a general point \((x,y)\)?

Suggestion for part 3

We already know how to differentiate constant multiples of powers of \(x\), so we know how to differentiate \(\dfrac{1}{2x}\).

Can you suggest other examples where you could use a similar approach to find derivatives?

In this problem we have only composed the function \(\dfrac{1}{x}\) with functions of the form \(ax+b\). Could you apply any of these ideas to polynomial, rational or trigonometric functions?

## Solution

There are several ways to find the gradient function or derivative of \(\dfrac{1}{x+1}.\) The approaches we discuss here assume that you do not already know how to differentiate this function directly.

The graph of \(y=\dfrac{1}{x+1}\) is a translation \(y=\dfrac{1}{x}.\)

Therefore the tangent to \(y=\dfrac{1}{x+1}\) at \((2,\tfrac{1}{3})\) is parallel to the tangent to \(y=\dfrac{1}{x}\) at \((3, \tfrac{1}{3}).\)

It follows that the gradient of \(y=\dfrac{1}{x+1}\) where \(x=2\) is the same as the gradient of \(\dfrac{1}{x}\) where \(x=3.\)

Therefore the gradient of \(y=\dfrac{1}{x+1}\) at \((2,\tfrac{1}{3})\) is \(-\tfrac{1}{9}.\)

Now consider a general point \((x,y)\) on the graph of \(y=\dfrac{1}{x+1}.\)

From the ideas in part 1, the gradient of \(y=\dfrac{1}{x+1}\) at a general point \((x,y)\) is the same as the gradient of \(y=\dfrac{1}{x}\) at the point with coordinates \((x+1,y)\).

You can see this by moving the point A in the GeoGebra file above.

Therefore the derivative of \(\dfrac{1}{x+1}\) is \(\dfrac{-1}{(x+1)^{2}}.\)

What would happen if the function we wanted to differentiate had been a translation of \(y=\dfrac{1}{x}\) parallel to the \(y\)-axis instead?

We already know how to differentiate constant multiples of powers of \(x\), so we know how to differentiate \(\dfrac{1}{2x}\). From the first part of the problem we also know a way of finding the derivatives of horizontal translations of functions. What is \(y=\dfrac{1}{2x+1}\) as a translation of \(y=\dfrac{1}{2x}\)?

The vertical asymptotes of the two graphs suggest that \(y=\dfrac{1}{2x+1}\) is a translation of \(y=\dfrac{1}{2x}\) by \(\dfrac{1}{2}\) in the negative \(x\)-direction.

Function notation can help to show this too.

If we write \(\dfrac{1}{2x}=f(x)\) then \(\dfrac{1}{2x+1} = \dfrac{1}{2(x+\tfrac{1}{2})} = f(x+\tfrac{1}{2}).\)

This means that the gradient of \(y=\dfrac{1}{2x+1}\) at \((x,y)\) is the same as the gradient of \(y=\dfrac{1}{2x}\) at \((x+\tfrac{1}{2}, y)\).

You can see this by moving the point A in the GeoGebra file below. *Be careful when the \(x\)-coordinate of A gets close to \(-\tfrac{1}{2}\).*

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/RExfGrf4/width/624/height/407/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/RExfGrf4)

It follows that the gradient of \(y=\dfrac{1}{2x+1}\) at \((x,y)\) is \(\dfrac{-1}{2(x+\tfrac{1}{2})^{2}}.\)

We can write this as \(\dfrac{-2}{(2x+1)^{2}}\) to help see the relationship between the original function and its derivative.

You could also think of \(y=\dfrac{1}{2x+1}\) as a transformation of \(y=\dfrac{1}{x}.\) How would this affect your approach?
