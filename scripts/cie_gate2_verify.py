#!/usr/bin/env python3
"""
T-SPECS-CIE-GATE-2 — independent verifier for the wave-2 AS chain
review/promotion gate (runs BEFORE the applier; the applier refuses on any
FAIL). The GATE-1 / REJOIN-GATE-1 precedent composed over the three
resolution classes of the wave-2 chain:

  V-class  the 18 VERDICT-2 operator-verdict fills re-fired from the
           verdict sheet's verbatim evidence (V3: head == artifact-stripped
           single-point subsection title, uniqueness re-checked over the
           FULL AS-scoped pool; official_text verbatim vs pool; the pair
           must be OUT of every item's pendings at HEAD and IN the codes
           with method operator_verdict; V4 pinned 0).
  J-class  the 124 REJOIN-2 index re-join resolutions re-fired from the
           re-join sheet (J1-J4 with the same evidence re-fire, uniqueness
           re-checks, scoping recomputed from ZERO_LANES + the lane's index
           universe — the AS lanes are not ZERO_LANES, so the gate pins
           verdict_evaluated == False for every pair).
  T2-class the 49 JOIN-2 T2_near anchors audited with the GATE-1 V3
           lower-bound method (per-anchor: definition-line Jaccard >= 0.55
           against either pool, OR name == point-text tokens with a line
           >= 0.35, OR name == the official subsection title), pools
           bounded by the AS scope law, anchors read fresh from HEAD blobs.
  State    the SUGGESTED states of record (top-level review_state from
           JOIN-2, rejoin on the 7 touched lanes, verdict on the 2 touched
           lanes) must be exactly as the lane records left them.
  Defects  the 11 inherited in-item REJOIN-2 duplicates are pinned at their
           disclosed census (known-defect disclosure, not a gate failure —
           the consume lane dedups per official_id at attach time).

Output: graph/reports/T_SPECS_CIE_GATE_2_VERIFY.json
{verdict: PASS|FAIL, verified, failed, failures[], counts}. Exit 0 iff PASS.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path("/home/z/my-project/syllabai-resources")
SL = REPO / "spec-links"
REPORTS = REPO / "graph" / "reports"
sys.path.insert(0, str(REPO / "scripts"))
import cie_verdict_fill as vf  # noqa: E402
import cie_index_rejoin_wave2as as rj2  # noqa: E402
import cie_verdict_fill_wave2as as veng  # noqa: E402

GATE = "T-SPECS-CIE-GATE-2"
STAMP = "2026-10-29T14:00:00Z"
DIRECTIVE = "verdict fills -> review gate -> v2 consume"
TRACE = "1a183e66619bd6dd"
BASE_COMMIT = "b97a80c72bcba64546b376746efac76fd7847737"
VERIFY_OUT = REPORTS / "T_SPECS_CIE_GATE_2_VERIFY.json"
VSHEET = REPO / "scripts" / "cie_verdict_wave2as_verdicts.yaml"
JSHEET = REPO / "scripts" / "cie_rejoin_wave2as_resolutions.yaml"
VSTATS = REPORTS / "T_SPECS_CIE_VERDICT_2_STATS.json"
JSTATS = REPORTS / "T_SPECS_CIE_REJOIN_2_STATS.json"

LANES = list(rj2.LANES_2)
REJOIN_METHOD = "cie_index_rejoin_wave2as"
JOIN_METHODS = {"cie_definition_text_join"}
KNOWN_DEFECT_DUP_ITEMS = 11


def git_show_text(path: str) -> str:
    r = subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{path}"],
                       capture_output=True, check=True)
    return r.stdout.decode("utf-8", "replace")


def main() -> int:
    import time
    t0 = time.time()
    failures: list[str] = []

    head = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                          capture_output=True, check=True).stdout.decode().strip()
    if head != BASE_COMMIT:
        print(f"FATAL: HEAD {head[:12]} != gate base {BASE_COMMIT[:12]}")
        return 1

    lane_to_qual, quals = {}, {}
    man = json.loads((REPO / "Official-Specifications" / "manifest.json")
                     .read_text())
    for q in man["qualifications"]:
        if str(q.get("slug", "")).startswith("cie-"):
            quals[q["slug"]] = q
            for lane in q.get("sme_courses") or []:
                lane_to_qual[lane] = q["slug"]

    sidecars = {l: json.loads(git_show_text(f"spec-links/{l}.json"))
                for l in LANES}
    indexes = {l: json.loads(git_show_text(
        f"SME-ExamQuestion/{l}/spec_point_index.json")) for l in LANES}
    universes = {l: set(indexes[l]["spec_points"]) for l in LANES}
    zero = set(vf.ZERO_LANES)

    # scoped pools per lane (fresh from the parsed registries)
    pools, texts = {}, {}
    for l in LANES:
        reg = __import__("cie_spec_join").Registry(quals[lane_to_qual[l]])
        pts, _note = rj2.scoped_pool(l, reg)
        pools[l] = pts
        texts[l] = [(p, vf.norm(p.get("text"))) for p in pts]

    vsheet = yaml.safe_load(VSHEET.read_text(encoding="utf-8"))
    jsheet = yaml.safe_load(JSHEET.read_text(encoding="utf-8"))
    vstats = json.loads(VSTATS.read_text(encoding="utf-8"))
    jstats = json.loads(JSTATS.read_text(encoding="utf-8"))

    pending_pairs = set()
    code_index: dict[tuple, bool] = {}
    dup_items = 0
    t2_by_lane: dict[str, int] = {}
    for l in LANES:
        t2_by_lane[l] = 0
        for key, it in sidecars[l]["items"].items():
            for sid in (it.get("pending") or []):
                pending_pairs.add((l, sid))
            entries = [c for c in (it.get("codes") or [])]
            ids = {}
            for c in entries:
                m, oid = c.get("method"), c.get("official_id")
                if m == REJOIN_METHOD:
                    ids.setdefault(oid, 0)
                    ids[oid] += 1
                if m in JOIN_METHODS:
                    t2_by_lane[l] += 1
            if any(v > 1 for v in ids.values()):
                dup_items += 1

    # ---------- V-class re-fire (18)
    def lane_has(lane, oid, tier, method):
        return any(c.get("method") == method
                   and c.get("official_id") == oid and c.get("tier") == tier
                   for it in sidecars[lane]["items"].values()
                   for c in (it.get("codes") or []))

    v_verified = 0
    for v in vsheet["verdicts"]:
        l, sid, tier = v["lane"], v["id"], v["tier"]
        ev = v["evidence"]
        oid, ocode = v["official_id"], v["official_code"]
        if (l, sid) in pending_pairs:
            failures.append(f"V {l}:{sid}: pair still pending at HEAD")
        if not lane_has(l, oid, tier, veng.METHOD):
            failures.append(f"V {l}:{sid}: no operator_verdict code entry")
        pts = [p for p in pools[l] if p["id"] == oid]
        if len(pts) != 1:
            failures.append(f"V {l}:{sid}: official id not unique in pool")
            continue
        p = pts[0]
        if str(p.get("official_code")) != ocode:
            failures.append(f"V {l}:{sid}: official_code mismatch")
        if vf.norm(p.get("text") or "") != vf.norm(ev.get("official_text") or ""):
            failures.append(f"V {l}:{sid}: official_text mismatch vs pool")
        if l in rj2.SCOPE_AS_ONLY and p.get("scope") != "AS Level":
            failures.append(f"V {l}:{sid}: scope law violation")
        if l in rj2.SCOPE_DROP_ALEVEL and p.get("scope") == "A Level":
            failures.append(f"V {l}:{sid}: scope law violation")
        if tier != "V3_subsection_head_identity":
            failures.append(f"V {l}:{sid}: unexpected tier {tier} for the "
                            "wave-2 class")
            continue
        # re-derive the head from the recorded evidence and re-fire V3
        head_cand = ev.get("head")
        if not head_cand:
            failures.append(f"V {l}:{sid}: V3 evidence missing head")
            continue
        nc = vf.norm(vf.ARTIFACT.sub(" ", head_cand))
        sub_hits = [p2 for p2 in pools[l]
                    if vf.norm(vf.ARTIFACT.sub(
                        " ", (p2.get("subsection") or {}).get("title")
                        or "")) == nc]
        if len(sub_hits) != 1 or sub_hits[0]["id"] != oid:
            failures.append(f"V {l}:{sid}: V3 did not re-fire uniquely "
                            f"(head {nc!r} -> {len(sub_hits)} hits)")
            continue
        v_verified += 1
    v4 = sum(1 for v in vsheet["verdicts"]
             if v["tier"] == "V4_settext_title_identity")
    if v4:
        failures.append(f"V: {v4} V4 resolves (pinned 0)")
    if len(vsheet["verdicts"]) != vstats["resolved_ids_total"]:
        failures.append("V: sheet size != verdict stats")

    # ---------- J-class re-fire (124)
    j_verified = 0
    for v in jsheet["verdicts"]:
        l, sid, tier = v["lane"], v["id"], v["tier"]
        ev = v["evidence"]
        oid, ocode = v["official_id"], v["official_code"]
        if (l, sid) in pending_pairs:
            failures.append(f"J {l}:{sid}: pair still pending at HEAD")
        if not lane_has(l, oid, tier, REJOIN_METHOD):
            failures.append(f"J {l}:{sid}: no rejoin code entry")
        pts = [p for p in pools[l] if p["id"] == oid]
        if len(pts) != 1:
            failures.append(f"J {l}:{sid}: official id not unique in pool")
            continue
        p = pts[0]
        if str(p.get("official_code")) != ocode:
            failures.append(f"J {l}:{sid}: official_code mismatch")
        if vf.norm(p.get("text") or "") != vf.norm(ev.get("official_text") or ""):
            failures.append(f"J {l}:{sid}: official_text mismatch vs pool")
        verdict_evaluated = l in zero and sid in universes[l]
        if verdict_evaluated:
            failures.append(f"J {l}:{sid}: verdict-evaluated pair in an AS "
                            "lane class")
        name_norm = vf.norm(ev.get("sme_name") or "")
        tlist = texts[l]
        hit_ok = False
        if tier == "J1_definition_text_identity":
            dn = vf.norm(ev.get("sme_definition") or "")
            eq = [q for q, t in tlist if t and t == dn]
            hit_ok = (len(eq) == 1 and eq[0]["id"] == oid)
        elif tier == "J2_definition_phrase_identity":
            dn = vf.norm(ev.get("sme_definition") or "")
            ph = [q for q, t in tlist
                  if len(dn) >= 3 and vf.phrase_in(dn, t)]
            hit_ok = (len(ph) == 1 and ph[0]["id"] == oid)
        elif tier == "J3_name_text_identity":
            eq = [q for q, t in tlist if t and t == name_norm]
            hit_ok = (len(eq) == 1 and eq[0]["id"] == oid)
        elif tier == "J4_name_phrase_identity":
            ph = [q for q, t in tlist
                  if len(name_norm) >= 3 and vf.phrase_in(name_norm, t)]
            hit_ok = (len(ph) == 1 and ph[0]["id"] == oid)
        else:
            failures.append(f"J {l}:{sid}: unknown tier {tier}")
        if hit_ok:
            j_verified += 1
        else:
            failures.append(f"J {l}:{sid}: rule {tier} did not re-fire "
                            "uniquely")
    if len(jsheet["verdicts"]) != jstats["resolved_pairs_total"]:
        failures.append("J: sheet size != rejoin stats")

    # ---------- T2-class lower-bound audit (49, GATE-1 V3 method)
    files = {}
    out = subprocess.run(["git", "-C", str(REPO), "ls-tree", "-r", "HEAD"],
                         capture_output=True, check=True).stdout.decode()
    for line in out.splitlines():
        meta, _, path = line.partition("\t")
        parts = meta.split()
        if len(parts) >= 3 and parts[1] == "blob":
            files[path] = parts[2]

    def jac(a: set, b: set) -> float:
        if not a or not b:
            return 0.0
        return len(a & b) / len(a | b)

    t2_total = t2_ok = 0
    for l in LANES:
        if not t2_by_lane[l]:
            continue
        reg = {p["id"]: p for p in pools[l]}
        note_paths = [p for p in files
                      if p.startswith(f"SME-RevisionNotes/{l}/notes/")
                      and p.endswith(".json")]
        eq_paths = [p for p in files
                    if p.startswith(f"SME-ExamQuestion/{l}/")
                    and p.endswith("/topic.json")]
        shas = {files[p]: p for p in note_paths + eq_paths}
        blobs = vf.cat_blobs(shas)
        uni = {}
        anchors: dict[str, list] = {}
        for p in note_paths:
            try:
                n = json.loads(blobs[p])
            except Exception:
                continue
            for b in n.get("blocks") or []:
                if b.get("type") == "spec_point" and b.get("id"):
                    u = uni.setdefault(b["id"], {"name": b.get("name"),
                                                 "definition": b.get("definition")})
                    if not u.get("definition") and b.get("definition"):
                        u["definition"] = b["definition"]
            for sid in n.get("spec_point_ids") or []:
                anchors.setdefault(n.get("note_id"), []).append(sid)
        for p in eq_paths:
            try:
                t = json.loads(blobs[p])
            except Exception:
                continue
            for q in t.get("questions") or []:
                for part in q.get("parts") or []:
                    for sid in part.get("spec_point_ids") or []:
                        anchors.setdefault(part["id"], []).append(sid)
        anchor_lines = {}
        for sid, u in uni.items():
            lls = []
            for ln in (u.get("definition") or "").split("\n"):
                tk = set(vf.norm(ln).split())
                if tk:
                    lls.append(tk)
            anchor_lines[sid] = (set(vf.norm(u.get("name") or "").split()),
                                 lls)
        pools2 = {}
        for pid, p in reg.items():
            base_t = set(vf.norm(p.get("text") or "").split())
            sub = " ".join(p.get("sub_items") or [])
            withsub = base_t | set(vf.norm(
                (p.get("text") or "") + " " + sub).split())
            pools2[pid] = [base_t, withsub] if base_t != withsub else [base_t]
        for cid, item in sidecars[l]["items"].items():
            anch = [a for a in anchors.get(cid, []) if a in uni]
            for c in item.get("codes") or []:
                if c.get("tier") != "T2_near":
                    continue
                pid = c["official_id"]
                t2_total += 1
                if pid not in reg:
                    failures.append(f"T2 {l}:{cid}:{pid}:not-in-scoped-pool")
                    continue
                weak = False
                ssec = reg[pid].get("subsection") or {}
                title_tk = set(vf.norm(ssec.get("title") or "").split())
                for a in anch:
                    nt, lls = anchor_lines[a]
                    for lt in lls:
                        for pool in pools2[pid]:
                            if jac(lt, pool) >= 0.55:
                                weak = True
                                break
                        if weak:
                            break
                    if not weak and nt:
                        ptoks = pools2[pid][0]
                        if nt == ptoks and any(jac(lt, ptoks) >= 0.35
                                               for lt in lls):
                            weak = True
                    if not weak and nt and nt == title_tk:
                        weak = True
                    if weak:
                        break
                if weak:
                    t2_ok += 1
                else:
                    failures.append(f"T2 {l}:{cid}:{pid}:T2-unverified")

    # ---------- state-of-record pins
    for l in LANES:
        rs = sidecars[l]["review_state"]
        if rs.get("state") != "SUGGESTED" or rs.get("gate") != "pending":
            failures.append(f"{l}: top-level review_state not the JOIN-2 "
                            "SUGGESTED/pending state of record")
        if l != "cie-as-maths-20-pure-2":
            if "rejoin" not in rs or rs["rejoin"].get("state") != "SUGGESTED":
                failures.append(f"{l}: rejoin block not SUGGESTED")
        elif "rejoin" in rs:
            failures.append("pure-2: unexpected rejoin block")
        if l in ("cie-as-business-23", "cie-as-chemistry-25"):
            if "verdict" not in rs or rs["verdict"].get("state") != "SUGGESTED":
                failures.append(f"{l}: verdict block not SUGGESTED")
        elif "verdict" in rs:
            failures.append(f"{l}: unexpected verdict block")
    if dup_items != KNOWN_DEFECT_DUP_ITEMS:
        failures.append(f"inherited duplicate census {dup_items} != "
                        f"{KNOWN_DEFECT_DUP_ITEMS} (the disclosed REJOIN-2 "
                        "known-defect state moved)")

    # ---------- ambiguous quarantines stay pending
    amb_pending = sum(1 for a in jsheet["ambiguous"]
                      if (a["lane"], a["id"]) in pending_pairs)
    vamb_pending = sum(1 for a in vsheet["ambiguous"]
                       if (a["lane"], a["id"]) in pending_pairs)
    if amb_pending != len(jsheet["ambiguous"]):
        failures.append("J: some quarantined pairs left pending")
    if vamb_pending != len(vsheet["ambiguous"]):
        failures.append("V: some quarantined pairs left pending")

    verified = v_verified + j_verified + t2_ok
    total = len(vsheet["verdicts"]) + len(jsheet["verdicts"]) + t2_total
    out = {
        "gate": GATE, "generated_utc": STAMP, "directive": DIRECTIVE,
        "gateway_trace": TRACE, "base_commit": BASE_COMMIT,
        "verdict": "PASS" if not failures else "FAIL",
        "sheet_verdicts": total,
        "verified": verified,
        "failed": total - verified,
        "verified_by_class": {"V": v_verified, "J": j_verified, "T2": t2_ok},
        "totals_by_class": {"V": len(vsheet["verdicts"]),
                            "J": len(jsheet["verdicts"]),
                            "T2": t2_total},
        "code_entries_total": {"V": vstats["code_entries_added_total"],
                               "J": jstats["code_entries_added_total"],
                               "T2": sum(t2_by_lane.values())},
        "ambiguous_stay_quarantined": {"J": len(jsheet["ambiguous"]),
                                       "V": len(vsheet["ambiguous"])},
        "inherited_dup_items_pinned": dup_items,
        "failures": failures[:50],
        "failures_total": len(failures),
        "elapsed_seconds": round(time.time() - t0, 1),
    }
    VERIFY_OUT.write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")
    print(json.dumps({k: out[k] for k in
                      ("verdict", "verified", "failed",
                       "verified_by_class", "totals_by_class",
                       "inherited_dup_items_pinned")}))
    if failures:
        for f in failures[:20]:
            print("FAIL:", f, file=sys.stderr)
    return 0 if out["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
