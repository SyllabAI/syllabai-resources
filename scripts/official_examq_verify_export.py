#!/usr/bin/env python3
"""
official_examq_verify_export.py — F-187 verification harness for the ADR-037
exporter of record (scripts/official_examq_export_hub.py — the #31 provenance
exporter as evolved on main: v0.10.0 topics-dir interface, F44 per-paper
topicSlug namespace + G-E1b identity closure, wave-14 disclosed-delta state).

Provenance law (F-187): the evolved #31 provenance exporter is the of record;
this harness is ADDITIVE verification only. It never rewrites the exporter
and never imports it — it verifies ARTIFACTS on disk:

    the staged export output  vs  the bundle of record being extended.

Gates (all fail closed; a gate that cannot prove success is a failure):

  G-E1  bundle-of-record parity. Every official set in the staged output must
        match the of-record set for the same slug — deep-equal, or differing
        ONLY in the disclosed v0.8.1-parity classes (assets, solutionMd,
        markPoints, answerStatus, problemMd, specPointCodes — the classes the
        of-record palimpsest may honestly drift in). The official set LATTICE
        (slug list + order) must match the of record exactly; missing, extra
        or reordered official sets refuse (pass --allow-new-official only when
        a wave legitimately appends new paper variants, e.g. 1CR/2CR).
        With --disclosure <exporter-disclosures/*.json>, the harness's OWN
        delta census (new/gone/changed part ids per slug — the exporter's
        G-E1 census shape) must equal the disclosure of record EXACTLY:
        disclosed-class drift outside the filed census refuses. The harness
        never appends new/gone parts (part lattice is strict — a part-append
        wave needs a harness revision in the same PR).
  G-E2  mark law. Per question: sum(parts.marks) == totalMarks. Per part with
        markPoints: sum(markPoints.marks) == marks. specPointCodes: list of
        strings. marks: non-negative ints. No exceptions are documented right
        now (the 2019-06 archive damage was repaired — see EXPECTED_MARK_GAPS).
  G-E3  census law. Per (series, paper): (questions, parts, marks) equals the
        frozen constants below (the MULTI-SERIES-REPORT of record, converter
        v0.10.0 / 2026-10-22 — the F41/F42 2019-06 re-capture wave — cross-
        checked against the 32 topic.json files on resources main and the
        live v2 bundle of record). With --report, the frozen constants must
        ALSO equal the report rows — both are of record; disagreement is a
        hard stop.
  G-E4  SME file byte-identity. The staged questions.json re-serializes
        byte-identically to the bundle of record's questions.json under the
        file law (indent=1, ensure_ascii=False, no trailing newline) — the
        SME corpus of record is never touched by an official-papers export.
        (Two-file law: since the v2 split, IA decision 662654ade0, the SME
        file IS the whole questions.json and official sets verify against
        official-papers.json via G-E1.)

Usage:

    verify:  official_examq_verify_export.py verify --stage <questions.json> \
                 --stage-official-papers <staged official-papers.json> \
                 --current <SME questions.json of record> \
                 --current-official-papers <official-papers.json of record> \
                 [--report <MULTI-SERIES-REPORT.json>] \
                 [--disclosure <scripts/exporter-disclosures/wave.json>] \
                 [--allow-new-official]

    self-test (F-187 acceptance: 4/4 gates refuse on seeded faults):

             official_examq_verify_export.py self-test --stage <clean stage> \
                 --stage-official-papers <clean official-papers stage> \
                 --current <SME bundle of record> \
                 --current-official-papers <official-papers.json of record> \
                 [--keep]

  The self-test seeds four faults into copies of the clean stage (undisclosed
  delta, markPoint bump, dropped question, SME-prefix mutation) and requires
  every seed to be REFUSED with the right gate name. The clean stage must pass
  all four gates first.

Exit codes: 0 = all gates proved; 1 = any gate refused / seed not detected.
"""

import argparse
import json
import os
import sys
import tempfile

