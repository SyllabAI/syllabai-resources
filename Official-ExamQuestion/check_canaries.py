#!/usr/bin/env python3
"""ADR-037 canary checker — re-verifies every assertion in CANARIES.json against
the current outputs. Exit 0 = all canaries hold (ship it); exit 1 = violation
(block). Run after any converter change; run_all.sh calls this automatically."""
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
BASE = HERE / "igcse-chemistry-19"

_solution_stats = {"linked": 0, "mp": 0, "badsum": 0}


def _solution_check(series_name, paper_name, p):
    """C13 per-part check (linked parts carry solution_md; mark_points sum to marks)."""
    if p.get("answer_status") != "linked":
        return
    _solution_stats["linked"] += 1
    if not p.get("solution_md"):
        raise AssertionError(f"{series_name}/{paper_name} {p['part_number']}: linked but no solution_md")
    mp = p.get("mark_points")
    if mp:
        _solution_stats["mp"] += 1
        if p.get("marks") is not None and sum(x["marks"] for x in mp) != p["marks"]:
            _solution_stats["badsum"] += 1
            raise AssertionError(f"{series_name}/{paper_name} {p['part_number']}: mark_points sum != marks")

cans = json.loads((HERE / "CANARIES.json").read_text())["canaries"]
fails = []

def load(series, paper="1C"):
    d = BASE / series / f"4CH1-{paper}"
    return (json.loads((d / "validation-report.json").read_text()),
            json.loads((d / "topic.json").read_text()))


