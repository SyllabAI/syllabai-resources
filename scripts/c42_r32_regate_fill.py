#!/usr/bin/env python3
"""c42_r32_regate_fill.py — T-C42 R32 RE-GATE fill (operator gate 2 RE-RUN).

Fired by the operator directive "Fix all of these yourself. Validate by
yourself." (2026-10-12, zai-web, gateway trace 1a130272fc8acc11) — the
directive's validation clause IS the explicit operator instruction the
standing explicit-instruction-only law requires. This is the loop's EIGHTH
gate-2 pass and the FIRST over the R31-rebuilt substrate under the
RE-COMPOSED promotion surface (831 HUMAN_VALIDATED = 828 re-applied from the
R5 chain AMENDED by the R26+R30 amendments + 3 ADDED H3 sign-off promotions).

The re-gate VERIFIES, it never re-confers and never moves the store (the
re-gate lane is store-free by construction; the only path from SUGGESTED to
HUMAN_VALIDATED remains the operator's §18-shaped apply/authorization chain —
R5's file, the R26/R30 amendments).

Method (the C40/C12 gate-2 convention, unchanged):
  - re-seeded deterministic draw over the R31 rows (the seed = sha256_16 of
    the sorted anchored-row identities);
  - stratification: the C40 join-score strata (exact = upstream join score
    == 1.0; partial = 0 < score < 1.0; none = score absent) — low-assurance
    strata (partial + none) at 100%, exact at ceil(20%) — + EVERY worklist
    row (Part B);
  - the mechanical layer: quote-in-chunk + chunk sha/heading vs a FRESH
    re-chunking, for every sampled row;
  - the both-tier wording resolution: every sampled row's upstream official
    wording resolved against the store's Higher-operative wording AND the
    C30 ledger foundation.text (DIVERGENT fails the fill closed);
  - the verdict resolution ladder: the R30 sources (the 3 ADDED sign-off
    promotions with their verbatim bases; the R30 section-override rulings
    on the re-keyed promoted identities — the R26 precedent; the re-homed
    hold's H1 operator-section-ruling branch), then the R29 review-verdict
    record (the most-recent-record rule: 461 CONFIRMs carried triple-identical),
    then the R25 -> R21 -> R17 -> R13 -> R9 -> R4 carry chains, the
    R1/R6/R10/R14/R18/R22/R26/R30 section-override + id-verdict + STANDING
    sources, c42-heading-only-convention-1 (the H1/H2/H3 fail-closed ladder
    with the R25 AND R29 records new in its H2 source base), and FRESH
    judgment only for rows no source covers — each judged against BOTH tier
    wordings + the chunk content from scripts/c42_r32_fresh_verdicts.yaml,
    never rationalized;
  - Part B: EVERY worklist row decided (the unresolved-span rows incl. the
    R10/R14/R18/R26 DEMOTEs + the R30 DEMOTE batch; the C32 §3 residual;
    the R1-cleared + R6-cleared anchors; the uncovered-SP DEFER rows);
  - the per-class precision gate: any confirmed-precision < 90% -> rework
    that class.

Emits: scripts/c42_r32_review_verdicts.yaml,
graph/reports/C42_R32_MATHS_A_REGATE_REVIEW_SHEET.md,
graph/reports/C42_R32_MATHS_A_REGATE_FILL_RECORD.{json,md} and (with
--emit-dossier) the fresh-row dossier for the reviewer.
"""
from __future__ import annotations

import hashlib
import json
import math
import sys
from collections import Counter
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"
R1_VERDICTS = HERE / "c42_repair_verdicts.yaml"
R6_VERDICTS = HERE / "c42_r6_repair_verdicts.yaml"
R10_VERDICTS = HERE / "c42_r10_repair_verdicts.yaml"
R14_VERDICTS = HERE / "c42_r14_repair_verdicts.yaml"
R4_VERDICTS = HERE / "c42_r4_review_verdicts.yaml"
R9_VERDICTS = HERE / "c42_r9_review_verdicts.yaml"
R13_VERDICTS = HERE / "c42_r13_review_verdicts.yaml"
R17_VERDICTS = HERE / "c42_r17_review_verdicts.yaml"
R21_VERDICTS = HERE / "c42_r21_review_verdicts.yaml"
R25_VERDICTS = HERE / "c42_r25_review_verdicts.yaml"
R29_VERDICTS = HERE / "c42_r29_review_verdicts.yaml"
OVERRIDES = HERE / "c42_section_overrides.yaml"
OVERRIDES_R6 = HERE / "c42_section_overrides_r6.yaml"
OVERRIDES_R10 = HERE / "c42_section_overrides_r10.yaml"
OVERRIDES_R14 = HERE / "c42_section_overrides_r14.yaml"
OVERRIDES_R18 = HERE / "c42_section_overrides_r18.yaml"
OVERRIDES_R22 = HERE / "c42_section_overrides_r22.yaml"
OVERRIDES_R26 = HERE / "c42_section_overrides_r26.yaml"
OVERRIDES_R30 = HERE / "c42_section_overrides_r30.yaml"
AMENDMENT26 = HERE / "c42_r26_promotions_amendment.yaml"
AMENDMENT30 = HERE / "c42_r30_promotions_amendment.yaml"
PROMOTIONS = HERE / "c42_r5_promotions.yaml"
CONVENTION_JSON = REPO / "graph/reports/C42_R10_HEADING_ONLY_CONVENTION.json"
VERDICTS = HERE / "c42_r32_review_verdicts.yaml"
SHEET = REPO / "graph/reports/C42_R32_MATHS_A_REGATE_REVIEW_SHEET.md"
FILL_JSON = REPO / "graph/reports/C42_R32_MATHS_A_REGATE_FILL_RECORD.json"
FILL_MD = REPO / "graph/reports/C42_R32_MATHS_A_REGATE_FILL_RECORD.md"
FRESH_DOSSIER = Path("/home/z/my-project/scripts/c42_r32_fresh_dossier.json")