OFFICIAL_PREFIX = "official-4ch1-"
# Task 22 hub-export wave: the lane registry (--spec; default 4ch1 byte-identical).
# The physics frozen census of record: igcse-physics-19/MULTI-SERIES-REPORT.json
# @ converter v0.25.0 - (questions, parts, sum(parts.marks), sum(question
# totalMarks)) per slice; both mark layers agree on all 55 sets (the footer law).
_LANES = {
    "4ch1": dict(prefix="official-4ch1-"),
    "4ph1": dict(prefix="official-4ph1-"),
}
LANE_SPEC = "4ch1"
_PH_EXPECTED_CENSUS_V = {
    ("2019-06", "1P"): (12, 47, 110, 110),
    ("2019-06", "1PR"): (11, 54, 110, 110),
    ("2019-06", "2P"): (9, 31, 70, 70),
    ("2019-06", "2PR"): (8, 34, 70, 70),
    ("2020-01", "1P"): (12, 50, 110, 110),
    ("2020-01", "1PR"): (12, 52, 110, 110),
    ("2020-01", "2P"): (8, 31, 70, 70),
    ("2020-01", "2PR"): (8, 33, 70, 70),
    ("2020-06", "1P"): (11, 42, 110, 110),
    ("2020-06", "1PR"): (13, 53, 110, 110),
    ("2020-06", "2P"): (8, 35, 70, 70),
    ("2020-06", "2PR"): (8, 36, 70, 70),
    ("2020-11", "1P"): (11, 42, 110, 110),
    ("2021-01", "1P"): (11, 50, 110, 110),
    ("2021-01", "1PR"): (12, 47, 110, 110),
    ("2021-01", "2P"): (8, 37, 70, 70),
    ("2021-01", "2PR"): (8, 33, 70, 70),
    ("2021-06", "1P"): (11, 48, 110, 110),
    ("2021-06", "2P"): (7, 32, 70, 70),
    ("2021-11", "1P"): (12, 53, 110, 110),
    ("2021-11", "2P"): (8, 37, 70, 70),
    ("2022-01", "1P"): (12, 55, 110, 110),
    ("2022-01", "1PR"): (12, 49, 110, 110),
    ("2022-01", "2P"): (9, 31, 70, 70),
    ("2022-01", "2PR"): (8, 30, 70, 70),
    ("2022-06", "1P"): (12, 59, 110, 110),
    ("2022-06", "1PR"): (12, 49, 110, 110),
    ("2022-06", "2P"): (7, 31, 70, 70),
    ("2022-06", "2PR"): (7, 30, 70, 70),
    ("2023-01", "1P"): (11, 50, 110, 110),
    ("2023-01", "1PR"): (11, 55, 110, 110),
    ("2023-01", "2P"): (8, 28, 70, 70),
    ("2023-01", "2PR"): (8, 34, 70, 70),
    ("2023-06", "1P"): (12, 45, 110, 110),
    ("2023-06", "1PR"): (11, 46, 110, 110),
    ("2023-06", "2P"): (8, 36, 70, 70),
    ("2023-06", "2PR"): (8, 30, 70, 70),
    ("2023-11", "1P"): (12, 49, 110, 110),
    ("2023-11", "2P"): (8, 29, 70, 70),
    ("2024-06", "1P"): (12, 51, 110, 110),
    ("2024-06", "1PR"): (12, 50, 110, 110),
    ("2024-06", "2P"): (8, 33, 70, 70),
    ("2024-06", "2PR"): (9, 30, 70, 70),
    ("2024-11", "1P"): (11, 53, 110, 110),
    ("2024-11", "2P"): (8, 35, 70, 70),
    ("2025-06", "1P"): (11, 49, 110, 110),
    ("2025-06", "1PR"): (11, 43, 110, 110),
    ("2025-06", "2P"): (8, 32, 70, 70),
    ("2025-06", "2PR"): (8, 31, 70, 70),
    ("2025-11", "1P"): (12, 50, 110, 110),
    ("2025-11", "2P"): (8, 36, 70, 70),
    ("2026-06", "1P"): (11, 46, 110, 110),
    ("2026-06", "1PR"): (11, 47, 110, 110),
    ("2026-06", "2P"): (8, 27, 70, 70),
    ("2026-06", "2PR"): (8, 28, 70, 70),
}


def apply_lane(spec):
    global OFFICIAL_PREFIX, EXPECTED_CENSUS, LANE_SPEC
    LANE_SPEC = spec
    if spec == "4ph1":
        OFFICIAL_PREFIX = _LANES["4ph1"]["prefix"]
        EXPECTED_CENSUS = dict(_PH_EXPECTED_CENSUS_V)
    else:
        OFFICIAL_PREFIX = _LANES["4ch1"]["prefix"]
        EXPECTED_CENSUS = dict(_CHEM_EXPECTED_CENSUS)
