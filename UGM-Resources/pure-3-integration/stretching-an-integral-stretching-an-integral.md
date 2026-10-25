---
created: 2026-10-26T02:40:04 (UTC +06:00)
source: https://undergroundmathematics.org/calculus-trig-log/stretching-an-integral
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- calculus-trig-log
- type/scaffolded-task
resource_identity:
  ugm_id: stretching-an-integral
  station: calculus-trig-log
  station_title: Calculus of Trigonometry & Logarithms
  resource_type_id: 3
  resource_type_label: Scaffolded task
  level: Developing
  ref: 8619
  old_site_id: C9_RT2_1
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
  - code: 3.5.1
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — P3c lane-13 cross-map (cross-map-p3-integration.json
        (P3c lane 13) @ syllabai-experimental 21845f3)
      evidence: the stretch-symmetry derivation that INT dx/x scales by ln b and the area reading of INT
        1/x^2 under f(bx)/b^2 leading to INT dx/x = ln|x| + C - the 3.5.1 reciprocal antiderivative derived
        rather than asserted
      rationale: 'Canonical UGM title: Stretching an integral'
      validation_status: SUGGESTED
    title: extend the idea of ‘reverse differentiation’ to Including examples such as ax + b 1 include
      the integration of e , , ax + b sin( ax + b ) , cos( ax + b ) , sec ( ax + b ) and 2 2 x + a
  mapped_date: '2026-10-26'
  mapper: cross-map-p3-integration.json (P3c lane 13) @ syllabai-experimental 21845f3
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-13
---

# Stretching an integral

> Excerpt: How can we integrate $\frac{1}{x}$?  Students are asked what happens to areas under the graph of $y=\frac{1}{x}$ when it is stretched, leading to a formula for the integral without requiring calculus tools.

## Warm-up

The graph of the function \(y=\dfrac{1}{x^2}\) is stretched as shown in this diagram.

If the graph is stretched by a factor of \(b\) in the \(x\)-direction (as shown), what is the equation of the resulting graph?

And if, instead, the original graph is stretched by a factor of \(c\) in the \(y\)-direction, what is the equation of the resulting graph?

## Warm-up solution

The graph of the function \(y=\dfrac{1}{x^2}\) is stretched as shown in this diagram.

If the graph is stretched by a factor of \(b\) in the \(x\)-direction (as shown), what is the equation of the resulting graph?

One way to think about this problem is to use the language of functions.

The original graph has equation \(y=f(x)\), where \(f(x)=\dfrac{1}{x^2}\).

When we stretch the graph by a factor of \(b\) in the \(x\)-direction, a point with coordinates \((x,f(x))\) is stretched to the point with coordinates \((bx,f(x))\), as shown in the following diagram. If we write \(X=bx\) for the new \(x\)-coordinate, then the new point has coordinates \((X,Y)=(X,f(X/b))\), so the new graph has equation \(Y=f(X/b)\), or \(y=f(x/b)\) using lower-case letters.

So the equation of the stretched graph is \(y=f(x/b)=\dfrac{1}{(x/b)^2}\). Multiplying the numerator and denominator by \(b^2\) gives the simpler form \(y=\dfrac{b^2}{x^2}\).

And if, instead, the original graph is stretched by a factor of \(c\) in the \(y\)-direction, what is the equation of the resulting graph?

This time, the point \((x,f(x))\) is stretched to the point with coordinates \((x,cf(x))\), as shown in the following diagram. Writing the coordinates of the new point again as \((X,Y)=(x,cf(x))\), we find the new graph has equation \(Y=cf(X)\), as \(X=x\), or \(y=cf(x)\) using lower-case letters.

Therefore the equation of the stretched graph is \(y=\dfrac{c}{x^2}\).

## Problem

