---
created: 2026-11-04T12:00:00 (UTC +06:00)
source: https://undergroundmathematics.org/thinking-about-algebra/r8158
author: Underground Mathematics (University of Cambridge)
rights: © University of Cambridge (Underground Mathematics). Use inside SyllabAI is authorised by the
  operator attestation of 2026-10-23 — see LICENSE-DATA.md (Amendment 2026-10-23) in this repository.
  Takedown / correction handling as stated in LICENSE-DATA.md.
tags:
- underground-mathematics
- thinking-about-algebra
- type/review-question
resource_identity:
  ugm_id: r8158
  station: thinking-about-algebra
  station_title: Thinking about Algebra
  resource_type_id: 10
  resource_type_label: Review question
  level: null
  ref: 8158
  old_site_id: Q220
spec_map:
  curriculum_code: CIE-IGCSE-0580-2025
  lane: cie-igcse-maths-25-extended
  board: Cambridge CIE
  syllabus_version: 2025-2027
  subsection: thinking-about-algebra
  subsection_provenance:
    tier: PROVIDER
    signal: source-url-slug
    slug: thinking-about-algebra
    validation_status: SUGGESTED
  spec_points:
  - code: E2.5.5
    provenance:
      tier: AI_SUGGESTED
      confidence: medium
      model_version: GLM (Super Z agent, z.ai) — the 0580 igcse-extended TE2 cross-map (generalisation
        lane 19) (cross-map-0580-te2-algebra-graphs.json @ syllabai-experimental 79088f34)
      evidence: When do these simultaneous equations have a positive solution — E2.5.5 register.
      rationale: 'Canonical UGM title: “When do these simultaneous equations have a positive solution?”;
        exam provenance: Oxford University Mathematics Aptitude Test, 2012, Q1G

        Question reproduced by kind permission of The University of Oxford. The question remains Copyright
        The University of Oxford,

        All rights reserved

        .'
      validation_status: SUGGESTED
  mapped_date: '2026-11-04'
  mapper: cross-map-0580-te2-algebra-graphs.json (P3c) @ syllabai-experimental 79088f34
  coverage_note: null
provenance:
  capture_date: '2026-10-22'
  capture_tool: P2 full-site crawl (ugm-crawl) → ugm-clean extraction; text-only import
  content_language: en
  exam_reference: 'Oxford University Mathematics Aptitude Test, 2012, Q1G

    Question reproduced by kind permission of The University of Oxford. The question remains Copyright
    The University of Oxford,

    All rights reserved

    .'
task: T-UGM-IMPORT-19
interactive:
- src: //www.geogebratube.org/material/iframe/id/n5cShw2z/width/600/height/500/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5
  kind: geogebra-iframe
---

# When do these simultaneous equations have a positive solution?

## Question

There are *positive* real numbers \(x\) and \(y\) which solve the equations \[2x + ky = 4, \qquad x+y = k\] for

1. all values of \(k\);
2. no values of \(k\);
3. \(k=2\) only;
4. only \(k>-2\).

## Solution

The second equation tells us that \(x=k-y\).

We can substitute this into the first equation to give \(2(k-y)+ky=4\), or \(y(k-2) +2k-4=0\).

Note that \(2k-4=2(k-2)\), so the equation factorises to \((k-2)(y+2)=0\).

So either \(k = 2\), or \(y = -2\), or both.

Clearly if \(y = -2\), we will never have a solution to the pair of equations that gives positive values for both \(x\) and \(y\).

Our only hope for such a solution is therefore \(k = 2\).

This gives us \(2x+2y = 4\) and \(x+y=2\). In this case, the lines representing each equation coincide, and we have infinitely many solutions for the pair of equations.

In particular we have the solution \(x = 1, y = 1\), and so a solution where both \(x\) and \(y\) are positive is possible.

Thus the answer is (c).

> [interactive embed (geogebra-iframe): //www.geogebratube.org/material/iframe/id/n5cShw2z/width/600/height/500/border/888888/rc/false/ai/false/sdz/false/smb/false/stb/false/stbh/false/ld/false/sri/true/asb/false/at/html5] — not part of the text import; see the source page.

[Download GeoGebra file](https://www.geogebratube.org/material/download/format/file/id/n5cShw2z)
