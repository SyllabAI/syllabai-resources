#!/usr/bin/env python3
"""c42_r36_override_projection.py — T-C42 R36 derived projection emitter.

The R36 lane is the TENTH R1-shaped repair round, the FOURTH over the
promoted surface, fired by the operator directive "① R36-shaped adjudication
of the R35 fresh REJECT a107f5041769fdd9 @ 1.6F (forward-only
express-as-percentage chunk)" (2026-10-16, zai-web, gateway trace
1a144b85ee89644d) over the R35 validation re-gate's defect inventory — the
loop's FIRST single-row DEMOTE disposition round. The inventory is the R35
fresh judgment record's own return: ONE fresh REJECT (basic-percentages :: 4,
the forward express-one-number-as-a-percentage surface joined at 1.6F).

The round has ZERO id-level REATTRIBUTEs and ZERO note-level re-points (the
note's corpus anchor spcpt_FHRjdMc6tvRR553q STANDS at the untouched join
layer; the resolution file stays byte-untouched), so the round's entire
state carrier is TWofold, both derived DETERMINISTICALLY from the
operator-owned verdict record scripts/c42_r36_repair_verdicts.yaml and
emitted here (idempotent, byte-identical re-runs):

  1. the next-re-build-facing override map
     scripts/c42_section_overrides_r36.yaml (schema
     c42-r28-section-overrides/1.0, the consuming-lane convention) carrying:
       - 1 verdicted DEMOTE_TO_WORKLIST entry (HUMAN_VALIDATED — the R30
         grouping-batch shape, the loop's SIXTH DEMOTE; override_code null
         per the c40 R8 rule):
           basic-percentages::4   1.6F -> (worklist)   (HV, the FIRED defect)
       - ZERO REATTRIBUTE entries (no canonical target exists in the
         ratified 188 — live-verified this round: the only 1.6 wording
         carrying both "express" and "percentage" is 1.6C, the CONVERSE)
       - the ZERO-retain contract block (nothing else is fired)
       - the note-level scoping note (the basic-percentages corpus anchor
         STANDS at 1.6F; ord 3's standing carry-chain verdict untouched —
         the anti-forgery rule; no new c40-pinned adjudications)
       - the census remarks (the promoted-surface interaction — 1 exclusion
         ONLY; the post-move per-code censuses) and the (empty)
         dated-corrections block

  2. the PROMOTIONS AMENDMENT — the exclusion-only record
     scripts/c42_r36_promotions_amendment.yaml (schema
     c42-r31-promotions-amendment/1.0 — the R30 schema, unchanged: the
     supersedes/additions capabilities are present and UNUSED this round)
     carrying:
       - ZERO supersedes_code entries
       - 1 excluded entry (disposition DEMOTE_TO_WORKLIST — the DEMOTE row
         leaves the re-applied promotion set at the R37-shaped rebuild)
       - ZERO added entries (no sign-offs are owed)
       - the derived census projections (PROJECTED, ASSERTED NOWHERE — the
         DC-R24-01 discipline): re-applied promotions 831 -> 830 (827 from
         the R5 chain + 3 R30-added sign-offs), covered 133 -> 133, anchored
         835 -> 834 (830 HV + 4 anchored SUGGESTED), unresolved-span 27 ->
         28, store rows 917 -> 917 (the DEMOTE row re-keys into the
         worklist — chunk identity intact, the W3 invariant); per-code
         4MA1-1.6F anchored 6 -> 5
     The R5 promotions file itself stays BYTE-UNTOUCHED (the P5 convention).

Consumed fail-closed by the c40-shaped substrate tool (TOOL_VERSION 2.7.0)
at the NEXT substrate re-build (the R37-shaped lane) TOGETHER WITH the
R1/R6/R10/R14/R18/R22/R26/R30/R33 maps — wiring the carriers into the tool
(with an operator-round descriptor the DEMOTE round-tag regex parses) is the
re-build lane's job (the R12/R16/R20/R24/R28/R31/R34 precedent).

Usage: python3 scripts/c42_r36_override_projection.py
"""
import hashlib
import json
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
VERDICTS = REPO / "scripts/c42_r36_repair_verdicts.yaml"
OVERRIDES_OUT = REPO / "scripts/c42_section_overrides_r36.yaml"
AMENDMENT_OUT = REPO / "scripts/c42_r36_promotions_amendment.yaml"
PROMOTIONS = REPO / "scripts/c42_r5_promotions.yaml"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
REGISTRY = REPO / "graph/igcse-maths-a/specification_points.yaml"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"

