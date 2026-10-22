---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/composing-gets-me-nowhere
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/building-blocks
- level/developing
resource_identity:
  ugm_id: composing-gets-me-nowhere
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Developing
  ref: 9925
  old_site_id: F2_RT2_1
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: combining-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: combining-functions
    validation_status: SUGGESTED
  spec_points:
  - code: 1.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: ff(x)=x self-composition; self-inverse naming and examples — inverse fluency extension.
      rationale: 'Canonical UGM title: “Composing gets me nowhere”'
      validation_status: SUGGESTED
    title: identify the range of a given function in simple cases, and find the composition of two given
      functions condition that a composite function
  - code: 1.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: ff(x)=x self-composition; self-inverse naming and examples — inverse fluency extension.
      rationale: 'Canonical UGM title: “Composing gets me nowhere”'
      validation_status: SUGGESTED
    title: determine whether or not a given function is one-one, and find the inverse of a one-one function
      in simple cases
  - code: 1.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: ff(x)=x self-composition; self-inverse naming and examples — inverse fluency extension.
      rationale: 'Canonical UGM title: “Composing gets me nowhere”'
      validation_status: SUGGESTED
    title: understand the terms function, domain, range, one-one function, inverse function and composition
      of functions
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/composing-gets-me-nowhere/images/graph-g.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/composing-gets-me-nowhere/images/graph-m.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/composing-gets-me-nowhere/images/newimage2.png
  kind: figure
---

# Composing gets me nowhere

> Excerpt: This resource is designed to be used as an introduction to self-inverse functions.
Students are asked to sketch a set of functions, work out which ones are self-inverse and find a graphical connection between them.

## Warm-up

If \(f(x)=\dfrac{1}{x}\), for \(x\ne 0\), what is \(ff(x)\)?

By \(ff(x)\) we mean the composition of \(f\) with itself, sometimes written as \(f^2(x)\).

\[ff(x)=f\left(\frac{1}{x}\right)=\frac{1}{\left(\frac{1}{x}\right)}=x\]

The composition of \(f\) with itself is a function whose output is the same as the input value. We call \(f\) a self-inverse function. Can you explain why we use this name?

Note that the composition \(ff(x)\) is undefined at \(x=0\) even though the function \(x\) *is* defined.

**Answer**

Can you find any other functions that behave in this way when composed with themselves?

## Problem

Sketch the following functions and determine which of them are [self-inverse](https://undergroundmathematics.org/glossary/self-inverse-function).

| \(g(x)=\dfrac{x+1}{x-1}\) | \(m(x)=\dfrac{x-1}{x+1}\) |
| --- | --- |
| \(h(x)=8-x\) | \(n(x)=8+x\) |
| \(k(x)=\dfrac{x}{x-1}\) | \(p(x)=x\) |

What do the graphs of the self-inverse functions have in common?

Sketch and find equations for some other self-inverse functions.

## Solution

In order to sketch the graph of \(y=g(x)\) it is helpful to rewrite it as \[y=\frac{x+1}{x-1}=\frac{x-1+2}{x-1} = 1+\frac{2}{x-1} .\] This reveals that the graph is a transformation of \(y=\dfrac{1}{x}\).

> [figure: graph of x+1 over x-1 — `https://undergroundmathematics.org/combining-functions/composing-gets-me-nowhere/images/graph-g.png`] (image not included in the text import; path of record).

We compose \(g(x)\) with itself: \[ gg(x) = g\left( \frac{x+1}{x-1} \right) = \frac{\frac{x+1}{x-1}+1}{\frac{x+1}{x-1}-1} = \frac{x+1+(x-1)}{x+1-(x-1)} = \frac{2x}{2} = x \]

So \(g(x)\) is self-inverse.

Strictly, for \(g\) to be self-inverse, we should check that its range exactly matches its domain since its output is used as its own input in the composition.

What are the domain and range of \(g(x)\)?

**\(g(x)=\dfrac{x+1}{x-1}\)**

By rewriting \(m\) we find that, as for \(g\), its graph is a transformation of \(y=\dfrac{1}{x}\).

so \(m(x)\) is **not** self-inverse.

What is different about \(g\) that makes it self-inverse while \(m\) is not?

 Composing, we find

\[\begin{align*} mm(x) &= m\left( \frac{x-1}{x+1} \right) = \frac{\frac{x-1}{x+1}-1}{\frac{x-1}{x+1}+1}\\ &= \frac{x-1-(x+1)}{x-1+(x+1)} = \frac{-2}{2x} = -\frac{1}{x} , \end{align*}\]

> [figure: graph of x-1 over x+1 — `https://undergroundmathematics.org/combining-functions/composing-gets-me-nowhere/images/graph-m.png`] (image not included in the text import; path of record).

What happens if we compose \(mm(x)\) with itself to make the function \(mmmm(x)\) (which could be written as \(m^4(x)\))?

**\(m(x)=\dfrac{x-1}{x+1}\)**

Of the remaining functions, we find that \(h\), \(k\) and \(p\) are self-inverse.

**Functions \(h\), \(k\), \(n\) and \(p\)**

We have sketched the four self-inverse functions on the same set of axes.

> [figure: sketch of functions g h k and p — `https://undergroundmathematics.org/combining-functions/composing-gets-me-nowhere/images/newimage2.png`] (image not included in the text import; path of record).

We remember that the graphs of any function and its inverse are reflections of one another in the line \(y=x\). So it is no surprise that the graph of each self-inverse function is a reflection of *itself* in \(y=x\).

Can you match up the four functions with their graphs?

By thinking about the reflection property we can see that any straight line parallel to the purple line in the graph above will represent a self-inverse function. Can you write down a generalised form of the equation?

Also, any translation of \(y=\dfrac{1}{x}\) will be self-inverse so long as the origin is transformed to a point on the line \(y=x\). What about stretches, reflections and other transformations?

Can you find any other families of self-inverse functions?
