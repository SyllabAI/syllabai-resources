#!/usr/bin/env python3
"""
T-SPECS-CIE-XJOIN-1 battery — X1-X10 for the cross-lane join round on the
44 CIE spec_point_index.json files.

Run AFTER scripts/cie_xlane_join.py has staged the additive cross_lane_join
blocks. Reads the staged entries from the git index (the files live outside
the sparse cone). The corpus truth (universes, EQ refs, sibling records) is
re-derived FRESH from the git blobs — the staged blocks are never trusted
as their own input.

Output: graph/reports/T_SPECS_CIE_XJOIN_1_CHECK.json; exit 0 iff ALL PASS.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import cie_spcpt_index_harvest as harvest  # noqa: E402
import cie_xlane_join as engine  # noqa: E402
from cie_xlane_join import norm  # noqa: E402

OUT = REPO / "graph" / "reports" / "T_SPECS_CIE_XJOIN_1_CHECK.json"
LANES = sorted(engine.lanes())
BASE_KEYS = ["schema", "generated_utc", "course_slug", "notes_base",
             "source_pages", "fetch_failures", "spec_points", "coverage"]
BLOCK_KEYS = ["schema", "generated_utc", "directive", "gateway_trace",
              "fires", "dangling_total", "resolved", "ambiguous",
              "unresolved_ids", "resolved_count", "ambiguous_count",
              "unresolved_count"]
DEF_KEYS = ["grade", "name", "definition", "notes", "subtopic_slugs",
            "via_lanes", "definition_lanes"]
NAME_KEYS = ["grade", "name", "definition", "notes", "subtopic_slugs",
             "via_lanes"]
DECLARED = ({f"SME-ExamQuestion/{l}/spec_point_index.json" for l in LANES}
            | {"scripts/cie_xlane_join.py", "scripts/cie_xlane_join_check.py",
               "graph/reports/T_SPECS_CIE_XJOIN_1_RECORD.md",
               "graph/reports/T_SPECS_CIE_XJOIN_1_STATS.json",
               "graph/reports/T_SPECS_CIE_XJOIN_1_CHECK.json"})

results: list[dict] = []


def check(cid: str, fn) -> None:
    try:
        detail = fn()
        results.append({"id": cid, "pass": True, "detail": detail})
        print(f"X{cid} PASS: {detail}")
    except AssertionError as exc:
        results.append({"id": cid, "pass": False, "detail": str(exc)})
        print(f"X{cid} FAIL: {exc}")


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def staged_bytes(path: str) -> bytes:
    ls = subprocess.run(["git", "-C", str(REPO), "ls-files", "-s", "--", path],
                        capture_output=True, check=True).stdout.decode().split()
    if len(ls) < 2:
        raise AssertionError(f"{path} not in index")
    return subprocess.run(["git", "-C", str(REPO), "cat-file", "-p", ls[1]],
                          capture_output=True, check=True).stdout


# fresh corpus truth, derived once
FRESH: dict[str, dict] = {}
FRESH_DOCS: dict[str, dict] = {}
HOLDERS: dict[str, list[str]] = {}


def derive_fresh() -> None:
    if FRESH:
        return
    for lane in LANES:
        targets = harvest.list_targets(lane)
        blobs = harvest.read_blobs(targets)
        spec: dict[str, dict] = {}
        eq_refs: list[str] = []
        for oid, path, kind in targets:
            if kind == "manifest":
                continue
            doc = json.loads(blobs[oid].decode("utf-8"))
            if kind == "note":
                hits: list[dict] = []
                harvest.walk_blocks(doc.get("blocks", []), hits)
                for h in hits:
                    e = spec.setdefault(h["id"], {
                        "name": h["name"], "definition": h["definition"],
                        "notes": set(), "slugs": set()})
                    if not e["definition"] and h["definition"]:
                        e["definition"] = h["definition"]
                    e["notes"].add(doc["note_id"])
                    e["slugs"].add(path.rsplit("/", 1)[-1][:-5])
            else:
                eq_refs.extend(harvest.eq_part_ids(doc))
        FRESH[lane] = {"spec": spec, "eq_refs": eq_refs}
    for lane in LANES:
        for sid in FRESH[lane]["spec"]:
            HOLDERS.setdefault(sid, []).append(lane)
    for lane in LANES:
        FRESH_DOCS[lane] = {
            "spec_points": {sid: {"name": e["name"],
                                  "definition": e["definition"],
                                  "notes": sorted(e["notes"]),
                                  "subtopic_slugs": sorted(e["slugs"])}
                            for sid, e in sorted(FRESH[lane]["spec"].items())},
            "coverage": {"missing_from_index":
                         sorted(set(FRESH[lane]["eq_refs"])
                                - set(FRESH[lane]["spec"]))},
        }


def main() -> int:
    staged = {l: staged_bytes(f"SME-ExamQuestion/{l}/spec_point_index.json")
              for l in LANES}
    docs = {l: json.loads(staged[l]) for l in LANES}
    heads = {l: engine.head_index_bytes(l) for l in LANES}
    head_docs = {l: json.loads(heads[l]) for l in LANES}

    def x1() -> str:
        for lane in LANES:
            d, raw = docs[lane], staged[lane]
            require(list(d.keys()) == BASE_KEYS + [engine.BLOCK_KEY],
                    f"{lane} top-level key order")
            require(not raw.endswith(b"\n"), f"{lane} trailing newline")
            b = d[engine.BLOCK_KEY]
            require(list(b.keys()) == BLOCK_KEYS, f"{lane} block key order")
            require(b["schema"] == engine.BLOCK_SCHEMA, f"{lane} block schema")
            require(b["generated_utc"] == engine.FIXED_STAMP, f"{lane} stamp")
            require(b["directive"] == engine.DIRECTIVE, f"{lane} directive")
            require(b["gateway_trace"] == engine.TRACE, f"{lane} trace")
            require(b["fires"] == engine.FIRES, f"{lane} fires")
            require(b["dangling_total"]
                    == len(d["coverage"]["missing_from_index"]),
                    f"{lane} dangling_total")
            require(b["resolved_count"] == len(b["resolved"]), f"{lane} rc")
            require(b["ambiguous_count"] == len(b["ambiguous"]), f"{lane} ac")
            require(b["unresolved_count"] == len(b["unresolved_ids"]),
                    f"{lane} uc")
            require(b["resolved_count"] + b["ambiguous_count"]
                    + b["unresolved_count"] == b["dangling_total"],
                    f"{lane} arithmetic")
            require(list(b["resolved"]) == sorted(b["resolved"]),
                    f"{lane} resolved sorted")
            require(b["unresolved_ids"] == sorted(b["unresolved_ids"]),
                    f"{lane} unresolved sorted")
            require([a["id"] for a in b["ambiguous"]]
                    == sorted(a["id"] for a in b["ambiguous"]),
                    f"{lane} ambiguous sorted")
            for sid, e in b["resolved"].items():
                if e["grade"] == "definition":
                    require(list(e.keys()) == DEF_KEYS
                            or list(e.keys()) == DEF_KEYS + ["norm_equivalent"],
                            f"{lane} def entry key order {sid}")
                    require(e["definition"] != "", f"{lane} {sid} def empty")
                    require(e["definition_lanes"], f"{lane} {sid} dl empty")
                    require(e["definition_lanes"]
                            == sorted(e["definition_lanes"]),
                            f"{lane} {sid} dl sorted")
                    require(set(e["definition_lanes"]) <= set(e["via_lanes"]),
                            f"{lane} {sid} dl subset")
                else:
                    require(list(e.keys()) == NAME_KEYS
                            or list(e.keys()) == NAME_KEYS + ["norm_equivalent"],
                            f"{lane} name entry key order {sid}")
                    require(e["definition"] == "", f"{lane} {sid} def set")
                require(e["grade"] in ("definition", "name_only"),
                        f"{lane} {sid} grade")
                require(e["via_lanes"] == sorted(e["via_lanes"]),
                        f"{lane} {sid} via sorted")
                require(len(set(e["via_lanes"])) == len(e["via_lanes"]),
                        f"{lane} {sid} via unique")
                require(lane not in e["via_lanes"], f"{lane} {sid} self-via")
            for a in b["ambiguous"]:
                require(list(a.keys()) == ["id", "reason", "via_lanes",
                                           "variants"],
                        f"{lane} ambiguous key order {a['id']}")
                require(a["reason"] in ("definition_conflict",
                                        "name_conflict"),
                        f"{lane} ambiguous reason {a['id']}")
                require(len(a["variants"]) >= 2, f"{lane} variants {a['id']}")
        return ("44/44 well-formed additive cross_lane_join blocks "
                "(shape/stamps/counts/key order/no-trailing-NL)")

    def x2() -> str:
        for lane in LANES:
            hd, nd = head_docs[lane], docs[lane]
            require(list(nd.keys()) == list(hd.keys()) + [engine.BLOCK_KEY],
                    f"{lane} key append-only")
            stripped = {k: v for k, v in nd.items()
                        if k != engine.BLOCK_KEY}
            require(json.dumps(stripped, ensure_ascii=False,
                               indent=1).encode("utf-8") == heads[lane],
                    f"{lane} pre-existing bytes drifted")
        return ("byte-additivity 44/44: staged file == HEAD bytes + exactly "
                "the appended block; coverage/spec_points byte-stable")

    def x3() -> str:
        derive_fresh()
        tu = tc = tm = tr = 0
        for lane in LANES:
            spec = FRESH[lane]["spec"]
            eq_refs = FRESH[lane]["eq_refs"]
            uniq = sorted(set(eq_refs))
            mis = [s for s in uniq if s not in spec]
            require(set(spec) == set(docs[lane]["spec_points"]),
                    f"{lane} universe mismatch vs fresh")
            require(mis == docs[lane]["coverage"]["missing_from_index"],
                    f"{lane} dangling mismatch vs fresh")
            for sid in mis:
                require(sid not in spec, f"{lane} {sid} not dangling")
            b = docs[lane][engine.BLOCK_KEY]
            res = set(b["resolved"])
            amb = {a["id"] for a in b["ambiguous"]}
            unr = set(b["unresolved_ids"])
            require(res | amb | unr == set(mis), f"{lane} partition")
            require(not (res & amb) and not (res & unr) and not (amb & unr),
                    f"{lane} partition overlap")
            for sid in res | amb:
                sibs = set(HOLDERS[sid]) - {lane}
                require(bool(sibs), f"{lane} {sid} cured but recordless")
            for sid in unr:
                require(sid not in HOLDERS, f"{lane} {sid} unresolved but held")
            tu += len(uniq); tc += len(uniq) - len(mis)
            tm += len(mis); tr += len(eq_refs)
        require((tu, tc, tm) == (5540, 5218, 322),
                f"sums {(tu, tc, tm)} != (5540, 5218, 322)")
        res_sum = sum(docs[l][engine.BLOCK_KEY]["resolved_count"]
                      for l in LANES)
        amb_sum = sum(docs[l][engine.BLOCK_KEY]["ambiguous_count"]
                      for l in LANES)
        unr_sum = sum(docs[l][engine.BLOCK_KEY]["unresolved_count"]
                      for l in LANES)
        require((res_sum + amb_sum, unr_sum, tm) == (54, 268, 322),
                f"global split {(res_sum + amb_sum, unr_sum, tm)} != (54, 268, 322)")
        return (f"fresh corpus re-derivation 44/44; refs {tr}, unique {tu} = "
                f"covered {tc} + missing {tm}; split {res_sum}+{amb_sum}+"
                f"{unr_sum} == 322 == (54 present-in-sibling) + (268 recordless)")

    def x4() -> str:
        derive_fresh()
        g = n = 0
        for lane in LANES:
            for sid, e in docs[lane][engine.BLOCK_KEY]["resolved"].items():
                require(e["via_lanes"] == sorted(m for m in HOLDERS[sid]
                                                 if m != lane),
                        f"{lane} {sid} via_lanes != fresh sibling holders")
                if e["grade"] == "definition":
                    g += 1
                    dl = e["definition_lanes"]
                    require(dl == sorted(m for m in e["via_lanes"]
                                         if FRESH[m]["spec"][sid]["definition"]),
                            f"{lane} {sid} definition_lanes != fresh")
                    rep = dl[0]
                    fr = FRESH[rep]["spec"][sid]
                    require(e["name"] == fr["name"], f"{lane} {sid} name")
                    require(e["definition"] == fr["definition"],
                            f"{lane} {sid} definition")
                    require(e["notes"] == sorted(fr["notes"]),
                            f"{lane} {sid} notes")
                    require(e["subtopic_slugs"] == sorted(fr["slugs"]),
                            f"{lane} {sid} slugs")
                    pairs = {(FRESH[m]["spec"][sid]["name"],
                              FRESH[m]["spec"][sid]["definition"])
                             for m in dl}
                    if len(pairs) == 1:
                        require("norm_equivalent" not in e,
                                f"{lane} {sid} spurious flag")
                    else:
                        require(e.get("norm_equivalent") is True,
                                f"{lane} {sid} missing flag")
                        require(len({(norm(a), norm(b2))
                                     for a, b2 in pairs}) == 1,
                                f"{lane} {sid} norm conflict uncured")
                else:
                    n += 1
                    require(all(FRESH[m]["spec"][sid]["definition"] == ""
                                for m in e["via_lanes"]),
                            f"{lane} {sid} name_only grade but def exists")
                    rep = e["via_lanes"][0]
                    fr = FRESH[rep]["spec"][sid]
                    require(e["name"] == fr["name"], f"{lane} {sid} name")
                    require(e["notes"] == sorted(fr["notes"]),
                            f"{lane} {sid} notes")
                    require(e["subtopic_slugs"] == sorted(fr["slugs"]),
                            f"{lane} {sid} slugs")
                    names = {FRESH[m]["spec"][sid]["name"]
                             for m in e["via_lanes"]}
                    if len(names) == 1:
                        require("norm_equivalent" not in e,
                                f"{lane} {sid} spurious flag")
                    else:
                        require(e.get("norm_equivalent") is True,
                                f"{lane} {sid} missing flag")
                        require(len({norm(a) for a in names}) == 1,
                                f"{lane} {sid} norm conflict uncured")
        require((g, n) == (9, 45), f"grade split {(g, n)} != (9, 45)")
        return (f"all {g + n} resolved entries verbatim-equal to fresh sibling "
                f"records (representative = first recorded lane); grades "
                f"def {g} / name {n}; corroboration via_lanes honest 44/44")

    def x5() -> str:
        derive_fresh()
        total = 0
        for lane in LANES:
            for a in docs[lane][engine.BLOCK_KEY]["ambiguous"]:
                total += 1
                require(a["id"] not in docs[lane][engine.BLOCK_KEY]["resolved"],
                        f"{lane} {a['id']} ambiguous AND resolved")
                require(a["via_lanes"] == sorted(m for m in HOLDERS[a["id"]]
                                                 if m != lane),
                        f"{lane} {a['id']} via_lanes != fresh")
                for v in a["variants"]:
                    require(v["lane"] in a["via_lanes"],
                            f"{lane} {a['id']} variant lane")
                    fr = FRESH[v["lane"]]["spec"][a["id"]]
                    require(v["name"] == fr["name"], f"{lane} variant name")
                    require(v["definition"] == fr["definition"],
                            f"{lane} variant definition")
        return (f"ambiguity quarantine honest: {total} entries, variants "
                f"deep-equal to fresh sibling records")

    def x6() -> str:
        st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                            capture_output=True, check=True).stdout.decode()
        seen = {line[3:].strip().strip('"') for line in st.splitlines()}
        extra = sorted(seen - DECLARED)
        require(not extra, f"undeclared paths: {extra[:8]}")
        for guard in ("spec-links/", "SME-RevisionNotes/",
                      "Official-Specifications/", "SME-Flashcards/"):
            bad = [p for p in seen if p.startswith(guard)]
            require(not bad, f"{guard} touched: {bad[:5]}")
        delta = subprocess.run(
            ["git", "-C", str(REPO), "diff", "HEAD", "--name-only", "--",
             "SME-ExamQuestion/"], capture_output=True, check=True
        ).stdout.decode().splitlines()
        require(set(delta) == {f"SME-ExamQuestion/{l}/spec_point_index.json"
                               for l in LANES},
                f"SME-ExamQuestion delta != the 44 CIE files: {sorted(set(delta) - {f'SME-ExamQuestion/{l}/spec_point_index.json' for l in LANES})[:5]}")
        all_idx = [p for p in subprocess.run(
            ["git", "-C", str(REPO), "ls-tree", "-r", "HEAD", "--name-only",
             "SME-ExamQuestion/"], capture_output=True, check=True
        ).stdout.decode().splitlines() if p.endswith("spec_point_index.json")]
        cie_paths = {f"SME-ExamQuestion/{l}/spec_point_index.json"
                     for l in LANES}
        edex = [p for p in all_idx if p not in cie_paths]
        require(len(all_idx) == 93,
                f"indexes at HEAD {len(all_idx)} != 93 (49 Edexcel + 44 CIE)")
        require(len(edex) == 49, f"Edexcel indexes {len(edex)} != 49")
        return (f"footprint {len(seen)} paths ⊆ declared set; guards intact; "
                f"SME-ExamQuestion delta == 44 CIE files; 93 indexes at HEAD "
                f"= 49 Edexcel (untouched) + 44 CIE")

    def x7() -> str:
        before = {l: hashlib.sha256(staged[l]).hexdigest() for l in LANES}
        r = subprocess.run([sys.executable,
                            str(REPO / "scripts" / "cie_xlane_join.py")],
                           capture_output=True, text=True)
        require(r.returncode == 0, f"engine re-run failed: {r.stderr[-400:]}")
        for l in LANES:
            b = staged_bytes(f"SME-ExamQuestion/{l}/spec_point_index.json")
            require(hashlib.sha256(b).hexdigest() == before[l],
                    f"{l} re-run byte drift")
        return "engine fixed-stamp re-run byte-identical across all 44 files"

    def x8() -> str:
        derive_fresh()
        for lane in ("cie-igcse-maths-25-core", "cie-igcse-chemistry-23"):
            hd = head_docs[lane]
            block = engine.resolve_lane(lane, FRESH_DOCS, HOLDERS)
            nd = {k: hd[k] for k in hd}
            nd[engine.BLOCK_KEY] = block
            rb = json.dumps(nd, ensure_ascii=False, indent=1).encode("utf-8")
            require(rb == staged[lane],
                    f"{lane} fresh-data rebuild != staged bytes")
            require(block["resolved_count"] > 0,
                    f"{lane} sample has no cures")
        return ("2-lane independent rebuild from fresh corpus data "
                "(maths-25-core 26 cures, chemistry-23 8 cures) == staged bytes")

    def x9() -> str:
        for lane in LANES:
            side = json.loads((REPO / "spec-links" / f"{lane}.json")
                              .read_text(encoding="utf-8"))
            require(side["anchors"]["universe_ids"]
                    == len(head_docs[lane]["spec_points"]),
                    f"{lane} sidecar universe drift")
        out = subprocess.run(
            ["git", "-C", str(REPO), "diff", "HEAD", "--name-only", "--",
             "spec-links/"], capture_output=True, check=True).stdout
        require(out == b"", "spec-links files modified")
        return ("sidecar universe reconciliation 44/44 fail-closed; "
                "spec-links byte-identical vs HEAD")

    def x10() -> str:
        s = json.loads((REPO / "graph" / "reports"
                        / "T_SPECS_CIE_XJOIN_1_STATS.json")
                       .read_text(encoding="utf-8"))
        for row in s["lanes_detail"]:
            lane = row["lane"]
            b = docs[lane][engine.BLOCK_KEY]
            g = sum(1 for e in b["resolved"].values()
                    if e["grade"] == "definition")
            require(row["dangling_total"] == b["dangling_total"],
                    f"{lane} stats dangling")
            require(row["resolved_count"] == b["resolved_count"],
                    f"{lane} stats resolved")
            require(row["resolved_definition_grade"] == g,
                    f"{lane} stats def grade")
            require(row["ambiguous_count"] == b["ambiguous_count"],
                    f"{lane} stats ambiguous")
            require(row["unresolved_count"] == b["unresolved_count"],
                    f"{lane} stats unresolved")
        require(s["lanes"] == 44, "stats lanes")
        require((s["dangling_total"], s["resolved_count"],
                 s["resolved_definition_grade"],
                 s["resolved_name_only_grade"], s["ambiguous_count"],
                 s["unresolved_count"]) == (322, 54, 9, 45, 0, 268),
                f"stats global pins {[(s[k]) for k in ('dangling_total', 'resolved_count', 'resolved_definition_grade', 'resolved_name_only_grade', 'ambiguous_count', 'unresolved_count')]}")
        require(s["present_in_sibling_pairs"] == 54, "stats present pairs")
        require(s["recordless_pairs"] == 268, "stats recordless")
        require(s["directive"] == engine.DIRECTIVE
                and s["gateway_trace"] == engine.TRACE
                and s["generated_utc"] == engine.FIXED_STAMP,
                "stats provenance")
        return ("stats coherent with staged blocks; record pins (322, 54, "
                "9, 45, 0, 268) ALL reproduced")

    check("1", x1)
    check("2", x2)
    check("3", x3)
    check("4", x4)
    check("5", x5)
    check("6", x6)
    check("7", x7)
    check("8", x8)
    check("9", x9)
    check("10", x10)

    all_pass = all(r["pass"] for r in results)
    OUT.write_text(json.dumps({
        "battery": "T-SPECS-CIE-XJOIN-1",
        "all_pass": all_pass,
        "checks": results,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\nALL {'PASS' if all_pass else 'FAIL'} "
          f"({sum(r['pass'] for r in results)}/{len(results)})")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
