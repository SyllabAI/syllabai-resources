#!/usr/bin/env python3
"""
T-SME-EQ-1 — resolve SME spcpt_ ids to official 4CH1 spec codes.

Inputs:
  SME-ExamQuestion/spec_point_index.json   (harvest output)
  graph/specification_points.yaml          (182-point registry, ground truth)
  Chemistry IGCSE Revision Notes/**.md     (spec_map front matter = cross-check)
  SME-ExamQuestion/*/*/topic.json          (subtopic slug -> revision_note_id)

Method (per spcpt id):
  1. normalise SME definition + registry official_wording
     (& -> and, lowercase, strip punctuation, tokenise)
  2. score = max(token_containment, token_f1) blended with sequence ratio
  3. subsection boost: +0.15 when registry subsection == note spec_map
     subsection (slug-anchored, deterministic)
  4. decision:
       a. top1 >= 0.75 and margin >= 0.05 -> definition-match
       b. top1 in containing note's spec_map codes -> definition-match+note-codes
       c. otherwise -> UNRESOLVED queue (scripts/sme_spcpt_decisions.yaml)
  5. cross-check: resolved code vs containing notes' spec_map codes

Validation status: AI_VALIDATED (operator-delegated, see SME-ExamQuestion/
VALIDATION.md). HUMAN_VALIDATED is never emitted.

Usage: python3 scripts/sme_spcpt_resolve.py [--decisions FILE] [--apply]
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import time
from pathlib import Path

import yaml

BASE = Path("/home/z/my-project/download/syllabai-resources")
EQ = BASE / "SME-ExamQuestion"
NOTES_ROOT = BASE / "Chemistry IGCSE Revision Notes"
DECISIONS_DEFAULT = Path(__file__).parent / "sme_spcpt_decisions.yaml"

SUBSECTION_BOOST = 0.15
AUTO_THRESHOLD = 0.75
MARGIN = 0.05

STOP = {"the", "a", "an", "of", "in", "to", "and", "or", "for", "with",
        "on", "at", "by", "is", "are", "be", "that", "this", "their"}


def norm_tokens(text: str) -> list[str]:
    text = text.replace("&", " and ").lower()
    text = re.sub(r"[^a-z0-9.\-\s]", " ", text)
    return [t for t in text.split() if t and t not in STOP]


def score(sme_def: str, official: str) -> float:
    a, b = norm_tokens(sme_def), norm_tokens(official)
    if not a or not b:
        return 0.0
    sa, sb = set(a), set(b)
    inter = len(sa & sb)
    f1 = 2 * inter / (len(sa) + len(sb))
    contain = inter / min(len(sa), len(sb))
    seq = difflib.SequenceMatcher(None, " ".join(a), " ".join(b)).ratio()
    return 0.7 * max(f1, contain) + 0.3 * seq


def load_registry() -> dict[str, dict]:
    doc = yaml.safe_load((BASE / "graph" / "specification_points.yaml")
                         .read_text(encoding="utf-8"))
    return {p["code"]: p for p in doc["specification_points"]}


def note_front_matter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    try:
        return yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None


def notes_by_slug() -> dict[str, dict]:
    """subtopic-slug -> {file, codes, subsection} from notes corpus."""
    out = {}
    for dirpath, _d, fnames in sorted(NOTES_ROOT.walk()):
        for fn in sorted(fnames):
            if not fn.endswith(".md"):
                continue
            p = dirpath / fn
            fm = note_front_matter(p)
            if not fm:
                continue
            src = str(fm.get("source", "")).rstrip("/")
            if not src:
                continue
            slug = src.split("/")[-1]
            sm = fm.get("spec_map") or {}
            codes = [sp.get("code") for sp in sm.get("spec_points", [])
                     if sp.get("code")]
            out[slug] = {"file": str(p.relative_to(BASE)), "codes": codes,
                         "subsection": sm.get("subsection")}
    return out


def slug_to_rn_from_topic_files() -> dict[str, str]:
    """SME's own subtopic slug -> revision_note_id, from exam-question corpus."""
    out = {}
    for f in sorted(EQ.glob("*/*/*/topic.json")) + sorted(
            EQ.glob("*/*/topic.json")):
        t = json.loads(f.read_text(encoding="utf-8"))
        for st in t.get("subtopics", []):
            out[st["slug"]] = st.get("revision_note_id")
    return out


