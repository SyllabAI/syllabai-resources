#!/usr/bin/env python3
"""
T-SPECS-CIE-INDEX-1 battery — H1-H10 for the SME-native spec-point index
harvest of the 44 CIE lanes.

Run AFTER scripts/cie_spcpt_index_harvest.py has staged the 44
SME-ExamQuestion/<lane>/spec_point_index.json files. Reads the staged
entries from the git index (the files live outside the sparse cone).
Independent re-derivations re-read the corpus blobs fresh.

Output: graph/reports/T_SPECS_CIE_INDEX_1_CHECK.json; exit 0 iff ALL PASS.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))
import cie_spcpt_index_harvest as engine  # noqa: E402

OUT = REPO / "graph" / "reports" / "T_SPECS_CIE_INDEX_1_CHECK.json"
DECLARED = ({f"SME-ExamQuestion/{lane}/spec_point_index.json" for lane in
             engine.lanes()}
            | {"scripts/cie_spcpt_index_harvest.py",
               "scripts/cie_index_harvest_check.py",
               "graph/reports/T_SPECS_CIE_INDEX_1_RECORD.md",
               "graph/reports/T_SPECS_CIE_INDEX_1_HARVEST.json",
               "graph/reports/T_SPECS_CIE_INDEX_1_CHECK.json"})

results: list[dict] = []


def check(cid: str, fn) -> None:
    try:
        detail = fn()
        results.append({"id": cid, "pass": True, "detail": detail})
        print(f"H{cid} PASS: {detail}")
    except AssertionError as exc:
        results.append({"id": cid, "pass": False, "detail": str(exc)})
        print(f"H{cid} FAIL: {exc}")


def staged_bytes(path: str) -> bytes:
    ls = subprocess.run(["git", "-C", str(REPO), "ls-files", "-s", "--", path],
                        capture_output=True, check=True).stdout.decode().split()
    if len(ls) < 2:
        raise AssertionError(f"{path} not in index")
    return subprocess.run(["git", "-C", str(REPO), "cat-file", "-p", ls[1]],
                          capture_output=True, check=True).stdout


def require(cond: bool, msg: str) -> None:
    if not cond:
        raise AssertionError(msg)


def fresh_lane_universe(lane: str):
    """Independent re-derivation of the lane's spec_points + EQ refs."""
    targets = engine.list_targets(lane)
    blobs = engine.read_blobs(targets)
    spec: dict[str, dict] = {}
    note_ids: set[str] = set()
    note_stems: set[str] = set()
    n_notes = n_eq = 0
    eq_refs: list[str] = []
    for oid, path, kind in targets:
        doc = json.loads(blobs[oid].decode("utf-8"))
        if kind == "manifest":
            continue
        if kind == "note":
            n_notes += 1
            note_ids.add(doc["note_id"])
            note_stems.add(path.rsplit("/", 1)[-1][:-5])
            hits: list[dict] = []
            engine.walk_blocks(doc.get("blocks", []), hits)
            for h in hits:
                e = spec.setdefault(h["id"], {"name": h["name"],
                                              "definition": h["definition"],
                                              "notes": set(), "slugs": set()})
                if not e["definition"] and h["definition"]:
                    e["definition"] = h["definition"]
                e["notes"].add(doc["note_id"])
                e["slugs"].add(path.rsplit("/", 1)[-1][:-5])
        else:
            n_eq += 1
            eq_refs.extend(engine.eq_part_ids(doc))
    return spec, note_ids, note_stems, n_notes, n_eq, eq_refs


