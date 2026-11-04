---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-functions/inequality-flip-flop
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-functions
- type/package-of-problems
- level/developing
resource_identity:
  ugm_id: inequality-flip-flop
  station: thinking-about-functions
  station_title: Thinking about Functions
  resource_type_id: 5
  resource_type_label: Package of problems
  level: Developing
  ref: 5356
  old_site_id: F1_RT7_1
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: thinking-about-functions
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-functions
    validation_status: SUGGESTED
  spec_points:
  - code: E2.6.1
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: How applying functions to inequalities affects the sign — representing and interpreting
        inequalities; the E2.6.1 register.
      rationale: 'Canonical UGM title: “Inequality flip-flop”'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-19
assets:
- path: https://undergroundmathematics.org/thinking-about-functions/inequality-flip-flop/images/xsquared.png
  kind: figure
- path: https://undergroundmathematics.org/thinking-about-functions/inequality-flip-flop/images/oneoverx.png
  kind: figure
interactive:
- src: //www.geogebratube.org/material/iframe/id/GTQAarWA/width/598/height/396/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
- src: //www.geogebratube.org/material/iframe/id/GTQAarWA/width/598/height/396/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
import_note: question well prepended (was not among crawled sections)
---

# Inequality flip-flop

> Excerpt: The resource is intended to support students’ understanding of algebraic manipulation by encouraging them to think in terms of functions. In particular, how applying certain functions to inequalities affects the inequality sign.

## Question

Use the interactivity below to find values of \(a\) and \(b\) for which

- \(a\) is less than \(b\) and \(f(a)\) is less than \(f(b).\)
- \(a\) is less than \(b\) but \(f(a)\) is greater than \(f(b).\)

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/GTQAarWA/width/598/height/396/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/GTQAarWA)

Here are some statements about the function \(f(x)\) in the graph above. In each case, decide if the statement is true. If it is not true, try to adapt it to make a true statement.

1. If \(-5<a<b<-3\) then \(f(a) < f(b).\)
2. If \(2.5 < a < b < 5\) then \(f(a) < f(b).\)
3. If \(-2.5 < a< b <2\) then \(f(a) > f(b).\)
4. If \(-2.5 < a < b < 3\) then \(f(a) > f(b).\)

Think about the statement “If \(-5<a<b<-3\) then \(f(a)<f(b)\)”.

This says that for every \(a\) and \(b\) between \(-5\) and \(-3\) where \(a\) is less than \(b\), the value of the function when \(x=a\) is less than the value of the function when \(x=b.\) Use the graph for \(x\) between \(-5\) and \(-3\) to make sense of this.

To decide that this statement is true, you need to be convinced that there are are no values of \(a\) and \(b\) where \(-5<a<b<-3\) but \(f(a)>f(b).\)

**How do we know if a statement is true?**

---

Now consider the following statements about real numbers \(a\) and \(b\) and some familiar functions. Try to sketch or visualise the graph of the functions as you think about the statements.

1. If \(a\) is less than \(b\), then \(a^{2}\) is less than \(b^{2}.\)
2. If \(a\) is less than \(b\), then \(a-5\) is less than \(b-5.\)
3. If \(a\) is less than \(b\), then \(3-2a\) is less than \(3-2b.\)
4. If \(a\) is less than \(b\), then \(\dfrac{1}{a}\) is greater than \(\dfrac{1}{b}.\)

If you think a statement is true or false for all \(a\) and \(b\), can you justify this using a graph?

If a statement may be true for some values of \(a\) and \(b\) and false for other values, can you form a true statement or statements by restricting the set of values for \(a\) and \(b\)?

## Warm-up

Can you think of examples of the following?

- a number less than \(3\) whose square is greater than \(9\)
- a number whose cube is larger than \(27\)
- a number whose reciprocal is smaller than \(\dfrac{1}{3}\)

One way to think about questions like these is to think about functions. Which functions are involved here and what do their graphs look like?

## Problem

Use the interactivity below to find values of \(a\) and \(b\) for which

- \(a\) is less than \(b\) and \(f(a)\) is less than \(f(b).\)
- \(a\) is less than \(b\) but \(f(a)\) is greater than \(f(b).\)

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/GTQAarWA/width/598/height/396/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/GTQAarWA)

Here are some statements about the function \(f(x)\) in the graph above. In each case, decide if the statement is true. If it is not true, try to adapt it to make a true statement.

1. If \(-5<a<b<-3\) then \(f(a) < f(b).\)
2. If \(2.5 < a < b < 5\) then \(f(a) < f(b).\)
3. If \(-2.5 < a< b <2\) then \(f(a) > f(b).\)
4. If \(-2.5 < a < b < 3\) then \(f(a) > f(b).\)

Think about the statement “If \(-5<a<b<-3\) then \(f(a)<f(b)\)”.