TASK = "T-C42"
ROUND = "R36"
DATE = "2026-10-16"

NOTE_PATH = ("notes/1-numbers-and-the-number-system/"
             "percentages/basic-percentages.json")
MOVER_ID = "a107f5041769fdd9"
MOVER_ORD = 4
MOVER_CODE = "4MA1-1.6F"
PROJECTED_DEMOTE_ID = "8254a7fc75ad2946"

# fail-closed fact set: 1.6F is ABSENT from the C30 ledger (single-tier
# Higher-operative row) — the tier-artifact escape is closed for this round's
# verdict.
LEDGER_FACTS = [("1.6F", False)]

# the ratified wordings the verdict cites — fail-closed registry pins:
REGISTRY_WORDINGS = {
    "4MA1-1.6F": "use reverse percentages",
    "4MA1-1.6C": "express a percentage as a fraction and as a decimal",
    "4MA1-1.6E": ("solve simple percentage problems, including percentage "
                  "increase and decrease"),
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
        print(f"c42_r36_override_projection: {label} already current "
              f"({n} entries) — idempotent no-op")
        return
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(new_text, encoding="utf-8")
    tmp.replace(path)
    print(f"c42_r36_override_projection: WROTE {path.relative_to(REPO)} "
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
    for bare, expected_present in LEDGER_FACTS:
        if (bare in led_rows) != expected_present:
            fail(f"C30 ledger fact drifted for {bare}: "
                 f"present={bare in led_rows} expected={expected_present}")
    for code, want in REGISTRY_WORDINGS.items():
        got = (points.get(code) or {}).get("official_wording")
        if got != want:
            fail(f"registry wording drifted for {code}: {got!r}")

    # THE NO-TARGET FACT, live: the only 'express'+'percentage' wording in
    # the ratified 188 is 1.6C (the converse) — and no wording names the
    # express-one-number-as-a-percentage surface at all.
    hits = sorted(p["code"] for p in reg["specification_points"]
                  if "express" in (p.get("official_wording") or "").lower()
                  and "percentage" in (p.get("official_wording") or "").lower())
    if hits != ["4MA1-1.6C"]:
        fail(f"no-target fact drifted: express+percentage hits {hits}")
    for p in reg["specification_points"]:
        w = (p.get("official_wording") or "").lower()
        if "as a percentage of another" in w or "one number as a percentage" in w:
            fail(f"no-target fact drifted: {p['code']} names the surface {w!r}")

    # the standing baseline censuses the projections assume
    if meta.get("rows_anchored") != 835 or meta.get("promoted_rows") != 831 \
            or meta.get("rows_worklist_anchor_unresolved") != 27 \
            or meta.get("sp_codes_covered") != 133 \
            or meta.get("registry_size") != 188:
        fail(f"baseline meta census drifted: "
             f"{dict((k, meta.get(k)) for k in ('rows_anchored', 'promoted_rows', 'rows_worklist_anchor_unresolved', 'sp_codes_covered', 'registry_size'))}")

    # ---- the verdict row -----------------------------------------------------
    so = ver.get("section_overrides") or {}
    if list(so.keys()) != ["basic-percentages::4"]:
        fail(f"expected exactly the fired inventory basic-percentages::4, "
             f"got {list(so.keys())}")
    v = so["basic-percentages::4"]
    if v.get("disposition") != "DEMOTE_TO_WORKLIST":
        fail(f"unexpected disposition {v.get('disposition')!r}")
    if v.get("override_code") is not None:
        fail("the DEMOTE verdict carries an override_code — the c40 R8 rule "
             "forbids it (no target exists)")
    if v.get("mapping_id") != MOVER_ID or v.get("current_code") != MOVER_CODE:
        fail("verdict identity drift")
    srow = rows_by_id.get(MOVER_ID)
    if srow is None:
        fail(f"verdict row {MOVER_ID} not found in the live substrate")
    if srow["spec_code"] != MOVER_CODE or v["current_code"] != srow["spec_code"]:
        fail(f"current_code drift: store {srow['spec_code']}")
    if srow.get("validation_status") != "HUMAN_VALIDATED":
        fail(f"mover is not HUMAN_VALIDATED: {srow.get('validation_status')}")
    if srow["note_path"] != NOTE_PATH or srow["chunk"]["ordinal"] != MOVER_ORD:
        fail(f"note::ordinal identity drift: {srow['note_path']}:"
             f"{srow['chunk']['ordinal']}")
    if srow["chunk"].get("sha256_16") != "d4947ba63e47dd1f":
        fail(f"mover chunk sha drifted: {srow['chunk'].get('sha256_16')}")
    pin = promo_pins.get(MOVER_ID)
    if pin is None:
        fail("the promoted mover is not pinned in the R5 file")
    if pin.get("spec_code") != MOVER_CODE or \
            pin.get("note_path") != NOTE_PATH or \
            pin.get("chunk_ordinal") != MOVER_ORD:
        fail(f"promotions pin identity drift: {pin}")

    # the projected demoted re-key (the c40 identity function)
    demoted_id = hashlib.sha256(
        f"demoted|{NOTE_PATH}|{MOVER_ORD}".encode("utf-8")).hexdigest()[:16]
    if demoted_id != PROJECTED_DEMOTE_ID:
        fail(f"projected demoted id drifted: {demoted_id}")

    # ---- the 1.6F family census (live, row-by-row) ---------------------------
    fam = [r for r in store["rows"] if r.get("spec_code") == MOVER_CODE]
    anchored = [r for r in fam if r.get("validation_status")
                in ("HUMAN_VALIDATED", "SUGGESTED")]
    if len(fam) != 6 or len(anchored) != 6:
        fail(f"1.6F family census drifted: {len(fam)} rows / "
             f"{len(anchored)} anchored")
    if any(r.get("validation_status") == "SUGGESTED" for r in fam):
        fail("SUGGESTED rows ride 1.6F — unexpected")
    if any(r.get("worklist_reason") for r in fam):
        fail("a 1.6F row carries a worklist_reason — unexpected")
    keepers = {r["mapping_id"] for r in anchored
               if r["mapping_id"] != MOVER_ID}
    expected_keepers = {"0bbe42313181c4c9", "24f7c615715385b1",
                        "0712e32bdab4b9c2", "b50465d5a341e0d6",
                        "f581371fd0524930"}
    if keepers != expected_keepers:
        fail(f"post-move 1.6F keepers drifted: {sorted(keepers)}")

    # covered-code census (HV rows -> distinct codes)
    covered = {r["spec_code"] for r in store["rows"]
               if r.get("validation_status") == "HUMAN_VALIDATED"}
    if len(covered) != 133 or MOVER_CODE not in covered:
        fail(f"covered census drifted: {len(covered)} (1.6F in covered: "
             f"{MOVER_CODE in covered})")

    # ---- blocks agreement ------------------------------------------------------
    retains = ver.get("retain_rulings") or {}
    if set(retains) - {"contract"}:
        fail(f"retain rulings expected EMPTY (the fired inventory is the "
             f"single DEMOTE row): {sorted(set(retains) - {'contract'})}")
    scoping = ver.get("note_level_scoping") or []
    if len(scoping) != 1 or scoping[0].get("note_slug") != "basic-percentages":
        fail("note-level scoping block drifted")
    remarks = ver.get("census_remarks") or []
    if len(remarks) < 2:
        fail("census remarks missing")

    # ---- 1. the override map -----------------------------------------------------
    entry = {
        "note_slug": "basic-percentages",
        "chunk_ordinal": MOVER_ORD,
        "mapping_id": MOVER_ID,
        "current_code": MOVER_CODE,
        "provenance_class": "verdicted",
        "action": "DEMOTE_TO_WORKLIST",
        "override_code": None,
        "evidence": (v.get("evidence") or "").strip(),
    }
    doc = {
        "schema": "c42-r28-section-overrides/1.0",
        "task": TASK,
        "round": ROUND,
        "generated": DATE,
        "source": ("scripts/c42_r36_repair_verdicts.yaml (section_overrides "
                   "+ retain_rulings + note_level_scoping + census_remarks + "
                   "dated_corrections)"),
        "contract": (
            "consumed fail-closed by the c40-shaped substrate tool "
            "(TOOL_VERSION 2.7.0) at the NEXT substrate re-build (the "
            "R37-shaped lane) TOGETHER WITH scripts/c42_section_overrides.yaml "
            "(R1), scripts/c42_section_overrides_r6.yaml (R6), "
            "scripts/c42_section_overrides_r10.yaml (R10), "
            "scripts/c42_section_overrides_r14.yaml (R14), "
            "scripts/c42_section_overrides_r18.yaml (R18), "
            "scripts/c42_section_overrides_r22.yaml (R22), "
            "scripts/c42_section_overrides_r26.yaml (R26), "
            "scripts/c42_section_overrides_r30.yaml (R30) and "
            "scripts/c42_section_overrides_r33.yaml (R33) — an override "
            "naming a code outside the ratified 188 fails the build; "
            "current_code must equal the join-derived code; REATTRIBUTE "
            "targets must sit in the ratified registry; DEMOTE entries carry "
            "override_code null and land the chunk unresolved-span (the "
            "R10/R14/R18/R26/R30 convention) — the consuming lane must wire "
            "this map with the operator-round descriptor \"C42 R36 (surface "
            "3: 1 verdicted DEMOTE_TO_WORKLIST — the R35 fresh REJECT "
            "adjudicated; ZERO REATTRIBUTEs, ZERO sign-offs)\" so the DEMOTE "
            "handler's round-tag regex parses (the R16 discipline). Applied "
            "rows carry provenance.override with the map sha. NO "
            "resolution-file amendment this round: the standing note-level "
            "joins remain STANDING at the untouched join layer (the "
            "basic-percentages corpus anchor spcpt_FHRjdMc6tvRR553q stands "
            "at 1.6F), the resolution file stays byte-untouched (since R14). "
            "PROMOTIONS INTERACTION (the R26/R30 shape): the R37-shaped "
            "rebuild must consume scripts/c42_r36_promotions_amendment.yaml "
            "in its promotions re-application — the 1 DEMOTE row is EXCLUDED "
            "from the re-applied set (landing unresolved-span via the c40 "
            "DEMOTE convention, chunk identity intact — the W3 invariant); "
            "ZERO supersedes and ZERO additions (the R30 additions mechanism "
            "unused — no sign-offs owed). The zero-retain contract rides NO "
            "carrier entry (zero movement). "
            "scripts/c42_r5_promotions.yaml itself stays BYTE-UNTOUCHED (the "
            "P5 convention). Coverage projections (PROJECTED, ASSERTED "
            "NOWHERE — the DC-R24-01 discipline): covered 133 -> 133 (1.6F "
            "keeps the reverse-percentages trio + basic-percentages ords 0/3 "
            "— no gain, no loss), anchored 835 -> 834 (830 HUMAN_VALIDATED + "
            "4 anchored SUGGESTED), unresolved-span 27 -> 28, uncovered-SP "
            "55 -> 55, store rows 917 -> 917; per-code 4MA1-1.6F anchored "
            "6 -> 5"),
        "overrides": [entry],
        "retain_rulings": ver.get("retain_rulings") or {},
        "note_level_scoping": ver["note_level_scoping"],
        "census_remarks": ver["census_remarks"],
        "promoted_surface_amendment": {
            "amendment_file": "scripts/c42_r36_promotions_amendment.yaml",
            "base_file": "scripts/c42_r5_promotions.yaml",
            "base_file_untouched": True,
            "supersedes": 0,
            "excluded": 1,
            "added": 0,
        },
        "dated_corrections": ver.get("dated_corrections", []),
    }
    body = yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100)
    header = (
        f"# T-C42 {ROUND} operator section-override map — derived from the R36 verdict record\n"
        f"# (the loop's TENTH R1-shaped repair round and the FOURTH over the promoted\n"
        f"# surface; 1 verdicted DEMOTE_TO_WORKLIST [HUMAN_VALIDATED, the R30 grouping-batch\n"
        f"# shape, the loop's SIXTH DEMOTE — the R35 fresh REJECT adjudicated: the forward\n"
        f"# express-one-number-as-a-percentage surface pinned at 1.6F 'use reverse\n"
        f"# percentages' with NO canonical target in the ratified 188]; ZERO REATTRIBUTEs;\n"
        f"# ZERO sign-offs owed; ZERO retain rulings; the basic-percentages corpus anchor\n"
        f"# STANDS at the untouched join layer). Written ONLY by\n"
        f"# scripts/c42_r36_override_projection.py; hand-editing is forbidden.\n"
    )
    emit(OVERRIDES_OUT, header + body, "override map", 1)

    # ---- 2. the promotions amendment -------------------------------------------
    adoc = {
        "schema": "c42-r31-promotions-amendment/1.0",
        "task": TASK,
        "round": ROUND,
        "generated": DATE,
        "source": ("scripts/c42_r36_repair_verdicts.yaml "
                   "(section_overrides)"),
        "base_file": "scripts/c42_r5_promotions.yaml",
        "base_file_sha256_16": "9bad739bd79e5899",
        "base_file_untouched": True,
        "prior_amendments": [
            "scripts/c42_r26_promotions_amendment.yaml",
            "scripts/c42_r30_promotions_amendment.yaml",
            "scripts/c42_r33_promotions_amendment.yaml",
        ],
        "contract": (
            "consumed fail-closed by the R37-shaped substrate re-build's "
            "promotions re-application AFTER the R5 file is loaded and AFTER "
            "the R26+R30+R33 amendments' outstanding effects are carried "
            "(those are already LANDED state in the R36 baseline store; the "
            "R36 amendment acts on the re-applied set): every excluded entry "
            "removes one row from the re-applied promotion set (the DEMOTE "
            "lands unresolved-span via the c40 DEMOTE convention, NOT "
            "re-promoted; chunk identity intact — the W3 invariant). ZERO "
            "supersedes_code entries and ZERO added entries this round — the "
            "supersedes/additions capabilities are present in the schema and "
            "UNUSED (no sign-offs are owed: the R30 round discharged all 4 "
            "H3 holds of record). The re-applied promotion count becomes 830 "
            "(831 - 1 exclusion = 827 from the R5 chain + 3 R30-added "
            "sign-offs). The R5 file itself stays BYTE-UNTOUCHED (the P5 "
            "convention — landed records never edited); this amendment is "
            "the dated record of the R36 operator-fired adjudication and "
            "remains reviewable and reversible by the operator before the "
            "R37-shaped lane fires."),
        "supersedes_code": [],
        "excluded": [
            {
                "mapping_id": MOVER_ID,
                "note_path": NOTE_PATH,
                "chunk_ordinal": MOVER_ORD,
                "pinned_code": MOVER_CODE,
                "disposition": "DEMOTE_TO_WORKLIST",
            },
        ],
        "added": [],
        "derived_census_projected": {
            "re_applied_promotions": 830,
            "re_applied_composition": ("827 from the R5 chain [832 - 1 R26 "
                                       "exclusion - 3 R30 exclusions - 1 R36 "
                                       "exclusion] + 3 R30-added sign-offs"),
            "covered_codes": "133 -> 133",
            "coverage_gained": [],
            "coverage_lost": [],
            "uncovered_sp": "55 -> 55",
            "resolved_defer_rows": [],
            "anchored": "835 -> 834 (830 HUMAN_VALIDATED + 4 anchored SUGGESTED)",
            "unresolved_span": "27 -> 28 (the R36 DEMOTE)",
            "store_rows": "917 -> 917 (the DEMOTE row re-keys into the "
                          "worklist — chunk identity intact, the W3 "
                          "invariant; no row vanishes)",
            "per_code": ("4MA1-1.6F anchored 6 -> 5 (the reverse-percentages "
                         "trio ords 0/1/2 + basic-percentages ords 0/3 "
                         "remain; the demoted ord 4 re-keys to "
                         f"{PROJECTED_DEMOTE_ID} in the worklist)"),
        },
        "caveat": (
            "PROJECTED from verified facts, ASSERTED NOWHERE — every count "
            "lands at the R37-shaped rebuild lane (which computes its own "
            "delta proofs, the R24 R5-gate convention) and the re-gate lane "
            "after it; the DC-R24-01 discipline (compute, never assert "
            "coverage) is in force"),
    }
    abody = yaml.safe_dump(adoc, allow_unicode=True, sort_keys=False, width=100)
    aheader = (
        f"# T-C42 {ROUND} promotions amendment — derived from the R36 verdict record\n"
        f"# (the loop's FOURTH promotions-affecting repair record and the FIRST\n"
        f"# exclusion-ONLY one: 0 code supersedes + 1 exclusion + 0 additions — the\n"
        f"# R30 additions mechanism present and UNUSED, no sign-offs owed; the R5\n"
        f"# promotions file stays byte-untouched per the P5 convention). Written\n"
        f"# ONLY by scripts/c42_r36_override_projection.py; hand-editing is forbidden.\n"
    )
    emit(AMENDMENT_OUT, aheader + abody, "promotions amendment", 1)

    print(f"  basic-percentages::4 {MOVER_CODE} -> (worklist) "
          f"[DEMOTE_TO_WORKLIST, projected re-key {PROJECTED_DEMOTE_ID}]")
    print("  RETAIN (zero-movement continuity): none fired beyond the "
          "single row")
    return 0


if __name__ == "__main__":
    sys.exit(main())
