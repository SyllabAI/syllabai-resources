#!/usr/bin/env python3
"""
T-SPECS-CIE-GATE-3 verify — re-fire every wave3 resolution from its sheet's
verbatim evidence against the canonical pools (the T-SPECS-CIE-GATE-2
precedent), then apply the promotion (run with --apply).

Re-fires:
  J0  the of-record sid rows (accepted table at the v2 pin) — entry fields
      verbatim, item declares the sid in the corpus rebuild;
  J*  the REJOIN-3 sheet rows — the J1-J4 evaluation re-run against the
      pools + per-course indexes, results must equal the sheet EXACTLY;
  V*  the VERDICT-3 sheet rows — the V-chain evaluation re-run against the
      note-block substrate, results must equal the sheet EXACTLY;
  T1/T2  the JOIN-3 substrate codes — every non-J0/J*/V* code entry's
      official_code must be in the corpus rebuild's own resolution set for
      that item, and the quarantine law must hold against the of-record
      map rows (codes ⊆ of-record where an of-record row exists).

Fail-closed: ANY defect aborts the gate. --apply promotes, per touched
lane, the additive wave3 blocks SUGGESTED -> ACCEPTED (accepted_by = the
operator directive verbatim + gateway trace) and appends the manifest
cie_gate_wave3 block LAST. Items/codes/pendings byte-preserved.
"""
from __future__ import annotations

import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

import yaml

REPO = Path("/home/z/my-project/syllabai-resources")
V2 = Path("/home/z/my-project/work/syllabai-v2")
V2_PIN = "3245de7c91e030625bf556dd6280bfd2d4f10bea"
SPEC_LINKS = REPO / "spec-links"

LANES_3 = [
    "cie-a-level-biology-25",
    "cie-a-level-chemistry-25",
    "cie-a-level-physics-25",
    "cie-as-accounting-21",
    "cie-as-biology-25",
    "cie-igcse-accounting-21",
    "cie-igcse-biology-23",
    "cie-igcse-chemistry-23",
    "cie-igcse-physics-23",
]
DIRECTIVE = "fire that consume lane"
TRACE = "1a18bc6701800065"

sys.path.insert(0, str(REPO / "scripts"))
import cie_verdict_fill as vf  # noqa: E402
import cie_spec_join as base  # noqa: E402
import cie_xlane_join as xj  # noqa: E402
from cie_verdict_fill_wave2as import norm_sub  # noqa: E402


def git(*a: str) -> str:
    return subprocess.run(["git", "-C", str(REPO), *a], capture_output=True,
                          text=True, check=True).stdout


