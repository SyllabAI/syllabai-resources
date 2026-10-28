# T-SPECS-CIE-JOIN-2 — CIE wave-2 AS sidecar lane record

- Date: 2026-10-28 (Asia/Dhaka; session zai-web `web-df0238cc-…`, gateway
  trace `1a180022cd3b552d`)
- Operator directive: *"the T-SPECS-CIE-JOIN sidecar lane to close the 8-bank
  anchor gap"* — fires the SME-WAVE2 r1 residual #1 (v2 `.syllabai/worklog.md`,
  entry `SME-WAVE2-r1`: "the T-SPECS-CIE-JOIN sidecar lane for the 9 AS
  anchor-gap lanes"; the operator's "8-bank" is the gap's own census class:
  the filled banks serving zero anchors, as-biology-25 excluded — it already
  serves 789 via the spine-rekey R3/R4 basis — and the honest EQ stub
  as-accounting-21 excluded, 0 questions to anchor).
- Base commit: `4b0e9dac` (fetched-first at branch cut; no divergence
  encountered).
- Lane script: `scripts/cie_spec_join_wave2as.py` (JOIN-1 machinery + the AS
  scope law), battery `scripts/cie_join_check_wave2as.py` (J1-J11).
- Apply stamp: `2026-10-28T05:15:32Z` (fixed; sidecars byte-idempotent on
  re-run — battery J10).

## What was built

8 learner spec-links sidecars `spec-links/cie-as-*.json` — one per wave-2 AS
bank — in the EXACT `syllabai.learner-spec-links/1.0` shape of the 44-lane
T-SPECS-CIE-JOIN-1 precedent, plus the additive CIE blocks (`board`,
`review_state`, `registry`, `anchors`, and the new `anchors.scope_law`):

- `review_state`: **SUGGESTED / gate pending** per AGENT.md rule 2 (agent-
  generated mappings are suggestions until the review/promotion gate accepts;
  this lane does NOT self-promote — the 44 went through T-SPECS-CIE-GATE-1 as
  its own operator-keyed lane and so will these).
- Items: only content items carrying `spec_point_ids` anchors (notes `rn_*`,
  question parts `qstnprt_*`); flashcards contribute honest zeros with the
  discovered-but-uncoded count recorded (1,189 chem / 601 phys / 448+236+207+
  230 maths decks' cards).

## The AS scope law (this lane's one new rule)

Candidates are restricted from the PARSED REGISTRIES' own printed markers —
the identical basis the SME-WAVE2 spine build used for its `scope_eq` rules:

| lane | law | lane points / registry |
|---|---|---|
| cie-as-chemistry-25 | `AS Level` only | 204 / 356 |
| cie-as-physics-25 | `AS Level` only | 145 / 303 |
| cie-as-business-23 | `AS Level` only | 62 / 116 |
| cie-as-computer-science-19 | `A Level`-marked (topics 13-20) EXCLUDED; shared scope-less topics 1-12 retained | 161 / 227 |
| cie-as-maths-20-{pure-1,pure-2,mechanics,probability-and-statistics-1} | unscoped 9709 registry — no filter (JOIN-1 semantics for that registry; the component law is a spine-build law) | 146 / 146 |

The registry block carries the FULL registry point count (truth); the lane
subset rides `anchors.scope_law`. Every served code is battery-checked
against the law (J11: zero violations).

## Mechanism

Identical to T-SPECS-CIE-JOIN-1 (`scripts/cie_spec_join.py`, imported, not
forked): universe from the notes' embedded `spec_point` blocks (git
`cat-file --batch`, chunked); candidates from the SME Cambridge path
numbering (leaf X.Y.Z, else topic X.Y.*, else global) with the scope law
applied structurally to the registry before resolution; T1_verbatim /
T2_near text confirmation; pending otherwise — nothing manufactured.

## Results (honest — the JOIN-1 baseline class)

The SME substrate is name-only for these lanes (definitions null corpus-wide,
consistent with the index harvest H4 checks), so the raw deterministic join
yields what the 44 yielded pre-rejoin:

