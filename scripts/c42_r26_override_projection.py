#!/usr/bin/env python3
"""c42_r26_override_projection.py — T-C42 R26 derived projection emitter.

The R26 lane is the SEVENTH R1-shaped repair round (scope §7 loop), fired by
the operator directive "(a) an R26-shaped repair over the 4-row inventory"
(2026-10-04, zai-web, gateway trace 1a10641c64283c99) over the R25 re-gate's
4-row defect inventory — the loop's FIRST repair round over the promoted
surface.

Like R18/R22 (and unlike R6/R10/R14), the round has ZERO id-level rows and
ZERO note-level re-points (all four R25 note-level joins STAND), so there is
NO resolution-file amendment this round: the resolution file stays
byte-untouched and the round's entire state carrier is TWofold, both derived
DETERMINISTICALLY from the operator-owned verdict record
scripts/c42_r26_repair_verdicts.yaml and emitted here (idempotent,
byte-identical re-runs):

  1. the next-re-build-facing override map
     scripts/c42_section_overrides_r26.yaml (schema
     c42-r28-section-overrides/1.0, the consuming-lane convention: R1 map ->
     r3, R6 map -> r8, R10 map -> r12, R14 map -> r16, R18 map -> r20,
     R22 map -> r24, R26 map -> r28) carrying:
       - 3 verdicted REATTRIBUTE entries:
           types-of-number::1              REATTRIBUTE 1.1G -> 1.1A
           introduction-to-vectors::3      REATTRIBUTE 5.1D -> 5.1C
           drawing-straight-line-graphs::4 REATTRIBUTE 3.3F -> 3.3H
       - 1 verdicted DEMOTE_TO_WORKLIST entry (the loop's fourth DEMOTE,
         first of a promoted row):
           factorising-by-grouping::2      DEMOTE (no canonical 188 target)
       - NO extension entries this round (every same-class candidate sits on
         the R5-PROMOTED surface and is recorded as a census remark for the
         operator, NOT adjudicated: no agent-side movement of promoted rows
         beyond the fired inventory)
       - the four note-level STANDING adjudications (all joins stand)
       - the standing heading-only convention reference (the 4 store H3 HOLD
         rows listed, no new decision — the per-row operator sign-off was
         not given)
       - the census remarks and the (empty) dated-corrections block

  2. the PROMOTIONS AMENDMENT — the R26 novelty record
     scripts/c42_r26_promotions_amendment.yaml (schema
     c42-r28-promotions-amendment/1.0) carrying:
       - 3 supersedes_code entries (the promoted rows' pinned codes move
         with their re-attributions — the promotion judged the sections'
         teaching value, the repair corrects their codes)
       - 1 excluded entry (the DEMOTE row leaves the promoted set entirely:
         832 -> 831 re-applied promotions at the R28-shaped rebuild)
       - the derived census projections (PROJECTED, ASSERTED NOWHERE — the
         DC-R24-01 discipline)
     The R5 promotions file itself stays BYTE-UNTOUCHED (the P5 convention:
     landed records never edited; corrections land as dated records of their
     own). Wiring the amendment into the rebuild tool's promotions
     re-application is the R28-shaped rebuild lane's job (the R24
     tool-bump precedent).

Consumed fail-closed by scripts/c40_maths_a_chunk_sp_substrate.py at the
NEXT substrate re-build (the R28-shaped lane) TOGETHER WITH the R1/R6/R10/
R14/R18/R22 maps — wiring this map into the tool is the re-build lane's job
(the R12/R16/R20/R24 precedent): an override naming a code outside the
ratified 188 fails the build; current_code must equal the join-derived code;
REATTRIBUTE targets must sit in the ratified registry; DEMOTE entries carry
override_code null and land the chunk unresolved-span (the c40 R10/R14/R18
convention); applied rows carry provenance.override with the map sha.

Usage: python3 scripts/c42_r26_override_projection.py
"""
import json
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
VERDICTS = REPO / "scripts/c42_r26_repair_verdicts.yaml"
OVERRIDES_OUT = REPO / "scripts/c42_section_overrides_r26.yaml"
AMENDMENT_OUT = REPO / "scripts/c42_r26_promotions_amendment.yaml"
PROMOTIONS = REPO / "scripts/c42_r5_promotions.yaml"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
REGISTRY = REPO / "graph/igcse-maths-a/specification_points.yaml"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"

