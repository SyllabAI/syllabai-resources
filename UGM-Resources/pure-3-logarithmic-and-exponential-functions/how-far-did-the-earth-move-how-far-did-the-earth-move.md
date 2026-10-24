---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/how-far-did-the-earth-move
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/food-for-thought
- level/developing
resource_identity:
  ugm_id: how-far-did-the-earth-move
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 9
  resource_type_label: Food for thought
  level: Developing
  ref: 6001
  old_site_id: "A4_RT12_3"
spec_map:
  curriculum_code: CIE-9709-P3-2023
  lane: cie-a-level-maths-20-pure-3
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: exp-and-log
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: exp-and-log
    validation_status: SUGGESTED
  spec_points:
  - code: 3.2.4
    provenance:
      tier: AI_SUGGESTED
      confidence: high
      model_version: "GLM (Super Z agent, z.ai) — P3c lane-10 cross-map (cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af)"
      evidence: "M_L=log_10(A/A_0) magnitude scale, then 'graph linearisation to establish a power law relationship from experimental data' - log-log plot with gradient/intercept constants"
      rationale: "Canonical UGM title: How far did the earth move?"
      validation_status: SUGGESTED
    title: "use logarithms to transform a given relationship e.g. to linear form, and hence determine unknown constants by considering the gradient and/or intercept."
  mapped_date: '2026-10-25'
  mapper: cross-map-log-and-exp.json (P3c lane 10) @ syllabai-experimental 980556af
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  task: T-UGM-IMPORT-10
---

# How far did the earth move?

> Excerpt: This resource explores the use of the logarithmic magnitude scale to describe the severity of earthquakes. Students are then asked to do some graph linearisation to establish a power law relationship from experimental data.

## Magnitudes

