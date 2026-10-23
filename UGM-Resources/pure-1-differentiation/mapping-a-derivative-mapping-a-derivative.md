---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/mapping-a-derivative
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/building-blocks
- level/introducing
resource_identity:
  ugm_id: mapping-a-derivative
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 1
  resource_type_label: Building blocks
  level: Introducing
  ref: 6509
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: introducing-calculus
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: introducing-calculus
    validation_status: SUGGESTED
  spec_points:
  - code: 1.7.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-7 cross-map (cross-map-differentiation.json
        (P3c lane 7) @ syllabai-experimental 93575e69)
      evidence: the derivative as a local scaling via mapping diagrams for f(x)=x^2 (acknowledged capture);
        the construct later proves the chain rule — lane-6 sweep routing pre-identified it for 1.7
      rationale: 'Canonical UGM title: "Mapping a derivative"; exam provenance: , None'
      validation_status: SUGGESTED
    title: understand the gradient of a curve at a point as the limit of the gradients of a suitable
      sequence of chords, and use the notations d y , and d y f ′ ( x ) , f ″( x ) , 2 for first and
      second derivatives
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: ', None'
task: T-UGM-IMPORT-7
assets:
- path: https://undergroundmathematics.org/introducing-calculus/mapping-a-derivative/assets/mapping-diagrams-small.pdf
  kind: printable
- path: https://undergroundmathematics.org/introducing-calculus/mapping-a-derivative/assets/mapping-diagrams.pdf
  kind: printable
- path: https://undergroundmathematics.org/introducing-calculus/mapping-a-derivative/download/teacher-notes.pdf
  kind: printable
interactive:
- src: //www.geogebratube.org/material/iframe/id/VNy9ty37/width/600/height/493/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# Mapping a derivative

> Excerpt: Students are introduced to using mapping diagrams as a way to think about derivatives; this can later be used to prove the chain rule.

## Problem

