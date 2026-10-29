# T-SPECS-CIE-REJOIN-2 run-002 — the inherited in-item duplicates fix-forward

- Date: 2026-10-29 (session zai-web `web-df0238cc-…`, the REJOIN-2 owner lane)
- Discharges the residual filed by T-SPECS-CIE-CONSUME-2: "the REJOIN-2
  in-item duplicates sidecar repair (rejoin owners, one line)".
- Base commit: `7765e43fa7b76fe73de4f0c693a1d15c56eb20e9` (resources main;
  engine asserts its pre-pins against the working tree and the battery
  re-derives everything independently from HEAD blobs).

## Defect (of record, disclosed at GATE-2)

The REJOIN-2 cascade appended the same code entry twice to **11 items**
across **3** of the 8 wave-2 AS sidecars — byte-identical twins (same
official_id / official_code / tier / method), i.e. the per-item dedup the
REJOIN-2 RECORD claimed ("1,541 code entries cascaded (deduped per item by
official_id)") missed exactly these items. Disclosed of record by
T-SPECS-CIE-GATE-2 ("the 11 inherited duplicates still pinned — a sidecar-side
repair remains the rejoin owners' one-line fix-forward") and pinned inert at
the bundle plane by T-SPECS-CIE-CONSUME-2 ("the engine's strongest-wins
per-code dedup collapses them at attach").

| lane | dup items | surplus entries | codes |
|---|---|---|---|
| cie-as-business-23 | 5 | 5 | 2.1.4 x2 (rn_jz7TdKSJPQXSjCBb, qstnprt_dbnrkZv4Trg9wnDz), 2.2.4 x2 (rn_P9pQrMHkSmkGyXxX, qstnprt_ZMNGwpykHNZvMyBK, qstnprt_7KHxrR4cy3f9QmQ8) |
| cie-as-computer-science-19 | 2 | 3 | 2.1.5 x3 (rn_g8sjd6PVPvy9XrKJ), x2 (qstnprt_GD2yB5srCYGmqfgX) |
| cie-as-maths-20-mechanics | 4 | 4 | 4.5.2 x2 (rn_7vFZ9m4DpPc6jx37, qstnprt_RFWJQ8HYSgVcNwWC, qstnprt_kMFW85MmhBPWfCbW, qstnprt_VFxRHRYz5kjSwqSH) |
| **total** | **11** | **12** | |

## Repair

`scripts/cie_rejoin2_dup_repair.py` — order-preserving **first-wins** dedup
within each affected item's `codes` array (the kept entry IS the original
landing payload; provenance preserved per resources AGENT.md rule 4).
Fail-closed pre-pins (entry census 1,759; exactly 11 dup items / 12 surplus;
all twins canonical-identical; per-lane pending refs pinned) refuse any
write on mismatch; the twin discipline refuses any non-identical duplicate.
Deterministic: the post-state has zero in-item duplicates, so a re-run takes
the pre-pin refusal path and performs **zero writes** (DR5).

- Codes census: **1,759 → 1,747** (−12 surplus twin entries; the GT7-pinned
  1,759 was the defect-inclusive census).
- Footprint: exactly `spec-links/{cie-as-business-23,cie-as-computer-science-19,
  cie-as-maths-20-mechanics}.json` + this record/check + the engine/battery.
- `manifest.json` **byte-untouched** (verified: no manifest row carries a
  code-ENTRY counter — `items_with_codes`/`coded_by_kind` count items and the
  11 items keep ≥1 code each; `pending_refs`, rejoin/verdict landing stats and
  the gate acceptance payload are landing receipts, not live entry counts).
- Sidecar `totals`, `review_state`, `anchors`, `pending` — deep-equal
  unchanged (battery DR2).
- v2 outcome **unchanged by construction** (DR6): every repaired item retains
  exactly the pre-state first payload — the one the consume's per-official_id
  attach already used. Zero v2 contact; no bundle, census, or prod effect.

## Battery

`scripts/cie_rejoin2_dup_repair_check.py` **DR1-DR6: 6/6 PASS**
(`T_SPECS_CIE_REJOIN_2_REPAIR_CHECK.json`): pre-state pins re-derived
independently from HEAD blobs; mutation discipline (later-twin removal only,
deep-equal everything else, exact per-lane deltas −5/−3/−4); post-census
(0 dup / 1,747); manifest sha256 stable; engine re-run zero-write; consume
payload retention for all 11 items.
