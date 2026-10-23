---
created: 2026-10-24T04:45:46 (UTC +06:00)
source: https://undergroundmathematics.org/chain-rule/slippery-areas
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- chain-rule
- type/building-blocks
resource_identity:
  ugm_id: slippery-areas
  station: chain-rule
  station_title: Chain Rule & Integration by Substitution
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Introducing
  ref: 5441
  old_site_id: None
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: chain-rule
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: chain-rule
    validation_status: SUGGESTED
  spec_points:
  - code: 1.8.3
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-8 cross-map (cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd)"
      evidence: "definite-integral values recovered from area data under transformations, with the sqrt(x+5) evaluation reducing to an (x+5)^(3/2) antiderivative — (ax+b)^n technique inside definite-interval evaluation (the lane-7 routing recorded the 1.8 bearing)"
      rationale: "Canonical UGM title: \"Slippery areas\""
      validation_status: SUGGESTED
    title: "evaluate definite integrals"
  mapped_date: '2026-10-24'
  mapper: cross-map-integration.json (P3c lane 8) @ syllabai-experimental c04abfbd
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-8
---

# Slippery areas

> Excerpt: In this problem students are invited to explore what happens to areas under graphs when the graphs are stretched or translated. They are then asked to apply this way of thinking to some concrete examples.

## Problem

Take a look at this diagram.

The area of the blue region is \(53\) and the area of the orange region is \(125\).

Use this to explain why \[\int_{15}^{30}3f(2x-45)\,dx=67.\]

Now try to evaluate each of the following integrals.

1. \(\int_{-4}^{-2}\sqrt{x+5}\,dx\)

---

1. \(\int_{0.2}^{1.3}e^{2x}\,dx\)

3. $\int_{-\tfrac{\pi}{6}}^{\tfrac{\pi}{6}}\sin(3x +\tfrac{\pi}{2})dx$

Give some examples of other functions that you can integrate in this way.

## Suggestion

Here are some things to think about while looking at the diagram.

- What transformations of \(y=f(x)\) give us the other two graphs?

- What are the \(x\)-intercepts of \(y=f(x)\)?

- How long are the vertical edges of the orange region?

- How could you express the area of the orange region in terms of areas underneath the untransformed blue graph?

You may find it helpful to explore what happens when you move the sliders in this GeoGebra file.

Can you make the purple graph line up with the black graph?

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/Qe6WD7UP/width/595/height/397/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/Qe6WD7UP)

What could \(a\), \(b\) and \(c\) represent?

The purple graph is a transformation of \(y=f(x)\) and this transformation involves three parameters, \(a\), \(b\) and \(c\). The parameters are related to scaling and translation, but the numerical value of the parameter \(b\) is not necessarily the same as the value the graph is translated by along the \(x\)-axis.

You may like to explore what the translation is for the same value of \(b\) but different values of \(a.\)

What if we applied these ideas to the orange curve too?

Think about what is happening in these GeoGebra files as you move the sliders.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/suaSfYy8/width/596/height/399/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/suaSfYy8)

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/us6tga9e/width/596/height/399/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/us6tga9e)

How could this help you to evaluate the integrals?

## Solution

Take a look at this diagram.

The area of the blue region is \(53\) and the area of the orange region is \(125\).

Use this to explain why \(\int_{15}^{30}3f(2x-45)\,dx=67.\)

Stretching the blue region

We can view the graph of \(y=3f(2x-45)\) as a transformation of the graph \(y=f(x)\): thinking of it as a stretch parallel to the \(x\)-axis of scale factor \(\tfrac{1}{2}\) (effectively making the graph twice as narrow), then a translation parallel to the \(x\)-axis, and also a stretch parallel to the \(y\)-axis of scale factor \(3.\) Only the stretches will affect the areas of regions under the graph.

So if the area of the blue region is \(B\), we know the area of the dark grey region is \(\tfrac{3}{2}\times B.\) Therefore \(\int_{15}^{25} 3f(2x-45)\,dx=\frac{3}{2}\times 53.\)

Splitting up the orange region