def main() -> int:
    lanes = engine.lanes()
    staged = {lane: staged_bytes(
        f"SME-ExamQuestion/{lane}/spec_point_index.json") for lane in lanes}
    docs = {lane: json.loads(staged[lane]) for lane in lanes}

    def h1() -> str:
        for lane in lanes:
            d = docs[lane]
            raw = staged[lane]
            require(list(d.keys()) == ["schema", "generated_utc", "course_slug",
                                       "notes_base", "source_pages",
                                       "fetch_failures", "spec_points",
                                       "coverage"], f"{lane} doc key order")
            require(d["schema"] == engine.SCHEMA, f"{lane} schema")
            require(d["course_slug"] == lane, f"{lane} course_slug")
            require(d["notes_base"].startswith("https://www.savemyexams.com/"),
                    f"{lane} notes_base")
            require(d["source_pages"] > 0, f"{lane} source_pages")
            require(d["fetch_failures"] == [], f"{lane} fetch_failures")
            require(d["generated_utc"] == engine.FIXED_STAMP, f"{lane} stamp")
            require(not raw.endswith(b"\n"), f"{lane} trailing newline")
            for sid, e in d["spec_points"].items():
                require(list(e.keys()) == ["name", "definition", "notes",
                                           "subtopic_slugs"],
                        f"{lane} entry key order {sid}")
                require(sid.startswith("spcpt_"), f"{lane} id prefix {sid}")
        return f"44/44 well-formed (schema/stamp/keys/no-trailing-NL)"

    fresh: dict[str, tuple] = {}

    def h2() -> str:
        total = 0
        for lane in lanes:
            spec, *_ = fresh_lane_universe(lane)
            fresh[lane] = None
            fresh[lane] = spec
            require(set(spec) == set(docs[lane]["spec_points"]),
                    f"{lane} universe ids mismatch")
            side = json.loads((REPO / "spec-links" / f"{lane}.json")
                              .read_text(encoding="utf-8"))
            require(side["anchors"]["universe_ids"] == len(spec),
                    f"{lane} sidecar universe {side['anchors']['universe_ids']} "
                    f"!= {len(spec)}")
            total += len(spec)
        require(total == 8651, f"universe sum {total} != 8651")
        return f"universe conservation 44/44, sum {total} == 8651"

    def h3() -> str:
        tu = tc = tm = tr = 0
        for lane in lanes:
            spec = fresh[lane]
            targets = [t for t in engine.list_targets(lane) if t[2] == "eq"]
            blobs = engine.read_blobs(targets)
            eq_refs: list[str] = []
            for oid, _p, _k in targets:
                eq_refs.extend(engine.eq_part_ids(
                    json.loads(blobs[oid].decode("utf-8"))))
            uniq = sorted(set(eq_refs))
            cov = [s for s in uniq if s in spec]
            mis = [s for s in uniq if s not in spec]
            c = docs[lane]["coverage"]
            require(c["question_part_ids_total"] == len(uniq),
                    f"{lane} total {c['question_part_ids_total']} != {len(uniq)}")
            require(c["covered_by_index"] == len(cov), f"{lane} covered")
            require(c["missing_from_index"] == mis, f"{lane} missing list")
            require(len(cov) + len(mis) == len(uniq), f"{lane} arithmetic")
            tu += len(uniq); tc += len(cov); tm += len(mis); tr += len(eq_refs)
        require((tu, tc, tm) == (5540, 5218, 322),
                f"sums {(tu, tc, tm)} != (5540, 5218, 322)")
        return (f"coverage arithmetic 44/44; refs {tr}, unique {tu} = "
                f"covered {tc} + missing {tm}")

    def h4() -> str:
        n = 0
        for lane in lanes:
            spec = fresh[lane]
            for sid, e in docs[lane]["spec_points"].items():
                f = spec[sid]
                require(e["name"] == f["name"], f"{lane} {sid} name")
                require(e["definition"] == f["definition"],
                        f"{lane} {sid} definition")
                require(e["notes"] == sorted(f["notes"]), f"{lane} {sid} notes")
                require(e["subtopic_slugs"] == sorted(f["slugs"]),
                        f"{lane} {sid} slugs")
                n += 1
        return f"{n} spec_point entries deep-equal vs fresh corpus re-derivation"

    def h5() -> str:
        for lane in lanes:
            spec, note_ids, note_stems, n_notes, _n_eq, _r = fresh_lane_universe(lane)
            d = docs[lane]
            require(d["source_pages"] == n_notes,
                    f"{lane} source_pages {d['source_pages']} != {n_notes}")
            for sid, e in d["spec_points"].items():
                require(set(e["notes"]) <= note_ids, f"{lane} {sid} rn dangling")
                require(set(e["subtopic_slugs"]) <= note_stems,
                        f"{lane} {sid} slug dangling")
        return "notes/subtopic provenance internal to the lane corpus, 44/44"

    def h6() -> str:
        universes = {lane: set(docs[lane]["spec_points"]) for lane in lanes}
        all_ids = set().union(*universes.values())
        cur = unc = 0
        for lane in lanes:
            mis = docs[lane]["coverage"]["missing_from_index"]
            for sid in mis:
                require(sid not in universes[lane],
                        f"{lane} {sid} missing but in universe")
            others = all_ids - universes[lane]
            cur += len(set(mis) & others)
            unc += len(set(mis) - others)
        require((cur, unc) == (54, 268),
                f"cross-lane {(cur, unc)} != (54, 268)")
        return (f"dangling honesty 44/44; cross-lane curable {cur}, "
                f"definition-less {unc}")

    def h7() -> str:
        out = subprocess.run(
            ["git", "-C", str(REPO), "diff", "HEAD", "--name-only", "--",
             "SME-ExamQuestion/"], capture_output=True, check=True
        ).stdout.decode().splitlines()
        added = {p for p in out if p.endswith("spec_point_index.json")}
        new_cie = {f"SME-ExamQuestion/{l}/spec_point_index.json" for l in lanes}
        require(added == new_cie,
                f"SME-ExamQuestion delta != the 44 CIE files: extra="
                f"{sorted(added - new_cie)[:5]}")
        edex = [p for p in subprocess.run(
            ["git", "-C", str(REPO), "ls-tree", "-r", "HEAD", "--name-only",
             "SME-ExamQuestion/"], capture_output=True, check=True
        ).stdout.decode().splitlines() if p.endswith("spec_point_index.json")]
        require(len(edex) == 49, f"Edexcel indexes {len(edex)} != 49")
        for p in edex:
            require(p not in out, f"Edexcel file modified: {p}")
        return f"49 Edexcel indexes untouched; SME-ExamQuestion delta == 44 CIE files"

    def h8() -> str:
        st = subprocess.run(["git", "-C", str(REPO), "status", "--porcelain"],
                            capture_output=True, check=True).stdout.decode()
        seen = set()
        for line in st.splitlines():
            path = line[3:].strip().strip('"')
            seen.add(path)
        extra = sorted(seen - DECLARED)
        require(not extra, f"undeclared paths: {extra[:8]}")
        for guard in ("spec-links/", "SME-RevisionNotes/",
                      "Official-Specifications/", "SME-Flashcards/"):
            bad = [p for p in seen if p.startswith(guard)]
            require(not bad, f"{guard} touched: {bad[:5]}")
        return f"footprint {len(seen)} paths ⊆ declared set; guards intact"

    def h9() -> str:
        before = {lane: hashlib.sha256(staged[lane]).hexdigest()
                  for lane in lanes}
        r = subprocess.run([sys.executable, str(REPO / "scripts" /
                            "cie_spcpt_index_harvest.py")],
                           capture_output=True, text=True)
        require(r.returncode == 0, f"engine re-run failed: {r.stderr[-400:]}")
        for lane in lanes:
            b = staged_bytes(f"SME-ExamQuestion/{lane}/spec_point_index.json")
            require(hashlib.sha256(b).hexdigest() == before[lane],
                    f"{lane} re-run byte drift")
        return "engine fixed-stamp re-run byte-identical across all 44 files"

    def h10() -> str:
        for lane in ("cie-igcse-biology-23", "cie-igcse-maths-25-extended"):
            spec, _ni, _ns, n_notes, _ne, eq_refs = fresh_lane_universe(lane)
            uniq = sorted(set(eq_refs))
            sp = {sid: {"name": e["name"], "definition": e["definition"],
                        "notes": sorted(e["notes"]),
                        "subtopic_slugs": sorted(e["slugs"])}
                  for sid, e in sorted(spec.items())}
            rebuild = {
                "schema": engine.SCHEMA,
                "generated_utc": engine.FIXED_STAMP,
                "course_slug": lane,
                "notes_base": docs[lane]["notes_base"],
                "source_pages": n_notes,
                "fetch_failures": [],
                "spec_points": sp,
                "coverage": {
                    "question_part_ids_total": len(uniq),
                    "covered_by_index": len([s for s in uniq if s in spec]),
                    "missing_from_index": [s for s in uniq if s not in spec],
                },
            }
            rb = json.dumps(rebuild, ensure_ascii=False, indent=1).encode("utf-8")
            require(rb == staged[lane], f"{lane} rebuild != staged bytes")
        return "2-lane independent in-battery rebuild == staged bytes"

    check("1", h1)
    check("2", h2)
    check("3", h3)
    check("4", h4)
    check("5", h5)
    check("6", h6)
    check("7", h7)
    check("8", h8)
    check("9", h9)
    check("10", h10)

    all_pass = all(r["pass"] for r in results)
    OUT.write_text(json.dumps({
        "battery": "T-SPECS-CIE-INDEX-1",
        "all_pass": all_pass,
        "checks": results,
    }, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    print(f"\nALL {'PASS' if all_pass else 'FAIL'} "
          f"({sum(r['pass'] for r in results)}/{len(results)})")
    return 0 if all_pass else 1


if __name__ == "__main__":
    sys.exit(main())
