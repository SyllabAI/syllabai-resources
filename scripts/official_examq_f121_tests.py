#!/usr/bin/env python3
"""F121 group-stem restore wave — zero-network unit battery (CI step).

Covers:
  A  the ledger of record: 48 group verdicts (36 F121 + 13 F123 2019-06
     stem-figure stubs) + the F125 part-level verdicts, shapes, served_by
     evidence
  B  the live anchor law: every cut anchor aligns whitespace-tolerantly and
     UNIQUELY against its raw corpus group_stem_md / part problem_md, and
     the pre-cut context ends complete prose
  C  restore_group_stem laws (mechanical / drop-tail / dropSpan / splice-guard
     / replace / empty) incl. the fail-closed refusals; the F125
     apply_part_cut laws (mirrored anchors, the of-record trailing-
     punctuation law, fail-closed refusals)
  D  G-E7 negative controls on a synthetic lane (stem missing on the
     group-first part; an adjudicated cut surviving; a stale group ledger
     key; the F125 part-level classes: a surviving part cut, a part cut
     whose served_by is not a crop asset of the part, a stale part key)
     + the happy-path accounting
  E  the live 567-census law: every non-empty group stem resolves to a
     group-first part on all 54 slices
  F  the print-order pin: 2019-06 2C Q5(a)(i) serves stem < aircraft fig <
     group stem < formulae fig < bond-tables fig; the F125 live pin:
     2019-06 1CR 8(b)(i) serves the cleaned part text with the soup cut and
     the re-cropped grid figure
"""
import json
import re
import sys
from pathlib import Path

RES = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(RES / "scripts"))

import official_examq_export_hub as ex  # noqa: E402

LEDGER = json.load(open(RES / "Official-ExamQuestion" / "STEM-RESTORE.json"))
CORPUS = RES / "Official-ExamQuestion" / "igcse-chemistry-19"

_checks = {"n": 0, "pass": 0}


def check(name, cond, detail=""):
    _checks["n"] += 1
    if cond:
        _checks["pass"] += 1
        print(f"  ok  {name}")
    else:
        print(f"  FAIL {name} {detail}")
        raise SystemExit(f"F121 battery FAILED at: {name} {detail}")


def expect_refuse(name, fn, needle):
    _checks["n"] += 1
    try:
        fn()
    except ex.ExportGateError as e:
        if needle in str(e):
            _checks["pass"] += 1
            print(f"  ok  {name} (refused: {str(e)[:80]}…)")
            return
        raise SystemExit(f"F121 battery FAILED at {name}: refused with the wrong "
                         f"error: {e}")
    except Exception as e:  # noqa: BLE001
        raise SystemExit(f"F121 battery FAILED at {name}: wrong exception "
                         f"{type(e).__name__}: {e}")
    raise SystemExit(f"F121 battery FAILED at {name}: no refusal raised")


def normsp(s):
    return re.sub(r"\s+", " ", s or "").strip()


def align(anchor, raw):
    """Whitespace-tolerant alignment (the builder's law, inlined)."""
    toks = anchor.split()
    for start in range(len(raw)):
        i, ti = start, 0
        while i < len(raw) and ti < len(toks):
            while i < len(raw) and raw[i].isspace():
                i += 1
            if i >= len(raw):
                break
            if raw.startswith(toks[ti], i):
                i += len(toks[ti])
                ti += 1
            else:
                break
        if ti == len(toks):
            return start, i
    return None


def group_keys():
    return {k: v for k, v in LEDGER["verdicts"].items()
            if "." in k.split(":")[-1] and "(" not in k.split(":")[-1]}


def part_keys():
    """F125: the part-level verdict space (parenthesized suffixes)."""
    return {k: v for k, v in LEDGER["verdicts"].items()
            if "(" in k.split(":")[-1]}


def raw_stem(key):
    sp, qgl = key.split(":")
    series, paper_code = sp.split("/")
    qnum, letter = qgl[1:].split(".")
    paper = paper_code.replace("4CH1-", "")
    t = json.load(open(CORPUS / series / f"4CH1-{paper}" / "topic.json"))
    q = next(x for x in t["questions"] if str(x["question_number"]) == qnum)
    return q, (q["groups"][letter]["group_stem_md"] or "").strip(), paper, qnum, letter


