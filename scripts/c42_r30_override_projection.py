#!/usr/bin/env python3
"""c42_r30_override_projection.py — T-C42 R30 derived projection emitter.

The R30 lane is the EIGHTH R1-shaped repair round (scope §7 loop), fired by
the operator directive "Fix all of these yourself. Validate by yourself."
(2026-10-12, zai-web, gateway trace 1a130272fc8acc11) over the R29 re-gate's
NEXT-OPERATOR-DECISIONS menu — the loop's SECOND repair round over the
promoted surface and the FIRST to exercise the R5 apply record's own per-row
H3 sign-off mechanism (the directive delegated the menu's per-item rulings as
OPERATOR-DELEGATE verdicts, the R26 precedent shape).

The round has ZERO id-level rows and ZERO note-level re-points (all standing
note-level joins remain STANDING at the untouched join layer; the resolution
file stays byte-untouched), so the round's entire state carrier is TWofold,
both derived DETERMINISTICALLY from the operator-owned verdict record
scripts/c42_r30_repair_verdicts.yaml and emitted here (idempotent,
byte-identical re-runs):

  1. the next-re-build-facing override map
     scripts/c42_section_overrides_r30.yaml (schema
     c42-r28-section-overrides/1.0, the consuming-lane convention: ... R26
     map -> r28, R30 map -> r31) carrying:
       - 6 verdicted REATTRIBUTE entries:
           equations-and-problem-solving::1      4.11C -> 2.7C   (HV)
           equations-and-problem-solving::2      4.11C -> 2.7C   (HV)
           equations-and-problem-solving::0      4.11C -> 2.7C   (HV)
           3d-pythagoras-and-trigonometry::3     4.8D  -> 4.8F   (HV)
           drawing-straight-line-graphs::5       3.3F  -> 3.3I   (HV)
           drawing-straight-line-graphs::0       3.3F  -> 3.3I   (SUGGESTED)
       - 3 verdicted DEMOTE_TO_WORKLIST entries (the grouping batch — the
         loop's FIFTH DEMOTE as a 3-row batch, all promoted rows):
           factorising-by-grouping::0/::1/::3    2.2F -> unresolved-span
       - the 2 retain rulings and the 3 H3 sign-offs are RECORDED here as
         their own blocks (retain = zero movement; sign-offs land via the
         amendment's ADDED block, not the map)
       - the note-level scoping notes (the 4.11C and 3.3F joins STAND with
         updated scoping; no new c40-pinned adjudications)
       - the census remarks (the rational/irrational gap CLOSED as a recorded
         decision; the promoted-surface interaction; the 4.8D post-move
         census) and the (empty) dated-corrections block

  2. the PROMOTIONS AMENDMENT — the R30 novelty record
     scripts/c42_r30_promotions_amendment.yaml (schema
     c42-r31-promotions-amendment/1.0 — the additions-capable bump of
     c42-r28-promotions-amendment/1.0) carrying:
       - 5 supersedes_code entries (promoted rows REMAIN promoted at their
         amended codes)
       - 3 excluded entries (the grouping batch LEAVES the promoted set)
       - 3 added entries (the loop's FIRST promotions ADDITIONS — the H3
         sign-off rows JOIN the promoted set under the R5 apply record's own
         per-row sign-off mechanism, authored in the R5 entry shape)
       - the derived census projections (PROJECTED, ASSERTED NOWHERE — the
         DC-R24-01 discipline): re-applied promotions 831 -> 831 (828 from
         the R5 chain + 3 added), covered 132 -> 133, uncovered-SP 56 -> 55,
         anchored 838 -> 835, unresolved-span 24 -> 27, store rows 918 -> 917
     The R5 promotions file itself stays BYTE-UNTOUCHED (the P5 convention).

Consumed fail-closed by the c40-shaped substrate tool (TOOL_VERSION 2.7.0)
at the NEXT substrate re-build (the R31-shaped lane) TOGETHER WITH the
R1/R6/R10/R14/R18/R22/R26 maps — wiring the carriers into the tool is the
re-build lane's job (the R12/R16/R20/R24/R28 precedent).

Usage: python3 scripts/c42_r30_override_projection.py
"""
import json
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
VERDICTS = REPO / "scripts/c42_r30_repair_verdicts.yaml"
OVERRIDES_OUT = REPO / "scripts/c42_section_overrides_r30.yaml"
AMENDMENT_OUT = REPO / "scripts/c42_r30_promotions_amendment.yaml"
PROMOTIONS = REPO / "scripts/c42_r5_promotions.yaml"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
REGISTRY = REPO / "graph/igcse-maths-a/specification_points.yaml"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"

