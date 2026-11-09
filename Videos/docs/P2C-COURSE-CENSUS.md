# Course census — SyllabAI courses × Cognito shelves × channel sources (P2C, 2026-11-01)

Answers the owner ask: *"Proceed with all subjects, not just biology. Check what courses syllabAI has."*

**106 courses have spines** (12246 spec points total). Every course in `apps/hub/content/` is spine-backed.

## Cognito coverage map (the 11 direct-match shelves)

| Shelf | Lessons | Lessons w/ video | Distinct video IDs | SyllabAI course(s) |
| --- | --- | --- | --- | --- |
| `b2-gcse-cie` | 107 | 75 | 72 | cie-igcse-biology-23 (+ co-ordinated double-award bio) |
| `b2-gcse-iedexcel` | 109 | 75 | 73 | igcse-biology-19 (+ double-award/modular bio variants) |
| `b3-alevel-cie` | 142 | 62 | 63 | cie-a-level-biology-25 (+ AS variant) |
| `c2-gcse-cie` | 80 | 55 | 54 | cie-igcse-chemistry-23 (+ co-ordinated chem) |
| `c2-gcse-iedexcel` | 93 | 64 | 63 | igcse-chemistry-19 (+ double-award/modular chem variants) |
| `c3-alevel-cie` | 130 | 0 | 0 | cie-a-level-chemistry-25 (+ AS variant) |
| `m2-gcse-cie` | 145 | 117 | 117 | cie-igcse-maths-25-extended/-25-core, international-maths-23 |
| `m2-gcse-iedexcel` | 142 | 117 | 117 | igcse-maths-a-18-higher / -foundation (+ modular variants) |
| `p2-gcse-cie` | 121 | 83 | 81 | cie-igcse-physics-23 (+ co-ordinated/combined phys) |
| `p2-gcse-iedexcel` | 113 | 82 | 82 | igcse-physics-19 (+ double-award/modular phys variants) |
| `p3-alevel-cie` | 93 | 0 | 0 | cie-a-level-physics-25 (+ AS variant) |

Key structural facts:
- **c3-alevel-cie / p3-alevel-cie have ZERO site videos** (fully guest-gated) — for CIE A-level Chemistry and Physics, third-party channels are the ONLY video source; both need a dedicated lane (FSL has 375 A-level videos, AQA-aligned — board mismatch must be adjudicated per row).
- CIE A-level Biology has 63 site videos; FSL A-level Bio (~120) is a viable supplement.
- The P2-method (site keyPoints) alignment is still owed to every shelf row above except b2-gcse-iedexcel (done: igcse-biology-19).

## Subjects with NO aligned channel source (honest empty)

History, Geography, Economics, Business, Accounting, English Language/Literature, ICT, Computer Science, Religious Studies, Environmental Management — none of the 5 scanned channels carry aligned teaching content (Malmesbury's GCSE English-Lit poetry analysis is AQA-anthology-specific; Cognito's 28 Psychology videos have no SyllabAI course). These lanes stay honestly video-less until a board-aligned source is identified.

## Per-course spec-point scale (science + maths)

| Course | Specs | Cognito site videos | Channel draft (P2C) |
| --- | --- | --- | --- |
| cie-igcse-biology-23 | 388 | 72 | 15 specs / 14 rows |
| cie-igcse-chemistry-23 | 252 | 54 | 17 specs / 15 rows |
| cie-igcse-further-maths-additional-maths-25 | 77 | - | — |
| cie-igcse-maths-25-core | 112 | - | — |
| cie-igcse-maths-25-extended | 178 | - | — |
| cie-igcse-maths-international-maths-23-core | 109 | - | — |
| cie-igcse-maths-international-maths-23-extended | 165 | - | — |
| cie-igcse-physics-23 | 294 | 81 | 16 specs / 16 rows |
| cie-igcse-science-co-ordinated-sciences-double-award-23-biology | 230 | - | — |
| cie-igcse-science-co-ordinated-sciences-double-award-23-chemistry | 181 | - | — |
| cie-igcse-science-co-ordinated-sciences-double-award-23-physics | 221 | - | — |
| cie-igcse-science-combined-science-23-biology | 70 | - | — |
| cie-igcse-science-combined-science-23-chemistry | 82 | - | — |
| cie-igcse-science-combined-science-23-physics | 86 | - | — |
| igcse-biology-19 | 176 | - | — |
| igcse-biology-modular-24-unit-1 | 54 | - | — |
| igcse-biology-modular-24-unit-2 | 122 | - | — |
| igcse-chemistry-19 | 182 | 63 | 126 specs / 94 rows |
| igcse-chemistry-modular-24-unit-1 | 100 | - | — |
| igcse-chemistry-modular-24-unit-2 | 81 | - | — |
| igcse-further-maths-19 | 43 | - | — |
| igcse-maths-a-18-foundation | 162 | - | — |
| igcse-maths-a-18-higher | 188 | 117 | 7 specs / 7 rows |
| igcse-maths-a-modular-24-foundation-unit-1 | 93 | - | — |
| igcse-maths-a-modular-24-foundation-unit-2 | 68 | - | — |
| igcse-maths-a-modular-24-higher-unit-1 | 99 | - | — |
| igcse-maths-a-modular-24-higher-unit-2 | 97 | - | — |
| igcse-maths-b-16 | 98 | - | — |
| igcse-physics-19 | 195 | 82 | 144 specs / 102 rows |
| igcse-physics-modular-24-unit-1 | 94 | - | — |
| igcse-physics-modular-24-unit-2 | 101 | - | — |
| igcse-science-double-award-17-biology | 134 | - | — |
| igcse-science-double-award-17-chemistry | 131 | - | — |
| igcse-science-double-award-17-physics | 147 | - | — |
| igcse-science-double-award-modular-24-biology-unit-1 | 74 | - | — |
| igcse-science-double-award-modular-24-biology-unit-2 | 60 | - | — |
| igcse-science-double-award-modular-24-chemistry-unit-1 | 83 | - | — |
| igcse-science-double-award-modular-24-chemistry-unit-2 | 47 | - | — |
| igcse-science-double-award-modular-24-physics-unit-1 | 90 | - | — |
| igcse-science-double-award-modular-24-physics-unit-2 | 57 | - | — |