def raw_part(key):
    """F125: (question, raw part problem_md, paper, qnum, part) for a
    part-level ledger key — the part is found by its derived ledger key."""
    sp, qgl = key.split(":")
    series, paper_code = sp.split("/")
    qnum, suffix = qgl[1:].split(".", 1)
    paper = paper_code.replace("4CH1-", "")
    t = json.load(open(CORPUS / series / f"4CH1-{paper}" / "topic.json"))
    q = next(x for x in t["questions"] if str(x["question_number"]) == qnum)
    p = next(x for x in q["parts"]
             if ex.part_ledger_key(qnum, x["part_number"]) == f"Q{qnum}.{suffix}")
    return q, (p["problem_md"] or "").strip(), paper, qnum, p


# ---------------------------------------------------------------- A: ledger
def section_a():
    print("A. the ledger of record")
    gk = group_keys()
    check("48 group verdicts present (36 F121 + 13 F123)", len(gk) == 48, f"got {len(gk)}")
    check("all group verdicts carry a known verdict",
          all(v.get("verdict") in ("drop-tail", "keep", "replace") for v in gk.values()))
    check("every cut verdict carries served_by + why evidence",
          all(("served_by" in v and "why" in v)
              for v in gk.values() if v.get("tail") or v.get("dropSpan") or v.get("dropTail")))
    figs = {k: v["figures"] for k, v in gk.items() if v.get("figures")}
    check("exactly 5 figures declarations (3 F121 + 2 F122)", len(figs) == 5, f"got {len(figs)}")
    # F125: the part-level verdict space
    pk = part_keys()
    check("1 part-level verdict present (F125)", len(pk) == 1, f"got {len(pk)}")
    check("part verdict carries a known verdict",
          all(v.get("verdict") in ("drop-tail", "keep", "replace") for v in pk.values()))
    check("every part cut verdict carries served_by + why + crop evidence",
          all(("served_by" in v and "why" in v and "cropRect" in v)
              for v in pk.values() if v.get("tail") or v.get("dropSpan") or v.get("dropTail")))


# ------------------------------------------------------------- B: live anchors
def section_b():
    print("B. the live anchor law (raw corpus bytes)")
    for key, v in sorted(group_keys().items()):
        raw = raw_stem(key)[1]
        cuts = []
        if v.get("tail"):
            cuts.append(("tail", v["tail"]))
        if v.get("dropTail"):
            cuts.append(("dropTail", v["dropTail"]))
        if v.get("dropSpan"):
            cuts.append(("dropSpan-from", v["dropSpan"][0]))
            cuts.append(("dropSpan-to", v["dropSpan"][1]))
        for kind, anchor in cuts:
            pos = align(anchor, raw)
            assert pos is not None, f"{key} {kind}: anchor does not align"
            assert raw.count(anchor) == 1, f"{key} {kind}: anchor not unique"
            check(f"{key} {kind} aligns uniquely", True)
            if kind in ("tail", "dropTail", "dropSpan-from"):
                pre = raw[:pos[0]].rstrip()
                marker = "complete-sentence-keep" in (v.get("why") or "")
                check(f"{key} {kind} pre-cut context ends in prose",
                      bool(pre) and (pre[-1] in ".!?\"" or marker),
                      f"ends {pre[-20:]!r} (a non-punctuated cut needs the "
                      f"complete-sentence-keep eyeball marker in why)")
    # F125: the part-level live anchor law (raw part problem_md bytes)
    for key, v in sorted(part_keys().items()):
        raw = raw_part(key)[1]
        cuts = []
        if v.get("dropTail"):
            cuts.append(("dropTail", v["dropTail"]))
        if v.get("dropSpan"):
            cuts.append(("dropSpan-from", v["dropSpan"][0]))
            cuts.append(("dropSpan-to", v["dropSpan"][1]))
        for kind, anchor in cuts:
            pos = align(anchor, raw)
            assert pos is not None, f"{key} {kind}: anchor does not align"
            assert raw.count(anchor) == 1, f"{key} {kind}: anchor not unique"
            check(f"{key} {kind} aligns uniquely", True)
            if kind in ("dropTail", "dropSpan-from"):
                pre = raw[:pos[0]].rstrip()
                marker = "complete-sentence-keep" in (v.get("why") or "")
                check(f"{key} {kind} pre-cut context ends in prose",
                      bool(pre) and (pre[-1] in ".!?\"" or marker),
                      f"ends {pre[-20:]!r}")


