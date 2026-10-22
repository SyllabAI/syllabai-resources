---
created: 2026-10-23T02:04:16 (UTC +06:00)
source: https://undergroundmathematics.org/circles/sector-spirals
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository. 
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- circles
- type/fluency-exercise
- level/introducing
resource_identity:
  ugm_id: sector-spirals
  station: circles
  station_title: Circles
  resource_type_id: 8
  resource_type_label: Fluency exercise
  level: Introducing
  ref: 8478
  old_site_id: None
spec_map:
  curriculum_code: CIE-9709-P1-2023
  lane: cie-a-level-maths-20-pure-1
  board: Cambridge CIE
  syllabus_version: 2023-2025
  subsection: circles
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: circles
    validation_status: SUGGESTED
  spec_points: []
  mapped_date: '2026-10-23'
  mapper: cross-map-coordinate-geometry.json (P3c lane 3) @ syllabai-experimental cb947595
  coverage_note: 'no CIE P1 spec point asserted — resource remains in the corpus unmapped (AGENT.md rule 3: coverage is never manufactured)'
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
task: T-UGM-IMPORT-3
assets:
- path: https://undergroundmathematics.org/circles/sector-spirals/download/teacher-notes.pdf
  kind: printable
---

# Sector spirals

> Excerpt: Students are asked to calculate a selection of arc lengths and sector areas in a given diagram. They are also encouraged to think about how adaptations to the diagram affect these values and to think about the special case where arc length is equal to sector area.

## Problem

Describe this image to someone who cannot see it. What information do you need to provide in order for them to accurately reconstruct it?

Assuming the four sectors are of equal angle, calculate the arc length and area of each sector.

What do you notice?

What features of the original image are preserved if it is adapted to create each of these?

What can you say about the arc length and area of each sector in each case?

## Things you might have noticed

In order to make our work clear let’s label the sectors 1 - 4 in a clockwise direction (from smallest to largest radius).

**Some things to notice**

- Each sector has a central angle of \(45^{\circ}\) (or \(\frac{\pi}{4}\) radians) and therefore represents \(\frac{1}{8}\) of its corresponding circle.

- As all circles are mathematically similar, and the radius doubles as we move from sector 1 to sector 2 and so on, each sector is an enlargement of the previous one by length scale factor 2.

How can these ideas help us to complete the task?

Numerical solutions

| Sector | Arc length | Sector area |
|---|---|---|
| 1 | \(\frac{\pi}{4}\) | \(\frac{\pi}{8}\) |
| 2 | \(\frac{\pi}{2}\) | \(\frac{\pi}{2}\) |
| 3 | \(\pi\) | \(2\pi\) |
| 4 | \(2\pi\) | \(8\pi\) |

What features of the original image are preserved if it is adapted to look like this?

**Some things that have stayed the same**

- There are four sectors, centred on the origin, that appear to be of equal angle.

- The four sectors are of radius 1, 2, 4 and 8 respectively.

- Starting with the smallest (light blue) sector, each sector is an enlargement of the previous one by length scale factor 2.

**Some things that have changed**

- The four sectors now make a complete loop and so we can assume that each sector has an angle of \(90^{\circ}\) (or \(\frac{\pi}{2}\) radians) and therefore represents \(\frac{1}{4}\) of its corresponding circle.

- The values for arc length will be double those of the corresponding sectors in the original problem. What do you expect to happen to the areas of the corresponding sectors?

Numerical solutions

| Sector | Arc length | Sector area |
|---|---|---|
| 1 | \(\frac{\pi}{2}\) | \(\frac{\pi}{4}\) |
| 2 | \(\pi\) | \(\pi\) |
| 3 | \(2\pi\) | \(4\pi\) |
| 4 | \(4\pi\) | \(16\pi\) |

**Some more things to notice**

- For sector 2 (of radius 2) the values for arc length and sector area are equal. This was also true for sector 2 in the original image.

- For each sector, the ratio of arc length to sector area is preserved from the original image.

Do you expect these things to be true for the second adaptation of the image too?

What features of the original image are preserved if it is adapted to look like this?

This image has been adapted differently. There are still four sectors, centred on the origin, of radius 1, 2, 4 and 8 respectively. However, they no longer appear to be of equal angle. It looks as though the sector angles may be increasing with sector radius but the exact values are unknown and this means that we cannot calculate arc length and sector area accurately for this diagram. So what can we say about the arc length and sector area in this case?

Perhaps if we think about some of the things that we noticed in the other two diagrams we might be able to decide if these still apply.

Why is it that for sector 2 the values of arc length and sector area are equal in the first two diagrams?

- Will those values be equal for sector 2 in this diagram?

What is the ratio of arc length to sector area for each sector in the previous two diagrams?

- Could you have predicted this to be the case?

- Can you say anything about these ratios in this diagram?
