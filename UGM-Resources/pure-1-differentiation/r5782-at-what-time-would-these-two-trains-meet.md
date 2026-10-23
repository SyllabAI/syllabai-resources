---
created: 2026-10-24T01:49:53 (UTC +06:00)
source: https://undergroundmathematics.org/introducing-calculus/r5782
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- introducing-calculus
- type/review-question
resource_identity:
  ugm_id: r5782
  station: introducing-calculus
  station_title: Introducing Calculus
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 5782
  old_site_id: Q4019
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
  spec_points: []
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md
    rule 3: coverage is never manufactured)'
  mapped_date: '2026-10-24'
  mapper: cross-map-differentiation.json (P3c lane 7) @ syllabai-experimental 93575e69
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: UCLES O level Mathematics Alternative B Paper 1, 1960, Q6
task: T-UGM-IMPORT-7
---

# At what time would these two trains meet?

## Question

Night trains run non-stop between King’s Cross and Edinburgh, a distance of \(392\) miles, as follows:

Edinburgh depart 10.00 p.m. King’s Cross depart 10.20 p.m.

King’s Cross arrive 6.10 a.m. Edinburgh arrive 5.48 a.m.

1. Calculate the average speed of each train in m.p.h.

---

1. If each train were to maintain a constant speed, find at what time the two trains would meet and at what distance from Edinburgh.

(A graphical method is recommended for this part of the question.)

## Suggestion

Do you have a formula for average speed?

How can you visualise trains starting from different positions but running towards each other?

How can we include the fact that their starting times are different?

## Solution

The train from Edinburgh to King’s Cross takes \(8\) hours and \(10\) minutes for the \(392\) miles. Since \(1\) minute corresponds to \(\dfrac{1}{60}\) hours, the whole journey takes \(8+\dfrac{1}{6} = \dfrac{49}{6}\) hours. Therefore, the average speed of the first train is \(\dfrac{392}{\left(\dfrac{49}{6}\right)} = 48\) m.p.h.

The train starting at King’s Cross needs \(7\) hours and \(28\) minutes, i.e. \(7 + \dfrac{28}{60} = \dfrac{112}{15}\) hours, to reach Edinburgh. That gives an average speed of \(\dfrac{392}{\left(\dfrac{112}{15}\right)} = 52.5\) m.p.h. for the second train.

**Approach 1**

Consider the sketch picture, where the graph representing the train starting in Edinburgh is \(y = 48x\).

As the graph describing the train starting at King’s Cross has slope \(-52.5\), it can be described by \(y = -52.5x + b\), where \(b\) is the \(y\)-intercept.

To work out \(b\), we use that the graph passes through the point \(\left(\dfrac{1}{3}, 392\right)\). We have \(392 = -52.5\times \dfrac{1}{3} + b\) and hence \(b = 409.5\).

The meeting point for the trains is given by \(-52.5x + 409.5 = 48x\), or \(409.5 = 100.5x.\)

This yields \(x = \dfrac{273}{67}\), or \(4\) hours and \(4\) minutes, and therefore the trains meet at \(2.04\) a.m.

The trains meet \(48 \times \dfrac{273}{67} \approx 195.6\) miles from Edinburgh.

**Approach 2**

The train starting at Edinburgh leaves \(20\) minutes (i.e. \(\dfrac{1}{3}\) hours) earlier than the train starting at King’s cross.

Since the earlier train has an average speed of \(48\) m.p.h. it has already travelled \(\dfrac{1}{3} \times 48 = 16\) miles when the second train sets off.

Suppose that the first \(20\) minutes are already over. Let us write \(t\) for the hours it now takes the two trains to meet.

That means that the train starting at Edinburgh travels another \(48t\) miles, and the train starting in King’s Cross travels \(52.5t\).

As the total distnce between Edinburgh and King’s cross is \(392\) miles, we get the equation \(392 = 16 + 48t + 52.5t\), which gives \(t = \dfrac{752}{201}\), or approximately \(3\) hours and \(42\) minutes.

Since the train from Edinburgh started \(20\) minutes before the other, the trains meet \(4\) hours and \(4\) minutes after the first train left Edinburgh, which is at \(2.04\) a.m.

The train starting in Edinburgh has an average speed of \(48\) m.p.h. and therefore travels \(\dfrac{752}{201} \times 48 + 16 \approx 195.6\) miles, which is the distance from Edinburgh at which the two trains meet.
