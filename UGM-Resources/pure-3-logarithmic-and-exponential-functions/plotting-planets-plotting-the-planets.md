---
created: 2026-10-24T22:06:39 (UTC +06:00)
source: https://undergroundmathematics.org/exp-and-log/plotting-planets
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- exp-and-log
- type/rich-example
- level/developing
resource_identity:
  ugm_id: plotting-planets
  station: exp-and-log
  station_title: Exponentials & Logarithms
  resource_type_id: 2
  resource_type_label: Rich example
  level: Developing
  ref: 9799
  old_site_id: null
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
      evidence: "planetary data linearised by logarithms: 'if we take the logarithms' of the orbital data the power law P=k r^m becomes a straight line; prior routing of record: lane-5 '2.2 Logarithmic and exponential functions'"
      rationale: "Canonical UGM title: Plotting the planets"
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

# Plotting the planets

> Excerpt: Students are asked to plot graphs of data about the Solar System to find lines of best fit. Logarithms are required to linearise the data and the modelled relationships are linked back to theoretical models used in astronomy.

## Problem

The following data is an extract from a [planetary fact sheet](https://nssdc.gsfc.nasa.gov/planetary/factsheet/) published by NASA.

|  | Distance from sun, \(r\) \((\quantity{10^6}{km})\) | Orbital period, \(P\) \((\mathrm{days})\) | Orbital speed, \(v\) \((\mathrm{km\,s^{-1}})\) | Mean surface temperature, \(T\) \((\mathrm{^\circ C})\) |
|---|---|---|---|---|
| Mercury | \(57.9\) | \(88\) | \(47.4\) | \(167\) |
| Venus | \(108.2\) | \(224.7\) | \(35\) | \(464\) |
| Earth | \(149.6\) | \(365.2\) | \(29.8\) | \(15\) |
| Mars | \(227.9\) | \(687\) | \(24.1\) | \(-65\) |
| Jupiter | \(778.6\) | \(4331\) | \(13.1\) | \(-110\) |
| Saturn | \(1433.5\) | \(10\,747\) | \(9.7\) | \(-140\) |
| Uranus | \(2872.5\) | \(30\,589\) | \(6.8\) | \(-195\) |
| Neptune | \(4495.1\) | \(59\,800\) | \(5.4\) | \(-200\) |
| Pluto | \(5906.4\) | \(90\,560\) | \(4.7\) | \(-225\) |

Physics suggests that the orbital period, \(P\), and distance from the sun, \(r\), are related by a formula of the form \[P=A \,r^k\] where \(A\) and \(k\) are constants. By plotting a suitable graph, estimate the values of \(A\) and \(k\).

Things to think about

- A straight-forward graph of \(P\) against \(r\) will probably show a curve from which it is hard to estimate values.

- Can you transform the data to give a straight line graph?

- You will probably find it helpful to use either graph paper or graphing software to obtain accurate values.

Use your results to predict the orbital period of Ceres, a dwarf planet in the asteroid belt with \(r=414.0\).

Now try this: temperature

The surface temperature is generally lower for planets further away from the sun. Use the data to find an exponential law (\(T=Ae^{-kr}\)) or a power law (\(T=Ar^k\)) to model this.

- You might need to use the absolute temperature, measured in Kelvin. A difference of \(\quantity{1}{K}\) is the same as a difference of \(\quantity{1}{^\circ C}\) but \(\quantity{0}{^\circ C}\approx\quantity{273}{K}\).

Use your results to predict the surface temperature of Ceres.

## Solution

A graph of \(P\) against \(r\) looks like this.

There is a nice smooth curve that fits the data, but unless you are using graphing software with polynomial regression it does not help us to find values for \(A\) and \(k\). However, if we take the logarithm of each side of the formula and then use the laws of logarithms, we get \[\log P = \log A + k\,\log r.\] So if we plot \(\log P\) against \(\log r\) we should get a straight line with gradient \(k\) and axis intercept at \(\log P=\log A\).

Note that we could use logarithms to any base, but here we have chosen to use natural logarithms (base \(e\)).

| \(\ln P\) | \(4.477\) | \(5.415\) | \(5.900\) | \(6.532\) | \(8.374\) | \(9.282\) | \(10.328\) | \(10.999\) | \(11.414\) |
|---|---|---|---|---|---|---|---|---|---|
| \(\ln r\) | \(4.059\) | \(4.684\) | \(5.008\) | \(5.429\) | \(6.657\) | \(7.268\) | \(7.963\) | \(8.411\) | \(8.684\) |

This straight line has gradient \(1.5\) and axis intercept \(-1.6\). So we have \(k=1.5\) and \(\ln A=-1.6\) which means that \(A=0.20\). We can write the formula as \[P=0.2 \,r^{1.5}.\]

The \(1.5\) power might seem surprising, but the Physics of gravity and planetary motion does in fact predict this. It is summed up in Kepler’s Third Law which states that \(P^2\propto r^3\). Note that orbits are actually elliptical and \(r\) is the [semi-major axis](https://undergroundmathematics.org/glossary/semi-major-axis) which is what NASA quote in their table. Kepler also tells us that our constant \(A\) is a function of the mass of the sun, \(M_\odot\). \[A=\frac{2\pi}{\sqrt{GM_\odot}},\] where \(G\) is the Gravitational Constant, \(\quantity{6.67\times10^{-11}}{m^3\,kg^{-1}\,s^{-2}}\). After sorting out the units, our value of \(A=0.20\) allows us to estimate the mass of the sun at \(M_\odot=\quantity{1.98\times10^{30}}{kg}\).

Substituting into our formula gives \[P=0.2\times 414^{1.5} \approx 1685.\] So we can predict that Ceres has an orbital period of \(\quantity{1685}{days}\). Astronomical tables give the actual value as \(\quantity{1682}{days}\).

**Temperature**

The surface temperature is generally lower for planets further away from the sun. Use the data to find an exponential law (\(T=Ae^{-kr}\)) or a power law (\(T=Ar^k\)) to model this.

- You might need to use the absolute temperature, measured in Kelvin. A difference of \(\quantity{1}{K}\) is the same as a difference of \(\quantity{1}{^\circ C}\) but \(\quantity{0}{^\circ C}\approx\quantity{273}{K}\).

The first thing to notice is that the general rule is not always true – the surface temperature of Venus seems to be exceptionally high. We’ll treat this as some kind of outlier.

The question suggests an exponential or power law, so one or other of the following.

| If we suppose that \[T=T_0\,e^{-ar}\] then this would mean that \[\ln T = \ln T_0-ar\] so a graph of \(\ln T\) against \(r\) would be a straight line. | If we suppose that \[T=T_1\,r^p\] then this would mean that \[\ln T = \ln T_1+p\ln r\] so a graph of \(\ln T\) against \(\ln r\) would be a straight line. |
|---|---|

So we’ll work out \(\ln T\) and \(\ln r\) and plot the graphs. The hint suggests using absolute temperature, so we’ll add that to our table and evaluate the logarithm of that rather than of the Celsius temperature.

| \(r\) | \(57.9\) | \(108.2\) | \(149.6\) | \(227.9\) | \(778.6\) | \(1433.5\) | \(2872.5\) | \(4495.1\) | \(5906.4\) |
|---|---|---|---|---|---|---|---|---|---|
| \(\ln r\) | \(4.059\) | \(4.684\) | \(5.008\) | \(5.429\) | \(6.657\) | \(7.268\) | \(7.963\) | \(8.411\) | \(8.684\) |
| \(T_a\) \((\mathrm{K})\) | \(440\) | \(737\) | \(288\) | \(208\) | \(163\) | \(133\) | \(78\) | \(73\) | \(48\) |
| \(\ln T_a\) | \(6.087\) | \(6.603\) | \(5.663\) | \(5.338\) | \(5.094\) | \(4.890\) | \(4.357\) | \(4.290\) | \(3.871\) |

Can you see why using absolute rather than Celsius temperature is important?

|  |  |
|---|---|

The graph against \(\ln r\) is a much better approximation to a straight line. We decided that Venus was an outlier and so we have drawn a line of best fit ignoring its data point. This line has gradient close to \(-0.43\) and intercept at \(7.8\). So in our formula \[T_a=T_1\,r^p\] we have \(p=-0.43\) and \(T_1\approx e^{7.8}\approx 2400\). Turning the temperature back into \(\mathrm{^\circ C}\), we can write the formula as \[T=\frac{2400}{r^{0.43}}-273.\]

As a check, substitute in a few values from the original table. It’s likely that none of them will match exactly, since the data points are scattered around our line of best fit.

There is a theoretical model that predicts that planetary equilibrium temperature varies as \(\dfrac{1}{\sqrt{r}}\) and our result is not far off from that. You could add a line to your graph corresponding to this theoretical result and compare it with the data points. You might also think about what factors other than \(r\) could affect the surface temperature and lead to the scattering of the data.

Substituting \(r=414.0\) into our formula gives \[T=\frac{2400}{414^{0.43}}-273 \approx -93.\] So we can predict the temperature to be \(\quantity{-93}{^\circ C}\) or \(\quantity{180}{K}\). Astronomical tables give the actual value as \(\quantity{168}{K}\).
