#!/usr/bin/env python3
"""ADR-037 canary checker — re-verifies every assertion in CANARIES.json against
the current outputs. Exit 0 = all canaries hold (ship it); exit 1 = violation
(block). Run after any converter change; run_all.sh calls this automatically."""
import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "igcse-chemistry-19"

cans = json.loads((HERE / "CANARIES.json").read_text())["canaries"]
fails = []

def load(series):
    d = BASE / series / "4CH1-1C"
    return (json.loads((d / "validation-report.json").read_text()),
            json.loads((d / "topic.json").read_text()))

def find_part(topic, pn):
    for q in topic["questions"]:
        for p in q["parts"]:
            if p["part_number"] == pn:
                return p
    return None

for c in cans:
    cid, chk = c["id"], c["check"]
    series = c["series"]
    try:
        if chk in ("part_unkeyed", "part_keyed_to", "question_count"):
            rep, t = load(series)
            if chk == "question_count":
                ok = len(t["questions"]) == c["expected"]
            else:
                p = find_part(t, c["part"])
                if p is None:
                    ok = False
                elif chk == "part_unkeyed":
                    ok = p.get("choices") and not any(ch.get("is_correct") for ch in p["choices"])
                else:
                    ok = any(ch.get("is_correct") and ch.get("label") == c["label"] for ch in (p.get("choices") or []))
        elif chk == "gate_status":
            rep, t = load(series)
            g = next((g for g in rep["gates"] if g["gate"] == c["gate"]), None)
            ok = g is not None and g["status"] == c["expected"]
            if ok and "marks_total" in c:
                ok = sum(q["total_marks"] for q in t["questions"]) == c["marks_total"]
            if ok and "affected_questions_include" in c:
                ok = (c["affected_questions_include"] in
                      (rep.get("source_defects", {}).get("affected_questions") or []))
        elif chk == "all_gates_pass_and_mcq_keyed":
            rep, t = load(series)
            ok = all(g["status"] == "PASS" for g in rep["gates"])
            keyed = sum(1 for q in t["questions"] for p in q["parts"]
                        if p.get("choices") and any(ch.get("is_correct") for ch in p["choices"]))
            ok = ok and keyed == c["mcq_keyed"]
        elif chk == "negative_controls_all_detected":
            ok = True
            for d in sorted(BASE.iterdir()):
                if not (d / "4CH1-1C" / "validation-report.json").exists():
                    continue
                rep = json.loads((d / "4CH1-1C" / "validation-report.json").read_text())
                for nc in rep.get("negative_controls", []):
                    if not nc.get("detected"):
                        ok = False
                        print(f"  ! {d.name}: {nc.get('id')} MISSED")
        elif chk == "cross_diff_full_agreement":
            cd = json.loads((HERE / "CROSS-DIFF.json").read_text())
            ok = bool(cd["series"]) and all(
                s["comparable_parts"] > 0 and not s["part_mismatches"] and not s["question_mismatches"]
                for s in cd["series"])
        elif chk == "no_hardcoded_output_root":
            # C12 (LEDGER F15): output roots must derive from the checkout, never
            # from a machine-specific mirror path that silently bypasses the
            # canaries' own reads.
            ok = True
            for rel in ("official_examq_extract.py", "cross_diff_parsed.py", "make_multiseries_report.py"):
                p = HERE.parent / "scripts" / rel
                if not p.exists():
                    print(f"  ! scripts/{rel} not found in the checkout")
                    ok = False
                elif "download/syllabai-resources" in p.read_text():
                    print(f"  ! scripts/{rel} still writes to the hardcoded mirror root (F15 regression)")
                    ok = False
        elif chk == "solution_fields_consistent":
            # C13 (v0.5): the reveal + Smart Mark layer must be complete and
            # self-consistent on every series.
            ok = True
            n_linked = n_sol = n_mp = n_badsum = 0
            for d in sorted(BASE.iterdir()):
                if not (d / "4CH1-1C" / "topic.json").exists():
                    continue
                t = json.loads((d / "4CH1-1C" / "topic.json").read_text())
                for q in t["questions"]:
                    for p in q["parts"]:
                        if p.get("answer_status") != "linked":
                            continue
                        n_linked += 1
                        if not p.get("solution_md"):
                            ok = False
                            print(f"  ! {d.name} {p['part_number']}: linked but no solution_md")
                        mp = p.get("mark_points")
                        if mp:
                            n_mp += 1
                            if p.get("marks") is not None and sum(x["marks"] for x in mp) != p["marks"]:
                                ok = False
                                n_badsum += 1
                                print(f"  ! {d.name} {p['part_number']}: mark_points sum != marks")
            print(f"  (linked parts: {n_linked}, with mark_points: {n_mp}, bad sums: {n_badsum})")
        elif chk == "figure_crops_present":
            # C14 (v0.5): the crop pass must keep emitting real PNGs; every
            # crop reference must resolve to a non-trivial file in the checkout.
            ok = True
            n_crops = n_files = 0
            for d in sorted(BASE.iterdir()):
                tp = d / "4CH1-1C" / "topic.json"
                if not tp.exists():
                    continue
                t = json.loads(tp.read_text())
                for q in t["questions"]:
                    for p in q["parts"]:
                        for a in p.get("assets") or []:
                            if a.get("kind") == "crop":
                                n_crops += 1
                                f = d / "4CH1-1C" / a.get("path", "")
                                if not f.exists() or f.stat().st_size < c.get("min_png_bytes", 1000):
                                    ok = False
                                    print(f"  ! {d.name} {p['part_number']}: crop file missing/too small: {a.get('path')}")
                                else:
                                    n_files += 1
            if n_crops < c.get("min_crops", 0):
                ok = False
                print(f"  ! corpus-wide crops {n_crops} < floor {c.get('min_crops')}")
            print(f"  (crops: {n_crops}, files verified: {n_files})")
        elif chk == "g0_summary_contains":
            rep, _ = load(series)
            g = next((g for g in rep["gates"] if g["gate"] == "G0-identity"), None)
            ok = g is not None and g["status"] == "PASS" and c["substring"] in g["summary"]
        else:
            ok = False
            print(f"  ! unknown check type {chk}")
    except Exception as e:
        ok = False
        print(f"  ! {cid}: error {e}")
    print(("PASS  " if ok else "FAIL  ") + cid + f" [{series}] — " + c["assertion"][:90])
    if not ok:
        fails.append(cid)

print()
if fails:
    print(f"CANARIES VIOLATED: {len(fails)} -> {fails}")
    print("Do not ship. Re-run the corpus after fixing; see AGENTS.md improvement loop.")
    sys.exit(1)
print(f"All {len(cans)} canaries hold — corpus consistent with the ledger.")