# ------------------------------------------------- C: restore_group_stem laws
def section_c():
    print("C. restore_group_stem laws (synthetic)")
    led = {"verdicts": {}}
    g = {"group_stem_md": "Intro prose here. Labels 1 2 3"}
    check("mechanical restore cleans and serves",
          ex.restore_group_stem(g, "2099-01", "1C", "9", "a", led, "Part text") ==
          "Intro prose here. Labels 1 2 3")
    check("empty stem -> None",
          ex.restore_group_stem({"group_stem_md": ""}, "2099-01", "1C", "9", "a",
                                led, "") is None)
    check("splice-guard folds -> None",
          ex.restore_group_stem(g, "2099-01", "1C", "9", "a", led,
                                "Intro prose here. Labels 1 2 3 plus part") is None)
    led_cut = {"verdicts": {"2099-01/4CH1-1C:Q9.a": {
        "verdict": "drop-tail", "tail": "Labels 1 2 3", "served_by": "x", "why": "w"}}}
    # the wave-15 trailing-punctuation law strips the final period on cut stems
    check("drop-tail cut applied",
          ex.restore_group_stem(g, "2099-01", "1C", "9", "a", led_cut, "Part text") ==
          "Intro prose here")
    bad = {"verdicts": {"2099-01/4CH1-1C:Q9.a": {
        "verdict": "drop-tail", "tail": "NOT PRESENT", "served_by": "x", "why": "w"}}}
    expect_refuse("drop-tail missing anchor refuses",
                  lambda: ex.restore_group_stem(g, "2099-01", "1C", "9", "a", bad, "t"),
                  "drop-tail anchor not found")
    led_span = {"verdicts": {"2099-01/4CH1-1C:Q9.a": {
        "verdict": "keep", "dropSpan": ["Labels 1 2 3", "END"],
        "served_by": "x", "why": "w"}}}
    expect_refuse("dropSpan unordered anchors refuse",
                  lambda: ex.restore_group_stem(g, "2099-01", "1C", "9", "a",
                                                led_span, "t"),
                  "dropSpan anchors")
    led_rep = {"verdicts": {"2099-01/4CH1-1C:Q9.a": {
        "verdict": "replace", "stemMd": "Authored intro", "served_by": "x", "why": "w"}}}
    check("replace verdict serves the authored stem",
          ex.restore_group_stem(g, "2099-01", "1C", "9", "a", led_rep, "t") ==
          "Authored intro")
    led_fig = {"verdicts": {"2099-01/4CH1-1C:Q9.a": {
        "verdict": "replace", "stemMd": "x {{FIG:5(a)}}", "served_by": "x", "why": "w"}}}
    expect_refuse("FIG placeholders refuse on group stems",
                  lambda: ex.restore_group_stem(g, "2099-01", "1C", "9", "a",
                                                led_fig, "t"),
                  "FIG placeholders")