We still need to find the area of the region between \(y=3f(2x-45)\) and the \(x\)-axis from \(x=25\) to \(x=30.\) By the previous argument, this is \(\tfrac{3}{2}\) times the area of the corresponding region between \(y=f(x)\) and the \(x\)-axis. We don’t know what the area of this region is yet, but it is related to the area of the orange region in some way.

Using the transformations in reverse, the \(x\)-intercepts of \(y=f(x)\) must be twice as far apart as the \(x\)-intercepts of \(y=3f(2x-45)\), so the width of the orange region must be \(10.\)

The orange curve is a reflection of \(y=f(x)\) in the \(x\)-axis and a stretch parallel to the \(y\)-axis scale factor \(3\), followed by a translation of \(10\) parallel to the \(y\)-axis. Therefore we can split up the orange region as shown here.

Why does this mean that \(\int_{25}^{30}3f(2x-45)\,dx=-\tfrac{25}{2}\)?

Combining these ideas explains why \(\int_{15}^{30}3f(2x-45)\,dx=67.\)

Using integrals

From our previous observations about graph transformations, we can work out that the remaining \(x\)-intercept of \(f(x)\) is at \(x=-15.\) We can now compute \(\int_{-15}^{15}f(x)\,dx\) and use this to obtain \(\int_{15}^{30}3f(2x-45)\,dx.\)

We know \(\int_{5}^{15} 10-3f(x)\,dx = 125\), and we can rearrange this to give \(\int_{5}^{15} f(x)\,dx=-\tfrac{25}{3}.\)

We were also told that \(\int_{-15}^5 f(x)\,dx=53\), so we now know that \(\int_{-15}^{15}f(x)\,dx=53-\tfrac{25}{3}.\)

Why isn’t \(\int_{-15}^{15}f(x)\,dx\) equal to \(53+\tfrac{25}{3}\)?

How could you continue this argument to explain why \(\int_{15}^{30}3f(2x-45)\,dx=67\)?

Thinking again about which transformations rescaled the areas of the regions above or below the axes, $$\int_{15}^{30}3f(2x-45)\,dx = \dfrac{3}{2} \times \left( 53-\dfrac{25}{3}\right) = 67.$$

By considering relationships between \(3f(2x-45)\), \(10-3f(x)\) and \(f(x)\), we were able to piece together enough information to find the complicated-looking integral \(\int_{15}^{30}3f(2x-45)\,dx.\)

More generally, if we can relate a complicated integral to a simpler one, we may be able to use this to evaluate the more complicated one.

Now try to evaluate each of the following integrals.

1. \(\int_{-4}^{-2}\sqrt{x+5}\,dx\)

---

1. \(\int_{0.2}^{1.3}e^{2x}\,dx\)

3. $\int_{-\tfrac{\pi}{6}}^{\tfrac{\pi}{6}}\sin(3x +\tfrac{\pi}{2})\,dx$

Give some examples of other functions that you can integrate in this way.

In the GeoGebra files below, the blue graphs show the functions we want to integrate and the orange graphs show a related function that we already know how to integrate. (The corresponding regions are shaded in blue and orange respectively.) We’ve also added a red function, which is controlled by the slider. Move the slider to see how the blue graph can be transformed into the orange graph, and back again.

Integral of \(\sqrt{x+5}\)

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/suaSfYy8/width/596/height/399/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/suaSfYy8)

We want to find the area of the region under \(y=\sqrt{x+5}\) between \(x=-4\) and \(x=-2\) (the region shaded in blue), but it looks as if this is the same as the area of the region under \(y=\sqrt{x}\) between \(x=1\) and \(x=3\) (the region shaded in orange). We can find the orange area because we know how to integrate powers of \(x\): \(\int_{1}^{3}\sqrt{x}\,dx = \left[\tfrac{2}{3}x^{3/2}\right]_1^3=2\sqrt{3}-\tfrac{2}{3}.\)

We can think of these regions as being made up of lots of narrow strips and we’ve shaded one strip in the GeoGebra file above as an illustration. We’re interested in what happens to this strip as the graph is transformed - anything that happens to this strip will also happen to the whole region. If we move the slider so that the red graph lines up with the orange graph, we can watch what happens to the shaded strip: it doesn’t change width or height as the graph is transformed, but the \(x\)-values that the strip lies between have increased by \(5.\) Why does this help to explain why \(\int_{-4}^{-2}\sqrt{x+5}\,dx=\int_{1}^{3}\sqrt{x}\,dx\)?

