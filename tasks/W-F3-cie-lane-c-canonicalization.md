# W-F3 — Lane C: CIE canonicalization (canonical bundles for the 34 CIE quals)

```yaml
wave: W-F3
tasks:
  - W-F3-T1   # Lane C design of record — CIE canonical-bundle plan: full-34 SOURCE
              # audit, per-family emitter rules against the 13-field contract of
              # record, honest bundle-shape law, blanket-flag adjudication classes,
              # census 0.5 rider proposal, build gates (executed 2026-11-14,
              # trace 1a1da5cb34cb05e1)
  - W-F3-T2   # Lane C build (EXECUTED 2026-11-14, trace 1a1db87bf72cb265) —
              # emitted the canonical bundles per the design for all 34 CIE quals,
              # staged as a swap package (68 files, G-F3-C1..C6 PASS); census 0.5
              # rider applied agent-side; repo commit pending operator order
origin_trace: 1a1da5cb34cb05e1
order_note: >-
  fired by the bare operator order "new wave" (trace 1a1da5cb34cb05e1). Interpreted as
  W-F3 because it is the ONLY wave of the repair map of record that has never fired —
  tasks/W-F1-validation-and-status-check.md §scope: "repairs belong to W-F2 (reparse),
  W-F3 (CIE), W-F4 (book layer)" (W-F2/W-F4 complete with receipts); tasks/W-F2-ial-reparse-probe.md
  non-goal: "No CIE canonicalization (W-F3, Lane C)". If the operator meant a different
  wave, this task file is the correction point; nothing repo-side has been touched.
inputs_of_record:
  - syllabai-resources @ HEAD d2902fcc064f62f8c9ae03ec2b012f49a8ff8922 (cached git tree; blob-sha verified)
  - Official-Specifications/parsed/cie-*/{*.parsed.json,parse_report.json} — 34 SOURCE
    parses by cie-spec-parser-1.0 (29 quals) / cie-spec-parser-1.0+spec-reparse-1.0 (5),
    parse gates G1-G4 PASS 34/34 at the pinned blobs
  - Official-Specifications/parsed/SCHEMA.md (blob 9567f891…) — parse contract; its ID
    table carries NO CIE rows (rider candidate §6)
  - the canonical 13-field row contract of record — staged W-F2-T2 output
    download/w-f2-swap/ial-chemistry/.../spec_points.json (fields: applicability, flags,
    id, leading_verb, official_code, ordering, practical, provenance, scope, sub_items,
    subsection, text, topic) and its topics.json twin
  - scripts/build_canonical.py @ d2902fcc (canonical-builder-2.0, 1093 lines, zero-LLM) —
    the builder of record; Pearson-configured (FAMILY registry, EQ_SECTIONS, COVER_CODE,
    MODULAR_UNIT_MAPS); no CIE rows anywhere in its config
  - spec-fineness-census 0.4 (local sha256 8483d282…) — 34 CIE rows, canonical_bundle
    false ×34, derived_graph false ×34, per-row remedy_lanes prescribing
    "C: canonical bundle (canonical-builder-2.0)" + "C: blanket-flag adjudication"
    + "V: book alignment"
  - books/CATALOG.md (blob 725e21e4…) §4.3 — CIE coursebook rollout rows (6 state S,
    the rest —); books/cambridge-international/{ial,igcse} lanes (34 files, parsed/=0)
  - receipts/W-F4/W-F4-T1-book-join-design.md §ledger — CIE books registered SOURCE_ONLY,
    Lane B follow-on explicitly out of W-F4; receipts/W-F1-T1-wave-report.md §next orders
status: W-F3-T1 COMPLETE 2026-11-14 (trace 1a1da5cb34cb05e1) — design of record filed at
  receipts/W-F3/W-F3-T1-design-of-record.md + JSON receipt + worklog entry; full-34 audit
  of record cached at cache/w-f3/full-34-audit.json; gates G-F3-D1..D3 PASS. W-F3-T2
  EXECUTED 2026-11-14 (trace 1a1db87bf72cb265) — 68 bundle files staged under
  download/w-f3-swap/ (receipts/W-F3/W-F3-T2-build-receipt.json + worklog entry +
  SWAP.md with sha256 pins); gates G-F3-C1..C6 PASS; census 0.4 -> 0.5 applied
  agent-side (additivity CLEAN); repo commit PENDING OPERATOR ORDER. LAND 2026-11-15 (operator order trace 1a1dcd599489036d): the 68 bundle files landed as commit d926be489c016d55b6d5bd3c9210b4d19b5acaf4; the records landing (this task file, T2/recovery receipts, LEDGER Waves 39-40) follows as the next commit of the same order.
write_surface: tasks/W-F3-cie-lane-c-canonicalization.md (NEW, this file) + receipts/W-F3/
  (design doc + JSON receipt + worklog entry) + worklog append + cache/w-f3/ (recon
  caches). Zero repo writes, zero census writes, zero spec-parse writes, zero book-lane
  writes.
```