def question_id_refs() -> dict[str, list[str]]:
    """spcpt id -> [topic slugs where referenced by parts]."""
    refs: dict[str, list[str]] = {}
    for f in sorted(EQ.glob("*/*/*/topic.json")) + sorted(
            EQ.glob("*/*/topic.json")):
        t = json.loads(f.read_text(encoding="utf-8"))
        tslug = t["topic"]["slug"]
        for q in t.get("questions", []):
            for part in q.get("parts", []):
                for sid in part.get("spec_point_ids", []) or []:
                    refs.setdefault(sid, [])
                    if tslug not in refs[sid]:
                        refs[sid].append(tslug)
    return refs


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--decisions", default=str(DECISIONS_DEFAULT))
    ap.add_argument("--apply", action="store_true",
                    help="write spec_point_codes into topic.json parts")
    args = ap.parse_args()

    index = json.loads((EQ / "spec_point_index.json")
                       .read_text(encoding="utf-8"))
    registry = load_registry()
    by_sub: dict[str, list[str]] = {}
    for code, p in registry.items():
        by_sub.setdefault(p.get("subsection"), []).append(code)
    notes = notes_by_slug()
    slug_to_rn = slug_to_rn_from_topic_files()
    refs = question_id_refs()

    decisions: dict[str, dict] = {}
    dpath = Path(args.decisions)
    if dpath.exists():
        doc = yaml.safe_load(dpath.read_text(encoding="utf-8")) or {}
        for d in doc.get("decisions", []):
            decisions[d["id"]] = d

    # pre-compute per-slug note anchor
    slug_anchor = {}
    for slug, info in notes.items():
        slug_anchor[slug] = info

    records = []
    queue = []
    for sid, entry in sorted(index["spec_points"].items()):
        sme_def = entry.get("definition") or entry.get("name") or ""
        # anchors: union of notes' codes/subsections over pages showing the id
        note_codes: set[str] = set()
        note_subsections: set[str] = set()
        for slug in entry.get("subtopic_slugs", []):
            info = slug_anchor.get(slug)
            if info:
                note_codes.update(info["codes"])
                if info.get("subsection"):
                    note_subsections.add(info["subsection"])

        scored = []
        for code, p in registry.items():
            s = score(sme_def, p.get("official_wording", ""))
            if p.get("subsection") in note_subsections:
                s += SUBSECTION_BOOST
            scored.append((s, code))
        scored.sort(reverse=True)
        top1_s, top1 = scored[0]
        top2_s, top2 = scored[1]

        resolved, method = None, None
        if top1_s >= AUTO_THRESHOLD and (top1_s - top2_s) >= MARGIN:
            resolved, method = top1, "definition-match"
        elif top1 in note_codes:
            resolved, method = top1, "definition-match+note-codes"

        if sid in decisions:
            dec = decisions[sid]
            resolved = dec["code"]
            method = "ai-adjudicated"
            if resolved not in registry:
                print(f"HARD FAIL: decision code {resolved} not in registry",
                      file=sys.stderr)
                return 3

        rec = {
            "id": sid,
            "sme_name": entry.get("name"),
            "sme_definition": entry.get("definition"),
            "resolved_code": resolved,
            "official_wording": registry[resolved]["official_wording"]
                                if resolved else None,
            "similarity": round(min(top1_s, 1.0), 4),
            "runner_up": {"code": top2, "similarity": round(top2_s, 4)},
            "note_codes": sorted(note_codes),
            "cross_check": ("code_in_note_codes" if resolved in note_codes
                            else "not_in_note_codes") if resolved else None,
            "referenced_by_topics": refs.get(sid, []),
            "method": method,
        }
        records.append(rec)
        if resolved is None:
            queue.append(rec)

    resolved_n = sum(1 for r in records if r["resolved_code"])
    in_notes = sum(1 for r in records if r["cross_check"] == "code_in_note_codes")
    print(f"index ids: {len(records)}  resolved: {resolved_n}  "
          f"unresolved: {len(queue)}")
    print(f"cross-check agree (code in note codes): {in_notes}/{resolved_n}")

    if queue:
        print("\nUNRESOLVED QUEUE (need decisions file entries):")
        for r in queue:
            print(f"  {r['id']}  {r['sme_name']!r} def={r['sme_definition']!r:.90}")
            print(f"    top: {r['runner_up']['code']} "
                  f"({r['runner_up']['similarity']})")
        out = EQ / "spec_point_resolution.json"
        doc = {
            "schema": "syllabai.sme-spec-point-resolution/1.0",
            "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ",
                                           time.gmtime()),
            "validation": "AI_VALIDATED (operator-delegated 2026-09-17); "
                          "HUMAN_VALIDATED reserved for human review",
            "resolved": records,
        }
        out.write_text(json.dumps(doc, ensure_ascii=False, indent=1),
                       encoding="utf-8")
        return 1

    # full doc + optionally apply
    doc = {
        "schema": "syllabai.sme-spec-point-resolution/1.0",
        "generated_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
        "validation": "AI_VALIDATED (operator-delegated 2026-09-17); "
                      "HUMAN_VALIDATED reserved for human review",
        "counts": {
            "ids": len(records),
            "resolved": resolved_n,
            "cross_check_agree": in_notes,
        },
        "resolved": records,
    }
    (EQ / "spec_point_resolution.json").write_text(
        json.dumps(doc, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"wrote {EQ / 'spec_point_resolution.json'}")

    if args.apply:
        id2code = {r["id"]: r["resolved_code"] for r in records}
        parts_total = 0
        missing = 0
        for f in sorted(EQ.glob("*/*/*/topic.json")) + sorted(
                EQ.glob("*/*/topic.json")):
            t = json.loads(f.read_text(encoding="utf-8"))
            changed = False
            for q in t.get("questions", []):
                for part in q.get("parts", []):
                    sids = part.get("spec_point_ids", []) or []
                    codes = [id2code[s] for s in sids if s in id2code]
                    codes = sorted(set(codes),
                                   key=lambda c: registry[c]["global_order"])
                    if sids and not codes:
                        missing += 1
                    if codes:
                        part["spec_point_codes"] = codes
                        changed = True
                    parts_total += 1
            if changed:
                f.write_text(json.dumps(t, ensure_ascii=False, indent=1),
                             encoding="utf-8")
        print(f"applied to {parts_total} parts (parts missing codes: "
              f"{missing})")
        if missing:
            return 2
    return 0


if __name__ == "__main__":
    sys.exit(main())
