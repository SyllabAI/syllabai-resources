# P13 — Alt Academy family lane (one brand, nine channels)

**Task:** T-VIDEOMAP-P13 · **Authorized:** owner chat 2026-11-14 "file it as lane P13" (after the
@altacademyorg recon: a CAIE-native multi-subject hub plus eight subject channels) · **Status:** built + gated locally; ship pending

## What shipped

**650 owner-reviewed rows onto 19 CIE courses** (24 Tier B paper-code anchors + 626 Tier A spec
rows) from **one brand's nine channels** — the multi-subject hub `@altacademyorg`
(`UCTgPevMIji1ZyP4IPhmwDsQ`, 685 uploads) plus 8 subject channels (chemistry 22 / economics 78 /
maths 77 / physics 47 / biology 9 / psychology 14 / accounting 53; the business subject channel IS
the P12 pool — 75 — not re-inventoried). **985 uploads inventoried, 0 intra-family overlap,
0 overlap with the shipped union.**

- **Tier B session/paper-code anchors (24):** machine-checkable session + CIE paper numbers in
  titles — `CAIE A Level Business 9609 | Paper 42 Oct/Nov 2024 Solved`, `Jun 2022 Paper 11 | Past
  Paper Solution | A level Math P1 9709`, `Nov 2022 Paper 22 | Past Paper Solution | A level
  Physics 9702`, `May/June Paper 22 Q5 | Group 17 | CAIE AS Level Chemistry 9701` and 20 more.
  Routing by paper number per subject: sciences papers 1-3 AS / 4-5 A2; maths P1/P2/P3/P4(M1)/
  P5(S1)/P6(S2) — two-digit "Paper 53" = paper 5 variant 3; econ/business/accounting by paper
  level. Maths shared units anchor to BOTH the AS and A-level course (one row per course,
  ANCHOR-GRANULARITY §5/§8). method `paper-code`, confidence high, boardMismatch false, specs []
  (zero spec weight).
- **The section-name binding (459 rows, the dominant class):** Alt Academy's format
  `Topic | Section | register` names the syllabus section verbatim in a pipe-field. When a
  STOP-stripped pipe-field equals a TOPIC or SUBTOPIC title's norm (node norm >= 8 chars,
  SUBTOPIC preferred), that section's SPEC_POINTs bind as ONE multi-spec row at confidence low —
  disclosed per row. Examples: `Deflation | Price Stability | A Level | Economics` → SUB4.6's
  points; `International Decision | Location and Scale | A Level Business 9609` → the Location
  and scale subtopic; `Volume of Gases | Ch Atoms, molecules & stoichiometry | AS Chemistry` →
  the AS section.
- **Distinctive-token binds (df <= 3):** e.g. `Rules of Integration | Integration | A Level |
  Math` → pure-3 integration points; `Overview of Perry et al.`-style distinctive tokens; the
  accounting series (`Activity Based Costing`, `Auditing and stewardship…`) at medium.
- **Four-gate topic lectures + N.M section-marker narrowing** complete the ladder (the P12
  classes, unchanged).
- **Maths unit-token routing:** `A level Maths S2 9709` / `M1` / `S1` / `P1`… route to the
  spine's unit courses; shared units (S1, M1, P1, P2) bind BOTH the AS and A-level course.
- **Identity:** oEmbed sweep **587/587** author_url channel id == channel-of-record (0 mismatch,
  0 dead, 0 thumb fallbacks).

## Coverage deltas (the point of the lane)

| course | specs before → after | videos before → after |
|---|---|---|
| cie-a-level-economics-23 | 44/253 → **179/253** | 73 → 165 |
| cie-a-level-chemistry-25 | 113/356 → **267/356** | 102 → 141 |
| cie-as-chemistry-25 (P13B) | 98/204 → **197/204** | 83 → 218 |
| cie-a-level-physics-25 | 156/303 → **241/303** | 228 → 294 |
| cie-a-level-business-23 | 8/116 → **44/116** | 12 → 50 |
| cie-as-business-23 | 16/62 → **53/62** | 24 → 78 |
| cie-a-level-maths-20-p&s-1 | 0/17 → **17/17** | 43 → 59 |
| cie-as-maths-20-p&s-1 | 0/17 → **17/17** | 43 → 60 |
| cie-a-level-maths-20-p&s-2 | 0/18 → **11/18** | 1 → 5 |
| cie-a-level-maths-20-pure-1 | → 25/34 | → 246 |
| cie-a-level-maths-20-pure-3 | → 24/43 | → 114 |
| cie-a-level-accounting-21 | 5/34 → **17/34** | 20 → 79 |
| cie-as-accounting-21 | 5/19 → **17/19** | 19 → 32 |
| cie-a-level-biology-25 | 180/257 → **212/257** | 222 → 247 |
| others (mechanics AS+AL, pure-1 AS, pure-2 AS) | increments | — |

## Honest skips (310)

- CIE 9990 psychology — **no spine course** (37 videos incl. the study-list subject channel):
  honest no-target.
- O-Level register (21): no O-level courses in the spine.
- Guidance/advice/marketing registers (29): "Top Tips for Acing your Business A2 Exam!",
  "How To Overcome Exam Anxiety", platform tours, podcasts, Urdu/Hindi promos.
- No distinctive match at the df<=3 bar (~221) with per-cluster reasons.
- **2 degenerate binds re-adjudicated to skips on review:** the S2 title bound to 6.5.1 via
  generic tokens (`between`,`two`) and the terse `A Level | Pricing strategies Short term` bound
  to business-finance via (`short`,`term`) — the honest pricing-strategy match failed on
  strategies/strategy morphology; a generic-token bind is not evidence.

## Gates

Hub video-map tests **16/16 pass (4,427 expects over the 95-course corpus)** — the
`ial-chemistry-17` at-rest count updated 70 → 99 (29 rows newly inherited from the parent's P13
rows). Spec-join census **95 courses / 9,566 rows / 13,712 refs / 0 violations** (P12: 8,775 rows
/ 7,511 refs). Emit replay idempotent (second run byte-stable modulo generatedUtc).

## Ship status

Built and gated locally. Resources lane: `videos/p13-alt-academy`; hub lane:
`t-videomap-p13/run-001` (to be cut at ship time). The push/PR/merge phase runs on the owner's
token (env-only, never stored) — **the previously flagged token string `ghp_rW7z…71xD` remains
unrotated; rotation is still outstanding and strongly recommended.**