## 1. Operator order

Order (trace `1a1da5cb34cb05e1`): **"new wave"**. No wave was named. The interpretation of
record is W-F3 (Lane C, CIE canonicalization) per the repair map cited in `order_note`
above — the unique un-fired wave. This wave is a DESIGN wave: it fixes the per-family
emitter rules, the honest bundle-shape law, the flag-adjudication classes, the census 0.5
rider and the build gates. Emitting the 34 bundles is W-F3-T2, fired by a separate
operator order (W-F4-T1/T2 precedent).

## 2. What the audit found (facts of record, cache/w-f3/full-34-audit.json)

- 34 CIE quals, 34 parse dirs, each exactly 2 files (`<syllabus>-parsed.json` +
  `parse_report.json`); **zero canonical bundle files**; census `canonical_bundle: false`
  ×34, `derived_graph: false` ×34.
- Parse gates G1-G4 PASS 34/34 at HEAD; ids unique, prefixes valid
  (`CIE_<QUAL>_<WINDOWS>:N.M.K` shape across families).
- **6 families**: nmk_outcomes 8, int_statements 13, heading_bullets 5, tier_columns 5,
  ce_codes 2, lettered_items 1. Totals: 6,920 spec_points / 598 topics / 1,646
  subsections / practicals_true 0.
- Tiers where applicable: Core (7 quals), Supplement (5), Extended (2); scopes: AS/A
  Level on the A-level quals, per-science (Biology/Chemistry/Physics) on the 2 combined/
  co-ordinated science quals, none elsewhere.
- Flag kinds (recorded, never cleared): code-assembled 14 quals, synthesized-ordinal 13,
  bullet-row 8, synthesized-id 5, reparse-1.0 4, possible-superscript-loss 3,
  control-glyph-stripped 1, edge-whitespace-stripped 1. The 5 heading_bullets quals
  (the 4 F4 CIE quals + GP) have 0 subsections — canonical rows carry `subsection: null`
  (staged IAL precedent).
- Census per-row remedy_lanes already prescribe this wave: `C: canonical bundle
  (canonical-builder-2.0)` + `C: blanket-flag adjudication (per-qual superscript/
  subscript classes)` + `V: book alignment`.

## 3. Scope

| set | quals | Lane C role |
|---|---|---|
| CIE canonical (34) | all `cie-*` census rows (30 F2 + 5 F4 + — see census) | canonical bundle emission from the SOURCE parses: `spec_points.json` + `topics.json` per qual (13-field contract), census 0.5 rider |
| OUT — graph | `derived_graph` | Layer-A YAMLs for CIE = follow-on wave (needs the bundles landed first); OUT of W-F3 |
| OUT — V: book alignment | 6 SOURCE_ONLY coursebooks | Lane B family, books-lane parse pipeline prerequisite; blocked on the books rollout queue (CATALOG §4.3); stays a recorded dependency, not W-F3 work |
| OUT — practicals | CIE practicals | practicals_true = 0 across all 34 SOURCE parses; CIE practical-endorsement content lives in separate documents not in the tree — honest-empty, no practicals.json emitted |
| OUT — repo scripts | build_canonical.py extension | the agent emits bundles with an agent-side zero-LLM emitter (`canonical-builder-2.0-cie-1.0`) honoring the of-record row shapes; a repo-side build_canonical.py CIE config block is an OPTIONAL operator commit alongside the swap (staged as a proposal file, not required) |

## 4. Method (this wave, design only)

