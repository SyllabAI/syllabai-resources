#!/usr/bin/env python3
"""c42_r18_override_projection.py — T-C42 R18 derived projection emitter.

The R18 lane is the fifth R1-shaped repair round (scope §7 loop), fired by the
operator directive "R18-shaped round over the 2 rows" (2026-10-04, zai-web).

Unlike R6/R10/R14, the R18 round has ZERO id-level rows and ZERO note-level
re-points (both R17 note-level joins STAND on the R17 evidence), so there is
NO resolution-file amendment this round: the resolution file stays
byte-untouched (counts 222/214/8) and the round's entire state carrier is the
next-re-build-facing override map — derived DETERMINISTICALLY from the
operator-owned verdict record scripts/c42_r18_repair_verdicts.yaml and
emitted here (idempotent, byte-identical re-runs).

The emitted map scripts/c42_section_overrides_r18.yaml (schema
c42-r20-section-overrides/1.0, the consuming-lane convention: R1 map -> r3,
R6 map -> r8, R10 map -> r12, R14 map -> r16) carries:
  - 2 verdicted entries: converting-between-fdp::3 REATTRIBUTE 1.2G -> 1.3D;
    basic-angle-properties::1 DEMOTE_TO_WORKLIST (the loop's third DEMOTE)
  - 2 transparently-labeled EXTENSION entries (the R6 precedent; the R17
    census remark's own finding): converting-between-fdp::2 -> 1.3D and
    converting-between-fdp::4 -> 1.6C
  - the two note-level STANDING adjudications (both joins stand)
  - the standing heading-only convention reference (8 H3 rows listed, no new
    decision; three H2-ready at the next re-gate's replay)
  - the observations

Consumed fail-closed by scripts/c40_maths_a_chunk_sp_substrate.py at the
NEXT substrate re-build (the R20-shaped lane) TOGETHER WITH the R1/R6/R10/R14
maps — wiring the R18 map into the tool is the re-build lane's job (the R12/
R16 precedent); an override naming a code outside the ratified 188 fails the
build; current_code must equal the join-derived code; a DEMOTE_TO_WORKLIST
entry moves the chunk row to the unresolved-span worklist with its recorded
reason.

Usage: python3 scripts/c42_r18_override_projection.py
"""
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
VERDICTS = REPO / "scripts/c42_r18_repair_verdicts.yaml"
OVERRIDES_OUT = REPO / "scripts/c42_section_overrides_r18.yaml"

TASK = "T-C42"
ROUND = "R18"
DATE = "2026-10-04"


