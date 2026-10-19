#!/usr/bin/env python3
"""T-SPEC-2b — sibling-course spec-point join over the FULL qualification pool.

Why a sibling-specific joiner: map_spec_points.py restricts modular courses to
their unit's statements (unit_key filter). That is correct for unit-aligned
ids, but SME reuses taxonomy ids across units (u1 EQ parts reference unit-2
statements like "describe tests for these gases:"). A hard unit filter makes
those ids unmappable even at near-verbatim evidence.

Method (per id, over the course's own official universe):
  - statement text = registry text + sub_items (enumerated statements carry
    their lists in sub_items)
  - regime A (definition-bearing, SDA): verbatim/near tiers T1/T2 as pass 2;
    T4 fuzzy >= 0.85 flagged; otherwise resolver-grade score
    0.7*max(token_f1, token_containment) + 0.3*sequence-ratio
  - regime B (name-only, modular): same resolver-grade score on the name
  - unit scope acts as a small boost (+0.05), never a filter; a winner outside
    the course's unit scope is accepted only with a cross-unit flag and a
    strong margin (>= 0.70 score and >= 0.05 margin)
  - S2 ambiguity flag when runner-up within 0.03
  - ids with no name/definition (unavailable corpora) stay unmapped with the
    recorded reason; never guessed

Existing mappings from the scoped pass 2 are REUSED when the new pass does not
produce a strictly better-evidence result for the same id (tier order T1 >
T2 > S1 > T4 > S2): the earlier pass is committed operator-era data and the
new pass must not silently downgrade it.

Outputs: SME-ExamQuestion/<course>/spec_point_map.json (full rewrite for the
3 sibling courses) + parsed/_sme_map_report.json merged update.
"""
import difflib
import json
import re
import sys
import time
from pathlib import Path

BASE = Path("/home/z/my-project/download/syllabai-resources")
PARSED = BASE / "Official-Specifications" / "parsed"
EQ = BASE / "SME-ExamQuestion"

COURSES = {
    "igcse-chemistry-modular-24-unit-1": ("igcse-chemistry-modular", None),
    "igcse-chemistry-modular-24-unit-2": ("igcse-chemistry-modular", None),
    "igcse-science-double-award-17-chemistry": ("igcse-science-double-award", "Chemistry"),
}

STOP = {"the", "a", "an", "of", "in", "to", "and", "or", "for", "with",
        "on", "at", "by", "is", "are", "be", "that", "this", "their"}