def paper_dirs(series_dir):
    """All paper-variant dirs with outputs under a series dir (1C, 2C, ...)."""
    return sorted(p for p in series_dir.iterdir()
                  if p.is_dir() and re.match(r"4CH1-[0-9][A-Z]R?$", p.name)
                  and (p / "topic.json").exists())

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
            rep, t = load(series, c.get("paper", "1C"))
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
            rep, t = load(series, c.get("paper", "1C"))
            g = next((g for g in rep["gates"] if g["gate"] == c["gate"]), None)
            ok = g is not None and g["status"] == c["expected"]
            if ok and "marks_total" in c:
                ok = sum(q["total_marks"] for q in t["questions"]) == c["marks_total"]
            if ok and "affected_questions_include" in c:
                ok = (c["affected_questions_include"] in
                      (rep.get("source_defects", {}).get("affected_questions") or []))
        elif chk == "all_gates_pass_and_mcq_keyed":
            rep, t = load(series, c.get("paper", "1C"))
            ok = all(g["status"] == "PASS" for g in rep["gates"])
            keyed = sum(1 for q in t["questions"] for p in q["parts"]
                        if p.get("choices") and any(ch.get("is_correct") for ch in p["choices"]))
            ok = ok and keyed == c["mcq_keyed"]
        elif chk == "negative_controls_all_detected":
            ok = True
            for d in sorted(BASE.iterdir()):
                if not d.is_dir():
                    continue
                for pd in paper_dirs(d):
                    rep = json.loads((pd / "validation-report.json").read_text())
                    for nc in rep.get("negative_controls", []):
                        if not nc.get("detected"):
                            ok = False
                            print(f"  ! {d.name}/{pd.name}: {nc.get('id')} MISSED")
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
            # self-consistent on every series (every paper variant since F34).
            ok = True
            _n_linked = _n_mp = _n_badsum = 0
            for d in sorted(BASE.iterdir()):
                if not d.is_dir():
                    continue
                for pd in paper_dirs(d):
                    t = json.loads((pd / "topic.json").read_text())
                    for q in t["questions"]:
                        for p in q["parts"]:
                            _solution_check(d.name, pd.name, p)
            print(f"  (linked parts: {_solution_stats['linked']}, with mark_points: {_solution_stats['mp']}, bad sums: {_solution_stats['badsum']})")
        elif chk == "figure_crops_present":
            # C14 (v0.5): the crop pass must keep emitting real PNGs; every
            # crop reference must resolve to a non-trivial file in the checkout.
            ok = True
            n_crops = n_files = 0
            for d in sorted(BASE.iterdir()):
                if not d.is_dir():
                    continue
                for pd in paper_dirs(d):
                    t = json.loads((pd / "topic.json").read_text())
                    for q in t["questions"]:
                        for p in q["parts"]:
                            for a in p.get("assets") or []:
                                if a.get("kind") != "crop":
                                    continue
                                n_crops += 1
                                f = pd / a.get("path", "")
                                if not f.exists() or f.stat().st_size < c.get("min_png_bytes", 1000):
                                    ok = False
                                    print(f"  ! {d.name}/{pd.name} {p['part_number']}: crop file missing/too small: {a.get('path')}")
                                else:
                                    n_files += 1
            if n_crops < c.get("min_crops", 0):
                ok = False
                print(f"  ! corpus-wide crops {n_crops} < floor {c.get('min_crops')}")
            print(f"  (crops: {n_crops}, files verified: {n_files})")
        elif chk == "asset_state":
            # C15–C21 (v0.6): figure-serving semantics pinned per part — the
            # exact resolutions from the crop-review wave must hold forever.
            t = json.loads((BASE / series / f"4CH1-{c.get('paper', '1C')}" / "topic.json").read_text())
            assets = [a for q in t["questions"] for p in q["parts"]
                      if p["part_number"] == c["part"] for a in (p.get("assets") or [])]
            if c.get("empty"):
                ok = not assets
                if not ok:
                    print(f"  ! {c['part']}: expected NO assets, got {assets[:1]}")
            else:
                matches = [a for a in assets if a.get("kind") == c.get("kind")]
                if c.get("shared") is not None:
                    matches = [a for a in matches if bool(a.get("shared")) == c["shared"]]
                if c.get("ref_part") is not None:
                    matches = [a for a in matches if a.get("ref_part") == c["ref_part"]]
                if c.get("page") is not None:
                    matches = [a for a in matches if a.get("page") == c["page"]]
                if c.get("path_contains"):
                    matches = [a for a in matches
                               if c["path_contains"] in (a.get("path") or "")]
                ok = bool(matches)
                if not ok:
                    print(f"  ! {c['part']}: no asset matches {c}")
        elif chk == "g0_summary_contains":
            rep, _ = load(series, c.get("paper", "1C"))
            g = next((g for g in rep["gates"] if g["gate"] == "G0-identity"), None)
            ok = g is not None and g["status"] == "PASS" and c["substring"] in g["summary"]
        elif chk == "crop_review_ledger":
            # C22 (v0.7/v0.7.1): the CROP-REVIEW.json verdict ledger and the
            # emitted corpus must agree in both directions. Verdict vocabulary:
            # 'accepted' pairs with kind=="crop", 'stub-accepted' pairs with
            # kind=="crop-required" (the eyeballed honest-stub decision).
            ledger = json.loads((HERE / "CROP-REVIEW.json").read_text()).get("reviews", {})
            ok = True
            n_verdicts = 0
            for d in sorted(BASE.iterdir()):
                if not d.is_dir():
                    continue
                for pd in paper_dirs(d):
                    # ledger keying: 1C keeps the legacy bare series name; other
                    # papers (F34) use '<series>:<paper>' so verdict homes never
                    # collide across variants.
                    s = d.name if pd.name == "4CH1-1C" else f"{d.name}:{pd.name.split('-')[1]}"
                    t = json.loads((pd / "topic.json").read_text())
                    assets = {a["id"]: a for q in t["questions"] for p in q["parts"]
                              for a in (p.get("assets") or [])}
                    for aid, v in (ledger.get(s) or {}).items():
                        n_verdicts += 1
                        vd = v.get("verdict")
                        want_kind = {"accepted": "crop", "stub-accepted": "crop-required"}.get(vd)
                        if want_kind is None:
                            ok = False
                            print(f"  ! {s}: ledger verdict {vd!r} for {aid} is not a known kind")
                        elif aid not in assets:
                            ok = False
                            print(f"  ! {s}: ledger {vd} {aid} but no such asset exists")
                        elif assets[aid].get("kind") != want_kind:
                            ok = False
                            print(f"  ! {s}: ledger {vd} {aid} but asset kind is "
                                  f"{assets[aid].get('kind')!r} (want {want_kind})")
                    for aid, a in assets.items():
                        rv = a.get("review_verdict")
                        if rv and not ((ledger.get(s) or {}).get(aid, {}).get("verdict") == rv):
                            ok = False
                            print(f"  ! {s}: {aid} carries review_verdict {rv!r} without a "
                                  f"matching ledger entry")
                        if a.get("kind") == "crop" and rv == "stub-accepted":
                            ok = False
                            print(f"  ! {s}: crop asset {aid} must not carry stub-accepted")
                        if a.get("kind") == "crop-required" and rv == "accepted":
                            ok = False
                            print(f"  ! {s}: stub asset {aid} must not carry accepted")
            print(f"  (ledger verdicts: {n_verdicts})")
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