# The v0.8.1-parity classes (F-187 G-E1): where the of-record bundle may
# honestly differ from a fresh regeneration. Anything else refuses.
# wave-22 (F62): "choices" joins — the 2020-01 2CR 1(b)(i) MCQ re-key is the
# first wave to change a keyed choice (is_correct flips through the
# paper-scoped MCQ-KEYS.json adjudication; converter 0.14.1). The class is
# disclosed the same way as every other class: the exporter census and this
# harness both count it, and anything outside the set still refuses.
DISCLOSED_DELTA_CLASSES = {
    "assets", "solutionMd", "markPoints", "answerStatus", "problemMd", "specPointCodes",
    "choices",
    # F119 (T-OEQ-PARTLABEL-3): the printed part label is a first-class serving
    # field — sourcePaper.questionPart is emitted by the exporter of record
    # (printed_part_label + the G-E6 label-identity gate) and the maths-B plane
    # carries it via the disclosed field-write; delta classes of record learned
    # the field in the same reviewed wave that introduced it.
    "sourcePaper",
}
# Frozen per-series census of record (converter v0.10.0, MULTI-SERIES-REPORT
# regenerated by the F41/F42 2019-06 re-capture wave; cross-checked against
# the 32 topic.json files on resources main and the live v2 bundle of record —
# the F44 exporter of record reproduces that bundle with the wave-14 disclosed
# census only).
# (questions, parts, sum(parts.marks), sum(question totalMarks)) — the two mark
# layers are pinned separately and AGREE on all 32 sets as of v0.10.0.
_CHEM_EXPECTED_CENSUS = {
    ("2019-06", "1C"): (15, 64, 110, 110),  # 2019-06 damage REPAIRED by v0.10.0 (was 14,53,90,104)
    ("2020-01", "1C"): (10, 60, 110, 110),
    ("2020-11", "1C"): (10, 64, 110, 110),
    ("2021-01", "1C"): (11, 53, 110, 110),
    ("2021-06", "1C"): (10, 54, 110, 110),
    ("2021-11", "1C"): (11, 67, 110, 110),
    ("2022-01", "1C"): (11, 65, 110, 110),
    ("2022-06", "1C"): (10, 57, 110, 110),
    ("2023-01", "1C"): (12, 60, 110, 110),
    ("2023-06", "1C"): (10, 55, 110, 110),
    ("2023-11", "1C"): (10, 66, 110, 110),
    ("2024-06", "1C"): (10, 56, 110, 110),
    ("2024-11", "1C"): (11, 56, 110, 110),
    ("2025-06", "1C"): (10, 49, 110, 110),
    ("2025-11", "1C"): (10, 59, 110, 110),
    ("2026-06", "1C"): (9, 56, 110, 110),
    ("2019-06", "2C"): (8, 39, 70, 70),
    ("2020-01", "2C"): (7, 39, 70, 70),
    ("2020-11", "2C"): (7, 35, 70, 70),
    ("2021-01", "2C"): (7, 39, 70, 70),
    ("2021-06", "2C"): (7, 43, 70, 70),
    ("2021-11", "2C"): (7, 41, 70, 70),
    ("2022-01", "2C"): (7, 41, 70, 70),
    ("2022-06", "2C"): (7, 39, 70, 70),
    ("2023-01", "2C"): (7, 37, 70, 70),
    ("2023-06", "2C"): (7, 41, 70, 70),
    ("2023-11", "2C"): (7, 37, 70, 70),
    ("2024-06", "2C"): (7, 37, 70, 70),
    ("2024-11", "2C"): (7, 34, 70, 70),
    ("2025-06", "2C"): (6, 38, 70, 70),
    ("2025-11", "2C"): (6, 31, 70, 70),
    ("2026-06", "2C"): (6, 36, 70, 70),
    # 1CR tranche (converter v0.12.0 corpus, trace 1a162ea420f90a75): 11 sets,
    # each carrying its printed 110/110 across both mark layers. The series set
    # is exactly the F-178 footer-verified 1CR schedule (tracker PR #32).
    ("2019-06", "1CR"): (10, 55, 110, 110),
    ("2020-01", "1CR"): (11, 59, 110, 110),
    ("2020-11", "1CR"): (10, 63, 110, 110),
    ("2021-01", "1CR"): (10, 58, 110, 110),
    ("2022-01", "1CR"): (11, 59, 110, 110),
    ("2022-06", "1CR"): (11, 57, 110, 110),
    ("2023-01", "1CR"): (10, 57, 110, 110),
    ("2023-06", "1CR"): (11, 59, 110, 110),
    ("2024-06", "1CR"): (12, 57, 110, 110),
    ("2025-06", "1CR"): (11, 55, 110, 110),
    ("2026-06", "1CR"): (11, 57, 110, 110),
    # 2CR tranche (converter v0.13.0 corpus, trace 1a16373bc7d373fd): 11 sets,
    # each carrying its printed 70/70 across both mark layers. The series set
    # is exactly the F-178 footer-verified 2CR schedule (tracker PR #32).
    ("2019-06", "2CR"): (7, 40, 70, 70),
    ("2020-01", "2CR"): (7, 38, 70, 70),
    ("2020-11", "2CR"): (7, 36, 70, 70),
    ("2021-01", "2CR"): (8, 45, 70, 70),
    ("2022-01", "2CR"): (7, 35, 70, 70),
    ("2022-06", "2CR"): (7, 40, 70, 70),
    ("2023-01", "2CR"): (8, 40, 70, 70),
    ("2023-06", "2CR"): (7, 38, 70, 70),
    ("2024-06", "2CR"): (7, 38, 70, 70),
    ("2025-06", "2CR"): (7, 38, 70, 70),
    ("2026-06", "2CR"): (7, 35, 70, 70),
}

