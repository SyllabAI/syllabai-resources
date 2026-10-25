---
created: 2026-10-25T21:48:43 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/sine-stretching
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/building-blocks
resource_identity:
  ugm_id: sine-stretching
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Developing
  ref: 8896
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: calculus-trig-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: calculus-trig-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.4.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-12 cross-map (cross-map-p3-differentiation.json
        (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4)
      evidence: gradient function of sin 3x selected from cos 3x / 3 cos x / 3 cos 3x by graphical reasoning
        - the chain-rule composite d/dx(sin 3x) = 3 cos 3x (flips the lane-11 non-overlap row of record
        routed 'P3 3.4 Differentiation')
      rationale: 'Canonical UGM title: Sine stretching'
      validation_status: SUGGESTED
    title: use the derivatives of e , ln x , sin x , cos x , tan x , tan x , together with constant multiples,
      sums, differences and composites
  mapped_date: '2026-10-25'
  mapper: cross-map-p3-differentiation.json (P3c lane 12) @ syllabai-experimental 506ea24f8e61cc75c4662f8ebb08cfd2b1d458d4
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-12
---

# Sine stretching

> Excerpt: Students are asked to use their knowledge of the derviatives of $\sin x$ and $\cos x$, alongside some graphical reasoning in order to find the derivative of the function $\sin (ax)$.

## Problem

Use the slider to change the value of \(a\).

- What do you notice?

- What questions do you have?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/K5B7w82h/width/600/height/320/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/K5B7w82h)

Decide which of the following is the gradient function of \(\sin 3x\) and justify your answer.

1. \(\cos 3x\)

---

1. \(3\cos x\)

---

1. \(3\cos 3x\)

It may be useful to use the GeoGebra applet or graph sketching to help you explain.

## Suggestion

What happens to the base of the triangle when the function changes from \(\sin x\) to \(\sin 2x\)?

How does this affect the gradient of the tangent?

The tangent to \(\sin x\) and the tangent to \(\sin 2x\) are drawn from two points with different \(x\) coordinates. What is the relationship between these \(x\) values?

## Solution

Things you might have noticed

How does the function change as \(a\) increases? You might have talked about the period of the graph decreasing or, if you thought about it as a transformation, you might describe a stretch parallel to the \(x\) axis. What is the scale factor of the stretch?

Thinking about the tangent to the graph, you should notice that the gradient of the tangent is getting steeper as \(a\) increases. The height of the triangle doesn’t change, but when \(a =2\), the base is half the original, and when \(a = 3\) the base is a third of the original. How much steeper is the gradient at these two points than when \(a=1\)?

Can you generalise some of your observations? As \(a\) increases, what happens to the \(x\) and \(y\) coordinates? What about the gradient?

Two possible ways to decide which is the gradient function are explored below.

Transforming

If we start with two points \(P\) and \(Q\), which lie on \(\sin x\) and \(\sin ax\) respectively, we can compare \(Q\) to \(P\) as we transform the graph from \(\sin x\) to \(\sin 3x\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/xWS8bQj6/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/xWS8bQj6)

The applet shows that the gradient of \(\sin 3x\) at \(Q\) is three times as steep as the gradient of \(\sin x\) at \(P\). As \(\cos x\) is the derivative of \(\sin x\) and has maximum and minimum values of \(1\) and \(-1\), we can argue that our derivative will have maximum and minimum values of \(3\) and \(-3\). This narrows our choice of gradient function to \(3\cos x\) or \(3\cos 3x.\)

The graph of \(\sin 3x\) cycles three times as fast as the graph of \(\sin x\). We could think about this as a stretch of \(\sin x\), parallel to the \(x\) axis, scale factor \(\frac{1}{3}\). What is the relationship between the \(x\) values at \(P\) and \(Q\)? Does this help us eliminate any of the possible answers?

One way we might write our argument down using mathematical notation is:

\[\dfrac{d}{dx}(\sin 3x_Q) = 3 \times \dfrac{d}{dx}(\sin x_P)\]

The gradient function of \(\sin 3x\) at \(Q\) is three times the gradient function of \(\sin x\) at \(P\).

\[\dfrac{d}{dx}(\sin 3x_Q) = 3 \times \cos x_P\]

We know the derivative of \(\sin x\) is \(\cos x\), so the derivative of \(\sin x_P = \cos x_P\).

\[\dfrac{d}{dx}(\sin 3x_Q) = 3 \times\cos 3x_Q\]

The relationship between the \(x\) values of \(P\) and \(Q\) is \(x_P = 3x_Q\).

Therefore the gradient function of \(\sin 3x\) is \(3\cos 3x\).

Gradient sketching

We could make a rough sketch of the gradient function by looking at when the gradient is positive, negative and zero. By marking the points where the gradient is zero, we can see that the gradient function will have the same period as \(\sin 3x\), and that the gradient function must be a multiple of \(\cos 3x\).

We need to think about what this multiple must be. If we compare the gradients of \(\sin 3x\) and \(\sin x\) at \((0,0)\), we can see that \(\sin 3x\) is steeper than \(\sin x\) at this point. Therefore the gradient of \(\sin 3x\) at \((0,0)\) is greater than \(1\).

This means that, from the options available, the gradient function of \(\sin 3x\) must be \(3\cos 3x\).

Alternatively, we might have estimated the gradient of \(\sin 3x\) at \((0,0)\) by considering the gradient of the chord from \((0,0)\) to \((0.1, \sin 0.3)\).

After thinking about the different ways you could have got the answer, can you see the two effects that the value of \(a\) has in the applet below?

For any value of \(a\), what is the gradient function of \(\sin ax\) (assuming \(a \neq 0\))?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/THfvDD8K/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/THfvDD8K)
