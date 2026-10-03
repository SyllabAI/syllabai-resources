#!/usr/bin/env python3
"""c42_r14_repair_proposals.py — T-C42 R14 deterministic PROPOSAL-ONLY scorer.

The R14 lane is the FOURTH R1-shaped verdict round of the C42 K2-B rework loop
(scope §7: "the rework lane repeats R1-shaped rounds only by explicit operator
instruction"), fired by the operator directive "R14-shaped round over the 6
rows" (2026-10-04, zai-web) over the R13 re-gate's defect inventory (6 fresh
REJECT rows in scripts/c42_r13_fresh_verdicts.yaml; the R13 gate FAILED at
exact-stratum 85/95 = 89.5% < 90% — short by half a point).

Surfaces (derived deterministically from the R13 fresh verdict record):
  surface 1 — the id-level rows (root == note-level-class): 1 reject row ->
              1 anchor (composite-functions); candidates for the corrected
              code of the note's anchor, scored from the note title AND the
              note's own taught-content signal (its chunk headings) against
              the ratified 188 — BOTH tier wordings (the R1 standing
              instruction): per candidate we score the store's operative
              wording AND the C30 tier-dedupe ledger's foundation.text and
              rank by the better of the two, recording both.
  surface 2 — the section-level rows (root == section-level or
              "unresolved-class section"): 5 rows; candidates for the section
              chunk's true code scored from the chunk heading + the fresh
              verdict's own note. The unresolved-class row (unit-conversions
              ord 2) is scored on the same footing for reviewability; its
              expected disposition is the scope §4 R1 menu's DEMOTE (no
              canonical 188 row teaches metric mass conversion — recorded,
              never forced).
  surface 3 — the heading-only class: the 4 fresh H3 HOLD rows on the R13
              sheet (source == heading-only-convention, verdict == HOLD) are
              LISTED as continuity inventory under the STANDING convention
              c42-heading-only-convention-1 — no scorer candidates (a
              heading-only chunk has no content signal to score), no new
              decision this round; they un-hold automatically at the R17
              re-gate once H1/H2 becomes true (bounds ord 2 CONFIRMed fresh
              at R13, so bounds ord 0 un-holds via H2 with the R13 record in
              the ladder's source base).
  residual  — continuity only: the C32 §3 residual stays KEPT UNRESOLVED per
              its R1 adjudication (re-affirmed at R6 and R10); no new scoring.

Scoring: 0.5*difflib(name, wording) + 0.5*token-jaccard(name, wording)
+ 0.10 section-prior when the note's corpus tree section matches the code's
spec section (the C32 residual-scorer convention, unchanged). PMT is not a
source; top-1 candidates are deliberately published as noisy — they bound
nothing; the operator verdict round decides.

Writes graph/reports/C42_R14_REPAIR_PROPOSALS.json; prints a compact table.
"""
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "graph/reports/C42_R14_REPAIR_PROPOSALS.json"
R13_FRESH = REPO / "scripts/c42_r13_fresh_verdicts.yaml"
R13_REVIEW = REPO / "scripts/c42_r13_review_verdicts.yaml"

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
    fresh = yaml.safe_load(R13_FRESH.read_text())["verdicts"]
    review = yaml.safe_load(R13_REVIEW.read_text())["verdicts"]
    join = json.loads((REPO / "Official-Specifications/parsed/_derived/notes-join/"
                       "igcse-maths-a-18-higher.json").read_text())
    jrows = {r["note_path"]: r for r in join["joins"]}

    note_headings = {}
    for r in chunks:
        if "note_path" not in r:
            continue
        note_headings.setdefault(r["note_path"], []).append(
            r.get("chunk", {}).get("heading") or r.get("evidence_quote") or "")

    def sec_of(np_):
        return np_.split("/notes/")[1].split("/")[0] if "/notes/" in np_ else None

    # surface 1: the id-level surface, derived from the R13 fresh roots
    # (note-level-class rows -> their note anchors). The unresolved-class
    # section root (unit-conversions ord 2) does NOT contribute here: the R13
    # root does not suspect the note-level join (ords 0-1/3 carry genuine
    # length/volume conversion content, ord 1 already R6-ruled to 4.9A), so
    # the anchor is not a repair candidate.
    anchors, rows_per_anchor = {}, {}
    for x in fresh.values():
        if x["verdict"] != "REJECT":
            continue
        if x.get("root") == "note-level-class":
            jr = jrows[x["note_path"]]
            aid = jr["anchor_id"]
            anchors.setdefault(aid, x["note_path"])
            rows_per_anchor[aid] = rows_per_anchor.get(aid, 0) + 1
    surface1 = []
    for aid, np_ in sorted(anchors.items()):
        jr = jrows[np_]
        headings = [h for h in note_headings.get(np_, []) if h]
        name_text = jr["note_title"] + " " + " ".join(headings)
        surface1.append({
            "anchor_id": aid, "note_path": np_, "note_title": jr["note_title"],
            "sme_name": jr["sme_name"], "wrong_code": jr["store_row_code"],
            "wrong_code_wording": jr["official_wording"],
            "r13_reject_rows": rows_per_anchor[aid],
            "store_rows_on_the_note": sum(
                1 for r in chunks if r.get("note_path") == np_),
            "note_headings": headings,
            "top_candidates": both_tier_candidates(name_text, sec_of(np_), points, ledger),
        })

    # surface 2: the 5 section-level rows (4 section-level + 1
    # unresolved-class section)
    sl, seen, surface2 = [], set(), []
    for x in sorted(fresh.values(), key=lambda y: (y["note_path"], y["chunk_ordinal"])):
        if x["verdict"] == "REJECT" and x.get("root") in ("section-level", "unresolved-class section"):
            key = (x["note_path"], x["chunk_ordinal"])
            if key not in seen:
                seen.add(key)
                sl.append({"note_path": x["note_path"], "chunk_ordinal": x["chunk_ordinal"],
                           "heading": x["chunk_heading"], "current_code": x["spec_code"],
                           "root": x.get("root"), "fill_note": x.get("note")})
    for x in sl:
        name_text = x["heading"] + " " + (x["fill_note"] or "")
        surface2.append({**x,
                         "top_candidates": both_tier_candidates(name_text, sec_of(x["note_path"]),
                                                                points, ledger)})

    # surface 3: the heading-only H3 HOLD rows on the R13 sheet — listed,
    # not scored; they ride the STANDING convention
    # c42-heading-only-convention-1 (no new decision this round)
    surface3 = []
    for mid, x in sorted(review.items(),
                         key=lambda kv: (kv[1]["note_path"], kv[1]["chunk_ordinal"])):
        if x["verdict"] == "HOLD":
            surface3.append({
                "mapping_id": mid, "note_path": x["note_path"],
                "chunk_ordinal": x["chunk_ordinal"], "heading": x["heading"],
                "current_code": x["spec_code"], "r13_source": x.get("source"),
                "r13_stratum": x.get("stratum"),
            })

    out = {
        "schema": "syllabai.c42-r14-repair-proposals/1.0",
        "task": "T-C42 / R14 (the fourth R1-shaped verdict round, over the R13 defect inventory)",
        "directive": "R14-shaped round over the 6 rows (2026-10-04, zai-web)",
        "method": "0.5*difflib(name, wording) + 0.5*token-jaccard + 0.10 section-prior, scored "
                  "against BOTH tier wordings (store operative + C30 ledger foundation.text, "
                  "better-of-two recorded); name_text = note title + the note's own chunk headings "
                  "(surface 1) or chunk heading + evidence note (surface 2); PROPOSAL-ONLY — binds "
                  "nothing; top-1 candidates are deliberately published as noisy; PMT excluded as "
                  "source; the operator verdict round decides. Surface 3 (the 4 H3 HOLD rows) is "
                  "LISTED not scored — they ride the STANDING convention "
                  "c42-heading-only-convention-1 and un-hold at the R17 re-gate via H1/H2; see "
                  "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.md",
        "surface1_id_level": surface1,
        "surface2_section_level": surface2,
        "surface3_heading_only_h3_continuity": surface3,
        "residual": {"anchor_id": "spcpt_QWXhzVp2S3VYZdZc",
                     "disposition": "KEPT UNRESOLVED — continuity from the R1 adjudication "
                                    "(re-affirmed at R6 and R10); the PDF-verified reason stands; "
                                    "no new scoring"},
    }
    OUT.write_text(json.dumps(out, indent=1, ensure_ascii=False) + "\n")

    print(f"surface1: {len(surface1)} id-level rows | surface2: {len(surface2)} section rows | "
          f"surface3: {len(surface3)} H3 HOLD rows listed (standing convention)")
    for s in surface1:
        c = s["top_candidates"][0]
        print(f"  {s['note_title'][:30]:30s} wrong={s['wrong_code']:10s} -> {c['code']:10s} "
              f"{c['score']:.3f} | {c['wording_store'][:48]}")
    print("  --- surface 2 ---")
    for s in surface2:
        c = s["top_candidates"][0]
        print(f"  {s['note_path'].split('/')[-1][:28]:28s} ord {s['chunk_ordinal']} "
              f"cur={s['current_code']:10s} -> {c['code']:10s} {c['score']:.3f} [{s['root']}]")
    print("  --- surface 3 (listed, standing convention) ---")
    for s in surface3:
        print(f"  {s['current_code']:11s} ord {s['chunk_ordinal']:2d} "
              f"{s['heading'][:48]!r}")
    print("proposals ->", OUT.relative_to(REPO))
    return 0


if __name__ == "__main__":
    sys.exit(main())