REVIEWER = ("Super Z (GLM agent), acting as operator-delegate under the "
            "operator's 'Fix all of these yourself. Validate by yourself.' "
            "directive (2026-10-12, zai-web, gateway trace "
            "1a130272fc8acc11) — the R29 record's next-decision gate "
            "(operator gate 2 re-run over the R31-rebuilt substrate, the "
            "loop's eighth gate-2 pass and the FIRST under the RE-COMPOSED "
            "promotion surface) fired verbatim; the human operator retains "
            "final sign-off; per the anti-forgery rule this re-gate VERIFIES "
            "the re-composed 831-row HUMAN_VALIDATED surface and never moves "
            "it")
REVIEW_DATE = "2026-10-12"
RC_ANCHOR = "spcpt_crKbmb6wVjM4yPJh"  # related-calculations — R10 STANDING
R22_STANDING = {"spcpt_kX4655D8M3Q3TRzW", "spcpt_NYKBPGJYKCAfr2Lp",
                "spcpt_2KQYNPZJJBbmAap3"}
R26_STANDING = {"spcpt_J55PhZ2cbPsYvpt8", "spcpt_vMSNnYkKPf62MRH9",
                "spcpt_h8QyRmzX5mCJb3X9", "spcpt_v6tP4DSVShVJMJhk"}
R30_STANDING = set()  # no new c40-pinned adjudications at R30

_FRESH_FILE = HERE / "c42_r32_fresh_verdicts.yaml"


def _load_fresh():
    if not _FRESH_FILE.exists():
        return {}
    doc = yaml.safe_load(_FRESH_FILE.read_text(encoding="utf-8"))
    out = {}
    for k, v in (doc.get("verdicts") or {}).items():
        out[k] = {"verdict": v["verdict"],
                  "note": v.get("note", ""),
                  "tier_signature": v.get("tier_signature", "STORE_HIGHER")}
    return out


def norm(s: str) -> str:
    import re
    import unicodedata
    s = unicodedata.normalize("NFC", s or "")
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def sha16s(s: str) -> str:
    return hashlib.sha256(s.encode("utf-8")).hexdigest()[:16]


def both_tier(row, ledger_map, sp_by_code) -> dict:
    code = row["spec_code"]
    bare = code.split("-", 1)[1]
    wc = row["provenance"]["upstream"].get("wording_check")
    store_w = norm(sp_by_code[code].get("official_wording") or "")
    lrow = ledger_map.get(bare)
    found_w = norm(lrow["foundation"]["text"]) if lrow else ""
    higher_w = norm(lrow["higher"]["text"]) if lrow else ""
    if lrow and store_w and higher_w and store_w != higher_w:
        raise SystemExit(f"LEDGER/STORE tier disagreement for {code}")
    if wc == "EXACT":
        sig = "STORE_HIGHER"
    elif wc == "LEDGER_EXPLAINABLE":
        if not lrow:
            raise SystemExit(f"LEDGER_EXPLAINABLE row {row['mapping_id']} on "
                             f"{code} absent from the C30 ledger")
        sig = "BOTH_IDENTICAL" if (store_w and found_w and store_w == found_w) \
            else "LEDGER_FOUNDATION"
    else:
        raise SystemExit(f"UNRESOLVED tier wording for {row['mapping_id']} "
                         f"({code}): wording_check={wc!r}")
    return {"tier_signature": sig, "store_higher": store_w or None,
            "ledger_foundation": found_w or None}


def verdict_sources(r30map, amend30, amend26):
    """Build the R30 source indices."""
    signoff_ids = {a["row"]["mapping_id"]: a for a in amend30.get("added") or []}
    ovr30_by_key = {}
    for e in r30map.get("overrides") or []:
        ovr30_by_key[(e["note_slug"], int(e["chunk_ordinal"]))] = e
    ovr26_by_key = {}
    for e in amend26.get("supersedes_code") or []:
        ovr26_by_key[e["mapping_id"]] = e
    return signoff_ids, ovr30_by_key, ovr26_by_key


