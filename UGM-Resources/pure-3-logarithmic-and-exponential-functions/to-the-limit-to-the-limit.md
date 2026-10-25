---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/to-the-limit
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/scaffolded-task
- level/introducing
resource_identity:
  ugm_id: to-the-limit
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 3
  resource_type_label: Scaffolded task
  level: Introducing
  ref: 9151
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
  - code: 3.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "the first-principles chain for d/dx a^x closes with 'a special case': lim_{h->0}(a^h-1)/h = 1 exactly when a = e, the defining property of e (the differentiation vehicle is 1.7 of record)"
      rationale: "Canonical UGM title: To the limit"
      validation_status: SUGGESTED
    title: "understand the definition and properties of e Including knowledge of the graph of and ln x , including their relationship as inverse functions and their graphs"
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-10
---

# To the limit

> Excerpt: Using a series of statements, students are asked to put together a chain of reasoning to find the derivative of $a^x$. This leads on to looking at a special case of this derivative.

## Warm-up

What is the gradient of the chord \(AB\)?

Solution

\[\begin{align*} \text{gradient of } AB &= \dfrac{f(x+h) - f(x)}{x+h - x} \\ &=\dfrac{a^{x+h} - a^x}{h} \end{align*}\]

This expression gives us the gradient of \(AB.\) If \(h\) is small enough, then this also gives us an estimation of the gradient of \(f(x)\) at \(A.\)

