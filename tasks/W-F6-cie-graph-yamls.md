# W-F6 — CIE graph YAMLs: loader-contract Layer-A graph layer for the 34 CIE quals

```yaml
wave: W-F6
tasks:
  - W-F6-T1   # Design of record (EXECUTED 2026-11-17, trace 1a1e9d9c217c8e75) —
              # schema precedents read at the pushed HEAD (landed graph layer:
              # emit_graph law + ial-chemistry/ial-biology/igcse-biology/igcse-ict
              # byte shapes), 34-qual input census (6,920/467/1,646 == Wave-39
              # counts of record), transform law (codes/parents/edges/honest-nulls),
              # gates G-F6-C1..C8 fixed; design filed receipts/W-F6/
  - W-F6-T2   # Build + land (EXECUTED 2026-11-17, same order) — zero-LLM emitter
              # (pure function of the pinned HEAD blobs), swap staging under
              # download/w-f6-swap/ with sha256 manifest, G-F6-C1..C8 ALL PASS
              # (106,266 battery checks; 136/136 determinism re-run), 136 NEW
              # files landed as one revertible commit via zero-index plumbing
origin_trace: 1a1e9d9c217c8e75
order_note: >-
  fired by the operator order "CIE graph YAMLs" (trace 1a1e9d9c217c8e75) — the
  backlog lane named in the Wave-43 push-confirm report. T1 + T2 same order
  (W-F5 precedent); push by separate operator order.
inputs_of_record:
  - the 34 CIE canonical bundles at commit 062a4c3463af9a45a9f086dd42d7637ed24b35bc
    (spec_points.json issue 2 + topics.json; read via git cat-file, zero worktree
    dependency)
  - the landed graph layer of record (23 Edexcel quals) as schema precedent
  - cache/w-f6/census-inputs.json (input census of record)
  - cache/w-f6/gate-verdicts.json (G-F6-C1..C8 verdict of record)
status: W-F6-T1 COMPLETE 2026-11-17 — design of record filed at
  receipts/W-F6/W-F6-T1-design-of-record.md + JSON receipt + worklog entry.
  W-F6-T2 EXECUTED 2026-11-17 — 136 files emitted (34 quals x
  specification_points/topics/relationships/practicals.yaml); counts 6,920 rows /
  467 topics / 1,646 SUBTOPICs / 8,561 PART_OF edges (1,646 sub->topic + 6,915
  point->topic; 5 honest topic-null rows carry no edge); code laws: canonical
  T-codes verbatim (gaps of record), 59 SF-fallback, 52 #k-disambiguated
  duplicated canonical codes, 47 multi-span provenance lists mirrored; parent law
  prefix 1,638 / page 8 / first-resort 0 (1,646/1,646 resolved); practicals
  honest-empty x34; official_wording = frozen text (text_render stays
  bundle-layer); gates G-F6-C1..C8 PASS; the 136 files landed as commit
  276c84aff1a0a8ed2151397d6ebdbd31a3e1d090 (re-parented 2026-11-18 from the pre-race 6a9e13ce83515134b24299ff42111d702d17ae47, tree byte-identical — race details in the LEDGER Wave-44 entry and the commit messages); the records landing (this task file,
  T1/T2 receipts, Wave-43 ride-along, LEDGER Waves 44-45) landed as commit
  d799fc2ce856e5e39fa12ef8465d9a9af7c3bcba (re-parented 2026-11-18 from the
  pre-race 109f04a8c78f4e3bfbbf94bb75222c0e88708446 — race details in the
  LEDGER Wave-44 entry and the commit messages); both commits PUSHED to GitHub
  main 2026-11-18 — race-checked fast-forward
  6e35df7f44a390548118d96a875578cec80b0913..d799fc2ce856e5e39fa12ef8465d9a9af7c3bcba,
  no force (trace 1a1aa4b6a7bb8c9; receipt
  receipts/EXEC-1a1aa4b6a7bb8c9-push-confirm.json). Zero bundle changes,
  zero parsed-tree changes outside _derived/graph/cie-*.
write_surface: Official-Specifications/parsed/_derived/graph/cie-*/ (NEW, 136
  files) + tasks/W-F6-cie-graph-yamls.md (NEW, this file) + receipts/W-F6/
  (design doc + JSON receipts + worklog entries) + receipts ride-along (Wave-43
  push-confirm receipt + worklog, append-only convention) + LEDGER.md append +
  cache/w-f6/ (census/gates/emit caches) + download/w-f6-swap/ (swap staging,
  agent-side). Zero bundle mutations, zero census writes.
```

## 1. Design of record (receipts/W-F6/W-F6-T1-design-of-record.md)

- File plan: 34 quals x 4 loader-contract YAMLs (136 NEW) under
  `Official-Specifications/parsed/_derived/graph/cie-*/`; one revertible build
  commit; census 0.6 unaffected (agent-side).
- Transform law: meta block per landed Edexcel law (curriculum_code = canonical
  id namespace, qualification = "<bundle id> (Issue 2)", graph_format_version 1,
  V2 edge_vocabulary string verbatim, counts honest); point rows mirror the
  canonical 14-field contract minus render/sub_items; topics.yaml carries TOPIC
  + SUBTOPIC (SUB{n} codes by array index, printed source_code preserved);
  relationships.yaml carries the two landed PART_OF classes only; practicals
  honest-empty (igcse-ict precedent).
- Honest boundaries: text_render and sub_items do not enter the graph (the
  landed layer has no sub-item nodes or SUB edges after the Stage-R vacates);
  no unit blocks (no structure.json for CIE); no REQUIRES_PREREQUISITE/... edges
  (no derivation law — honest-empty).

## 2. Build of record (receipts/W-F6/W-F6-T2-build-receipt.json)

- Emitter `scripts/wf6_emit_cie_graph.py`: pure function of the pinned blobs
  (git cat-file at 062a4c34), deterministic (BUILD_DATE pinned 2026-11-17),
  zero-LLM, zero-network; swap staging `download/w-f6-swap/` + sha256 manifest.
- Gates `scripts/wf6t2_gates.py`: G-F6-C1..C8 ALL PASS — 106,266 battery checks
  (meta parity, code/parent law re-derivation, edge resolution, field fidelity
  vs canonical on all 6,920 rows, counts honesty vs Wave-39 totals, provenance
  pins, 136/136 sha256 byte-identical determinism re-run).
- Landing: zero-index plumbing commit (`scripts/wf6t2_land.py`, mktree
  bottom-up, 4-level tree chain), candidate + post-commit surface verified
  exactly 136 A paths; commit `276c84aff1a0a8ed2151397d6ebdbd31a3e1d090`
  (parent 6e35df7f44a390548118d96a875578cec80b0913, re-parented 2026-11-18 from the original parent 062a4c34 after the pre-push race found the parallel Videos P14 advance 062a4c34..6e35df7f, surface untouched). PUSHED 2026-11-18 — race-checked fast-forward 6e35df7f44a390548118d96a875578cec80b0913..d799fc2ce856e5e39fa12ef8465d9a9af7c3bcba, no force (trace 1a1aa4b6a7bb8c9).
