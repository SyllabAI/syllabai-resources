---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r5966
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r5966
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5966
  old_site_id: Q121
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
  - code: 1.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Domain/codomain/range/bijective vocabulary; range of f and of g∘f; bijectivity <-> inverse
        existence. phi/psi cycle extends beyond P1 routine.
      rationale: 'Canonical UGM title: “Can we work with the domain, codomain and range of a bijection?”;
        exam provenance: UCLES 1980 Q[''Q3''] [9202/2]'
      validation_status: SUGGESTED
    title: understand the terms function, domain, range, one-one function, inverse function and composition
      of functions
  - code: 1.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Domain/codomain/range/bijective vocabulary; range of f and of g∘f; bijectivity <-> inverse
        existence. phi/psi cycle extends beyond P1 routine.
      rationale: 'Canonical UGM title: “Can we work with the domain, codomain and range of a bijection?”;
        exam provenance: UCLES 1980 Q[''Q3''] [9202/2]'
      validation_status: SUGGESTED
    title: identify the range of a given function in simple cases, and find the composition of two given
      functions condition that a composite function
  - code: 1.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Domain/codomain/range/bijective vocabulary; range of f and of g∘f; bijectivity <-> inverse
        existence. phi/psi cycle extends beyond P1 routine.
      rationale: 'Canonical UGM title: “Can we work with the domain, codomain and range of a bijection?”;
        exam provenance: UCLES 1980 Q[''Q3''] [9202/2]'
      validation_status: SUGGESTED
    title: determine whether or not a given function is one-one, and find the inverse of a one-one function
      in simple cases
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1980 Q['Q3'] [9202/2]
task: T-UGM-IMPORT-2
---

# Can we work with the domain, codomain and range of a bijection?

## Question

1. The function \(f\) from \(\mathbb{R}\) to \(\mathbb{R}\) is given by \(f: x\mapsto x^2+2x+2\). Find the range of \(f\), and state, with a reason, whether or not \(f\) is [bijective](https://undergroundmathematics.org/glossary/bijective).  The range of \(f\) is denoted by \(S\), and the function \(g\) from \(S\) to \(\mathbb{R}\) is given by \(g: x\mapsto 1/x\). State the image of \(x\) under the composite function \(g\circ f\), and give the range of this composite function.
2. \(R'\) denotes the set of real numbers excluding \(0\) and \(1\). Functions \(\phi\) and \(\psi\) from $ R’$ to \(R'\) are given by \[\phi : x\mapsto \frac{1}{1-x}, \qquad \qquad \psi : x \mapsto 1-x.\]  Give in a similar form the definitions of \(\phi ^{-1}\) and \((\phi \circ \psi)^{-1}\).

## Suggestion

To explain, the symbol \(\mathbb{R}\) denotes the set of all real numbers, that is, the set of all numbers on the number line.

We’re definitely going to need to understand the word *bijective* for this question. Click on the link in the question above for a careful explanation.

The notation \(f \circ g\) means ‘the function \(g\) followed by the function \(f\)’, or ‘\(f\) composed with \(g\)’.

Could we complete the square on \(x^2+2x+2\)?

## Solution

In the context of this question, we could say a function \(f\) is *bijective* if and only if

1. it is \(one-one,\) and
2. its codomain equals its range.

So for \(f\) to be a bijection, no horizontal line cuts the graph of \(y = f(x)\) more than once, and if \(k\) is a value in the codomain, then the horizontal line \(y = k\) cuts \(y = f(x)\) exactly once. In this case, we say \(f\) is ‘one-one and onto’.

We can rewrite the definition of \(f\) so that it will be easier to see the range. Completing the square, we have \[f: x\mapsto (x+1)^2 +1.\] Now \((x+1)^2\) can take every value greater than or equal to \(0\), so \(f(x)\) must be greater than or equal to \(1\).

Therefore the range of \(f\) is the set of all real numbers greater than or equal to \(1\), which can be written as \(\{f(x) \in \mathbb{R}, f(x) \geq 1\}\).

Since \(f(0) = f(-2)\), \(f\) is not one-one, and therefore not bijective.

We know by the definition of \(g\) that

\[g\circ f:x \mapsto \frac{1}{f(x)} = \frac{1}{x^2+2x+2},\]

which is the image of \(x\) under \(g \circ f\). We don’t have to worry about the denominator being zero since \(f(x) > 0\).

Since \(f(x) \geq 1\), we have \(\dfrac{1}{f(x)} \leq 1\). Also, since \(f(x)>0\), we have \(\dfrac{1}{f(x)} > 0\).

The function \(g \circ f\) therefore takes no value less than or equal to \(0\) or greater than \(1\).

Does it take every value in the interval from 0 to 1?

Take any \(y\) with \(0 < y \leq 1\). Let \(w = \dfrac{1}{y}\), so \(w \geq 1\). Then \(f(z)=w\) for some \(z\) (since \(f\) takes every value greater than or equal to \(1\)), and so \(g \circ f(z) = y\).

Hence the range of \(g \circ f\) is \(0 < g \circ f(x) \leq 1\).

Or we could say that to find the range of a function, we can draw a graph of the function, and ask, ‘What are the possible \(y\)-values?’

1. \(R'\) denotes the set of real numbers excluding \(0\) and \(1\). Functions \(\phi\) and \(\psi\) from $ R’$ to \(R'\) are given by \[\phi : x\mapsto \dfrac{1}{1-x}, \qquad \qquad \psi : x \mapsto 1-x.\]

Give in a similar form the definitions of \(\phi ^{-1}\) and \((\phi \circ \psi)^{-1}\).

If \(y=\dfrac{1}{1-x}\), can we make \(x\) the subject here? We have \(y-yx=1\), and so \(x=1-\dfrac{1}{y}\). Therefore \[\phi ^{-1}: x\mapsto 1-\frac{1}{x}.\]

Check: does

\((\phi^{-1} \circ \phi)(x)=x\)

? If not, we’ve made a mistake! We have

\[\begin{align*} (\phi^{-1} \circ \phi)(x) &= \phi^{-1} ( \phi(x))\\ &= \phi^{-1} \left(\dfrac{1}{1-x}\right) \\ &= 1-\frac{1}{\left(\dfrac{1}{1-x}\right)} \\ &= 1-(1-x) \\ &= x. \end{align*}\]

In order to find \((\phi \circ \psi)^{-1}\) we first need to find \(\phi \circ \psi\). We have \[\phi (\psi(x)) = \phi(1-x)=\frac{1}{1-(1-x)}=\frac{1}{x}.\] This is clearly a self-inverse function, so \[(\phi \circ \psi)^{-1}:x \mapsto \frac{1}{x}.\]

Alternatively, we could use the fact that

\((\phi \circ \psi)^{-1} = \psi^{-1} \circ \phi^{-1}\)

, and the observation that

\(\psi\)

 is self-inverse (it is its own inverse), so

\[\begin{align*} (\phi \circ \psi)^{-1}(x) &= \psi^{-1}\left(\phi^{-1}(x)\right) \\ &= \psi^{-1} \left(1 - \dfrac{1}{x}\right) \\ &= 1 - \left(1 - \dfrac{1}{x}\right) \\ &= \dfrac{1}{x}. \end{align*}\]
