#!/usr/bin/env python3
"""
T-SPECS-CIE-VERDICT-2 battery — VD1-VD10 for the wave-2 AS verdict-fill lane.

Run AFTER scripts/cie_verdict_fill_wave2as.py has applied the verdict fills
to the touched spec-links sidecars + manifest and emitted the sheet + stats.
The base state is read from HEAD (pre-commit); the verdicts are
RE-DERIVED INDEPENDENTLY (fresh pool builders from the raw parsed
registries under a fresh AS scope law, fresh normalization, fresh note-block
substrate read from HEAD blobs, fresh V-rule chain) and the staged sidecars
are never trusted as their own input.

Output: graph/reports/T_SPECS_CIE_VERDICT_2_CHECK.json; exit 0 iff ALL PASS.
"""
from __future__ import annotations

import copy
import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import cie_verdict_fill as vf  # noqa: E402
import cie_verdict_fill_wave2as as eng  # noqa: E402

OUT = REPO / "graph" / "reports" / "T_SPECS_CIE_VERDICT_2_CHECK.json"
LANES = sorted(eng.LANES_2)
METHOD = eng.METHOD
RULES = dict(eng.RULES)
VERDICT_NOTE = eng.VERDICT_NOTE
# ---- independent lane-metadata copies (pinned by the lane records)
SCOPE_AS_ONLY = {"cie-as-chemistry-25", "cie-as-physics-25",
                 "cie-as-business-23"}
SCOPE_DROP_ALEVEL = {"cie-as-computer-science-19"}
DECLARED = ({f"spec-links/{l}.json" for l in LANES}
            | {"spec-links/manifest.json",
               "scripts/cie_verdict_fill_wave2as.py",
               "scripts/cie_verdict_check_wave2as.py",
               "scripts/cie_verdict_wave2as_verdicts.yaml",
               "graph/reports/T_SPECS_CIE_VERDICT_2_RECORD.md",
               "graph/reports/T_SPECS_CIE_VERDICT_2_STATS.json",
               "graph/reports/T_SPECS_CIE_VERDICT_2_CHECK.json"})

results: list[dict] = []


def check(cid: str, fn) -> None:
    try:
        detail = fn()
        results.append({"id": cid, "pass": True, "detail": detail})
        print(f"VD{cid} PASS: {detail}")
    except AssertionError as exc:
        results.append({"id": cid, "pass": False, "detail": str(exc)})
        print(f"VD{cid} FAIL: {exc}")


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def head_json(path: str):
    return json.loads(subprocess.run(
        ["git", "-C", str(REPO), "show", f"HEAD:{path}"],
        capture_output=True, check=True).stdout.decode("utf-8"))


def staged_bytes(path: str) -> bytes:
    ls = subprocess.run(["git", "-C", str(REPO), "ls-files", "-s", "--", path],
                        capture_output=True, check=True).stdout.decode().split()
    if len(ls) < 2:
        raise AssertionError(f"{path} not in index")
    return subprocess.run(["git", "-C", str(REPO), "cat-file", "-p", ls[1]],
                          capture_output=True, check=True).stdout


# ---- independent normalization + pools + note substrate + rule chain
def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def phrase_in(needle: str, hay: str) -> bool:
    if not needle:
        return False
    return (" " + needle + " ") in (" " + hay + " ")


INDEP: dict = {}


