---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/combining-functions/translating-or-not
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
  ugm_id: translating-or-not
  station: combining-functions
  station_title: Combining Functions
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 6208
  old_site_id: F5_RT7_1
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
  - code: 1.2.5
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — P3c functions cross-map (generalisation lane 2) (cross-map-functions.json
        @ syllabai-experimental 4a592ed0)
      evidence: 'y=1/(x+a) and y=1/(x^2+a) parameter study: genuine translations vs lookalikes (non-example
        design; pattern exemplar).'
      rationale: 'Canonical UGM title: “Translating or not?”'
      validation_status: SUGGESTED
    title: understand and use the transformations of the Including use of the terms 'translation', 'reflection'
      graph of y = f( x ) given by and 'stretch' in describing transformations. Questions y = f( x ) +
      a , y = f( x + a ) , may involve algebraic or trigonometric functions, or other graphs with given
      features. y = a f( x ) , y = f( ax ) and simple combinations of these.
  mapped_date: '2026-10-23'
  mapper: cross-map-functions.json (P3c) @ syllabai-experimental 4a592ed0
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-2
assets:
- path: https://undergroundmathematics.org/combining-functions/translating-or-not/images/oneoveroneplusx.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/translating-or-not/images/oneoverxsquared.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/translating-or-not/images/oneoverxsquaredminus1.png
  kind: figure
- path: https://undergroundmathematics.org/combining-functions/translating-or-not/images/oneoverxsquaredplus1.png
  kind: figure
interactive:
- src: //www.geogebratube.org/material/iframe/id/dfhxYDYQ/width/592/height/420/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
- src: //www.geogebratube.org/material/iframe/id/j6rdeJuX/width/592/height/420/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Translating or not?

> Excerpt: This resource is designed to make students think about sketching graphs of unfamiliar functions, in particular reciprocals of familiar functions. They are asked to explain the behaviour of $y=\frac{1}{x^2+a}$ for different values of $a$.

## Problem

Sketch the graph of \(y=\dfrac{1}{x+a}\) for different values of \(a\). We suggest you start by trying the values \(a=0\), \(1\), \(-1\).

What do you notice?

Can you explain your observations?

---

Now sketch the graph of \(y=\dfrac{1}{x^2+a}\) for different values of \(a\), again starting with \(a=0\), \(1\), \(-1\).

What do you notice this time?

Can you explain why the graphs behave in this way?

## Suggestion

### Graph sketching

When sketching the graph of an unfamiliar function, it might help to think about the following.

- Where does the graph cross the axes?
- When is the function positive and when is it negative?
- Does it have any asymptotes?
- Is it increasing or decreasing?
- What happens as \(x\) gets very large?
- Is it related to any other graphs whose shape I know?

As a check, you could substitute in some values of \(x\) such as \(x=0\), \(1\), \(2\), \(-1\).

If you want a final check of your sketches, you could use a graphical calculator or software such as [Desmos](https://www.desmos.com/calculator). Alternatively, you could use the [Interactive graphs](https://undergroundmathematics.org/combining-functions/translating-or-not/interactive-graphs) section of this resource.

Now sketch the graph of \(y=\dfrac{1}{x^2+a}\) for different values of \(a\).

In addition to the above, you might find it helpful to first sketch the graph of \(y=x^2+a\) (for your chosen value of \(a\)). How does the graph of \(y=\dfrac{1}{f(x)}\) relate to the graph of \(y=f(x)\)?

## Things you may have noticed

> [figure: gtraph of 1 over x plus 1 — `https://undergroundmathematics.org/combining-functions/translating-or-not/images/oneoveroneplusx.png`] (image not included in the text import; path of record).

*\(y=\dfrac{1}{x+1}\)*

The graph of \(y=\dfrac{1}{x}\) is familiar. The family of graphs of \(y=\dfrac{1}{x+a}\) all look very similar.

Can you describe how they are related and the significance of the value \(a\)?

The shape of these graphs is very different for different values of \(a\). We can split our graphs into the cases \(a<0\), \(a=0\) and \(a>0\).

### When \(a=0\)

> [figure: graph when a equals zero — `https://undergroundmathematics.org/combining-functions/translating-or-not/images/oneoverxsquared.png`] (image not included in the text import; path of record).

*\(y=\dfrac{1}{x^2}\)*

This is the familiar graph \(y=\dfrac{1}{x^2}\).

We can visualise it as the reciprocal of \(y=x^2\).

- When \(x=0\), \(x^2=0\) so \(y=\frac{1}{x^2}\) has a vertical asymptote.
- As \(x\) increases, \(x^2\) increases so \(\frac{1}{x^2}\) decreases towards zero.
- The function is [even](https://undergroundmathematics.org/glossary/even-function) since the \(x\) value is squared, so the \(y\)-axis is a line of symmetry.

### When \(a<0\)

> [figure: graph when a is negative — `https://undergroundmathematics.org/combining-functions/translating-or-not/images/oneoverxsquaredminus1.png`] (image not included in the text import; path of record).

*\(y=\dfrac{1}{x^2-1}\)*

We might have expected \(y=\dfrac{1}{x^2-1}\) to be a translation of \(y=\dfrac{1}{x^2}\), but instead it does something much more interesting!

To understand this behaviour, we could think about the graph of \(y=x^2-1\) and what the reciprocal will look like, paying particular attention to where it crosses the \(x\)-axis. How, then, does the shape of \(y=\dfrac{1}{x^2+a}\) change as \(a\) takes negative values other than \(-1\)?

Another way to visualise this is to rewrite the function in terms of other functions whose graphs we are familiar with. Since \(a\) is negative, we could rewrite our function as \(y=\dfrac{1}{x^2-b^2}\) (where \(b^2=-a\)). Can you now rewrite this further?

We can factorise the denominator, \[y=\frac{1}{(x+b)(x-b)},\] and then expand this as [partial fractions](https://undergroundmathematics.org/glossary/partial-fractions). \[y=\frac{c}{x-b} - \frac{c}{x+b} \text{, where }c=\frac{1}{2b}\] The function can now be seen as the sum of two translated and scaled \(\dfrac{1}{x}\) functions. How can this help to understand the behaviour of our function as \(a\) varies?

**Solution**

### When \(a>0\)

> [figure: graph when a is positive — `https://undergroundmathematics.org/combining-functions/translating-or-not/images/oneoverxsquaredplus1.png`] (image not included in the text import; path of record).

*\(y=\dfrac{1}{x^2+1}\)*

Now, we find that there are no vertical asymptotes. Can you explain why by thinking about the graph of the quadratic \(y=x^2+1\)?

What if we rewrite this function as \(y=\dfrac{1}{x^2+b^2}\)? Can you expand this as we did above?

In this case, when \(a>0\), what happens to the graph as \(a\) takes different positive values?

---

### Joining them up

As \(a\) gets close to zero, can you visualise how each of these more interesting graphs will become closer and closer to the graph of \(y=\dfrac{1}{x^2}\)?

Use graphing software or the applets in the [next section](https://undergroundmathematics.org/combining-functions/translating-or-not/interactive-graphs) to view this transition.

## Interactive graphs

Here is the graph of \(y=\dfrac{1}{x+a}\); you can use the slider to change the value of \(a\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/dfhxYDYQ/width/592/height/420/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/dfhxYDYQ)

---

Here is the graph of \(y=\dfrac{1}{x^2+a}\); you can again use the slider to change the value of \(a\).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/j6rdeJuX/width/592/height/420/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/j6rdeJuX)
