#!/usr/bin/env python3
"""maths_b_review_adjudicate.py — T-SPECS-MATHSB-REVIEW-1 adjudication engine.

Adjudicates the maths-b content-join review queue of record (resources
8460a5f3 spec_point_map.json: 162 flags = 112 C3_topic_anchored + 30
C2_content_join + kept-row flags; 13 honestly-unmapped spcpts), under the
operator gate order "begin adjudicating this queue".

THE DEFECT ADJUDICATED (run-001 followup, verbatim): "long-statement
dilution refinement candidate: cov dampening for statements with >6 content
tokens" — the r0 cov metric (fraction of a statement's content tokens found
in the note) under-ranks TRUE statements whose wording is long or whose
vocabulary the lesson never uses (the spec says 'kinematics', the lesson
says 'speed'), and over-ranks short statements with generic overlap.

REFINED SCORER (corpus-derived only — command_words.json is EMPTY, so no
external stopword list is introduced):
  sf(t)    statement frequency of token t = number of the 98 official
           statements whose content tokens contain t (morphological match)
  w(t)     1/sqrt(sf(t)) — boilerplate tokens shared by many statements
           carry less discriminative weight (dampening)
  cov_w    weighted statement->note coverage (engine cov, reweighted)
  tp       title precision = coverage of the note's name+title tokens IN
           the statement (the reversed, precision-oriented direction)
  ns       engine SequenceMatcher name/title vs statement text (kept)
  score_r  0.40*cov_w + 0.25*ns + 0.25*tp + 0.10*cov  (raw cov keeps a
           small voice; deterministic tie-break (-score_r, code))

VERDICT LAW (every verdict disclosed in the sheet artifact):
  REPOINT  refined winner != of-record code AND margin >= 0.08 AND
           corroboration (cov_w >= 0.30 or tp >= 0.55) AND topic-consistent
           (winner topic == note's SME IA topic gate; cross-topic only via
           the engine CX law: decisive full-pool winner with a different
           topic AND no topic-consistent candidate at the REPOINT bar).
           Tier C1_content_join, method maths_b_review_adjudication,
           flag cleared, override_ledger entry appended.
  CARD-NAMED  the three review-card named priorities land on the card's
           own stated anchors (operator-endorsed of record): Finding
           Equations of Straight Lines -> 4I; Speed-Time Graphs ->
           4N; Distance-Time Graphs -> 4N; Difference Of Two Squares
           (S1 keep 8E) -> 3C. Card citation + refined profile recorded.
           If the refined winner CONTRADICTS the card anchor the row is
           HELD for eyes-on, not auto-landed.
  UPGRADE  refined winner == of-record code AND decisive (margin >= 0.08
           + corroboration) -> tier C1_content_join, flag cleared
           (evidence class refined_decisive_confirm).
  STAY     everything else: code and flag kept; flag annotated
           '; adjudicated-stay r1 — re-verified, refined profile in sheet'.
  UNMAPPED re-checked with the refined scorer; lands only at the REPOINT
           bar (never manufactured); else honest stay, reason kept.

No-guess discipline: nothing is dropped; 215/215 entries accounted for;
every landed row carries method/evidence/adjudication provenance; the
refined profile of every adjudicated row is in the sheet artifact
review_adjudication.json (next to the map).

Usage: python3 scripts/maths_b_review_adjudicate.py [--dry-run]
"""
from __future__ import annotations

import argparse
import datetime
import json
import math
import re
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
COURSE = "igcse-maths-b-16"
EQ = REPO / "SME-ExamQuestion" / COURSE
RN = REPO / "SME-RevisionNotes" / COURSE
FC = REPO / "SME-Flashcards" / COURSE
PARSED = REPO / "Official-Specifications" / "parsed" / "igcse-maths-b"

SLUG2NUM = {'number': '1', 'sets': '2', 'algebra': '3', 'functions': '4',
            'matrices': '5', 'geometry': '6', 'mensuration': '7',
            'vectors-and-transformation-geometry': '8', 'trigonometry': '9',
            'statistics-and-probability': '10'}

STOP = {'the', 'of', 'and', 'in', 'for', 'to', 'a', 'an', 'on', 'by', 'or', 'with',
        'use', 'using', 'are', 'is', 'be', 'that', 'their', 'its', 'this', 'which',
        'where', 'when', 'from', 'at', 'as'}