# Documented archive damage of record (G-E2 exceptions) — currently EMPTY.
# History: 2019-06 1C lost five rasterized content pages (ADR-037 honest REVIEW
# state, 104/110 marks; per-question part-sum gaps 3+6+2+3 = 14 on
# offq_2019-06_{1,11,12,15}, verified at the #263 post-merge review). That
# damage was REPAIRED by converter v0.10.0's F41 OCR re-capture (wave of
# record: 2019-06 G1 110/110 PASS, 15 new/renumbered parts; v2 bundle of
# record re-synced and now carrying the wave-14 disclosed-delta state). The
# mark law is therefore STRICT on all 32 sets as of this harness revision.
# If a future archive defect reintroduces a gap: re-eyeball the source pages
# FIRST, then re-record it here AND in the review queue of record — never
# extend this table from exporter output alone.
EXPECTED_MARK_GAPS = {}



class GateRefusal(Exception):
    def __init__(self, gate, reason):
        super().__init__(f"{gate}: {reason}")
        self.gate = gate
        self.reason = reason


def parse_slug(slug):
    # official-4ch1-<paper-lower>-<series>  (series = YYYY-MM — itself hyphenated)
    if not slug.startswith(OFFICIAL_PREFIX):
        return None
    rest = slug[len(OFFICIAL_PREFIX):]
    parts = rest.rsplit("-", 2)
    if len(parts) != 3:
        return None
    paper, year, month = parts
    return f"{year}-{month}", paper.upper()  # (series, paper) — the table key convention


def set_census(s):
    nq = len(s["questions"])
    nps = sum(len(q["parts"]) for q in s["questions"])
    pm = sum(p["marks"] for q in s["questions"] for p in q["parts"])
    qt = sum(q["totalMarks"] for q in s["questions"])
    return nq, nps, pm, qt


def by_slug(sets):
    return {s.get("slug"): s for s in sets}


# ---------------------------------------------------------------- G-E1
def gate_e1(stage_sets, current_sets, allow_new_official=False, renames=None):
    """renames (wave-15): an id-identity wave discloses, PER SLUG,
    {"<slug>": {"questions": {old: new}, "parts": {old: new}}} — the stage
    lattice is walked through the rename map, so drift beyond the disclosed
    renames (order, count, unrenamed ids) still refuses. Per-slug because the
    old scheme's cross-paper collisions mean one old id can map to different
    new ids in different sets. Content deltas are then keyed by the NEW ids
    and must stay inside DISCLOSED_DELTA_CLASSES."""
    st_by, cu_by = by_slug(stage_sets), by_slug(current_sets)
    st_off = [s.get("slug") for s in stage_sets if parse_slug(s.get("slug") or "")]
    cu_off = [s.get("slug") for s in current_sets if parse_slug(s.get("slug") or "")]
    missing = [s for s in cu_off if s not in st_by]
    if missing:
        raise GateRefusal("G-E1", f"official sets missing from the export: {missing}")
    extra = [s for s in st_off if s not in cu_by]
    if extra and not allow_new_official:
        raise GateRefusal(
            "G-E1",
            f"official sets absent from the bundle of record: {extra} "
            f"(re-run with --allow-new-official only for a legitimate append wave)")
    if [s for s in st_off if s in cu_by] != [s for s in cu_off if s in st_by]:
        raise GateRefusal("G-E1", "official set ORDER differs from the bundle of record")
    delta_rows = []
    new_rows = []
    for slug in st_off:
        if slug not in cu_by:
            # reachable only under --allow-new-official (the lattice check above
            # refuses extras otherwise): an append wave's new sets disclose their
            # full part lattice in the 'new' census class
            st_s = st_by[slug]
            new_rows.append((slug, sorted(p["id"] for q in st_s["questions"] for p in q["parts"])))
            continue
        st_s, cu_s = st_by[slug], cu_by[slug]
        keys_changed = {k for k in set(st_s) | set(cu_s)
                        if json.dumps(st_s.get(k), sort_keys=True) != json.dumps(cu_s.get(k), sort_keys=True)}
        content_keys = keys_changed - {"questions"}
        if content_keys:
            raise GateRefusal("G-E1", f"{slug}: set-level fields changed: {sorted(content_keys)}")
        slug_ren = (renames or {}).get(slug, {})
        qren = slug_ren.get("questions", {})
        pren = slug_ren.get("parts", {})
        # current lattice (old ids) walked forward through the rename map
        # must equal the stage lattice (new ids) — position-for-position
        cu_q_ids = [qren.get(q["id"], q["id"]) for q in cu_s["questions"]]
        if cu_q_ids != [q["id"] for q in st_s["questions"]]:
            raise GateRefusal("G-E1", f"{slug}: question lattice/order drift "
                              f"(renames disclose {len(qren)} question ids)")
        for st_q, cu_q in zip(st_s["questions"], cu_s["questions"]):
            cu_p_ids = [pren.get(p["id"], p["id"]) for p in cu_q["parts"]]
            if cu_p_ids != [p["id"] for p in st_q["parts"]]:
                raise GateRefusal("G-E1", f"{slug} {st_q['id']}: part lattice/order drift")
            for st_p, cu_p in zip(st_q["parts"], cu_q["parts"]):
                new_pid = pren.get(st_p["id"], st_p["id"])
                changed = {k for k in (set(st_p) | set(cu_p)) - {"id"}
                           if json.dumps(st_p.get(k), sort_keys=True) != json.dumps(cu_p.get(k), sort_keys=True)}
                if changed and not changed <= DISCLOSED_DELTA_CLASSES:
                    raise GateRefusal(
                        "G-E1",
                        f"UNDISCLOSED DELTA {slug} {new_pid}: {sorted(changed)} "
                        f"(disclosed classes only: {sorted(DISCLOSED_DELTA_CLASSES)})")
                if changed:
                    delta_rows.append((slug, new_pid, sorted(changed)))
    return delta_rows, new_rows


