#!/usr/bin/env python3
"""c42_r39_override_projection.py — T-C42 R39 derived projection emitter.

The R39 lane is the ELEVENTH R1-shaped repair round, the FIFTH over the
promoted surface, fired by the operator directive "fire R39/R40"
(2026-10-16, zai-web, gateway trace 1a145a7c26a0d4e5) over the R38
validation re-gate's defect inventory — the loop's FIRST 2-row DEMOTE
disposition round. The inventory is the R38 fresh judgment record's own
return: TWO fresh REJECTs (basic-probability :: 1, the probability-scale
surface joined at 6.3A; calculations-with-the-mean :: 1, the mean surface
joined at 6.2B).

The round has ZERO id-level REATTRIBUTEs and ZERO note-level re-points (the
notes' corpus anchors spcpt_FVX7YRftjhnwYHQF / spcpt_n9ZtYfjh8sFCp5Kz STAND
at the untouched join layer; the resolution file stays byte-untouched), so
the round's entire state carrier is TWofold, both derived
DETERMINISTICALLY from the operator-owned verdict record
scripts/c42_r39_repair_verdicts.yaml and emitted here (idempotent,
byte-identical re-runs):

  1. the next-re-build-facing override map
     scripts/c42_section_overrides_r39.yaml (schema
     c42-r28-section-overrides/1.0, the consuming-lane convention) carrying:
       - 2 verdicted DEMOTE_TO_WORKLIST entries (both HUMAN_VALIDATED — the
         R30 grouping-batch shape, the loop's SEVENTH and EIGHTH DEMOTEs;
         override_code null per the c40 R8 rule):
           basic-probability::1            6.3A -> (worklist)  (HV, FIRED)
           calculations-with-the-mean::1   6.2B -> (worklist)  (HV, FIRED)
       - ZERO REATTRIBUTE entries (no canonical target exists in the
         ratified 188 — live-verified this round for both surfaces)
       - the ZERO-retain contract block (nothing else is fired)
       - the note-level scoping notes (both corpus anchors STAND; the
         siblings' standing carry-chain verdicts untouched — the
         anti-forgery rule; no new c40-pinned adjudications)
       - the census remarks (the promoted-surface interaction — 2
         exclusions ONLY; the post-move per-code censuses) and the
         dated-corrections block (ONE entry: the R38 ledger-prose defect)

  2. the PROMOTIONS AMENDMENT — the second exclusion-only record
     scripts/c42_r39_promotions_amendment.yaml (schema
     c42-r31-promotions-amendment/1.0 — the R30 schema, unchanged: the
     supersedes/additions capabilities are present and UNUSED this round)
     carrying:
       - ZERO supersedes_code entries
       - 2 excluded entries (disposition DEMOTE_TO_WORKLIST — the DEMOTE
         rows leave the re-applied promotion set at the R40-shaped rebuild)
       - ZERO added entries (no sign-offs are owed)
       - the derived census projections (PROJECTED, ASSERTED NOWHERE — the
         DC-R24-01 discipline): re-applied promotions 830 -> 828 (825 from
         the R5 chain + 3 R30-added sign-offs), covered 133 -> 133,
         anchored 834 -> 832 (828 HV + 4 anchored SUGGESTED),
         unresolved-span 28 -> 30, store rows 917 -> 917 (the DEMOTE rows
         re-key into the worklist — chunk identity intact, the W3
         invariant); per-code 6.3A anchored 18 -> 17, 6.2B anchored
         24 -> 23
     The R5 promotions file itself stays BYTE-UNTOUCHED (the P5 convention).

Consumed fail-closed by the c40-shaped substrate tool (TOOL_VERSION 2.7.0)
at the NEXT substrate re-build (the R40-shaped lane) TOGETHER WITH the
R1/R6/R10/R14/R18/R22/R26/R30/R33/R36 maps — wiring the carriers into the
tool (with an operator-round descriptor the DEMOTE round-tag regex parses)
is the re-build lane's job (the R12/R16/R20/R24/R28/R31/R34/R37 precedent).

Usage: python3 scripts/c42_r39_override_projection.py
"""
import hashlib
import json
import re
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
VERDICTS = REPO / "scripts/c42_r39_repair_verdicts.yaml"
OVERRIDES_OUT = REPO / "scripts/c42_section_overrides_r39.yaml"
AMENDMENT_OUT = REPO / "scripts/c42_r39_promotions_amendment.yaml"
PROMOTIONS = REPO / "scripts/c42_r5_promotions.yaml"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
REGISTRY = REPO / "graph/igcse-maths-a/specification_points.yaml"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"

