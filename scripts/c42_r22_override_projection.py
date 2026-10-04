#!/usr/bin/env python3
"""c42_r22_override_projection.py — T-C42 R22 derived projection emitter.

The R22 lane is the SIXTH R1-shaped repair round (scope §7 loop), fired by
the operator directive "R1 shaped repair" (2026-10-04, discord, gateway
trace f63adc3fd5ac8155cf81200804acb165) over the R21 re-gate's 3-row defect
inventory.

Like R18 (and unlike R6/R10/R14), the round has ZERO id-level rows and ZERO
note-level re-points (all three R21 note-level joins STAND on the R21
evidence), so there is NO resolution-file amendment this round: the
resolution file stays byte-untouched and the round's entire state carrier is
the next-re-build-facing override map — derived DETERMINISTICALLY from the
operator-owned verdict record scripts/c42_r22_repair_verdicts.yaml and
emitted here (idempotent, byte-identical re-runs).

The emitted map scripts/c42_section_overrides_r22.yaml (schema
c42-r24-section-overrides/1.0, the consuming-lane convention: R1 map -> r3,
R6 map -> r8, R10 map -> r12, R14 map -> r16, R18 map -> r20) carries:
  - 3 verdicted REATTRIBUTE entries (the loop's first zero-census-movement
    repair round — every target is already covered and every current code
    keeps coverage via its standing ords):
      3d-pythagoras-and-trigonometry::4 REATTRIBUTE 4.8D -> 4.8F
      difference-of-two-squares::3    REATTRIBUTE 2.2F -> 2.2B
      graphical-solutions::1          REATTRIBUTE 2.6B -> 3.3E
  - NO extension entries this round (the one census-surfaced candidate —
    3d-pythagoras ord 3 — sits on the R5-PROMOTED surface and is recorded as
    a census remark for the operator, NOT adjudicated: no agent-side
    movement of promoted rows)
  - the three note-level STANDING adjudications (all joins stand)
  - the standing heading-only convention reference (the 4 R21 H3 HOLD rows
    listed, no new decision — the per-row operator sign-off was not given)
  - the observations (ord-5 mixed-surface; DOTS ord 4; GRPH ord 0) and the
    dated correction DC-R22-01 (the R21 note's 3.3E ledger-status citation)

Consumed fail-closed by scripts/c40_maths_a_chunk_sp_substrate.py at the
NEXT substrate re-build (the R24-shaped lane) TOGETHER WITH the R1/R6/R10/
R14/R18 maps — wiring the R22 map into the tool is the re-build lane's job
(the R12/R16/R20 precedent); an override naming a code outside the ratified
188 fails the build; current_code must equal the join-derived code. The
re-build lane must ALSO re-apply scripts/c42_r5_promotions.yaml to the
rebuilt store (the c40 tool emits all-SUGGESTED; the 3 R22 override rows are
NOT in the promotions file — they stayed SUGGESTED at R5 — so the 832-entry
promotion set is identity- and code-stable under the three re-attributions).

Usage: python3 scripts/c42_r22_override_projection.py
"""
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
VERDICTS = REPO / "scripts/c42_r22_repair_verdicts.yaml"
OVERRIDES_OUT = REPO / "scripts/c42_section_overrides_r22.yaml"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
REGISTRY = REPO / "graph/igcse-maths-a/specification_points.yaml"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"

TASK = "T-C42"
ROUND = "R22"
DATE = "2026-10-04"


