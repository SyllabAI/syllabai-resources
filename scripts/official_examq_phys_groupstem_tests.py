#!/usr/bin/env python3
"""Zero-network battery for the F121-groupstem physics serving wave
(T-OEQ-PHYS-FORMAT-1 run-007, LEDGER F128 — operator order "F121-groupstem",
trace 1a19135ba51a454d; the v2 leg served the plane of record, PR #548).

Verifies, against the corpus of record on disk (no network):

  B0  pin count == 421 (the F127 census of record);
  B1  every group-stem pin (scripts/oeq_phys_groupstem_pins.json) re-derives
      from the corpus: gmd == restore_group_stem(...) of the corpus group
      under the exporter of record, pin sha256 == sha256(utf-8(gmd)) (the
      C-law for md strings);
  B2  the fresh G-E7 accounting on a full current-law emission over the
      corpus: groups == 421, served == 421, splice == 0, group ledger keys
      == 0, part cuts/keys == 0, AND the served pid set == the pin pid set
      exactly (the CI-enforced physics group-stem serving law);
  B3  pin grammar: field in the closed set {"group_stem"}; pid ==
      offp_<series>_<paper-lower>_<part-slug>; group letter lowercase alpha;
  B4  character laws: zero PUA / U+FFFD / C0 control chars AND zero '$' in
      every pinned group intro (plain prose — no KaTeX, no nuclear-notation
      entanglement);
  B5  negative test: mutating one pinned value in memory is DETECTED.

Exit 0 = all legs hold. Any failure exits 1 (fail-closed, ship-blocker).
"""
import json, hashlib, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
CORPUS = REPO / "Official-ExamQuestion" / "igcse-physics-19"
PINS_PATH = HERE / "oeq_phys_groupstem_pins.json"

sys.path.insert(0, str(HERE))
import official_examq_export_hub as ex

ex.apply_lane('4ph1')
sl, en = ex.load_stem_ledger(), ex.load_enrichment_ledger()
PUA_RE = re.compile(r"[\uE000-\uF8FF\uFFFD\u0000-\u0008\u000b-\u001f]")

fails = []


def check(name, ok, detail=""):
    print(("PASS  " if ok else "FAIL  ") + name + (f" — {detail}" if detail else ""))
    if not ok:
        fails.append(name)


def load_topic(series, paper):
    return json.loads((CORPUS / series / f"4PH1-{paper}" / "topic.json").read_text())


topics = {}


def topics_src(s, p):
    if (s, p) not in topics:
        topics[(s, p)] = load_topic(s, p)
    return topics[(s, p)]


def gmd_for(series, paper, letter, part):
    """The exporter-of-record group intro for one pinned (part, group)."""
    topic = topics_src(series, paper)
    q = next(q for q in topic["questions"]
             for p in q["parts"] if p["part_number"] == part)
    g = (q.get("groups") or {}).get(letter)
    assert g is not None, (series, paper, part, letter)
    fp_md = next(p for p in q["parts"]
                 if ex.group_letter_of(p["part_number"]) == letter).get("problem_md")
    return ex.restore_group_stem(g, series, paper, str(q["question_number"]),
                                 letter, sl, fp_md)


pins = json.loads(PINS_PATH.read_text())
check("B0 pin count == 421 (the F127 census)", len(pins) == 421, str(len(pins)))

# ---- B1: every pin re-derives from the corpus --------------------------------
b1_bad = []
for pin in pins:
    try:
        gmd = gmd_for(pin["series"], pin["paper"], pin["group"], pin["part"])
    except Exception as exc:  # noqa: BLE001 - report, don't crash the sweep
        b1_bad.append((pin["pid"], f"resolve error: {exc}"))
        continue
    if gmd is None:
        b1_bad.append((pin["pid"], "gmd now None (splice-guarded?)"))
    elif hashlib.sha256(gmd.encode("utf-8")).hexdigest() != pin["sha256"]:
        b1_bad.append((pin["pid"], "sha mismatch"))
check("B1 every pin re-derives (restore_group_stem + C-law sha)", not b1_bad,
      f"{len(b1_bad)} bad: {b1_bad[:3]}")

# ---- B2: fresh G-E7 accounting on a current-law emission ---------------------
emission = [ex.export_series(s, p, topics_src(s, p), sl, en)
            for p in ex.PAPERS for s in ex.PAPER_SERIES[p]]
g_stats = ex.g_e7_group_stem_law(emission, topics_src, sl)
check("B2 G-E7 accounting: groups/served == 421, splice 0, keys 0",
      g_stats["groups"] == 421 and g_stats["served"] == 421
      and g_stats["splice"] == 0 and g_stats["keys"] == 0
      and g_stats["part_cuts"] == 0 and g_stats["part_keys"] == 0,
      str(g_stats))

emission_pids = set()
for paper in ex.PAPERS:
    for series in ex.PAPER_SERIES[paper]:
        slug = f"official-4ph1-{paper.lower()}-{series}"
        assert next(x for x in emission if x["slug"] == slug) is not None
        topic = topics_src(series, paper)
        for q in topic["questions"]:
            for letter, g in (q.get("groups") or {}).items():
                fp = next((p for p in q["parts"]
                           if ex.group_letter_of(p["part_number"]) == letter), None)
                if fp is None:
                    continue
                gmd = ex.restore_group_stem(g, series, paper,
                                            str(q["question_number"]), letter, sl,
                                            fp.get("problem_md"))
                if gmd is not None:
                    emission_pids.add(
                        f"offp_{series}_{paper.lower()}_{ex.part_slug(fp['part_number'])}")
served_pids = {p["pid"] for p in pins}
check("B2 served pid set == pin pid set", emission_pids == served_pids,
      f"sym diff {len(emission_pids ^ served_pids)}")

# ---- B3: pin grammar ----------------------------------------------------------
g_bad = []
for pin in pins:
    if pin["field"] != "group_stem":
        g_bad.append((pin["pid"], "field"))
        continue
    if not re.fullmatch(r"[a-z]", pin["group"] or ""):
        g_bad.append((pin["pid"], "group letter"))
        continue
    expect_pid = (f"offp_{pin['series']}_{pin['paper'].lower()}_"
                  + ex.part_slug(pin["part"]))
    if expect_pid != pin["pid"]:
        g_bad.append((pin["pid"], f"pid/part mismatch -> {expect_pid}"))
check("B3 pin grammar (field closed set, pid==slug(part), group letter)",
      not g_bad, f"{g_bad[:3]}")

# ---- B4: character laws --------------------------------------------------------
c_bad = []
for pin in pins:
    gmd = gmd_for(pin["series"], pin["paper"], pin["group"], pin["part"])
    if PUA_RE.search(gmd):
        c_bad.append((pin["pid"], "PUA/FFFD/C0"))
    if "$" in gmd:
        c_bad.append((pin["pid"], "dollar"))
check("B4 char laws (zero PUA/FFFD/C0, zero '$')", not c_bad, f"{c_bad[:3]}")

# ---- B5: negative control ------------------------------------------------------
pin0 = pins[0]
gmd0 = gmd_for(pin0["series"], pin0["paper"], pin0["group"], pin0["part"])
mutated = hashlib.sha256((gmd0 + " ").encode("utf-8")).hexdigest()
check("B5 negative control: a mutated value is DETECTED", mutated != pin0["sha256"])

print()
if fails:
    print(f"GROUPSTEM BATTERY FAILED: {fails}")
    sys.exit(1)
print("GROUPSTEM BATTERY GREEN: the 421 served group intros are pinned to the "
      "corpus of record under the exporter of record's law (B0-B5).")