TASK = "T-C42"
ROUND = "R39"
DATE = "2026-10-16"

NOTE1 = ("notes/6-statistics-and-probability/probability-toolkit/"
         "basic-probability.json")
MOVER1 = "a5b737e510606829"
ORD1 = 1
CODE1 = "4MA1-6.3A"
SHA1 = "74b5c6214777c054"
REKEY1 = "09f012e4cabef0cc"
ANCHOR1 = "spcpt_FVX7YRftjhnwYHQF"

NOTE2 = ("notes/6-statistics-and-probability/statistics-toolkit/"
         "calculations-with-the-mean.json")
MOVER2 = "d545cd5f5aeae9a9"
ORD2 = 1
CODE2 = "4MA1-6.2B"
SHA2 = "22c1475d80a7d6df"
REKEY2 = "80d783fb13def4e2"
ANCHOR2 = "spcpt_n9ZtYfjh8sFCp5Kz"

MOVERS = {
    MOVER1: {"note": NOTE1, "ord": ORD1, "code": CODE1, "sha": SHA1,
             "rekey": REKEY1, "slug": "basic-probability"},
    MOVER2: {"note": NOTE2, "ord": ORD2, "code": CODE2, "sha": SHA2,
             "rekey": REKEY2, "slug": "calculations-with-the-mean"},
}

# the post-move keeper sets (live-verified this round; fail-closed) — the
# FULL same-code families: 6.3A keeps 17 anchored rows (the tree-diagrams
# quartet + the combined/conditional 8 + basic-probability's own ords
# 0/2/3/4/5); 6.2B keeps 23 (averages-from-tables 7 + the mean note's ord 0
# + comparing-distributions 5 + mean-median-and-mode 5 + range-and-quartiles 5)
KEEPERS1 = {"083b022f29358c51", "0aaeb3087163a2e2", "0d6a3b79dfd8a342",
            "202c160ef0ac3acf", "23ee88394f5dc132", "282ed1399101c134",
            "2f37fe5456f312e6", "40c24bc6a29ca254", "49d9c162749e6483",
            "5ec7170ce4cf1759", "8b1205674e5e68a5", "8fa41b23ee3fc5ce",
            "a37004be54955077", "bca5ee1833756107", "ca6f2a4b34021ec5",
            "d437d30f579f84d7", "e1d4ed2fb3e55f06"}
KEEPERS2 = {"0d417a743225afd3", "201c2a9df20b85d1", "28572319a8d1f35f",
            "2d215566e1c7d3f3", "32fcc1f67707ee62", "465131272f6985de",
            "500aeabde0de68d0", "58c131db5d09c786", "599553367c64e2fd",
            "61fc2e03d781e4ce", "8638b91481a3daf9", "8805634e5d5f8299",
            "882b64f82f888243", "88c6fa1d4db64e89", "8b1c1c639cb3402a",
            "9c8b7caf914c7548", "a076aa2fedbf7017", "adbbcbdb7678aa36",
            "c00a5e94e96f40ac", "c2ec54dc3b663bab", "cc6d3e4495476e4d",
            "de8f9de094683246", "ef2dcd5bd4a63f09"}

# fail-closed ledger facts — THE CORRECTED FORM: both codes ARE two-tier
# ledger rows with higher_preferred true (the R38 notes' "absent —
# single-tier" clause was a record-prose defect, corrected in the verdict
# record's dated_corrections).
LEDGER_FACTS = {
    "6.3A": {"higher_preferred": True,
             "higher": "draw and use tree diagrams",
             "foundation": "understand the language of probability"},
    "6.2B": {"higher_preferred": True,
             "higher": "understand the concept of a measure of spread",
             "foundation": ("calculate the mean, median, mode and range "
                            "for a discrete data set")},
    "6.3B": {"higher_preferred": True,
             "foundation": "understand and use the probability scale"},
}

