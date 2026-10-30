#!/usr/bin/env python3
"""
T-SPECS-CIE-JOIN-3 battery — WJ1-WJ8 (independent re-derivation against HEAD;
the sidecar landing must already be committed).
"""
from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

REPO = Path("/home/z/my-project/syllabai-resources")
V2 = Path("/home/z/my-project/work/syllabai-v2")
V2_PIN = "3245de7c91e030625bf556dd6280bfd2d4f10bea"

sys.path.insert(0, str(REPO / "scripts"))
import cie_spec_join as base  # noqa: E402
import cie_spec_join_wave2as as j2  # noqa: E402
import cie_verdict_fill as vf  # noqa: E402

fails: list[str] = []
oks: list[str] = []


def check(name: str, cond: bool, detail: str = "") -> None:
    (oks if cond else fails).append(f"{name}{': ' + detail if detail else ''}")
    print(("PASS " if cond else "FAIL ") + name + (f" — {detail}" if detail else ""))


def git(*a: str) -> str:
    return subprocess.run(["git", "-C", str(REPO), *a], capture_output=True,
                          text=True, check=True).stdout


def v2blob(path: str) -> dict:
    return json.loads(subprocess.run(
        ["git", "show", f"{V2_PIN}:{path}"], cwd=V2, capture_output=True,
        text=True, check=True).stdout)