TASK = "T-C42"
ROUND = "R26"
DATE = "2026-10-04"

# (bare code, expected C30 ledger presence) — the A4-analog fact set,
# fail-closed: 1.1G/1.1A/5.1D/5.1C/3.3H/2.2F Higher-only (absent),
# 3.3F a shared-tier row (present, Foundation = conversion graphs)
LEDGER_FACTS = [("1.1G", False), ("1.1A", False), ("5.1D", False),
                ("5.1C", False), ("3.3H", False), ("2.2F", False),
                ("3.3F", True)]


def fail(msg: str) -> None:
    print(f"FAIL-CLOSED: {msg}", file=sys.stderr)
    sys.exit(1)


def emit(path: Path, new_text: str, label: str, n: int) -> None:
    if path.exists():
        old = path.read_text(encoding="utf-8")
        if old != new_text:
            fail(f"{label} exists with different content — refusing to "
                 "overwrite (deterministic regeneration violated)")
        print(f"c42_r26_override_projection: {label} already current "
              f"({n} entries) — idempotent no-op")
        return
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(new_text, encoding="utf-8")
    tmp.replace(path)
    print(f"c42_r26_override_projection: WROTE {path.relative_to(REPO)} "
          f"— {label} ({n} entries)")


def main() -> int:
    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    store = yaml.safe_load(STORE.read_text(encoding="utf-8"))
    reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    points = {p["code"] for p in reg["specification_points"]}
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    led_rows = {r["official_code"]: r for r in ledger["rows"]}
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    promo_pins = {e["row"]["mapping_id"]: e["row"] for e in promo["promotions"]}

    rows_by_id = {r["mapping_id"]: r for r in store["rows"]}
    verdicts = ver["verdicts"] if "verdicts" in ver else ver["section_overrides"]

    # ---- shared fail-closed checks ------------------------------------------
    for bare, expected_present in LEDGER_FACTS:
        if (bare in led_rows) != expected_present:
            fail(f"C30 ledger fact drifted for {bare}: "
                 f"present={bare in led_rows} expected={expected_present}")

    overrides = []
    amendment_supersedes = []
    amendment_excluded = []
    for key, v in sorted(verdicts.items()):
        mid = v["mapping_id"]
        action = v["disposition"]
        srow = rows_by_id.get(mid)
        if srow is None:
            fail(f"verdict row {mid} not found in the live substrate")
        cur = srow["spec_code"]
        if cur != v["current_code"]:
            fail(f"current_code drift for {mid}: store {cur} vs verdict "
                 f"{v['current_code']}")
        if srow.get("validation_status") != "HUMAN_VALIDATED":
            fail(f"row {mid} is not HUMAN_VALIDATED — the R26 inventory is "
                 f"expected to sit on the R5-promoted surface")
        pin = promo_pins.get(mid)
        if pin is None:
            fail(f"row {mid} is not pinned in the R5 promotions file — "
                 f"promoted-row state mismatch")
        if pin.get("spec_code") != cur:
            fail(f"promotions pin drift for {mid}: file {pin.get('spec_code')} "
                 f"vs store {cur}")

        note_slug = key.split("::")[0]
        chunk_ord = int(key.split("::")[1])
        srow_slug = srow["note_path"].rsplit("/", 1)[-1].replace(".json", "")
        if srow_slug != note_slug or srow["chunk"]["ordinal"] != chunk_ord:
            fail(f"note::ordinal identity drift for {mid}: "
                 f"{srow_slug}::{srow['chunk']['ordinal']} vs {key}")

        entry = {
            "note_slug": note_slug,
            "chunk_ordinal": chunk_ord,
            "mapping_id": mid,
            "current_code": cur,
            "provenance_class": "verdicted",
            "action": action,
            "override_code": v.get("override_code"),
            "evidence": (v.get("evidence") or "").strip(),
        }
        if action == "REATTRIBUTE":
            tgt = v["override_code"]
            if tgt not in points:
                fail(f"override target {tgt} outside the ratified 188")
            if tgt == cur:
                fail(f"override target equals current for {mid}")
            amendment_supersedes.append({
                "mapping_id": mid,
                "note_path": srow["note_path"],
                "chunk_ordinal": chunk_ord,
                "pinned_code": cur,
                "amended_code": tgt,
            })
        elif action == "DEMOTE_TO_WORKLIST":
            if v.get("override_code") is not None:
                fail(f"DEMOTE entry with non-null override_code for {mid}")
            amendment_excluded.append({
                "mapping_id": mid,
                "note_path": srow["note_path"],
                "chunk_ordinal": chunk_ord,
                "pinned_code": cur,
                "disposition": "DEMOTE_TO_WORKLIST",
            })
        else:
            fail(f"unexpected action for {mid}: {action}")
        overrides.append(entry)

    n_reattr = sum(1 for e in overrides if e["action"] == "REATTRIBUTE")
    n_demote = sum(1 for e in overrides if e["action"] == "DEMOTE_TO_WORKLIST")
    if len(overrides) != 4 or n_reattr != 3 or n_demote != 1:
        fail(f"expected the 4-row inventory as 3 REATTRIBUTE + 1 DEMOTE, got "
             f"{n_reattr}+{n_demote}")
    if len(amendment_supersedes) != 3 or len(amendment_excluded) != 1:
        fail("promotions amendment shape drifted from the verdict record")

    # ---- 1. the override map -------------------------------------------------
    doc = {
        "schema": "c42-r28-section-overrides/1.0",
        "task": TASK,
        "round": ROUND,
        "generated": DATE,
        "source": ("scripts/c42_r26_repair_verdicts.yaml (section_overrides + "
                   "note_level_adjudications + heading_only_convention + "
                   "census_remarks + promoted_surface_amendment + "
                   "dated_corrections)"),
        "contract": (
            "consumed fail-closed by scripts/c40_maths_a_chunk_sp_substrate.py "
            "at the NEXT substrate re-build (the R28-shaped lane) TOGETHER WITH "
            "scripts/c42_section_overrides.yaml (R1), "
            "scripts/c42_section_overrides_r6.yaml (R6), "
            "scripts/c42_section_overrides_r10.yaml (R10), "
            "scripts/c42_section_overrides_r14.yaml (R14), "
            "scripts/c42_section_overrides_r18.yaml (R18) and "
            "scripts/c42_section_overrides_r22.yaml (R22) — wiring this map "
            "into the tool is the re-build lane's job (the R12/R16/R20/R24 "
            "precedent): an override naming a code outside the ratified 188 "
            "fails the build; current_code must equal the join-derived code; "
            "REATTRIBUTE targets must sit in the ratified registry; DEMOTE "
            "entries carry override_code null and land the chunk "
            "unresolved-span (the R10/R14/R18 convention); applied rows carry "
            "provenance.override with the map sha. NO resolution-file "
            "amendment this round: all four note-level joins STAND, the "
            "resolution file stays byte-untouched (counts 222/214/8). "
            "PROMOTIONS INTERACTION (the R26 novelty — the first repair round "
            "over the promoted surface): the R28-shaped rebuild must consume "
            "scripts/c42_r26_promotions_amendment.yaml in its promotions "
            "re-application — the 3 REATTRIBUTE rows' pinned codes are "
            "superseded to the override codes (they REMAIN in the promoted "
            "set, re-keyed old->new at the rebuild per the R24 id_pairs "
            "convention) and the DEMOTE row is EXCLUDED from the re-applied "
            "set (832 -> 831), landing unresolved-span (23 -> 24) via the c40 "
            "DEMOTE convention; scripts/c42_r5_promotions.yaml itself stays "
            "BYTE-UNTOUCHED (the P5 convention). Coverage projections "
            "(PROJECTED, ASSERTED NOWHERE — the DC-R24-01 discipline): "
            "covered 130 -> 132 (gained 4MA1-1.1A + 4MA1-5.1C, lost none — "
            "every vacated code keeps standing rows, verified row-by-row at "
            "R26), uncovered-SP 58 -> 56 (the 1.1A DEFER row "
            "da25da48e0be5c64 and the 5.1C DEFER row 2332964a4f1b02ca resolve "
            "into anchored rows), anchored 839 -> 838, store rows 920 -> 918"),
        "overrides": overrides,
        "note_level_adjudications": ver["note_level_adjudications"],
        "heading_only_convention": ver["heading_only_convention"],
        "census_remarks": ver["census_remarks"],
        "promoted_surface_amendment": {
            "amendment_file": "scripts/c42_r26_promotions_amendment.yaml",
            "base_file": "scripts/c42_r5_promotions.yaml",
            "base_file_untouched": True,
            "supersedes": len(amendment_supersedes),
            "excluded": len(amendment_excluded),
        },
        "dated_corrections": ver.get("dated_corrections", []),
    }
    body = yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100)
    header = (
        f"# T-C42 {ROUND} operator section-override map — derived from the R26 verdict record\n"
        f"# (the loop's SEVENTH R1-shaped repair round and the FIRST over the promoted\n"
        f"# surface; 3 verdicted REATTRIBUTEs + the loop's fourth DEMOTE — first of a\n"
        f"# promoted row; no extensions, all four note-level joins STANDING). Written ONLY\n"
        f"# by scripts/c42_r26_override_projection.py; hand-editing is forbidden.\n"
    )
    emit(OVERRIDES_OUT, header + body, "override map", len(overrides))

    # ---- 2. the promotions amendment -----------------------------------------
    adoc = {
        "schema": "c42-r28-promotions-amendment/1.0",
        "task": TASK,
        "round": ROUND,
        "generated": DATE,
        "source": "scripts/c42_r26_repair_verdicts.yaml (promoted_surface_amendment)",
        "base_file": "scripts/c42_r5_promotions.yaml",
        "base_file_sha256_16": "9bad739bd79e5899",
        "base_file_untouched": True,
        "contract": (
            "consumed fail-closed by the R28-shaped substrate re-build's "
            "promotions re-application (the c42_r24-shaped lane convention), "
            "AFTER the R5 file is loaded: every supersedes_code entry re-pins "
            "one promoted row's code (identity by mapping_id + note_path + "
            "chunk_ordinal, pinned_code verified against the R5 file BEFORE "
            "the amendment applies — any drift fails the rebuild); the "
            "excluded entry removes one row from the re-applied promotion "
            "set (the DEMOTE row lands unresolved-span via the c40 DEMOTE "
            "convention, NOT re-promoted). The re-applied promotion count "
            "becomes 831 (832 - 1); the 3 superseded rows REMAIN in the "
            "promoted set at their amended codes and re-key old->new at the "
            "rebuild (the R24 id_pairs convention). The R5 file itself stays "
            "BYTE-UNTOUCHED (the P5 convention — landed records never "
            "edited); this amendment is the dated record of the R26 "
            "operator-fired adjudication and remains reviewable and "
            "reversible by the operator before the R28-shaped lane fires. "
            "Wiring this amendment into the rebuild tool is the rebuild "
            "lane's job (the R24 tool-bump precedent)."),
        "supersedes_code": amendment_supersedes,
        "excluded": amendment_excluded,
        "derived_census_projected": {
            "re_applied_promotions": 831,
            "covered_codes": "130 -> 132",
            "coverage_gained": ["4MA1-1.1A", "4MA1-5.1C"],
            "coverage_lost": [],
            "uncovered_sp": "58 -> 56",
            "resolved_defer_rows": ["da25da48e0be5c64", "2332964a4f1b02ca"],
            "anchored": "839 -> 838 (831 HUMAN_VALIDATED + 7 anchored SUGGESTED)",
            "unresolved_span": "23 -> 24 (the DEMOTE row)",
            "store_rows": ("920 -> 918 (the 2 resolved DEFER rows vanish; "
                           "the DEMOTE row re-keys into the worklist)"),
        },
        "caveat": (
            "PROJECTED from verified facts, ASSERTED NOWHERE — every count "
            "lands at the R28-shaped rebuild lane (which computes its own "
            "delta proofs, the R24 R5-gate convention) and the re-gate lane "
            "after it; the DC-R24-01 discipline (compute, never assert "
            "coverage) is in force"),
    }
    abody = yaml.safe_dump(adoc, allow_unicode=True, sort_keys=False, width=100)
    aheader = (
        f"# T-C42 {ROUND} promotions amendment — derived from the R26 verdict record\n"
        f"# (the loop's FIRST promotions-affecting repair record: 3 code supersedes +\n"
        f"# 1 exclusion; the R5 promotions file stays byte-untouched per the P5\n"
        f"# convention). Written ONLY by scripts/c42_r26_override_projection.py;\n"
        f"# hand-editing is forbidden.\n"
    )
    emit(AMENDMENT_OUT, aheader + abody, "promotions amendment",
         len(amendment_supersedes) + len(amendment_excluded))

    for o in overrides:
        tgt = o["override_code"] if o["override_code"] else "(worklist)"
        print(f"  {o['note_slug']}::{o['chunk_ordinal']} "
              f"{o['current_code']} -> {tgt}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
