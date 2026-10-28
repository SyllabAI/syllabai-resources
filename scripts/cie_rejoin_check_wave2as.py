#!/usr/bin/env python3
"""
T-SPECS-CIE-REJOIN-2 battery — RJ1-RJ10 for the wave-2 AS index re-join lane.

Run AFTER scripts/cie_index_rejoin_wave2as.py has applied the re-join cures
to the touched spec-links sidecars + manifest and emitted the sheet + stats.
The base state is read from HEAD (pre-commit); the resolutions are
RE-DERIVED INDEPENDENTLY (fresh pool builders from the raw parsed
registries, fresh normalization, fresh rule chain, fresh AS scope law) and
the staged sidecars are never trusted as their own input.

Output: graph/reports/T_SPECS_CIE_REJOIN_2_CHECK.json; exit 0 iff ALL PASS.
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
import cie_xlane_join as xj  # noqa: E402
import cie_index_rejoin_wave2as as eng  # noqa: E402

OUT = REPO / "graph" / "reports" / "T_SPECS_CIE_REJOIN_2_CHECK.json"
LANES = sorted(eng.LANES_2)
METHOD = eng.METHOD
RULES = dict(eng.RULES)
REJOIN_NOTE = eng.REJOIN_NOTE
# ---- independent lane-metadata copies (pinned by the verdict record)
ZERO_LANES = {
    "cie-a-level-business-23", "cie-a-level-computer-science-19",
    "cie-a-level-economics-23", "cie-a-level-maths-20-mechanics",
    "cie-a-level-maths-20-probability-and-statistics-1",
    "cie-a-level-maths-20-probability-and-statistics-2",
    "cie-a-level-maths-20-pure-1", "cie-a-level-maths-20-pure-3",
    "cie-as-english-general-paper-21", "cie-igcse-accounting-21",
    "cie-igcse-accounting-25", "cie-igcse-economics-25",
    "cie-igcse-english-language-20", "cie-igcse-english-language-25",
    "cie-igcse-english-literature-21", "cie-igcse-environmental-management-25",
    "cie-igcse-further-maths-additional-maths-25", "cie-igcse-history-18",
    "cie-igcse-ict-21", "cie-igcse-maths-25-core", "cie-igcse-maths-25-extended",
    "cie-igcse-maths-international-maths-23-core",
    "cie-igcse-maths-international-maths-23-extended",
    "cie-igcse-religious-studies-23",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-biology",
}
# fresh AS scope law (JOIN-2 record's law, independently re-implemented)
SCOPE_AS_ONLY = {"cie-as-chemistry-25", "cie-as-physics-25",
                 "cie-as-business-23"}
SCOPE_DROP_ALEVEL = {"cie-as-computer-science-19"}
REJOIN_2_NOTE = ("index re-join cures applied additively to the wave-2 AS "
                 "lanes' pending anchors; pairs with no identity evidence "
                 "stay pending honestly (AGENT.md rule 3)")
DECLARED = ({f"spec-links/{l}.json" for l in LANES}
            | {"spec-links/manifest.json",
               "scripts/cie_index_rejoin_wave2as.py",
               "scripts/cie_rejoin_check_wave2as.py",
               "scripts/cie_rejoin_wave2as_resolutions.yaml",
               "graph/reports/T_SPECS_CIE_REJOIN_2_RECORD.md",
               "graph/reports/T_SPECS_CIE_REJOIN_2_STATS.json",
               "graph/reports/T_SPECS_CIE_REJOIN_2_CHECK.json"})

results: list[dict] = []


def check(cid: str, fn) -> None:
    try:
        detail = fn()
        results.append({"id": cid, "pass": True, "detail": detail})
        print(f"RJ{cid} PASS: {detail}")
    except AssertionError as exc:
        results.append({"id": cid, "pass": False, "detail": str(exc)})
        print(f"RJ{cid} FAIL: {exc}")


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


# ---- independent normalization + pools + rule chain (fresh implementation)
def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", s or "").lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def phrase_in(needle: str, hay: str) -> bool:
    if not needle:
        return False
    return (" " + needle + " ") in (" " + hay + " ")


INDEP: dict = {}


def derive_independent() -> None:
    if INDEP:
        return
    man = json.loads((REPO / "Official-Specifications" / "manifest.json")
                     .read_text())
    quals = {q["slug"]: q for q in man["qualifications"]}
    heads = {l: head_json(f"spec-links/{l}.json") for l in LANES}
    indexes = {l: json.loads(xj.head_index_bytes(l)) for l in LANES}
    universes = {l: set(indexes[l]["spec_points"]) for l in LANES}
    # corpus-wide definition context over ALL cie-* lanes (engine semantics)
    all_cie = [line.rsplit("/", 1)[1][:-5] for line in subprocess.run(
        ["git", "-C", str(REPO), "ls-tree", "-r", "--name-only", "HEAD",
         "spec-links/"], capture_output=True, check=True
    ).stdout.decode().splitlines()
        if line.startswith("spec-links/cie-") and line.endswith(".json")]
    def_holders: dict[str, list[str]] = {}
    all_indexes: dict[str, dict] = dict(indexes)
    for l in sorted(all_cie):
        if l in all_indexes:
            idx = all_indexes[l]
        else:
            try:
                idx = json.loads(xj.head_index_bytes(l))
            except Exception:
                continue
            all_indexes[l] = idx
        for sid, e in idx["spec_points"].items():
            if e["definition"]:
                def_holders.setdefault(sid, []).append(l)
    xjoin = {}
    for l in LANES:
        for sid, e in (indexes[l].get("cross_lane_join", {})
                       .get("resolved", {}) or {}).items():
            xjoin[(l, sid)] = e
    pools, texts, pool_ids = {}, {}, {}
    for l in LANES:
        q = heads[l]["qual"]
        stem = Path(quals[q]["pdf"]).stem
        reg = json.loads((REPO / "Official-Specifications" / "parsed" / q /
                          f"{stem}.parsed.json").read_text())
        pts = reg["spec_points"]
        full = len(pts)
        if l in SCOPE_AS_ONLY:
            pts = [p for p in pts if p.get("scope") == "AS Level"]
        elif l in SCOPE_DROP_ALEVEL:
            pts = [p for p in pts if p.get("scope") != "A Level"]
        require(len(pts) < full or l not in SCOPE_AS_ONLY | SCOPE_DROP_ALEVEL,
                f"{l} scope law reduced nothing")
        pools[l] = pts
        texts[l] = [(p, norm(p.get("text"))) for p in pts]
        pool_ids[l] = {p["id"]: str(p.get("official_code")) for p in pts}
    resolves, ambiguous = {}, {}
    pairs = set()
    for l in LANES:
        for key, it in heads[l]["items"].items():
            for sid in (it.get("pending") or []):
                pairs.add((l, sid))
    for (l, sid) in sorted(pairs):
        own = indexes[l]["spec_points"].get(sid)
        defs: dict[str, tuple[str, str]] = {}
        if own and own["definition"]:
            defs.setdefault(norm(own["definition"]), (own["definition"], "own"))
        for m in sorted(def_holders.get(sid, ())):
            if m == l:
                continue
            dd = all_indexes[m]["spec_points"][sid]["definition"]
            defs.setdefault(norm(dd), (dd, f"sibling:{m}"))
        xe = xjoin.get((l, sid))
        if xe and xe["grade"] == "definition":
            defs.setdefault(norm(xe["definition"]),
                            (xe["definition"], "cross_lane_join"))
        name = own["name"] if own else (xe["name"] if xe else "")
        if len(defs) > 1:
            ambiguous[(l, sid)] = {"lane": l,
                                   "reason": "definition_conflict_across_lanes"}
            continue
        dnorm = next(iter(defs)) if defs else ""
        hit = None
        tlist = texts[l]
        if dnorm:
            eq = [p for p, t in tlist if t and t == dnorm]
            if len(eq) == 1:
                hit = ("J1_definition_text_identity", eq[0])
            elif len(eq) > 1:
                ambiguous[(l, sid)] = {"lane": l,
                                       "reason": "definition_eq_multi_text"}
                continue
            else:
                ph = [p for p, t in tlist
                      if len(dnorm) >= 3 and phrase_in(dnorm, t)]
                if len(ph) == 1:
                    hit = ("J2_definition_phrase_identity", ph[0])
                elif len(ph) > 1:
                    ambiguous[(l, sid)] = {
                        "lane": l, "reason": "definition_phrase_multi_text"}
                    continue
        verdict_evaluated = l in ZERO_LANES and sid in universes[l]
        if hit is None and not verdict_evaluated and name:
            nn = norm(name)
            eq = [p for p, t in tlist if t and t == nn]
            if len(eq) == 1:
                hit = ("J3_name_text_identity", eq[0])
            elif len(eq) > 1:
                ambiguous[(l, sid)] = {"lane": l,
                                       "reason": "name_eq_multi_text"}
                continue
            else:
                ph = [p for p, t in tlist
                      if len(nn) >= 3 and phrase_in(nn, t)]
                if len(ph) == 1:
                    hit = ("J4_name_phrase_identity", ph[0])
                elif len(ph) > 1:
                    ambiguous[(l, sid)] = {
                        "lane": l, "reason": "name_phrase_multi_text"}
                    continue
        if hit is not None:
            rule, op = hit
            resolves[(l, sid)] = {"tier": rule, "official_id": op["id"],
                                  "official_code":
                                      str(op.get("official_code"))}
    INDEP.update(resolves=resolves, ambiguous=ambiguous, pairs=pairs,
                 universes=universes, heads=heads, indexes=indexes,
                 pools=pools, pool_ids=pool_ids, xjoin=xjoin)


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
                        / "T_SPECS_CIE_REJOIN_2_STATS.json").read_text())

    def rj1() -> str:
        for l in touched:
            raw = staged_bytes(f"spec-links/{l}.json")
            a, rs = staged[l]["anchors"], staged[l]["review_state"]
            require(list(a.keys())[-1] == "rejoin", f"{l} anchors rejoin last")
            require(list(rs.keys())[-1] == "rejoin", f"{l} rs rejoin last")
            rj = a["rejoin"]
            require(rj["lane"] == eng.LANE_ID
                    and rj["applied_utc"] == eng.STAMP, f"{l} anchors stamp")
            require(rj["resolved_pairs"] == len(lane_res[l]),
                    f"{l} resolved_pairs")
            require(rj["note"] == REJOIN_NOTE, f"{l} anchors note")
            require(rj["scope_law"]["lane_points"] == len(INDEP["pools"][l]),
                    f"{l} scope law lane_points")
            require(raw.endswith(b"\n"), f"{l} trailing newline")
            rj2b = rs["rejoin"]
            require(rj2b["state"] == "SUGGESTED", f"{l} state")
            require(rj2b["method"] == METHOD
                    and rj2b["gateway_trace"] == eng.TRACE
                    and rj2b["base_commit"] == eng.PIN,
                    f"{l} rs provenance")
            require(rj2b["tiers"] == dict(sorted(RULES.items())),
                    f"{l} tiers")
            for key, it in staged[l]["items"].items():
                for c in (it.get("codes") or []):
                    if c.get("method") == METHOD:
                        require(c["tier"] in RULES, f"{l} {key} tier vocab")
        return (f"{len(touched)} touched sidecars well-formed (additive "
                f"rejoin blocks, SUGGESTED state, method/tier vocab)")

    def rj2() -> str:
        for l in touched:
            h, n = heads[l], staged[l]
            require(list(n.keys()) == list(h.keys()), f"{l} top keys")
            for k in ("schema", "generated_utc", "course", "qual", "board",
                      "registry"):
                require(n[k] == h[k], f"{l} {k} drifted")
            require(list(n["review_state"].keys())
                    == list(h["review_state"].keys()) + ["rejoin"],
                    f"{l} review_state keys")
            for k in h["review_state"]:
                require(n["review_state"][k] == h["review_state"][k],
                        f"{l} review_state {k} drifted")
            require(list(n["anchors"].keys())
                    == list(h["anchors"].keys()) + ["rejoin"],
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
                for c in nc[len(oc):]:
                    require(c["method"] == METHOD and c["tier"] in RULES
                            and c["official_id"] in valid_oids,
                            f"{l} {key} appended code")
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
            if "verdict" in h["anchors"]:
                require(n["anchors"]["universe_resolved"]
                        == int(n["anchors"]["universe_ids"]) - len(pend_u),
                        f"{l} universe_resolved")
            else:
                require(n["anchors"]["universe_resolved"]
                        == h["anchors"]["universe_resolved"],
                        f"{l} universe_resolved (join semantics preserved)")
            for k in h["anchors"]:
                if k == "pending_refs":
                    require(n["anchors"][k] == sum(
                        len(it.get("pending") or [])
                        for it in n["items"].values()),
                        f"{l} pending_refs")
                elif k != "universe_resolved":
                    require(n["anchors"][k] == h["anchors"][k],
                            f"{l} anchors {k} drifted")
        return ("mutation discipline: only codes-append / pending-shrink / "
                "additive rejoin blocks / recounted counters; every other "
                "field deep-equal to HEAD")

    def rj3() -> str:
        sheet = yaml.safe_load(
            (REPO / "scripts" / "cie_rejoin_wave2as_resolutions.yaml")
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
            require(ev["evidence_source"] in ("own", "cross_lane_join")
                    or ev["evidence_source"].startswith("sibling:"),
                    f"{k} evidence source")
            require(bool(ev["official_text"]) and bool(ev["rule"]),
                    f"{k} evidence fields")
        sh_amb = {(e["lane"], e["id"]): e["reason"]
                  for e in sheet["ambiguous"]}
        require(set(sh_amb) == set(ambiguous),
                f"sheet/derived ambiguous mismatch: "
                f"{sorted(set(sh_amb) ^ set(ambiguous))[:6]}")
        for k, a_entry in ambiguous.items():
            require(sh_amb[k] == a_entry["reason"],
                    f"{k} ambiguous reason")
        return (f"INDEPENDENT re-derivation + sheet bijection: all "
                f"{len(resolves)} resolves + {len(ambiguous)} quarantines "
                f"equal (fresh pools, fresh norm, fresh rule chain)")

    def rj4() -> str:
        for l in touched:
            h, n = heads[l], staged[l]
            res_sids = set(lane_res[l])
            refs_res = sum(1 for key in h["items"]
                           for s in (h["items"][key].get("pending") or [])
                           if s in res_sids)
            rj = n["anchors"]["rejoin"]
            require(rj["resolved_refs"] == refs_res,
                    f"{l} resolved_refs {rj['resolved_refs']} != {refs_res}")
            by_rule = Counter(v["tier"] for v in lane_res[l].values())
            require(rj["by_rule"] == {k: by_rule.get(k, 0)
                                      for k in sorted(RULES)},
                    f"{l} by_rule")
            row = next((r for r in stats["lanes_detail"]
                        if r["lane"] == l), None)
            require(row is not None
                    and row["resolved_pairs"] == len(lane_res[l])
                    and row["resolved_refs"] == refs_res
                    and row["pending_refs_after"] == n["anchors"]["pending_refs"],
                    f"{l} stats row")
        tot_codes = sum(sum(1 for it in staged[l]["items"].values()
                            for c in (it.get("codes") or [])
                            if c.get("method") == METHOD)
                        for l in touched)
        require(tot_codes == stats["code_entries_added_total"],
                f"codes total {tot_codes} != stats")
        require(stats["resolved_pairs_total"] == len(resolves),
                "stats pairs total")
        return (f"cascade integrity (codes dedup-correct, pendings shrunk "
                f"exactly, anchors recounts, stats coherent); "
                f"{tot_codes} code entries")

    def rj5() -> str:
        m = head_json("spec-links/manifest.json")
        nm = json.loads(staged_bytes("spec-links/manifest.json"))
        require(list(nm.keys()) == list(m.keys()) + ["cie_rejoin_wave2as"],
                "manifest top keys (additive, appended last)")
        for row_l, row in m["courses"].items():
            if row_l in touched:
                nr = nm["courses"][row_l]
                d = staged[row_l]
                require(nr["items_with_codes"]
                        == d["totals"]["items_with_codes"]
                        and nr["pending_refs"] == d["anchors"]["pending_refs"],
                        f"{row_l} manifest row totals")
                require(nr["rejoin"]["resolved_pairs"]
                        == d["anchors"]["rejoin"]["resolved_pairs"],
                        f"{row_l} manifest rejoin")
            else:
                require(nm["courses"][row_l] == row,
                        f"{row_l} untouched row drifted")
        require(set(nm["courses"]) == set(m["courses"]), "courses set")
        cr = nm["cie_rejoin_wave2as"]
        require(cr["lane"] == eng.LANE_ID and cr["state"] == "SUGGESTED"
                and cr["resolved_pairs_total"] == len(resolves)
                and cr["lanes"] == len(touched), "cie_rejoin_wave2as block")
        return ("manifest discipline: touched rows updated "
                "value-consistently, all pre-existing rows/keys preserved, "
                "cie_rejoin_wave2as block additive + appended last")

    def rj6() -> str:
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
        edex = [p for p in subprocess.run(
            ["git", "-C", str(REPO), "ls-tree", "-r", "HEAD", "--name-only",
             "spec-links/"], capture_output=True, check=True
        ).stdout.decode().splitlines()
            if p.endswith(".json") and "/cie-" not in p
            and p != "spec-links/manifest.json"]
        for p in edex:
            require(p not in delta, f"Edexcel sidecar touched: {p}")
        return (f"footprint {len(seen)} paths subset-of declared; spec-links "
                f"delta == {len(touched)} sidecars + manifest; guards intact; "
                f"{len(edex)} Edexcel sidecars untouched")

    def rj7() -> str:
        before = {l: hashlib.sha256(
            staged_bytes(f"spec-links/{l}.json")).hexdigest()
            for l in touched}
        before_m = hashlib.sha256(
            staged_bytes("spec-links/manifest.json")).hexdigest()
        before_s = hashlib.sha256(
            (REPO / "scripts" / "cie_rejoin_wave2as_resolutions.yaml")
            .read_bytes()).hexdigest()
        before_j = hashlib.sha256(
            (REPO / "graph" / "reports"
             / "T_SPECS_CIE_REJOIN_2_STATS.json").read_bytes()).hexdigest()
        r = subprocess.run([sys.executable,
                            str(REPO / "scripts"
                                / "cie_index_rejoin_wave2as.py")],
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
            (REPO / "scripts" / "cie_rejoin_wave2as_resolutions.yaml")
            .read_bytes()).hexdigest() == before_s, "sheet re-run drift")
        require(hashlib.sha256(
            (REPO / "graph" / "reports"
             / "T_SPECS_CIE_REJOIN_2_STATS.json").read_bytes()).hexdigest()
            == before_j, "stats re-run drift")
        return ("engine fixed-stamp re-run byte-identical "
                f"({len(touched)} sidecars + manifest + sheet + stats)")

    def rj8() -> str:
        rec = 0
        for (l, sid) in INDEP["pairs"]:
            if sid not in INDEP["universes"][l] and (l, sid) not in INDEP["xjoin"]:
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
        require(rec == stats["stays"]["recordless_no_corpus_record"],
                f"recordless {rec} != stats")
        # verdict-exhaustion gate: NO AS-lane pair was verdict-evaluated
        zc = sum(1 for (l, sid) in resolves
                 if l in ZERO_LANES and sid in INDEP["universes"][l])
        require(zc == 0, f"zero-lane verdict-evaluated resolves {zc} != 0")
        require(stats["verdict_evaluated_pairs"] == 0,
                "stats verdict_evaluated_pairs != 0")
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
                f"pending; 0 verdict-evaluated pairs (AS lane class); all "
                f"{len(resolves)} resolves inside their lane's AS-scoped "
                f"pool (raw predicate re-checked)")

    def rj9() -> str:
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
                for sid in pend:
                    if sid in code_by_sid:
                        oid, ocode, tier = code_by_sid[sid]
                        if not any(c.get("official_id") == oid
                                   for c in (it.get("codes") or [])):
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
            a["pending_refs"] = sum(len(it.get("pending") or [])
                                    for it in nd["items"].values())
            res_l = lane_res[l]
            a["rejoin"] = {
                "lane": eng.LANE_ID, "applied_utc": eng.STAMP,
                "resolved_pairs": len(res_l),
                "resolved_refs": sum(1 for it in h["items"].values()
                                     for s in (it.get("pending") or [])
                                     if s in code_by_sid),
                "by_rule": {k: sum(1 for v in res_l.values()
                                   if v["tier"] == k)
                            for k in sorted(RULES)},
                "ambiguous_pairs": sum(1 for (ll, _s) in ambiguous
                                       if ll == l),
                "pending_refs": sum(len(it.get("pending") or [])
                                    for it in nd["items"].values()),
                "scope_law": staged[l]["anchors"]["rejoin"]["scope_law"],
                "note": REJOIN_2_NOTE,
            }
            nd["review_state"]["rejoin"] = staged[l]["review_state"]["rejoin"]
            rb = json.dumps(nd, ensure_ascii=False, indent=1) + "\n"
            require(rb.encode() == staged_bytes(f"spec-links/{l}.json"),
                    f"{l} rebuild != staged bytes")
        return (f"{len(rebuild_lanes)}-lane full-document rebuild from HEAD "
                f"+ independent resolutions == staged bytes "
                f"({', '.join(rebuild_lanes)})")

    def rj10() -> str:
        m = head_json("spec-links/manifest.json")
        nm = json.loads(staged_bytes("spec-links/manifest.json"))
        pend_head = sum(row["pending_refs"] for row in m["courses"].values()
                        if "pending_refs" in row)
        pend_staged = sum(row["pending_refs"] for row in nm["courses"].values()
                          if "pending_refs" in row)
        require(stats["reconciliation"]["pairs"]
                == stats["reconciliation"]["must_equal"] == len(INDEP["pairs"]),
                "reconciliation pin")
        # manifest-row cross-foot (touched rows may GAIN the pending_refs key
        # — the REJOIN-1 recount pattern on rows that never carried it): the
        # row-sum delta is exactly the touched-row delta; the RESOLVED term
        # lives in the sidecar-anchors cross-foot below
        head_touched = sum(m["courses"][l].get("pending_refs", 0)
                           for l in touched)
        staged_touched = sum(nm["courses"][l].get("pending_refs", 0)
                             for l in touched)
        require(pend_staged - pend_head == staged_touched - head_touched,
                f"manifest cross-foot {pend_head} -> {pend_staged}")
        # sidecar-anchors cross-foot (shape-independent truth):
        # head anchors sum - resolved == staged anchors sum
        a_head = sum(head_json(f"spec-links/{l}.json")["anchors"]["pending_refs"]
                     for l in LANES)
        a_staged = sum(json.loads(staged_bytes(f"spec-links/{l}.json"))
                       ["anchors"]["pending_refs"] for l in LANES)
        require(a_head - stats["resolved_refs_total"] == a_staged,
                f"sidecar anchors cross-foot {a_head} -> {a_staged}")
        require(stats["stays"]["no_new_evidence_verdict_evaluated"] == 0,
                "no_new_evidence pin (AS class: none verdict-evaluated)")
        require(sum(stats["resolves_by_rule"].values()) == len(resolves),
                "by_rule sum pin")
        return (f"cross-foots: manifest rows {pend_head} -> {pend_staged} "
                f"(+{staged_touched - head_touched} gained-key recount, "
                f"-{stats['resolved_refs_total']} resolved); 8-lane sidecar "
                f"anchors {a_head} -> {a_staged}; reconciliation "
                f"{len(INDEP['pairs'])} pairs exact")

    check("1", rj1)
    check("2", rj2)
    check("3", rj3)
    check("4", rj4)
    check("5", rj5)
    check("6", rj6)
    check("7", rj7)
    check("8", rj8)
    check("9", rj9)
    check("10", rj10)

    all_pass = all(r["pass"] for r in results)
    OUT.write_text(json.dumps({
        "battery": "T-SPECS-CIE-REJOIN-2",
        "all_pass": all_pass,
        "checks": results,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\nALL {'PASS' if all_pass else 'FAIL'} "
          f"({sum(r['pass'] for r in results)}/{len(results)})")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
