#!/usr/bin/env python3
"""c42_r33_override_projection.py — T-C42 R33 derived projection emitter.

The R33 lane is the NINTH R1-shaped repair round (scope §7 loop), fired by
the operator directive "Start repair" (2026-10-12, zai-web, gateway trace
1a1311195c15d3cd) over the R32 validation re-gate's defect inventory — the
loop's THIRD repair round over the promoted surface. The inventory is the
R32 fresh judgment record's own return: ONE fresh REJECT
(rounding-and-estimation::8, the estimate-evaluation surface joined at
1.8B) plus the sibling exposure its root disclosed (ords 5/6/7 of the same
note, the estimation half riding the ONE spec_point anchor).

The round has ZERO id-level rows and ZERO note-level re-points (both
standing note-level anchors — the note's own 1.8B anchor and the
related-calculations 1.8D R10 STANDING join — remain STANDING at the
untouched join layer; the resolution file stays byte-untouched), so the
round's entire state carrier is TWofold, both derived DETERMINISTICALLY
from the operator-owned verdict record
scripts/c42_r33_repair_verdicts.yaml and emitted here (idempotent,
byte-identical re-runs):

  1. the next-re-build-facing override map
     scripts/c42_section_overrides_r33.yaml (schema
     c42-r28-section-overrides/1.0, the consuming-lane convention) carrying:
       - 3 verdicted REATTRIBUTE entries (ALL HUMAN_VALIDATED — the
         supersedes shape, zero SUGGESTED riders this round):
           rounding-and-estimation::6   1.8B -> 1.8D   (HV, the purpose)
           rounding-and-estimation::7   1.8B -> 1.8D   (HV, the method)
           rounding-and-estimation::8   1.8B -> 1.8D   (HV, the FIRED defect)
       - ZERO DEMOTE entries (no canonical-target absence arises: the R18
         no-target class is not implicated)
       - the 2 retain rulings are RECORDED here as their own block (the
         honest-split ord 5 ruling + the not-fired ord 0 continuity; retain
         = zero movement)
       - the note-level scoping note (the 1.8B anchor STANDS with the
         SPLIT scoping — the loop's first split-note ruling; no new
         c40-pinned adjudications)
       - the census remarks (the promoted-surface interaction — supersedes
         ONLY, zero exclusions/additions; the post-move per-code censuses)
         and the (empty) dated-corrections block

  2. the PROMOTIONS AMENDMENT — the supersedes-only record
     scripts/c42_r33_promotions_amendment.yaml (schema
     c42-r31-promotions-amendment/1.0 — the R30 schema, unchanged: the
     additions capability is present and UNUSED this round) carrying:
       - 3 supersedes_code entries (promoted rows REMAIN promoted at their
         amended codes)
       - ZERO excluded entries
       - ZERO added entries (no sign-offs are owed — the R30 round
         discharged all 4 H3 holds of record)
       - the derived census projections (PROJECTED, ASSERTED NOWHERE — the
         DC-R24-01 discipline): re-applied promotions 831 -> 831, covered
         133 -> 133, anchored 835 -> 835, unresolved-span 27 -> 27, store
         rows 917 -> 917; per-code 1.8B 9 -> 6 and 1.8D 3 -> 6
     The R5 promotions file itself stays BYTE-UNTOUCHED (the P5 convention).

Consumed fail-closed by the c40-shaped substrate tool (TOOL_VERSION 2.7.0)
at the NEXT substrate re-build (the R34-shaped lane) TOGETHER WITH the
R1/R6/R10/R14/R18/R22/R26/R30 maps — wiring the carriers into the tool is
the re-build lane's job (the R12/R16/R20/R24/R28/R31 precedent).

Usage: python3 scripts/c42_r33_override_projection.py
"""
import json
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
VERDICTS = REPO / "scripts/c42_r33_repair_verdicts.yaml"
OVERRIDES_OUT = REPO / "scripts/c42_section_overrides_r33.yaml"
AMENDMENT_OUT = REPO / "scripts/c42_r33_promotions_amendment.yaml"
PROMOTIONS = REPO / "scripts/c42_r5_promotions.yaml"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
REGISTRY = REPO / "graph/igcse-maths-a/specification_points.yaml"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"

