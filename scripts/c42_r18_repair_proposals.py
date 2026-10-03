#!/usr/bin/env python3
"""c42_r18_repair_proposals.py — T-C42 R18 deterministic PROPOSAL-ONLY scorer.

The R18 lane is the FIFTH R1-shaped repair round of the C42 K2-B rework loop
(scope §7: "the rework lane repeats R1-shaped rounds only by explicit operator
instruction"), fired by the operator directive "R18-shaped round over the 2
rows" (2026-10-04, zai-web) over the R17 re-gate's defect inventory (2 fresh
REJECT rows in scripts/c42_r17_fresh_verdicts.yaml; the R17 gate FAILED at
exact-stratum 84/94 = 89.4% < 90% — the R13 projection falsified by the draw
mechanics and recorded honestly at R17).

Surfaces (derived deterministically from the R17 fresh verdict record):
  surface 1 — the id-level rows (root contains "note-level"): NONE this round.
              Both R17 REJECT roots are section-level classes and both
              note-level joins STAND by the R17 evidence itself (converting-
              between-fdp via its forward-conversion sections ords 5/6;
              basic-angle-properties via its property sections ords 0/2/3) —
              so there is no id-level anchor to score and NO resolution-file
              amendment this round (the R14 apply surface does not exist here).
  surface 2 — the section-level rows (every REJECT row that is not
              note-level-class): 2 rows; candidates for the section chunk's
              true code scored from the chunk heading + the fresh verdict's
              own note against the ratified 188 — BOTH tier wordings (the R1
              standing instruction): per candidate we score the store's
              operative wording AND the C30 tier-dedupe ledger's
              foundation.text and rank by the better of the two, recording
              both. The labeling-primer row (basic-angle-properties ord 1) is
              scored on the same footing for reviewability; its expected
              disposition is the scope §4 R1 menu's DEMOTE (no canonical 188
              row teaches geometric labeling per se — recorded, never forced;
              the R10/R14 precedent).
  surface 3 — the heading-only class: the 8 fresh H3 HOLD rows on the R17
              sheet (source == heading-only-convention, verdict == HOLD) are
              LISTED as continuity inventory under the STANDING convention
              c42-heading-only-convention-1 — no scorer candidates (a
              heading-only chunk has no content signal to score), no new
              decision this round. Continuity note recorded per row: three of
              the eight (standard-form ord 0, classifying-stationary-points
              ord 0, working-with-vectors ord 0) have R17-fresh CONTENT-row
              CONFIRMs of the same note+code now on the record, which the
              ladder's H2 branch resolves at the NEXT re-gate's replay (the
              R17 fill's own source-base convention: the H2 index is built
              from PRIOR re-gate records only — R4/R9/R13 at R17), so they
              un-hold automatically; the other five stay H3 fail-closed until
              evidence accumulates.
  residual  — continuity only: the C32 §3 residual stays KEPT UNRESOLVED per
              its R1 adjudication (re-affirmed at R6, R10 and R14); no new
              scoring.

Scoring: 0.5*difflib(name, wording) + 0.5*token-jaccard(name, wording)
+ 0.10 section-prior when the note's corpus tree section matches the code's
spec section (the C32 residual-scorer convention, unchanged). PMT is not a
source; top-1 candidates are deliberately published as noisy — they bound
nothing; the operator verdict round decides.

Writes graph/reports/C42_R18_REPAIR_PROPOSALS.json; prints a compact table.
"""
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "graph/reports/C42_R18_REPAIR_PROPOSALS.json"
R17_FRESH = REPO / "scripts/c42_r17_fresh_verdicts.yaml"
R17_REVIEW = REPO / "scripts/c42_r17_review_verdicts.yaml"

