---
created: 2026-10-23T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/quadratics/r6864
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- quadratics
- type/review-question
resource_identity:
  ugm_id: r6864
  station: quadratics
  station_title: Quadratics
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 6864
  old_site_id: null
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: quadratics
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: quadratics
    validation_status: SUGGESTED
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-quadratics.json (P3c) @ syllabai-experimental 915bfa8c
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule
    3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES 1974 Q1
task: T-UGM-IMPORT-1
assets:
- path: https://undergroundmathematics.org/quadratics/r6864/images/r6864.svg
  kind: figure
---

# How fast are these particles sliding when they pass?

## Question

Two particles \(A\) and \(B\) are placed side by side on rough horizontal ground, and are simultaneously projected along the ground in the same direction with speeds \(\quantity{14}{m\,s^{-1}}\) and \(\quantity{21}{m\,s^{-1}}\) respectively. \(A\) comes to rest after travelling \(\quantity{70}{m}\), and \(B\) after travelling \(\quantity{35}{m}\). Calculate the coefficient of friction between each particle and the ground, and show that the times for which the particles are in motion are in the ratio \(3:1\).

Show also that \(A\) passes \(B\) before either particle comes to rest, and calculate the speed of each particle when this happens.

Take \(g\) to be \(\quantity{9.8}{m\,s^{-2}}\).

## Solution

Two particles \(A\) and \(B\) are placed side by side on rough horizontal ground, and are simultaneously projected along the ground in the same direction with speeds \(\quantity{14}{m\,s^{-1}}\) and \(\quantity{21}{m\,s^{-1}}\) respectively. \(A\) comes to rest after travelling \(\quantity{70}{m}\), and \(B\) after travelling \(\quantity{35}{m}\). Calculate the coefficient of friction between each particle and the ground, and show that the times for which the particles are in motion are in the ratio \(3:1\).

Take \(g\) to be \(\quantity{9.8}{m\,s^{-2}}\).

Let’s start by drawing a diagram.

> [figure: Image showing the two particles A with initial speed 14 m/s travelling 70m to halt and B with initial speed 21m/s travelling 35m to halt — `https://undergroundmathematics.org/quadratics/r6864/images/r6864.svg`] (image not included in the text import; path of record).

The particles are moving so friction is a maximum and we can use the relationship \(F=\mu R\), where \(R\) is the normal reaction and \(\mu\) is the coefficient of friction. \(F\) is the only horizontal force on the object.

We know \(R=mg\) and Newton’s 3rd law tells us that \(F=ma\) leading to \(\mu=a/g\) (where \(a\) is directed to the left, in the same direction as the frictional force).

To find the coefficient of friction for each particle we must first find its acceleration. For this we can use the equation \(v^2=u^2+2as\).

\(a_A = \dfrac{0-14^2}{2\times70} =\dfrac{-196}{140} = -\dfrac{7}{5}\) so \(\mu_A=\dfrac{7}{5g}=\dfrac{1}{7}\).

\(a_B = \dfrac{0-21^2}{2\times35} =\dfrac{-441}{70} = -\dfrac{63}{10}\) so \(\mu_B=\dfrac{63}{10g}=\dfrac{9}{14}\).

To find out the time of travel we can use \(v=u+at\).

\(t_A = \dfrac{0-14}{-7/5}=10\) and \(t_B = \dfrac{0-21}{-63/10}=\dfrac{10}{3}\).

So the ratio \(t_A:t_B=10:\frac{10}{3}=3:1\) as required.

Using

\(s=ut+\frac{1}{2} at^2\)

to find distances at time

\(t\)

,

\[\begin{align*} s_A &=14t-\frac{7}{10}t^2 \\ s_B &=21t-\frac{63}{20}t^2. \end{align*}\]

They pass when \(s_A=s_B\), so subtracting the above equations, \(7t-\frac{49}{20}t^2=0\) which means \(t=0\) (i.e. the start) or \(t=\frac{20}{7}\).

At this time \(A\) has speed \(14-\frac{7}{5} \times \frac{20}{7}= \quantity{10}{m\,s^{-1}}\) and \(B\) has speed \(21-\frac{63}{10} \times \frac{20}{7}=\quantity{3}{m\, s^{-1}}\). This is clearly before either particle has come to rest.
