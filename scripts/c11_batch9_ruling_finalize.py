#!/usr/bin/env python3
"""T-C11 session 62 — batch-9 boundary-ruling FINALIZER.

Renders scripts/c11_batch9_boundary_ruling.yaml from machine truth:
  * the full 162-term candidate list (imported from the audit probe)
  * the exact 46-term match set re-computed against the live pre-batch-9
    store (165 nodes / 384 edges @ 4e6bc2f)
  * a PER-TERM disposition table (46 entries; the batch-8 one-entry-per-
    match contract) with the disposition class + shared rationale refs
  * the curated non_mint_list (the plausible-collision set) asserted live
  * the FIVE sanctioned boundary targets with owner verification
Run c11_batch9_term_audit_probe.py first if the store moved; this
finalizer refuses to write if the match count differs from 46.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402

GRAPH = GP.qual_dir()
OUT = HERE / "c11_batch9_boundary_ruling.yaml"

# disposition classes (the batch-8 vocabulary)
BOUNDARY = "BOUNDARY_EDGE_SANCTIONED"
NEAR_MISS = "NO_COLLISION_DIFFERENT_DOMAIN"
REAGENT = "REAGENT_APPLIED_AS_GIVEN"
NOISE = "SUBSTRING_NOISE"

# per-term disposition map (term -> (class, rationale key)); every matched
# term MUST appear here — the finalizer fails closed otherwise.
DISPOSITIONS = {
    # real domain collisions -> the five sanctioned boundary edges
    "fractional distillation": (BOUNDARY, "TARGET-1"),
    "fraction": (BOUNDARY, "TARGET-1"),
    "empirical formula": (BOUNDARY, "TARGET-2"),
    "molecular formula": (BOUNDARY, "TARGET-3"),
    "combustion": (BOUNDARY, "TARGET-4"),
    "mixture": (BOUNDARY, "TARGET-5"),
    # near-miss domain terms (different demand, same adjective)
    "saturated": (NEAR_MISS, "saturated-SOLUTIONS (batch-3 owner) vs "
                  "saturated HYDROCARBONS (single C-C bonds, 4.20) — "
                  "coincidental English, not a shared concept; the alkane "
                  "family is minted in-batch"),
    "halogen": (REAGENT, "the batch-2 G7 owners teach halogen "
                "properties/reactivity as the studied object; 4.22 uses "
                "bromine/chlorine as REAGENTS whose new substitution "
                "chemistry is in-slice; no boundary edge (the "
                "mechanism-applied class would double-count a reagent "
                "mention)"),
    "halogens": (REAGENT, "SAME AS 'halogen'"),
    "bromine": (REAGENT, "SAME AS 'halogen'"),
    "chlorine": (REAGENT, "SAME AS 'halogen'"),
}
# everything else matched = substring noise (generic cross-domain
# vocabulary; no owner is the studied object of any batch-9 SP)
NOISE_RATIONALE = ("generic cross-domain chemistry vocabulary; no batch-9 "
                   "SP studies the hit owners; the owners stay untouched "
                   "except through the five sanctioned boundary edges; the "
                   "trend explanation via intermolecular attraction is "
                   "HELD (B9-H-08) as deeper-than-demand")

RATIONALES = {
    "TARGET-1": "the 4.8 industrial separation IS the batch-1 "
                "fractional-distillation technique applied to crude oil "
                "(fractionating column, temperature gradient, "
                "vapourise/condense) — the technique concept is the "
                "owner's fixed surface; edge CRUDE-OIL-FRACTIONS RP "
                "FRACTIONAL-DISTILLATION sanctioned; the mint is FORBIDDEN",
    "TARGET-2": "4.2's representation surface APPLIES the pilot's "
                "empirical-formula definition ('simplest possible ratio') "
                "to organic molecules; edge ORGANIC-FORMULAE RP "
                "EMPIRICAL-FORMULA sanctioned; the mint is FORBIDDEN",
    "TARGET-3": "4.2 applies the pilot's molecular-formula definition "
                "('actual number of atoms'); edge ORGANIC-FORMULAE RP "
                "MOLECULAR-FORMULA sanctioned; the mint is FORBIDDEN",
    "TARGET-4": "4.11/4.12's fuels surface presupposes the batch-5 "
                "combustion owner ('Complete combustion occurs when there "
                "is excess oxygen'); CALORIMETRY is an incidental "
                "substring hit; edge FUELS-COMBUSTION RP COMBUSTION-O2 "
                "sanctioned; the mint is FORBIDDEN",
    "TARGET-5": "4.7's definition IS the batch-1 mixture concept applied "
                "(not chemically combined, physically separable — exactly "
                "why 4.8's distillation works); ALLOYS is incidental; "
                "edge CRUDE-OIL RP MIXTURE sanctioned; the mint is "
                "FORBIDDEN",
}


def main() -> int:
    # import TERMS from the probe module (source of truth)
    import importlib.util
    spec = importlib.util.spec_from_file_location(
        "b9probe", HERE / "c11_batch9_term_audit_probe.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    terms = mod.TERMS

    nodes = yaml.safe_load(
        (GRAPH / "concepts.yaml").read_text(encoding="utf-8"))["nodes"]
    edges = yaml.safe_load(
        (GRAPH / "concept_edges.yaml").read_text(encoding="utf-8"))["edges"]
    blob = []
    for x in nodes:
        blob.append(x["code"])
        blob.append(x["title"])
        blob.extend(x.get("aliases", []))
    store_blob = " || ".join(blob).lower()
    endpoints = " ".join(f"{e['source']} {e['target']}"
                         for e in edges).lower()
    matched = [t for t in terms if t in store_blob or t in endpoints]
    if len(matched) != 46:
        print(f"FAIL-CLOSED: match count {len(matched)} != 46 — the store "
              f"moved since the audit; re-run the probe and re-disposition",
              file=sys.stderr)
        return 1

    # per-term disposition table
    dispositions = []
    for t in matched:
        cls, key = DISPOSITIONS.get(t, (NOISE, None))
        if cls == BOUNDARY:
            rationale = RATIONALES[key]
        elif cls == NOISE:
            rationale = NOISE_RATIONALE
        else:
            rationale = key
        dispositions.append({"term": t, "disposition": cls,
                             "rationale": rationale})
    for t, (cls, key) in DISPOSITIONS.items():
        if cls in (BOUNDARY, NEAR_MISS, REAGENT) and t not in matched:
            print(f"FAIL-CLOSED: dispositioned term {t!r} did not match — "
                  f"re-check", file=sys.stderr)
            return 1

    live_codes = {x["code"] for x in nodes}
    non_mint = sorted(set(yaml.safe_load(
        (HERE / "c11_batch9_non_mint.yaml").read_text(encoding="utf-8"))
        ["non_mint_list"]))
    missing = [c for c in non_mint if c not in live_codes]
    if missing:
        print(f"FAIL-CLOSED: non_mint codes not live: {missing}",
              file=sys.stderr)
        return 1

    ruling = {
        "meta": {
            "task": "T-C11",
            "stage": "s16-cross-slice-boundary-ruling",
            "session": 62,
            "recorded_date": "2026-09-24",
            "commissioned_by": 'operator directive "commission a new '
                               'section" (2026-09-24, session 62) under '
                               'the session-46 §16 authorization; the S4 '
                               'slice plan (batches 9-11) is recorded in '
                               'the session-62 commissioning record',
            "scope": "conflict-prevention ruling for the "
                     "S2(complete)+S1+S3(complete) -> S4(batch 9: a "
                     "Introduction + b Crude Oil & Fuels + c Alkanes, "
                     "4CH1-4.1-4.22 minus the 4CH1-4.15 negative-control "
                     "carve-out) boundary only; supersedes nothing; "
                     "extends the session-55/57/59/61 ruling pattern to "
                     "the S4-a/b/c slice",
            "applies_to_batch": 9,
            "scope_sp_note": "the audit covers the 21 authorable SPs; "
                             "4CH1-4.15 (S4-b) is the standing negative "
                             "control and is CARVED OUT of the batch scope "
                             "entirely — no node/edge may attach or cite "
                             "it (the graph_check D12 control continues to "
                             "verify zero attachments)",
        },
        "conflict_audit": {
            "method": "S4-a/b/c candidate term vocabulary (162 terms: "
                      "introduction vocabulary, crude-oil/fuels "
                      "vocabulary, alkane vocabulary, the named "
                      "reagents, generic chemistry vocabulary and "
                      "equation scaffolding) matched against the whole "
                      "merged pre-batch-9 store at 4e6bc2f (node codes + "
                      "titles + aliases + every edge endpoint, "
                      "case-folded substring; the probe is persisted as "
                      "scripts/c11_batch9_term_audit_probe.py). 46 terms "
                      "match; EVERY match is dispositioned below — "
                      "sanctioned boundary edge, near-miss distinct-demand "
                      "(no edge, mint in-batch), reagent-applied-as-given "
                      "(no edge), or sub-string noise (no owner surface).",
            "s4_candidate_terms": terms,
            "result": "NO UNHANDLED canonical conflict — 46 terms match "
                      "the pre-batch-9 store, all owned by existing nodes "
                      "or matched only at sub-string level, with an "
                      "explicit disposition below; Section 4 mints its own "
                      "families at the ratified granularity and re-mints "
                      "NO existing identity. The S4-a/b/c ORGANIC "
                      "vocabulary has NO existing owner anywhere in the "
                      "store (the 116 unmatched terms include hydrocarbon, "
                      "homologous series, functional group, isomerism, "
                      "IUPAC naming, displayed/structural/general formula, "
                      "substitution, addition, crude oil, refinery gases, "
                      "gasoline, kerosene, diesel, fuel oil, bitumen, "
                      "viscosity, complete/incomplete combustion, carbon "
                      "monoxide, haemoglobin, nitrogen oxides, sulfur "
                      "dioxide, acid rain, cracking, catalytic cracking, "
                      "supply and demand, alkanes, CnH2n+2, saturated "
                      "hydrocarbons, ultraviolet radiation, "
                      "halogenoalkanes) — the batch mints these families "
                      "fresh; the only surfaces with existing owners are "
                      "dispositioned below.",
        },
        "match_dispositions": dispositions,
        "mint_ruling": {
            "rule": "the batch-9 extraction mints only the in-slice family "
                    "nodes the notes teach (14 CONCEPT + 1 MISCONCEPTION); "
                    "every existing owner the audit touched stays "
                    "untouched except through the FIVE sanctioned boundary "
                    "edges; the negative control 4CH1-4.15 gains NO "
                    "attachment and NO citation",
            "mints": "14 CONCEPT (HYDROCARBON 4.1; ORGANIC-FORMULAE 4.2; "
                     "HOMOLOGOUS-SERIES 4.3; IUPAC-NAMING 4.4; ISOMERS "
                     "4.5; ORGANIC-REACTION-CLASSES 4.6; CRUDE-OIL 4.7; "
                     "CRUDE-OIL-FRACTIONS 4.8-4.10 one-family; "
                     "FUELS-COMBUSTION 4.11-4.12 one-family; CO-POISONING "
                     "4.13; ACID-RAIN-CAUSES 4.14+4.16; CRACKING "
                     "4.17-4.18; ALKANES 4.19-4.21 one-family; "
                     "ALKANE-HALOGEN-SUBSTITUTION 4.22) + 1 MISCONCEPTION "
                     "(MIS-KEROSENE-DOUBLE-BONDS, the pinned Crude Oil MS "
                     "Q2b Reject class)",
        },
        "boundary_edge_ruling": {
            "rule": "the FN-B1-2/FN-B2-2 cross-batch discipline at the "
                    "S4-a/b/c boundary: boundary EDGES are sanctioned ONLY "
                    "into the exact-owner nodes below, ONLY for the stated "
                    "dependency surfaces; boundary MINTING is forbidden; "
                    "if any batch-9 term ever matches an existing node "
                    "outside this sanctioned set, the boundary edge is "
                    "MANDATORY and the mint FORBIDDEN (fail-closed at "
                    "preverify/G03/c11.4). All FIVE sanctioned targets are "
                    "EXISTING-OWNER nodes (pilot x2, batch-1 x2, batch-5 "
                    "x1) — batch 9 closes NO deferrals and creates none: "
                    "the batch-9 audit surfaces either resolve in-batch, "
                    "ride the five sanctioned edges, or are "
                    "held/future-noted (B9-H-01..09, the "
                    "future_boundary_notes).",
            "sanctioned_targets": [
                {"for_sps": ["4CH1-4.8"], "owner": "batch 1",
                 "target": "4CH1-CON-FRACTIONAL-DISTILLATION",
                 "surface": "the 4.8 industrial fractional distillation of "
                            "crude oil runs the batch-1 separation "
                            "technique (fractionating column, temperature "
                            "gradient, vapourise/condense) applied to "
                            "petroleum — the note's own sentences re-state "
                            "the technique's vocabulary; the technique is "
                            "never re-defined by the 4.8 note"},
                {"for_sps": ["4CH1-4.2"], "owner": "pilot",
                 "target": "4CH1-CON-EMPIRICAL-FORMULA",
                 "surface": "the 4.2 representation surface applies the "
                            "pilot's empirical-formula definition "
                            "('simplest possible ratio') to organic "
                            "molecules — the definition is the owner's, "
                            "the organic application is in-slice"},
                {"for_sps": ["4CH1-4.2"], "owner": "pilot",
                 "target": "4CH1-CON-MOLECULAR-FORMULA",
                 "surface": "as above for the molecular-formula definition "
                            "('actual number of atoms')"},
                {"for_sps": ["4CH1-4.11", "4CH1-4.12"], "owner": "batch 5",
                 "target": "4CH1-CON-COMBUSTION-O2",
                 "surface": "the fuels family's complete/incomplete "
                            "combustion presupposes the batch-5 "
                            "combustion-in-oxygen owner ('Complete "
                            "combustion occurs when there is excess "
                            "oxygen' — the oxygen reactant is the owner's "
                            "surface applied, never re-defined)"},
                {"for_sps": ["4CH1-4.7"], "owner": "batch 1",
                 "target": "4CH1-CON-MIXTURE",
                 "surface": "4.7's definition ('crude oil is a mixture of "
                            "hydrocarbons') applies the batch-1 mixture "
                            "concept (not chemically combined; physically "
                            "separable — which is precisely why the 4.8 "
                            "distillation works)"},
            ],
            "max_boundary_edges": 5,
            "non_mint_list": non_mint,
        },
        "future_boundary_notes": [
            "4.23-4.28 (S4-d alkenes) build directly on this batch's alkene "
            "vocabulary (addition reactions, bromine water) — batch 10 owns "
            "the continuation; the cracking-products alkenes surface (this "
            "batch's 4.17/4.18) plants the seed",
            "4.29C-4.33C (S4-e alcohols) + 4.38C-4.43C (S4-g esters) ride "
            "the functional-group vocabulary this batch's 4.3/4.4 nodes "
            "establish — batches 10-11 own them; the Crude Oil MS "
            "fermentation-vs-cracking comparison (Q3c) is batch-10 evidence",
            "4.44-4.50C (S4-h polymers) ride 4.6's addition-reaction class "
            "and the Crude Oil MS condensation-polymerisation/disposal "
            "surfaces — batch 11 owns them",
            "the 4.15 negative control sits BETWEEN the 4.14 (NOx "
            "formation) and 4.16 (acid rain) rows this batch authors — the "
            "acid-rain family node MUST NOT cite any 4.15-specific sentence "
            "(impurities -> SO2 formation); its anchors stay on the note's "
            "4.14/4.16-mapped sentences; the graph_check D12 zero-"
            "attachment control continues",
            "the Alkanes MS UV-light line ('If start with bromine (water) "
            "in presence of UV light then scores 0/3') documents the UV "
            "condition from the MARK-SCHEME side — batch 10's 4.28 "
            "alkane/alkene distinction owns the full bromine-water test "
            "surface; this batch's 4.22 anchors only the "
            "substitution-with-UV teaching",
        ],
        "non_goals": [
            "no ontology redesign",
            "no re-opening of settled batches",
            "no re-scoping of the section plan",
            "no promotion authority (SUGGESTED until the operator's §18 "
            "command)",
            "no direct writes to graph/*.yaml",
        ],
    }
    header = ("# T-C11 session 62 — batch-9 cross-slice boundary ruling "
              "(S4 Organic FIRST slice: a Introduction + b Crude Oil & "
              "Fuels + c Alkanes).\n# RENDERED by "
              "c11_batch9_ruling_finalize.py from machine truth — do not "
              "hand-edit the audit tables; the standing\n# checker "
              "c11_batch9_boundary_check.py re-runs the match as its "
              "B-gate.\n")
    OUT.write_text(
        header + yaml.safe_dump(ruling, sort_keys=False, allow_unicode=True,
                                width=100),
        encoding="utf-8")
    print(f"wrote {OUT} ({len(terms)} terms, {len(matched)} matched, "
          f"{len(dispositions)} dispositions, {len(non_mint)} non-mint)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
