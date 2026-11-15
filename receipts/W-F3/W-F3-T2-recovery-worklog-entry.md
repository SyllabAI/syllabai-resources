# W-F3-T2 recovery worklog entry (append-ready block)

```yaml
task: W-F3-T2-RECOVERY (rescue + independent re-verification of the W-F3-T2 build artifacts)
wave: W-F3
origin_trace: 1a1dcc849294ab51
trace_id: 1a1dcc849294ab51
executed_utc: 2026-11-15
operator: SyllabAI operator (zai-web 1a1dcc849294ab51)
order: "Proceed"
verdict: RESCUED_AND_REVERIFIED — 216/216 T2 artifacts rescued byte-identical from the
  orphaned volatile workspace; gate battery re-run from the durable area (755 checks,
  0 fail); census 0.5 additivity + swap pins re-verified independently; zero repo writes;
  W-F3-T2 commit still PENDING OPERATOR ORDER
```

## What was done

- Found the W-F3-T2 execution workspace (trace 1a1db87bf72cb265, 2026-11-14T19:45:52Z)
  orphaned in a volatile area: swap, census 0.5, T2 receipts, emitter/verify scripts and
  caches existed only there and had never reached the durable project area.
- Rescued every artifact into the durable area and proved byte-identity file-by-file
  (216/216; manifest at cache/w-f3-t2/rescue-manifest.json). The one file not rescued is
  an accidental duplicate of the task file at the download root (byte-identical to the
  rescued of-record copy; disposition recorded).
- Re-ran the W-F3-T2 gate battery from the durable area: G-F3-C1 374 / C2 272 / C3 3 /
  C4 102 / C6 4 — ALL PASS (755 checks, 0 fail).
- Re-verified the census 0.5 rider with a fresh own-walk deep-compare (independent of the
  rider script): byte-identity to both receipt pins; exactly the declared amendments;
  0 violations.
- Re-verified SWAP.md pins bi-directionally (68 file pins exactly-once, value-resolved;
  2 additional hex64 tokens are the census context shas).
- Re-ran the Waves 35-38 byte verification: 33/35 MATCH; the 2 non-matches are the known
  adjudicated drifts (_summary.json merged-of-record @ Wave 36; task file T2 status
  update riding the next landing).
- Repo hygiene: removed a stale 0-byte .git/index.lock (2026-11-13) and rebuilt the
  missing index via git reset; status honest again (unstaged partial-clone deletions +
  157 worktree mode-only changes; 0 staged). Refs fact recorded: persistent clone refs
  remain at d2902fcc (last fetch 2026-11-13); wave-35-38 commit objects present in the
  object DB; remote not re-queried (no credentials delegated this round).
- Filed: receipts/EXEC-1a1dcc849294ab51-recover-verify.json + this block.

## Findings recorded, not repaired

- The T2 receipt of record (W-F3-T2-build-receipt.json) is unchanged and remains the
  build's receipt; this recovery adds no build content.
- The committed task file at f80920be still shows the T1-era status (committed blob
  06e35973…); the T2 status update (5e1073b4…) rides the next landing as intended.
- Operator credential rotation (PAT) remains OUTSTANDING.

## Operator actions (repo-side)

1. Commit the 68 new bundle files as ONE revertible commit (git diff --stat shows ONLY
   the 68 create-mode additions; revert = delete the 68 files), with the records
   (task status, T2 receipt/worklog, census 0.5) per the established landing pattern.
2. Optional separate orders: promote SCHEMA-cie-rider.md; commit the CIE config
   proposal; CIE graph YAMLs; deferred ial-chemistry book-join; V: book alignment;
   practicals lane.
