#!/usr/bin/env python3
"""
map_spec_points.py — Pass (2): map SME spcpt_ entries to official spec points.

Two regimes:
  A (definition-bearing): SME definition is a transcription of the official statement.
     T1 verbatim        — normalized text equality
     T2 near            — SequenceMatcher ratio >= 0.93
     T3 section_anchored— slug topic/subsection agrees with official anchors + ratio >= 0.80
     T4 fuzzy           — ratio >= 0.85 without section agreement  -> flagged for review
     unmapped           — SME merge/paraphrase -> flag list
  B (name-only): SME exposes name + subtopic_slugs only (definitions empty).
     S1 name_match      — best candidate score >= threshold, clear winner
     S2 name_ambiguous  — winner and runner-up within 0.03 -> flagged
     blocked            — course's qual has a parse gap (igcse-maths-a-modular)

Unit scoping: ial-maths per-unit courses restricted via structure.json spec_point_units;
modular unit-1/2 courses restricted likewise. Notation-appendix junk points excluded via
structure validation gaps. Outputs:
  SME-ExamQuestion/<course>/spec_point_map.json
  Official-Specifications/parsed/_sme_map_report.json
"""
import json, os, re, difflib, datetime

BASE = "/home/z/my-project/download/syllabai-resources"
PARSED = os.path.join(BASE, "Official-Specifications", "parsed")
SME = os.path.join(BASE, "SME-ExamQuestion")

manifest = json.load(open(os.path.join(BASE, "Official-Specifications", "manifest.json")))

def norm(s):
    if not s:
        return ""
    s = s.replace("\r\n", " ").replace("\n", " ")
    s = s.replace("\u2019", "'").replace("\u2018", "'").replace("\u201c", '"').replace("\u201d", '"')
    s = s.replace("\u2013", "-").replace("\u2014", "-").replace("\u00d7", "x")
    s = re.sub(r"[^a-z0-9()'<>=/.\s-]", " ", s.lower())
    return re.sub(r"\s+", " ", s).strip()

def tokens(s):
    return set(t for t in re.split(r"[\s/]+", norm(s)) if len(t) > 2)

def slug_numbers(slug):
    return [int(x) for x in re.findall(r"(?<![\w-])(\d+)(?=-)", slug or "")[:3]]

# ---------- load per-qual official data ----------

def load_qual(slug):
    sp = json.load(open(os.path.join(PARSED, slug, "spec_points.json")))
    pts = sp["spec_points"]
    st_path = os.path.join(PARSED, slug, "structure.json")
    struct = json.load(open(st_path)) if os.path.exists(st_path) else None
    # exclude points flagged by structure pass (appendix/notation junk etc.)
    excluded = {}
    if struct:
        for g in struct["validation"].get("gaps", []):
            if "appendix/notation region" in g.get("reason", ""):
                excluded[g["id"]] = True
    by_topic = {}
    for p in pts:
        if p["id"] in excluded:
            continue
        by_topic.setdefault((p.get("topic") or {}).get("number"), []).append(p)
    for k in by_topic:
        by_topic[k].sort(key=lambda p: str(p["official_code"]))
    return {"pts": pts, "excluded": excluded, "by_topic": by_topic, "struct": struct}

QUALS = {}
for q in manifest["qualifications"]:
    QUALS[q["slug"]] = load_qual(q["slug"])

# ---------- course -> candidate restriction ----------

def course_scope(course, qual_slug):
    """Return (unit_key or None, blocked_reason or None)."""
    struct = QUALS[qual_slug]["struct"]
    if struct is None:
        return None, None
    # parse gap blocks per-point mapping regardless of unit suffix (junk pool)
    gaps = struct.get("validation", {}).get("gaps", [])
    if any(g.get("id") == "*structure_parse_gap*" for g in gaps):
        return None, "parse_gap"
    if qual_slug == "ial-maths":
        m = re.search(r"(pure|mechanics|statistics|decision|further-pure)-(\d)", course)
        if m:
            label = {"pure": "P", "mechanics": "M", "statistics": "S", "decision": "D", "further-pure": "FP"}[m.group(1)] + m.group(2)
            return label, None
    if re.search(r"unit-([12])$", course):
        return f"Unit {re.search(r'unit-([12])$', course).group(1)}", None
    if re.search(r"(foundation|higher)-unit-([12])$", course):
        return f"Unit {re.search(r'unit-([12])$', course).group(2)}", None
    return None, None

def candidates_for(qual_slug, unit_key):
    q = QUALS[qual_slug]
    su = q["struct"]["spec_point_units"] if q["struct"] else None
    out = []
    for p in q["pts"]:
        if p["id"] in q["excluded"]:
            continue
        if unit_key and su:
            if su.get(p["id"]) != unit_key:
                continue
        out.append(p)
    return out