The severity of an earthquake is measured and recorded as its local magnitude, \(M_L\), often referred to as its position on the Richter Scale. For instance the New Zealand earthquake of 2011 was of magnitude \(6.1\) (according to [USGS](http://earthquake.usgs.gov/earthquakes/eventpage/usp000huvq)).

The magnitude is defined as a function of \(A\), the maximum amplitude of horizontal displacement of the earth’s surface at a distance of \(\quantity{100}{km}\) from the epicentre, \[M_L=\log_{10}\left(\frac{A}{A_0}\right)\]

where \(A_0\) is a constant displacement chosen as a reference value by Charles Richter in 1935. \[A_0=\quantity{1}{\mu m}=\quantity{10^{-6}}{m}\]

Typical output from a seismometer

What is the magnitude of an earthquake causing a displacement, \(A\), equal to

- \(\quantity{1.0}{\mu m}\)?

- \(\quantity{1.0}{cm}\)?

- \(\quantity{30}{cm}\)?

What was the surface displacement for the following earthquakes? What might that have looked or felt like?

- New Zealand, 2011, \(M_L=6.1\)

- Lincolnshire, 2008, \(M_L=5.2\)

- Chile, 1960, \(M_L=9.5\)

What makes a logarithmic scale useful for describing phenomena like this? Do you know of any other commonly used logarithmic scales?

## Solution

The magnitude is defined as a function of \(A\), the maximum amplitude of horizontal displacement of the earth’s surface at a distance of \(\quantity{100}{km}\) from the epicentre, \[M_L=\log_{10}\left(\frac{A}{A_0}\right)\] where \[A_0=\quantity{1}{\mu m}=\quantity{10^{-6}}{m}\]

What is the magnitude of an earthquake causing a displacement, \(A\), equal to

- \(\quantity{1.0}{\mu m}\)?

In this case, \(A=A_0\), so \[M_L=\log_{10}1=0 .\]

Charles Richter chose this as the reference because no equipment existed at the time that could detect displacements this small.

Modern seismometers can detect movements smaller than this. How would they appear on the magnitude scale?

- \(\quantity{1.0}{cm}\)?

\(\quantity{1.0}{cm}=\quantity{10^{-2}}{m}=\quantity{10^{4}}{\mu m}\), so \[M_L=\log_{10}{10^4}=4.0 .\]

This would be described as a minor or light earthquake, easily felt but causing minimal damage.

- \(\quantity{30}{cm}\)?

\(\quantity{30}{cm}=\quantity{0.3}{m}=\quantity{3\times10^{5}}{\mu m}\), so \[M_L=\log_{10}{(3\times10^5)}\approx5.5 .\]

This would be a moderate earthquake, causing significant damage to poorly constructed buildings.

What was the surface displacement for the following earthquakes? What might that have looked or felt like?

- New Zealand, 2011, \(M_L=6.1\)

To find

\(A\)

we can rearrange the formula and substitute in the

\(M_L\)

value.

\[\begin{align*} M_L &= \log_{10}\left(\frac{A}{A_0}\right)\\ \frac{A}{A_0} &= 10^{M_L}\\ A &= \quantity{10^{6.1}\times 1.0}{\mu m}\\ &\approx \quantity{1.3}{m} \end{align*}\]

If the earth’s surface moved

\(\quantity{1.3}{m}\)

you would expect it to cause severe damage to buildings, which is what happened in Christchurch in 2011.

- Lincolnshire, 2008, \(M_L=5.2\)

\[\begin{align*} \frac{A}{A_0} &= 10^{M_L}\\ A &= \quantity{10^{5.2}}{\mu m}\\ &\approx \quantity{16}{cm} \end{align*}\]

This caused minor damage to buildings.

- Chile, 1960, \(M_L=9.5\)

This was the strongest earthquake ever recorded on earth.

\[\begin{align*} A&=\quantity{10^{9.5}}{\mu m}\\ &\approx\quantity{3.2}{km} \end{align*}\]

Do you find this surprising? How realistic do you think it is?

What factors may effect the reliability of this result?

## Energy

The magnitude scale is based on horizontal displacement, \[M_L=\log_{10}\left(\frac{A}{A_0}\right) \text{, where } A_0=\quantity{1}{\mu m} .\]

But the destructive power of an earthquake is better indicated by the amount of energy dissipated. It has been suggested that the energy, \(E\), is related to the displacement, \(A\), by a simple power law, \[E=E_0 \left(\frac{A}{A_0}\right)^p\] where \(E_0\) and \(p\) are constants.

Can you use the following data from the [British Geological Survey](http://www.earthquakes.bgs.ac.uk/earthquakes/UKsignificant/index.html) and the [US Geological Survey](http://earthquake.usgs.gov/earthquakes/world/historical.php) to verify this suggestion and find values for \(E_0\) and \(p\)?

| Earthquake | Magnitude, \(M_L\) | Energy, \(\quantity{E}{(GJ)}\) |
|---|---|---|
| San Francisco, USA, 1906 | \(7.8\) | \(6\times10^7\) |
| Chile, 1960 | \(9.5\) | \(1\times10^{10}\) |
| Kobe, Japan, 1995 | \(6.9\) | \(1\times10^6\) |
| Kent, 2007 | \(4.3\) | \(200\) |
| Lincolnshire, 2008 | \(5.2\) | \(3000\) |

Estimate the energy dissipation of the 2011 New Zealand earthquake, magnitude \(6.1\).

## Energy solution

The given data shows how

\(E\)

changes with

\(M_L\)

, so first we need to use the formulae above to find a relationship between these two. Using logarithms on the suggested power law, then combining with the definition of

\(M_L\)

,

\[\begin{align*} \log_{10}E&=\log_{10}\left[ E_0 \left(\frac{A}{A_0}\right)^p \right]\\ &=\log_{10}{E_0}+p\log_{10}{\left(\frac{A}{A_0}\right)}\\ &=\log_{10}{E_0}+p M_L . \end{align*}\]

If we plot a graph of \(\log_{10}E\) against \(M_L\), this should give a straight line with gradient \(p\) and intercept \(\log_{10}{E_0}\).

Indeed the points do lie roughly on a straight line, so we can confirm the suggested relationship. Reading the gradient and intercept from the graph, we find

\[\begin{align*} p&=1.5\\ \log_{10}{E_0}&=-4.2\\ E_0&=10^{-4.2}\approx \quantity{6.3\times10^{-5}}{GJ}\\ &=\quantity{63}{kJ} . \end{align*}\]

This value of \(p\) agrees with Charles Richter’s empirical model that states \(E\propto A^{\frac{3}{2}}\). A consequence of this is that an increase of \(2\) in magnitude corresponds to an increase of energy by a factor of \(1000\).

Estimate the energy dissipation of the 2011 New Zealand earthquake, magnitude \(6.1\).

This can either be read from the graph, or calculated using the formula which can now be rewritten as

\[\begin{align*} E&=E_0\times10^{\tfrac{3M_L}{2}}\\ &=63\times10^{\tfrac{3\times6.1}{2}}\\ &\approx\quantity{8.9\times10^{10}}{kJ}\\ &=\quantity{8.9\times10^{4}}{GJ} . \end{align*}\]

This is a little more than the energy released by the atomic bomb that was dropped on Hiroshima in 1945.
