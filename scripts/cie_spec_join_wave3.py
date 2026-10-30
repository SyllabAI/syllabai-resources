#!/usr/bin/env python3
"""
T-SPECS-CIE-JOIN-3 — the EQ/FC wave-growth sidecar lane (the EQFC-CONSUME-1
receipt residual of record: "the wave's unmapped growth (+2,705 q / +8,855 p
at the official-code layer) joins the verdict fills -> review gate -> v2
consume chain"; operator directive "fire that consume lane", 2026-10-30,
zai-web, gateway trace 1a18bc6701800065).

Two lane classes, one engine:

A. ADDITIVE EXTENSION (lanes with committed sidecars): the corpus universe
   is rebuilt at HEAD exactly by the T-SPECS-CIE-JOIN-1 machinery
   (cie_spec_join.lane_bundle, imported — NOT forked); the lane's wave
   items = rebuilt item ids MINUS the committed sidecar's item ids, taken
   verbatim from the rebuilt bundle (codes = the lane's own T1/T2
   resolutions on the note substrate; pending = the declared sids the
   substrate cannot resolve). Committed items/blocks are byte-untouched.

B. FRESH BUILD (sidecar-less wave lanes: cie-as-biology-25 — excluded from
   JOIN-2's 8 because it then served via the spine-rekey basis; its wave
   parts have no such basis): the full JOIN-2 build with the parse-printed
   AS scope law (cie_spec_join_wave2as.apply_scope class), registry block
   carrying the FULL registry truth and the subset disclosed in
   anchors.scope_law.

The J0 law (both classes) — cascade of the of-record gate-accepted sid rows:
a new item's declared sid that already carries an ACCEPTED spec_links row in
the v2 content-map mirror of record (spcptToOfficial, lineage
"spec_links_sidecar_accepted" — the gate-promoted sidecar chain output,
CI-verified at the v2 pin) resolves BY THAT ROW: the code entry
{official_id, official_code, tier, method} is copied verbatim from the row
with via="wave3-cascade-of-record-sid-row" added, the sid leaves the pending
list, and NOTHING is re-derived or re-decided. AGENT.md rules 1/4: the
mapping is authoritative at its validation state and its provenance is
preserved. Rule 3 is honoured by construction: no candidates beyond the
declared substrate, no semantic-similarity manufacture.

Review state: every wave3 landing stays SUGGESTED (additive
review_state.wave3 block) — AGENT.md rule 2; promotion is the chain's
stage-#4 gate (T-SPECS-CIE-GATE-3 class, operator-keyed).

Determinism: fixed stamp, HEAD-pinned reads on both repos (TOCTOU-free),
sorted iteration, byte-idempotent pre-commit re-runs; the stats artifact
carries NO wall-clock fields.
Battery: scripts/cie_join_check_wave3.py (WJ1-WJ8).
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

RES = Path("/home/z/my-project/work/res-worktree")
V2 = Path("/home/z/my-project/work/syllabai-v2")
SPEC_LINKS = RES / "spec-links"

V2_PIN = "3245de7c91e030625bf556dd6280bfd2d4f10bea"

LANE_ID = "T-SPECS-CIE-JOIN-3"
STAMP = "2026-10-30T09:00:00Z"

sys.path.insert(0, str(RES / "scripts"))
import cie_spec_join as base  # noqa: E402
import cie_spec_join_wave2as as j2  # noqa: E402


def head_sha(cwd: Path) -> str:
    return subprocess.run(["git", "rev-parse", "HEAD"], cwd=cwd,
                          capture_output=True, text=True, check=True).stdout.strip()


def accepted_sid_table(slug: str) -> tuple[dict, str]:
    """sid -> verbatim row, for lineage spec_links_sidecar_accepted rows of
    the v2 content-map mirror of record at the v2 pin."""
    raw = subprocess.run(
        ["git", "show", f"{V2_PIN}:apps/hub/content-maps/{slug}.json"],
        cwd=V2, capture_output=True, text=True)
    if raw.returncode != 0:
        return {}, ""
    att = json.loads(raw.stdout)
    rows = {sid: row for sid, row in (att.get("spcptToOfficial") or {}).items()
            if row.get("lineage") == "spec_links_sidecar_accepted"}
    blob_sha = hashlib.sha256(raw.stdout.encode("utf-8")).hexdigest()
    return rows, blob_sha


def j0_cascade(items: dict, acc: dict, item_map_codes: dict) -> Counter:
    """Apply the J0 law + the collision quarantine law to NEW items (in place).

    Quarantine law (the NO-GUESS posture of the sid-anchor/sheet conflict
    classes): a NEW item whose of-record map row already carries codes may
    only carry codes that AGREE with that row (superset suggestions are
    suppressed); a suppressed (item, code) pair is recorded in the wave3
    quarantine census and re-enforced at every later cascade stage."""
    st = Counter()
    for iid in sorted(items):
        it = items[iid]
        of_record = item_map_codes.get(iid) or set()
        kept = []
        for sid in it.get("pending") or []:
            row = acc.get(sid)
            if not row:
                kept.append(sid)
                continue
            code = row.get("officialCode")
            if not code:
                kept.append(sid)
                continue
            if of_record and code not in of_record:
                st["j0_quarantined"] += 1
                continue
            entry = {
                "official_id": row.get("officialId") or code,
                "official_code": code,
                "tier": row.get("tier"),
                "method": row.get("method"),
                "via": "wave3-cascade-of-record-sid-row",
            }
            it.setdefault("codes", [])
            if not any(c.get("official_code") == code for c in it["codes"]):
                it["codes"].append(entry)
            st["j0_sids"] += 1
        it["pending"] = kept
        if of_record:
            agree = [c for c in it.get("codes") or []
                     if c.get("official_code") in of_record]
            dropped = len(it.get("codes") or []) - len(agree)
            if dropped:
                st["t12_quarantined"] += dropped
            it["codes"] = agree
        it["codes"] = sorted(it.get("codes") or [],
                             key=lambda c: (c.get("official_code") or "",
                                            c.get("tier") or ""))
    return st


def map_row_codes(slug: str) -> dict:
    """item id -> set of of-record codes, from the v2 map mirror at the pin."""
    raw = subprocess.run(
        ["git", "show", f"{V2_PIN}:apps/hub/content-maps/{slug}.json"],
        cwd=V2, capture_output=True, text=True)
    if raw.returncode != 0:
        return {}
    att = json.loads(raw.stdout)
    return {iid: {c.get("spineCode") or c.get("officialCode")
                  for c in (v.get("codes") or [])}
            for iid, v in (att.get("items") or {}).items()
            if v.get("codes")}


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--stamp", default=STAMP)
    ap.add_argument("--lanes", default="")
    args = ap.parse_args()
    stamp = args.stamp

    v2_head = head_sha(V2)
    v2_tip = subprocess.run(["git", "ls-remote", "origin", "main"], cwd=V2,
                            capture_output=True, text=True,
                            check=True).stdout.split()[0]
    if v2_head != V2_PIN and v2_tip != V2_PIN:
        sys.exit(f"FATAL: v2 pin drifted: local {v2_head[:8]} and origin "
                 f"both != {V2_PIN[:8]}")

    lane_to_qual, quals = base.load_manifest()
    files = base.ls_tree()

    all_lanes = sorted(l for l in lane_to_qual
                       if l.startswith(("cie-", "ial-")))
    want = {x.strip() for x in args.lanes.split(",") if x.strip()} or None

    manifest_path = SPEC_LINKS / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    pre_courses = json.loads(json.dumps(manifest.get("courses", {})))
    pre_blocks = json.dumps({k: v for k, v in manifest.items()
                             if k not in ("courses", "generated_utc")},
                            sort_keys=True)

    grand: Counter = Counter()
    per_lane = {}
    touched = []
    for lane in all_lanes:
        if want and lane not in want:
            continue
        committed_path = SPEC_LINKS / f"{lane}.json"
        committed = None
        if committed_path.exists():
            committed = json.loads(committed_path.read_text(encoding="utf-8"))
        qual = quals[lane_to_qual[lane]]
        reg = base.Registry(qual)

        rebuilt = base.lane_bundle(lane, qual, reg, files, stamp)

        if committed is None:
            # class B: fresh build with the parse-printed AS scope law
            full, kept = j2.apply_scope(lane, reg)
            if kept == full:
                scope_note = {"law": "none (registry carries no printed scope markers)",
                              "full": full, "kept": kept}
            else:
                rebuilt = base.lane_bundle(lane, qual, reg, files, stamp)
                rebuilt["registry"]["official_points"] = full
                scope_note = {"law": "AS Level only (parse-printed markers)",
                              "full": full, "kept": kept}
            fresh_items = rebuilt["items"]
            if not fresh_items:
                # the honest-stub exclusion (the JOIN-2 record class): a lane
                # with zero anchored corpus items gets NO sidecar file at all
                continue
            acc_rows, _ = accepted_sid_table(lane)
            st = j0_cascade(fresh_items, acc_rows, map_row_codes(lane))
            rebuilt["anchors"]["scope_law"] = scope_note
            rebuilt["anchors"]["wave3"] = {
                "lane": LANE_ID, "class": "fresh-build",
                "stamp": stamp, "j0": dict(st),
                "items": len(fresh_items),
                "items_with_codes": sum(1 for v in fresh_items.values() if v["codes"]),
            }
            rebuilt["review_state"]["wave3"] = {
                "state": "SUGGESTED", "lane": LANE_ID, "gate": "pending",
                "stamp": stamp,
                "note": "wave-growth sidecar (agent-generated, AGENT.md rule 2); "
                        "promotion at the chain's stage-#4 gate",
            }
            rebuilt["generated_utc"] = stamp
            (SPEC_LINKS / f"{lane}.json").write_text(
                json.dumps(rebuilt, indent=1, ensure_ascii=False) + "\n",
                encoding="utf-8")
            manifest["courses"][lane] = {"qual": rebuilt["qual"],
                                         **rebuilt["totals"]}
            per_lane[lane] = {"class": "fresh-build",
                              "new_items": len(fresh_items),
                              "j0": dict(st)}
            grand.update({k: v for k, v in st.items()})
            grand["lanes_fresh"] += 1
            touched.append(lane)
            print(f"[{lane}] FRESH items={len(fresh_items)} "
                  f"coded={rebuilt['totals']['items_with_codes']} j0={dict(st)}",
                  flush=True)
            continue

        # class A: additive extension
        committed_ids = set(committed.get("items") or {})
        new_items = {iid: json.loads(json.dumps(it))
                     for iid, it in rebuilt["items"].items()
                     if iid not in committed_ids}
        if not new_items:
            continue
        acc_rows, acc_blob = accepted_sid_table(lane)
        st = j0_cascade(new_items, acc_rows, map_row_codes(lane))

        anchors = committed.setdefault("anchors", {})
        anchors["wave3"] = {
            "lane": LANE_ID, "class": "additive-extension",
            "stamp": stamp,
            "base_commit": head_sha(RES),
            "corpusUniverse": {
                "universe_ids": rebuilt["anchors"]["universe_ids"],
                "universe_resolved": rebuilt["anchors"]["universe_resolved"],
                "parts_anchored_corpus": rebuilt["anchors"]["parts"],
                "flashcards_discovered_uncoded":
                    rebuilt["anchors"]["flashcards_discovered_uncoded"],
            },
            "itemsAdded": len(new_items),
            "itemsAddedWithCodes": sum(1 for v in new_items.values() if v["codes"]),
            "pendingRefsAdded": sum(len(v.get("pending") or [])
                                    for v in new_items.values()),
            "j0": dict(st),
            "v2MirrorInput": {"pin": V2_PIN, "contentMapSha256": acc_blob},
        }
        rs = committed.setdefault("review_state", {})
        rs["wave3"] = {
            "state": "SUGGESTED", "lane": LANE_ID, "gate": "pending",
            "stamp": stamp,
            "note": "wave-growth items are agent-generated suggestions "
                    "(AGENT.md rule 2); promotion at the chain's stage-#4 gate",
        }
        totals = committed["totals"]
        totals["items"] += len(new_items)
        totals["items_with_codes"] += sum(1 for v in new_items.values()
                                          if v["codes"])
        for it in new_items.values():
            kind = "notes" if it["kind"] == "note" else "question_parts"
            totals["by_kind"][kind] = totals["by_kind"].get(kind, 0) + 1
            if it["codes"]:
                totals["coded_by_kind"][kind] = \
                    totals["coded_by_kind"].get(kind, 0) + 1
        committed["items"].update(new_items)
        (SPEC_LINKS / f"{lane}.json").write_text(
            json.dumps(committed, indent=1, ensure_ascii=False) + "\n",
            encoding="utf-8")
        per_lane[lane] = {"class": "additive", "new_items": len(new_items),
                          "j0": dict(st)}
        grand.update({k: v for k, v in st.items()})
        grand["lanes_additive"] += 1
        grand["items_added"] += len(new_items)
        touched.append(lane)
        print(f"[{lane}] +{len(new_items)} items "
              f"(coded {sum(1 for v in new_items.values() if v['codes'])}) "
              f"j0={dict(st)}", flush=True)

    if touched:
        manifest["generated_utc"] = stamp
        manifest["cie_wave3"] = {
            "lane": LANE_ID,
            "review_state": "SUGGESTED",
            "lanes": len(touched),
            "operator_directive": "fire that consume lane (gateway trace "
                                  "1a18bc6701800065)",
            "residual_of_record": "EQFC-CONSUME-1: the wave's unmapped growth "
                                  "joins the verdict fills -> review gate -> v2 "
                                  "consume chain",
            "items_added": grand["items_added"],
            "j0_cascade_sids": grand["j0_sids"],
        }
        manifest_path.write_text(
            json.dumps(manifest, indent=1, ensure_ascii=False) + "\n",
            encoding="utf-8")
        changed = [k for k, v in pre_courses.items()
                   if manifest["courses"].get(k) != v]
        drifted = [k for k, v in json.loads(pre_blocks).items()
                   if manifest.get(k) != v]
        print(f"TOTAL lanes additive={grand['lanes_additive']} "
              f"fresh={grand['lanes_fresh']} "
              f"items_added={grand['items_added']} "
              f"j0_sids={grand['j0_sids']} | "
              f"pre_existing_rows_changed={len(changed)} "
              f"blocks_drifted={len(drifted)}", flush=True)
        if changed:
            print("FATAL: pre-existing manifest rows changed:", changed[:8])
            return 1
        if drifted:
            print("FATAL: pre-existing manifest blocks drifted:", drifted[:8])
            return 1

    # the stats artifact is a pure function of the LANDED sidecars (re-derived
    # every run — idempotent re-runs regenerate it byte-identically instead of
    # clobbering it with the empty delta of a no-op run)
    landed = {}
    for lane in all_lanes:
        p = SPEC_LINKS / f"{lane}.json"
        if not p.exists():
            continue
        sc = json.loads(p.read_text(encoding="utf-8"))
        w3a = (sc.get("anchors") or {}).get("wave3")
        if w3a:
            landed[lane] = {
                "class": w3a.get("class"),
                "new_items": w3a.get("items", w3a.get("itemsAdded")),
                "items_with_codes": w3a.get("items_with_codes",
                                            w3a.get("itemsAddedWithCodes")),
                "pending_refs": w3a.get("pendingRefsAdded", 0),
                "j0": w3a.get("j0", {}),
            }
    grand_landed = {
        "lanes_additive": sum(1 for v in landed.values()
                              if v["class"] == "additive-extension"),
        "lanes_fresh": sum(1 for v in landed.values()
                           if v["class"] == "fresh-build"),
        "items_added": sum(v["new_items"] or 0 for v in landed.values()),
        "j0_sids": sum(v["j0"].get("j0_sids", 0) for v in landed.values()),
        "pending_refs": sum(v["pending_refs"] for v in landed.values()),
    }
    (RES / "graph" / "reports" / "T_SPECS_CIE_WAVE3_JOIN.json").write_text(
        json.dumps({"lane": LANE_ID, "stamp": stamp, "lanes": landed,
                    "grand": grand_landed},
                   indent=1, sort_keys=True) + "\n", encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