def main() -> int:
    verdicts = yaml.safe_load(VERDICTS.read_text())
    sec_ov = verdicts["section_overrides"]
    ext_ov = verdicts["extension_section_overrides"]
    adjud = verdicts["note_level_adjudications"]
    convention = verdicts["heading_only_convention"]
    subsumed = verdicts.get("subsumed_prior_entries", {})
    observations = verdicts.get("observations", {})
    residual = verdicts["residual"]

    entries = []
    for k, x in sorted(sec_ov.items()):
        entries.append({
            "note_slug": k.split("::")[0], "chunk_ordinal": int(k.split("::")[1]),
            "mapping_id": x.get("mapping_id"),
            "current_code": x["current_code"], "provenance_class": "verdicted",
            "action": x["disposition"], "override_code": x.get("override_code"),
            "evidence": x["evidence"],
        })
    for k, x in sorted(ext_ov.items()):
        if k == "contract":
            continue
        entries.append({
            "note_slug": k.split("::")[0], "chunk_ordinal": int(k.split("::")[1]),
            "mapping_id": x.get("mapping_id"),
            "current_code": x["current_code"], "provenance_class": "extension",
            "action": x["disposition"], "override_code": x.get("override_code"),
            "evidence": x["evidence"],
        })
    entries.sort(key=lambda e: (e["note_slug"], e["chunk_ordinal"]))

    proj = {
        "schema": "c42-r20-section-overrides/1.0",
        "task": TASK, "round": ROUND, "generated": DATE,
        "source": "scripts/c42_r18_repair_verdicts.yaml (section_overrides + "
                  "extension_section_overrides + note_level_adjudications + "
                  "heading_only_convention)",
        "contract": "consumed fail-closed by scripts/c40_maths_a_chunk_sp_substrate.py at the "
                    "NEXT substrate re-build (the R20-shaped lane) TOGETHER WITH "
                    "scripts/c42_section_overrides.yaml (R1), scripts/c42_section_overrides_r6.yaml "
                    "(R6), scripts/c42_section_overrides_r10.yaml (R10) and "
                    "scripts/c42_section_overrides_r14.yaml (R14) — wiring this map into the tool "
                    "is the re-build lane's job (the R12/R16 precedent): an override naming a code "
                    "outside the ratified 188 fails the build; current_code must equal the "
                    "join-derived code; a DEMOTE_TO_WORKLIST entry moves the chunk row to the "
                    "unresolved-span worklist with its recorded reason; extension entries carry "
                    "provenance_class 'extension' (the R6 precedent, recorded zero-silent-repair). "
                    "NO resolution-file amendment this round: both note-level joins STAND (the "
                    "R17 evidence), the resolution file stays byte-untouched, counts 222/214/8",
        "overrides": entries,
        "note_level_adjudications": {
            "converting-between-fdp": {
                "anchor_id": adjud["converting-between-fdp"]["anchor_id"],
                "ruling": adjud["converting-between-fdp"]["ruling"],
                "evidence": adjud["converting-between-fdp"]["evidence"],
                "consequence": adjud["converting-between-fdp"]["consequence"],
            },
            "basic-angle-properties": {
                "anchor_id": adjud["basic-angle-properties"]["anchor_id"],
                "ruling": adjud["basic-angle-properties"]["ruling"],
                "evidence": adjud["basic-angle-properties"]["evidence"],
                "consequence": adjud["basic-angle-properties"]["consequence"],
            },
        },
        "heading_only_convention": {
            "decision_id": convention.get("decision"),
            "record": convention.get("record"),
            "ruling_summary": convention.get("ruling_summary"),
            "enforcement": "the next re-gate fill resolves heading-only rows via the standing "
                           "convention ladder — its H2 index is built from PRIOR re-gate records "
                           "only (R4/R9/R13/R17 at the next replay; the R17 fill's own "
                           "source-base convention), so the three H2-ready rows un-hold "
                           "automatically; the re-build itself needs no convention wiring "
                           "(chunk identity is untouched)",
        },
        "subsumed_prior_entries": subsumed.get("entries", []) if isinstance(subsumed, dict) else [],
        "residual": {"anchor_id": residual["anchor_id"],
                     "disposition": residual["disposition"]},
        "observations": observations,
    }
    OVERRIDES_OUT.write_text(yaml.safe_dump(proj, sort_keys=False, allow_unicode=True,
                                            width=100))

    nv = sum(1 for e in entries if e["provenance_class"] == "verdicted")
    ne = sum(1 for e in entries if e["provenance_class"] == "extension")
    nd = sum(1 for e in entries if e["action"] == "DEMOTE_TO_WORKLIST")
    print(f"projection: {len(entries)} entries ({nv} verdicted [{nv - nd} REATTRIBUTE + "
          f"{nd} DEMOTE_TO_WORKLIST] + {ne} extension) "
          f"+ {len(proj['note_level_adjudications'])} note-level STANDING rulings")
    for e in entries:
        print(f"  {e['note_slug']}::{e['chunk_ordinal']} {e['current_code']} -> "
              f"{e['override_code'] or '(worklist)'} [{e['provenance_class']} {e['action']}]")
    print("overrides ->", OVERRIDES_OUT.relative_to(REPO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