def note_blocks(lane: str) -> dict:
    """(sid -> (name, topic_title, section)) fresh from HEAD blobs."""
    out = subprocess.run(
        ["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", "HEAD",
         f"SME-RevisionNotes/{lane}/notes/"], capture_output=True,
        check=True).stdout.decode().splitlines()
    paths = [p for p in out if p.endswith(".json")]
    shas = {}
    for p in paths:
        sha = subprocess.run(
            ["git", "-C", str(REPO), "rev-parse", f"HEAD:{p}"],
            capture_output=True, check=True).stdout.decode().strip()
        shas[sha] = p
    texts = vf.cat_blobs(shas) if hasattr(vf, "cat_blobs") else {}
    if not texts:
        sys.path.insert(0, str(REPO / "scripts"))
        import cie_spec_join as base
        texts = base.cat_blobs(shas)
    blocks: dict[str, tuple] = {}
    conflicts: set = set()
    for p in paths:
        try:
            n = json.loads(texts[p])
        except Exception:
            continue
        tt = (n.get("titles") or {}).get("topic") or ""
        nsec = n.get("section") or ""
        for b in n.get("blocks") or []:
            if b.get("type") == "spec_point" and b.get("id"):
                tup = (b.get("name") or "", tt, nsec)
                if b["id"] in blocks and blocks[b["id"]] != tup:
                    conflicts.add(b["id"])
                    continue
                blocks.setdefault(b["id"], tup)
    return blocks, conflicts


def derive_independent() -> None:
    if INDEP:
        return
    man = json.loads((REPO / "Official-Specifications" / "manifest.json")
                     .read_text())
    quals = {q["slug"]: q for q in man["qualifications"]}
    heads = {l: head_json(f"spec-links/{l}.json") for l in LANES}
    pools, texts, pool_ids = {}, {}, {}
    sub_pts, top_titles, reg_ids = {}, {}, {}
    for l in LANES:
        q = heads[l]["qual"]
        stem = Path(quals[q]["pdf"]).stem
        reg = json.loads((REPO / "Official-Specifications" / "parsed" / q /
                          f"{stem}.parsed.json").read_text())
        reg_ids[l] = reg["id"]
        pts = reg["spec_points"]
        full = len(pts)
        if l in SCOPE_AS_ONLY:
            pts = [p for p in pts if p.get("scope") == "AS Level"]
        elif l in SCOPE_DROP_ALEVEL:
            pts = [p for p in pts if p.get("scope") != "A Level"]
        require(l not in SCOPE_AS_ONLY | SCOPE_DROP_ALEVEL or len(pts) < full,
                f"{l} scope law reduced nothing")
        pools[l] = pts
        texts[l] = [(p, norm(p.get("text"))) for p in pts]
        pool_ids[l] = {p["id"]: str(p.get("official_code")) for p in pts}
        sp: dict[str, list] = {}
        for p in pts:
            st = norm(re.sub(r"\b(notes?|examples?)\b", " ",
                             (p.get("subsection") or {}).get("title") or ""))
            sp.setdefault(st, []).append(p)
        sub_pts[l] = sp
        tt: dict[str, list] = {}
        for p in pts:
            t = p.get("topic") or {}
            tt.setdefault(norm(t.get("title") if isinstance(t, dict)
                               else ""), []).append(p)
        top_titles[l] = tt
    resolves, ambiguous = {}, {}
    stays = Counter()
    pairs = set()
    for l in LANES:
        for key, it in heads[l]["items"].items():
            for sid in (it.get("pending") or []):
                pairs.add((l, sid))
    for l in LANES:
        blocks, conflicts = note_blocks(l)
        INDEP.setdefault("blocks", {})[l] = blocks
        INDEP.setdefault("conflicts", {})[l] = conflicts
    for (l, sid) in sorted(pairs):
        blk = INDEP["blocks"][l].get(sid)
        if blk is None:
            stays["dangling_eq_reference"] += 1
            continue
        if sid in INDEP["conflicts"][l]:
            ambiguous[(l, sid)] = {"lane": l,
                                   "reason": "note_name_conflict_across_blocks"}
            continue
        name, ttopic, nsec = blk
        nn = norm(name)
        if not nn:
            stays["no_unique_identity"] += 1
            continue
        tlist = texts[l]
        eq = [p for p, t in tlist if t and t == nn]
        if len(eq) == 1:
            resolves[(l, sid)] = {"tier": "V1_name_text_identity",
                                  "official_id": eq[0]["id"],
                                  "official_code":
                                      str(eq[0].get("official_code"))}
            continue
        if len(eq) > 1:
            ambiguous[(l, sid)] = {"lane": l, "reason": "name_eq_multi_text"}
            continue
        ph = [p for p, t in tlist if len(nn) >= 3 and phrase_in(nn, t)]
        if len(ph) == 1:
            resolves[(l, sid)] = {"tier": "V2_name_phrase_identity",
                                  "official_id": ph[0]["id"],
                                  "official_code":
                                      str(ph[0].get("official_code"))}
            continue
        if len(ph) > 1:
            scoped, cand = [], None
            for c in (nsec, ttopic):
                nc = norm(c)
                if nc and nc in top_titles[l]:
                    scoped = [p for p in top_titles[l][nc]
                              if phrase_in(nn, norm(p.get("text")))]
                    if len(scoped) == 1:
                        cand = c
                        break
                    scoped = []
            if len(scoped) == 1:
                resolves[(l, sid)] = {
                    "tier": "V5_topic_scoped_phrase_identity",
                    "official_id": scoped[0]["id"],
                    "official_code": str(scoped[0].get("official_code"))}
                continue
            ambiguous[(l, sid)] = {"lane": l,
                                   "reason": "name_phrase_multi_text"}
            continue
        fired = False
        for cand, src in ((name, "spcpt_name"), (ttopic, "note_topic_title")):
            nc = norm(re.sub(r"\b(notes?|examples?)\b", " ", cand or ""))
            if nc and nc in sub_pts[l]:
                if len(sub_pts[l][nc]) == 1:
                    op = sub_pts[l][nc][0]
                    resolves[(l, sid)] = {
                        "tier": "V3_subsection_head_identity",
                        "official_id": op["id"],
                        "official_code": str(op.get("official_code"))}
                else:
                    ambiguous[(l, sid)] = {
                        "lane": l, "reason": "finer_than_official_subsection"}
                fired = True
                break
        if fired:
            continue
        if "literature" in reg_ids[l]:
            seg = norm(name.split(":")[0]) if name else ""
            if seg:
                qh = [p for p, _t in tlist
                      if vf.quoted_title(p.get("text"))
                      and vf.quoted_title(p.get("text")) == seg]
                if len(qh) == 1:
                    resolves[(l, sid)] = {
                        "tier": "V4_settext_title_identity",
                        "official_id": qh[0]["id"],
                        "official_code": str(qh[0].get("official_code"))}
                    continue
                if len(qh) > 1:
                    ambiguous[(l, sid)] = {
                        "lane": l, "reason": "name_phrase_multi_text"}
                    continue
        stays["no_unique_identity"] += 1
    INDEP.update(resolves=resolves, ambiguous=ambiguous, pairs=pairs,
                 heads=heads, pools=pools, pool_ids=pool_ids,
                 stays=stays, universes={
                     l: set(INDEP["blocks"][l]) for l in LANES})