# ---------------------------------------------------------------- G-E2
def gate_e2(official_sets):
    checked, damage_ok = 0, 0
    for s in official_sets:
        key = parse_slug(s["slug"])
        documented = EXPECTED_MARK_GAPS.get(key, {})
        for q in s["questions"]:
            parts = q["parts"]
            psum = sum(p["marks"] for p in parts)
            if psum != q["totalMarks"]:
                gap = q["totalMarks"] - psum
                if documented.get(q["id"]) == gap:
                    damage_ok += 1
                    continue
                raise GateRefusal(
                    "G-E2",
                    f"{s['slug']} {q['id']}: sum(parts.marks) {psum} != totalMarks "
                    f"{q['totalMarks']} (gap {gap}) — not in the documented damage "
                    f"table ({sorted(documented)} for {key}); archive damage must be "
                    f"re-eyeballed and recorded before this table changes")
            for p in parts:
                m = p["marks"]
                if not isinstance(m, int) or isinstance(m, bool) or m < 0:
                    raise GateRefusal("G-E2", f"{s['slug']} {p['id']}: marks not a non-negative int: {m!r}")
                mp = p.get("markPoints") or []
                if mp:
                    ms = sum(x["marks"] for x in mp)
                    if ms != m:
                        raise GateRefusal("G-E2",
                                          f"{s['slug']} {p['id']}: markPoints sum {ms} != marks {m}")
                codes = p.get("specPointCodes")
                if not isinstance(codes, list) or not all(isinstance(c, str) for c in codes):
                    raise GateRefusal("G-E2", f"{s['slug']} {p['id']}: specPointCodes not a list of strings")
                checked += 1
    return checked, damage_ok


# ---------------------------------------------------------------- G-E3
def gate_e3(official_sets, report_path=None):
    seen = {}
    for s in official_sets:
        key = parse_slug(s["slug"])
        seen[key] = set_census(s)
    for key, census in sorted(seen.items()):
        exp = EXPECTED_CENSUS.get(key)
        if exp is None:
            raise GateRefusal("G-E3",
                              f"{key}: no frozen census constant (update EXPECTED_CENSUS with the "
                              f"MULTI-SERIES-REPORT of record when a new paper variant lands)")
        if census != exp:
            raise GateRefusal("G-E3", f"{key}: exported census {census} != frozen {exp}")
    if report_path:
        rep = json.load(open(report_path))
        # Task 22: the report key is the lane's own marks column name — chemistry
        # reports carry marks_total; the physics report of record (Task 22 regen)
        # carries marks. Parsed-level the two are the same G1-measurable layer.
        def _rmarks(e):
            return e.get("marks_total", e.get("marks"))
        rows = {(e["series"], e["paper"]): (e["questions"], e["parts"], _rmarks(e))
                for e in rep["series"]}
        for key, exp in sorted(EXPECTED_CENSUS.items()):
            if key in rows:
                r = rows[key]
                # the report's marks_total is the G1 measurable question-total layer
                if (r[0], r[1], r[2]) != (exp[0], exp[1], exp[3]):
                    raise GateRefusal("G-E3",
                                      f"{key}: frozen constant {exp} != report of record {r} "
                                      f"(--report {report_path}); both are of record and must agree")
    unmapped = 0
    for s in official_sets:
        for q in s["questions"]:
            if all(len(p.get("specPointCodes") or []) == 0 for p in q["parts"]):
                unmapped += 1
    return len(seen), unmapped


