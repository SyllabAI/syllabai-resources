#!/usr/bin/env python3
"""sme_maths_b_content_join.py — evidence-based content join for igcse-maths-b-16.

Closes the maths-b spec-anchor gap (166/199 revision notes render loose on the
hub because their SME spec-point ids sit in spec_point_map.json's unmapped
list). The 2026-09-17 pass (map_spec_points.py regime B) joined names only —
the official 4MB1 spine is course-level coarse (98 statements) while SME's
maths-b spec points are lesson-level (215), so 181/215 fell below the 0.62
name-similarity floor.

This pass joins on CONTENT evidence, all corpus-derived:

  E-topic    the note's SME notes-IA topic (path.segs[0] in the scraped note
             JSON) — byte evidence, corroborated by 25/34 existing S1 rows
  E-content  the note's title + block text + the text of any flashcards whose
             own spec_links declare the spcpt (scraped SME card anchors)

Official pool: the 98 parsed 4MB1 statements
(Official-Specifications/parsed/igcse-maths-b/spec_points.json).

Scoring (stemmed-token containment + statement-similarity + title coverage):
    cov   — fraction of the statement's content tokens matched by the note's
            content tokens (exact 1.0; morphological 0.5: trailing-s stem,
            >=5-char prefix families)
    ns    — best SequenceMatcher(sme name | note title, statement text)
    tcov  — statement tokens covered by the name+title
    score = 0.45*cov + 0.30*ns + 0.25*tcov

Decision law (three passes; deterministic tie-break by (score, code)):

  pass 1 — topic-gated (hard gate on E-topic):
    C1_content_join      score >= 0.60, margin >= 0.05
    C2_content_join      score >= 0.50 (margin >= 0.05: moderate; else ambiguous)
  pass 2 — full-pool fallback (SME IA topic vs official statement topic):
    CX (tier C2)         score >= 0.60, margin >= 0.10, winner's topic !=
                         gate topic -> cross-topic join, flagged
  pass 3 — corroborated topic anchor (the operator-ordered extension; the
    topic placement is certain evidence, the statement within the topic is
    not uniquely text-derivable — the best-scoring statement is recorded
    with a review flag and the full candidate profile):
    C3_topic_anchored    content corroboration (cov >= 0.25 or tcov >= 0.34)
  else unmapped with reason + recorded top candidates.

  flat top-3 within 0.02 in pass 1 skips straight to pass 2/3 (generic
  lessons: no statement is text-derivable; C3 still applies via topic).

Existing 34 S1 rows (T-SME-11 of record):
    agree (same code)                        -> row kept untouched
    topic-inconsistent + decisive new C1     -> repointed, override ledger
    topic-inconsistent + not decisive        -> kept + review flag
    topic-consistent, different new-best     -> kept silently (near-miss
                                                inside the same topic)

Discipline: NO-GUESS beyond the recorded tiers; every attached row carries
tier/method/score/flag; every repoint is disclosed; nothing is dropped.

Outputs (repo-relative):
    SME-ExamQuestion/igcse-maths-b-16/spec_point_map.json          (rewritten)
    SME-ExamQuestion/igcse-maths-b-16/spec_point_resolution.json   (rewritten)

Usage:
    python3 scripts/sme_maths_b_content_join.py [--dry-run]
"""
from __future__ import annotations

import argparse
import datetime
import difflib
import json
import re
from collections import Counter
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
COURSE = "igcse-maths-b-16"
EQ = REPO / "SME-ExamQuestion" / COURSE
RN = REPO / "SME-RevisionNotes" / COURSE
FC = REPO / "SME-Flashcards" / COURSE
PARSED = REPO / "Official-Specifications" / "parsed" / "igcse-maths-b"

SCHEMA_MAP = "syllabai.sme-spec-point-map/1.0"
SCHEMA_RES = "syllabai.sme-spec-point-resolution/1.0"

# SME notes-IA topic slug -> official 4MB1 topic number (1:1 by title;
# verified against the parsed topic titles at load time)
SLUG2NUM = {'number': '1', 'sets': '2', 'algebra': '3', 'functions': '4',
            'matrices': '5', 'geometry': '6', 'mensuration': '7',
            'vectors-and-transformation-geometry': '8', 'trigonometry': '9',
            'statistics-and-probability': '10'}

STOP = {'the', 'of', 'and', 'in', 'for', 'to', 'a', 'an', 'on', 'by', 'or', 'with',
        'use', 'using', 'are', 'is', 'be', 'that', 'their', 'its', 'this', 'which',
        'where', 'when', 'from', 'at', 'as'}