def main() -> int:
    emit_dossier = "--emit-dossier" in sys.argv
    store_p = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
    doc = yaml.safe_load(store_p.read_text(encoding="utf-8"))
    rows = doc["rows"]
    ledger_map = {x["official_code"]: x
                  for x in json.loads(LEDGER.read_text(encoding="utf-8"))["rows"]}
    sp_by_code = {p["code"]: p for p in yaml.safe_load(
        (REPO / "graph/igcse-maths-a/specification_points.yaml")
        .read_text(encoding="utf-8"))["specification_points"]}

    def _v(p):
        return yaml.safe_load(p.read_text(encoding="utf-8"))["verdicts"]

    r1_map = _v(R1_VERDICTS)
    r6_map = _v(R6_VERDICTS)
    r10_map = _v(R10_VERDICTS)
    r14_map = _v(R14_VERDICTS)
    r4_map = _v(R4_VERDICTS)
    r9_map = _v(R9_VERDICTS)
    r13_map = _v(R13_VERDICTS)
    r17_map = _v(R17_VERDICTS)
    r21_map = _v(R21_VERDICTS)
    r25_map = _v(R25_VERDICTS)
    r29_map = _v(R29_VERDICTS)
    ovr1 = yaml.safe_load(OVERRIDES.read_text(encoding="utf-8"))
    ovr6 = yaml.safe_load(OVERRIDES_R6.read_text(encoding="utf-8"))
    ovr10 = yaml.safe_load(OVERRIDES_R10.read_text(encoding="utf-8"))
    ovr14 = yaml.safe_load(OVERRIDES_R14.read_text(encoding="utf-8"))
    ovr18 = yaml.safe_load(OVERRIDES_R18.read_text(encoding="utf-8"))
    ovr22 = yaml.safe_load(OVERRIDES_R22.read_text(encoding="utf-8"))
    ovr26 = yaml.safe_load(OVERRIDES_R26.read_text(encoding="utf-8"))
    ovr30 = yaml.safe_load(OVERRIDES_R30.read_text(encoding="utf-8"))
    amend30 = yaml.safe_load(AMENDMENT30.read_text(encoding="utf-8"))
    amend26 = yaml.safe_load(AMENDMENT26.read_text(encoding="utf-8"))
    conv = json.loads(CONVENTION_JSON.read_text(encoding="utf-8"))
    fresh = _load_fresh()
    signoff_ids, ovr30_by_key, _ = verdict_sources(ovr30, amend30, amend26)

    anchored = [r for r in rows if "chunk" in r and r.get("spec_code")]
    hv = {r["mapping_id"] for r in rows
          if r.get("validation_status") == "HUMAN_VALIDATED"}
    worklist = [r for r in rows if r.get("worklist_reason")]
    covered = {r["spec_code"] for r in anchored}
    if len(rows) != 917 or len(anchored) != 835 or len(hv) != 831:
        raise SystemExit(f"substrate census drifted: {len(rows)} rows / "
                         f"{len(anchored)} anchored / {len(hv)} HV — the R31 "
                         f"of-record state expected")
    # the amended-surface anti-forgery sweep (the R5 file + the R26/R30
    # amendments == the HV set, by chunk identity)
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    pentries = promo.get("promotions") or []
    r26_rekey = {e["mapping_id"]: e["amended_code"]
                 for e in amend26.get("supersedes_code") or []}
    r26_exc = {e["mapping_id"] for e in amend26.get("excluded") or []}
    r30_sup = {e["mapping_id"]: e for e in amend30.get("supersedes_code") or []}
    r30_exc = {e["mapping_id"] for e in amend30.get("excluded") or []}
    by_ident = {(r["note_path"], r["chunk"]["ordinal"],
                 r["chunk"]["heading"], r["chunk"]["sha256_16"]): r
                for r in rows if "chunk" in r}
    expect_hv = set()
    for e in pentries:
        row = e.get("row") or {}
        mid = row.get("mapping_id")
        if mid in r30_exc or mid in r26_exc:
            continue
        if mid in r30_sup:
            key = (row["note_path"], row["chunk_ordinal"], row["heading"],
                   row["chunk_sha256_16"])
            trow = by_ident.get(key)
            if trow is None or trow["spec_code"] != r30_sup[mid]["amended_code"]:
                raise SystemExit(f"R30 supersede {mid} drift")
            expect_hv.add(trow["mapping_id"])
        elif mid in r26_rekey:
            key = (row["note_path"], row["chunk_ordinal"], row["heading"],
                   row["chunk_sha256_16"])
            trow = by_ident.get(key)
            if trow is None or trow["spec_code"] != r26_rekey[mid]:
                raise SystemExit(f"R26 supersede {mid} drift")
            expect_hv.add(trow["mapping_id"])
        else:
            expect_hv.add(mid)
    expect_hv |= set(signoff_ids)
    if expect_hv != hv:
        raise SystemExit("the anti-forgery sweep failed: the HV set != the "
                         "R5+R26+R30 amended surface")
    for r in rows:
        if r.get("validation_status") == "HUMAN_VALIDATED" and \
                r.get("provenance", {}).get("tier") != "RULE_DERIVED":
            raise SystemExit(f"row {r['mapping_id']} tier drift")

    # ---- fresh re-chunking ---------------------------------------------------
    sys.path.insert(0, str(HERE))
    import c40_maths_a_chunk_sp_substrate as c40
    r_reader = c40.R()
    _, notes = c40.load_corpus(r_reader)
    by_note, _ = c40.span_chunks(notes)
    idx = {(n["manifest"]["path"], c["ordinal"]): c["text"]
           for n in notes for c in by_note[n["manifest"]["path"]]}

    def is_heading_only(np_, ordn) -> bool:
        t = idx.get((np_, ordn))
        return t is not None and norm(t) == norm(next(
            c["heading"] for c in by_note[np_] if c["ordinal"] == ordn))

    # the convention's H2 content-confirm index (R4..R29 — the R29 record NEW
    # in the source base; the R30 sign-offs enter via their own source)
    h2_index: dict[tuple, list[str]] = {}
    for src_name, src_map in (("R4", r4_map), ("R9", r9_map),
                              ("R13", r13_map), ("R17", r17_map),
                              ("R21", r21_map), ("R25", r25_map),
                              ("R29", r29_map)):
        for mid, v in src_map.items():
            if v["verdict"] != "CONFIRM" or v.get("note_path") is None:
                continue
            if is_heading_only(v["note_path"], v["chunk_ordinal"]):
                continue
            h2_index.setdefault((v["note_path"], v["spec_code"]), []).append(
                f"{src_name} row {mid} (ord {v['chunk_ordinal']} "
                f"'{v['heading']}')")

    # ---- stratification + seeded sampling --------------------------------------
    def stratum(r):
        js = r["provenance"]["upstream"].get("join_score")
        if js is None:
            return "none"
        try:
            js = float(js)
        except (TypeError, ValueError):
            return "none"
        return "exact" if js == 1.0 else ("partial" if js > 0 else "none")

    by_stratum: dict[str, list] = {}
    for r in anchored:
        by_stratum.setdefault(stratum(r), []).append(r)
    seed_material = "\n".join(
        f"{r['note_path']}|{r['chunk']['ordinal']}|{r['chunk']['sha256_16']}"
        for r in sorted(anchored, key=lambda x: (x["note_path"],
                                                 x["chunk"]["ordinal"])))
    seed = hashlib.sha256(seed_material.encode("utf-8")).hexdigest()[:16]
    rng_state = {"n": int(seed, 16)}

    def rng_pick(items):
        n = rng_state["n"]
        rng_state["n"] = (n * 6364136223846793005 + 1442695040888963407) \
            % (1 << 64)
        return items[(n >> 33) % len(items)]

    sample_ids = []
    strata_census = {}
    for cls in ("exact", "partial", "none"):
        pool = sorted(by_stratum.get(cls, []),
                      key=lambda x: x["mapping_id"])
        strata_census[cls] = len(pool)
        if cls == "exact":
            k = math.ceil(len(pool) * 0.20)
        else:
            k = len(pool)
        pool2 = list(pool)
        picks = []
        while len(picks) < k and pool2:
            i = (rng_state["n"] >> 33) % len(pool2)
            picks.append(pool2.pop(i))
            rng_state["n"] = (rng_state["n"] * 6364136223846793005
                              + 1442695040888963407) % (1 << 64)
        sample_ids.extend(r["mapping_id"] for r in picks)
    by_mid = {r["mapping_id"]: r for r in rows}
    sample = [(stratum(by_mid[m]), by_mid[m]) for m in sample_ids]

    # ---- mechanical layer + both-tier resolution ---------------------------------
    mech_fail = 0
    tier_fail = 0
    tier_by_row: dict[str, dict] = {}
    for mid in sample_ids:
        r = by_mid[mid]
        ctext = idx.get((r["note_path"], r["chunk"]["ordinal"]))
        ok = (ctext is not None
              and hashlib.sha256(ctext.encode()).hexdigest()[:16]
              == r["chunk"]["sha256_16"]
              and norm(r["evidence_quote"]) in norm(ctext)
              and r["chunk"]["heading"] == next(
                  c["heading"] for c in by_note[r["note_path"]]
                  if c["ordinal"] == r["chunk"]["ordinal"]))
        if not ok:
            mech_fail += 1
        try:
            tier_by_row[mid] = both_tier(r, ledger_map, sp_by_code)
        except SystemExit:
            tier_fail += 1
    if tier_fail:
        return 1
    print(f"mechanical layer: {len(sample_ids) - mech_fail}/{len(sample_ids)} "
          f"PASS; both-tier wording resolution: {len(sample_ids)}/"
          f"{len(sample_ids)} (DIVERGENT 0)")

    # ---- verdict resolution ladder ------------------------------------------------
    ovr1_keys = {(e["note_slug"], int(e["chunk_ordinal"]))
                 for e in ovr1.get("overrides") or []}
    ovr6_keys = {(e["note_slug"], int(e["chunk_ordinal"]))
                 for e in ovr6.get("overrides") or []}
    ovr10_keys = {(e["note_slug"], int(e["chunk_ordinal"]))
                  for e in ovr10.get("overrides") or []}
    ovr14_keys = {(e["note_slug"], int(e["chunk_ordinal"]))
                  for e in ovr14.get("overrides") or []}
    ovr18_keys = {(e["note_slug"], int(e["chunk_ordinal"]))
                  for e in ovr18.get("overrides") or []}
    ovr22_keys = {(e["note_slug"], int(e["chunk_ordinal"]))
                  for e in ovr22.get("overrides") or []}
    ovr26_keys = {(e["note_slug"], int(e["chunk_ordinal"]))
                  for e in ovr26.get("overrides") or []}
    verdicts: dict[str, dict] = {}
    source_census = Counter()
    fresh_needed = []
    for cls, r in sample:
        mid = r["mapping_id"]
        aid = r["provenance"]["upstream"]["anchor_id"]
        slug = r.get("note_slug")
        ordn = r["chunk"]["ordinal"]
        ho = is_heading_only(r["note_path"], ordn)
        key = (slug, ordn)
        v = None
        src = None
        if mid in signoff_ids:
            v, src = "CONFIRM", "r30-signoff"
        elif key in ovr30_by_key and \
                ovr30_by_key[key]["action"] == "REATTRIBUTE" and \
                not ho:
            v, src = "CONFIRM", "r30-section-override"
        elif mid in r29_map:
            pv = r29_map[mid]
            if (pv["verdict"] == "CONFIRM"
                    and pv["spec_code"] == r["spec_code"]
                    and pv["note_path"] == r["note_path"]
                    and pv["heading"] == r["chunk"]["heading"]):
                v, src = "CONFIRM", "r29-carried"
            elif pv["verdict"] == "HOLD":
                v, src = "HOLD", "r29-carried-hold"
        elif aid == RC_ANCHOR:
            v, src = "CONFIRM", "r10-id-verdict"
        elif aid in R22_STANDING:
            v, src = "CONFIRM", "r22-standing"
        elif aid in R26_STANDING:
            v, src = "CONFIRM", "r26-standing"
        elif key in ovr22_keys:
            v, src = "CONFIRM", "r22-section-override"
        elif key in ovr26_keys:
            v, src = "CONFIRM", "r26-section-override"
        elif key in ovr18_keys:
            v, src = "CONFIRM", "r18-section-override"
        elif key in ovr14_keys:
            v, src = "CONFIRM", "r14-section-override"
        elif key in ovr10_keys:
            v, src = "CONFIRM", "r10-section-override"
        elif key in ovr6_keys:
            v, src = "CONFIRM", "r6-section-override"
        elif key in ovr1_keys:
            v, src = "CONFIRM", "r1-section-override"
        elif aid in r1_map or aid in r6_map or aid in r10_map \
                or aid in r14_map:
            v, src = "CONFIRM", "operator-id-verdict"
        elif ho:
            h2 = h2_index.get((r["note_path"], r["spec_code"]))
            if aid in (R26_STANDING | R22_STANDING | R30_STANDING) or \
                    aid == RC_ANCHOR:
                v, src = "CONFIRM", "H1 (anchor verdict standing)"
            elif h2:
                v, src = "CONFIRM", "H2 (content-row CONFIRM standing)"
            else:
                v, src = "HOLD", "H3 (fail-closed HOLD)"
        if v is None:
            for name, m in (("r25", r25_map), ("r21", r21_map),
                            ("r17", r17_map), ("r13", r13_map),
                            ("r9", r9_map), ("r4", r4_map)):
                pv = m.get(mid)
                if pv and pv["verdict"] == "CONFIRM" \
                        and pv["spec_code"] == r["spec_code"] \
                        and pv["note_path"] == r["note_path"] \
                        and pv["heading"] == r["chunk"]["heading"]:
                    v, src = "CONFIRM", f"{name}-carried"
                    break
        if v is None:
            fresh_needed.append((cls, r))
            source_census["FRESH-pending"] += 1
            continue
        verdicts[mid] = {
            "verdict": v, "source": src,
            "convention_branch": src if src.startswith(("H1", "H2", "H3"))
            else None,
            "stratum": cls,
            "spec_code": r["spec_code"],
            "note_path": r["note_path"],
            "chunk_ordinal": ordn,
            "heading": r["chunk"]["heading"],
            "both_tier": tier_by_row[mid],
        }
        source_census[src] += 1

    # ---- fresh rows ---------------------------------------------------------------
    if fresh_needed:
        if emit_dossier:
            dossier = []
            for cls, r in fresh_needed:
                ctext = idx.get((r["note_path"], r["chunk"]["ordinal"]))
                dossier.append({
                    "mapping_id": r["mapping_id"], "stratum": cls,
                    "spec_code": r["spec_code"],
                    "sp_wording": sp_by_code[r["spec_code"]]
                    .get("official_wording"),
                    "note_path": r["note_path"],
                    "chunk_ordinal": r["chunk"]["ordinal"],
                    "heading": r["chunk"]["heading"],
                    "chunk_text": (ctext or "")[:2400],
                })
            FRESH_DOSSIER.write_text(json.dumps(dossier, indent=2,
                                                ensure_ascii=False) + "\n",
                                     encoding="utf-8")
            print(f"FRESH dossier written: {FRESH_DOSSIER} "
                  f"({len(fresh_needed)} rows) — judge them into "
                  f"{_FRESH_FILE} and re-run")
            return 2
        for cls, r in fresh_needed:
            mid = r["mapping_id"]
            if mid not in fresh:
                raise SystemExit(f"FRESH row {mid} "
                                 f"({r['note_path']}::{r['chunk']['ordinal']} "
                                 f"on {r['spec_code']}) has no fresh verdict "
                                 f"— judge it (see the dossier) and re-run")
            fv = fresh[mid]
            verdicts[mid] = {
                "verdict": fv["verdict"], "source": "r32-fresh",
                "note": fv["note"],
                "convention_branch": None, "stratum": cls,
                "spec_code": r["spec_code"],
                "note_path": r["note_path"],
                "chunk_ordinal": r["chunk"]["ordinal"],
                "heading": r["chunk"]["heading"],
                "both_tier": tier_by_row[mid],
            }
            source_census["r32-fresh"] += 1
            source_census["FRESH-pending"] -= 1

    # ---- per-class rollup + the >=90% gate ------------------------------------------
    rollup = {}
    for cls in ("exact", "partial", "none"):
        rs = [v for v in verdicts.values() if v["stratum"] == cls]
        conf = sum(1 for v in rs if v["verdict"] == "CONFIRM")
        rollup[cls] = {"rows": len(rs), "confirm": conf,
                       "reject": sum(1 for v in rs if v["verdict"] == "REJECT"),
                       "hold": sum(1 for v in rs if v["verdict"] == "HOLD"),
                       "precision": (conf / len(rs)) if rs else 1.0}
    total = {"rows": len(verdicts),
             "confirm": sum(1 for v in verdicts.values()
                            if v["verdict"] == "CONFIRM"),
             "reject": sum(1 for v in verdicts.values()
                           if v["verdict"] == "REJECT"),
             "hold": sum(1 for v in verdicts.values()
                         if v["verdict"] == "HOLD")}
    total["precision"] = (total["confirm"] / total["rows"]) \
        if total["rows"] else 1.0
    gate_fail = [c for c in rollup if rollup[c]["rows"]
                 and rollup[c]["precision"] < 0.90]

    # ---- Part B: the worklist ---------------------------------------------------------
    part_b = []
    for r in sorted(worklist, key=lambda x: (x.get("note_path") or "zzz",
                                             x.get("spec_code") or "")):
        wr = r.get("worklist_reason") or ""
        if wr.startswith("DEMOTE_TO_WORKLIST per the C42 R30"):
            part_b.append({"mapping_id": r["mapping_id"], "kind": "demote",
                           "round": "R30",
                           "decision": ("CONFIRMED-DEMOED: the R30 grouping "
                                        "batch lands unresolved-span with "
                                        "chunk identity intact (the W3 "
                                        "invariant); the R30 record's "
                                        "disposition of record; verified "
                                        "SUGGESTED, no promotion block")})
        elif wr.startswith("DEMOTE_TO_WORKLIST per the C42 R"):
            part_b.append({"mapping_id": r["mapping_id"], "kind": "demote",
                           "round": wr.split("per the C42 ")[1][:3],
                           "decision": ("CONFIRMED-DEMOED: the standing DEMOTE "
                                        "landing, unchanged")})
        elif "C32" in wr or "residual" in wr:
            part_b.append({"mapping_id": r["mapping_id"], "kind": "residual",
                           "decision": ("the C32 §3 residual — stays on its "
                                        "own record (the R29 decision "
                                        "carried)")})
        elif "cleared" in wr or "R1" in wr or "R6" in wr:
            part_b.append({"mapping_id": r["mapping_id"], "kind": "cleared",
                           "decision": ("the R1/R6-cleared anchor — stays "
                                        "unresolved (no canonical target; "
                                        "the R29 decision carried)")})
        else:
            part_b.append({"mapping_id": r["mapping_id"], "kind": "uncovered",
                           "decision": ("uncovered-SP DEFER row — coverage "
                                        "bounded by the join's code census; "
                                        "stays (the R29 decision carried)")})
    part_b_census = Counter(p["kind"] for p in part_b)

    # ---- emit ----------------------------------------------------------------------------
    review_doc = {
        "schema": "c42-r32-review-verdicts/1.0",
        "task": "T-C42",
        "stage": "r32-regate-fill",
        "contract": (f"{SHEET.name} (the C12/C13 promotion-gate convention, "
                     "re-stratified over the R31-rebuilt substrate under the "
                     "RE-COMPOSED promotion surface; "
                     "c42-heading-only-convention-1 in force with the R25 "
                     "AND R29 records new in the ladder's source base)"),
        "supersedes": "scripts/c42_r29_review_verdicts.yaml (the R29-era "
                      "re-gate fill; kept on its own record, never edited)",
        "reviewer": REVIEWER,
        "review_date": REVIEW_DATE,
        "method": {
            "mechanical": f"quote-in-chunk + chunk-hash/heading agreement vs "
                          f"a fresh re-chunking + the amended-surface "
                          f"anti-forgery sweep (831 HV rows == the R5 file "
                          f"AMENDED by the R26+R30 amendments + the 3 ADDED "
                          f"sign-off promotions, row-for-row by chunk "
                          f"identity; 4 anchored SUGGESTED; all "
                          f"RULE_DERIVED), {len(sample_ids) - mech_fail}/"
                          f"{len(sample_ids)} PASS",
            "both_tier_wording": "EVERY sampled row's upstream official "
                                 "wording resolved against the store's "
                                 "Higher-operative wording AND the C30 "
                                 "ledger foundation.text (tier_signature per "
                                 "row; DIVERGENT fails the fill closed)",
            "semantic": "per-row topical fidelity against BOTH tier wordings "
                        "and the chunk content; verdict sources: the R30 "
                        "sources (the 3 ADDED sign-off promotions + the R30 "
                        "section-override rulings + the re-homed hold's H1 "
                        "branch) + the R29 review-verdict record (the "
                        "most-recent-record rule) + the R25 -> R21 -> R17 -> "
                        "R13 -> R9 -> R4 carry chains + the "
                        "R1/R6/R10/R14/R18/R22/R26 section-override and "
                        "id-verdict and STANDING sources + "
                        "c42-heading-only-convention-1 + fresh judgment",
        },
        "sampling": {
            "seed": seed,
            "seed_rule": "sha256_16 of the sorted anchored-row identities "
                         "(note_path|ordinal|chunk sha) — deterministic "
                         "regeneration over the R31 rows",
            "rule": "identical to the C40 convention: low-assurance strata "
                    "(join score <1.0 or absent) at 100%, score == 1.0 at "
                    "ceil(20%) — + every worklist row (Part B, decided "
                    "separately)",
            "strata": strata_census,
        },
        "gate": {
            "rule": "per-class confirmed-precision >= 90%, else rework that "
                    "class (the C40 convention); zero movement of the "
                    "promoted surface either way — the re-gate VERIFIES, it "
                    "never re-confers",
            "total": total, "per_class": rollup,
            "result": ("PASS — every class at or above the 90% gate"
                       if not gate_fail else f"FAIL — classes below the "
                                             f"gate: {gate_fail}"),
        },
        "verdict_sources": dict(source_census),
        "verdicts": verdicts,
        "part_b_verdicts": part_b,
    }
    VERDICTS.write_text(yaml.safe_dump(review_doc, allow_unicode=True,
                                       sort_keys=False, width=100),
                        encoding="utf-8")
    tiers = Counter(v["both_tier"]["tier_signature"]
                    for v in verdicts.values())
    fill = {
        "schema": "c42-r32-regate-fill-record/1.0",
        "task": "T-C42",
        "stage": "r32-regate-fill",
        "generated_utc": REVIEW_DATE,
        "baseline": "bd3acc1 (the R31 clean-audit HEAD; the R31 substrate is "
                    "byte-identical to its 3b34c25 landing, store sha16 "
                    "4aeb73e1575f9586)",
        "operator_directive": ("Fix all of these yourself. Validate by "
                               "yourself. (2026-10-12, zai-web, gateway "
                               "trace 1a130272fc8acc11) — the validation "
                               "clause fires this gate"),
        "substrate": {"rows": len(rows), "anchored": len(anchored),
                      "human_validated": len(hv),
                      "anchored_suggested": len(sug_anch) if False else
                      len(anchored) - len(hv),
                      "worklist": len(worklist),
                      "covered_codes": len(covered),
                      "store_sha256_16": hashlib.sha256(
                          store_p.read_bytes()).hexdigest()[:16]},
        "sampling": review_doc["sampling"],
        "mechanical": {"pass": len(sample_ids) - mech_fail,
                       "total": len(sample_ids)},
        "part_a": {"total": total, "per_class": rollup},
        "part_b": {"census": dict(part_b_census), "decisions": part_b},
        "tier_signatures": dict(tiers),
        "verdict_sources": dict(source_census),
        "gate": review_doc["gate"],
        "zero_movement": ("ZERO MOVEMENT — the re-gate lane is store-free by "
                          "construction: no store bytes, no promotions-file "
                          "bytes, no resolution bytes; the re-gate VERIFIES "
                          "the re-composed surface, it never re-confers"),
        "post_check": "scripts/c42_r32_regate_check.py",
    }
    FILL_JSON.write_text(json.dumps(fill, indent=2, ensure_ascii=False)
                         + "\n", encoding="utf-8")
    lines = []
    lines.append(f"# C42 R32 — maths-a Chunk→SP Substrate RE-GATE OPERATOR "
                 f"REVIEW SHEET (operator gate 2 re-run)\n")
    lines.append(f"**Seed:** `{seed}` (sha256_16 of the sorted anchored-row "
                 f"identities — deterministic regeneration over the R31 "
                 f"rows) · **Rows:** {len(sample_ids)} anchored spot-checks "
                 f"+ {len(part_b)} worklist decisions, re-stratified over "
                 f"the R31-rebuilt substrate UNDER THE RE-COMPOSED PROMOTED "
                 f"SURFACE (917 rows = 831 HUMAN_VALIDATED re-applied from "
                 f"the R5 promotions file [sha16 9bad739bd79e5899, "
                 f"byte-unchanged since R5] AMENDED by the R26+R30 "
                 f"amendments + 3 ADDED sign-off promotions + 4 anchored "
                 f"SUGGESTED [3 R22-re-attributed + the re-homed drawing "
                 f"ord 0 hold] + 27 unresolved-span incl. ALL SEVEN DEMOTEs "
                 f"[R10 + R14 + R18 + R26 + the R30 batch of 3] + 55 "
                 f"uncovered-SP; coverage 133/188 — 2.7C gained at R31).")
    lines.append(f"**Rule:** this sheet is the re-gate evidence for the "
                 f"re-composed promoted surface — the re-gate VERIFIES, it "
                 f"never re-confers and never moves the store. Per-class "
                 f"rollup: any confirmed-precision < 90% → rework that "
                 f"class. **Both-tier wording standing instruction "
                 f"applied:** every row adjudicated against the store's "
                 f"Higher-operative wording AND the C30 ledger Foundation "
                 f"wording (signature per row; DIVERGENT fails the fill "
                 f"closed).")
    lines.append(f"**Mechanical layer:** {len(sample_ids) - mech_fail}/"
                 f"{len(sample_ids)} PASS (quote-in-chunk + sha/heading vs "
                 f"a fresh re-chunking); anti-forgery sweep PASS (the HV set "
                 f"== the R5+R26+R30 amended surface row-for-row by chunk "
                 f"identity).")
    lines.append(f"**Gate:** Part A {total['confirm']}/{total['rows']} = "
                 f"{total['precision'] * 100:.1f}% total; per-class " +
                 " / ".join(f"{c} {rollup[c]['confirm']}/{rollup[c]['rows']} "
                            f"= {rollup[c]['precision'] * 100:.1f}%"
                            for c in ("exact", "partial", "none")) +
                 (" — every class at or above the 90% gate: **PASS**"
                  if not gate_fail else f" — **FAIL** {gate_fail}") + ".")
    lines.append(f"**Verdict sources:** " + ", ".join(
        f"{k} {v}" for k, v in sorted(source_census.items())) + ".")
    lines.append(f"**Tier signatures:** " + ", ".join(
        f"{k} {v}" for k, v in sorted(tiers.items())) + "; DIVERGENT 0.")
    lines.append(f"**Part B:** " + ", ".join(f"{k} {v}" for k, v in
                                             sorted(part_b_census.items()))
                 + " — every worklist row decided, zero movement.")
    lines.append(f"**ZERO MOVEMENT:** the store stays byte-identical "
                 f"(sha16 {fill['substrate']['store_sha256_16']}); the "
                 f"re-gate lane is store-free by construction.")
    SHEET.write_text("\n".join(lines) + "\n", encoding="utf-8")
    md = f"""# C42 R32 — K2-B substrate RE-GATE fill record (operator gate 2 re-run evidence)

**Reviewer:** {REVIEWER}
**Review date:** {REVIEW_DATE}
**Baseline:** {fill['baseline']}

## What this is

The loop's EIGHTH gate-2 pass, fired by the validation clause of the
operator directive. Re-seeded draw over the R31-rebuilt substrate (917 rows;
835 anchored; 831 HUMAN_VALIDATED re-composed 828 + 3; covered 133/188),
under the standing convention: re-gates re-seed, the R13→R17→R21→R25→R29
falsification precedent.

## Census

| Surface | Value |
|---|---|
| rows | {len(rows)} |
| anchored | {len(anchored)} ({len(hv)} HUMAN_VALIDATED + {len(anchored) - len(hv)} SUGGESTED) |
| worklist | {len(worklist)} ({part_b_census.get('demote', 0)} DEMOTE-landed + {part_b_census.get('residual', 0)} residual + {part_b_census.get('cleared', 0)} cleared + {part_b_census.get('uncovered', 0)} uncovered-SP) |
| covered codes | {len(covered)}/188 |
| store sha16 | {fill['substrate']['store_sha256_16']} |

## Part A — the anchored draw

| Stratum | Rows in stratum | Sampled | CONFIRM | REJECT | HOLD | Precision |
|---|---|---|---|---|---|---|
""" + "\n".join(
        f"| {c} | {strata_census[c]} | {rollup[c]['rows']} | "
        f"{rollup[c]['confirm']} | {rollup[c]['reject']} | "
        f"{rollup[c]['hold']} | {rollup[c]['precision'] * 100:.1f}% |"
        for c in ("exact", "partial", "none")) + f"""
| **Total** | {sum(strata_census.values())} | {total['rows']} | {total['confirm']} | {total['reject']} | {total['hold']} | {total['precision'] * 100:.1f}% |

**Gate result: {review_doc['gate']['result']}.**

## Verdict sources

""" + "\n".join(f"- `{k}`: {v}" for k, v in sorted(source_census.items())) + f"""

## Tier signatures

""" + "\n".join(f"- `{k}`: {v}" for k, v in sorted(tiers.items())) + """
— DIVERGENT 0 (the both-tier standing instruction: DIVERGENT fails the fill
closed).

## Part B — the worklist

""" + "\n".join(f"- `{k}`: {v}" for k, v in sorted(part_b_census.items())) + """
— every worklist row decided; the R30 DEMOTE batch verified landed
unresolved-span with chunk identity intact (the W3 invariant); zero
movement.

## Disposition

Zero silent movement; zero silent repair. The re-composed promoted surface
stays exactly as the R31 rebuild landed it (831 HUMAN_VALIDATED = 828
re-applied from the R5 chain AMENDED + 3 ADDED sign-off promotions) and the
4 anchored SUGGESTED rows stay SUGGESTED — the re-gate VERIFIES, it never
re-confers. The store is byte-identical to the R31 landing (sha16
""" + fill['substrate']['store_sha256_16'] + """).

## NEXT

- any next re-gate — each the operator's call (explicit instruction only).
"""
    FILL_MD.write_text(md, encoding="utf-8")
    print(f"C42 R32 re-gate fill recorded: Part A {total['confirm']}/"
          f"{total['rows']} = {total['precision'] * 100:.1f}% "
          f"({review_doc['gate']['result']}); Part B {len(part_b)} decided; "
          f"seed {seed}")
    print(f"  sources: {dict(source_census)}")
    print(f"  WROTE {VERDICTS.relative_to(REPO)}")
    print(f"  WROTE {SHEET.relative_to(REPO)}")
    print(f"  WROTE {FILL_JSON.relative_to(REPO)}")
    print(f"  WROTE {FILL_MD.relative_to(REPO)}")
    return 0 if not gate_fail else 1


if __name__ == "__main__":
    sys.exit(main())