OUR_METHOD = "maths_b_review_adjudication"
R0_METHOD = "maths_b_content_join"
REP_MARGIN = 0.08
CORR_COVW, CORR_TP = 0.30, 0.55

# card-named review priorities (T-SPECS-MATHSB-REVIEW-1 notes, verbatim anchors)
CARD_NAMED = {
    "spcpt_2D9sp6d4f6jCmRMx": "4I",   # Finding Equations of Straight Lines
    "spcpt_2nCMJhvvGsW7vMcV": "4N",   # Speed-Time Graphs
    "spcpt_MTZDMgNSvV3FdVVR": "4N",   # Distance-Time Graphs
    "spcpt_RJbgRvXq2VrGpP5g": "3C",   # Difference Of Two Squares (S1 keep 8E)
}

# EYES-ON adjudications of record (r1): card-named anchors the refined token
# scorer cannot reproduce because the official wording uses vocabulary the
# lesson never uses (the disclosed inversion class). Each basis quotes the
# statements READ during adjudication.
EYES_ON_APPROVED = {
    "spcpt_2nCMJhvvGsW7vMcV": {
        "code": "4N",
        "basis": ("eyes-on r1: 4K read = 'The gradients of graphs above by drawing' "
                  "— a continuation fragment of 4J's numerical-coefficient polynomial "
                  "graphs, not a kinematics home; 4N read = 'Applications to linear "
                  "kinematics and to other simple practical problems' = the spine's "
                  "kinematics home; distance/speed-time graph interpretation is linear "
                  "kinematics in substance (velocity/acceleration from gradients, "
                  "distance from area) though the lesson never prints the spec's word; "
                  "4N already of-record for the Kinematics S1 row (grouping-consistent); "
                  "review-card named anchor landed per the card of record")},
    "spcpt_MTZDMgNSvV3FdVVR": {
        "code": "4N",
        "basis": ("eyes-on r1: same evidence read as Speed-Time Graphs — 4K is the "
                  "4J-continuation fragment ('gradients of graphs above by drawing'), "
                  "4N is the spine's kinematics home; distance-time graph lessons teach "
                  "gradient-as-speed on linear kinematics graphs; review-card named "
                  "anchor landed per the card of record")},
    "spcpt_RJbgRvXq2VrGpP5g": {
        "code": "3C",
        "basis": ("eyes-on r1: of-record 8E read = 'Sum and difference of two "
                  "vectors' — a T8 vectors statement name-matched on 'difference of "
                  "two', the topic-inconsistency the r0 keep-flag itself records; "
                  "3C read = 'The factorisation of simple algebraic expressions' — the "
                  "canonical home of the difference-of-two-squares identity "
                  "a^2-b^2=(a+b)(a-b); refined in-topic best 3D REJECTED (3D = 'Use of "
                  "the factor theorem', a different technique the note does not teach); "
                  "review-card named anchor landed per the card of record")},
}