1. Full-34 audit at the pinned blobs (DONE — §2; audit JSON is the evidence of record).
2. Fix the emitter contract: canonical rows byte-shaped like the staged W-F2-T2 outputs
   (13-field spec_points rows; topics.json with code/number/title/ordering/provenance);
   CIE rows keep their SOURCE ids verbatim (no re-keying); `provenance` carries pdf +
   pdf_sha1 + page + oy + extraction_method from the SOURCE row fields.
3. Fix the per-family emitter rules (§6 of the design doc of record) for the 6 families,
   including leading_verb derivation (first verb token of the statement text; CIE
   outcome sentences are verb-led), ordering (SOURCE row order), applicability rules per
   scope/tier class, and the honest-absent block for the families the SOURCE does not
   carry (AO / command_words / equations / practicals).
4. Fix the blanket-flag adjudication classes (record-only: per-qual flag -> class table
   in each bundle's manifest block; no flag is ever dropped).
5. Define build gates (§5) and the W-F3-T2 execution plan; propose the census 0.5 rider
   (34 row amendments + changelog seq 7, before/after values in the entry).

## 5. Gates

| gate | wave | pass condition |
|---|---|---|
| G-F3-D1 | T1 | every emitter rule, bundle-shape law and gate rule cites a real artifact of record (path + blob sha where repo-side) — no invented shapes |
| G-F3-D2 | T1 | the audit of record covers all 34 CIE quals from the pinned blobs (families, counts, flags, gates); honest-empty rows name their evidence path |
| G-F3-D3 | T1 | zero writes outside `tasks/W-F3-*.md` + `receipts/W-F3/` + worklog append + `cache/w-f3/`; zero repo writes; census stays 0.4 (0.5 rider proposed, not executed) |
| G-F3-C1 | T2 | every emitted canonical row carries the 13 fields of record; every id/code resolves against the SOURCE parse at its pinned blob (verify script: 0 unresolved); zero LLM |
| G-F3-C2 | T2 | counts equality per qual: canonical spec_points == SOURCE spec_points 1:1 (no drops, no dupes, id-set equality); topics/subsections totals match the SOURCE arrays; flags carried verbatim |
| G-F3-C3 | T2 | SCHEMA.md rider filed for the 6 CIE families (ID-scheme + family-strategy rows); canonical ids byte-identical to SOURCE ids |
| G-F3-C4 | T2 | honest bundle shape: only files with real data emitted (2-file bundle for CIE: spec_points.json + topics.json); absent families recorded in a per-qual honest-absent block; no practicals.json anywhere |
| G-F3-C5 | T2 | census 0.5 rider applied exactly as design §5: 34 row amendments (canonical_bundle false->true + bundle manifest fields + remedy_lanes annotation) + changelog seq 7 with before/after values; zero other fields touched (deep-compare) |
| G-F3-C6 | T2 | swap discipline: everything staged under `download/w-f3-swap/` mirroring repo paths; SWAP.md with sha256 pins; `git diff --stat` at commit time must show ONLY the 68 new bundle files (2 per qual); single revertible commit |

## 6. Receipts of record

One JSON receipt at `receipts/W-F3/W-F3-T1-design-receipt.json` (schema
`syllabai.task-receipt/1`, `origin_trace: 1a1da5cb34cb05e1`), the design of record at
`receipts/W-F3/W-F3-T1-design-of-record.md`, and the append-ready worklog block at
`receipts/W-F3/W-F3-worklog-entry.md`.

## 7. Non-goals

- No bundle emission (no canonical file built anywhere) — W-F3-T2.
- No CIE graph YAMLs (derived_graph follow-on), no notes-join, no book-lane work.
- No repo script edits (build_canonical.py extension is an optional staged proposal).
- No flag clearing (adjudication classes are recorded, never repaired away).
- No census amendment (the 0.5 rider is a proposal inside the design).
- No book acquisition and no LLM anywhere.

## 8. Definition of done

- Design of record + JSON receipt + worklog block filed under `receipts/W-F3/`; task file
  committed alongside; full-34 audit cached as evidence.
- All gates G-F3-D1..D3 adjudicated in the receipt (PASS/FAIL/DEVIATION each recorded).
- Operator actions listed (commit + optional W-F3-T2 order).
