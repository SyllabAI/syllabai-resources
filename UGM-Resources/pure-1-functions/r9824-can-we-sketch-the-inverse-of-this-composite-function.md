---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/r9824
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- combining-functions
- type/review-question
resource_identity:
  ugm_id: r9824
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 9824
  old_site_id: Q1025
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
  - code: 1.2.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Define fg and f⁻¹; state the relationship between the graphs of f and fg and of f and
        f⁻¹ (mirror line); prove hf is not one-one. ln vocabulary is P2/P3 in CIE.
      rationale: 'Canonical UGM title: “Can we sketch the inverse of this composite function?”; exam provenance:
        UCLES 1988 Q[''Q16''] [9205/1 and 9206/1]; cross-mapped primary pick of record (UGM-Enrichment
        perSpecPoint primaryPick, T-UGM-MODE1-2 (syllabai-resources))'
      validation_status: SUGGESTED
      primaryPick: true
    title: illustrate in graphical terms the relation between Sketches should include an indication of
      the mirror a one-one function and its inverse line
  - code: 1.2.3
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Define fg and f⁻¹; state the relationship between the graphs of f and fg and of f and
        f⁻¹ (mirror line); prove hf is not one-one. ln vocabulary is P2/P3 in CIE.
      rationale: 'Canonical UGM title: “Can we sketch the inverse of this composite function?”; exam provenance:
        UCLES 1988 Q[''Q16''] [9205/1 and 9206/1]'
      validation_status: SUGGESTED
    title: determine whether or not a given function is one-one, and find the inverse of a one-one function
      in simple cases
  - code: 1.2.2
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: Define fg and f⁻¹; state the relationship between the graphs of f and fg and of f and
        f⁻¹ (mirror line); prove hf is not one-one. ln vocabulary is P2/P3 in CIE.
      rationale: 'Canonical UGM title: “Can we sketch the inverse of this composite function?”; exam provenance:
        UCLES 1988 Q[''Q16''] [9205/1 and 9206/1]'
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
  exam_reference: UCLES 1988 Q['Q16'] [9205/1 and 9206/1]
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/r9824/images/sketch1.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r9824/images/sketch1.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/r9824/images/img-9824.png
  kind: figure
---

# Can we sketch the inverse of this composite function?

## Question

The functions

\(f\)

,

\(g\)

and

\(h\)

are defined by

\[\begin{align*} f &: x \mapsto \ln x, & \qquad \left(x\in\mathbb{R}^+\right), \\ g &: x \mapsto \frac{1}{x},& \qquad \left(x\in\mathbb{R}^+\right), \\ h &: x \mapsto x^2, &\quad \big(x\in\mathbb{R}\big). \end{align*}\]

1. Give definitions of each of the functions \(fg\) and \(f^{-1}\), and state, in each of the following cases, a relationship between the graphs of
  1. \(f\) and \(fg\),
  2. \(f\) and \(f^{-1}\).
2.

> [figure: Graph of y = hf(x) against x for positive x. The graph approaches infinity as x tends to zero and is increasing for larger x, with a minimum at (1, 0). — `https://undergroundmathematics.org/combining-functions/r9824/images/sketch1.png`] (image not included in the text import; path of record).

The diagram shows a sketch of the graph \(y=hf(x)\). State how the sketch shows that \(hf\) is not one–one, and prove that, if \(\alpha\) and \(\beta\), where \(0<\alpha <\beta\), are such that \(hf(\alpha)=hf(\beta)\), then \(\alpha=g(\beta)\).

1. The function \(\phi\) is defined by \[ \phi : x \mapsto hf(x),\qquad (0 < x \leq 1).\] Sketch the graph of \(\phi^{-1}\), and give an explicit expression in terms of \(x\) for \(\phi^{-1}(x)\).

## Suggestion

1. Give definitions of each of the functions \(fg\) and \(f^{-1}\) and state the relationship between the graphs of \(f\) and both \(fg\) and \(f^{-1}\).