def main() -> int:
    derive_independent()
    resolves: dict = INDEP["resolves"]
    ambiguous: dict = INDEP["ambiguous"]
    touched = sorted({l for (l, _s) in resolves})
    heads = INDEP["heads"]
    staged = {l: json.loads(staged_bytes(f"spec-links/{l}.json"))
              for l in touched}
    lane_res = {l: {sid: v for (ll, sid), v in resolves.items() if ll == l}
                for l in touched}
    stats = json.loads((REPO / "graph" / "reports"
                        / "T_SPECS_CIE_VERDICT_2_STATS.json").read_text())

    def vd1() -> str:
        for l in touched:
            raw = staged_bytes(f"spec-links/{l}.json")
            a, rs = staged[l]["anchors"], staged[l]["review_state"]
            require(list(a.keys())[-1] == "verdict", f"{l} anchors verdict last")
            require(list(rs.keys())[-1] == "verdict", f"{l} rs verdict last")
            vb = a["verdict"]
            require(vb["lane"] == eng.LANE_ID
                    and vb["applied_utc"] == eng.STAMP, f"{l} anchors stamp")
            require(vb["resolved_ids"] == len(lane_res[l]),
                    f"{l} resolved_ids")
            require(vb["note"] == VERDICT_NOTE, f"{l} anchors note")
            require(raw.endswith(b"\n"), f"{l} trailing newline")
            rvb = rs["verdict"]
            require(rvb["state"] == "SUGGESTED", f"{l} state")
            require(rvb["method"] == METHOD
                    and rvb["gateway_trace"] == eng.TRACE
                    and rvb["base_commit"] == eng.PIN,
                    f"{l} rs provenance")
            require(rvb["tiers"] == dict(sorted(RULES.items())),
                    f"{l} tiers")
            # the rejoin + join blocks byte-preserved
            require(rs["rejoin"] == heads[l]["review_state"]["rejoin"],
                    f"{l} rejoin block drifted")
            for key, it in staged[l]["items"].items():
                for c in (it.get("codes") or []):
                    if c.get("method") == METHOD:
                        require(c["tier"] in RULES, f"{l} {key} tier vocab")
        return (f"{len(touched)} touched sidecars well-formed (additive "
                f"verdict blocks appended last, SUGGESTED state, rejoin "
                f"blocks byte-preserved, method/tier vocab)")

    def vd2() -> str:
        for l in touched:
            h, n = heads[l], staged[l]
            require(list(n.keys()) == list(h.keys()), f"{l} top keys")
            for k in ("schema", "generated_utc", "course", "qual", "board",
                      "registry"):
                require(n[k] == h[k], f"{l} {k} drifted")
            require(list(n["review_state"].keys())
                    == list(h["review_state"].keys()) + ["verdict"],
                    f"{l} review_state keys")
            for k in h["review_state"]:
                require(n["review_state"][k] == h["review_state"][k],
                        f"{l} review_state {k} drifted")
            require(list(n["anchors"].keys())
                    == list(h["anchors"].keys()) + ["verdict"],
                    f"{l} anchors keys")
            res_sids = set(lane_res[l])
            uids = INDEP["universes"][l]
            pend_u = set()
            for key in h["items"]:
                ho, no = h["items"][key], n["items"][key]
                require(list(no.keys()) == list(ho.keys()),
                        f"{l} {key} item keys")
                oc = ho.get("codes") or []
                nc = no.get("codes") or []
                require(nc[:len(oc)] == oc, f"{l} {key} codes prefix")
                valid_oids = {v["official_id"] for v in lane_res[l].values()}
                seen_oids = set()
                for c in nc[len(oc):]:
                    require(c["method"] == METHOD and c["tier"] in RULES
                            and c["official_id"] in valid_oids,
                            f"{l} {key} appended code")
                    require(c["official_id"] not in seen_oids,
                            f"{l} {key} dedup violated")
                    seen_oids.add(c["official_id"])
                op_ = ho.get("pending") or []
                np_ = no.get("pending") or []
                require(np_ == [s for s in op_ if s not in res_sids],
                        f"{l} {key} pending delta")
                for k in ho:
                    if k not in ("codes", "pending"):
                        require(no[k] == ho[k], f"{l} {key} {k} drifted")
            for key in h["items"]:
                for s in (staged[l]["items"][key].get("pending") or []):
                    if s in uids:
                        pend_u.add(s)
            require(n["anchors"]["universe_resolved"]
                    == int(n["anchors"]["universe_ids"]) - len(pend_u),
                    f"{l} universe_resolved join semantics")
            for k in h["anchors"]:
                if k == "pending_refs":
                    require(n["anchors"][k] == sum(
                        len(it.get("pending") or [])
                        for it in n["items"].values()),
                        f"{l} pending_refs")
                elif k != "universe_resolved":
                    require(n["anchors"][k] == h["anchors"][k],
                            f"{l} anchors {k} drifted")
        return ("mutation discipline: only codes-append (deduped) / "
                "pending-shrink / additive verdict blocks / recounted "
                "counters (universe_resolved join semantics); every other "
                "field deep-equal to HEAD")

    def vd3() -> str:
        sheet = yaml.safe_load(
            (REPO / "scripts" / "cie_verdict_wave2as_verdicts.yaml")
            .read_text())
        require(sheet["lane"] == eng.LANE_ID
                and sheet["generated_utc"] == eng.STAMP
                and sheet["gateway_trace"] == eng.TRACE
                and sheet["base_commit"] == eng.PIN, "sheet header")
        sh_res = {(e["lane"], e["id"]): e for e in sheet["verdicts"]}
        require(set(sh_res) == set(resolves),
                f"sheet/derived resolve set mismatch: "
                f"{sorted(set(sh_res) ^ set(resolves))[:6]}")
        for k, v in resolves.items():
            e = sh_res[k]
            require(e["tier"] == v["tier"]
                    and e["official_id"] == v["official_id"]
                    and e["official_code"] == v["official_code"],
                    f"{k} sheet resolve mismatch")
            ev = e["evidence"]
            require(bool(ev["sme_name"]) and bool(ev["official_text"])
                    and bool(ev["rule"]), f"{k} evidence fields")
        sh_amb = {(e["lane"], e["id"]): e["reason"]
                  for e in sheet["ambiguous"]}
        require(set(sh_amb) == set(ambiguous),
                f"sheet/derived ambiguous mismatch: "
                f"{sorted(set(sh_amb) ^ set(ambiguous))[:6]}")
        for k, a_entry in ambiguous.items():
            require(sh_amb[k] == a_entry["reason"], f"{k} ambiguous reason")
        return (f"INDEPENDENT re-derivation + sheet bijection: all "
                f"{len(resolves)} resolves + {len(ambiguous)} quarantines "
                f"equal (fresh pools, fresh norm, fresh note substrate, "
                f"fresh rule chain)")

    def vd4() -> str:
        for l in touched:
            h, n = heads[l], staged[l]
            res_sids = set(lane_res[l])
            refs_res = sum(1 for key in h["items"]
                           for s in (h["items"][key].get("pending") or [])
                           if s in res_sids)
            vb = n["anchors"]["verdict"]
            require(vb["resolved_refs"] == refs_res,
                    f"{l} resolved_refs {vb['resolved_refs']} != {refs_res}")
            by_tier = Counter(v["tier"] for v in lane_res[l].values())
            require(vb["by_tier"] == {k: by_tier.get(k, 0)
                                      for k in sorted(RULES)},
                    f"{l} by_tier")
            row = next((r for r in stats["lanes_detail"]
                        if r["lane"] == l), None)
            require(row is not None
                    and row["resolved_ids"] == len(lane_res[l])
                    and row["resolved_refs"] == refs_res
                    and row["pending_refs_after"] == n["anchors"]["pending_refs"],
                    f"{l} stats row")
        tot_codes = sum(sum(1 for it in staged[l]["items"].values()
                            for c in (it.get("codes") or [])
                            if c.get("method") == METHOD)
                        for l in touched)
        require(tot_codes == stats["code_entries_added_total"],
                f"codes total {tot_codes} != stats")
        require(stats["resolved_ids_total"] == len(resolves),
                "stats ids total")
        return (f"cascade integrity (codes dedup-correct, pendings shrunk "
                f"exactly, anchors recounts, stats coherent); "
                f"{tot_codes} code entries")

    def vd5() -> str:
        m = head_json("spec-links/manifest.json")
        nm = json.loads(staged_bytes("spec-links/manifest.json"))
        require(list(nm.keys()) == list(m.keys()) + ["cie_verdict_wave2as"],
                "manifest top keys (additive, appended last)")
        for row_l, row in m["courses"].items():
            if row_l in touched:
                nr = nm["courses"][row_l]
                d = staged[row_l]
                require(nr["items_with_codes"]
                        == d["totals"]["items_with_codes"]
                        and nr["pending_refs"] == d["anchors"]["pending_refs"],
                        f"{row_l} manifest row totals")
                require(nr["verdict"]["resolved_ids"]
                        == d["anchors"]["verdict"]["resolved_ids"],
                        f"{row_l} manifest verdict")
            else:
                require(nm["courses"][row_l] == row,
                        f"{row_l} untouched row drifted")
        require(set(nm["courses"]) == set(m["courses"]), "courses set")
        cv = nm["cie_verdict_wave2as"]
        require(cv["lane"] == eng.LANE_ID and cv["state"] == "SUGGESTED"
                and cv["resolved_ids_total"] == len(resolves)
                and cv["lanes"] == len(touched), "cie_verdict_wave2as block")
        return ("manifest discipline: touched rows updated "
                "value-consistently, all pre-existing rows/keys preserved, "
                "cie_verdict_wave2as block additive + appended last")

    def vd6() -> str:
        st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                            capture_output=True, check=True).stdout.decode()
        seen = {line[3:].strip().strip('"') for line in st.splitlines()}
        extra = sorted(seen - DECLARED)
        require(not extra, f"undeclared paths: {extra[:8]}")
        delta = subprocess.run(
            ["git", "-C", str(REPO), "diff", "HEAD", "--name-only", "--",
             "spec-links/"], capture_output=True, check=True
        ).stdout.decode().splitlines()
        require(set(delta) == {f"spec-links/{l}.json" for l in touched}
                | {"spec-links/manifest.json"},
                f"spec-links delta != touched+manifest: "
                f"{sorted(set(delta))[:6]}")
        for guard in ("SME-ExamQuestion/", "SME-RevisionNotes/",
                      "Official-Specifications/", "SME-Flashcards/"):
            bad = [p for p in seen if p.startswith(guard)]
            require(not bad, f"{guard} touched: {bad[:5]}")
        other = [p for p in subprocess.run(
            ["git", "-C", str(REPO), "ls-tree", "-r", "HEAD", "--name-only",
             "spec-links/"], capture_output=True, check=True
        ).stdout.decode().splitlines()
            if p.endswith(".json") and p != "spec-links/manifest.json"
            and p not in {f"spec-links/{l}.json" for l in LANES}]
        for p in other:
            require(p not in delta, f"out-of-lane sidecar touched: {p}")
        return (f"footprint {len(seen)} paths subset-of declared; spec-links "
                f"delta == {len(touched)} sidecars + manifest; guards intact; "
                f"{len(other)} out-of-lane sidecars untouched")

    def vd7() -> str:
        before = {l: hashlib.sha256(
            staged_bytes(f"spec-links/{l}.json")).hexdigest()
            for l in touched}
        before_m = hashlib.sha256(
            staged_bytes("spec-links/manifest.json")).hexdigest()
        before_s = hashlib.sha256(
            (REPO / "scripts" / "cie_verdict_wave2as_verdicts.yaml")
            .read_bytes()).hexdigest()
        before_j = hashlib.sha256(
            (REPO / "graph" / "reports"
             / "T_SPECS_CIE_VERDICT_2_STATS.json").read_bytes()).hexdigest()
        r = subprocess.run([sys.executable,
                            str(REPO / "scripts"
                                / "cie_verdict_fill_wave2as.py")],
                           capture_output=True, text=True)
        require(r.returncode == 0, f"engine re-run failed: {r.stderr[-400:]}")
        for l in touched:
            require(hashlib.sha256(
                staged_bytes(f"spec-links/{l}.json")).hexdigest()
                == before[l], f"{l} re-run byte drift")
        require(hashlib.sha256(
            staged_bytes("spec-links/manifest.json")).hexdigest()
            == before_m, "manifest re-run drift")
        require(hashlib.sha256(
            (REPO / "scripts" / "cie_verdict_wave2as_verdicts.yaml")
            .read_bytes()).hexdigest() == before_s, "sheet re-run drift")
        require(hashlib.sha256(
            (REPO / "graph" / "reports"
             / "T_SPECS_CIE_VERDICT_2_STATS.json").read_bytes()).hexdigest()
            == before_j, "stats re-run drift")
        return ("engine fixed-stamp re-run byte-identical "
                f"({len(touched)} sidecars + manifest + sheet + stats)")

    def vd8() -> str:
        rec = 0
        for (l, sid) in INDEP["pairs"]:
            if sid not in INDEP["universes"][l]:
                rec += 1
                if l not in staged:
                    continue
                h, n = heads[l], staged[l]
                h_refs = sum(1 for it in h["items"].values()
                             if sid in (it.get("pending") or []))
                n_refs = sum(1 for it in n["items"].values()
                             if sid in (it.get("pending") or []))
                require(h_refs == n_refs and h_refs > 0,
                        f"{l}:{sid} recordless pair mutated")
        require(rec == stats["stays"]["dangling_eq_reference"],
                f"recordless {rec} != stats")
        v4 = sum(1 for v in resolves.values()
                 if v["tier"] == "V4_settext_title_identity")
        require(v4 == 0, f"V4 resolves {v4} != 0 (AS lane class)")
        require(stats["resolves_by_tier"].get("V4_settext_title_identity", 0)
                == 0, "stats V4 != 0")
        # scope law, independently: every resolved id inside the fresh
        # scoped pool AND satisfying the raw scope predicate
        for (l, sid), v in resolves.items():
            require(v["official_id"] in INDEP["pool_ids"][l],
                    f"{l}:{sid} official id outside scoped pool")
            if l in SCOPE_AS_ONLY:
                p = next(p for p in INDEP["pools"][l]
                         if p["id"] == v["official_id"])
                require(p.get("scope") == "AS Level",
                        f"{l}:{sid} raw scope violation")
            if l in SCOPE_DROP_ALEVEL:
                p = next(p for p in INDEP["pools"][l]
                         if p["id"] == v["official_id"])
                require(p.get("scope") != "A Level",
                        f"{l}:{sid} raw scope violation")
        return (f"honesty + scope pins: {rec} record-less pairs still "
                f"pending; V4 == 0 (AS lane class); all {len(resolves)} "
                f"resolves inside their lane's AS-scoped pool (raw "
                f"predicate re-checked)")

    def vd9() -> str:
        rebuild_lanes = touched[:2]
        for l in rebuild_lanes:
            h = heads[l]
            res = lane_res[l]
            code_by_sid = {sid: (v["official_id"], v["official_code"],
                                 v["tier"]) for sid, v in res.items()}
            nd = copy.deepcopy(h)
            for key, it in nd["items"].items():
                pend = it.get("pending") or []
                if not pend:
                    continue
                keep, new_codes = [], []
                seen_oids = {c.get("official_id")
                             for c in (it.get("codes") or [])}
                for sid in pend:
                    if sid in code_by_sid:
                        oid, ocode, tier = code_by_sid[sid]
                        if oid not in seen_oids:
                            seen_oids.add(oid)
                            new_codes.append({"official_id": oid,
                                              "official_code": ocode,
                                              "tier": tier,
                                              "method": METHOD})
                    else:
                        keep.append(sid)
                if new_codes:
                    it["codes"] = (it.get("codes") or []) + new_codes
                it["pending"] = keep
            t = nd["totals"]
            by = {"notes": 0, "question_parts": 0, "flashcards": 0}
            coded = {"notes": 0, "question_parts": 0, "flashcards": 0}
            for it in nd["items"].values():
                by[it["kind"] + "s"] += 1
                coded[it["kind"] + "s"] += 1 if it["codes"] else 0
            t["by_kind"] = by
            t["coded_by_kind"] = coded
            t["items_with_codes"] = sum(coded.values())
            a = nd["anchors"]
            uids = INDEP["universes"][l]
            pend_u = {sid for it in nd["items"].values()
                      for sid in (it.get("pending") or []) if sid in uids}
            a["universe_resolved"] = int(a["universe_ids"]) - len(pend_u)
            a["pending_refs"] = sum(len(it.get("pending") or [])
                                    for it in nd["items"].values())
            res_l = lane_res[l]
            amb_l = sum(1 for (ll, _s) in ambiguous if ll == l)
            dang_l = sum(1 for (ll, sid) in INDEP["pairs"]
                         if ll == l and sid not in uids)
            a["verdict"] = {
                "lane": eng.LANE_ID, "applied_utc": eng.STAMP,
                "resolved_ids": len(res_l),
                "resolved_refs": sum(1 for it in h["items"].values()
                                     for s in (it.get("pending") or [])
                                     if s in code_by_sid),
                "by_tier": {k: sum(1 for v in res_l.values()
                                   if v["tier"] == k)
                            for k in sorted(RULES)},
                "pending_ids": len(pend_u),
                "pending_reasons": staged[l]["anchors"]["verdict"]
                    ["pending_reasons"],
                "dangling_eq_refs_pending": dang_l,
                "scope_law": staged[l]["anchors"]["verdict"]["scope_law"],
                "note": VERDICT_NOTE,
            }
            nd["review_state"]["verdict"] = \
                staged[l]["review_state"]["verdict"]
            rb = json.dumps(nd, ensure_ascii=False, indent=1) + "\n"
            require(rb.encode() == staged_bytes(f"spec-links/{l}.json"),
                    f"{l} rebuild != staged bytes")
        return (f"{len(rebuild_lanes)}-lane full-document rebuild from HEAD "
                f"+ independent resolutions == staged bytes "
                f"({', '.join(rebuild_lanes)})")

    def vd10() -> str:
        m = head_json("spec-links/manifest.json")
        nm = json.loads(staged_bytes("spec-links/manifest.json"))
        pend_head = sum(row["pending_refs"] for row in m["courses"].values()
                        if "pending_refs" in row)
        pend_staged = sum(row["pending_refs"] for row in nm["courses"].values()
                          if "pending_refs" in row)
        require(stats["reconciliation"]["pairs"]
                == stats["reconciliation"]["must_equal"] == len(INDEP["pairs"]),
                "reconciliation pin")
        head_touched = sum(m["courses"][l].get("pending_refs", 0)
                           for l in touched)
        staged_touched = sum(nm["courses"][l].get("pending_refs", 0)
                             for l in touched)
        require(pend_staged - pend_head == staged_touched - head_touched,
                f"manifest cross-foot {pend_head} -> {pend_staged}")
        a_head = sum(head_json(f"spec-links/{l}.json")["anchors"]["pending_refs"]
                     for l in LANES)
        a_staged = sum(json.loads(staged_bytes(f"spec-links/{l}.json"))
                       ["anchors"]["pending_refs"] for l in LANES)
        require(a_head - stats["resolved_refs_total"] == a_staged,
                f"sidecar anchors cross-foot {a_head} -> {a_staged}")
        require(sum(stats["resolves_by_tier"].values()) == len(resolves),
                "by_tier sum pin")
        amb_by_reason = dict(sorted(Counter(
            a["reason"] for a in ambiguous.values()).items()))
        require(stats["ambiguous_by_reason"] == amb_by_reason,
                "ambiguous_by_reason pin")
        return (f"cross-foots: manifest rows {pend_head} -> {pend_staged} "
                f"(touched delta {staged_touched - head_touched}); 8-lane "
                f"sidecar anchors {a_head} -> {a_staged}; reconciliation "
                f"{len(INDEP['pairs'])} pairs exact; ambiguous "
                f"{amb_by_reason}")

    check("1", vd1)
    check("2", vd2)
    check("3", vd3)
    check("4", vd4)
    check("5", vd5)
    check("6", vd6)
    check("7", vd7)
    check("8", vd8)
    check("9", vd9)
    check("10", vd10)

    all_pass = all(r["pass"] for r in results)
    OUT.write_text(json.dumps({
        "battery": "T-SPECS-CIE-VERDICT-2",
        "all_pass": all_pass,
        "checks": results,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\nALL {'PASS' if all_pass else 'FAIL'} "
          f"({sum(r['pass'] for r in results)}/{len(results)})")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