TASK = "T-C42"
ROUND = "R30"
DATE = "2026-10-12"

# (bare code, expected C30 ledger presence) — fail-closed fact set:
# absent (Higher-only / single-tier rows): 2.7C 4.11C 4.8D 4.8F 3.3I 2.2F 1.7B 6.3J 5.1D
# present (shared-tier rows with the cited Foundation wordings): 3.3F 2.2C
LEDGER_FACTS = [("2.7C", False), ("4.11C", False), ("4.8D", False),
                ("4.8F", False), ("3.3I", False), ("2.2F", False),
                ("1.7B", False), ("6.3J", False), ("5.1D", False),
                ("3.3F", True), ("2.2C", True)]
LEDGER_FOUNDATION_TEXTS = {"3.3F": "draw and interpret straight line conversion graphs",
                           "2.2C": "multiply a single term over a bracket"}

SIGN_OFF_SOURCE = "r30-operator-signoff"


def fail(msg: str) -> None:
    print(f"FAIL-CLOSED: {msg}", file=sys.stderr)
    sys.exit(1)


def emit(path: Path, new_text: str, label: str, n: int) -> None:
    if path.exists():
        old = path.read_text(encoding="utf-8")
        if old != new_text:
            fail(f"{label} exists with different content — refusing to "
                 "overwrite (deterministic regeneration violated)")
        print(f"c42_r30_override_projection: {label} already current "
              f"({n} entries) — idempotent no-op")
        return
    tmp = path.with_name(path.name + ".tmp")
    tmp.write_text(new_text, encoding="utf-8")
    tmp.replace(path)
    print(f"c42_r30_override_projection: WROTE {path.relative_to(REPO)} "
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

    # ---- shared fail-closed checks ------------------------------------------
    for bare, expected_present in LEDGER_FACTS:
        if (bare in led_rows) != expected_present:
            fail(f"C30 ledger fact drifted for {bare}: "
                 f"present={bare in led_rows} expected={expected_present}")
    for bare, want in LEDGER_FOUNDATION_TEXTS.items():
        got = (led_rows.get(bare) or {}).get("foundation", {}).get("text", "")
        if got != want:
            fail(f"C30 foundation wording drifted for {bare}: {got!r}")

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

        if action == "REATTRIBUTE":
            tgt = v["override_code"]
            if tgt not in points:
                fail(f"override target {tgt} outside the ratified 188")
            if tgt == cur:
                fail(f"override target equals current for {mid}")
            if status == "HUMAN_VALIDATED":
                pin = promo_pins.get(mid)
                if pin is None:
                    fail(f"promoted row {mid} is not pinned in the R5 file")
                if pin.get("spec_code") != cur:
                    fail(f"promotions pin drift for {mid}: "
                         f"file {pin.get('spec_code')} vs store {cur}")
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
            if v.get("override_code") is not None:
                fail(f"DEMOTE entry with non-null override_code for {mid}")
            if status != "HUMAN_VALIDATED":
                fail(f"DEMOTE row {mid} is not HUMAN_VALIDATED — the grouping "
                     f"batch is the promoted same-class set")
            pin = promo_pins.get(mid)
            if pin is None or pin.get("spec_code") != cur:
                fail(f"DEMOTE row {mid} R5 pin missing or drifted")
            amendment_excluded.append({
                "mapping_id": mid,
                "note_path": srow["note_path"],
                "chunk_ordinal": chunk_ord,
                "pinned_code": cur,
                "disposition": "DEMOTE_TO_WORKLIST",
            })
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
    n_demote = sum(1 for e in overrides if e["action"] == "DEMOTE_TO_WORKLIST")
    n_reattr_hv = sum(1 for e in overrides if e["action"] == "REATTRIBUTE"
                      and rows_by_id[e["mapping_id"]]["validation_status"]
                      == "HUMAN_VALIDATED")
    if len(overrides) != 9 or n_reattr != 6 or n_demote != 3:
        fail(f"expected the 9-row inventory as 6 REATTRIBUTE + 3 DEMOTE, got "
             f"{n_reattr}+{n_demote}")
    if len(amendment_supersedes) != 5 or len(amendment_excluded) != 3:
        fail("promotions amendment supersedes/excluded shape drifted from the "
             "verdict record (5 HV supersedes + 3 HV exclusions expected; the "
             "SUGGESTED re-home rides the map alone)")

    # ---- the 3 H3 sign-offs -> amendment ADDED entries -----------------------
    added = []
    for key, s in sorted(ver["h3_signoffs"].items()):
        if key == "contract":
            continue
        mid = s["mapping_id"]
        srow = rows_by_id.get(mid)
        if srow is None:
            fail(f"sign-off row {mid} not found in the live substrate")
        if srow.get("validation_status") != "SUGGESTED":
            fail(f"sign-off row {mid} is not SUGGESTED — the R5-apply hold "
                 f"set rides SUGGESTED until the sign-off lands")
        if srow["spec_code"] != s["code"]:
            fail(f"sign-off code drift for {mid}: store {srow['spec_code']} "
                 f"vs verdict {s['code']}")
        if mid in promo_pins:
            fail(f"sign-off row {mid} already pinned in the R5 file — "
                 f"not an H3 hold")
        note_slug = key.split("::")[0]
        chunk_ord = int(key.split("::")[1])
        if (srow["note_path"].rsplit("/", 1)[-1].replace(".json", "")
                != note_slug or srow["chunk"]["ordinal"] != chunk_ord):
            fail(f"sign-off note::ordinal identity drift for {mid}")
        added.append({
            "row": {
                "mapping_id": mid,
                "spec_code": srow["spec_code"],
                "note_path": srow["note_path"],
                "chunk_ordinal": chunk_ord,
                "heading": srow["chunk"]["heading"],
                "chunk_sha256_16": srow["chunk"]["sha256_16"],
            },
            "verdict": "SIGN_OFF",
            "verdict_source": SIGN_OFF_SOURCE,
            "validated_by": "operator",
            "validated_date": DATE,
            "review_reference": ("graph/reports/"
                                 "C42_R30_RESOLUTION_REPAIR_RECORD.md"),
            "signoff_basis": (s.get("evidence") or "").strip(),
            "tier_wording_source": s.get("tier_wording_source", "store"),
        })
    if len(added) != 3:
        fail(f"expected exactly 3 H3 sign-offs (1.7B / 6.3J / 2.2C), got "
             f"{len(added)} — the 3.3F hold is resolved by re-homing, not "
             f"sign-off")
    signed_ids = {a["row"]["mapping_id"] for a in added}
    moved_map_ids = {e["mapping_id"] for e in overrides}
    if signed_ids & moved_map_ids:
        fail("a sign-off row also carries a map override — disjoint sets "
             "required")
    if {a["row"]["spec_code"] for a in added} != {"4MA1-1.7B", "4MA1-6.3J",
                                                  "4MA1-2.2C"}:
        fail("the signed-off code set drifted from 1.7B / 6.3J / 2.2C")

    retain_rulings = ver["retain_rulings"]
    retains = {k: v for k, v in retain_rulings.items() if k != "contract"}
    if len(retains) != 2:
        fail(f"expected exactly 2 retain rulings (vectors ord 4 / "
             f"factorising-methods), got {len(retains)}")
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
                mid in signed_ids or mid in moved_map_ids:
            fail(f"retain ruling row {mid} also carries a moving disposition "
                 f"— retain rows must be zero-movement")

    # ---- 1. the override map -------------------------------------------------
    doc = {
        "schema": "c42-r28-section-overrides/1.0",
        "task": TASK,
        "round": ROUND,
        "generated": DATE,
        "source": ("scripts/c42_r30_repair_verdicts.yaml (section_overrides "
                   "+ h3_signoffs + retain_rulings + note_level_scoping + "
                   "census_remarks + dated_corrections)"),
        "contract": (
            "consumed fail-closed by the c40-shaped substrate tool "
            "(TOOL_VERSION 2.7.0) at the NEXT substrate re-build (the "
            "R31-shaped lane) TOGETHER WITH scripts/c42_section_overrides.yaml "
            "(R1), scripts/c42_section_overrides_r6.yaml (R6), "
            "scripts/c42_section_overrides_r10.yaml (R10), "
            "scripts/c42_section_overrides_r14.yaml (R14), "
            "scripts/c42_section_overrides_r18.yaml (R18), "
            "scripts/c42_section_overrides_r22.yaml (R22) and "
            "scripts/c42_section_overrides_r26.yaml (R26) — an override "
            "naming a code outside the ratified 188 fails the build; "
            "current_code must equal the join-derived code; REATTRIBUTE "
            "targets must sit in the ratified registry; DEMOTE entries carry "
            "override_code null and land the chunk unresolved-span (the "
            "R10/R14/R18/R26 convention); applied rows carry "
            "provenance.override with the map sha. NO resolution-file "
            "amendment this round: all standing note-level joins remain "
            "STANDING at the untouched join layer, the resolution file stays "
            "byte-untouched (counts 222/214/8). PROMOTIONS INTERACTION (the "
            "R26/R30 shape): the R31-shaped rebuild must consume "
            "scripts/c42_r30_promotions_amendment.yaml in its promotions "
            "re-application — the 5 HV REATTRIBUTE rows' pinned codes are "
            "superseded to the override codes (they REMAIN in the promoted "
            "set, re-keyed old->new per the R24 id_pairs convention), the 3 "
            "DEMOTE rows are EXCLUDED from the re-applied set (landing "
            "unresolved-span via the c40 DEMOTE convention), and — the loop's "
            "FIRST additions — the 3 H3 sign-off rows are ADDED to the "
            "re-applied promotion set (the R5 apply record's own per-row "
            "sign-off mechanism: 'Not auto-promoted at R5 without the "
            "operator's explicit per-row sign-off'; the operator directive "
            "trace 1a130272fc8acc11 delegated the sign-offs; the re-gate lane "
            "stays store-free and never confers). The re-homed SUGGESTED row "
            "(drawing-straight-line-graphs::0) rides the MAP alone (the R22 "
            "SUGGESTED-row re-attribution precedent) and STAYS SUGGESTED. "
            "scripts/c42_r5_promotions.yaml itself stays BYTE-UNTOUCHED (the "
            "P5 convention). Coverage projections (PROJECTED, ASSERTED "
            "NOWHERE — the DC-R24-01 discipline): covered 132 -> 133 (gained "
            "4MA1-2.7C, lost none — 4.11C keeps 4, 3.3F keeps 4, 4.8D keeps "
            "4, 2.2F keeps 14, verified row-by-row at R30), uncovered-SP 56 "
            "-> 55 (the 2.7C DEFER row f081d3d51385cb8f resolves into the "
            "re-homed trio), anchored 838 -> 835 (831 HUMAN_VALIDATED + 4 "
            "anchored SUGGESTED), unresolved-span 24 -> 27, store rows 918 "
            "-> 917"),
        "overrides": overrides,
        "h3_signoffs": {k: v for k, v in ver["h3_signoffs"].items()},
        "retain_rulings": ver["retain_rulings"],
        "note_level_scoping": ver["note_level_scoping"],
        "census_remarks": ver["census_remarks"],
        "promoted_surface_amendment": {
            "amendment_file": "scripts/c42_r30_promotions_amendment.yaml",
            "base_file": "scripts/c42_r5_promotions.yaml",
            "base_file_untouched": True,
            "supersedes": len(amendment_supersedes),
            "excluded": len(amendment_excluded),
            "added": len(added),
        },
        "dated_corrections": ver.get("dated_corrections", []),
    }
    body = yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100)
    header = (
        f"# T-C42 {ROUND} operator section-override map — derived from the R30 verdict record\n"
        f"# (the loop's EIGHTH R1-shaped repair round and the SECOND over the promoted\n"
        f"# surface; 6 verdicted REATTRIBUTEs [5 HV + 1 SUGGESTED] + the grouping DEMOTE\n"
        f"# batch of 3; 3 H3 sign-offs landing as the loop's FIRST promotions additions;\n"
        f"# 2 retain rulings; all standing note-level joins STANDING at the untouched\n"
        f"# join layer). Written ONLY by scripts/c42_r30_override_projection.py;\n"
        f"# hand-editing is forbidden.\n"
    )
    emit(OVERRIDES_OUT, header + body, "override map", len(overrides))

    # ---- 2. the promotions amendment -----------------------------------------
    adoc = {
        "schema": "c42-r31-promotions-amendment/1.0",
        "task": TASK,
        "round": ROUND,
        "generated": DATE,
        "source": ("scripts/c42_r30_repair_verdicts.yaml (section_overrides "
                   "+ h3_signoffs)"),
        "base_file": "scripts/c42_r5_promotions.yaml",
        "base_file_sha256_16": "9bad739bd79e5899",
        "base_file_untouched": True,
        "prior_amendments": ["scripts/c42_r26_promotions_amendment.yaml"],
        "contract": (
            "consumed fail-closed by the R31-shaped substrate re-build's "
            "promotions re-application AFTER the R5 file is loaded and AFTER "
            "the R26 amendment's outstanding effects are carried (the R26 "
            "supersedes/exclusion are already LANDED state in the R31 "
            "baseline store; the R30 amendment acts on the re-applied set): "
            "every supersedes_code entry re-pins one promoted row's code "
            "(identity by mapping_id + note_path + chunk_ordinal, pinned_code "
            "verified against the R5 file BEFORE the amendment applies — any "
            "drift fails the rebuild); every excluded entry removes one row "
            "from the re-applied promotion set (the DEMOTE batch lands "
            "unresolved-span via the c40 DEMOTE convention, NOT re-promoted); "
            "every added entry PROMOTES one SUGGESTED row into the re-applied "
            "set — the loop's FIRST promotions additions, the R5 apply "
            "record's own per-row H3 sign-off mechanism ('Not auto-promoted "
            "at R5 without the operator's explicit per-row sign-off') "
            "completed under the operator's explicit delegation (directive "
            "trace 1a130272fc8acc11): each added row's identity is verified "
            "against the LIVE store (SUGGESTED at the pinned code) and each "
            "entry carries its sign-off basis verbatim. The re-applied "
            "promotion count becomes 831 (832 - 1 R26 exclusion - 3 "
            "exclusions + 3 additions); the 5 superseded rows REMAIN in the "
            "promoted set at their amended codes and re-key old->new at the "
            "rebuild (the R24 id_pairs convention). The R5 file itself stays "
            "BYTE-UNTOUCHED (the P5 convention — landed records never "
            "edited); this amendment is the dated record of the R30 "
            "operator-fired adjudication and remains reviewable and "
            "reversible by the operator before the R31-shaped lane fires."),
        "supersedes_code": amendment_supersedes,
        "excluded": amendment_excluded,
        "added": added,
        "derived_census_projected": {
            "re_applied_promotions": 831,
            "re_applied_composition": ("828 from the R5 chain [832 - 1 R26 "
                                       "exclusion - 3 exclusions] + 3 added "
                                       "sign-offs"),
            "covered_codes": "132 -> 133",
            "coverage_gained": ["4MA1-2.7C"],
            "coverage_lost": [],
            "uncovered_sp": "56 -> 55",
            "resolved_defer_rows": ["f081d3d51385cb8f"],
            "anchored": "838 -> 835 (831 HUMAN_VALIDATED + 4 anchored SUGGESTED)",
            "unresolved_span": "24 -> 27 (the 3-row DEMOTE batch)",
            "store_rows": ("918 -> 917 (the 2.7C DEFER row the only "
                           "vanishing row; the 3 DEMOTE rows re-key into the "
                           "worklist)"),
        },
        "caveat": (
            "PROJECTED from verified facts, ASSERTED NOWHERE — every count "
            "lands at the R31-shaped rebuild lane (which computes its own "
            "delta proofs, the R24 R5-gate convention) and the re-gate lane "
            "after it; the DC-R24-01 discipline (compute, never assert "
            "coverage) is in force"),
    }
    abody = yaml.safe_dump(adoc, allow_unicode=True, sort_keys=False, width=100)
    aheader = (
        f"# T-C42 {ROUND} promotions amendment — derived from the R30 verdict record\n"
        f"# (the loop's SECOND promotions-affecting repair record and the FIRST with\n"
        f"# ADDITIONS: 5 code supersedes + 3 exclusions + 3 added sign-off promotions;\n"
        f"# the R5 promotions file stays byte-untouched per the P5 convention). Written\n"
        f"# ONLY by scripts/c42_r30_override_projection.py; hand-editing is forbidden.\n"
    )
    emit(AMENDMENT_OUT, aheader + abody, "promotions amendment",
         len(amendment_supersedes) + len(amendment_excluded) + len(added))

    for o in overrides:
        tgt = o["override_code"] if o["override_code"] else "(worklist)"
        print(f"  {o['note_slug']}::{o['chunk_ordinal']} "
              f"{o['current_code']} -> {tgt}")
    for a in added:
        print(f"  SIGN_OFF {a['row']['mapping_id']} "
              f"{a['row']['spec_code']} (added to the promoted set)")
    for k in sorted(retains):
        print(f"  RETAIN {k} {retains[k]['code']} (zero movement)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