# ---------------------------------------------------------------- G-E4
def gate_e4(stage_raw, current_raw):
    # Two-file law (v2 IA 662654ade0): the staged questions.json must be a
    # byte-identical passthrough of the SME bundle of record — the whole file,
    # since the split made the SME file the whole questions.json. The official
    # plane's parity is G-E1's law (its bytes may drift in a disclosed wave).
    if stage_raw != current_raw:
        n = min(len(stage_raw), len(current_raw))
        for i in range(n):
            if stage_raw[i] != current_raw[i]:
                raise GateRefusal(
                    "G-E4",
                    f"SME file diverges at byte {i}: "
                    f"{current_raw[max(0, i - 60):i + 60]!r} vs "
                    f"{stage_raw[max(0, i - 60):i + 60]!r}")
        raise GateRefusal("G-E4",
                          f"SME file length drift: of record {len(current_raw)} bytes "
                          f"vs export {len(stage_raw)} bytes")
    return len(current_raw)


# ---------------------------------------------------------------- driver
def check_disclosure(delta_rows, new_rows, disclosure_path, stage_eq_current=False):
    """G-E1 closure: the harness's own census must equal the disclosure of
    record (the exporter's --expected-deltas shape: new/gone/changed part ids
    per slug). The harness lattice is strict, so 'gone' is always empty here
    and 'changed' covers only common sets; 'new' names the append wave's sets
    with their full part lattices (the harness revision the F-187 protocol
    filed for set-append waves — a part-append WITHIN a common set still
    refuses at the lattice check)."""
    flat = {"new": {}, "gone": {}, "changed": {}}
    for slug, pids in new_rows:
        flat["new"][slug] = list(pids)
    for slug, pid, _classes in delta_rows:
        flat["changed"].setdefault(slug, []).append(pid)
    for slug in flat["changed"]:
        flat["changed"][slug].sort()
    flat["new"] = {k: v for k, v in sorted(flat["new"].items())}
    expected = json.load(open(disclosure_path))
    if "idRenames" in expected:
        # rename-wave shape: the exporter census is new/gone (ids are identity);
        # the harness compares the content census keyed by the NEW ids and the
        # rename map itself is the lattice disclosure (checked in gate_e1)
        exp_changed = {k: sorted(v) for k, v in expected.get("changed", {}).items()}
        mine_changed = {k: sorted(v) for k, v in flat["changed"].items() if flat["changed"][k]}
        if not mine_changed and stage_eq_current and exp_changed:
            # the disclosure's wave is already MATERIALIZED: the staged export is a
            # byte-level no-op vs the bundle of record (the exporter's G-E1 no-op
            # law proves the stage is the honest corpus regeneration), so there
            # are no pending deltas left for the rename walk to find. The lattice
            # still walked the disclosure (gate_e1 above); a doctored stage that
            # merely COPIES the bundle cannot pass anything beyond this — the
            # exporter no-op plus the corpus canaries pin the content.
            print("G-E1 ok: rename disclosure already materialized — staged export is a "
                  "byte-level no-op vs the bundle of record (0 pending deltas; the "
                  f"disclosure's {sum(len(v) for v in exp_changed.values())}-part wave is on record)")
            return 0
        if json.dumps(mine_changed, sort_keys=True) != json.dumps(exp_changed, sort_keys=True):
            mine = sum(len(v) for v in mine_changed.values())
            theirs = sum(len(v) for v in exp_changed.values())
            raise GateRefusal(
                "G-E1",
                f"harness content census ({mine} parts, keyed by renamed ids) != "
                f"disclosure of record ({theirs} parts, {disclosure_path}) — "
                f"regenerate only after eyeballing every class")
        return sum(len(v) for v in flat["changed"].values())
    if json.dumps(flat, sort_keys=True) != json.dumps(expected, sort_keys=True):
        mine = sum(len(v) for d in flat.values() for v in d.values())
        theirs = sum(len(v) for d in expected.values() for v in d.values())
        raise GateRefusal(
            "G-E1",
            f"harness delta census ({mine} parts) != disclosure of record "
            f"({theirs} parts, {disclosure_path}) — disclosed-class drift outside "
            f"the filed census refuses; regenerate the disclosure only after "
            f"eyeballing every class")
    return sum(len(v) for v in flat["changed"].values())