| lane | items | coded | notes | parts | universe | resolved | pending refs |
|---|---|---|---|---|---|---|---|
| cie-as-chemistry-25 | 2,068 | 49 | 2/134 | 47/1,934 | 181 | 2 | 2,511 |
| cie-as-physics-25 | 1,770 | 0 | 0/92 | 0/1,678 | 145 | 0 | 2,170 |
| cie-as-business-23 | 451 | 0 | 0/67 | 0/384 | 242 | 0 | 803 |
| cie-as-computer-science-19 | 449 | 0 | 0/77 | 0/372 | 156 | 0 | 789 |
| cie-as-maths-20-pure-1 | 1,283 | 0 | 0/74 | 0/1,209 | 77 | 0 | 1,689 |
| cie-as-maths-20-pure-2 | 868 | 0 | 0/39 | 0/829 | 41 | 0 | 1,099 |
| cie-as-maths-20-mechanics | 565 | 0 | 0/31 | 0/534 | 36 | 0 | 859 |
| cie-as-maths-20-probability-and-statistics-1 | 633 | 0 | 0/31 | 0/602 | 46 | 0 | 947 |
| **TOTAL** | **8,087** | **49** | **2/545** | **47/7,542** | **924** | **2** | **10,867** |

chem-25's 49 entries = the 2 AS subsection-head identities (2.2.1, 3.7.1 —
SME spec-point name == unique `AS Level` subsection title, T2_near,
`cie_definition_text_join` path-restricted) cascaded to their anchoring
notes/parts. All other anchors stay `pending`, carried verbatim.

## What this lane does NOT do (fail-closed)

- No review-state promotion (SUGGESTED stays SUGGESTED; the gate is its own
  operator-keyed lane, T-SPECS-CIE-GATE-class).
- No v2 contact: the bundle consume / re-emit / census re-pin chain is the
  documented follow-on (below) — v2 main is untouched by this lane.
- No invented coverage: name-only substrates stay pending exactly as the 44
  did pre-rejoin (AGENT.md rule 3).

## Follow-on chain of record (each its own gated lane, as the 44 evolved)

1. Index re-join class (T-SPECS-CIE-REJOIN precedent) — the per-course
   `spec_point_index.json` (present for all 8; definition-poor, name-rich)
   against the J1-J4 identity classes.
2. Operator-verdict fills (V-class) where identity is single-target.
3. Review/promotion gate (the T-SPECS-CIE-GATE-1 precedent).
4. v2 consume (`cie_consume_spec_links.py`) + bundle linkage re-emit
   (linkage-fields-only law) + census re-pin (computed, never transcribed)
   + the operator-gated prod-apply posture per the phase-4 plane law.

## Footprint

- Added: `spec-links/cie-as-{chemistry-25,physics-25,business-23,
  computer-science-19,maths-20-pure-1,maths-20-pure-2,maths-20-mechanics,
  maths-20-probability-and-statistics-1}.json` (8),
  `scripts/cie_spec_join_wave2as.py`, `scripts/cie_join_check_wave2as.py`,
  `graph/reports/T_SPECS_CIE_JOIN_2_RECORD.md`,
  `graph/reports/T_SPECS_CIE_JOIN_2_CHECK.json`.
- Modified (additive only): `spec-links/manifest.json` (8 rows appended +
  additive `cie_join_wave2as` block; every pre-existing row value-identical
  vs HEAD — J7b; every pre-existing block untouched — J7c),
  `spec-links/README.md` (wave-2 AS section appended).
- Byte-untouched: all 94 pre-existing spec-links files (J8, sha256 vs HEAD),
  both SME trees, Official-Specifications/**, graph/** (records added only),
  everything else (J9 footprint guard).

## Battery

J1-J11: 13/13 PASS (`graph/reports/T_SPECS_CIE_JOIN_2_CHECK.json`) — schema,
qual mapping, zero dangling ids, prefix, vocabulary, universe conservation,
cross-foot, manifest additive-only discipline, file byte-identity, footprint,
fixed-stamp reproducibility, and the AS scope law.
