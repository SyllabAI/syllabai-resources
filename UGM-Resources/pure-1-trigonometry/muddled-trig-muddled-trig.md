---
created: 2026-10-23T16:39:10 (UTC +06:00)
source: https://undergroundmathematics.org/trigonometry-triangles-to-functions/muddled-trig
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- trigonometry-triangles-to-functions
- type/building-blocks
- level/developing
resource_identity:
  ugm_id: muddled-trig
  station: trigonometry-triangles-to-functions
  station_title: 'Trigonometry: Triangles to Functions'
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Developing
  ref: 5337
  old_site_id: null
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
  spec_points:
  - code: 1.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: match plotted graphs to sin x, sin^2 x, sin(sin x), sin 2x, arcsin(sin x)... — graph recognition
        including inverse notation
      rationale: 'Canonical UGM title: “Muddled trig”'
      validation_status: SUGGESTED
    title: sketch and use graphs of the sine, cosine and Including e.g. tangent functions (for angles
      of any size, and using either degrees or radians)
  - code: 1.5.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c lane-5 cross-map (cross-map-trigonometry.json (P3c
        lane 5) @ syllabai-experimental 75f1cfb8)
      evidence: match plotted graphs to sin x, sin^2 x, sin(sin x), sin 2x, arcsin(sin x)... — graph recognition
        including inverse notation
      rationale: 'Canonical UGM title: “Muddled trig”'
      validation_status: SUGGESTED
    title: use the notations sin x , cos­ x , tan x to denote No specialised knowledge of these functions
      is the principal values of the inverse trigonometric required, but understanding of them as examples
      of relations inverse functions is expected. sin i
  mapped_date: '2026-10-23'
  mapper: cross-map-trigonometry.json (P3c lane 5) @ syllabai-experimental f3ef5745
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-5
assets:
- path: https://undergroundmathematics.org/trigonometry-triangles-to-functions/muddled-trig/components/function-cards.pdf
  kind: printable
- path: https://undergroundmathematics.org/trigonometry-triangles-to-functions/muddled-trig/components/graphs-cards.pdf
  kind: printable
- path: https://undergroundmathematics.org/trigonometry-triangles-to-functions/muddled-trig/download/teacher-notes.pdf
  kind: printable
---

# Muddled trig

> Excerpt: Students are asked to match various trigonometric functions with their graphs, at the same time as thinking about the notational anomalies involved. The integer scale on the $x$-axis provides an opportunity to discuss radians and degrees and estimations of $\pi$, $\frac{\pi}{2}$ and so on.

## Problem

We have plotted the graphs of four of the following functions.

\[\sin x \quad \,\,\sin^{2}x \quad \,\,\sin(\sin x) \quad \,\, \sin (2x) \quad \,\, \arcsin x \quad \,\, \sin^{-1} x \quad \,\, \dfrac{1}{\sin x}\]

Which of these functions have we plotted?

Which properties of the functions and graphs may help you to decide?

How many different functions are there in the list above?

Graph A

Graph B

Graph C

Graph D

You might find it helpful to think about function machines for some of these functions, or to describe what the function is doing in words.