The function \(\ln x\) is the [logarithm](https://undergroundmathematics.org/glossary/logarithm) to base \(e\) of \(x\).

Be careful with the order of your functions when composing them! If we take the function \(fg\), which order for \(f\) and \(g\) do we apply here?

Would a sketch help us describe the relationship between \(f\) and \(fg\)? And \(f\) and \(f^{-1}\)?

---

1. State how the sketch shows that \(hf\) is not one–one…

What does one–one mean? What do graphs of one–one functions look like?

---

…and prove that, if \(\alpha\) and \(\beta\), where \(0<\alpha <\beta\), are such that \(hf(\alpha)=hf(\beta)\), then \(\alpha=g(\beta)\).

What is the function \(hf\)?

How do we find the inverse of a function? And its graph?

What happens if we sketch \(y=\phi(x)\) on a graph, then the line \(y=x\)?

How do we find the inverse of a function using algebra?

Can we rearrange \(y=(\ln x)^2\) to make \(x\) the subject? What happens when we take the square root?

## Solution

For \(fg\): composing \(f\) and \(g\) we find \[fg(x) = f[g(x)]=\ln\left(\frac{1}{x}\right)=-\ln x.\]

For \(f^{-1}\): rearranging the formula \(y=\ln x\) to make \(x\) the subject we find \(x=e^y\), so \[f^{-1}(x)=e^x.\]

…(a) state a relationship between the graphs of \(f\) and \(fg\)

Reflection in the \(x\)–axis.

…(b) state a relationship between the graphs of \(f\) and \(f^{-1}.\)

Reflection in the line \(y=x\).

1.

> [figure: Graph of y = hf(x) against x for positive x. The graph approaches infinity as x tends to zero and is increasing for larger x, with a minimum at (1, 0). — `https://undergroundmathematics.org/combining-functions/r9824/images/sketch1.png`] (image not included in the text import; path of record).

The diagram shows a sketch of the graph \(y=hf(x)\). State how the sketch shows that \(hf\) is not one–one.

There are horizontal lines that cut the graph twice. In fact, for every positive \(y\)-value, there are two \(x\)-values that \(hf\) maps to the \(y\)-value.

… and prove that, if \(\alpha\) and \(\beta\), where \(0<\alpha <\beta\), are such that \(hf(\alpha)=hf(\beta)\), then \(\alpha=g(\beta)\).

The composition \(hf(x)=h(\ln x)=(\ln x)^2\).

\[\begin{align*} hf(\alpha) &= hf(\beta) \\ \Longrightarrow(\ln \alpha)^2 &= (\ln\beta)^2\\ \Longrightarrow \ln \alpha &= -\ln\beta. \end{align*}\]

We must have the minus sign here, since

\(\alpha \neq \beta\)

. Now we have

\[\begin{align*} \ln \alpha &= -\ln\beta = \ln\left(\frac{1}{\beta}\right)\\ \Longrightarrow \alpha &= \frac{1}{\beta}=g(\beta). \end{align*}\]

From the graph we see that if \(\alpha < \beta\), \(0<\alpha < 1\) and \(\beta > 1\).

\[\begin{align*} y &= (\ln x)^2 \\ \Longrightarrow -\sqrt{y} &= \ln x \end{align*}\]

(since

\(0 < x \leq 1\)

, we know

\(\ln x\)

is negative) and exponentiating both sides gives

\[\begin{align*} x &= e^{-\sqrt{y}} \end{align*}\]

Switching \(x\) and \(y\) we find that the inverse of \(\phi\) is \[\phi^{-1}(x)=e^{-\sqrt{x}}.\] We can find the graph of the inverse of a one-one function by reflecting in the line \(y=x\).

Below are the graphs of both \(y=\phi(x)\) and \(y=\phi^{-1}(x)\).

> [figure: Graph of the two curves phi of x and phi to the minus one of x. — `https://undergroundmathematics.org/combining-functions/r9824/images/img-9824.png`] (image not included in the text import; path of record).
