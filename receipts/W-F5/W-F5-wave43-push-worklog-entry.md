### Wave-43 rebuild + push — records ride lands on GitHub main (trace 1a1e9cc2677bbfd1)

- Order: "push Wave 43" + fresh PAT — the push named as pending by the Wave-43
  records-ride receipt (next_operator_actions).
- Recycle #3 between messages: workspace-root .git replaced by the platform
  persistence repo; the real clone survived at `cache/syllabai-resources` with .git
  rolled back to pre-build state — first Wave-43 commit `ee524911` (order
  1a1e9830c256fdd9) lost with its tree; worktree records surface degraded again
  (135K dirty entries, `tasks/` wiped). Workspace-level artifacts of the first
  build survived (mktree plumbing script, original commit message, both receipt
  copies) and drove the rebuild.
- Rebuild: identical 2A+2M records surface via zero-index plumbing
  (`scripts/wf43_rebuild_wave43.py`); receipts reused byte-exact; original commit
  message kept verbatim + REBUILD clause; LEDGER Wave-43 section re-authored
  (+1,079 bytes vs the lost +1,396 — byte-exact recovery impossible); repo-local
  SyllabAI identity re-fixed.
- Race: pre-push check found main advanced `0111c9c1..16bbd4e8` (7 guided-lane /
  corpus commits; records surface untouched, base blobs byte-identical) — rebuild
  re-parented onto `16bbd4e8`, then pushed `16bbd4e8..062a4c34` (fast-forward, no
  force); remote tip verified post-push; origin/main synced; ancestry re-proven.
  Pushed commit `062a4c3463af9a45a9f086dd42d7637ed24b35bc`.
- Credential: transient URL only; output masked; nothing persisted (project-wide
  grep clean); ROTATION OUTSTANDING (6th exposure).