# ---------- Regime A: definition join ----------

def section_agree(sme_slug, p):
    nums = slug_numbers(sme_slug)
    if not nums:
        return False
    tp = (p.get("topic") or {}).get("number")
    sb = (p.get("subsection") or {}).get("letter")
    if tp is None:
        return False
    if str(nums[0]) != str(tp):
        return False
    if len(nums) >= 2 and sb:
        return nums[1] == ord(sb) - 96
    return True

def top_candidates(query_norm, query_toks, prep, k=40):
    """Stage 1: cheap token-overlap prefilter; returns up to k candidate indexes."""
    scored = []
    for i, (p, ttoks, ntext) in enumerate(prep):
        shared = len(query_toks & ttoks)
        if shared:
            scored.append((shared, i))
    scored.sort(reverse=True)
    idxs = [i for _, i in scored[:k]]
    if not idxs:  # degenerate query: fall back to first k with any 2+ char token
        idxs = list(range(min(k, len(prep))))
    return idxs

def map_regime_A(course, qual_slug, entries):
    cands = candidates_for(qual_slug, None)
    prep = [(p, tokens(p["text"]), norm(p["text"])) for p in cands]
    exact = {}
    for i, (p, ttoks, ntext) in enumerate(prep):
        exact.setdefault(ntext, i)
    mappings, unmapped, flags = {}, [], []
    for sid, e in entries.items():
        d = norm(e.get("definition") or ""
                 )
        if not d:
            continue
        dtoks = tokens(d)
        best, bs = None, 0.0
        if d in exact:
            best, bs = prep[exact[d]][0], 1.0
        else:
            for i in top_candidates(d, dtoks, prep):
                p, _, ntext = prep[i]
                r = difflib.SequenceMatcher(None, d, ntext).ratio()
                if r > bs:
                    bs, best = r, p
        slug = (e.get("subtopic_slugs") or [""])[0]
        sec_ok = best is not None and section_agree(slug, best)
        tier, flag = None, None
        if best is None:
            unmapped.append({"spcpt_id": sid, "name": e.get("name"), "reason": "no candidates"})
            continue
        if norm(d) == norm(best["text"]) or bs >= 0.995:
            tier = "T1_verbatim"
        elif bs >= 0.93:
            tier = "T2_near"
        elif sec_ok and bs >= 0.80:
            tier = "T3_section_anchored"
        elif bs >= 0.85:
            tier, flag = "T4_fuzzy", "high-similarity but section disagreement — review"
        if tier:
            mappings[sid] = {
                "official_id": best["id"], "official_code": best["official_code"],
                "tier": tier, "score": round(bs, 4),
                "unit": (QUALS[qual_slug]["struct"]["spec_point_units"].get(best["id"])
                         if QUALS[qual_slug]["struct"] else None),
                "method": "definition_text_join",
            }
            if flag:
                mappings[sid]["flag"] = flag
                flags.append({"spcpt_id": sid, "official_id": best["id"], "flag": flag})
        else:
            unmapped.append({"spcpt_id": sid, "name": e.get("name"),
                             "reason": f"merged/paraphrased beyond safe threshold (best {bs:.2f})"})
    return mappings, unmapped, flags

# ---------- Regime B: name join ----------