def norm(s):
    if not s:
        return ""
    s = (s.replace("\r\n", " ").replace("\n", " ")
          .replace("\u2019", "'").replace("\u2018", "'")
          .replace("\u201c", '"').replace("\u201d", '"')
          .replace("\u2013", "-").replace("\u2014", "-").replace("\u00d7", "x"))
    s = re.sub(r"[^a-z0-9()'<>=/.\s-]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()


def _stem(t):
    """Light deterministic suffix strip (matching aid only, both sides)."""
    for suf in ("ing", "ion", "ies", "ied", "ed", "es", "s"):
        if len(t) > 4 and t.endswith(suf):
            return t[: -len(suf)]
    return t


def ntokens(s):
    raw = [t for t in re.split(r"[\s/]+", norm(s)) if t]
    out = set()
    for t in raw:
        if len(t) > 2 or any(ch.isdigit() for ch in t):
            out.add(t)
            out.add(_stem(t))
    return out


def resolver_score(query, statement):
    a, b = ntokens(query), ntokens(statement)
    if not a or not b:
        return 0.0
    inter = len(a & b)
    f1 = 2 * inter / (len(a) + len(b))
    cont = inter / min(len(a), len(b))
    seq = difflib.SequenceMatcher(None, norm(query), norm(statement)).ratio()
    return 0.7 * max(f1, cont) + 0.3 * seq


TIER_ORDER = {"T1_verbatim": 6, "T2_near": 5, "T3_section_anchored": 4,
              "S1_name_match": 3, "T4_fuzzy": 2, "S2_name_ambiguous": 1}


def statement_text(p):
    parts = [p.get("text") or ""]
    for si in p.get("sub_items") or []:
        if isinstance(si, str):
            parts.append(si)
        elif isinstance(si, dict):
            parts.append(si.get("text") or "")
    return " ".join(parts)


def load_registry(qual_slug, scope=None):
    pts = json.loads((PARSED / qual_slug / "spec_points.json")
                     .read_text(encoding="utf-8"))["spec_points"]
    if scope:
        scoped = [p for p in pts if p.get("scope") == scope]
        pts = scoped or pts  # single-subject parses carry no scope field
    excluded = set()
    st_path = PARSED / qual_slug / "structure.json"
    if st_path.exists():
        struct = json.loads(st_path.read_text(encoding="utf-8"))
        for g in struct.get("validation", {}).get("gaps", []):
            if "appendix/notation region" in g.get("reason", ""):
                excluded.add(g["id"])
    units = {}
    if st_path.exists():
        units = json.loads(st_path.read_text(encoding="utf-8")).get("spec_point_units", {})
    out = []
    for p in pts:
        if p["id"] in excluded:
            continue
        out.append({"p": p, "text": statement_text(p),
                    "unit": units.get(p["id"])})
    return out


MD_MARKER = re.compile(r">\s*\*\*Spec point\*\*\s*\u2014\s*`?(spcpt_\w+)`?\s*(?:\u00b7\s*(.+))?")


def note_section_text(course):
    """spcpt id -> teaching text of its anchored note sections (committed RN
    .md corpora, all chemistry courses: SME reuses ids across them).
    Section = text after the id's spec marker until the next marker."""
    texts = {}
    roots = [BASE / "SME-RevisionNotes" / c for c in COURSES]
    roots.append(BASE / "Chemistry IGCSE Revision Notes")
    md_by_nid = {}
    for root in roots:
        if not root.exists():
            continue
        for mf in sorted(root.rglob("*.md")):
            try:
                txt = mf.read_text(encoding="utf-8", errors="replace")
            except Exception:
                continue
            mfm = re.match(r"^---\n(.*?)\n---\n", txt, re.S)
            nid = None
            if mfm:
                n = re.search(r'^note_id:\s*"(rn_\w+)"', mfm.group(1), re.M)
                if n:
                    nid = n.group(1)
            body = txt[mfm.end():] if mfm else txt
            hits = list(MD_MARKER.finditer(body))
            for i, m in enumerate(hits):
                sid = m.group(1)
                start = m.end()
                end = hits[i + 1].start() if i + 1 < len(hits) else len(body)
                seg = body[start:end]
                seg = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", seg)  # images
                seg = re.sub(r"\|", " ", seg)
                seg = re.sub(r"\s+", " ", seg).strip()
                if m.group(2):  # the statement line itself, when present
                    seg = (m.group(2) + " ") * 3 + seg
                if seg:
                    key = (sid, nid or str(mf))
                    texts.setdefault(sid, {})[key] = seg[:1500]
    return texts


def course_unit(course):
    m = re.search(r"unit-([12])$", course)
    return f"Unit {m.group(1)}" if m else None


def join(course, qual_slug, entries, reg, notes):
    unit_key = course_unit(course)
    old_map_path = EQ / course / "spec_point_map.json"
    old = json.loads(old_map_path.read_text(encoding="utf-8")) \
        if old_map_path.exists() else {"mappings": {}, "flags": []}

    mappings, unmapped, flags = {}, [], []
    for sid, e in sorted(entries.items()):
        name = e.get("name") or ""
        definition = e.get("definition") or ""
        query = definition or name
        rec = None
        fail = None

        # ---------- stage 1: name/definition vs statements ----------
        if query.strip():
            regime = "A" if definition.strip() else "B"
            scored = []
            for r in reg:
                s = resolver_score(query, r["text"])
                if r["unit"] and unit_key and r["unit"] == unit_key:
                    s += 0.05
                scored.append((s, r))
            scored.sort(key=lambda x: (-x[0], str(x[1]["p"]["official_code"])))
            top_s, top = scored[0]
            second_s = scored[1][0] if len(scored) > 1 else 0.0

            dnorm, tnorm = norm(query), norm(top["text"])
            tier, flag = None, None
            if regime == "A":
                if dnorm == tnorm or top_s >= 0.995:
                    tier = "T1_verbatim"
                elif top_s >= 0.93:
                    tier = "T2_near"
                elif top_s >= 0.85:
                    tier, flag = "T4_fuzzy", \
                        "high-similarity but not near-verbatim — review"
            cross_unit = bool(unit_key and top["unit"] and top["unit"] != unit_key)

            if tier is None:
                if top_s >= 0.75 and (top_s - second_s) >= 0.05:
                    tier = "S1_name_match" if regime == "B" else "T3_section_anchored"
                    if regime == "A":
                        tier, flag = "T3_section_anchored", \
                            "resolver-grade definition join (no section anchor) — review"
                elif top_s >= 0.62 and regime == "B":
                    tier, flag = "S2_name_ambiguous", \
                        f"weak/ambiguous name similarity ({top_s:.2f} vs {second_s:.2f}) — review"

            decisive = top_s >= 0.70 and (top_s - second_s) >= 0.05
            if tier is not None and (not cross_unit or decisive):
                rec = {
                    "official_id": top["p"]["id"],
                    "official_code": top["p"]["official_code"],
                    "tier": tier, "score": round(min(top_s, 1.0), 4),
                    "unit": top["unit"],
                    "method": ("definition_text_join" if regime == "A"
                               else "name_to_statement_join") +
                          " (full-pool, sub_items)",
                }
                if cross_unit:
                    flag = (flag + "; " if flag else "") + \
                        f"cross-unit: statement in {top['unit']}, course scope {unit_key}"
                if flag:
                    rec["flag"] = flag
            elif tier is not None and cross_unit and not decisive:
                fail = f"cross-unit winner not decisive (best {top_s:.2f}, " \
                       f"runner-up {second_s:.2f})"
            else:
                fail = f"below safe join threshold (best {top_s:.2f}, " \
                       f"runner-up {second_s:.2f})"

        # ---------- stage 2: note-coverage rescue (title-only ids) ----------
        if rec is None and not definition.strip() and notes.get(sid):
            secs = list(notes[sid].values())[:3]
            scored2 = []
            for r in reg:
                stmt_toks = ntokens(r["text"])
                if not stmt_toks:
                    continue
                cov = 0.0
                for seg in secs:
                    cov = max(cov, len(stmt_toks & ntokens(seg)) / len(stmt_toks))
                scored2.append((cov, r))
            scored2.sort(key=lambda x: (-x[0], str(x[1]["p"]["official_code"])))
            if scored2:
                c_s, c_top = scored2[0]
                c_second = scored2[1][0] if len(scored2) > 1 else 0.0
                cross_unit = bool(unit_key and c_top["unit"] and
                                  c_top["unit"] != unit_key)
                if c_s >= 0.80 and (c_s - c_second) >= 0.10 and \
                        (not cross_unit or (c_s >= 0.85 and (c_s - c_second) >= 0.10)):
                    rec = {
                        "official_id": c_top["p"]["id"],
                        "official_code": c_top["p"]["official_code"],
                        "tier": "T4_fuzzy",
                        "score": round(min(c_s, 1.0), 4),
                        "unit": c_top["unit"],
                        "method": "note_coverage_join (statement-token coverage "
                                  "by anchored note section, committed RN corpora)",
                        "flag": f"note-coverage join (coverage {c_s:.2f}, "
                                f"runner-up {c_second:.2f}) — review",
                    }
                    if cross_unit:
                        rec["flag"] += (f"; cross-unit: statement in "
                                        f"{c_top['unit']}, course scope {unit_key}")

        if rec is not None:
            old_rec = old["mappings"].get(sid)
            if old_rec and TIER_ORDER.get(old_rec["tier"], 0) > TIER_ORDER.get(rec["tier"], 0):
                mappings[sid] = dict(old_rec)
                mappings[sid]["recheck"] = {
                    "by": "sme_spcpt_sibling_map.py (full-pool + note-coverage)",
                    "kept_tier": old_rec["tier"], "new_tier": rec["tier"],
                    "new_score": rec["score"],
                }
                if old_rec.get("flag"):
                    flags.append({"spcpt_id": sid,
                                  "official_id": old_rec["official_id"],
                                  "flag": old_rec["flag"]})
            else:
                mappings[sid] = rec
                if rec.get("flag"):
                    flags.append({"spcpt_id": sid,
                                  "official_id": rec["official_id"],
                                  "flag": rec["flag"]})
        elif not query.strip():
            unmapped.append({
                "spcpt_id": sid, "name": name,
                "reason": "no SME statement text available in committed corpora "
                          "(cross-cutting id; never guessed)"})
        else:
            unmapped.append({
                "spcpt_id": sid, "name": name,
                "reason": (fail or "unresolved") +
                          "; note-coverage rescue not decisive"})

    return mappings, unmapped, flags


def main():
    now = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    report_path = PARSED / "_sme_map_report.json"
    report = json.loads(report_path.read_text(encoding="utf-8")) \
        if report_path.exists() else {"courses": {}}

    for course, (qual_slug, scope) in COURSES.items():
        reg = load_registry(qual_slug, scope)
        idx = json.loads((EQ / course / "spec_point_index.json")
                         .read_text(encoding="utf-8"))
        entries = idx["spec_points"]
        notes = note_section_text(course)
        mappings, unmapped, flags = join(course, qual_slug, entries, reg, notes)
        unit_key = course_unit(course)
        out = {
            "schema": "syllabai.sme-spec-point-map/1.0",
            "course": course, "qual": qual_slug,
            "regime": "A" if course.endswith("17-chemistry") else "B",
            "unit_scope": unit_key,
            "generated_utc": now,
            "sme_entries": len(entries),
            "official_pool": len(reg),
            "mappings": mappings,
            "unmapped": unmapped,
            "flags": flags,
            "join_method": "sme_spcpt_sibling_map.py full-pool join "
                           "(resolver-grade scoring, unit-scope boost, cross-unit "
                           "winners flagged; pre-existing better-evidence mappings kept)",
        }
        (EQ / course / "spec_point_map.json").write_text(
            json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")

        tiers = {}
        for m in mappings.values():
            tiers[m["tier"]] = tiers.get(m["tier"], 0) + 1
        report.setdefault("courses", {})[course] = {
            "qual": qual_slug, "regime": out["regime"], "unit_scope": unit_key,
            "sme_entries": len(entries), "official_pool": len(reg),
            "mapped": len(mappings), "tiers": tiers,
            "unmapped": len(unmapped), "flags": len(flags),
            "join_method": "full-pool",
        }
        print(f"[{course}] mapped={len(mappings)}/{len(entries)} tiers={tiers} "
              f"unmapped={len(unmapped)} flags={len(flags)}")

    report_path.write_text(json.dumps(report, ensure_ascii=False, indent=1),
                           encoding="utf-8")
    return 0


if __name__ == "__main__":
    sys.exit(main())