How could we find the exact gradient at \(A\)? See the [gradient of \(a^x\)](https://undergroundmathematics.org/calculus-trig-log/to-the-limit/gradient-a-to-x) to find out.

## Gradient of $a^x$

We can find the gradient of a function by taking the limit of the gradient of a chord between \(x\) and \(x+h\) as \(h\) tends to \(0\).

\[f'(x) = \lim_{h \to 0} \dfrac{f(x+h)-f(x)}{h}\]

These statements and explanations can be used to create a chain of reasoning to find the gradient function of \(f(x) = a^x\). Sort the statements into a logical argument, either writing your own explanations of the steps, or turning over the hidden cards to use the explanations provided.

\(\displaystyle{f'(x) = \lim_{h \to 0} \left(a^x \left(\dfrac{a^{h} - 1}{h} \right) \right)}\)

The expression is factorised as \(a^x\) is a common factor.

\(\displaystyle{f'(x) = a^x \, \lim_{h \to 0} \left(\dfrac{a^{h} - a^0}{h} \right)}\)

As \(h \to 0\) the limit will give the gradient function at \(x = 0\).

\(\displaystyle{f'(x) = \lim_{h \to 0} \left(\dfrac{a^{x+h} - a^x}{h} \right)}\)

The expression in the limit gives the gradient of a chord between \(x = 0\) and \(x = h\) on \(f(x) = a^x\).

\(\displaystyle{f'(x) = a^x \, \lim_{h \to 0} \left(\dfrac{a^{h} - 1}{h} \right)}\)

This is the general formula for differentiating from first principles.

\(f'(x) = a^x \times f'(0)\)

This is an expression for the gradient of \(f(x) = a^x.\)

\(\displaystyle{f'(x) = \lim_{h \to 0} \left(\dfrac{f(x+h)-f(x)}{h} \right)}\)

As \(a^x\) is not affected by \(h\) it can be taken outside of the limit.

What does the final statement tell you about the gradient function of \(f(x)\)?

- What does the graph of \(f'(x)\) look like?

- How will the gradient function change as \(a\) changes?

- There is a special case of the gradient function of \(a^x\). What could it be? To find out more look at [A special case](https://undergroundmathematics.org/calculus-trig-log/to-the-limit/special-case).

## Solution

\(\displaystyle{f'(x) = \lim_{h \to 0} \left(\dfrac{f(x+h)-f(x)}{h} \right)}\)

This is the general formula for differentiating from first principles.

\(\displaystyle{f'(x) = \lim_{h \to 0} \left(\dfrac{a^{x+h} - a^x}{h} \right)}\)

This is an expression for the gradient of \(f(x) = a^x.\)

Remember the expression in the brackets gives the gradient of the chord between \(x\) and \(x+h\). Taking the limit as \(h \to 0\) gives us the gradient of the function at \(x\).

\(\displaystyle{f'(x) = \lim_{h \to 0} \left(a^x \left(\dfrac{a^{h} - 1}{h} \right) \right)}\)

The expression is factorised as \(a^x\) is a common factor.

\(\displaystyle{f'(x) = a^x \, \lim_{h \to 0} \left(\dfrac{a^{h} - 1}{h} \right)}\)

As \(a^x\) is not affected by \(h\) it can be taken outside of the limit.

The value of \(h\) is tending to \(0\), so any expressions not involving \(h\) are unaffected by this limiting process.

\(\displaystyle{f'(x) = a^x \, \lim_{h \to 0} \left(\dfrac{a^{h} - a^0}{h} \right)}\)

The expression in the limit gives the gradient of a chord between \(x = 0\) and \(x = h\) on \(f(x) = a^x\).

Think about how the expression \(\dfrac{a^h - a^0}{h}\) could be represented on the graph of \(f(x) = a^x\). What does it show?

\(f'(x) = a^x \times f'(0)\)

As \(h \to 0\) the limit will give the gradient function at \(x = 0\).

The final step implies that \(\displaystyle{\lim_{h \to 0} \dfrac{a^h - a^0}{h} = f'(0)}\).

This is not a simple limit to find as both the numerator and denominator tend to zero as \(h \to 0\). However, if we look at how we find \(f'(x)\) from first principles we should see some similarities. \[f'(x) = \lim_{h \to 0} \dfrac{f(x+h) - f(x)}{h} \text{ and } \lim_{h \to 0} \dfrac{a^h - a^0}{h}\] Instead of finding the gradient for a generic point \(x\), the limit on the right gives us the gradient for the specific point \(x = 0\), i.e. \(f'(0)\).

What does your final answer tell you about the gradient function of \(f(x)\)?

- What does the graph of \(f'(x)\) look like?

\[f'(x) = a^x \times f'(0)\]

The gradient function is the original function multiplied by a constant. This tells us the graph of

\(f'(x)\)

will look very similar to

\(f(x).\)

|  |  |
|---|---|

In fact it will be a transformation of the original function; a stretch in the \(y\) direction, scale factor \(f'(0).\) (Or a stretch in the \(x\) direction, scale factor \(\frac{1}{f'(0)}.\))

What do the graphs tell you about \(f'(0)\) when \(a = 2\) and when \(a = 4\)?

- How will the gradient function change as \(a\) changes?

We can see from the graphs above that as \(a\) gets bigger, \(f(x) = a^x\) gets steeper more quickly and so the gradient at zero will be larger. Therefore, as \(a\) gets bigger, \(f'(x)\) will also get steeper more quickly. What will happen as \(a\) gets smaller?

- There is a special case of the gradient function of \(a^x\). Can you think what it might be? To find out more look at [A special case](https://undergroundmathematics.org/calculus-trig-log/to-the-limit/special-case).

The gradient function itself could be steeper than the original function. This will happen if the stretch factor is bigger than one, i.e. \(f'(0) >1\). It could also be less steep, i.e. when \(f'(0) <1.\) This implies there will be a special case in the middle when \(f'(0) = 1\) and the gradient function and original function will be exactly the same!

## A special case

We have found that the gradient function of \(a^x\) can be written as \[f'(x) = a^x\times f'(0),\]

i.e. the gradient function is the function itself multiplied by a constant, and this constant is the gradient of

\(a^x\)

at

\(x = 0\)

. There will be a special case when

\(f'(0) = 1\)

as then the gradient function of

\(a^x\)

would be itself,

\(a^x\)

.

Before using the applet, look at the values given. Approximately what value do you think \(a\) will take to give \(f'(0) \approx 1?\)

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/UqaKEFMd/width/600/height/400/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/UqaKEFMd)

Use the slider to find the value of \(a\) when \(f'(0) \approx 1\).

Does the gradient function look as you expected?

Solution

We find that \(f'(0) \approx 1\) when \(a = 2.72\). This means that the gradient function becomes \(f'(x) = a^x\), so \(a^x\) and its gradient function are identical.

Of course this value of \(a\) is an approximation, but does it look familiar?

It turns out that the exact value of \(a\) for which the gradient function is the same as the original function is \(a = 2.7181...\), in fact it is \(a = e\). You have probably met \(e\) before as the exponential function \(e^x\) and as the base of natural logarithms. Here we have found that if \(f(x) = e^x\), then \(f'(x) = e^x\).

What about other values of \(a\)? To think about what \(f'(0)\) is for any value, you can look at [Differentiating exponentials](https://undergroundmathematics.org/chain-rule/differentiating-exponentials).