# the ratified wordings the verdicts cite — fail-closed registry pins:
REGISTRY_WORDINGS = {
    "4MA1-6.3A": "draw and use tree diagrams",
    "4MA1-6.2B": "understand the concept of a measure of spread",
    "4MA1-6.3B": ("determine the probability that two or more independent "
                  "events will occur"),
    "4MA1-6.3D": "apply probability to simple problems",
    "4MA1-6.2A": "estimate the median from a cumulative frequency diagram",
    "4MA1-6.2C": "find the interquartile range from a discrete data set",
    "4MA1-6.2D": ("estimate the interquartile range from a cumulative "
                  "frequency diagram"),
    "4MA1-4.4F": ("understand and use the relationship between average "
                  "speed, distance and time"),
}


def fail(msg: str) -> None:
    print(f"FAIL-CLOSED: {msg}", file=sys.stderr)
    sys.exit(1)


def emit(path: Path, new_text: str, label: str, n: int) -> None:
    if path.exists():
        old = path.read_text(encoding="utf-8")
        if old != new_text:
            fail(f"{label} exists with different content — refusing to "
                 "overwrite (deterministic regeneration violated)")
        print(f"c42_r39_override_projection: {label} already current "
              f"({n} entries) — idempotent no-op")
        return
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(new_text, encoding="utf-8")
    tmp.replace(path)
    print(f"c42_r39_override_projection: WROTE {path.relative_to(REPO)} "
          f"— {label} ({n} entries)")