# floors (see module docstring)
C1_SCORE, C1_MARGIN = 0.60, 0.05
C2_SCORE = 0.50
CX_SCORE, CX_MARGIN = 0.60, 0.10
C3_COV, C3_TCOV = 0.25, 0.34
FLAT_DELTA = 0.02
TIE_MARGIN = 0.05


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
    """rn_id -> {title, topic_slug, subtopic_title, text, spec_point_ids}"""
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


def verify_topic_titles() -> dict:
    """official statements indexed by topic number; titles cross-checked."""
    sp = json.loads((PARSED / "spec_points.json").read_text(encoding="utf-8"))["spec_points"]
    by_topic = {}
    for p in sp:
        by_topic.setdefault(p["topic"]["number"], []).append(p)
    # title check: slug must equal the hyphenated official topic title
    for slug, num in SLUG2NUM.items():
        title = by_topic[num][0]["topic"]["title"]
        hy = title.lower().replace(" ", "-")
        assert hy == slug, f"topic title drift: {slug} vs official '{title}'"
    for pool in by_topic.values():
        pool.sort(key=lambda p: (p["official_code"]))
    return by_topic


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    args = ap.parse_args()

    idx = json.loads((EQ / "spec_point_index.json").read_text(encoding="utf-8"))
    entries = idx["spec_points"]
    spm_old = json.loads((EQ / "spec_point_map.json").read_text(encoding="utf-8"))
    notes = load_notes()
    cards = load_cards()

    by_topic = {t: [(p, ctoks(p["text"]), norm(p["text"])) for p in pool]
                for t, pool in verify_topic_titles().items()}
    full_pool = [(p, st, sn) for pool in by_topic.values() for (p, st, sn) in pool]

    # note-side anchors are authoritative (index 'notes' arrays corrupted)
    note_of = {}
    for rn, rec in notes.items():
        for s in rec["spec_point_ids"]:
            note_of.setdefault(s, rec)
    cards_of = {}
    for c in cards.values():
        for s in c["spec_links"]:
            cards_of.setdefault(s, []).append(c)

    def score(v, pool):
        ttoks = ctoks(f'{v["name"]} {v["note"]["title"]} {v["note"]["subtopic_title"]}')
        etoks = ctoks(v["note"]["text"])
        for c in v["cards"]:
            etoks += ctoks(c["front"] + " " + c["back"])
        res = []
        for p, st, sn in pool:
            cov = cov_set(st, etoks)
            tc = cov_set(st, ttoks)
            ns = max(difflib.SequenceMatcher(None, norm(v["name"]), sn).ratio(),
                     difflib.SequenceMatcher(None, norm(v["note"]["title"]), sn).ratio())
            res.append({"code": p["official_code"], "id": p["id"], "text": p["text"],
                        "topic": p["topic"]["number"],
                        "score": round(0.45 * cov + 0.30 * ns + 0.25 * tc, 4),
                        "cov": round(cov, 3), "ns": round(ns, 3), "tcov": round(tc, 3)})
        res.sort(key=lambda r: (-r["score"], r["code"]))
        return res

    mappings = {}
    unmapped = []
    flags = []
    joins = {}
    override_ledger = []

    for sid, e in sorted(entries.items()):
        n = note_of.get(sid)
        if not n or not n.get("topic_slug"):
            unmapped.append({"spcpt_id": sid, "name": e.get("name"),
                             "reason": "no note-side topic anchor"})
            continue
        v = {"name": e.get("name") or "", "note": n,
             "cards": cards_of.get(sid) or []}
        tnum = SLUG2NUM[n["topic_slug"]]
        res = score(v, by_topic[tnum])  # (p, stmt-tokens, stmt-norm) pool
        best = res[0]
        second = res[1] if len(res) > 1 else {"score": 0.0, "code": None}
        third = res[2] if len(res) > 2 else {"score": 0.0, "code": None}
        margin = round(best["score"] - second["score"], 4)
        flat = len(res) >= 3 and third["score"] >= best["score"] - FLAT_DELTA
        profile = [(r["code"], r["score"]) for r in res[:3]]

        d = None
        if not flat:
            if best["score"] >= C1_SCORE and margin >= C1_MARGIN:
                d = {"tier": "C1_content_join", "code": best["code"], "flag": None}
            elif best["score"] >= C2_SCORE and margin >= TIE_MARGIN:
                d = {"tier": "C2_content_join", "code": best["code"],
                     "flag": "moderate content evidence — review"}
            elif best["score"] >= C2_SCORE:
                d = {"tier": "C2_content_join", "code": best["code"],
                     "flag": f"runner-up within {TIE_MARGIN} ({second['code']} {second['score']:.2f}) — review"}
        fres = None
        if d is None:
            fres = score(v, full_pool)
            fb = fres[0]
            fs = fres[1] if len(fres) > 1 else {"score": 0.0, "code": None}
            fm = round(fb["score"] - fs["score"], 4)
            if fb["score"] >= CX_SCORE and fm >= CX_MARGIN and fb["topic"] != tnum:
                d = {"tier": "C2_content_join", "code": fb["code"], "cross_topic": True,
                     "flag": f"cross-topic content join (SME IA T{tnum}, statement T{fb['topic']}) — review"}
        if d is None:
            # corroborated topic anchor
            corr = best["cov"] >= C3_COV or best["tcov"] >= C3_TCOV
            if corr:
                tie = margin < TIE_MARGIN
                d = {"tier": "C3_topic_anchored", "code": best["code"],
                     "flag": ("topic-anchored join within T%s — statement not uniquely "
                              "derivable%s — review" % (tnum, "; tied candidates" if tie else ""))}
        if d:
            if d["code"] == best["code"]:
                chosen = best
            else:
                pool = fres if fres is not None else score(v, full_pool)
                chosen = next(r for r in pool if r["code"] == d["code"])
            row = {"official_id": chosen["id"], "official_code": d["code"],
                   "tier": d["tier"], "score": chosen["score"], "unit": None,
                   "method": "maths_b_content_join",
                   "evidence": {"cov": chosen["cov"], "ns": chosen["ns"],
                                "tcov": chosen["tcov"],
                                "runner_up": {"code": second["code"], "score": second["score"]},
                                "topic_gate": tnum, "profile": profile}}
            if d.get("flag"):
                row["flag"] = d["flag"]
                flags.append({"spcpt_id": sid, "official_id": chosen["id"],
                              "flag": d["flag"]})
            mappings[sid] = row
            joins[sid] = {"tier": d["tier"], "code": d["code"], "topic_gate": tnum,
                          "profile": profile, "note_rn": n["rn"], "cards": len(v["cards"])}
        else:
            unmapped.append({"spcpt_id": sid, "name": e.get("name"),
                             "reason": f"content evidence below corroboration floor "
                                       f"(T{tnum} best {best['code']} {best['score']:.2f}, "
                                       f"cov {best['cov']:.2f}, tcov {best['tcov']:.2f})",
                             "profile": profile})

    # ---- existing mapped rows reconciliation --------------------------------
    # idempotence: rows already produced by this tool (method
    # maths_b_content_join) or already carrying the keep-flag marker are
    # final — recompute their join silently and never re-append flags or
    # re-add ledger entries.
    OUR_METHOD = "maths_b_content_join"
    KEEP_MARKER = "content join below decisive bar"
    prior_ledger = list(spm_old.get("override_ledger") or [])
    prior_ledger_ids = {x.get("spcpt_id") for x in prior_ledger}

    for sid, old in sorted(spm_old.get("mappings", {}).items()):
        if old.get("method") == OUR_METHOD:
            continue                       # ours from a previous run — final
        already_kept = KEEP_MARKER in (old.get("flag") or "")
        if sid not in mappings:
            if not already_kept:
                mappings.setdefault(sid, old)   # no content derivation — verbatim
            else:
                mappings[sid] = old
            continue
        new = mappings[sid]
        old_code, new_code = old["official_code"], new["official_code"]
        if old_code == new_code:
            mappings[sid] = old          # keep the of-record row verbatim
            continue
        old_topic = re.match(r"^(\d+)", old_code).group(1)
        new_topic = re.match(r"^(\d+)", new_code).group(1)
        gate = joins.get(sid, {}).get("topic_gate")
        if old_topic != gate and new_topic == gate and new["tier"] == "C1_content_join":
            if sid not in prior_ledger_ids:
                override_ledger.append({
                    "spcpt_id": sid, "name": entries[sid].get("name"),
                    "from": {"code": old_code, "tier": old.get("tier"), "score": old.get("score")},
                    "to": {"code": new_code, "tier": new["tier"], "score": new["score"]},
                    "reason": f"existing row topic-inconsistent with SME notes IA (T{gate}); "
                              f"decisive topic-consistent C1 content join",
                })
        elif old_topic != gate:
            kept = dict(old)
            if not already_kept:
                kept_flag = ("existing row topic-inconsistent with SME notes IA; "
                             "content join below decisive bar — review")
                kept["flag"] = (kept.get("flag", "") + " " + kept_flag).strip()
            mappings[sid] = kept
            # the flag stays part of the of-record state — always listed
            flags.append({"spcpt_id": sid, "official_id": old.get("official_id"),
                          "flag": kept.get("flag")})
            joins[sid] = {"tier": old.get("tier"), "code": old_code, "kept": True,
                          "topic_gate": gate, "new_best": new_code}
        else:
            # topic-consistent near-miss: keep the of-record row silently
            mappings[sid] = old
            joins[sid] = {"tier": old.get("tier"), "code": old_code, "kept": True,
                          "topic_gate": gate, "new_best": new_code}

    # ---- assemble outputs ---------------------------------------------------
    now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    tiers = Counter(m["tier"] for m in mappings.values())
    out_map = {
        "schema": SCHEMA_MAP,
        "course": COURSE,
        "qual": "igcse-maths-b",
        "regime": "B",
        "unit_scope": None,
        "generated_utc": now,
        "sme_entries": len(entries),
        "official_pool": sum(len(v) for v in by_topic.values()),
        "mappings": {k: mappings[k] for k in sorted(mappings)},
        "unmapped": unmapped,
        "flags": flags,
        "content_join": {
            "tool": "scripts/sme_maths_b_content_join.py",
            "pass": "r0 (2026-10-28; operator-ordered attachment-map extension)",
            "evidence": "note-side anchors (index notes arrays corrupted, disclosed) + "
                        "note block text + anchored-card text; official pool = parsed "
                        "4MB1 statements",
            "tiers": {
                "C1_content_join": "unique content match (score >= 0.60, margin >= 0.05)",
                "C2_content_join": "moderate/ambiguous/cross-topic content match (flagged)",
                "C3_topic_anchored": "topic-certain, statement not uniquely derivable; best "
                                     "content-corroborated statement of the gated topic (flagged)",
            },
            "topic_gate": "note SME notes-IA topic == official topic title (1:1 verified)",
            "tie_break": "(-score, code) — deterministic",
        },
        "override_ledger": prior_ledger + override_ledger,
    }
    unmapped_ids = {x["spcpt_id"] for x in unmapped}
    out_res = {
        "schema": SCHEMA_RES,
        "generated_utc": now,
        "validation": "AI_VALIDATED (operator-delegated chain; T-SME-11 initial tiered "
                      "auto-join; r0 content-join pass 2026-10-28 by "
                      "scripts/sme_maths_b_content_join.py — tiers C1/C2/C3, override "
                      "ledger in spec_point_map.json; C3 rows and all flags are an "
                      "open review queue, no-guess discipline preserved)",
        "counts": {"ids": len(entries)},
        "unresolved_allowlist_note": "parts whose ids are all unresolved stay uncoded by "
                                     "design (no-guess discipline)",
        "resolved": [],
    }
    for sid in sorted(entries):
        u = next((x for x in unmapped if x["spcpt_id"] == sid), None)
        m = mappings.get(sid)
        row = {
            "id": sid,
            "sme_name": entries[sid].get("name"),
            "sme_definition": "",
            "referenced_by_parts": 0,
            "resolved_code": (m["official_code"] if m else None),
            "official_id": (m["official_id"] if m else None),
            "tier": (m["tier"] if m else None),
            "score": (m.get("score") if m else None),
            "method": (m.get("method") if m else None),
        }
        if u:
            row["reason"] = u["reason"]
        out_res["resolved"].append(row)

    if args.dry_run:
        print("DRY RUN — no files written")
    else:
        (EQ / "spec_point_map.json").write_text(
            json.dumps(out_map, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        (EQ / "spec_point_resolution.json").write_text(
            json.dumps(out_res, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
        print("written: spec_point_map.json, spec_point_resolution.json")

    print(f"mappings: {len(mappings)}/{len(entries)}  tiers={dict(tiers)}")
    print(f"unmapped: {len(unmapped)}  flags: {len(flags)}  override_ledger: {len(override_ledger)}")
    coded_notes = {note_of[s]["rn"] for s in mappings if s in note_of}
    print(f"notes with >=1 code: {len(coded_notes)}/{len(notes)}")
    for x in override_ledger:
        print(f"  REPOINT {x['from']['code']} -> {x['to']['code']}: {x['name']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
