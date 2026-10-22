---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r6735
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r6735
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6735
  old_site_id: Q1059
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
  - code: 1.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: f⁻¹ and ff for f:x->1/(x+1); solve f=f⁻¹ and f=ff (both reduce to x^2+x-1=0). f=f⁻¹ invites
        the y=x mirror-line reading.
      rationale: 'Canonical UGM title: “For which $x$-values does a function equal its inverse?”; exam
        provenance: UCLES 1979 Q[''Q10''] [986/1]'
      validation_status: SUGGESTED
    title: determine whether or not a given function is one-one, and find the inverse of a one-one function
      in simple cases
  - code: 1.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: f⁻¹ and ff for f:x->1/(x+1); solve f=f⁻¹ and f=ff (both reduce to x^2+x-1=0). f=f⁻¹ invites
        the y=x mirror-line reading.
      rationale: 'Canonical UGM title: “For which $x$-values does a function equal its inverse?”; exam
        provenance: UCLES 1979 Q[''Q10''] [986/1]'
      validation_status: SUGGESTED
    title: identify the range of a given function in simple cases, and find the composition of two given
      functions condition that a composite function
  - code: 1.2.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: f⁻¹ and ff for f:x->1/(x+1); solve f=f⁻¹ and f=ff (both reduce to x^2+x-1=0). f=f⁻¹ invites
        the y=x mirror-line reading.
      rationale: 'Canonical UGM title: “For which $x$-values does a function equal its inverse?”; exam
        provenance: UCLES 1979 Q[''Q10''] [986/1]'
      validation_status: SUGGESTED
    title: illustrate in graphical terms the relation between Sketches should include an indication of
      the mirror a one-one function and its inverse line
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1979 Q['Q10'] [986/1]
task: T-UGM-IMPORT-2
---

# For which $x$-values does a function equal its inverse?

## Question

A function \(f\) is defined by \(f:x\rightarrow \dfrac{1}{x+1}\). Write down in similar form expressions for \(f^{-1}\) and \(ff\).

It is required to find the values of \(x\) for which \((i)\) \(f=f^{-1}\), \((ii)\) \(f=ff\). Show that, in each case, the values of \(x\) are given by the equation \[ x^2+x-1=0.\]

## Suggestion

A function \(f\) is defined by \(f:x\rightarrow \dfrac{1}{x+1}\). Write down in similar form expressions for \(f^{-1}...\)

How can we find the [inverse function](https://undergroundmathematics.org/glossary/inverse-function)? What happens if we make \(x\) the subject of \(y=f(x)\)?

… and \(ff\).

Would it help to view the [composite function](https://undergroundmathematics.org/glossary/composite-function) \(ff(x)\) as \(f(f(x))\)?

It is required to find the values of \(x\) for which \((i)\) \(f=f^{-1}\), \((ii)\) \(f=ff\).

Show that, in each case, the values of \(x\) are given by the equation \[x^2+x-1=0.\]

From the above, we should now know \(f(x)\), \(f^{-1}(x)\) and \(ff(x)\). Can we form equations using these?

## Solution

To find the [inverse of a function](https://undergroundmathematics.org/glossary/inverse-function) we can write \(y=f(x)\) and rearrange to make \(x\) the subject. This gives

\[\begin{align*} y &= \dfrac{1}{x+1}\\ x+1 &= \dfrac{1}{y}\\ x &= \dfrac{1}{y} - 1\\ &= \dfrac{1-y}{y} \end{align*}\]

Replacing \(y\) with \(x\) in the right hand side, we obtain the inverse function \[f^{-1}:x\rightarrow\frac{1-x}{x}.\]

… and \(ff\).

The [composite function](https://undergroundmathematics.org/glossary/composite-function) of \(f\) with itself can be found by ‘replacing the \(x\) in \(f(x)\) with \(f(x)\)’. This gives \[f\bigl( f(x) \bigr) = \dfrac{1}{ \left( \dfrac{1}{x+1} \right)+1 }.\]

We can now simplify by multiplying top and bottom by \(x+1\), yielding

\[\begin{align*} ff(x) &= \dfrac{1}{ \left( \dfrac{1}{x+1} \right)+1 } \times \dfrac{x+1}{x+1} \\ &= \dfrac{x+1}{1 + (x + 1)} \\ &= \dfrac{x+1}{x+2}. \end{align*}\]

Our solution then reads \[ff:x\rightarrow \frac{x+1}{x+2}.\]

Using the result from above, we set \(f(x) = f^{-1}(x)\), giving

\[\begin{align*} \dfrac{1}{x+1}&=\dfrac{1-x}{x}\\ 1&=\dfrac{(1-x)(1+x)}{x}\\ x&=1-x^2\\ x^2+x-1&=0 \end{align*}\]

as required.

Similarly, setting \(f(x) = ff(x)\) we have

\[\begin{align*} \dfrac{1}{x+1} &= \dfrac{x+1}{x+2}\\ 1&=\dfrac{(x+1)^2}{x+2}\\ x+2 &= (x+1)^2\\ x+2 &=x^2+2x+1\\ x^2+x-1&=0. \end{align*}\]

The question does not require us to solve this equation for \(x\), but we could do so using the [quadratic formula](https://undergroundmathematics.org/glossary/quadratic-equation-solution). We have

\[\begin{align*} x^2+x-1&=0\\ x &= \dfrac{-1 \pm \sqrt{1^2 - 4 \times 1 \times -1}}{2 \times 1} \\ &= \dfrac{-1 \pm \sqrt{5}}{2} . \end{align*}\]