STOP = {"the", "a", "an", "of", "and", "to", "in", "use", "uses", "using",
        "find", "understand", "understanding", "for", "with", "on", "from",
        "how", "do", "i", "what", "is", "are", "their", "your", "it", "s"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", str(s)).lower()
    s = re.sub(r"[^a-z0-9]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def toks(s: str):
    return {t for t in norm(s).split() if t not in STOP and len(t) > 1}


def score(name_text: str, wording: str, note_section: str | None, code: str) -> dict:
    nn, wn = norm(name_text), norm(wording)
    nt, wt = toks(name_text), toks(wording)
    d = difflib.SequenceMatcher(None, nn, wn).ratio()
    j = len(nt & wt) / len(nt | wt) if (nt | wt) else 0.0
    boost = 0.0
    if note_section and note_section[0].isdigit() and code.split("-", 1)[1].split(".")[0] == note_section[0]:
        boost = 0.10
    return {"difflib_ratio": round(d, 4), "token_overlap": round(j, 4),
            "section_prior_boost": boost}


def both_tier_candidates(name_text, note_section, points, ledger, k=3):
    """Score every 188 code against BOTH the store wording and the ledger
    foundation.text; rank by the better score; record both."""
    scored = []
    for p in points:
        s_store = score(name_text, p["official_wording"], note_section, p["code"])
        led = ledger.get(p["code"].split("-", 1)[1])
        s_led = score(name_text, led["foundation"]["text"], note_section, p["code"]) if led else None
        best = max(s_store["difflib_ratio"] * 0.5 + s_store["token_overlap"] * 0.5 + s_store["section_prior_boost"],
                   (s_led["difflib_ratio"] * 0.5 + s_led["token_overlap"] * 0.5 + s_led["section_prior_boost"])
                   if s_led else -1.0)
        scored.append({"code": p["code"],
                       "wording_store": p["official_wording"],
                       "wording_ledger": led["foundation"]["text"] if led else None,
                       "score": round(best, 4),
                       "score_store": round(s_store["difflib_ratio"] * 0.5 + s_store["token_overlap"] * 0.5
                                            + s_store["section_prior_boost"], 4),
                       "score_ledger": round(s_led["difflib_ratio"] * 0.5 + s_led["token_overlap"] * 0.5
                                             + s_led["section_prior_boost"], 4) if s_led else None,
                       "tier": (p.get("applicability") or {}).get("tier")
                       if isinstance(p.get("applicability"), dict) else None})
    scored.sort(key=lambda x: -x["score"])
    return scored[:k]


def main() -> int:
    store = yaml.safe_load((REPO / "graph/igcse-maths-a/specification_points.yaml").read_text())
    points = store["specification_points"]
    ledger = {r["official_code"]: r for r in json.loads(
        (REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json").read_text())["rows"]}
    chunks = yaml.safe_load((REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml").read_text())["rows"]
    fresh = yaml.safe_load(R17_FRESH.read_text())["verdicts"]
    review = yaml.safe_load(R17_REVIEW.read_text())["verdicts"]
    bymap = {r["mapping_id"]: r for r in chunks}

    def sec_of(np_):
        return np_.split("/notes/")[1].split("/")[0] if "/notes/" in np_ else None

    # surface 1: id-level rows — root contains "note-level" -> NONE this round
    # (verified explicitly, not assumed: both R17 roots are section-level
    # classes and both note-level joins stand on the R17 evidence). NOTE: the
    # R17 fresh record carries {verdict, root, note, tier_signature} keyed by
    # mapping_id — the row context (note_path/ordinal/code/heading) joins from
    # the live R16 substrate (the R17 fill's own convention).
    surface1 = []
    note_level_roots = [m for m, x in fresh.items()
                        if x["verdict"] == "REJECT" and "note-level" in (x.get("root") or "")]
    assert not note_level_roots, f"unexpected note-level-class rows at R17: {note_level_roots}"

    # surface 2: the 2 section-level rows (both R17 REJECT rows)
    sl, seen, surface2 = [], set(), []
    for mid, x in sorted(fresh.items()):
        if x["verdict"] != "REJECT":
            continue
        srow = bymap[mid]
        key = (srow["note_path"], srow["chunk"]["ordinal"])
        if key in seen:
            continue
        seen.add(key)
        sl.append({"mapping_id": mid, "note_path": srow["note_path"],
                   "chunk_ordinal": srow["chunk"]["ordinal"],
                   "heading": srow["chunk"]["heading"],
                   "current_code": srow["spec_code"], "root": x.get("root"),
                   "fill_note": x.get("note"),
                   "substrate_sha": srow["chunk"]["sha256_16"],
                   "substrate_status": srow["validation_status"]})
    for x in sl:
        name_text = x["heading"] + " " + (x["fill_note"] or "")
        surface2.append({**x,
                         "top_candidates": both_tier_candidates(name_text, sec_of(x["note_path"]),
                                                                points, ledger)})

    # surface 3: the heading-only H3 HOLD rows on the R17 sheet — listed,
    # not scored; they ride the STANDING convention. Continuity note: the
    # R17-fresh content CONFIRMs now on the record resolve three of the eight
    # via H2 at the NEXT re-gate's replay (the source-base convention).
    surface3 = []
    for mid, x in sorted(review.items(),
                         key=lambda kv: (kv[1]["note_path"], kv[1]["chunk_ordinal"])):
        if x["verdict"] == "HOLD":
            surface3.append({
                "mapping_id": mid, "note_path": x["note_path"],
                "chunk_ordinal": x["chunk_ordinal"], "heading": x["heading"],
                "current_code": x["spec_code"], "r17_source": x.get("source"),
                "r17_stratum": x.get("stratum"),
            })
    H2_READY = {  # note_path fragment -> the R17-fresh content-CONFIRM evidence
        "standard-form.json": "R17 fresh rows 0211af0e0b8a806d (ord 3) + d7339b416c53ba5e (ord 2), "
                              "content CONFIRMs on standard-form + 1.9A",
        "classifying-stationary-points.json": "R17 fresh row 59aec49753b23112 (ord 1), content "
                                              "CONFIRM on classifying-stationary-points + 3.4C",
        "working-with-vectors.json": "R17 fresh row 7b279735e8877e9e (ord 1), content CONFIRM on "
                                     "working-with-vectors + 5.1F",
    }
    for s in surface3:
        frag = s["note_path"].split("/")[-1]
        s["h2_projection_next_regate"] = H2_READY.get(frag)

    out = {
        "schema": "syllabai.c42-r18-repair-proposals/1.0",
        "task": "T-C42 / R18 (the fifth R1-shaped repair round, over the R17 2-row defect inventory)",
        "directive": "R18-shaped round over the 2 rows (2026-10-04, zai-web)",
        "method": "0.5*difflib(name, wording) + 0.5*token-jaccard + 0.10 section-prior, scored "
                  "against BOTH tier wordings (store operative + C30 ledger foundation.text, "
                  "better-of-two recorded); name_text = chunk heading + evidence note (surface 2); "
                  "PROPOSAL-ONLY — binds nothing; top-1 candidates are deliberately published as "
                  "noisy; PMT excluded as source; the operator verdict round decides. Surface 1 is "
                  "EMPTY this round (no note-level-class root — both note-level joins STAND on the "
                  "R17 evidence, so there is no id-level anchor and NO resolution-file amendment). "
                  "Surface 3 (the 8 H3 HOLD rows) is LISTED not scored — they ride the STANDING "
                  "convention c42-heading-only-convention-1; three carry R17-fresh content CONFIRM "
                  "evidence that resolves them via H2 at the next re-gate's replay; see "
                  "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md",
        "surface1_id_level": surface1,
        "surface2_section_level": surface2,
        "surface3_heading_only_h3_continuity": surface3,
        "residual": {"anchor_id": "spcpt_QWXhzVp2S3VYZdZc",
                     "disposition": "KEPT UNRESOLVED — continuity from the R1 adjudication "
                                    "(re-affirmed at R6, R10 and R14); the PDF-verified reason "
                                    "stands; no new scoring"},
    }
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")

    print(f"surface1: {len(surface1)} id-level rows | surface2: {len(surface2)} section rows | "
          f"surface3: {len(surface3)} H3 HOLD rows listed (standing convention)")
    print("  --- surface 2 ---")
    for s in surface2:
        c = s["top_candidates"][0]
        print(f"  {s['note_path'].split('/')[-1][:28]:28s} ord {s['chunk_ordinal']} "
              f"cur={s['current_code']:10s} -> {c['code']:10s} {c['score']:.3f} [{s['root'][:44]}]")
    print("  --- surface 3 (listed, standing convention) ---")
    for s in surface3:
        h2p = s["h2_projection_next_regate"]
        tag = "H2-ready (un-holds at next re-gate)" if h2p else "stays H3 until evidence accumulates"
        print(f"  {s['current_code']:11s} ord {s['chunk_ordinal']:2d} "
              f"{s['heading'][:44]!r} | {tag}")
    print("proposals ->", OUT.relative_to(REPO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