def map_regime_B(course, qual_slug, entries):
    cands = candidates_for(qual_slug, None)
    prep = []
    for p in cands:
        prep.append((p, tokens(p["text"]), norm(p["text"])))
    mappings, unmapped, flags = {}, [], []
    for sid, e in entries.items():
        name = e.get("name") or ""
        slug = (e.get("subtopic_slugs") or [""])[0]
        ntok = tokens(name)
        nnorm = norm(name)
        # stage 1: containment scores (fast) -> top-K
        prelim = []
        for i, (p, ttoks, ntext) in enumerate(prep):
            cont = (len(ntok & ttoks) / len(ntok)) if ntok else 0.0
            nums = slug_numbers(slug)
            boost = 0.05 if (nums and str(nums[0]) == str((p.get("topic") or {}).get("number"))) else 0.0
            prelim.append((0.6 * cont + boost, i))
        prelim.sort(key=lambda x: -x[0])
        shortlist = [i for _, i in prelim[:40]]
        # stage 2: precise score on shortlist
        scored = []
        for i in shortlist:
            p, ttoks, ntext = prep[i]
            cont = (len(ntok & ttoks) / len(ntok)) if ntok else 0.0
            part = difflib.SequenceMatcher(None, nnorm, ntext).ratio()
            nums = slug_numbers(slug)
            boost = 0.05 if (nums and str(nums[0]) == str((p.get("topic") or {}).get("number"))) else 0.0
            scored.append((0.6 * cont + 0.4 * part + boost, p))
        scored.sort(key=lambda x: -x[0])
        if not scored:
            unmapped.append({"spcpt_id": sid, "name": name, "reason": "no candidates"})
            continue
        bs, best = scored[0]
        second = scored[1][0] if len(scored) > 1 else 0.0
        if bs < 0.62:
            unmapped.append({"spcpt_id": sid, "name": name,
                             "reason": f"weak name similarity ({bs:.2f})"})
            continue
        tier = "S1_name_match"
        flag = None
        if bs - second <= 0.03:
            tier, flag = "S2_name_ambiguous", f"runner-up within 0.03 ({second:.2f}) — review"
        mappings[sid] = {
            "official_id": best["id"], "official_code": best["official_code"],
            "tier": tier, "score": round(bs, 4),
            "unit": (QUALS[qual_slug]["struct"]["spec_point_units"].get(best["id"])
                     if QUALS[qual_slug]["struct"] else None),
            "method": "name_to_statement_join",
        }
        if flag:
            mappings[sid]["flag"] = flag
            flags.append({"spcpt_id": sid, "official_id": best["id"], "flag": flag})
    return mappings, unmapped, flags

# ---------- run all courses ----------

report = {"schema": "syllabai.sme-spec-point-map-report/1.0",
          "generated_utc": datetime.datetime.now(datetime.timezone.utc).isoformat(timespec="seconds"),
          "courses": {}}

for q in manifest["qualifications"]:
    qual_slug = q["slug"]
    for course in q["sme_courses"]:
        idx_path = os.path.join(SME, course, "spec_point_index.json")
        entries = json.load(open(idx_path))["spec_points"]
        unit_key, blocked = course_scope(course, qual_slug)
        defs_present = sum(1 for e in entries.values() if (e.get("definition") or "").strip())
        regime = "A" if defs_present > len(entries) * 0.5 else "B"

        if blocked == "parse_gap":
            result = {"status": "blocked_parse_gap", "regime": regime,
                      "sme_entries": len(entries),
                      "note": "qualification parse gap (see structure.json validation); mapping deferred to T-PARSE-FIX"}
            report["courses"][course] = {"qual": qual_slug, **{k: v for k, v in result.items()}}
            with open(os.path.join(SME, course, "spec_point_map.json"), "w") as f:
                json.dump({"schema": "syllabai.sme-spec-point-map/1.0", "course": course,
                           "qual": qual_slug, **result, "mappings": {}, "unmapped": [], "flags": []},
                          f, indent=1, ensure_ascii=False)
            print(f"[{course}] qual={qual_slug} regime={regime} -> BLOCKED (parse gap)")
            continue

        if unit_key:
            cands = candidates_for(qual_slug, unit_key)
        else:
            cands = candidates_for(qual_slug, None)

        fn = map_regime_A if regime == "A" else map_regime_B
        mappings, unmapped, flags = fn(course, qual_slug, entries)

        out = {
            "schema": "syllabai.sme-spec-point-map/1.0",
            "course": course, "qual": qual_slug, "regime": regime,
            "unit_scope": unit_key,
            "generated_utc": report["generated_utc"],
            "sme_entries": len(entries),
            "official_pool": len(cands),
            "mappings": mappings,
            "unmapped": unmapped,
            "flags": flags,
        }
        with open(os.path.join(SME, course, "spec_point_map.json"), "w") as f:
            json.dump(out, f, indent=1, ensure_ascii=False)

        tiers = {}
        for m in mappings.values():
            tiers[m["tier"]] = tiers.get(m["tier"], 0) + 1
        report["courses"][course] = {
            "qual": qual_slug, "regime": regime, "unit_scope": unit_key,
            "sme_entries": len(entries), "official_pool": len(cands),
            "mapped": len(mappings), "tiers": tiers,
            "unmapped": len(unmapped), "flags": len(flags),
        }
        print(f"[{course}] qual={qual_slug} regime={regime} scope={unit_key or '-'} "
              f"mapped={len(mappings)}/{len(entries)} tiers={tiers} unmapped={len(unmapped)} flags={len(flags)}")

with open(os.path.join(PARSED, "_sme_map_report.json"), "w") as f:
    json.dump(report, f, indent=1, ensure_ascii=False)

tot = sum(c.get("mapped", 0) for c in report["courses"].values())
sme_tot = sum(c.get("sme_entries", 0) for c in report["courses"].values())
print(f"\nTOTAL mapped {tot}/{sme_tot} across {len(report['courses'])} courses")
