### W-F6 land confirm — build + records commits pending push (trace 1a1e9d9c217c8e75)

- Order: "CIE graph YAMLs" (W-F6). No credential delegated — everything below is
  LOCAL; push PENDING OPERATOR ORDER.
- T1 design of record filed (`receipts/W-F6/W-F6-T1-design-of-record.md` in the
  records commit): 136 NEW loader-contract YAMLs for the 34 CIE quals, schema per
  the landed Edexcel graph layer; honest boundaries fixed (no text_render, no
  sub_items, no units, practicals honest-empty, 5 topic-null rows carry no edge).
- Build commit `6a9e13ce83515134b24299ff42111d702d17ae47` (parent = pushed tip
  `062a4c34`): 136 A paths verified pre/post-commit; totals 6,920 rows / 467
  topics / 1,646 SUBTOPICs / 8,561 PART_OF edges == of-record expectations;
  gates G-F6-C1..C8 ALL PASS (106,266 checks; 136/136 sha256 determinism).
- Records commit `109f04a8c78f4e3bfbbf94bb75222c0e88708446`: W-F6 task file +
  T1/T2 receipts + the Wave-43 push-confirm ride-along + LEDGER Waves 44-45
  (+2,136 bytes, prefix-verified). Surface exactly 8A + 1M.
- One build-land incident, self-caught by the surface assert: the first tree
  chain was 3-level (graph subtree one level high; 342-path surface) — fixed to
  the true 4-level chain; wrong tree unreferenced. Zero bundle changes; zero
  parsed-tree changes outside `_derived/graph/cie-*/`.
- Credential: none used; standing rotation reminder for the 6th-exposure PAT.