def main() -> int:
    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    store = yaml.safe_load(STORE.read_text(encoding="utf-8"))
    reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    points = {p["code"]: p for p in reg["specification_points"]}
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    led_rows = {r["official_code"]: r for r in ledger["rows"]}
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    promo_pins = {e["row"]["mapping_id"]: e["row"] for e in promo["promotions"]}
    rows_by_id = {r["mapping_id"]: r for r in store["rows"]}
    meta = store.get("meta") or {}

    # ---- shared fail-closed checks ------------------------------------------
    for bare, fact in LEDGER_FACTS.items():
        row = led_rows.get(bare)
        if row is None:
            fail(f"C30 ledger fact drifted: {bare} expected PRESENT")
        if row.get("higher_preferred") != fact["higher_preferred"]:
            fail(f"C30 ledger higher_preferred drifted for {bare}")
        if fact.get("higher") and \
                (row.get("higher") or {}).get("text") != fact["higher"]:
            fail(f"C30 ledger Higher text drifted for {bare}")
        if (row.get("foundation") or {}).get("text") != fact["foundation"]:
            fail(f"C30 ledger Foundation text drifted for {bare}")
    for code, want in REGISTRY_WORDINGS.items():
        got = (points.get(code) or {}).get("official_wording")
        if got != want:
            fail(f"registry wording drifted for {code}: {got!r}")

    # THE NO-TARGET FACTS, live:
    # (a) 'tree diagram' wording ONLY on 6.3A
    hits = sorted(p["code"] for p in reg["specification_points"]
                  if "tree diagram" in (p.get("official_wording") or "").lower())
    if hits != ["4MA1-6.3A"]:
        fail(f"no-target fact drifted: tree-diagram hits {hits}")
    # (b) the non-6.3 'scale' hits are instruments/drawings/enlargements
    scale = sorted(p["code"] for p in reg["specification_points"]
                   if "scale" in (p.get("official_wording") or "").lower())
    if scale != ["4MA1-4.4A", "4MA1-4.5C", "4MA1-5.2J", "4MA1-5.2L"]:
        fail(f"no-target fact drifted: scale hits {scale}")
    # (c) word-boundary mean/average scan hits ONLY 4.4F
    mean_hits = sorted(p["code"] for p in reg["specification_points"]
                       if re.search(r"\bmean\b|\baverage\b",
                                    (p.get("official_wording") or "").lower()))
    if mean_hits != ["4MA1-4.4F"]:
        fail(f"no-target fact drifted: mean/average hits {mean_hits}")
    # (d) 'spread' wording ONLY on 6.2B
    spread = sorted(p["code"] for p in reg["specification_points"]
                    if "spread" in (p.get("official_wording") or "").lower())
    if spread != ["4MA1-6.2B"]:
        fail(f"no-target fact drifted: spread hits {spread}")
    # (e) no wording names the probability-scale surface (Higher tier)
    for p in reg["specification_points"]:
        w = (p.get("official_wording") or "").lower()
        if "probability scale" in w:
            fail(f"no-target fact drifted: {p['code']} names the scale {w!r}")
        if "central tendency" in w or "measure of central" in w:
            fail(f"no-target fact drifted: {p['code']} names the mean "
                 f"surface {w!r}")

    # the standing baseline censuses the projections assume
    if meta.get("rows_anchored") != 834 or meta.get("promoted_rows") != 830 \
            or meta.get("rows_worklist_anchor_unresolved") != 28 \
            or meta.get("rows_worklist_unmapped_sps") != 55 \
            or meta.get("sp_codes_covered") != 133 \
            or meta.get("registry_size") != 188:
        fail(f"baseline meta census drifted: "
             f"{dict((k, meta.get(k)) for k in ('rows_anchored', 'promoted_rows', 'rows_worklist_anchor_unresolved', 'rows_worklist_unmapped_sps', 'sp_codes_covered', 'registry_size'))}")

    # ---- the verdict rows -----------------------------------------------------
    so = ver.get("section_overrides") or {}
    if sorted(so.keys()) != ["basic-probability::1",
                             "calculations-with-the-mean::1"]:
        fail(f"expected exactly the fired inventory basic-probability::1 + "
             f"calculations-with-the-mean::1, got {sorted(so.keys())}")
    for mid, f in MOVERS.items():
        v = next((v for v in so.values() if v.get("mapping_id") == mid), None)
        if v is None:
            fail(f"verdict row {mid} missing from the verdict record")
        if v.get("disposition") != "DEMOTE_TO_WORKLIST":
            fail(f"unexpected disposition on {mid}: {v.get('disposition')!r}")
        if v.get("override_code") is not None:
            fail(f"the {mid} DEMOTE verdict carries an override_code — the "
                 "c40 R8 rule forbids it (no target exists)")
        if v.get("current_code") != f["code"]:
            fail(f"verdict identity drift on {mid}")
        srow = rows_by_id.get(mid)
        if srow is None:
            fail(f"verdict row {mid} not found in the live substrate")
        if srow["spec_code"] != f["code"]:
            fail(f"current_code drift on {mid}: store {srow['spec_code']}")
        if srow.get("validation_status") != "HUMAN_VALIDATED":
            fail(f"mover {mid} is not HUMAN_VALIDATED: "
                 f"{srow.get('validation_status')}")
        if srow["note_path"] != f["note"] or \
                srow["chunk"]["ordinal"] != f["ord"]:
            fail(f"note::ordinal identity drift on {mid}: "
                 f"{srow['note_path']}:{srow['chunk']['ordinal']}")
        if srow["chunk"].get("sha256_16") != f["sha"]:
            fail(f"mover {mid} chunk sha drifted: "
                 f"{srow['chunk'].get('sha256_16')}")
        if "promotion" not in srow:
            fail(f"mover {mid} carries no promotion block")
        pin = promo_pins.get(mid)
        if pin is None:
            fail(f"the promoted mover {mid} is not pinned in the R5 file")
        if pin.get("spec_code") != f["code"] or \
                pin.get("note_path") != f["note"] or \
                pin.get("chunk_ordinal") != f["ord"]:
            fail(f"promotions pin identity drift on {mid}: {pin}")
        # the projected demoted re-key (the c40 identity function)
        demoted_id = hashlib.sha256(
            f"demoted|{f['note']}|{f['ord']}".encode("utf-8")).hexdigest()[:16]
        if demoted_id != f["rekey"]:
            fail(f"projected demoted id drifted on {mid}: {demoted_id}")

    # ---- the family censuses (live, row-by-row) -------------------------------
    for mid, f, keepers in ((MOVER1, MOVERS[MOVER1], KEEPERS1),
                            (MOVER2, MOVERS[MOVER2], KEEPERS2)):
        fam = [r for r in store["rows"] if r.get("spec_code") == f["code"]
               and "chunk" in r]
        anchored = [r for r in fam if r.get("validation_status")
                    in ("HUMAN_VALIDATED", "SUGGESTED")]
        want_n = len(keepers) + 1
        if len(fam) != want_n or len(anchored) != want_n:
            fail(f"{f['code']} family census drifted: {len(fam)} rows / "
                 f"{len(anchored)} anchored (want {want_n})")
        if any(r.get("validation_status") == "SUGGESTED" for r in fam):
            fail(f"SUGGESTED rows ride {f['code']} — unexpected")
        if any(r.get("worklist_reason") for r in fam):
            fail(f"a {f['code']} row carries a worklist_reason — unexpected")
        keep = {r["mapping_id"] for r in anchored
                if r["mapping_id"] != mid}
        if keep != keepers:
            fail(f"post-move {f['code']} keepers drifted: {sorted(keep)}")

    # covered-code census (HV rows -> distinct codes)
    covered = {r["spec_code"] for r in store["rows"]
               if r.get("validation_status") == "HUMAN_VALIDATED"}
    if len(covered) != 133 or CODE1 not in covered or CODE2 not in covered:
        fail(f"covered census drifted: {len(covered)} (6.3A in covered: "
             f"{CODE1 in covered}; 6.2B in covered: {CODE2 in covered})")

    # ---- blocks agreement ------------------------------------------------------
    retains = ver.get("retain_rulings") or {}
    if set(retains) - {"contract"}:
        fail(f"retain rulings expected EMPTY (the fired inventory is the "
             f"2-row DEMOTE batch): {sorted(set(retains) - {'contract'})}")
    scoping = ver.get("note_level_scoping") or []
    if [s.get("note_slug") for s in scoping] != \
            ["basic-probability", "calculations-with-the-mean"]:
        fail("note-level scoping block drifted")
    remarks = ver.get("census_remarks") or []
    if len(remarks) < 2:
        fail("census remarks missing")
    dcorr = ver.get("dated_corrections") or []
    if len(dcorr) != 1 or "c42_r38_fresh_verdicts" not in dcorr[0].get(
            "corrects", ""):
        fail("the dated-corrections block must carry exactly the R38 "
             "ledger-prose correction")

    # ---- 1. the override map -----------------------------------------------------
    entries = []
    for mid, f in MOVERS.items():
        v = next(v for v in so.values() if v.get("mapping_id") == mid)
        entries.append({
            "note_slug": f["slug"],
            "chunk_ordinal": f["ord"],
            "mapping_id": mid,
            "current_code": f["code"],
            "provenance_class": "verdicted",
            "action": "DEMOTE_TO_WORKLIST",
            "override_code": None,
            "evidence": (v.get("evidence") or "").strip(),
        })
    doc = {
        "schema": "c42-r28-section-overrides/1.0",
        "task": TASK,
        "round": ROUND,
        "generated": DATE,
        "source": ("scripts/c42_r39_repair_verdicts.yaml (section_overrides "
                   "+ retain_rulings + note_level_scoping + census_remarks + "
                   "dated_corrections)"),
        "contract": (
            "consumed fail-closed by the c40-shaped substrate tool "
            "(TOOL_VERSION 2.7.0) at the NEXT substrate re-build (the "
            "R40-shaped lane) TOGETHER WITH scripts/c42_section_overrides.yaml "
            "(R1), scripts/c42_section_overrides_r6.yaml (R6), "
            "scripts/c42_section_overrides_r10.yaml (R10), "
            "scripts/c42_section_overrides_r14.yaml (R14), "
            "scripts/c42_section_overrides_r18.yaml (R18), "
            "scripts/c42_section_overrides_r22.yaml (R22), "
            "scripts/c42_section_overrides_r26.yaml (R26), "
            "scripts/c42_section_overrides_r30.yaml (R30), "
            "scripts/c42_section_overrides_r33.yaml (R33) and "
            "scripts/c42_section_overrides_r36.yaml (R36) — an override "
            "naming a code outside the ratified 188 fails the build; "
            "current_code must equal the join-derived code; REATTRIBUTE "
            "targets must sit in the ratified registry; DEMOTE entries carry "
            "override_code null and land the chunk unresolved-span (the "
            "R10/R14/R18/R26/R30/R36 convention) — the consuming lane must "
            "wire this map with the operator-round descriptor \"C42 R39 "
            "(surface 3: 2 verdicted DEMOTE_TO_WORKLIST — the R38 fresh "
            "REJECTs adjudicated; ZERO REATTRIBUTEs, ZERO sign-offs)\" so "
            "the DEMOTE handler's round-tag regex parses (the R16 "
            "discipline). Applied rows carry provenance.override with the "
            "map sha. NO resolution-file amendment this round: the standing "
            "note-level joins remain STANDING at the untouched join layer "
            "(the basic-probability corpus anchor spcpt_FVX7YRftjhnwYHQF "
            "stands at 6.3A; the calculations-with-the-mean corpus anchor "
            "spcpt_n9ZtYfjh8sFCp5Kz stands at 6.2B), the resolution file "
            "stays byte-untouched (since R14). PROMOTIONS INTERACTION (the "
            "R26/R30/R36 shape): the R40-shaped rebuild must consume "
            "scripts/c42_r39_promotions_amendment.yaml in its promotions "
            "re-application — the 2 DEMOTE rows are EXCLUDED from the "
            "re-applied set (landing unresolved-span via the c40 DEMOTE "
            "convention, chunk identity intact — the W3 invariant); ZERO "
            "supersedes and ZERO additions (the R30 additions mechanism "
            "unused — no sign-offs owed). The zero-retain contract rides NO "
            "carrier entry (zero movement). "
            "scripts/c42_r5_promotions.yaml itself stays BYTE-UNTOUCHED (the "
            "P5 convention). Coverage projections (PROJECTED, ASSERTED "
            "NOWHERE — the DC-R24-01 discipline): covered 133 -> 133 (6.3A "
            "keeps the tree-diagrams quartet + the combined/conditional 8 + "
            "basic-probability ords 0/2/3/4/5; 6.2B keeps its 23 — no gain, "
            "no loss), anchored 834 -> 832 (828 HUMAN_VALIDATED + 4 anchored "
            "SUGGESTED), unresolved-span 28 -> 30, uncovered-SP 55 -> 55, "
            "store rows 917 -> 917; per-code 4MA1-6.3A anchored 18 -> 17, "
            "4MA1-6.2B anchored 24 -> 23"),
        "overrides": entries,
        "retain_rulings": ver.get("retain_rulings") or {},
        "note_level_scoping": ver["note_level_scoping"],
        "census_remarks": ver["census_remarks"],
        "promoted_surface_amendment": {
            "amendment_file": "scripts/c42_r39_promotions_amendment.yaml",
            "base_file": "scripts/c42_r5_promotions.yaml",
            "base_file_untouched": True,
            "supersedes": 0,
            "excluded": 2,
            "added": 0,
        },
        "dated_corrections": ver.get("dated_corrections", []),
    }
    body = yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100)
    header = (
        f"# T-C42 {ROUND} operator section-override map — derived from the R39 verdict record\n"
        f"# (the loop's ELEVENTH R1-shaped repair round and the FIFTH over the promoted\n"
        f"# surface; 2 verdicted DEMOTE_TO_WORKLIST [both HUMAN_VALIDATED, the R30 grouping-batch\n"
        f"# shape, the loop's SEVENTH and EIGHTH DEMOTEs — the R38 fresh REJECTs adjudicated:\n"
        f"# basic-probability ord 1 (the probability-scale surface pinned at 6.3A 'draw and use\n"
        f"# tree diagrams') and calculations-with-the-mean ord 1 (the mean surface pinned at 6.2B\n"
        f"# 'understand the concept of a measure of spread'), each with NO canonical target in the\n"
        f"# ratified 188; the C30 ledger facts CORRECTED in the verdict record's dated_corrections\n"
        f"# block]; ZERO REATTRIBUTEs; ZERO sign-offs owed; ZERO retain rulings; both corpus\n"
        f"# anchors STAND at the untouched join layer). Written ONLY by\n"
        f"# scripts/c42_r39_override_projection.py; hand-editing is forbidden.\n"
    )
    emit(OVERRIDES_OUT, header + body, "override map", 2)

    # ---- 2. the promotions amendment -------------------------------------------
    adoc = {
        "schema": "c42-r31-promotions-amendment/1.0",
        "task": TASK,
        "round": ROUND,
        "generated": DATE,
        "source": ("scripts/c42_r39_repair_verdicts.yaml "
                   "(section_overrides)"),
        "base_file": "scripts/c42_r5_promotions.yaml",
        "base_file_sha256_16": "9bad739bd79e5899",
        "base_file_untouched": True,
        "prior_amendments": [
            "scripts/c42_r26_promotions_amendment.yaml",
            "scripts/c42_r30_promotions_amendment.yaml",
            "scripts/c42_r33_promotions_amendment.yaml",
            "scripts/c42_r36_promotions_amendment.yaml",
        ],
        "contract": (
            "consumed fail-closed by the R40-shaped substrate re-build's "
            "promotions re-application AFTER the R5 file is loaded and AFTER "
            "the R26+R30+R33+R36 amendments' outstanding effects are carried "
            "(those are already LANDED state in the R39 baseline store; the "
            "R39 amendment acts on the re-applied set): every excluded entry "
            "removes one row from the re-applied promotion set (the DEMOTE "
            "lands unresolved-span via the c40 DEMOTE convention, NOT "
            "re-promoted; chunk identity intact — the W3 invariant). ZERO "
            "supersedes_code entries and ZERO added entries this round — the "
            "supersedes/additions capabilities are present in the schema and "
            "UNUSED (no sign-offs are owed: the R30 round discharged all 4 "
            "H3 holds of record). The re-applied promotion count becomes 828 "
            "(830 - 2 exclusions = 825 from the R5 chain + 3 R30-added "
            "sign-offs). The R5 file itself stays BYTE-UNTOUCHED (the P5 "
            "convention — landed records never edited); this amendment is "
            "the dated record of the R39 operator-fired adjudication and "
            "remains reviewable and reversible by the operator before the "
            "R40-shaped lane fires."),
        "supersedes_code": [],
        "excluded": [
            {
                "mapping_id": MOVER1,
                "note_path": NOTE1,
                "chunk_ordinal": ORD1,
                "pinned_code": CODE1,
                "disposition": "DEMOTE_TO_WORKLIST",
            },
            {
                "mapping_id": MOVER2,
                "note_path": NOTE2,
                "chunk_ordinal": ORD2,
                "pinned_code": CODE2,
                "disposition": "DEMOTE_TO_WORKLIST",
            },
        ],
        "added": [],
        "derived_census_projected": {
            "re_applied_promotions": 828,
            "re_applied_composition": ("825 from the R5 chain [832 - 1 R26 "
                                       "exclusion - 3 R30 exclusions - 1 R36 "
                                       "exclusion - 2 R39 exclusions] + 3 "
                                       "R30-added sign-offs"),
            "covered_codes": "133 -> 133",
            "coverage_gained": [],
            "coverage_lost": [],
            "uncovered_sp": "55 -> 55",
            "resolved_defer_rows": [],
            "anchored": "834 -> 832 (828 HUMAN_VALIDATED + 4 anchored SUGGESTED)",
            "unresolved_span": "28 -> 30 (the R39 DEMOTE batch of 2)",
            "store_rows": "917 -> 917 (the DEMOTE rows re-key into the "
                          "worklist — chunk identity intact, the W3 "
                          "invariant; no row vanishes)",
            "per_code": ("4MA1-6.3A anchored 18 -> 17 (the tree-diagrams "
                         "quartet + the combined/conditional 8 + "
                         "basic-probability ords 0/2/3/4/5 remain; the "
                         f"demoted ord 1 re-keys to {REKEY1} in the "
                         "worklist); 4MA1-6.2B anchored 24 -> 23 (the mean "
                         "note's ord 0 + its 22 family rows remain; the "
                         f"demoted ord 1 re-keys to {REKEY2})"),
        },
        "caveat": (
            "PROJECTED from verified facts, ASSERTED NOWHERE — every count "
            "lands at the R40-shaped rebuild lane (which computes its own "
            "delta proofs, the R24 R5-gate convention) and the re-gate lane "
            "after it; the DC-R24-01 discipline (compute, never assert "
            "coverage) is in force"),
    }
    abody = yaml.safe_dump(adoc, allow_unicode=True, sort_keys=False, width=100)
    aheader = (
        f"# T-C42 {ROUND} promotions amendment — derived from the R39 verdict record\n"
        f"# (the loop's FIFTH promotions-affecting repair record and the SECOND\n"
        f"# exclusion-ONLY one: 0 code supersedes + 2 exclusions + 0 additions — the\n"
        f"# R30 additions mechanism present and UNUSED, no sign-offs owed; the R5\n"
        f"# promotions file stays byte-untouched per the P5 convention). Written\n"
        f"# ONLY by scripts/c42_r39_override_projection.py; hand-editing is forbidden.\n"
    )
    emit(AMENDMENT_OUT, aheader + abody, "promotions amendment", 2)

    print(f"  basic-probability::1 {CODE1} -> (worklist) "
          f"[DEMOTE_TO_WORKLIST, projected re-key {REKEY1}]")
    print(f"  calculations-with-the-mean::1 {CODE2} -> (worklist) "
          f"[DEMOTE_TO_WORKLIST, projected re-key {REKEY2}]")
    print("  RETAIN (zero-movement continuity): none fired beyond the "
          "2-row batch")
    return 0


if __name__ == "__main__":
    sys.exit(main())