TASK = "T-C42"
ROUND = "R33"
DATE = "2026-10-12"

# (bare code, expected C30 ledger presence) — fail-closed fact set:
# 1.8B and 1.8D are BOTH absent (Higher-only / single-tier rows) — the
# tier-artifact escape is closed for this round's every verdict.
LEDGER_FACTS = [("1.8B", False), ("1.8D", False)]

# the ratified wordings the verdicts cite — fail-closed registry pins:
REGISTRY_WORDINGS = {
    "4MA1-1.8B": "round to a given number of significant figures or decimal places",
    "4MA1-1.8D": "use estimation to evaluate approximations to numerical calculations",
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
        print(f"c42_r33_override_projection: {label} already current "
              f"({n} entries) — idempotent no-op")
        return
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(new_text, encoding="utf-8")
    tmp.replace(path)
    print(f"c42_r33_override_projection: WROTE {path.relative_to(REPO)} "
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

    # ---- shared fail-closed checks ------------------------------------------
    for bare, expected_present in LEDGER_FACTS:
        if (bare in led_rows) != expected_present:
            fail(f"C30 ledger fact drifted for {bare}: "
                 f"present={bare in led_rows} expected={expected_present}")
    for code, want in REGISTRY_WORDINGS.items():
        got = (points.get(code) or {}).get("official_wording")
        if got != want:
            fail(f"registry wording drifted for {code}: {got!r}")

    overrides = []
    amendment_supersedes = []
    amendment_excluded = []
    for key, v in sorted(ver["section_overrides"].items()):
        mid = v["mapping_id"]
        action = v["disposition"]
        srow = rows_by_id.get(mid)
        if srow is None:
            fail(f"verdict row {mid} not found in the live substrate")
        cur = srow["spec_code"]
        if cur != v["current_code"]:
            fail(f"current_code drift for {mid}: store {cur} vs verdict "
                 f"{v['current_code']}")
        status = srow.get("validation_status")
        note_slug = key.split("::")[0]
        chunk_ord = int(key.split("::")[1])
        srow_slug = srow["note_path"].rsplit("/", 1)[-1].replace(".json", "")
        if srow_slug != note_slug or srow["chunk"]["ordinal"] != chunk_ord:
            fail(f"note::ordinal identity drift for {mid}: "
                 f"{srow_slug}::{srow['chunk']['ordinal']} vs {key}")
        if srow["note_path"] != ("notes/1-numbers-and-the-number-system/"
                                 "rounding-estimation-and-bounds/"
                                 "rounding-and-estimation.json"):
            fail(f"note_path drift for {mid}: {srow['note_path']}")

        if action == "REATTRIBUTE":
            tgt = v["override_code"]
            if tgt not in points:
                fail(f"override target {tgt} outside the ratified 188")
            if tgt == cur:
                fail(f"override target equals current for {mid}")
            if tgt != "4MA1-1.8D":
                fail(f"override target drift for {mid}: {tgt} — the R33 "
                     f"inventory is the 1.8B -> 1.8D re-home batch")
            if status == "HUMAN_VALIDATED":
                pin = promo_pins.get(mid)
                if pin is None:
                    fail(f"promoted row {mid} is not pinned in the R5 file")
                if pin.get("spec_code") != cur:
                    fail(f"promotions pin drift for {mid}: "
                         f"file {pin.get('spec_code')} vs store {cur}")
                if pin.get("note_path") != srow["note_path"] or \
                        pin.get("chunk_ordinal") != chunk_ord:
                    fail(f"promotions pin identity drift for {mid}")
                amendment_supersedes.append({
                    "mapping_id": mid,
                    "note_path": srow["note_path"],
                    "chunk_ordinal": chunk_ord,
                    "pinned_code": cur,
                    "amended_code": tgt,
                })
            elif status == "SUGGESTED":
                if mid in promo_pins:
                    fail(f"SUGGESTED row {mid} unexpectedly pinned in the R5 "
                         f"file")
            else:
                fail(f"unexpected validation_status for {mid}: {status}")
        elif action == "DEMOTE_TO_WORKLIST":
            fail(f"unexpected DEMOTE entry for {mid} — the R33 inventory "
                 f"carries zero DEMOTEs (no canonical-target absence)")
        else:
            fail(f"unexpected action for {mid}: {action}")
        overrides.append({
            "note_slug": note_slug,
            "chunk_ordinal": chunk_ord,
            "mapping_id": mid,
            "current_code": cur,
            "provenance_class": "verdicted",
            "action": action,
            "override_code": v.get("override_code"),
            "evidence": (v.get("evidence") or "").strip(),
        })

    n_reattr = sum(1 for e in overrides if e["action"] == "REATTRIBUTE")
    n_reattr_hv = sum(1 for e in overrides if e["action"] == "REATTRIBUTE"
                      and rows_by_id[e["mapping_id"]]["validation_status"]
                      == "HUMAN_VALIDATED")
    if len(overrides) != 3 or n_reattr != 3:
        fail(f"expected the 3-row inventory as 3 REATTRIBUTE, got "
             f"{len(overrides)} entries / {n_reattr} REATTRIBUTE")
    if n_reattr_hv != 3:
        fail(f"expected 3 HUMAN_VALIDATED movers, got {n_reattr_hv}")
    if len(amendment_supersedes) != 3 or len(amendment_excluded) != 0:
        fail("promotions amendment shape drifted from the verdict record "
             "(3 HV supersedes + 0 exclusions + 0 additions expected — "
             "supersedes only)")

    # ---- the zero sign-offs fact --------------------------------------------
    if "h3_signoffs" in ver:
        fail("the R33 verdict record carries no h3_signoffs block — the R30 "
             "round discharged all 4 H3 holds of record")
    moved_map_ids = {e["mapping_id"] for e in overrides}

    retain_rulings = ver["retain_rulings"]
    retains = {k: v for k, v in retain_rulings.items() if k != "contract"}
    if len(retains) != 2:
        fail(f"expected exactly 2 retain rulings (ord 5 honest-split / "
             f"ord 0 not-fired continuity), got {len(retains)}")
    for key, r in retains.items():
        mid = r["mapping_id"]
        srow = rows_by_id.get(mid)
        if srow is None or srow["spec_code"] != r["code"]:
            fail(f"retain ruling row drift for {key}")
        if srow.get("validation_status") != "HUMAN_VALIDATED":
            fail(f"retain ruling row {mid} is not HUMAN_VALIDATED")
        if r["ruling"] != "RETAIN":
            fail(f"unexpected retain ruling for {key}: {r['ruling']}")
        if mid in {e["mapping_id"] for e in amendment_supersedes} or \
                mid in {e["mapping_id"] for e in amendment_excluded} or \
                mid in moved_map_ids:
            fail(f"retain ruling row {mid} also carries a moving disposition "
                 f"— retain rows must be zero-movement")
    expected_retains = {"rounding-and-estimation::5": "4MA1-1.8B",
                        "rounding-and-estimation::0": "4MA1-1.8B"}
    if {k: v["code"] for k, v in retains.items()} != expected_retains:
        fail("the retain set drifted from the fired-inventory shape "
             "(ord 5 + ord 0, both at 1.8B)")

    # the not-fired rows' continuity: ords 1-4 untouched, zero movement
    for ordn, mid in ((1, "ea1e00fd2aa484ad"), (2, "ba9cb33680c338a4"),
                      (3, "e7b9b7d3cbbdbbd6"), (4, "a1510bc4ed0196b2")):
        if mid in moved_map_ids:
            fail(f"rounding-and-estimation::{ordn} ({mid}) carries an "
                 f"override — the rounding-half method rows are NOT in the "
                 f"fired inventory and must not move")

    # ---- 1. the override map -------------------------------------------------
    doc = {
        "schema": "c42-r28-section-overrides/1.0",
        "task": TASK,
        "round": ROUND,
        "generated": DATE,
        "source": ("scripts/c42_r33_repair_verdicts.yaml (section_overrides "
                   "+ retain_rulings + note_level_scoping + census_remarks + "
                   "dated_corrections)"),
        "contract": (
            "consumed fail-closed by the c40-shaped substrate tool "
            "(TOOL_VERSION 2.7.0) at the NEXT substrate re-build (the "
            "R34-shaped lane) TOGETHER WITH scripts/c42_section_overrides.yaml "
            "(R1), scripts/c42_section_overrides_r6.yaml (R6), "
            "scripts/c42_section_overrides_r10.yaml (R10), "
            "scripts/c42_section_overrides_r14.yaml (R14), "
            "scripts/c42_section_overrides_r18.yaml (R18), "
            "scripts/c42_section_overrides_r22.yaml (R22), "
            "scripts/c42_section_overrides_r26.yaml (R26) and "
            "scripts/c42_section_overrides_r30.yaml (R30) — an override "
            "naming a code outside the ratified 188 fails the build; "
            "current_code must equal the join-derived code; REATTRIBUTE "
            "targets must sit in the ratified registry; applied rows carry "
            "provenance.override with the map sha. NO resolution-file "
            "amendment this round: all standing note-level joins remain "
            "STANDING at the untouched join layer (the note's own 1.8B "
            "anchor spcpt_p8zkdCF8QVvDZyVX and the related-calculations 1.8D "
            "anchor spcpt_crKbmb6wVjM4yPJh both stand — the SPLIT scoping "
            "note), the resolution file stays byte-untouched (counts "
            "222/214/8). PROMOTIONS INTERACTION (the R26/R30 shape): the "
            "R34-shaped rebuild must consume "
            "scripts/c42_r33_promotions_amendment.yaml in its promotions "
            "re-application — the 3 HV REATTRIBUTE rows' pinned codes are "
            "superseded to the override codes (they REMAIN in the promoted "
            "set, re-keyed old->new per the R24 id_pairs convention); ZERO "
            "exclusions and ZERO additions (the R30 additions mechanism "
            "unused — no sign-offs owed). The 2 retain rulings ride NO "
            "carrier entry (zero movement). "
            "scripts/c42_r5_promotions.yaml itself stays BYTE-UNTOUCHED (the "
            "P5 convention). Coverage projections (PROJECTED, ASSERTED "
            "NOWHERE — the DC-R24-01 discipline): covered 133 -> 133 (1.8B "
            "keeps ords 0-5; 1.8D already covered via the R10 join — no "
            "gain, no loss), anchored 835 -> 835 (831 HUMAN_VALIDATED + 4 "
            "anchored SUGGESTED), unresolved-span 27 -> 27, uncovered-SP 55 "
            "-> 55, store rows 917 -> 917; per-code 1.8B anchored 9 -> 6 and "
            "1.8D anchored 3 -> 6"),
        "overrides": overrides,
        "retain_rulings": ver["retain_rulings"],
        "note_level_scoping": ver["note_level_scoping"],
        "census_remarks": ver["census_remarks"],
        "promoted_surface_amendment": {
            "amendment_file": "scripts/c42_r33_promotions_amendment.yaml",
            "base_file": "scripts/c42_r5_promotions.yaml",
            "base_file_untouched": True,
            "supersedes": len(amendment_supersedes),
            "excluded": len(amendment_excluded),
            "added": 0,
        },
        "dated_corrections": ver.get("dated_corrections", []),
    }
    body = yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100)
    header = (
        f"# T-C42 {ROUND} operator section-override map — derived from the R33 verdict record\n"
        f"# (the loop's NINTH R1-shaped repair round and the THIRD over the promoted\n"
        f"# surface; 3 verdicted REATTRIBUTEs [all HUMAN_VALIDATED, the supersedes shape]\n"
        f"# carrying the R32 defect inventory's 1.8B -> 1.8D re-home batch; ZERO DEMOTEs;\n"
        f"# ZERO sign-offs owed; 2 retain rulings incl. the loop's first SPLIT-note\n"
        f"# scoping; all standing note-level joins STANDING at the untouched join layer).\n"
        f"# Written ONLY by scripts/c42_r33_override_projection.py; hand-editing is\n"
        f"# forbidden.\n"
    )
    emit(OVERRIDES_OUT, header + body, "override map", len(overrides))

    # ---- 2. the promotions amendment -----------------------------------------
    adoc = {
        "schema": "c42-r31-promotions-amendment/1.0",
        "task": TASK,
        "round": ROUND,
        "generated": DATE,
        "source": ("scripts/c42_r33_repair_verdicts.yaml "
                   "(section_overrides)"),
        "base_file": "scripts/c42_r5_promotions.yaml",
        "base_file_sha256_16": "9bad739bd79e5899",
        "base_file_untouched": True,
        "prior_amendments": [
            "scripts/c42_r26_promotions_amendment.yaml",
            "scripts/c42_r30_promotions_amendment.yaml",
        ],
        "contract": (
            "consumed fail-closed by the R34-shaped substrate re-build's "
            "promotions re-application AFTER the R5 file is loaded and AFTER "
            "the R26+R30 amendments' outstanding effects are carried (those "
            "are already LANDED state in the R33 baseline store; the R33 "
            "amendment acts on the re-applied set): every supersedes_code "
            "entry re-pins one promoted row's code (identity by mapping_id + "
            "note_path + chunk_ordinal, pinned_code verified against the R5 "
            "file BEFORE the amendment applies — any drift fails the "
            "rebuild); the supersedes rows REMAIN in the promoted set at "
            "their amended codes and re-key old->new at the rebuild (the "
            "R24 id_pairs convention). ZERO excluded entries and ZERO added "
            "entries this round — the R30 additions mechanism is present in "
            "the schema and UNUSED (no sign-offs are owed: the R30 round "
            "discharged all 4 H3 holds of record). The re-applied promotion "
            "count stays 831. The R5 file itself stays BYTE-UNTOUCHED (the "
            "P5 convention — landed records never edited); this amendment "
            "is the dated record of the R33 operator-fired adjudication and "
            "remains reviewable and reversible by the operator before the "
            "R34-shaped lane fires."),
        "supersedes_code": amendment_supersedes,
        "excluded": amendment_excluded,
        "added": [],
        "derived_census_projected": {
            "re_applied_promotions": 831,
            "re_applied_composition": ("828 from the R5 chain + 3 R30-added "
                                       "sign-offs, UNCHANGED in count; the 3 "
                                       "R33 movers re-pin within the set"),
            "covered_codes": "133 -> 133",
            "coverage_gained": [],
            "coverage_lost": [],
            "uncovered_sp": "55 -> 55",
            "resolved_defer_rows": [],
            "anchored": "835 -> 835 (831 HUMAN_VALIDATED + 4 anchored SUGGESTED)",
            "unresolved_span": "27 -> 27",
            "store_rows": "917 -> 917 (REATTRIBUTE re-keys only — no row "
                          "vanishes, no row lands)",
            "per_code": ("1.8B anchored 9 -> 6 (the rounding half keeps "
                         "ords 0-5); 1.8D anchored 3 -> 6 (the R10 join "
                         "rows + the re-homed estimation trio ords 6/7/8)"),
        },
        "caveat": (
            "PROJECTED from verified facts, ASSERTED NOWHERE — every count "
            "lands at the R34-shaped rebuild lane (which computes its own "
            "delta proofs, the R24 R5-gate convention) and the re-gate lane "
            "after it; the DC-R24-01 discipline (compute, never assert "
            "coverage) is in force"),
    }
    abody = yaml.safe_dump(adoc, allow_unicode=True, sort_keys=False, width=100)
    aheader = (
        f"# T-C42 {ROUND} promotions amendment — derived from the R33 verdict record\n"
        f"# (the loop's THIRD promotions-affecting repair record and the FIRST\n"
        f"# supersedes-ONLY one: 3 code supersedes + 0 exclusions + 0 additions —\n"
        f"# the R30 additions mechanism present and UNUSED, no sign-offs owed; the\n"
        f"# R5 promotions file stays byte-untouched per the P5 convention). Written\n"
        f"# ONLY by scripts/c42_r33_override_projection.py; hand-editing is forbidden.\n"
    )
    emit(AMENDMENT_OUT, aheader + abody, "promotions amendment",
         len(amendment_supersedes) + len(amendment_excluded))

    for o in overrides:
        tgt = o["override_code"] if o["override_code"] else "(worklist)"
        print(f"  {o['note_slug']}::{o['chunk_ordinal']} "
              f"{o['current_code']} -> {tgt}")
    for k in sorted(retains):
        print(f"  RETAIN {k} {retains[k]['code']} (zero movement)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