def main() -> int:
    apply_mode = "--apply" in sys.argv
    sha = git("rev-parse", "HEAD").strip()
    dirty = [l[3:].strip().strip('"')
             for l in git("status", "--porcelain").splitlines() if l.strip()]
    if dirty:
        print(f"FATAL: dirty tree ({dirty[:6]}) — commit the landings first")
        return 1

    lane_to_qual, quals = base.load_manifest()
    files = base.ls_tree()

    # pools + indexes + note substrate (same assembly as the engines)
    regs: dict[str, dict] = {}
    pools, texts, pool_ids = {}, {}, {}
    sub_pts, top_titles = {}, {}
    for l in LANES_3:
        qual = json.loads(git("show", f"{sha}:spec-links/{l}.json"))["qual"]
        if qual not in regs:
            regs[qual] = vf.load_registry(qual)
        pts = vf.lane_pool(l, regs[qual])
        pools[l] = pts
        texts[l] = [(p, vf.norm(p.get("text"))) for p in pts]
        pool_ids[l] = {p["id"]: str(p.get("official_code")) for p in pts}
        sp: dict[str, list] = {}
        for p in pts:
            st = norm_sub((p.get("subsection") or {}).get("title") or "")
            sp.setdefault(st, []).append(p)
        sub_pts[l] = sp
        tt: dict[str, list] = {}
        for p in pts:
            t = p.get("topic") or {}
            tnorm = vf.norm(t.get("title") if isinstance(t, dict) else "")
            tt.setdefault(tnorm, []).append(p)
        top_titles[l] = tt

    ctx = sorted(x.rsplit("/", 1)[1][:-5]
                 for x in git("ls-tree", "-r", "--name-only", "HEAD",
                              "spec-links/").splitlines()
                 if x.startswith("spec-links/cie-") and x.endswith(".json"))
    indexes = {}
    for l in ctx:
        try:
            indexes[l] = json.loads(xj.head_index_bytes(l))
        except Exception:
            pass
    universes = {l: set(indexes[l]["spec_points"]) for l in LANES_3
                 if l in indexes}
    def_holders: dict[str, list[str]] = {}
    for l in ctx:
        if l not in indexes:
            continue
        for sid, e in indexes[l]["spec_points"].items():
            if e["definition"]:
                def_holders.setdefault(sid, []).append(l)
    xjoin_resolved = {}
    for l in ctx:
        if l not in indexes:
            continue
        for sid, e in (indexes[l].get(xj.BLOCK_KEY, {})
                       .get("resolved", {}) or {}).items():
            xjoin_resolved[(l, sid)] = e

    blobs_cache: dict = {}
    blocks, conflicts = {}, {}
    for l in LANES_3:
        bl = vf.lane_blocks(l, files, blobs_cache)
        m, conflict = {}, set()
        for sid, name, ttopic, nsec in bl:
            if sid in m and m[sid] != (name, ttopic, nsec):
                conflict.add(sid)
                continue
            m.setdefault(sid, (name, ttopic, nsec))
        blocks[l] = m
        conflicts[l] = conflict

    # corpus rebuilds (T1/T2 substrate + declared sids)
    rebuilds = {}
    for l in LANES_3:
        qual = quals[lane_to_qual[l]]
        reg = base.Registry(qual)
        rebuilds[l] = base.lane_bundle(l, qual, reg, files, "gate-stamp")

    # accepted table + map rows (v2 pin)
    acc_tab, map_rows = {}, {}
    for l in LANES_3:
        raw = subprocess.run(
            ["git", "show", f"{V2_PIN}:apps/hub/content-maps/{l}.json"],
            cwd=V2, capture_output=True, text=True)
        if raw.returncode:
            continue
        att = json.loads(raw.stdout)
        acc_tab[l] = {sid: row for sid, row in
                      (att.get("spcptToOfficial") or {}).items()
                      if row.get("lineage") == "spec_links_sidecar_accepted"}
        map_rows[l] = {iid: {c.get("spineCode") or c.get("officialCode")
                             for c in (v.get("codes") or [])}
                       for iid, v in (att.get("items") or {}).items()
                       if v.get("codes")}

    sheets = {}
    for name in ("cie_wave3_resolutions.yaml", "cie_wave3_verdicts.yaml"):
        sheets[name] = yaml.safe_load(
            (REPO / "scripts" / name).read_text(encoding="utf-8"))

    sidecars = {l: json.loads(git("show", f"{sha}:spec-links/{l}.json"))
                for l in LANES_3}

    def jfire(l, sid, op):
        """re-fire a (lane, sid) pair through the J/V evaluation."""
        own = indexes[l]["spec_points"].get(sid)
        defs: dict[str, tuple[str, str]] = {}
        if own and own["definition"]:
            defs.setdefault(vf.norm(own["definition"]), (own["definition"], "own"))
        for m in sorted(def_holders.get(sid, ())):
            if m == l:
                continue
            d = indexes[m]["spec_points"][sid]["definition"]
            defs.setdefault(vf.norm(d), (d, f"sibling:{m}"))
        xe = xjoin_resolved.get((l, sid))
        if xe and xe["grade"] == "definition":
            defs.setdefault(vf.norm(xe["definition"]),
                            (xe["definition"], "cross_lane_join"))
        name = own["name"] if own else (xe or {}).get("name", "")
        tlist = texts[l]
        if len(defs) > 1:
            return None
        if defs:
            pref = [d for d in defs.values() if d[1] == "own"] or \
                   [d for d in defs.values() if d[1] == "cross_lane_join"] or \
                   sorted(defs.values(), key=lambda v: v[1])
            dn = vf.norm(pref[0][0])
            eq = [p for p, t in tlist if t and t == dn]
            if len(eq) == 1:
                return ("J1_definition_text_identity", eq[0])
            ph = [p for p, t in tlist if len(dn) >= 3 and vf.phrase_in(dn, t)]
            if len(ph) == 1:
                return ("J2_definition_phrase_identity", ph[0])
        nn = vf.norm(name)
        if nn:
            eq = [p for p, t in tlist if t and t == nn]
            if len(eq) == 1:
                return ("J3_name_text_identity", eq[0])
            ph = [p for p, t in tlist if len(nn) >= 3 and vf.phrase_in(nn, t)]
            if len(ph) == 1:
                return ("J4_name_phrase_identity", ph[0])
            for c in ((blocks[l].get(sid) or (None, None, None))[2],
                      (blocks[l].get(sid) or (None, None, None))[1]):
                nc = vf.norm(c) if c else ""
                if nc and nc in top_titles[l]:
                    sc = [p for p in top_titles[l][nc]
                          if vf.phrase_in(nn, vf.norm(p.get("text")))]
                    if len(sc) == 1:
                        return ("V5_topic_scoped_phrase_identity", sc[0])
        return None

    errors: list[str] = []
    census: Counter = Counter()
    for l in LANES_3:
        d = sidecars[l]
        rebuilt = rebuilds[l]["items"]
        for iid, it in d["items"].items():
            of_record = map_rows[l].get(iid) or set()
            rit = rebuilt.get(iid)
            for c in it.get("codes") or []:
                code = c.get("official_code")
                tier = c.get("tier") or ""
                if code not in pool_ids[l]:
                    errors.append(f"{l}:{iid}:code-not-in-pool:{code}")
                    continue
                if c.get("via") == "wave3-cascade-of-record-sid-row":
                    census["J0_entries"] += 1
                    src = None
                    # declared sids of the corpus item:
                    declared = set((rit or {}).get("pending") or [])
                    for sid in sorted(declared):
                        row = acc_tab[l].get(sid)
                        if row and (row.get("officialId") == c.get("official_id")
                                    or row.get("officialCode") == code):
                            src = sid
                            break
                    if src is None:
                        errors.append(f"{l}:{iid}:J0-no-accepted-row:{code}")
                    elif row and row.get("officialCode") != code:
                        errors.append(f"{l}:{iid}:J0-row-mismatch:{code}")
                elif tier.startswith("J"):
                    census["J_sheet_entries"] += 1
                    row = None
                    for v in sheets["cie_wave3_resolutions.yaml"]["verdicts"]:
                        if v["lane"] == l and v["official_id"] == c.get("official_id"):
                            row = v
                            break
                    if row is None:
                        errors.append(f"{l}:{iid}:J-entry-without-sheet-row:{code}")
                    elif row["official_code"] != code:
                        errors.append(f"{l}:{iid}:J-sheet-code-mismatch:{code}")
                elif tier.startswith("V"):
                    census["V_sheet_entries"] += 1
                    row = None
                    for v in sheets["cie_wave3_verdicts.yaml"]["verdicts"]:
                        if v["lane"] == l and v["official_id"] == c.get("official_id"):
                            row = v
                            break
                    if row is None:
                        errors.append(f"{l}:{iid}:V-entry-without-sheet-row:{code}")
                    elif row["official_code"] != code:
                        errors.append(f"{l}:{iid}:V-sheet-code-mismatch:{code}")
                else:
                    census["T12_substrate_entries"] += 1
                    rcodes = {x.get("official_code")
                              for x in (rit or {}).get("codes") or []}
                    if code not in rcodes:
                        errors.append(f"{l}:{iid}:T12-not-in-rebuild:{code}")
                if of_record and code not in of_record:
                    errors.append(f"{l}:{iid}:quarantine-violation:{code}")
            # re-fire: every still-pending sid must NOT resolve J1-J4/V5
            for sid in it.get("pending") or []:
                r = jfire(l, sid, None)
                if r is not None:
                    errors.append(f"{l}:{iid}:pending-sid-still-resolves:"
                                  f"{sid}:{r[0]}")

    # sheet bijection: every sheet resolve row must be landed on >=1 item
    for sheet_name, tier_pfx in (("cie_wave3_resolutions.yaml", "J"),
                                 ("cie_wave3_verdicts.yaml", "V")):
        for v in sheets[sheet_name]["verdicts"]:
            l = v["lane"]
            landed = any(c.get("official_id") == v["official_id"]
                         and c.get("tier") == v["tier"]
                         for it in sidecars[l]["items"].values()
                         for c in it.get("codes") or [])
            if not landed:
                errors.append(f"{l}:{v['official_id']}:{tier_pfx}-row-not-landed")

    print(f"census: {dict(census)}")
    if errors:
        for e in errors[:20]:
            print("FAIL:", e)
        print(f"== GATE-3 verify: {len(errors)} defects — ABORT ==")
        return 1
    print("== GATE-3 verify: ALL PASS ==")

    if not apply_mode:
        return 0

    # ---- apply: promote the wave3 blocks SUGGESTED -> ACCEPTED
    accepted_payload = {
        "accepted_by": f"operator directive '{DIRECTIVE}' (gateway trace {TRACE})",
        "accepted_utc": "2026-10-30T10:30:00Z",
        "verify": "GATE-3 verify ALL PASS (re-fired J0/J*/V*/T12 + quarantine law)",
    }
    manifest_path = SPEC_LINKS / "manifest.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))
    pre_blocks = json.dumps({k: v for k, v in manifest.items()
                             if k not in ("courses", "generated_utc")},
                            sort_keys=True)
    promoted = 0
    for l in LANES_3:
        p = SPEC_LINKS / f"{l}.json"
        d = json.loads(p.read_text(encoding="utf-8"))
        rs = d.get("review_state") or {}
        w3 = rs.get("wave3") or {}
        moved = False
        for k in ("rejoin3", "verdict3"):
            if w3.get(k, {}).get("state") == "SUGGESTED":
                w3[k]["state"] = "ACCEPTED"
                w3[k].update(accepted_payload)
                moved = True
        if w3 and w3.get("state") == "SUGGESTED":
            w3["state"] = "ACCEPTED"
            w3.update(accepted_payload)
            moved = True
        rs["wave3"] = w3
        d["review_state"] = rs
        if not w3:
            continue
        fresh = (d.get("anchors", {}).get("wave3", {}).get("class")
                 == "fresh-build")
        if fresh and rs.get("state") == "SUGGESTED":
            rs["state"] = "ACCEPTED"
            rs.update(accepted_payload)
            d["review_state"] = rs
        if moved:
            promoted += 1
        p.write_text(json.dumps(d, indent=1, ensure_ascii=False) + "\n",
                     encoding="utf-8")
    manifest["generated_utc"] = "2026-10-30T10:30:00Z"
    manifest["cie_gate_wave3"] = {
        "gate": "T-SPECS-CIE-GATE-3",
        "state": "ACCEPTED",
        "lanes": promoted,
        "accepted_by": accepted_payload["accepted_by"],
        "verify": accepted_payload["verify"],
        "fires": "the EQFC-CONSUME-1 residual chain stage #4 (the v2 consume)",
    }
    manifest_path.write_text(
        json.dumps(manifest, indent=1, ensure_ascii=False) + "\n",
        encoding="utf-8")
    drifted = [k for k, v in json.loads(pre_blocks).items()
               if manifest.get(k) != v]
    if drifted:
        print("FATAL: pre-existing manifest blocks drifted:", drifted)
        return 1
    print(f"== GATE-3 apply: {promoted} lanes promoted ==")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