def fail(msg: str) -> None:
    print(f"FAIL-CLOSED: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    store = yaml.safe_load(STORE.read_text(encoding="utf-8"))
    reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    points = {p["code"] for p in reg["specification_points"]}
    import json
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    led_rows = {r["official_code"]: r for r in ledger["rows"]}

    rows_by_id = {r["mapping_id"]: r for r in store["rows"]}
    verdicts = ver["verdicts"]

    overrides = []
    for mid, v in sorted(verdicts.items()):
        if v.get("action") != "REATTRIBUTE":
            fail(f"unexpected action for {mid}: {v.get('action')}")
        srow = rows_by_id.get(mid)
        if srow is None:
            fail(f"verdict row {mid} not found in the live substrate")
        cur = srow["spec_code"]
        if cur != v["from_code"]:
            fail(f"current_code drift for {mid}: store {cur} vs verdict "
                 f"{v['from_code']}")
        if srow.get("validation_status") != "SUGGESTED":
            fail(f"row {mid} is not SUGGESTED — promoted rows are out of "
                 f"scope for repair rounds")
        tgt = v["to_code"]
        if tgt not in points:
            fail(f"override target {tgt} outside the ratified 188")
        if tgt == cur:
            fail(f"override target equals current for {mid}")
        overrides.append({
            "note_slug": srow["note_slug"],
            "chunk_ordinal": srow["chunk"]["ordinal"],
            "mapping_id": mid,
            "current_code": cur,
            "provenance_class": "verdicted",
            "action": "REATTRIBUTE",
            "override_code": tgt,
            "evidence": (v.get("rationale") or "").strip(),
        })

    # ledger facts asserted for the record (A4 analog, fail-closed)
    for bare, expected_present in [("4.8D", False), ("4.8F", False),
                                   ("2.2F", False), ("2.2B", True),
                                   ("2.6B", False), ("3.3E", True)]:
        if (bare in led_rows) != expected_present:
            fail(f"C30 ledger fact drifted for {bare}: present={bare in led_rows}")

    doc = {
        "schema": "c42-r24-section-overrides/1.0",
        "task": TASK,
        "round": ROUND,
        "generated": DATE,
        "source": ("scripts/c42_r22_repair_verdicts.yaml (verdicts + "
                   "note_level_adjudications + heading_only_convention + "
                   "census_remarks + dated_corrections)"),
        "contract": (
            "consumed fail-closed by scripts/c40_maths_a_chunk_sp_substrate.py "
            "at the NEXT substrate re-build (the R24-shaped lane) TOGETHER WITH "
            "scripts/c42_section_overrides.yaml (R1), "
            "scripts/c42_section_overrides_r6.yaml (R6), "
            "scripts/c42_section_overrides_r10.yaml (R10), "
            "scripts/c42_section_overrides_r14.yaml (R14) and "
            "scripts/c42_section_overrides_r18.yaml (R18) — wiring this map "
            "into the tool is the re-build lane's job (the R12/R16/R20 "
            "precedent): an override naming a code outside the ratified 188 "
            "fails the build; current_code must equal the join-derived code; "
            "REATTRIBUTE targets must sit in the ratified registry; applied "
            "rows carry provenance.override with the map sha. NO "
            "resolution-file amendment this round: all three note-level joins "
            "STAND (the R21 evidence), the resolution file stays "
            "byte-untouched. PROMOTIONS INTERACTION: the R24-shaped rebuild "
            "must re-apply scripts/c42_r5_promotions.yaml to the rebuilt store "
            "(the c40 tool emits all-SUGGESTED); the 3 R22 override rows are "
            "NOT in the promotions file — they stayed SUGGESTED at R5 — so the "
            "832-entry promotion set is identity- and code-stable under the "
            "three re-attributions; coverage is STATIONARY 129/188 (all three "
            "targets already covered; all three current codes keep coverage "
            "via their standing ords); anchored 839 and unresolved-span 23 "
            "unchanged (no DEMOTEs)"),
        "overrides": overrides,
        "note_level_adjudications": ver["note_level_adjudications"],
        "heading_only_convention": ver["heading_only_convention"],
        "census_remarks": ver["census_remarks"],
        "dated_corrections": ver["dated_corrections"],
    }

    body = yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100)
    header = (
        f"# T-C42 {ROUND} operator section-override map — derived from the R22 verdict record\n"
        f"# (the loop's sixth R1-shaped repair round; 3 verdicted REATTRIBUTEs, no DEMOTEs,\n"
        f"# no extensions, all three note-level joins STANDING). Written ONLY by\n"
        f"# scripts/c42_r22_override_projection.py; hand-editing is forbidden.\n"
    )
    new_text = header + body
    if OVERRIDES_OUT.exists():
        old = OVERRIDES_OUT.read_text(encoding="utf-8")
        if old != new_text:
            fail("override map exists with different content — refusing to "
                 "overwrite (deterministic regeneration violated)")
        print(f"c42_r22_override_projection: map already current "
              f"({len(overrides)} entries) — idempotent no-op")
        return 0
    tmp = OVERRIDES_OUT.with_suffix(".yaml.tmp")
    tmp.write_text(new_text, encoding="utf-8")
    tmp.replace(OVERRIDES_OUT)
    print(f"c42_r22_override_projection: WROTE "
          f"{OVERRIDES_OUT.relative_to(REPO)} — {len(overrides)} verdicted "
          f"REATTRIBUTE entries (0 DEMOTE, 0 extension)")
    for o in overrides:
        print(f"  {o['note_slug']}::{o['chunk_ordinal']} "
              f"{o['current_code']} -> {o['override_code']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