Integral of \(e^{2x}\)

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/us6tga9e/width/596/height/399/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/us6tga9e)

This time we are interested in the area of the region under \(y=e^{2x}\) between \(x=0.2\) and \(x=1.3.\) Our previous work suggests that finding a way to relate this to a region under \(y=e^x\) would help, but what would be the appropriate region?

What happens to the darker shaded strip this time as we transform the red graph so that it lines up with the orange graph?

The height of the strip remains the same as we move from the blue graph to the orange graph, but it has doubled in width. In other words, the strip under the blue graph is half as wide as the corresponding strip under the orange graph. What can you say about the values of \(x\) that each strip lies between? How does this relate to graph transformations?

Coming back to the integral we are trying to compute, this suggests that \[\int_{0.2}^{1.3}e^{2x}\,dx=\tfrac{1}{2} \int_{0.4}^{2.6}e^{x}\,dx.\] Can you explain the choice of limits and the factor of \(\tfrac{1}{2}\)?

Using this argument, we are able to evaluate the required integral. \[\int_{0.2}^{1.3}e^{2x}\,dx= \tfrac{1}{2}\big[e^{x}\big]_{0.4}^{2.6}=\tfrac{1}{2}\left(e^{2.6}-e^{0.4}\right)\approx 6.0\]

<cm-toggle label="$\int_{-\pi/6}^{\pi/6}\sin\left(3x+\dfrac{\pi}{2}\right)\,dx?$" type="success" alt-content="" output="all" print-style="content-only"> <cm-geogebra target-id="tvx7a3B2" width="599" height="399" alt-text="Image from GeoGebra file of the transformation $\sin(ax+b)$" alt-image="images/slidingsine.png"/> Now let's look at the third question. Can we find $\int_{-\pi/6}^{\pi/6}\sin\left(3x+\dfrac{\pi}{2}\right)\,dx?$ Let's look at this GeoGebra file. As we vary the $x$ coefficient here (=$a$), we can see that in changing $a$ from $1$ to $3$, the strip shown changes width from $0.3$ to $0.1$. In doing this, we are multiplying the area by $\frac{1}{3}$. (So the pale red area is one third of the orange area.) We are also moving the point where the curve bounding the shaded area meets the $x$-axis from $\pi$ to $\frac{\pi}{3}$. We can see (and we know) that as we vary $b$, we move this integral in a similar way to question 1. The integral we are interested in had limits $\pm \frac {\pi}{6}$ when we set $b=\frac{\pi}{2}$ we can see that we have translated the function to be symmetrical about the $y$-axis so the boundary points have moved from $0$ and $\frac {\pi}{3}$ to $\pm \frac {\pi}{6}$. How could we know this without the GeoGebra image? <cm-chalk> We need to remember that we already shrank everything on the $x$-axis to one third of it's original size so our function will have its maximum when $3x+\frac{\pi}{2}=\frac{\pi}{2}$ and will intersect the $x$-axis when $3x+\frac{\pi}{2}=0 \text{or} \pi$. </cm-chalk> So we know that the integral we are trying to calculate $\int_{-\pi/6}^{\pi/6}\sin\left(3x+\dfrac{\pi}{2}\right)\,dx$ is one third of the much easier looking $\int_{0}^{\pi}\sin x \,dx.$ This becomes $\dfrac{1}{3}[-\cos x]_{0}^{\pi} = -\dfrac{1}{3}\left[\left(\cos \pi\right)-\left(\cos 0\right)\right] = \dfrac{2}{3}$. Can you generalize this result too? <cm-chalk> You might also have realized that $sin(3x+\frac{\pi}{2})=cos 3x$ could you have used this to help evaluate the integral. </cm-chalk> </cm-toggle> Using our results to these questions and our generalizations we could come up with lots of similar functions and we can use our knowledge in other functions we know. E.g. $\int_{4}^{5} \dfrac{2}{(x-1)^2} \,dx= 2\int_{3}^{4} \dfrac{1}{x^2}\,dx$