def section_c125():
    print("C125. apply_part_cut laws (synthetic + the live bytes)")
    # key derivation
    check("8(b)(i) -> Q8.b(i)", ex.part_ledger_key("8", "8(b)(i)") == "Q8.b(i)")
    check("6(a) -> Q6.a", ex.part_ledger_key("6", "6(a)") == "Q6.a")
    check("15(b)(iv) -> Q15.b(iv)", ex.part_ledger_key("15", "15(b)(iv)") == "Q15.b(iv)")
    check("whole-question part -> None", ex.part_ledger_key("3", "3") is None)
    # the of-record cut, on the live corpus bytes
    led = ex.load_stem_ledger()
    entry = led["verdicts"]["2019-06/4CH1-1CR:Q8.b(i)"]
    _, raw, _, _, part = raw_part("2019-06/4CH1-1CR:Q8.b(i)")
    out = ex.apply_part_cut(raw, entry, "2019-06/4CH1-1CR:Q8.b(i)")
    check("the F123 residual soup is cut", "Temperature of reaction mixture" not in out)
    check("the cleaned text ends at the printed prose",
          out.endswith("Make sure that the two lines cross"))
    check("the of-record trailing-punctuation law holds on part cuts",
          not out.endswith("."))
    bad = dict(entry)
    bad["dropTail"] = "NOT PRESENT"
    expect_refuse("part dropTail missing anchor refuses",
                  lambda: ex.apply_part_cut(raw, bad, "k"),
                  "dropTail anchor not found")
    bad_span = dict(entry)
    bad_span.pop("dropTail", None)
    bad_span["dropSpan"] = ["NOT PRESENT", "ALSO NOT"]
    expect_refuse("part dropSpan unordered anchors refuse",
                  lambda: ex.apply_part_cut(raw, bad_span, "k"),
                  "dropSpan anchors")


# ------------------------------------------------- D: G-E7 negative controls
def synth_lane():
    """One synthetic slice (2099-01/1C Q9 groups a/b) + served set shape."""
    topic = {
        "questions": [{
            "question_number": 9, "total_marks": 4,
            "stem_md": "",
            "groups": {
                "a": {"group_stem_md": "Group intro alpha with table soup 1 2 3"},
                "b": {"group_stem_md": "Group intro beta"},
            },
            "parts": [
                {"part_number": "9(a)(i)", "marks": 2, "problem_md": "Alpha asks. Soup 1 2 3",
                 "solution_md": None, "mark_points": [], "choices": None,
                 "assets": [{"id": "ax", "kind": "crop"}], "spec_point_codes": []},
                {"part_number": "9(b)(i)", "marks": 2, "problem_md": "Beta asks.",
                 "solution_md": None, "mark_points": [], "choices": None,
                 "assets": [], "spec_point_codes": []},
            ],
        }],
    }
    q = topic["questions"][0]
    parts = []
    for p in q["parts"]:
        # compose the served problemMd the way the exporter would (group stem
        # prepended on the group's first part; the F125 part-level cut applied
        # when its ledger entry is in play)
        letter = ex.group_letter_of(p["part_number"])
        head = q["groups"][letter]["group_stem_md"]
        body = p["problem_md"].replace(" Soup 1 2 3", "")
        parts.append({
            "id": f"offp_2099-01_1c_{ex.part_slug(p['part_number'])}",
            "order": len(parts), "marks": p["marks"],
            "problemMd": head + "\n\n" + body,
            "markPoints": [], "assets": [], "choices": None,
        })
    served = {"slug": "official-4ch1-1c-2099-01",
              "questions": [{"id": "offq_2099-01_1c_9", "parts": parts}]}
    return topic, served