def main() -> int:
    head = git("rev-parse", "HEAD").strip()
    prev = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD~1"],
                          capture_output=True, text=True).stdout.strip()

    join_report = json.loads((REPO / "graph" / "reports" /
                              "T_SPECS_CIE_WAVE3_JOIN.json").read_text())
    lanes = sorted(join_report["lanes"])

    lane_to_qual, quals = base.load_manifest()
    files = base.ls_tree()

    all_new_items: dict[str, set] = {}
    pre_sidecars: dict[str, dict] = {}
    for l in lanes:
        pre_sidecars[l] = json.loads(subprocess.run(
            ["git", "show", f"{prev}:spec-links/{l}.json"],
            capture_output=True, text=True,
            cwd=str(REPO)).stdout or "null") if prev else None
    # fresh-build lanes have no pre sidecar (404) — detect and treat
    fresh = [l for l in lanes if pre_sidecars.get(l) is None]
    additive = [l for l in lanes if l not in fresh]

    # ---- WJ1: schema/shape of every touched sidecar
    for l in lanes:
        d = json.loads((REPO / "spec-links" / f"{l}.json").read_text())
        ok = d.get("schema") == "syllabai.learner-spec-links/1.0" and \
            isinstance(d.get("items"), dict) and d.get("board") == "cambridge-cie"
        for iid, it in d["items"].items():
            if not ("kind" in it and it["kind"] in ("note", "question_part")
                    and "codes" in it and "pending" in it):
                ok = False
                break
        check(f"WJ1 {l}", ok)

    # ---- WJ2: pre-existing sidecar surface byte-identical (additive lanes)
    for l in additive:
        pre = pre_sidecars[l]
        cur = json.loads((REPO / "spec-links" / f"{l}.json").read_text())
        same_items = all(json.dumps(pre["items"][k], sort_keys=True) ==
                         json.dumps(cur["items"].get(k), sort_keys=True)
                         for k in pre["items"])
        blocks_kept = all(json.dumps(pre["anchors"].get(k), sort_keys=True) ==
                          json.dumps(cur["anchors"].get(k), sort_keys=True)
                          for k in pre.get("anchors", {}) if k != "wave3")
        rs_kept = all(json.dumps(pre["review_state"].get(k), sort_keys=True) ==
                      json.dumps(cur["review_state"].get(k), sort_keys=True)
                      for k in pre.get("review_state", {}) if k != "wave3")
        check(f"WJ2 {l}", same_items and blocks_kept and rs_kept,
              f"items={len(pre['items'])}")

    # ---- WJ3/WJ4/WJ5/WJ8 per lane (re-derive the wave items independently)
    grand_new = 0
    for l in lanes:
        cur = json.loads((REPO / "spec-links" / f"{l}.json").read_text())
        pre = pre_sidecars[l]
        pre_ids = set((pre or {}).get("items") or {})
        new_ids = set(cur["items"]) - pre_ids
        all_new_items[l] = new_ids
        grand_new += len(new_ids)

        qual = quals[lane_to_qual[l]]
        reg = base.Registry(qual)
        rebuilt = base.lane_bundle(l, qual, reg, files, "battery-stamp")
        exp = set(rebuilt["items"]) - pre_ids
        check(f"WJ3 {l} universe-faithful", exp == new_ids,
              f"engine={len(new_ids)} rederived={len(exp)}")

        # pending/codes provenance: pendings must be declared sids (rebuilt),
        # possibly minus J0-cascaded; codes must be subset of rebuilt codes ∪
        # accepted-row codes, with quarantine honoured
        acc_raw = subprocess.run(
            ["git", "show", f"{V2_PIN}:apps/hub/content-maps/{l}.json"],
            cwd=V2, capture_output=True, text=True)
        acc = {} if acc_raw.returncode else {
            sid: row for sid, row in json.loads(acc_raw.stdout)
            .get("spcptToOfficial", {}).items()
            if row.get("lineage") == "spec_links_sidecar_accepted"}
        mapcodes = {} if acc_raw.returncode else {
            iid: {c.get("spineCode") or c.get("officialCode")
                  for c in (v.get("codes") or [])}
            for iid, v in json.loads(acc_raw.stdout).get("items", {}).items()
            if v.get("codes")}
        j0 = quar = t12 = 0
        bad = []
        # expected j0 resolution events: rebuilt pendings with an accepted row
        # that is not quarantined by the item's of-record row
        j0_events = 0
        reg2 = vf.load_registry(cur["qual"])
        pts = vf.lane_pool(l, reg2)
        pool = {str(p.get("official_code")) for p in pts}
        for iid in sorted(new_ids):
            it = cur["items"][iid]
            rit = rebuilt["items"].get(iid)
            if rit is None:
                bad.append(f"{iid}:absent-from-rebuild")
                continue
            of_record_pre = mapcodes.get(iid) or set()
            for sid in (rit.get("pending") or []):
                row = acc.get(sid)
                if row and row.get("officialCode") and \
                        (not of_record_pre or
                         row["officialCode"] in of_record_pre):
                    j0_events += 1
            # every pending sid must be declared-but-unresolved substrate
            for sid in it.get("pending") or []:
                if sid not in (rit.get("pending") or []):
                    bad.append(f"{iid}:pending-not-substrate:{sid}")
            of_record = mapcodes.get(iid) or set()
            for c in it.get("codes") or []:
                code = c.get("official_code")
                if code not in pool:
                    bad.append(f"{iid}:code-not-in-pool:{code}")
                if c.get("via") == "wave3-cascade-of-record-sid-row":
                    j0 += 1
                    src = None
                    for sid in (rit.get("pending") or []) + \
                            [s for s in (rit.get("pending") or [])]:
                        row = acc.get(sid)
                        if row and (row.get("officialId") == c.get("official_id")
                                    or row.get("officialCode") == code):
                            src = sid
                            break
                    if src is None:
                        bad.append(f"{iid}:j0-no-accepted-row:{code}")
                    elif of_record and code not in of_record:
                        bad.append(f"{iid}:j0-quarantine-violation:{code}")
                else:
                    if of_record and code not in of_record:
                        t12 += 1
        j0_census = dict(cur["anchors"].get("wave3", {}).get("j0", {}))
        # replay oracle: re-run the engine's cascade over the rebuilt items;
        # the replay counter must equal the census AND the replayed codes and
        # pendings must equal the landed state exactly
        import cie_spec_join_wave3 as eng  # noqa: E402
        replay = json.loads(json.dumps(
            {iid: rebuilt["items"][iid] for iid in new_ids}))
        rep_st = eng.j0_cascade(replay, acc, mapcodes)
        replay_ok = dict(rep_st) == j0_census and all(
            json.dumps(replay[iid].get("codes"), sort_keys=True) ==
            json.dumps(cur["items"][iid].get("codes"), sort_keys=True) and
            json.dumps(replay[iid].get("pending"), sort_keys=True) ==
            json.dumps(cur["items"][iid].get("pending"), sort_keys=True)
            for iid in new_ids)
        wj4_ok = not bad and replay_ok and j0 == sum(
            1 for iid in new_ids
            for c in cur["items"][iid].get("codes") or []
            if c.get("via") == "wave3-cascade-of-record-sid-row")
        check(f"WJ4 {l} j0+quarantine law", wj4_ok,
              f"j0={j0} t12q={t12} bad={bad[:3]}")

        # WJ8: totals cross-foot
        t = cur["totals"]
        by, coded = Counter(), Counter()
        for it in cur["items"].values():
            by[it["kind"] + "s"] += 1
            coded[it["kind"] + "s"] += 1 if it["codes"] else 0
        kinds = ("notes", "question_parts", "flashcards")
        xfoot = all(t["by_kind"].get(k, 0) == by.get(k, 0) for k in kinds) and \
            all(t["coded_by_kind"].get(k, 0) == coded.get(k, 0) for k in kinds) and \
            t["items"] == len(cur["items"]) and \
            t["items_with_codes"] == sum(coded.values()) and \
            t["items"] - len(pre_ids) == len(new_ids)
        check(f"WJ8 {l} census cross-foot", xfoot,
              f"items={t['items']} (+{len(new_ids)})")

    check("WJ3 grand item count",
          grand_new == join_report["grand"]["items_added"],
          f"{grand_new} vs {join_report['grand']['items_added']}")

    # ---- WJ5: scope law note present on fresh builds
    for l in fresh:
        d = json.loads((REPO / "spec-links" / f"{l}.json").read_text())
        check(f"WJ5 {l} scope_law disclosed",
              "scope_law" in d.get("anchors", {}))

    # ---- WJ6: idempotence (engine re-run must be a byte no-op)
    import hashlib
    before = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
              for p in sorted((REPO / "spec-links").glob("*.json"))}
    r = subprocess.run([sys.executable, str(REPO / "scripts" /
                                            "cie_spec_join_wave3.py")],
                       capture_output=True, text=True)
    after = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
             for p in sorted((REPO / "spec-links").glob("*.json"))}
    check("WJ6 idempotent re-run", r.returncode == 0 and before == after)

    # ---- WJ7: manifest additive (pre rows/blocks preserved; fresh-lane
    # course rows are the allowed delta)
    m = json.loads((REPO / "spec-links" / "manifest.json").read_text())
    mprev = json.loads(subprocess.run(
        ["git", "show", f"{prev}:spec-links/manifest.json"],
        capture_output=True, text=True, cwd=str(REPO)).stdout)
    kept = all(json.dumps(mprev[k], sort_keys=True) == json.dumps(m.get(k),
                                                                  sort_keys=True)
               for k in mprev if k not in ("generated_utc", "courses"))
    courses_ok = all(k in m.get("courses", {}) for k in mprev.get("courses", {})) and \
        set(m.get("courses", {})) - set(mprev.get("courses", {})) <= set(fresh)
    check("WJ7 manifest additive", kept and courses_ok and "cie_wave3" in m)

    print(f"\n== JOIN-3 battery: {len(oks)} PASS / {len(fails)} FAIL ==")
    return 1 if fails else 0


if __name__ == "__main__":
    raise SystemExit(main())