def run_gates(stage_path, stage_official_path, current_path, current_official_path,
              report_path=None, allow_new_official=False, quiet=False,
              disclosure_path=None):
    stage_raw = open(stage_path, "rb").read()
    current_raw = open(current_path, "rb").read()
    stage_official_raw = open(stage_official_path, "rb").read()
    current_official_raw = open(current_official_path, "rb").read()
    stage_sets, current_sets = json.loads(stage_raw), json.loads(current_raw)
    official = [s for s in json.loads(stage_official_raw) if parse_slug(s.get("slug") or "")]
    current_official = [s for s in json.loads(current_official_raw) if parse_slug(s.get("slug") or "")]

    renames = None
    if disclosure_path and os.path.exists(disclosure_path):
        renames = json.load(open(disclosure_path)).get("idRenames")
    rows, new_rows = gate_e1(official, current_official, allow_new_official, renames)
    disclosed_n = (check_disclosure(rows, new_rows, disclosure_path,
                                    stage_eq_current=(stage_official_raw == current_official_raw))
                   if disclosure_path else None)
    n_parts, damage_ok = gate_e2(official)
    n_sets, unmapped = gate_e3(official, report_path)
    prefix_len = gate_e4(stage_raw, current_raw)
    if not quiet:
        print(f"G-E1 ok: official lattice equal; {len(rows)} disclosed-class part deltas"
              + (f" ({sum(len(r[2]) for r in rows)} fields)" if rows else ""))
        if new_rows:
            print(f"G-E1 ok: {len(new_rows)} new official sets accepted under --allow-new-official "
                  f"({sum(len(p) for _, p in new_rows)} parts disclosed as 'new')")
        if disclosed_n is not None:
            print(f"G-E1 ok: census matches the disclosure of record exactly ({disclosed_n} parts)")
        for slug, pid, ch in rows[:12]:
            print(f"    {slug} {pid}: {','.join(ch)}")
        if len(rows) > 12:
            print(f"    ... +{len(rows) - 12} more")
        tot_q = sum(len(s['questions']) for s in official)
        tot_p = sum(len(q['parts']) for s in official for q in s['questions'])
        tot_m = sum(p['marks'] for s in official for q in s['questions'] for p in q['parts'])
        print(f"G-E2 ok: mark law holds on {n_parts} parts across {tot_q} questions"
              + (f" ({damage_ok} documented damage gaps honored)" if damage_ok else ""))
        print(f"G-E3 ok: {n_sets} series/paper census constants match "
              f"(official totals {tot_q}Q/{tot_p}P/{tot_m}M; {unmapped} questions unmapped under the anchor law)")
        print(f"G-E4 ok: questions.json byte-identical passthrough ({prefix_len} bytes)")
    return {"delta_rows": rows, "parts": n_parts, "sets": n_sets, "prefix": prefix_len}