def section_d():
    print("D. G-E7 negative controls (synthetic lane)")
    topic, served = synth_lane()
    led = {"verdicts": {}}
    topics_src = lambda s, p: topic  # noqa: E731
    # pin the lane to the synthetic slice for the unit runs (restored after)
    real = (ex.PAPERS, ex.PAPER_SERIES)
    ex.PAPERS = ("1C",)
    ex.PAPER_SERIES = {"1C": ["2099-01"]}
    try:
        stats = ex.g_e7_group_stem_law([served], topics_src, led)
        check("happy path: 2 groups accounted", stats["groups"] == 2, str(stats))
        check("happy path: 2 served", stats["served"] == 2, str(stats))
        # served set MISSING the group stem on the group-first part
        broken = json.loads(json.dumps(served))
        broken["questions"][0]["parts"][0]["problemMd"] = "Alpha asks."
        expect_refuse("missing group stem refuses",
                      lambda: ex.g_e7_group_stem_law([broken], topics_src, led),
                      "not served on the group's first part")
        # group stem attached to the WRONG part
        wrong = json.loads(json.dumps(served))
        wrong["questions"][0]["parts"][0]["problemMd"] = "Alpha asks."
        wrong["questions"][0]["parts"][1]["problemMd"] = \
            "Group intro beta Beta asks."
        expect_refuse("mis-attached group stem refuses",
                      lambda: ex.g_e7_group_stem_law([wrong], topics_src, led),
                      "not served on the group's first part")
        # an adjudicated cut that did NOT cut (soup survives)
        led_cut = {"verdicts": {"2099-01/4CH1-1C:Q9.a": {
            "verdict": "drop-tail", "tail": "with table soup 1 2 3",
            "served_by": "x", "why": "w"}}}
        soup = json.loads(json.dumps(served))
        soup["questions"][0]["parts"][0]["problemMd"] = \
            "Group intro alpha with table soup 1 2 3 Alpha asks."
        expect_refuse("surviving cut refuses",
                      lambda: ex.g_e7_group_stem_law([soup], topics_src, led_cut),
                      "was not applied")
        # stale group ledger key (lane-hosted series, no such group)
        led_stale = {"verdicts": {"2099-01/4CH1-1C:Q9.z": {
            "verdict": "drop-tail", "tail": "x", "served_by": "x", "why": "w"}}}
        expect_refuse("stale group ledger key refuses",
                      lambda: ex.g_e7_group_stem_law([served], topics_src, led_stale),
                      "never resolved")
        # foreign-lane group keys are NOT stale for this lane
        led_foreign = {"verdicts": {"2099-01/4PH1-1P:Q9.z": {
            "verdict": "drop-tail", "tail": "x", "served_by": "x", "why": "w"}}}
        stats = ex.g_e7_group_stem_law([served], topics_src, led_foreign)
        check("foreign-lane group keys ignored", stats["groups"] == 2, str(stats))
        # ---- F125: the part-level classes ----
        led_p = {"verdicts": {"2099-01/4CH1-1C:Q9.a(i)": {
            "verdict": "keep", "dropTail": "Soup 1 2 3",
            "served_by": "ax", "why": "w"}}}
        stats = ex.g_e7_group_stem_law([served], topics_src, led_p)
        check("part cut happy path: 1 part cut consumed",
              stats["part_cuts"] == 1, str(stats))
        check("part key consumed slice-scoped", stats["part_keys"] == 1, str(stats))
        raw_served = json.loads(json.dumps(served))
        raw_served["questions"][0]["parts"][0]["problemMd"] = \
            "Group intro alpha with table soup 1 2 3\n\nAlpha asks. Soup 1 2 3"
        expect_refuse("surviving PART cut refuses",
                      lambda: ex.g_e7_group_stem_law([raw_served], topics_src, led_p),
                      "part cut")
        led_bad_sb = {"verdicts": {"2099-01/4CH1-1C:Q9.a(i)": {
            "verdict": "keep", "dropTail": "Soup 1 2 3",
            "served_by": "nope", "why": "w"}}}
        expect_refuse("part cut served_by not a crop of the part refuses",
                      lambda: ex.g_e7_group_stem_law([served], topics_src, led_bad_sb),
                      "not a crop asset of the part")
        led_stale_p = {"verdicts": {"2099-01/4CH1-1C:Q9.z(9)": {
            "verdict": "keep", "dropTail": "x", "served_by": "ax", "why": "w"}}}
        expect_refuse("stale PART ledger key refuses",
                      lambda: ex.g_e7_group_stem_law([served], topics_src, led_stale_p),
                      "never resolved")
        led_bad_asset = {"verdicts": {"2099-01/4CH1-1C:Q9.a(i)": {
            "verdict": "keep", "dropTail": "Soup 1 2 3",
            "served_by": "ax", "why": "w"}}}
        nocrop = json.loads(json.dumps(topic))
        nocrop["questions"][0]["parts"][0]["assets"] = [{"id": "ax", "kind": "crop-required"}]
        expect_refuse("part cut served_by non-crop kind refuses",
                      lambda: ex.g_e7_group_stem_law(
                          [served], lambda s, p: nocrop, led_bad_asset),
                      "not a crop asset of the part")
    finally:
        ex.PAPERS, ex.PAPER_SERIES = real