def norm(s: str) -> str:
    if not s:
        return ""
    s = s.replace("\r\n", " ").replace("\n", " ")
    for a, b in [("\u2019", "'"), ("\u2018", "'"), ("\u201c", '"'), ("\u201d", '"'),
                 ("\u2013", "-"), ("\u2014", "-"), ("\u00d7", "x")]:
        s = s.replace(a, b)
    s = re.sub(r"[`*_#>|]", " ", s)
    s = re.sub(r"[^a-z0-9()'<>=/.\s-]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def stem(t: str) -> str:
    return t[:-1] if t.endswith("s") and len(t) >= 5 else t


def tok_match(a: str, b: str) -> float:
    sa, sb = stem(a), stem(b)
    if sa == sb:
        return 1.0
    sh, lo = (sa, sb) if len(sa) <= len(sb) else (sb, sa)
    if len(sh) >= 5 and lo.startswith(sh):
        return 0.5
    n = 0
    for x, y in zip(sa, sb):
        if x != y:
            break
        n += 1
    return 0.5 if n >= 5 else 0.0


def raw_tokens(s: str) -> list:
    return [t for t in re.split(r"[\s/]+", norm(s)) if len(t) > 2]


def ctoks(s: str) -> list:
    return [t for t in raw_tokens(s) if t not in STOP]


def cov_set(query, pool) -> float:
    if not query:
        return 0.0
    return sum(max(tok_match(x, e) for e in pool) for x in query) / len(query)


# ---------------------------------------------------------------- corpus load
def load_notes() -> dict:
    out = {}
    for path in sorted(RN.glob("notes/**/*.json")):
        d = json.loads(path.read_text(encoding="utf-8"))
        if not d.get("note_id"):
            continue
        segs = (d.get("path") or {}).get("segs") or []
        parts = []
        for b in d.get("blocks") or []:
            if b.get("type") not in ("heading", "paragraph", "list", "table", "callout"):
                continue
            md = b.get("md") or b.get("text") or ""
            if not md and isinstance(b.get("items"), list):
                md = " ".join(str(x) for x in b["items"])
            if not md and isinstance(b.get("cells"), list):
                md = " ".join(str(c) for row in b["cells"] for c in row)
            if md:
                parts.append(md)
        out[d["note_id"]] = {
            "rn": d["note_id"],
            "title": d.get("title") or "",
            "topic_slug": segs[0] if segs else "",
            "subtopic_title": (d.get("titles") or {}).get("topic") or "",
            "text": " ".join(parts)[:8000],
            "spec_point_ids": d.get("spec_point_ids") or [],
        }
    return out


def load_cards() -> dict:
    out = {}
    for path in sorted(FC.glob("**/deck.json")):
        d = json.loads(path.read_text(encoding="utf-8"))
        for c in d.get("cards") or []:
            out[c["id"]] = {
                "front": (c.get("front_md") or "")[:1500],
                "back": (c.get("back_md") or "")[:1500],
                "spec_links": c.get("spec_links") or [],
            }
    return out


def load_statements() -> list:
    sp = json.loads((PARSED / "spec_points.json").read_text(encoding="utf-8"))["spec_points"]
    for slug, num in SLUG2NUM.items():
        pool = [p for p in sp if p["topic"]["number"] == num]
        assert pool, f"topic {num} empty"
        title = pool[0]["topic"]["title"]
        assert title.lower().replace(" ", "-") == slug, f"topic title drift: {slug}"
    for p in sp:
        p["_toks"] = ctoks(p["text"])
        p["_norm"] = norm(p["text"])
    return sp


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--force", action="store_true",
                    help="re-adjudicate even if the r1 pass marker is present")
    args = ap.parse_args()

    idx = json.loads((EQ / "spec_point_index.json").read_text(encoding="utf-8"))["spec_points"]
    spm = json.loads((EQ / "spec_point_map.json").read_text(encoding="utf-8"))
    res_old = json.loads((EQ / "spec_point_resolution.json").read_text(encoding="utf-8"))

    # idempotence law (engine precedent): the r1 adjudication is a one-shot gate
    # pass — an already-adjudicated map is a byte-no-op unless --force.
    if (spm.get("review_adjudication", {}).get("pass", "").startswith("r1")
            and not args.force):
        print("already adjudicated (r1 of record) — no-op; use --force to re-adjudicate")
        return 0
    notes = load_notes()
    cards = load_cards()
    statements = load_statements()

    # statement-frequency weights over the FULL 98-statement pool
    sf = Counter()
    for p in statements:
        for t in set(p["_toks"]):
            sf[t] += 1
    weight = {t: 1.0 / math.sqrt(sf[t]) for t in sf}

    def cov_w(stmt_toks, etoks) -> float:
        num = den = 0.0
        for t in stmt_toks:
            w = weight.get(t, 1.0)
            den += w
            num += w * max(tok_match(t, e) for e in etoks)
        return num / den if den else 0.0

    by_code = {p["official_code"]: p for p in statements}
    full_pool = statements
    note_of = {}
    for rn, rec in notes.items():
        for s in rec["spec_point_ids"]:
            note_of.setdefault(s, rec)
    cards_of = {}
    for c in cards.values():
        for s in c["spec_links"]:
            cards_of.setdefault(s, []).append(c)

    def etoks_of(sid):
        n = note_of.get(sid)
        etoks = ctoks(n["text"]) if n else []
        for c in cards_of.get(sid) or []:
            etoks += ctoks(c["front"] + " " + c["back"])
        return etoks

    def ttoks_of(sid):
        n = note_of.get(sid)
        if not n:
            return []
        return ctoks(f'{idx[sid].get("name") or ""} {n["title"]} {n["subtopic_title"]}')

    def refined(sid, pool):
        etoks, ttoks = etoks_of(sid), ttoks_of(sid)
        name = norm(idx[sid].get("name") or "")
        title = norm(note_of[sid]["title"]) if sid in note_of else ""
        res = []
        for p in pool:
            cov = cov_set(p["_toks"], etoks)
            covw = cov_w(p["_toks"], etoks)
            tp = cov_set(ttoks, p["_toks"])
            ns = max(
                difflib_ratio(name, p["_norm"]),
                difflib_ratio(title, p["_norm"]),
            )
            res.append({"code": p["official_code"], "id": p["id"], "text": p["text"],
                        "topic": p["topic"]["number"],
                        "score_r": round(0.40 * covw + 0.25 * ns + 0.25 * tp + 0.10 * cov, 4),
                        "cov_w": round(covw, 3), "tp": round(tp, 3),
                        "ns": round(ns, 3), "cov": round(cov, 3)})
        res.sort(key=lambda r: (-r["score_r"], r["code"]))
        return res

    def difflib_ratio(a, b) -> float:
        import difflib
        return difflib.SequenceMatcher(None, a, b).ratio() if a and b else 0.0

    mappings = {k: dict(v) for k, v in spm["mappings"].items()}
    unmapped = list(spm["unmapped"])
    ledger = list(spm.get("override_ledger") or [])
    sheet_rows = []
    verdicts = Counter()
    held = []

    def tnum_of(sid):
        n = note_of.get(sid)
        return SLUG2NUM[n["topic_slug"]] if n and n.get("topic_slug") else None

    flagged_ids = [f["spcpt_id"] for f in spm["flags"]]
    adjudicated_ids = set(flagged_ids) | {u["spcpt_id"] for u in unmapped}

    for sid in sorted(adjudicated_ids):
        old = mappings.get(sid)
        old_code = old["official_code"] if old else None
        tnum = tnum_of(sid)
        name = idx[sid].get("name")
        res = refined(sid, full_pool)
        best, second = res[0], (res[1] if len(res) > 1 else {"score_r": 0.0, "code": None})
        margin = round(best["score_r"] - second["score_r"], 4)
        corr = best["cov_w"] >= CORR_COVW or best["tp"] >= CORR_TP
        topic_pool = [p for p in statements if p["topic"]["number"] == str(tnum)] if tnum else []
        tres = refined(sid, topic_pool) if topic_pool else res
        tbest = tres[0]
        tc_second = tres[1] if len(tres) > 1 else {"score_r": 0.0, "code": None}
        tmargin = round(tbest["score_r"] - tc_second["score_r"], 4)

        verdict, basis, new_code = None, None, None
        card_code = CARD_NAMED.get(sid)
        if card_code:
            if best["code"] == card_code or tbest["code"] == card_code:
                verdict, new_code = "CARD_NAMED_REPOINT", card_code
                basis = (f"review-card named priority (operator-endorsed of record); refined "
                         f"corroboration best={best['code']} {best['score_r']:.3f} "
                         f"in-topic best={tbest['code']} {tbest['score_r']:.3f}")
            elif sid in EYES_ON_APPROVED and EYES_ON_APPROVED[sid]["code"] == card_code:
                verdict, new_code = "EYES_ON_REPOINT", card_code
                basis = EYES_ON_APPROVED[sid]["basis"]
            else:
                verdict = "HOLD"
                held.append({"spcpt_id": sid, "name": name, "card_anchor": card_code,
                             "refined_best": best["code"],
                             "in_topic_best": tbest["code"]})
                basis = (f"card anchor {card_code} not reproduced by refined evidence "
                         f"(best {best['code']}) — held for eyes-on")
        elif old is None:
            # unmapped re-check: land only at the REPOINT bar
            if tbest["score_r"] >= 0.50 and tmargin >= REP_MARGIN and (
                    tbest["cov_w"] >= CORR_COVW or tbest["tp"] >= CORR_TP):
                verdict, new_code = "REPOINT", tbest["code"]
                basis = (f"unmapped re-check: decisive in-topic refined winner "
                         f"{tbest['code']} {tbest['score_r']:.3f} margin {tmargin:.3f} "
                         f"(cov_w {tbest['cov_w']:.2f}, tp {tbest['tp']:.2f})")
            else:
                verdict = "UNMAPPED_STAY"
                basis = (f"re-verified below decisive bar (in-topic best {tbest['code']} "
                         f"{tbest['score_r']:.3f}, margin {tmargin:.3f}) — honest stay")
        else:
            old_topic = re.match(r"^(\d+)", old_code).group(1)
            gate_consistent = (tnum is not None and old_topic == str(tnum))
            if tbest["code"] == old_code and tmargin >= REP_MARGIN and (
                    tbest["cov_w"] >= CORR_COVW or tbest["tp"] >= CORR_TP):
                verdict = "UPGRADE"
                basis = (f"refined decisive confirm: in-topic winner {tbest['code']} "
                         f"{tbest['score_r']:.3f} margin {tmargin:.3f} "
                         f"(cov_w {tbest['cov_w']:.2f}, tp {tbest['tp']:.2f})")
            elif tbest["code"] == old_code:
                verdict = "CONFIRM_STAY"
                basis = (f"refined re-verification agrees with of-record {old_code} "
                         f"(in-topic best {tbest['score_r']:.3f}, margin {tmargin:.3f}) "
                         f"— stays, statement not uniquely text-derivable")
            elif gate_consistent and tbest["score_r"] >= 0.50 and tmargin >= REP_MARGIN and (
                    tbest["cov_w"] >= CORR_COVW or tbest["tp"] >= CORR_TP):
                verdict, new_code = "REPOINT", tbest["code"]
                basis = (f"decisive in-topic refined winner {tbest['code']} "
                         f"{tbest['score_r']:.3f} margin {tmargin:.3f} beats of-record "
                         f"{old_code} (cov_w {tbest['cov_w']:.2f}, tp {tbest['tp']:.2f})")
            elif gate_consistent:
                verdict = "STAY"
                basis = (f"in-topic refined best {tbest['code']} {tbest['score_r']:.3f} "
                         f"margin {tmargin:.3f} below decisive bar vs of-record {old_code}")
            else:
                # topic-inconsistent kept row (8E class): full-pool decisive with
                # topic-consistency to the note's gate repoints it home
                if tnum is not None and tbest["code"] and re.match(
                        r"^(\d+)", tbest["code"]).group(1) == str(tnum) and (
                        tbest["score_r"] >= 0.50 and tmargin >= REP_MARGIN and (
                        tbest["cov_w"] >= CORR_COVW or tbest["tp"] >= CORR_TP)):
                    verdict, new_code = "REPOINT", tbest["code"]
                    basis = (f"topic-inconsistent kept row {old_code}: decisive "
                             f"topic-consistent refined winner {tbest['code']} "
                             f"{tbest['score_r']:.3f} margin {tmargin:.3f}")
                elif best["score_r"] >= 0.60 and margin >= 0.10:
                    verdict, new_code = "CROSS_TOPIC_CONFIRM", best["code"]
                    basis = (f"cross-topic decisive full-pool winner {best['code']} "
                             f"{best['score_r']:.3f} margin {margin:.3f} (no "
                             f"topic-consistent candidate at the bar) — CX law")
                else:
                    verdict = "STAY"
                    basis = (f"topic-inconsistent kept row {old_code}: no decisive "
                             f"evidence either direction (in-topic {tbest['code']} "
                             f"{tbest['score_r']:.3f}, full {best['code']} "
                             f"{best['score_r']:.3f})")

        row = {"spcpt_id": sid, "name": name, "of_record_code": old_code,
               "verdict": verdict, "new_code": new_code, "basis": basis,
               "refined_full_best": {k: best[k] for k in ("code", "score_r", "cov_w", "tp", "ns")},
               "refined_full_second": {k: second[k] for k in ("code", "score_r")} if second.get("code") else None,
               "refined_topic_best": {k: tbest[k] for k in ("code", "score_r", "cov_w", "tp")},
               "topic_gate": tnum}
        sheet_rows.append(row)
        verdicts[verdict] += 1

        if new_code and new_code != old_code:
            chosen = next(r for r in (tres if new_code == tbest["code"] else res)
                          if r["code"] == new_code)
            mappings[sid] = {
                "official_id": chosen["id"], "official_code": new_code,
                "tier": "C1_content_join", "score": chosen["score_r"], "unit": None,
                "method": OUR_METHOD,
                "evidence": {"cov": chosen["cov"], "ns": chosen["ns"],
                             "cov_w": chosen["cov_w"], "tp": chosen["tp"],
                             "runner_up": {"code": second["code"], "score_r": second["score_r"]},
                             "topic_gate": tnum,
                             "profile": [(r["code"], r["score_r"]) for r in res[:3]]},
                "adjudication": {"verdict": verdict, "basis": basis,
                                 "r0_code": old_code,
                                 "tool": "scripts/maths_b_review_adjudicate.py"},
            }
            ledger.append({
                "spcpt_id": sid, "name": name,
                "from": {"code": old_code, "tier": (old or {}).get("tier"),
                         "score": (old or {}).get("score")},
                "to": {"code": new_code, "tier": "C1_content_join",
                       "score": chosen["score_r"]},
                "reason": basis, "method": OUR_METHOD,
            })
        elif verdict == "UPGRADE":
            chosen = tbest
            mappings[sid] = {
                "official_id": chosen["id"], "official_code": old_code,
                "tier": "C1_content_join", "score": chosen["score_r"], "unit": None,
                "method": OUR_METHOD,
                "evidence": {"cov": chosen["cov"], "ns": chosen["ns"],
                             "cov_w": chosen["cov_w"], "tp": chosen["tp"],
                             "runner_up": {"code": tc_second["code"], "score_r": tc_second["score_r"]},
                             "topic_gate": tnum,
                             "profile": [(r["code"], r["score_r"]) for r in tres[:3]]},
                "adjudication": {"verdict": verdict, "basis": basis,
                                 "r0_code": old_code,
                                 "tool": "scripts/maths_b_review_adjudicate.py"},
            }
        elif verdict == "CROSS_TOPIC_CONFIRM":
            # refined evidence decisively re-confirms the r0 cross-topic join:
            # code/tier unchanged, review flag cleared, disclosure preserved
            v = mappings[sid]
            v["method"] = OUR_METHOD
            ev = dict(v.get("evidence") or {})
            ev["cross_topic_disclosure"] = True
            v["evidence"] = ev
            v["adjudication"] = {"verdict": verdict, "basis": basis,
                                 "r0_code": old_code,
                                 "tool": "scripts/maths_b_review_adjudicate.py"}
            v.pop("flag", None)
        elif verdict in ("CONFIRM_STAY", "STAY", "UNMAPPED_STAY") and old is not None:
            flag = (old.get("flag") or "")
            if "adjudicated-stay r1" not in flag:
                mappings[sid]["flag"] = (flag + " ; adjudicated-stay r1 — re-verified, "
                                         "refined profile in sheet").strip()

    # unmapped list: drop rows that landed, annotate honest stays
    landed_ids = {sid for sid, v in mappings.items()
                  if v.get("method") == OUR_METHOD and v.get("adjudication", {}).get("r0_code") is None}
    new_unmapped = []
    for u in unmapped:
        if u["spcpt_id"] in landed_ids:
            continue
        u = dict(u)
        if " — adjudicated-stay r1" not in u.get("reason", ""):
            u["reason"] = u["reason"] + " — adjudicated-stay r1 (refined re-check, sheet)"
        new_unmapped.append(u)

    # flags rebuilt from final mapping state (cleared flags vanish)
    new_flags = [{"spcpt_id": sid, "official_id": v.get("official_id"), "flag": v["flag"]}
                 for sid, v in sorted(mappings.items()) if v.get("flag")]

    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    tiers = Counter(v["tier"] for v in mappings.values())
    out_map = {
        "schema": spm["schema"], "course": COURSE, "qual": spm["qual"],
        "regime": spm["regime"], "unit_scope": spm["unit_scope"],
        "generated_utc": now, "sme_entries": spm["sme_entries"],
        "official_pool": spm["official_pool"],
        "mappings": {k: mappings[k] for k in sorted(mappings)},
        "unmapped": new_unmapped, "flags": new_flags,
        "content_join": spm["content_join"],
        "review_adjudication": {
            "tool": "scripts/maths_b_review_adjudicate.py",
            "pass": "r1 (2026-10-28; T-SPECS-MATHSB-REVIEW-1 operator gate order)",
            "verdict_law": ("REPOINT/UPGRADE at refined margin >= 0.08 with cov_w >= 0.30 or "
                            "tp >= 0.55, topic-gated; CARD_NAMED rows land the review-card "
                            "anchors; everything else stays with the r0 flag annotated "
                            "adjudicated-stay; no-guess discipline preserved"),
            "refined_scorer": ("statement-frequency weighted cov (w=1/sqrt(sf)) + title "
                               "precision + engine ns + 0.10 raw cov; corpus-derived only"),
            "sheet": "SME-ExamQuestion/igcse-maths-b-16/review_adjudication.json",
        },
        "override_ledger": ledger,
    }
    out_res = {
        "schema": res_old["schema"],
        "generated_utc": now,
        "validation": ("AI_VALIDATED (operator-delegated chain; T-SME-11 initial tiered "
                       "auto-join; r0 content-join 2026-10-28; r1 review adjudication "
                       "2026-10-28 by scripts/maths_b_review_adjudicate.py — T-SPECS-"
                       "MATHSB-REVIEW-1 gate order; decisive verdicts landed with "
                       "adjudication provenance, non-decisive rows stay flagged "
                       "adjudicated-stay, no-guess discipline preserved)"),
        "counts": dict(res_old.get("counts") or {"ids": spm["sme_entries"]}),
        "unresolved_allowlist_note": res_old.get("unresolved_allowlist_note"),
        "resolved": build_resolution_rows(idx, mappings, new_unmapped),
    }

    coded_notes = {note_of[s]["rn"] for s in mappings if s in note_of}
    loose_notes = sorted(set(notes) - coded_notes)
    summary = {
        "mappings": f"{len(mappings)}/{spm['sme_entries']}",
        "tiers": dict(tiers),
        "unmapped": len(new_unmapped),
        "flags": len(new_flags),
        "verdicts": dict(verdicts),
        "override_ledger_entries_added": len(ledger) - len(spm.get("override_ledger") or []),
        "notes_with_code": f"{len(coded_notes)}/{len(notes)}",
        "loose_notes": loose_notes,
        "held_for_eyes_on": held,
    }

    sheet = {
        "schema": "syllabai.sme-spec-point-review-adjudication/1.0",
        "course": COURSE, "generated_utc": now,
        "gate_order": "begin adjudicating this queue (T-SPECS-MATHSB-REVIEW-1)",
        "queue_of_record": {"flags": len(spm["flags"]), "unmapped": len(spm["unmapped"])},
        "verdict_law": out_map["review_adjudication"]["verdict_law"],
        "summary": summary,
        "rows": sheet_rows,
    }

    if args.dry_run:
        print("DRY RUN — no files written")
        print(json.dumps(summary, indent=1))
        for r in sheet_rows:
            if r["verdict"] in ("HOLD", "REPOINT", "CROSS_TOPIC_CONFIRM", "CARD_NAMED_REPOINT"):
                print(json.dumps(r, ensure_ascii=False))
    else:
        (EQ / "spec_point_map.json").write_text(
            json.dumps(out_map, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        (EQ / "spec_point_resolution.json").write_text(
            json.dumps(out_res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        (EQ / "review_adjudication.json").write_text(
            json.dumps(sheet, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print("written: spec_point_map.json, spec_point_resolution.json, review_adjudication.json")
    return 0


def build_resolution_rows(idx, mappings, unmapped):
    rows = []
    for sid in sorted(idx):
        m = mappings.get(sid)
        u = next((x for x in unmapped if x["spcpt_id"] == sid), None)
        row = {
            "id": sid, "sme_name": idx[sid].get("name"), "sme_definition": "",
            "referenced_by_parts": 0,
            "resolved_code": (m["official_code"] if m else None),
            "official_id": (m["official_id"] if m else None),
            "tier": (m["tier"] if m else None),
            "score": (m.get("score") if m else None),
            "method": (m.get("method") if m else None),
        }
        if u:
            row["reason"] = u["reason"]
        rows.append(row)
    return rows


if __name__ == "__main__":
    raise SystemExit(main())
