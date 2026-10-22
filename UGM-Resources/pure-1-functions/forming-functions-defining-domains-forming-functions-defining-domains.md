---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/forming-functions-defining-domains
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/building-blocks
- level/introducing
resource_identity:
  ugm_id: forming-functions-defining-domains
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Introducing
  ref: 7511
  old_site_id: F2_RT2_2
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
      evidence: Function = domain + rule + range; choose domains, state ranges, sketch; largest possible
        domain. Canonical 1.2.1 builder.
      rationale: 'Canonical UGM title: “Forming functions — defining domains”; cross-mapped primary pick
        of record (UGM-Enrichment perSpecPoint primaryPick, T-UGM-MODE1-2 (syllabai-resources))'
      validation_status: SUGGESTED
      primaryPick: true
    title: understand the terms function, domain, range, one-one function, inverse function and composition
      of functions
  - code: 1.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Function = domain + rule + range; choose domains, state ranges, sketch; largest possible
        domain. Canonical 1.2.1 builder.
      rationale: 'Canonical UGM title: “Forming functions — defining domains”'
      validation_status: SUGGESTED
    title: identify the range of a given function in simple cases, and find the composition of two given
      functions condition that a composite function
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/forming-functions-defining-domains/images/functions3.svg
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/forming-functions-defining-domains/images/combinedafunctions.svg
  kind: figure
---

# Forming functions — defining domains

> Excerpt: For each rule, define several different functions by choosing different domains. How does the choice of domain affect the range of the resulting function?

## Problem

To define a function we need a set of inputs (called the [domain](https://undergroundmathematics.org/glossary/domain)) and some sort of rule for turning inputs into outputs. The set of outputs is called the [range](https://undergroundmathematics.org/glossary/range-of-a-function) of the function.

Here are some rules which tell us what will happen to a given input value, \(x\).

> [figure: rule A x maps to x squared minus 2, rule B x maps to x minus x cubed, rule C x maps to 4 over x squared minus 4, rule D x maps to the square root of x plus 2 — `https://undergroundmathematics.org/combining-functions/forming-functions-defining-domains/images/functions3.svg`] (image not included in the text import; path of record).

For each rule,

- Define a function by choosing a domain. Now define another function by choosing a different domain.
- For each function you have defined, state the corresponding range of the function.
- Sketch graphs of the functions you have defined.

For each rule,

- What is the largest possible domain you can define within the real numbers?
- What is the smallest possible domain that will define a function with the largest possible range?

## Things you might have tried

There are many possible functions that you could define in each case. We will illustrate some of these ideas using rule \(A.\)

We could define a function using rule \(A\) and letting \(x\) be any real number. We could write this function as \[A : x \mapsto x^2-2, \quad x\in \mathbb{R}.\] The range is all real numbers greater than or equal to \(-2\), which we can write as \(A(x)\in \mathbb{R}\) with \(A(x) \geq -2\).

We could also define a function by restricting \(x\) to be a real number that is greater than or equal to \(1\) but less than \(4\). We could write this as \[A : x \mapsto x^2-2, \quad x\in \mathbb{R}, \; 1 \leq x <4.\] This time, the range is \(A(x)\in \mathbb{R},\) \(-1 \leq A(x) < 14\).

Alternatively, we could restrict \(x\) to being an integer greater than \(-3\), which would give the following function \[A : x \mapsto x^2-2, \quad x\in \mathbb{Z},\; x> -3.\] For this third function, \(A(x)\in \mathbb{Z}\), with \(A(x)\) always \(2\) less than a square number, i.e. \(A(x) \in \{ -2, -1, 2, 7, 14, 23, \ldots\}\).

> [figure: Three graphs of A(x) for different domains. The first is a simple parabola, the second is a section, and the third is a set of points described on the parabola. — `https://undergroundmathematics.org/combining-functions/forming-functions-defining-domains/images/combinedafunctions.svg`] (image not included in the text import; path of record).

Note the open and closed circles at the ends of the line in the second graph, indicating whether or not the end point is included in the domain.

**Sketch graphs**

For each rule,

- What is the function with the largest possible domain within the real numbers?

Rules \(A\) and \(B\) are defined for all real inputs, so the largest possible domain would be, for instance, \[A: x \mapsto x^2-2, \quad x\in \mathbb{R}.\]

In contrast, there are values of \(x\) for which rules \(C\) and \(D\) are undefined. For instance the largest possible domain of \(C\) would be, \[C: x\mapsto \dfrac{4}{x^2-4}, \quad x\in \mathbb{R}, \; x\neq \pm2.\]

For each rule,

- What is the smallest possible domain that will define a function with the largest possible range?

Thinking about our three suggested functions for \(A\) above, we found the ranges were as follows.

| Function | Domain | Range |
| --- | --- | --- |
| 1 | \(x\in \mathbb{R}\) | \(A(x)\in \mathbb{R}\), \(A(x)\geq -2\) |
| 2 | \(x\in \mathbb{R}\), \(1 \leq x < 4\) | \(A(x)\in \mathbb{R}\), \(-1 \leq x < 14\) |
| 3 | \(x\in \mathbb{Z}\), \(x > -3\) | \(A(x) \in \{ -2, -1, 2, 7, 14, 23, \ldots\}\) |

Out of these three, function 1 has the largest range. Its range includes all the values in the other two ranges and other values too.

In the case of rule \(A\), the largest possible range results from the function with the largest possible domain.

Is it true in general that if we make the domain of a function as large as possible, we also make the range as large as possible?

But can we obtain the same range with a smaller domain?

For function 1, it is possible to find two different values of \(x\) which give the same value of \(A(x)\), for example, \(A(-1)=A(1)\). So we could remove one of these input values from the domain without changing the range.

We can restrict the domain of \(A(x)\) to be \(x\in \mathbb{R}\), \(x\geq 0\), and the range will still be \(A(x)\geq -2\), as required. What happens if we make the domain any smaller?

Another way would be to define \(A(x)\) for \(x\in \mathbb{R}\), \(x<-5\) or \(0\leq x \leq 5\). What would the graph of this function look like? What other domains could you have which still give you the same range?

Which of these ideas could be applied to functions which are defined using the other rules?

Are there any of the rules for which the only way to achieve the maximum possible range is to define it on the maximum possible domain? What could you say about such functions?

As we’ll see later, this idea of restricting the domain without limiting the range becomes important when we look at [making inverse functions](https://undergroundmathematics.org/combining-functions/making-inverse-functions).