# ------------------------------------------------------- E: live census law
def section_e():
    print("E. the live census law (all 54 slices)")
    n_groups = 0
    for series_dir in sorted(CORPUS.iterdir()):
        if not series_dir.is_dir():
            continue
        for slice_dir in sorted(series_dir.iterdir()):
            if not slice_dir.name.startswith("4CH1-"):
                continue
            paper = slice_dir.name.replace("4CH1-", "")
            t = json.load(open(slice_dir / "topic.json"))
            for q in t["questions"]:
                for letter, g in (q.get("groups") or {}).items():
                    gs = (g.get("group_stem_md") or "").strip()
                    if not gs:
                        continue
                    fp = next((p for p in q["parts"]
                               if ex.group_letter_of(p["part_number"]) == letter), None)
                    assert fp is not None, \
                        f"{series_dir.name}/{paper} Q{q['question_number']}({letter})"
                    n_groups += 1
    check("every non-empty group stem resolves to a group-first part "
          "(567 corpus-wide)", n_groups == 567, f"got {n_groups}")


# ------------------------------------------------------- F: print-order pin
def section_f():
    print("F. the print-order pin (2019-06 2C Q5(a)(i))")
    ex.apply_lane("4ch1")
    led = ex.load_stem_ledger()
    t = ex.export_series("2019-06", "2C", stem_ledger=led,
                         enrich=ex.load_enrichment_ledger())
    q5 = next(q for q in t["questions"] if q["id"].endswith("_5"))
    md = q5["parts"][0]["problemMd"]
    i_stem = md.find("During the Second World War")
    i_air = md.find("asset_5_stem_aircraft.png")
    i_group = md.find("The tables give the bond energies")
    i_form = md.find("asset_5_stem_displayed-formulae.png")
    i_tab = md.find("asset_5_stem_bond-tables.png")
    check("stem < aircraft fig < group stem < formulae fig < tables fig",
          0 <= i_stem < i_air < i_group < i_form < i_tab,
          f"{i_stem},{i_air},{i_group},{i_form},{i_tab}")
    check("the bond-table soup is cut",
          "Bonds broken Bonds made" not in md)
    check("the group stem head is served",
          "The tables give the bond energies for the bonds broken" in md)
    # and the dropSpan case
    t2 = ex.export_series("2024-11", "1C", stem_ledger=led,
                          enrich=ex.load_enrichment_ledger())
    q5c = next(x for x in t2["questions"] if x["id"].endswith("_5"))
    mdc = next(p for p in q5c["parts"]
               if p["id"] == "offp_2024-11_1c_5-c-i")["problemMd"]
    check("dropSpan apparatus soup cut",
          "hydrogen peroxide solution 0 20 40" not in mdc)
    check("dropSpan join is clean prose",
          "peroxide solution. The student adds 100 cm³" in mdc)
    check("dropTail graph axes cut",
          "100 Volume of oxygen in cm³ 0 4 8" not in mdc)
    # ---- F125: the part-level live pin (2019-06 1CR 8(b)(i)) ----
    t3 = ex.export_series("2019-06", "1CR", stem_ledger=led,
                          enrich=ex.load_enrichment_ledger())
    q8 = next(x for x in t3["questions"] if x["id"].endswith("_8"))
    md8 = next(p for p in q8["parts"]
               if p["id"] == "offp_2019-06_1cr_8-b-i")["problemMd"]
    check("the F123 residual part soup is cut from the served bytes",
          "Temperature of reaction mixture 25" not in md8)
    check("the cleaned part text is served",
          "Make sure that the two lines cross" in md8)
    check("the re-cropped grid figure is served",
          "asset_8_b_i_grid.png" in md8)
    check("the group stem head is still served on the part",
          "The table shows the student" in md8)


def main():
    print(f"F121 group-stem battery — converter under test: "
          f"official_examq_export_hub.py (repo {RES})")
    section_a()
    section_b()
    section_c()
    section_c125()
    section_d()
    section_e()
    section_f()
    print(f"\nF121 battery: {_checks['pass']}/{_checks['n']} PASS")
    if _checks["pass"] != _checks["n"]:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
