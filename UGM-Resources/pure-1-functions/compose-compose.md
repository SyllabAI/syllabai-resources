---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/compose
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/package-of-problems
- level/developing
resource_identity:
  ugm_id: compose
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 5753
  old_site_id: F2_RT7_1
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
      evidence: Largest domain/range for A-D, then decompose composite functions — composition fluency
        package (pattern exemplar).
      rationale: 'Canonical UGM title: “Compose!”; cross-mapped primary pick of record (UGM-Enrichment
        perSpecPoint primaryPick, T-UGM-MODE1-2 (syllabai-resources))'
      validation_status: SUGGESTED
      primaryPick: true
    title: identify the range of a given function in simple cases, and find the composition of two given
      functions condition that a composite function
  - code: 1.2.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Largest domain/range for A-D, then decompose composite functions — composition fluency
        package (pattern exemplar).
      rationale: 'Canonical UGM title: “Compose!”'
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
- path: https://undergroundmathematics.org/combining-functions/compose/images/oneoverx.png
  kind: figure
---

# Compose!

> Excerpt: Students are given four functions and asked to compose them to create the given set of six new functions.

## Problem

Part of the definition of a function is the specification of its [domain](https://undergroundmathematics.org/glossary/domain). The choice of domain may affect the [range](https://undergroundmathematics.org/glossary/range-of-a-function) of the function.

| \(A(x)= x^2-2\) | \(B(x)= 2x+4\) |
| --- | --- |
| \(C(x)= \dfrac{1}{x}\) | \(D(x)= \sqrt{x+2}-2\) |

 What is the largest possible domain for each of the functions

\(A\)

 to

\(D\)

 and what is the corresponding range?

The functions above have been composed in some way to make the following new functions:

| \(f(x)=\dfrac{2}{x}+4\) | \(f(x)=4x^2+16x+14\) |
| --- | --- |
| \(f(x)=\dfrac{1}{2x^2}\) | \(f(x)=x-2\) |
| \(f(x)=\dfrac{1}{4x+12}\) | \(f(x)=x\) |

Can you work out which functions have been composed and in what order to make the new functions?

What are the domain and range for each composition of functions above?

Note that the *composition* might only be defined on a smaller domain than is possible for the function \(f(x)\).

Looking at each composition in turn,

- Can you match it with original functions that have similar features?
- Can you eliminate any of the original functions that cannot possibly be involved in creating it?

**Prompting questions**

## Solution

To find the domain and range for a function, it sometimes helps to sketch its graph.

We can sketch the graph of \(y=x^2\), and \(y=A(x)\) is a translation of it—in which direction?

\(A(x)\) can be evaluated for any input \(x\) so the domain of \(A(x)\) is all real numbers, which can be written as \(x\in\mathbb{R}\). The range is \(A(x)\geq-2\).

**Function \(A(x)= x^2-2\)**

The domain and range are both the full set of real numbers, \(\mathbb{R}\).

**Function \(B(x)= 2x+4\)**

> [figure: graph of y=1 over x — `https://undergroundmathematics.org/combining-functions/compose/images/oneoverx.png`] (image not included in the text import; path of record).

Allowing \(x=0\) would produce an undefined result so we need to restrict the domain to \(x\in\mathbb{R}, x\neq0\). No input value can achieve \(C(x)=0\) so the range is also restricted to the real numbers excluding \(0\).  but it's now fixed.

 This version used to make the image crash into the bottom of the box in PDF

 This version works in both outputs but wastes some space in HTML <cm-columns> <cm-column> Allowing $x=0$ would produce an undefined result so we need to restrict the domain to $x\in\mathbb{R}, x\neq0$. No input value can achieve $C(x)=0$ so the range is also restricted to the real numbers excluding $0$. </cm-column> <cm-column> <cm-image url="images/oneoverx.png" alt-text="graph of y=1 over x" caption=""/> </cm-column> </cm-columns>

**Function \(C(x)= \dfrac{1}{x}\)**

> [figure: graph of root x+2 subtract 2 — `https://undergroundmathematics.org/combining-functions/compose/images/rootxplus2minus2.png`] (image not included in the text import; path of record). The graph of this function is a translation of \(y=\sqrt{x}\).

The square root is undefined when \(x+2<0\) so the domain of this function is \(x\ge-2\).

We can evaluate \(D(-2)=-2\) and the square root function always increases as \(x\) increases, so the range is \(D(x)\ge-2\).

 This version used to crash the box in PDF. It wastes less space in HTML but chalk doesn't clear the float so I've had to de-chalk it

 This version works in both outputs but wastes some space in HTML <cm-columns> <cm-column> <cm-chalk> The graph of this function is a translation of $y=\sqrt{x}$. </cm-chalk> The square root is undefined when $x+2<0$ so the domain of this function is $x\ge-2$. We can evaluate $D(-2)=-2$ and the square root function always increases as $x$ increases, so the range is $D(x)\ge-2$. </cm-column> <cm-column> <cm-image url="images/rootxplus2minus2.png" alt-text="graph of root x+2 subtract 2" caption=""/> </cm-column> </cm-columns>

**Function \(D(x)= \sqrt{x+2}-2\)**

Note that the *composition* might only be defined on a smaller domain than is possible for the function \(f(x)\).

We can see that this contains \(\dfrac{1}{x}\), suggesting function \(C\), and the form “\(something+4\)” hints at \(B\) being involved. \(B\left(\dfrac{1}{x}\right)=\dfrac{2}{x}+4\), giving us \[f(x)= \frac{2}{x}+4= BC(x).\]

The notation \(BC(x)\) is used to mean \(B\bigl(C(x)\bigr)\).

Using \(C(x)\) means the domain is \(x\neq0\) and since \(C(x)\neq0\) we cannot achieve 4 from \(BC(x)\). Hence the range is \(BC(x)\neq 4\). Can you illustrate this with a sketch of \(y=BC(x)\)?

**1.\(\quad f(x)=\dfrac{2}{x}+4\)**

We require a quadratic which leads us straight to \(A\). We don’t want any fractions, so we’re probably going to compose it with the linear function \(B\). Notice that we want the coefficient of \(x^2\) to be \(4\) which we could achieve by squaring \(B\).

We try \((2x+4)^2=4x^2+16x+16\) and see that \[f(x) = 4x^2+16x+14 = AB(x) .\]

We can allow any input value, hence the domain is \(\mathbb{R}\). As \(B(x)\in \mathbb{R}\), it follows that \(AB(x)\) has the same range as \(A(x)\), so \(AB(x)\geq-2\).

**2.\(\quad f(x)={4x^2~+~16x~+~14}\)**

The fraction means we probably need to use \(C\), and the \(x^2\) indicates \(A\), but \(CA(x)=\dfrac{1}{x^2-2}\). We need the coefficient of \(x^2\) in the denominator to be \(2\), so first applying \(B\) before \(C\) will do this and helpfully it will also remove the unwanted \(-2\).

Since \(BA(x)=2(x^2-2)+4=2x^2\) we have \[f(x) =\frac{1}{2x^2} =CBA(x) .\]

To determine the domain and range we note that for \(A\) (which is applied first) the domain is the real numbers and the range is \(A(x)\geq-2\). This becomes the input of \(B\) so \(BA(x)\geq0\). The domain of \(C\) excludes \(x=0\) so we must exclude that output from \(B\). We do this by excluding the input of \(-2\). This means that the domain of \(CBA(x)\) is \(x\ne-2\) and it has range \(CBA(x)>0\).

**3.\(\quad f(x)=\dfrac{1}{2x^2}\)**

Notice that the function \(\sqrt{x^2}\) gives the *positive* square root, so in order for \(DA(x)\) to equal \(x-2\) as required, \(x\) must be non-negative.

This gives \(DA(x)\) the restricted domain of \(x\ge0\). We need to check whether the domain is further restricted by the functions \(D\) and \(A\). The domain of \(A\) is \(\mathbb{R}\) which includes all of \(x\ge0\). Even with the restricted domain, the range is \(A(x) \ge-2\). This becomes the input of \(D\) and matches its domain, so \(DA\) has the same range as \(D\).

The composed function therefore has domain \(x\ge0\) and range \(DA(x) \ge-2\).

 We notice the similarity to the function

\(A(x)\)

, but

\(A\)

 has a quadratic term—how could we cancel that out?

\(D\)

 contains the square root of

\(x+2\)

, so if we apply

\(D\)

 to the output of

\(A\)

 we get

\[\begin{align*} DA(x)&=\sqrt{A(x)+2}-2\\ &=\sqrt{x^2-2+2}-2\\ &=\sqrt{x^2}-2\\ &=|x|-2 . \end{align*}\]

**4.\(\quad f(x)=x-2\)**

We might look at this and think about function \(C\), but we need the input to this to be \(4x+12\) which doesn’t immediately look like any of the other functions.

It might be a good idea to change tack and think what we can generate by composing some of the functions with themselves.

1. Since \(A(x)\) is quadratic \(A^2(x)\) will be quartic. So this is not going to help!  The notation \(A^2(x)\) is used to mean \(A\bigl(A(x)\bigr)\).
2. \(B^2(x)=B(2x+4)=2(2x+4)+4=4x+12\)  That is what we need as input for \(C\) so \[f(x) =\frac{1}{4x+12} =CB^2(x) .\]

The domain and range of \(B\) are the real numbers, \(\mathbb{R}\), but the domain of \(C\) excludes zero so we must exclude \(4x+12=0\) from the input of the composition. Hence its domain is \(x\neq-3\) and its range is \(CB^2(x)\neq0\).

**5.\(\quad f(x)=\dfrac{1}{4x+12}\)**

This is another case of a function composed with itself.

\[f(x) =x =\dfrac{1}{\left(\frac{1}{x}\right)} =C^2(x)\]

We might suppose that the domain and range of \(f(x)=x\) would be the real numbers, but because it was created by composing \(C(x)\) we have to exclude \(x=0\) from both.

Does this in fact mean that \(C^2(x)\) is not the same as the function \(f(x)=x\)?

**6.\(\quad f(x)=x\)**