In [Mapping a function](https://undergroundmathematics.org/thinking-about-functions/mapping-a-function), we explored the mapping diagrams of linear functions such as \(f(x)=3x\) and \(f(x)=2x+1\). Here, we’ll do the same for a familiar non-linear function, considering how it compares to linear functions.

What does the mapping diagram of the function \(f(x)=x^2\) look like?

- What does the mapping diagram look like if it is centred on the arrow from \(0\) to \(f(0)\), at a scale of \(1\) unit per tick-mark?

- What if it is centred at some other arrow, say from \(1\) to \(f(1)\) or \(-1\) to \(f(-1)\) or \(\frac{3}{2}\) to \(f\bigl(\frac{3}{2}\bigl)\)?

- What does the mapping diagram look like if it is centred on the arrow from \(1\) to \(f(1)\), but this time zoomed in to \(0.1\) or \(0.01\) units per tick-mark?

- What if it is instead centred on some other arrow and then zoomed in?

- Can you describe what you observe?

- In what ways are the mapping diagrams of the function \(f(x)=x^2\) similar to those of a linear function, and in what ways are they different?

You can download [large](https://undergroundmathematics.org/introducing-calculus/mapping-a-derivative/assets/mapping-diagrams.pdf) or [small](https://undergroundmathematics.org/introducing-calculus/mapping-a-derivative/assets/mapping-diagrams-small.pdf) blank mapping diagrams for this, or you can use the GeoGebra applet below (which is the same as the first applet in [Mapping a function](https://undergroundmathematics.org/thinking-about-functions/mapping-a-function)).

How does this relate to the graph of the function \(y=x^2\)? You might want to think about the resource [Zooming in](https://undergroundmathematics.org/introducing-calculus/zooming-in) as you consider this question.

To enter the function \(x^2\) into this applet, type x^2.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/VNy9ty37/width/600/height/493/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/VNy9ty37)

## Things you might have noticed

Here are the mapping diagrams for \(f(x)=x^2\) centred at the arrows starting at \(0\), \(1\) and \(-1\), with extended lines as we used in [Mapping a function](https://undergroundmathematics.org/thinking-about-functions/mapping-a-function).

|  |  |  |
|---|---|---|

As we can see, unlike in the linear function case, there is no focal point for the arrows. We also see that multiple arrows hit the same value on the output numberline: there is a pair of arrows hitting every point on the output numberline greater than zero, as this function is not [one-to-one](https://undergroundmathematics.org/glossary/injective). Centring the diagrams on different arrows does not appear to make much difference. (There does seem to be a nice curve shape at the bottom of each diagram formed by the arrows, though.)

Here is what it looks like when zoomed in to \(0.1\) units per tick-mark:

The lines now appear to be close to meeting at a single focal point, as in the linear case.

If we now zoom in further, we see this:

The lines really seem to meet at a focal point now. Either by looking at the location of the focal point and using the formula we worked out in [Mapping a function](https://undergroundmathematics.org/thinking-about-functions/mapping-a-function), or by just looking at where the arrows go, we see that the scale factor is \(2\). So when we zoom in at \(1\), the function \(f(x)=x^2\) looks just like a scaling. We can say that the function \(f\) is [locally](https://undergroundmathematics.org/glossary/local) a scaling at \(x=1\) with scale factor \(2\).

Another way of saying this is that when we zoom in at \(1\), we can approximate \(f(x)=x^2\) by the function \(g(x)=2x+b\) for some appropriate value of \(b\).

Here are zoomed in mapping diagrams centred at \(\frac{3}{2}\) and \(0\):

|  |  |
|---|---|

Again, the function \(f(x)=x^2\) looks locally like a scaling: at \(x=\frac{3}{2}\), the scale factor is \(3\), while at \(x=0\), the scale factor is \(0\).

We now have three values of \(x\) at which we have zoomed in, and at each one, \(f(x)\) can be approximated by a scaling (or a linear function, which itself is a scaling, as we saw in [Mapping a function](https://undergroundmathematics.org/thinking-about-functions/mapping-a-function)).

We might conjecture from our three examples that if we zoom in at \(x=k\) for any choice of \(k\), then \(f(x)\) will (locally) look like a scaling, and so we can approximate the behaviour of \(f(x)\) by some linear function \(g(x)=ax+b\). We could even go further, and make a conjecture about what the scale factor will be.

What might you conjecture about the scale factor at \(x=k\)? You could explore your conjecture using the GeoGebra applet in the [Problem](https://undergroundmathematics.org/introducing-calculus/mapping-a-derivative/) section.

So we see that when we zoom in at a point, the function \(f\) looks like a scaling, and we described this above by saying that \(f\) is locally a scaling. This scaling is called the *derivative* of \(f\) at that point. So for example, the derivative of \(f\) at \(x=1\) is a scaling with scale factor \(2\).

We usually describe a derivative as a pure number, by considering gradients of graphs, as we see in [Zooming in](https://undergroundmathematics.org/introducing-calculus/zooming-in) and [Binomials are the answer!](https://undergroundmathematics.org/calculus-of-powers/binomials-are-the-answer). How can we reconcile these two different descriptions?

As an example, we have just said that the derivative of \(f(x)=x^2\) at \(x=1\) is a scaling with scale factor \(2\), whereas we would normally say that the derivative at this point is just \(2\).

Since every scaling is described by a single number (the scale factor), what we usually call the derivative is just this scale factor, so the two definitions are essentially the same. It can sometimes be very helpful, though, to think about a derivative as describing a scaling rather than as a gradient of a graph. We will see such an example in [Chain mapping](https://undergroundmathematics.org/chain-rule/chain-mapping).

Furthermore, if we were to think about derivatives for functions in more than one dimension, the scale factor approach can easily be extended to handle this case (by replacing our 1-dimensional numberlines by 2-dimensional “number-planes”, for example), whereas it is much harder to extend the gradient definition.

We can give a practical example of thinking about derivatives as scale factors.

Let’s suppose the function \(f\) represents displacement of a particle as a function of time. Then the input numberline shows time and the output numberline shows the displacement of the particle. The local scaling (the derivative) is then the displacement change (on the output numberline) per unit time (on the input line), in other words, the velocity. This offers another perspective on velocity, in addition to that provided by the “gradient of the displacement-time graph” approach.

More generally, if the function \(f\) represents anything as a function of time, then the scale factor represented by the derivative is the rate of change of that thing.

Here are a few things we noticed when comparing these, some of which we have already mentioned earlier:

- The mapping diagram for \(f(x)=x^2\) looks different when centred at different points and when zoomed in by different amounts, whereas for a linear function, it always looks the same.

- The mapping diagram of a linear function \(f(x)=ax+b\) (with \(a\ne0\)) only ever has one arrow hitting any point on the output numberline, whereas this is not the case for \(f(x)=x^2\).

- There are points on the output numberline for \(f(x)=x^2\) which are never reached, but this is not the case for linear functions (as long as \(a\ne0\)).

- There is a beautiful pattern made by the lines on the mapping diagram of \(f(x)=x^2\).

- When we zoom in, the function \(f(x)=x^2\) looks like a linear function. However, it is not the same linear function at each point.

How do the mapping diagrams of \(f(x)=x^2\) relate to the graph of the function \(y=x^2\)?

How does this approach to derivatives compare to that in [Zooming in](https://undergroundmathematics.org/introducing-calculus/zooming-in)? How are the approaches similar, and how do they differ?

You might also want to think about how this approach relates to the algebraic point of view explored in [Binomials are the answer](https://undergroundmathematics.org/calculus-of-powers/binomials-are-the-answer): the derivative there is found as the limit of the gradients of chords, using the algebraic expression \(\dfrac{(x+h)^2-x^2}{(x+h)-x}\).