Take a look at these diagrams. (There is a [printable version](https://undergroundmathematics.org/calculus-trig-log/stretching-an-integral/components/diagrams.pdf) of them available.)

Diagram 1 shows the graph of \(y=\dfrac1x\). \(I(a)\) is the shaded region under the graph between \(x=1\) and \(x=a\), where \(a>1\), so \(I(a)=\displaystyle{\int_1^a \dfrac{1}{x}\,dx}\).

**Step 1:** The shaded region in Diagram 4 has the same area as the shaded region in Diagram 1 (\(I(a)\)) after undergoing two stretches (either via Diagram 2 or via Diagram 3). Fill in the following information on each diagram where it is missing:

- the scale factor that was used in the stretch;

- the \(x\)-coordinate at each end of the shaded region;

- the area of the shaded region in terms of \(I(a)\), and

- the equation of the graph.

Interactive applet

In the following applet, you can:

- choose the value of \(a\)

- stretch the graph (and the shaded region with it) in the \(x\)-direction by a scale factor of \(b\)

- stretch the graph (and the shaded region with it) in the \(y\)-direction by a scale factor of \(c\)

The original area \(I(a)\) is shown, and the area of the stretched shaded region is also shown.

The original (unstretched) graph of \(y=\dfrac{1}{x}\) is shown as a dashed red line.

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/xa8hvBNg/width/584/height/398/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/xa8hvBNg)

**Step 2:** Investigating the function \(I(x)\).

Recall from above that \(I(x)\) is the function that gives the area of the shaded region between \(1\) and \(x\) under the graph of \(y = \dfrac1x\), so \(I(x)=\displaystyle{\int_1^x \frac{1}{t}\,dt}\). (To avoid confusion, we have used \(t\) when writing this integral instead of \(x\), since \(x\) appears in the limits.)

- Looking now at Diagram 4, can you identify the area \(I(b)\) on the diagram?

- Are there any other \(I(x)\) values which you can easily identify on the diagram?

- How are \(I(a)\) and \(I(b)\) related?

What do these answers suggest about the function \(I(x)\)? Have you seen anything with these properties before?

**Some further questions**

- Using this applet or some graphing software, investigate values of \(I(x)\). Which value of \(a\) gives \(I(a)=1\)? What does this tell you?  > [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/RTkHVBpq/width/577/height/396/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.   [Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/RTkHVBpq)

- What happens if one or both of \(a\) and \(b\) are less than \(1\)?

## Solution

Take a look at these diagrams.

Diagram 1 shows the graph of \(y=\dfrac1x\). \(I(a)\) is the shaded region under the graph between \(x=1\) and \(x=a\), where \(a>1\), so \(I(a)=\displaystyle{\int_1^a \dfrac{1}{x}\,dx}\).

**Step 1:** The shaded region in Diagram 4 has the same area as the shaded region in Diagram 1 (\(I(a)\)) after undergoing two stretches (either via Diagram 2 or via Diagram 3). Fill in the following information on each diagram where it is missing:

- the scale factor that was used in the stretch;

- the \(x\)-coordinate at each end of the shaded region;

- the area of the shaded region in terms of \(I(a)\), and

- the equation of the graph.

Using the ideas from the Warm-up problem, we can complete the diagrams as follows:

**Step 2:** Investigating the function \(I(x)\).

- Looking now at Diagram 4, can you identify the area \(I(b)\) on the diagram?

- Are there any other \(I(x)\) values which you can easily identify on the diagram?

- How are \(I(a)\) and \(I(b)\) related?

Recall that \(I(b)\) is the area under the graph between \(x=1\) and \(x=b\), which we can see fits on the diagram very easily, giving the following:

The other \(I(x)\) value which is now easy to identify on the diagram is the whole shaded area from \(x=1\) to \(x=ab\), which is \(I(ab)\).

Putting these together, we see that \[I(ab) = I(a)+I(b).\]

In terms of integrals, this says that \[\int_1^{ab} \frac{1}{x}\,dx=\int_1^a \frac{1}{x}\,dx+\int_1^b \frac{1}{x}\,dx,\] which is far from obvious from the above sketch.

This suggests that \(I(x)\) may be a logarithm, because logarithms also have the property that \[\log ab=\log a + \log b.\]

**Some further questions**

Experiment shows that \(I(a)=1\) when \(a\approx 2.72\). Therefore if \(I(x)\) really is a logarithm, the base of the logarithm is approximately \(2.72\).

We can actually use this result to **define** logarithms: we define the **natural logarithm** of \(x\), usually written \(\ln x\), to be \(I(x)\), so \[\ln x=\int_1^x \frac{1}{t}\,dt.\]

The base of these logarithms is called “\(e\)”, so we have discovered that \(e\approx 2.72\). Therefore, the natural logarithm can also be written as \(\log_e x\).

If you have already met the natural logarithm function, how can you check that the definition given here and your existing definition agree?

- What happens if \(a\) and/or \(b\) is less than \(1\)?

The relationship we have discovered, \(I(ab)=I(a)+I(b)\) does still work, but we have to require that if \(a<1\), then \(I(a)\) is considered to be negative. This fits with the integral definition of \(I(a)\), that is \(I(a)=\displaystyle{\int_1^a \frac{1}{x}\,dx}\). Then if \(a<1\), the limits of the integral are in the “wrong order”, so we take the value of the integral to be \(\displaystyle{-\int_a^1 \frac{1}{x}\,dx}\) (with the limits in the “right order”), and this is negative. This is because we always require \[\int_b^a f(x)\,dx=-\int_a^b f(x)\,dx.\]

Why might we require integrals to behave in this way?