This says that for every \(a\) and \(b\) between \(-5\) and \(-3\) where \(a\) is less than \(b\), the value of the function when \(x=a\) is less than the value of the function when \(x=b.\) Use the graph for \(x\) between \(-5\) and \(-3\) to make sense of this.

To decide that this statement is true, you need to be convinced that there are are no values of \(a\) and \(b\) where \(-5<a<b<-3\) but \(f(a)>f(b).\)

**How do we know if a statement is true?**

<cm-block output="pdf"> <cm-chalk> How do we know if a statement is true? Think about the statement "If $-5<a<b<-3$ then $f(a)<f(b)$". This says that for every $a$ and $b$ between $-5$ and $-3$ where $a$ is less than $b$, the value of the function when $x=a$ is less than the value of the function when $x=b.$ Use the graph for $x$ between $-5$ and $-3$ to make sense of this. To decide that this statement is true, you need to be convinced that there are are no values of $a$ and $b$ where $-5<a<b<-3$ but $f(a)>f(b).$ </cm-chalk> </cm-block>

---

Now consider the following statements about real numbers \(a\) and \(b\) and some familiar functions. Try to sketch or visualise the graph of the functions as you think about the statements.

1. If \(a\) is less than \(b\), then \(a^{2}\) is less than \(b^{2}.\)
2. If \(a\) is less than \(b\), then \(a-5\) is less than \(b-5.\)
3. If \(a\) is less than \(b\), then \(3-2a\) is less than \(3-2b.\)
4. If \(a\) is less than \(b\), then \(\dfrac{1}{a}\) is greater than \(\dfrac{1}{b}.\)

If you think a statement is true or false for all \(a\) and \(b\), can you justify this using a graph?

If a statement may be true for some values of \(a\) and \(b\) and false for other values, can you form a true statement or statements by restricting the set of values for \(a\) and \(b\)?

## Things you might have noticed

From the graph above, we can see that for any \(a\) and \(b\) between \(-5\) and \(-3\), if \(a < b\) then we always have \(f(a) < f(b).\) In other words, as \(x\) increases, the value of \(f(x)\) increases. Therefore statement 1 is true.

**Statement 1**

If $ 2.5 < a < b < 5$ then \(f(a) < f(b).\)

The lowest point of the graph between \(x=2.5\) and \(x=5\) occurs when \(x=3.2.\) We say the graph has a ‘local minimum’ when \(x=3.2.\) This means that for \(x\) near \(3.2\) but less than \(3.2\), as \(x\) gets larger the value of \(f(x)\) decreases, but once \(x\) is larger than \(3.2\) the value of \(f(x)\) starts to increase again. There are some values of \(a\) and \(b\) between \(2.5\) and \(5\) for which \(a<b\) and \(f(a)<f(b)\) and others for which \(a<b\) but \(f(a)>f(b)\), so statement 2 is not true. One way to modify statement 2 to give a true statement is to restrict the set of values for \(a\) and \(b\) to, say, \(3.2< a < b < 5.\)

**Statement 2**

The graph shows that as \(x\) increases from \(-2.8\) to \(2\), the value of \(f(x)\) decreases. Therefore statement 3 is true. Also, as \(x\) increases from \(2\) to \(3\) the value of \(f(x)\) decreases, but does this mean that statement 4 is true?

This tells us that we need to look at behaviour around critical points, such as the asymptote at \(x=2\) where the function isn’t defined, as well as looking at whether the function is increasing or decreasing.

**Statements 3 and 4**

As the function \(f(x)=x^2\) only increases for \(x>0\), statement 5 is true if \(a\) and \(b\) are both positive. Otherwise the statement could be false and we’d need to know more about \(a\) and \(b.\) For example, if \(a=-5\) and \(b=-2\) then \(f(a)>f(b)\) whereas if \(a=-5\) and \(b=6\) then \(f(a)<f(b).\)

> [figure: Graph of y=x^2 — `https://undergroundmathematics.org/thinking-about-functions/inequality-flip-flop/images/xsquared.png`] (image not included in the text import; path of record).

**Statement 5**

What do the graphs of \(y=x-5\) and \(y=3-2x\) tell you about increasing and decreasing behaviour? Can you describe what happens for any function of the form \(f(x)=mx+c\)?

**Statements 6 and 7**

The function \(f(x)=\tfrac{1}{x}\) is decreasing for \(x<0\) and for \(x>0\), so if \(a\) and \(b\) are both negative or both positive and \(a<b\), we have \(\tfrac{1}{a} > \tfrac{1}{b}.\) However, if \(a=-2\) and \(b=3\) then \(\tfrac{1}{a} < \tfrac{1}{b}.\) We need to know more about \(a\) and \(b\) if want to know how \(\tfrac{1}{a}\) and \(\tfrac{1}{b}\) are related.

> [figure: Graph of $y=\dfrac{1}{x}$ — `https://undergroundmathematics.org/thinking-about-functions/inequality-flip-flop/images/oneoverx.png`] (image not included in the text import; path of record).

**Statement 8**