The [functions](https://undergroundmathematics.org/trigonometry-triangles-to-functions/muddled-trig/components/function-cards.pdf) and [graphs](https://undergroundmathematics.org/trigonometry-triangles-to-functions/muddled-trig/components/graphs-cards.pdf) are available to cut out.

## Solution

There are many ways to decide which functions have been plotted. We will start by exploring properties of the functions and then use these properties to decide which have been plotted. You may find it helpful to try to sketch the graphs of the functions, or try to match them to the given graphs, as you read.

**Thinking about the functions**

All of these functions are related to \(\sin x\) in some way. We can think about the following questions to help identify properties of the functions.

- What are the domains and ranges of these functions?

- Are any of these functions periodic and what could the period be?

- Are these functions odd or even or neither?

\(\sin x\)

We know that \(\sin x\) is defined for any real number \(x\), so its domain is \(\mathbb{R}.\) We also know that \(-1 \leq \sin x \leq 1\) and the period is \(2\pi\).

The rotational symmetry of the graph \(y=\sin x\) about the origin means that \(\sin x\) is an odd function, i.e. \(\sin (-x)=-\sin x.\)

\(\sin^{2}x\)

Although the notation might be confusing, \(\sin^{2}x\) means \((\sin x)^2.\)

By thinking about \(\sin^{2}x\) as a composition of functions, we can see that the sine function is applied to \(x\) and then the result is squared. Therefore the domain of \(\sin^{2} x\) is \(\mathbb{R}.\) As the function is a square, it cannot be negative so we must have \(0 \leq \sin^{2} x \leq 1.\)

You may find it helpful to draw a function machine for \(\sin^{2}x\) or to think about how the domain or range could be affected if we had a different power, such as \(\tfrac{1}{2}.\)

From the symmetry of the graph \(y=\sin x\) we know that \(\sin (x+\pi)=-\sin x\), so \(\sin^{2}(x+\pi)=\sin^{2}x\) and we can check that the period of \(\sin^{2}x\) is not less than \(\pi.\)

Although \(\sin x\) is an odd function, \(\sin^{2}(-x)=(\sin(-x))^{2}=(-\sin x)^2=\sin^{2}x\), so \(\sin^{2}x\) is an even function.

\(\sin(\sin x)\)

This could be read as “sine of sine of \(x\)”. This function is defined for all real values of \(x.\) As \(-1 \leq \sin x \leq 1\), the range of \(\sin(\sin x)\) must be all values between \(\sin (-1)\) and \(\sin 1.\) Note that \(\sin (-1) = -\sin 1\) so the range of \(\sin(\sin x)\) is symmetric about \(0.\)

The period of \(\sin(\sin x)\) must also be \(2\pi.\) How could you convince yourself of this?

\(\sin (2x)\)

As the graph of \(y=\sin (2x)\) is a stretch of the standard sine wave by scale factor \(\tfrac{1}{2}\) parallel to the \(x\)-axis, the period of \(\sin (2x)\) is \(\pi\), the domain is \(\mathbb{R}\) and \(-1 \leq \sin (2x) \leq 1.\)

\(\arcsin x\)

There are lots of values of \(x\) which give the same value of \(\sin x\), but the function \(\arcsin x\) is defined to give us an output between \(-\dfrac{\pi}{2}\) and \(\dfrac{\pi}{2}.\) As \(\sin x\) only has values between \(-1\) and \(1\), the domain of \(\arcsin x\) is \(-1 \leq x \leq 1.\) The function \(\arcsin x\) is not periodic, and it is an odd function.

\(\sin^{-1} x\)

This is the same function as \(\arcsin x\) and both notations are regularly used. Crucially, \(\sin^{-1} x\) is not the same as \(\dfrac{1}{\sin x}.\)

\(\dfrac{1}{\sin x}\)

Note that this function is also called \(\cosec x.\). The function is not defined if \(\sin x =0\) and hence the domain is all real numbers except integer multiples of \(\pi.\) As \(\sin x\) must give a value between \(-1\) and \(1\), we must have \(\dfrac{1}{\sin x} \leq -1\) or \(\dfrac{1}{\sin x} \geq 1.\)

From the periodicity of the \(\sin x\) function, the period of \(\dfrac{1}{\sin x}\) must be \(2\pi.\)

This function is odd because \(\dfrac{1}{\sin (-x)}= \dfrac{1}{-\sin x} = -\dfrac{1}{\sin x}.\) We could also see this by thinking more generally about composition of odd functions.

If you find it confusing that \(\sin^{2} x\) means \((\sin x)^{2}\) but \(\sin^{-1} x\) does not mean \(\dfrac{1}{\sin x}\), then you are in good company. The famous mathematician [Carl Friedrich Gauss](http://www-groups.dcs.st-and.ac.uk/~history/Biographies/Gauss.html) wrote

“\(\sin^{2} \varphi\) is odious to me, even though Laplace made use of it; should it be feared that \(\sin \varphi^{2}\) might become ambiguous, which would perhaps never occur, or at most very rarely when speaking of \(\sin(\varphi^{2})\), well then, let us write \((\sin \varphi)^{2}\), but not \(\sin^{2} \varphi\), which by analogy should signify \(\sin (\sin \varphi).\)”

**Matching the graphs**

Graph A

This looks very much like the standard sine wave \(y=\sin x\) as the graph shows an odd function with period slightly greater than \(6.\) However, the \(y\)-values don’t quite reach \(1\) or \(-1\). Therefore we need a different odd, periodic function whose range includes \(0\) and negative values. We cannot use \(y=\sin 2x\) as this has period \(\pi.\) This only leaves \(y=\sin(\sin x)\), which has many similar properties to \(y=\sin x\) but its maximum value is \(\sin 1\), which is less than \(1.\)

Graph B

This graph appears to have period \(2\pi\), like Graph A. The vertical [asymptotes](https://undergroundmathematics.org/glossary/asymptote) suggest that this could be the graph of \(y=\dfrac{1}{\sin x}\) and this is the only candidate with a suitable range.

Graph C

This graph looks like a smaller, translated version of a standard sine wave. The period could be \(\pi\) and the graph has no negative values. This leads us to \(y=\sin^{2} x.\) The symmetry in the \(y\)-axis also tells us that we are looking for an even function and \(\sin^{2}x\) is the only even function in the list.

Graph D

This graph is not periodic and the domain looks as if it could be \(-1\leq x \leq 1\). Looking at the properties of the available functions we note that \(\arcsin x\) is the only candidate, so we have found our match. Note that we could equally well say that \(\sin^{-1}x\) is the function shown in Graph D.
