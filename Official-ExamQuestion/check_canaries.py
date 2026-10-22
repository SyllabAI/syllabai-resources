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
            # v0.10.1 (F45): the byte floor is recalibrated (1000 -> 250) for the
            # sparse text-only scaffold class (a printed 2-letter skeleton in
            # whitespace compresses below the old floor legitimately), and the
            # degenerate-sliver guard the byte floor was proxying becomes an
            # explicit pixel-dimension floor (PNG IHDR, no new dependency).
            import struct as _struct

            def _png_dims(path):
                with open(path, "rb") as fh:
                    head = fh.read(24)
                if len(head) < 24 or head[:8] != b"\x89PNG\r\n\x1a\n":
                    return None
                w, h = _struct.unpack(">II", head[16:24])
                return w, h

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
                                dims = _png_dims(f) if f.exists() else None
                                if (not f.exists()
                                        or f.stat().st_size < c.get("min_png_bytes", 250)
                                        or dims is None
                                        or dims[0] < c.get("min_px_w", 0)
                                        or dims[1] < c.get("min_px_h", 0)):
                                    ok = False
                                    print(f"  ! {d.name}/{pd.name} {p['part_number']}: crop file missing/too small/degenerate: {a.get('path')} dims={dims}")
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
        elif chk == "mcq_keys_ledger":
            # C31 (v0.8.1/F37): MCQ-KEYS.json and the corpus must agree in both
            # directions — every adjudicated entry is applied to its part (key
            # set on that choice, answer_key_source marker, validation report
            # lists the application), and no part claims adjudication that the
            # ledger does not carry. solution_md must also start from the
            # adjudicated block's first line (the override replaces the
            # mis-linked rows before build_solution runs).
            ledger = json.loads((HERE / "MCQ-KEYS.json").read_text()).get("entries", [])
            ok = True
            n_applied = 0
            corpus = {}
            for d in sorted(BASE.iterdir()):
                if not d.is_dir():
                    continue
                for pd in paper_dirs(d):
                    s = d.name if pd.name == "4CH1-1C" else f"{d.name}:{pd.name.split('-')[1]}"
                    t = json.loads((pd / "topic.json").read_text())
                    rep = json.loads((pd / "validation-report.json").read_text())
                    applied = set(rep.get("mcq_keys_applied") or [])
                    for q in t["questions"]:
                        for p in q["parts"]:
                            if p.get("answer_key_source") == "mcq-keys-ledger":
                                corpus[(s, p["part_number"])] = (p, f"{s}/{p['part_number']}" in applied)
            for e in ledger:
                s, part = e["series"], e["part"]
                if (s, part) not in corpus:
                    ok = False
                    print(f"  ! ledger {s} {part}: no corpus part carries the adjudication")
                    continue
                p, in_report = corpus[(s, part)]
                n_applied += 1
                # F56 (wave 16): the validation report lists applications by the
                # converter's plain series ('2023-01/2(a)(i)'); the corpus home
                # for non-1C papers is '<series>:<paper>' - resolve the home's
                # report before failing (first paper-aware ledger exercise)
                if not in_report and s.count(':'):
                    hs, hp = s.split(':')
                    rep2 = json.loads((BASE / hs / f"4CH1-{hp}" / "validation-report.json").read_text())
                    in_report = f"{hs}/{p['part_number']}" in set(rep2.get("mcq_keys_applied") or [])
                keyed = [ch["label"] for ch in (p.get("choices") or []) if ch.get("is_correct")]
                if keyed != [e["key"]]:
                    ok = False
                    print(f"  ! ledger {s} {part}: key {e['key']} but corpus keyed {keyed}")
                if not in_report:
                    ok = False
                    print(f"  ! ledger {s} {part}: applied but missing from validation report")
                if not (p.get("solution_md") or "").startswith(e["ms_lines"][0].split()[0]):
                    ok = False
                    print(f"  ! ledger {s} {part}: solution_md not rebuilt from adjudicated block")
            for (s, part) in corpus:
                if not any(e["series"] == s and e["part"] == part for e in ledger):
                    ok = False
                    print(f"  ! {s} {part}: answer_key_source marker without a ledger entry")
            print(f"  (ledger entries: {len(ledger)}, applied: {n_applied})")
        elif chk == "spec_tag_terminal":
            # C32 (v0.8.1/F38): spec tagging is terminal on the spec-labelled 1C
            # tranche. Zero pending-llm parts among 1C slices; the
            # no-spec-point state must agree bidirectionally with the series
            # spec-labels files, and every entry must resolve to a real part
            # carrying no codes.
            # v0.9 (F40 wave): paper-aware — the 2C tranche runs the same check
            # with paper=2C and the '<series>-2C.json' label files (C33) after
            # its first wave; 1C stays the legacy default.
            paper = c.get("paper", "1C")
            suffix = "" if paper == "1C" else f"-{paper}"
            ok = True
            n_pending = n_nospec = 0
            nsp_by_series = {}
            for d in sorted(BASE.iterdir()):
                if not d.is_dir():
                    continue
                pd = d / f"4CH1-{paper}"
                if not (pd / "topic.json").exists():
                    continue
                s = d.name
                lp = HERE / "spec-labels" / f"{s}{suffix}.json"
                lab = json.loads(lp.read_text()) if lp.exists() else {}
                nsp_by_series[s] = set((lab.get("no_spec_point") or {}).keys())
                t = json.loads((pd / "topic.json").read_text())
                for q in t["questions"]:
                    for p in q["parts"]:
                        if p.get("tagging") == "pending-llm":
                            ok = False
                            n_pending += 1
                            print(f"  ! {paper} {s} {p['part_number']}: still pending-llm")
                        if p.get("tagging") == "no-spec-point":
                            n_nospec += 1
                            if p["part_number"] not in nsp_by_series[s]:
                                ok = False
                                print(f"  ! {paper} {s} {p['part_number']}: no-spec-point without a labels-file entry")
            for s, parts in nsp_by_series.items():
                if not parts:
                    continue
                t = json.loads((BASE / s / f"4CH1-{paper}" / "topic.json").read_text())
                pn = {p["part_number"] for q in t["questions"] for p in q["parts"]}
                for part in parts:
                    if part not in pn:
                        ok = False
                        print(f"  ! {paper} {s}: no_spec_point entry {part} does not resolve to a part")
                    else:
                        got = [p for q in t["questions"] for p in q["parts"]
                               if p["part_number"] == part][0]
                        if got.get("spec_point_codes"):
                            ok = False
                            print(f"  ! {paper} {s} {part}: labelled no-spec-point but carries codes")
            print(f"  ({paper} pending-llm: {n_pending}, no-spec-point: {n_nospec})")
        elif chk == "part_linked":
            # C46/C47 (v0.9/F40h+F40i): MS-linkage fixes pinned — the named part
            # must be linked with a non-empty solution block.
            t = json.loads((BASE / series / f"4CH1-{c.get('paper', '1C')}" / "topic.json").read_text())
            got = [p for q in t["questions"] for p in q["parts"]
                   if p["part_number"] == c["part"]]
            ok = bool(got) and got[0].get("answer_status") == "linked" \
                and bool((got[0].get("solution_md") or "").strip())
            if not ok:
                print(f"  ! {series} {c.get('paper')} {c['part']}: expected linked with solution_md")
        elif chk == "parts_all_linked":
            # C53 (v0.10/F42): the 2019-06 early-MS bare-marker linkage wave —
            # every named part must exist, be linked, and carry a solution block.
            # Doubles as the damage-repair renumber pin (15(b)(i..iii), 11(b)(iii)).
            t = json.loads((BASE / series / f"4CH1-{c.get('paper', '1C')}" / "topic.json").read_text())
            ok = True
            for pn in c["parts"]:
                got = [p for q in t["questions"] for p in q["parts"] if p["part_number"] == pn]
                if not got or got[0].get("answer_status") != "linked" \
                        or not (got[0].get("solution_md") or "").strip():
                    ok = False
                    print(f"  ! {series} {pn}: expected linked with solution_md")
        elif chk == "part_answer_status":
            # C52 (v0.10/F42): honest-state pins — e.g. 3(d)(ii) stays unmatched
            # because its MS answer cell is a printed image, not text.
            t = json.loads((BASE / series / f"4CH1-{c.get('paper', '1C')}" / "topic.json").read_text())
            got = [p for q in t["questions"] for p in q["parts"] if p["part_number"] == c["part"]]
            ok = bool(got) and got[0].get("answer_status") == c["expected"]
            if not ok:
                st = got[0].get("answer_status") if got else "PART MISSING"
                print(f"  ! {series} {c['part']}: expected answer_status {c['expected']!r}, got {st!r}")
        elif chk == "part_problem_md_contains":
            # C49/C50/C51 (v0.10/F41): OCR-recovered verbatim pins — the
            # transcribed spans (equation subscripts, table values) must never
            # silently regress to the raw-OCR garble.
            t = json.loads((BASE / series / f"4CH1-{c.get('paper', '1C')}" / "topic.json").read_text())
            if c.get("question") is not None:
                q = next((q for q in t["questions"] if q["question_number"] == c["question"]), None)
                text = (q.get("stem_md") or "") if q else ""
                if not text and q is not None:
                    text = " ".join(p.get("problem_md") or "" for p in q["parts"])
            else:
                got = [p for q in t["questions"] for p in q["parts"] if p["part_number"] == c["part"]]
                text = (got[0].get("problem_md") or "") if got else ""
            needles = c.get("contains_all") or ([c["substring"]] if c.get("substring") else [])
            ok = bool(text) and all(n in text for n in needles)
            if not ok:
                print(f"  ! {series} {c.get('question') or c.get('part')}: pinned text missing {needles}")
        elif chk == "part_solution_md_contains":
            # C66 (wave 16): served-solution pins - the F53 de-interleave and
            # F54 total-row drop must keep their exact reconstructed shapes
            # (the pre-wave interleaved garble must never silently return)
            t = json.loads((BASE / series / f"4CH1-{c.get('paper', '1C')}" / "topic.json").read_text())
            got = [p for q in t["questions"] for p in q["parts"] if p["part_number"] == c["part"]]
            text = (got[0].get("solution_md") or "") if got else ""
            needles = c.get("contains_all") or ([c["substring"]] if c.get("substring") else [])
            banned = c.get("contains_none") or []
            ok = bool(text) and all(n in text for n in needles) and not any(b in text for b in banned)
            if not ok:
                print(f"  ! {series} {c.get('part')}: pinned solution text mismatch")
        elif chk == "solution_blocks_header_free":
            # C54 (v0.10/F43): no served solution block may carry the repeated
            # MS page-table header — a marker row near a page break used to
            # inherit the next page's 'Question / Answer (Notes) Marks / number'
            # lines into solution_md/mark_points corpus-wide.
            import re as _re
            hdr = _re.compile(r"Question\s*Answer( Additional guidance)? Notes Marks\s*number|Question\s*\n?\s*Answer Notes Marks\s*\n?\s*number")
            ok = True
            n = 0
            for d in sorted(BASE.iterdir()):
                if not d.is_dir():
                    continue
                for pd in paper_dirs(d):
                    t = json.loads((pd / "topic.json").read_text())
                    for q in t["questions"]:
                        for p in q["parts"]:
                            s = p.get("solution_md") or ""
                            mps = p.get("mark_points") or []
                            n += 1
                            if hdr.search(s) or any(hdr.search(m.get("text_md") or "") for m in mps):
                                ok = False
                                print(f"  ! {d.name}/{pd.name} {p['part_number']}: solution block carries the MS page-table header")
            print(f"  (solution blocks scanned: {n})")
        elif chk == "no_pua_served":
            # C56 (v0.11/F48): no served string in any topic.json may carry a
            # Private Use Area char (U+E000–U+F8FF) — every symbol-font glyph
            # must surface as its real Unicode form (PUA_MAP). The optional
            # pins re-prove specific evidenced mappings at their exact parts,
            # so a silent PUA_MAP regression (e.g. mapping a glyph to '')
            # cannot pass the absence law.
            # v0.13.1 (F52): the optional canary field extra_chars [[bad, good], ...]
            # extends the absence law beyond the PUA range to any evidenced
            # source-char artifact (the MyriadPro-It italic-Delta U+01FB).
            ok = True
            n_files = 0
            extra_bad = {chr(x[0]): x for x in (c.get("extra_chars") or [])}

            def _walk(o, path, hits):
                if isinstance(o, dict):
                    for k, v in o.items():
                        _walk(v, f"{path}.{k}", hits)
                elif isinstance(o, list):
                    for i, v in enumerate(o):
                        _walk(v, f"{path}[{i}]", hits)
                elif isinstance(o, str):
                    for idx, ch in enumerate(o):
                        if 0xE000 <= ord(ch) <= 0xF8FF:
                            hits.append(f"{path}[{idx}]=U+{ord(ch):04X}")
                        elif ch in extra_bad:
                            hits.append(f"{path}[{idx}]=U+{ord(ch):04X} (extra_chars law)")

            for d in sorted(BASE.iterdir()):
                if not d.is_dir():
                    continue
                for pd in paper_dirs(d):
                    t = json.loads((pd / "topic.json").read_text())
                    n_files += 1
                    hits = []
                    _walk(t, "$", hits)
                    for h in hits[:3]:
                        print(f"  ! {d.name}/{pd.name}: PUA char served at {h}")
                    if hits:
                        ok = False
            for pin in c.get("pins") or []:
                t = json.loads((BASE / pin["series"] /
                                f"4CH1-{pin.get('paper', '1C')}" / "topic.json").read_text())
                texts = []
                for q in t["questions"]:
                    for p in q["parts"]:
                        if pin.get("part") and p["part_number"] != pin["part"]:
                            continue
                        if pin.get("field") == "stem":
                            texts.append(q.get("stem_md") or "")
                        else:
                            fields = [p.get("problem_md") or "",
                                      p.get("solution_md") or "",
                                      "\n".join(m.get("text_md") or ""
                                                for m in p.get("mark_points") or [])]
                            texts.append("\n".join(fields))
                if not any(pin["contains"] in tx for tx in texts):
                    ok = False
                    print(f"  ! pin missing: {pin['series']}/{pin.get('paper', '1C')} "
                          f"{pin.get('part')} {pin['contains']!r}")
            print(f"  (topic.json scanned: {n_files}, pins: {len(c.get('pins') or [])})")
        elif chk == "ms_link_overrides_ledger":
            # C57 (v0.11/F47): MS-LINK-OVERRIDES.json and the corpus must agree
            # in both directions — every adjudicated entry is applied to its
            # part (linked, answer_key_source marker, validation report lists
            # the application, solution_md rebuilt from the adjudicated block),
            # and no part claims adjudication that the ledger does not carry.
            ledger = json.loads((HERE / "MS-LINK-OVERRIDES.json").read_text()).get("entries", [])
            ok = True
            n_applied = 0
            corpus = {}
            for d in sorted(BASE.iterdir()):
                if not d.is_dir():
                    continue
                for pd in paper_dirs(d):
                    paper = pd.name.split("-")[1]
                    rep = json.loads((pd / "validation-report.json").read_text())
                    applied = set(rep.get("ms_link_overrides_applied") or [])
                    t = json.loads((pd / "topic.json").read_text())
                    for q in t["questions"]:
                        for p in q["parts"]:
                            if p.get("answer_key_source") == "ms-link-overrides-ledger":
                                corpus[(d.name, paper, p["part_number"])] = (
                                    p, f"{d.name}:{paper}/{p['part_number']}" in applied)
            for e in ledger:
                s, paper, part = e["series"], e["paper"], e["part"]
                if (s, paper, part) not in corpus:
                    ok = False
                    print(f"  ! ledger {s}:{paper} {part}: no corpus part carries the adjudication")
                    continue
                p, in_report = corpus[(s, paper, part)]
                n_applied += 1
                if p.get("answer_status") != "linked":
                    ok = False
                    print(f"  ! ledger {s}:{paper} {part}: applied but answer_status != linked")
                if not in_report:
                    ok = False
                    print(f"  ! ledger {s}:{paper} {part}: applied but missing from validation report")
                if not (p.get("solution_md") or "").startswith(e["ms_lines"][0].split()[0]):
                    ok = False
                    print(f"  ! ledger {s}:{paper} {part}: solution_md not rebuilt from adjudicated block")
            for (s, paper, part) in corpus:
                if not any(e["series"] == s and e["paper"] == paper and e["part"] == part
                           for e in ledger):
                    ok = False
                    print(f"  ! {s}:{paper} {part}: answer_key_source marker without a ledger entry")
            print(f"  (ledger entries: {len(ledger)}, applied: {n_applied})")
        elif chk == "ocr_pages_receipt":
            # C48 (v0.10/F41): the OCR source-layer receipts must be present and
            # cover exactly the recovered pages (fail-closed sha verification is
            # G0's job at run time; this pins the receipt census).
            rep, _ = load(series, c.get("paper", "1C"))
            pages = [e["page"] for e in rep.get("ocr_pages", [])]
            ok = pages == c["pages"]
            if not ok:
                print(f"  ! {series} {c.get('paper')}: ocr_pages {pages} != {c['pages']}")
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