def self_test(stage_path, stage_official_path, current_path, current_official_path,
              keep=False, allow_new_official=False, disclosure_path=None):
    """disclosure_path: for a rename-wave stage the clean baseline itself needs
    the id-rename disclosure to pass; faults are then seeded on top of it."""
    stage_sets = json.load(open(stage_path))
    stage_official_sets = json.load(open(stage_official_path))
    current_sets = json.load(open(current_path))
    current_official_sets = json.load(open(current_official_path))
    official = [s for s in stage_official_sets if parse_slug(s.get("slug") or "")]
    # seed targets: one part with markPoints, one non-disclosed field, one series set, one SME set
    mp_part = next(p for s in official for q in s["questions"] for p in q["parts"]
                   if p.get("markPoints"))
    type_part = next(p for s in official for q in s["questions"] for p in q["parts"])
    seed_set = official[0]
    sme_slug = next(s["slug"] for s in stage_sets if not parse_slug(s.get("slug") or ""))

    def reserialize(sets):
        return (json.dumps(sets, indent=1, ensure_ascii=False)).encode()

    workdir = tempfile.mkdtemp(prefix="examq-verify-selftest-")
    # each seed: (gate, description, stage_sme, stage_official, cur_sme, cur_official)
    # — most seeds touch only the staged official file; seed 3 mutates BOTH
    # official files consistently, the collusive-drift threat that only the
    # frozen census (G-E3) can catch; seed 4 touches the staged SME file.
    seeds = []

    # Seed 1 / G-E1: an UNDISCLOSED field (questionType) drifts in one official part
    s1 = json.loads(json.dumps(stage_official_sets))
    for s in s1:
        for q in s["questions"]:
            for p in q["parts"]:
                if p["id"] == type_part["id"]:
                    p["questionType"] = "seed_fault_undefined_type"
    seeds.append(("G-E1", "undisclosed class: questionType mutated on " + type_part["id"],
                  stage_sets, s1, current_sets, current_official_sets))

    # Seed 2 / G-E2: a markPoint award exceeds the part's marks (closure broken)
    s2 = json.loads(json.dumps(stage_official_sets))
    for s in s2:
        for q in s["questions"]:
            for p in q["parts"]:
                if p["id"] == mp_part["id"]:
                    p["markPoints"][0]["marks"] += 1
    seeds.append(("G-E2", f"markPoint bump on {mp_part['id']} (markPoints closure)",
                  stage_sets, s2, current_sets, current_official_sets))

    # Seed 3 / G-E3: one question dropped from a series set in BOTH the export
    # and the bundle of record (collusive drift — G-E1 parity holds, G-E2 mark
    # law holds; only the frozen per-series census refuses). Wave-19 note: with
    # a rename disclosure in play the lattice walk refuses FIRST (G-E1 — the
    # dropped question breaks the disclosed id lattice one gate earlier, a
    # strictly stronger property; without a disclosure the old attribution
    # G-E3 still holds because the lattices match and only the census sees it).
    s3 = json.loads(json.dumps(stage_official_sets))
    c3 = json.loads(json.dumps(current_official_sets))
    for coll in (s3, c3):
        for s in coll:
            if s["slug"] == seed_set["slug"]:
                s["questions"].pop()
    seeds.append(("G-E1" if disclosure_path else "G-E3",
                  f"question dropped from {seed_set['slug']} in BOTH export and bundle of record",
                  stage_sets, s3, current_sets, c3))

    # Seed 4 / G-E4: the SME file is touched (an SME set's name edited)
    s4 = json.loads(json.dumps(stage_sets))
    for s in s4:
        if s["slug"] == sme_slug:
            s["name"] = s["name"] + " (seed fault)"
    seeds.append(("G-E4", f"SME file mutation on {sme_slug}",
                  s4, stage_official_sets, current_sets, current_official_sets))

    print(f"self-test: clean stage must pass, then 4 seeded faults must be refused "
          f"(workdir {workdir}{' , kept' if keep else ''})")
    clean = run_gates(stage_path, stage_official_path, current_path, current_official_path,
                      quiet=True, allow_new_official=allow_new_official,
                      disclosure_path=disclosure_path)
    print(f"  PASS clean stage (G-E1..G-E4; {clean['parts']} parts, prefix {clean['prefix']}B)")

    detected = 0
    failures = []
    for want_gate, desc, st_sme, st_off, cu_sme, cu_off in seeds:
        seed_path = os.path.join(workdir, f"seed-{want_gate}-stage.json")
        seed_off_path = os.path.join(workdir, f"seed-{want_gate}-stage-official.json")
        cur_path = os.path.join(workdir, f"seed-{want_gate}-current.json")
        cur_off_path = os.path.join(workdir, f"seed-{want_gate}-current-official.json")
        with open(seed_path, "wb") as f:
            f.write(reserialize(st_sme))
        with open(seed_off_path, "wb") as f:
            f.write(reserialize(st_off))
        with open(cur_path, "wb") as f:
            f.write(reserialize(cu_sme))
        with open(cur_off_path, "wb") as f:
            f.write(reserialize(cu_off))
        try:
            run_gates(seed_path, seed_off_path, cur_path, cur_off_path,
                      quiet=True, allow_new_official=allow_new_official,
                      disclosure_path=disclosure_path)
            print(f"  FAIL seed NOT DETECTED ({desc})")
            failures.append((want_gate, desc, "not detected"))
        except GateRefusal as e:
            if e.gate == want_gate:
                print(f"  PASS {want_gate} refused the seed — {desc}")
                detected += 1
            else:
                print(f"  FAIL seed refused by {e.gate}, expected {want_gate} ({desc})")
                failures.append((want_gate, desc, f"refused by {e.gate}: {e.reason}"))
    print(f"self-test: {detected}/4 seeds refused" + (" — ACCEPTANCE MET" if detected == 4 else " — VOID"))
    if failures:
        for f_ in failures:
            print("   ", f_)
    if not keep:
        for name in os.listdir(workdir):
            os.unlink(os.path.join(workdir, name))
        os.rmdir(workdir)
    return detected == 4


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = ap.add_subparsers(dest="mode", required=True)
    v = sub.add_parser("verify", help="verify a staged export against the bundle of record")
    v.add_argument("--stage", required=True)
    v.add_argument("--stage-official-papers", required=True)
    v.add_argument("--current", required=True)
    v.add_argument("--current-official-papers", required=True)
    v.add_argument("--report", default=None, help="MULTI-SERIES-REPORT.json to cross-check constants")
    v.add_argument("--disclosure", default=None,
                   help="exporter-disclosures wave census the G-E1 delta census must equal")
    v.add_argument("--allow-new-official", action="store_true")
    t = sub.add_parser("self-test", help="seed 4 faults; every gate must refuse")
    t.add_argument("--stage", required=True)
    t.add_argument("--stage-official-papers", required=True)
    t.add_argument("--current", required=True)
    t.add_argument("--current-official-papers", required=True)
    t.add_argument("--keep", action="store_true")
    t.add_argument("--allow-new-official", action="store_true")
    t.add_argument("--disclosure", default=None,
                   help="rename-wave disclosure: the clean baseline passes through it")
    for sp in (v, t):
        sp.add_argument("--spec", default="4ch1", choices=sorted(_LANES),
                        help="corpus lane (Task 22): 4ch1 (default) | 4ph1")

    args = ap.parse_args()
    apply_lane(args.spec)
    try:
        if args.mode == "verify":
            run_gates(args.stage, args.stage_official_papers, args.current,
                      args.current_official_papers, args.report, args.allow_new_official,
                      disclosure_path=args.disclosure)
        else:
            ok = self_test(args.stage, args.stage_official_papers, args.current,
                           args.current_official_papers, args.keep, args.allow_new_official,
                           args.disclosure)
            if not ok:
                sys.exit(1)
    except GateRefusal as e:
        print(f"EXPORT GATE FAILED — {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
