#!/usr/bin/env python3
"""
T-SPECS-CIE-VERDICT-1 — operator-verdict fill lane engine (T-SPECS-CIE-GATE-1 NEXT #1).

Fills the honest-zero CIE lanes (25 lanes, coded==0) with identity-grade
operator verdicts, mirroring the Edexcel T-SPEC-2b/2c evolution. The lane's
verdicts land authoritative by construction (AGENT.md rule 1): every resolve
is a deterministic, single-target identity match whose evidence is verbatim
from committed sources; everything else stays pending with a structured
reason (AGENT.md rule 3 — nothing manufactured).

Rules (priority order; a spec-point id resolves once, by its strongest rule):
  V1_name_text_identity        norm(spcpt name) == norm(official point text),
                               unique in the lane pool
  V2_name_phrase_identity      norm(spcpt name) (>=3 chars) appears as a
                               token-bounded phrase in exactly one official
                               point text of the lane pool
  V3_subsection_head_identity  norm(name | note topic title) == artifact-
                               stripped norm(subsection title) AND that
                               subsection has exactly one point in the pool
  V4_settext_title_identity    (0475 literature) note-name segment 0 == the
                               quoted set-text title inside exactly one
                               official point text
  V5_topic_scoped_phrase       V2 was ambiguous globally but exactly one hit
                               within the official topic whose title equals
                               the SME note's section|topic title

Pools mirror the join lane's scoping: Biology/Chemistry/Physics scope filter
(0654 lanes), Core/Extended tier filter (ce_codes maths lanes), and the 9709
per-component lanes restricted to their official topic(s).

Pending reason taxonomy (recorded per lane; ids stay pending — rule 3):
  no_unique_identity              name-only substrate, no identity evidence
  name_phrase_multi_text          phrase appears in N official point texts
  name_eq_multi_text              name equals N official point texts
  finer_than_official_subsection  topic-head identity exists but the
                                  subsection holds >1 point (Edexcel 2c
                                  doctrine: an id spanning several statements
                                  is never collapsed)
  dangling_eq_reference           EQ-referenced spcpt id with no embedded
                                  record anywhere in the corpus (cured by the
                                  planned SME-native index harvest, NEXT #2)

Deterministic: fixed stamp, sorted iteration, no dict-order or wall-clock
dependence; re-run with the same stamp is byte-identical (battery V10).

Usage:
  python3 cie_verdict_fill.py           # evaluate + apply + emit everything
"""
from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

REPO = Path("/home/z/my-project/syllabai-resources")
SL = REPO / "spec-links"
REPORTS = REPO / "graph" / "reports"
sys.path.insert(0, str(REPO / "scripts"))
from cie_spec_join import ls_tree, cat_blobs, lane_scope, lane_tier_pref  # noqa: E402

LANE_ID = "T-SPECS-CIE-VERDICT-1"
STAMP = "2026-10-18T22:46:00Z"
DIRECTIVE = ("operator directive 'operator-verdict fill lane' (gateway trace "
             "1a15123a0964b44d, 2026-10-19, zai-web)")
TIERS = {
    "V1_name_text_identity": "authoritative (name == official point text, unique)",
    "V2_name_phrase_identity": "authoritative (name phrase-unique in official point text)",
    "V3_subsection_head_identity": "authoritative (head == single-point subsection title)",
    "V4_settext_title_identity": "authoritative (set-text title identity)",
    "V5_topic_scoped_phrase_identity": "authoritative (topic-scoped phrase identity)",
}
METHOD = "operator_verdict"

# The honest-zero lanes (coded == 0 post-gate), from the JOIN/GATE records.
ZERO_LANES = [
    "cie-a-level-business-23", "cie-a-level-computer-science-19",
    "cie-a-level-economics-23", "cie-a-level-maths-20-mechanics",
    "cie-a-level-maths-20-probability-and-statistics-1",
    "cie-a-level-maths-20-probability-and-statistics-2",
    "cie-a-level-maths-20-pure-1", "cie-a-level-maths-20-pure-3",
    "cie-as-english-general-paper-21", "cie-igcse-accounting-21",
    "cie-igcse-accounting-25", "cie-igcse-economics-25",
    "cie-igcse-english-language-20", "cie-igcse-english-language-25",
    "cie-igcse-english-literature-21", "cie-igcse-environmental-management-25",
    "cie-igcse-further-maths-additional-maths-25", "cie-igcse-history-18",
    "cie-igcse-ict-21", "cie-igcse-maths-25-core", "cie-igcse-maths-25-extended",
    "cie-igcse-maths-international-maths-23-core",
    "cie-igcse-maths-international-maths-23-extended",
    "cie-igcse-religious-studies-23",
    "cie-igcse-science-co-ordinated-sciences-double-award-23-biology",
]

# 9709 per-component lanes: official topic title each lane's pool is
# restricted to (the registry covers all components; a component lane's
# notes live in their own course tree).
COMPONENT_TOPICS = {
    "cie-a-level-maths-20-mechanics": ["mechanics"],
    "cie-a-level-maths-20-probability-and-statistics-1": ["probability and statistics 1"],
    "cie-a-level-maths-20-probability-and-statistics-2": ["probability and statistics 2"],
    "cie-a-level-maths-20-pure-1": ["pure mathematics 1", "pure mathematics 2"],
    "cie-a-level-maths-20-pure-3": ["pure mathematics 3"],
}

ARTIFACT = re.compile(r"\b(notes?|examples?)\b", re.I)


def norm(s: str) -> str:
    """Normalization SPEC (shared with the join/gate lineage, NOT its code):
    NFKC, lower, & -> and, strip punctuation to spaces, collapse whitespace."""
    s = unicodedata.normalize("NFKC", s or "").lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9 ]+", " ", s)
    return re.sub(r"\s+", " ", s).strip()


def phrase_in(needle: str, hay: str) -> bool:
    """Token-bounded phrase containment on normalized single-space strings."""
    if not needle:
        return False
    return (" " + needle + " ") in (" " + hay + " ")


def load_registry(qual: str) -> dict:
    man = json.loads((REPO / "Official-Specifications" / "manifest.json").read_text())
    for q in man["qualifications"]:
        if q["slug"] == qual:
            pdf = Path(q["pdf"]).stem
            return json.loads(
                (REPO / "Official-Specifications" / "parsed" / qual / f"{pdf}.parsed.json")
                .read_text())
    raise SystemExit(f"qual {qual} not in manifest")


def lane_pool(lane: str, reg: dict) -> list:
    pts = reg["spec_points"]
    scope = lane_scope(lane)
    if scope:
        pts = [p for p in pts if (p.get("scope") or "") == scope]
    tier = lane_tier_pref(lane)
    if tier:
        tf = [p for p in pts if p.get("tier") == tier]
        pts = tf or pts
    comps = COMPONENT_TOPICS.get(lane)
    if comps:
        def t_of(p):
            t = p.get("topic") or {}
            return norm(t.get("title") if isinstance(t, dict) else "")
        sel = [p for p in pts if t_of(p) in comps]
        pts = sel or pts
    return pts


def quoted_title(text: str) -> str:
    m = re.search(r"[\u2018'\"“]([^'\u2019\"”]+)[\u2019'\"”]", text or "")
    return norm(m.group(1)) if m else ""


def lane_blocks(lane: str, files: dict, blobs_cache: dict) -> list:
    """(sid, name, topic_title, section) per spec_point block in the lane's notes."""
    note_paths = [p for p in files
                  if p.startswith(f"SME-RevisionNotes/{lane}/notes/") and p.endswith(".json")]
    sha_to_path = {files[p]: p for p in note_paths}
    blobs = cat_blobs(sha_to_path)
    blobs_cache[lane] = blobs
    out = []
    for p in note_paths:
        try:
            n = json.loads(blobs[p])
        except Exception:
            continue
        tt = (n.get("titles") or {}).get("topic") or ""
        nsec = n.get("section") or ""
        for b in n.get("blocks") or []:
            if b.get("type") == "spec_point" and b.get("id"):
                out.append((b["id"], b.get("name") or "", tt, nsec))
    return out


def evaluate_lane(lane: str, reg: dict, files: dict, blobs_cache: dict) -> dict:
    pts = lane_pool(lane, reg)
    texts = [norm(p.get("text")) for p in pts]
    sub_pts: dict[str, list] = {}
    for p in pts:
        st = norm(ARTIFACT.sub(" ", (p.get("subsection") or {}).get("title") or ""))
        sub_pts.setdefault(st, []).append(p)
    top_titles: dict[str, list] = {}
    for p in pts:
        t = p.get("topic") or {}
        top_titles.setdefault(norm(t.get("title") if isinstance(t, dict) else ""), []).append(p)

    blocks = lane_blocks(lane, files, blobs_cache)
    universe = {b[0] for b in blocks}
    verdicts: dict[str, dict] = {}
    reasons: dict[str, int] = {
        "no_unique_identity": 0, "name_phrase_multi_text": 0,
        "name_eq_multi_text": 0, "finer_than_official_subsection": 0,
        "dangling_eq_reference": 0,
    }
    ambiguous: dict[str, dict] = {}

    def resolve(sid, tier, code_pts, evidence):
        verdicts[sid] = {
            "lane": lane, "verdict": "resolve", "tier": tier,
            "official_id": code_pts["id"],
            "official_code": str(code_pts.get("official_code")),
            "evidence": evidence,
        }

    for sid, name, ttopic, nsec in sorted(blocks, key=lambda b: (b[0], b[1])):
        nn = norm(name)
        if not nn:
            reasons["no_unique_identity"] += 1
            continue
        # --- V1: name == point text (unique)
        eq = [p for p, t in zip(pts, texts) if t and t == nn]
        if len(eq) == 1:
            resolve(sid, "V1_name_text_identity", eq[0],
                    {"sme_name": name, "official_text": eq[0].get("text"),
                     "rule": "norm(name) == norm(official point text), unique in lane pool"})
            continue
        if len(eq) > 1:
            reasons["name_eq_multi_text"] += 1
            ambiguous[sid] = {"lane": lane, "reason": "name_eq_multi_text",
                              "matched_codes": sorted(str(p.get("official_code")) for p in eq)}
            continue
        # --- V2: name phrase-unique in point text
        ph = [p for p, t in zip(pts, texts) if len(nn) >= 3 and phrase_in(nn, t)]
        if len(ph) == 1:
            resolve(sid, "V2_name_phrase_identity", ph[0],
                    {"sme_name": name, "official_text": ph[0].get("text"),
                     "rule": "token-bounded norm(name) phrase in exactly one official point text"})
            continue
        if len(ph) > 1:
            # --- V5: topic-scoped disambiguation of the phrase ambiguity
            scoped = []
            for cand in (nsec, ttopic):
                nc = norm(cand)
                if nc and nc in top_titles:
                    scoped = [p for p in top_titles[nc]
                              if phrase_in(nn, norm(p.get("text")))]
                    if len(scoped) == 1:
                        break
                    scoped = []
            if len(scoped) == 1:
                resolve(sid, "V5_topic_scoped_phrase_identity", scoped[0],
                        {"sme_name": name,
                         "official_text": scoped[0].get("text"),
                         "topic_title": cand,
                         "rule": ("phrase ambiguous globally; exactly one hit within the "
                                  "official topic whose title == the SME note's "
                                  "section/topic title")})
                continue
            reasons["name_phrase_multi_text"] += 1
            ambiguous[sid] = {"lane": lane, "reason": "name_phrase_multi_text",
                              "matched_codes": sorted(str(p.get("official_code")) for p in ph)}
            continue
        # --- V3: head identity against a single-point subsection
        fired = False
        for cand, src in ((name, "spcpt_name"), (ttopic, "note_topic_title")):
            nc = norm(ARTIFACT.sub(" ", cand))
            if nc and nc in sub_pts:
                if len(sub_pts[nc]) == 1:
                    op = sub_pts[nc][0]
                    resolve(sid, "V3_subsection_head_identity", op,
                            {"sme_name": name, "official_text": op.get("text"),
                             "head": cand, "head_source": src,
                             "subsection_title": (op.get("subsection") or {}).get("title"),
                             "rule": ("head == artifact-stripped subsection title; subsection "
                                      "holds exactly one point in the lane pool")})
                    fired = True
                else:
                    reasons["finer_than_official_subsection"] += 1
                    ambiguous[sid] = {
                        "lane": lane, "reason": "finer_than_official_subsection",
                        "head": cand, "head_source": src,
                        "matched_codes": sorted(str(p.get("official_code"))
                                                for p in sub_pts[nc]),
                    }
                    fired = True
                break
        if fired:
            continue
        # --- V4: set-text title identity (literature lanes)
        if "literature" in reg["id"]:
            seg = norm(name.split(":")[0]) if name else ""
            if seg:
                qh = [p for p in pts
                      if quoted_title(p.get("text")) and quoted_title(p.get("text")) == seg]
                if len(qh) == 1:
                    resolve(sid, "V4_settext_title_identity", qh[0],
                            {"sme_name": name, "official_text": qh[0].get("text"),
                             "rule": "note-name leading segment == quoted set-text title, unique"})
                    continue
                if len(qh) > 1:
                    reasons["name_phrase_multi_text"] += 1
                    ambiguous[sid] = {"lane": lane, "reason": "name_phrase_multi_text",
                                      "matched_codes": sorted(str(p.get("official_code"))
                                                              for p in qh)}
                    continue
        reasons["no_unique_identity"] += 1

    dangling = 0  # counted at apply time from the sidecar's pending lists
    return {"lane": lane, "verdicts": verdicts, "ambiguous": ambiguous,
            "reasons": reasons, "universe": universe}


def main() -> int:
    files = ls_tree()
    sidecars = {lane: json.loads((SL / f"{lane}.json").read_text()) for lane in ZERO_LANES}
    regs = {lane: load_registry(sidecars[lane]["qual"]) for lane in ZERO_LANES}

    blobs_cache: dict = {}
    lane_results = {}
    for lane in ZERO_LANES:
        lane_results[lane] = evaluate_lane(lane, regs[lane], files, blobs_cache)

    # ---------------- fail-closed validation before any write
    errors = []
    for lane, r in lane_results.items():
        reg = regs[lane]
        ids = {p["id"]: str(p.get("official_code")) for p in reg["spec_points"]}
        prefix = ""
        if reg["spec_points"]:
            prefix = reg["spec_points"][0]["id"].split(":", 1)[0] + ":"
        for sid, v in sorted(r["verdicts"].items()):
            if sid not in r["universe"]:
                errors.append(f"{lane}:{sid}:verdict id not in lane universe")
            if v["official_id"] not in ids:
                errors.append(f"{lane}:{sid}:dangling official id {v['official_id']}")
            elif ids[v["official_id"]] != v["official_code"]:
                errors.append(f"{lane}:{sid}:code mismatch")
            if not v["official_id"].startswith(prefix):
                errors.append(f"{lane}:{sid}:prefix")
            if v["tier"] not in TIERS:
                errors.append(f"{lane}:{sid}:tier vocab")
    if errors:
        for e in errors:
            print("FAIL-CLOSED:", e)
        return 1

    # ---------------- apply to sidecars
    fill_summary = {}
    for lane in ZERO_LANES:
        r = lane_results[lane]
        d = sidecars[lane]
        items = d["items"]
        code_by_sid = {sid: (v["official_id"], v["official_code"], v["tier"])
                       for sid, v in r["verdicts"].items()}
        added = 0
        dangling = 0
        pend_universe = set()
        for key in sorted(items):
            it = items[key]
            pend = it.get("pending") or []
            if not pend:
                continue
            keep, new_codes = [], []
            for sid in pend:
                if sid in code_by_sid:
                    oid, ocode, tier = code_by_sid[sid]
                    if not any(c.get("official_id") == oid for c in (it.get("codes") or [])):
                        new_codes.append({"official_id": oid, "official_code": ocode,
                                          "tier": tier, "method": METHOD})
                        added += 1
                else:
                    keep.append(sid)
                    if sid in r["universe"]:
                        pend_universe.add(sid)
                    else:
                        dangling += 1
            if new_codes:
                it["codes"] = (it.get("codes") or []) + new_codes
            it["pending"] = keep
        # totals
        t = d["totals"]
        by = {"notes": 0, "question_parts": 0, "flashcards": 0}
        coded = {"notes": 0, "question_parts": 0, "flashcards": 0}
        for it in items.values():
            by[it["kind"] + "s"] += 1
            coded[it["kind"] + "s"] += 1 if it["codes"] else 0
        t["by_kind"] = by
        t["coded_by_kind"] = coded
        t["items_with_codes"] = sum(coded.values())
        # stable bookkeeping: verdict code entries present post-apply
        added = sum(1 for it in items.values()
                    for c in (it.get("codes") or []) if c.get("method") == METHOD)
        # anchors
        a = d["anchors"]
        a["universe_resolved"] = int(a["universe_ids"]) - len(pend_universe)
        a["pending_refs"] = sum(len(it.get("pending") or []) for it in items.values())
        n_res = len(r["verdicts"])
        a["verdict"] = {
            "lane": LANE_ID, "applied_utc": STAMP,
            "resolved_ids": n_res,
            "by_tier": {k: sum(1 for v in r["verdicts"].values() if v["tier"] == k)
                        for k in sorted(TIERS)},
            "pending_ids": len(r["universe"]) - n_res,
            "pending_reasons": dict(sorted(r["reasons"].items())),
            "dangling_eq_refs_pending": dangling,
        }
        # review_state (state stays ACCEPTED; verdict block additive)
        rs = d["review_state"]
        rs["verdict"] = {
            "lane": LANE_ID, "directive": DIRECTIVE, "applied_utc": STAMP,
            "base_commit": "fea58c8a",
            "method": METHOD,
            "tiers": dict(sorted(TIERS.items())),
            "note": ("identity-grade operator verdicts applied to the honest-zero "
                     "anchors (T-SPECS-CIE-GATE-1 NEXT #1); authoritative by "
                     "construction per AGENT.md rule 1; unresolved anchors stay "
                     "pending with structured reasons (rule 3); the gate's "
                     "ACCEPTED state and provenance are preserved"),
        }
        (SL / f"{lane}.json").write_text(
            json.dumps(d, indent=1, ensure_ascii=False) + "\n")
        fill_summary[lane] = {
            "resolved_ids": n_res,
            "code_entries_added": added,
            "by_tier": a["verdict"]["by_tier"],
            "pending_reasons": a["verdict"]["pending_reasons"],
            "dangling_eq_refs_pending": dangling,
            "items_with_codes": t["items_with_codes"],
        }

    # ---------------- verdict sheet (decision record, T-SPEC-2b shape).
    # Entries are LISTS keyed by (lane, id): SME reuses spcpt ids across
    # course trees, and a shared id may legitimately resolve differently
    # per lane (different registry pool).
    sheet = {
        "lane": LANE_ID, "generated_utc": STAMP, "directive": DIRECTIVE,
        "base_commit": "fea58c8a",
        "header": (
            "Operator-verdict fill on the 25 honest-zero CIE lanes. Identity-grade "
            "deterministic verdicts rendered by cie_verdict_fill.py and re-validated "
            "fail-closed by cie_verdict_check.py (V5 re-derives every resolve from "
            "source blobs with an independent implementation). Entries are per (lane, "
            "id): SME reuses spcpt ids across course trees. Unresolved ids stay "
            "pending with structured reasons (AGENT.md rule 3)."),
        "verdicts": [],
        "ambiguous": [],
    }
    for lane in ZERO_LANES:
        for sid, v in sorted(lane_results[lane]["verdicts"].items()):
            sheet["verdicts"].append({"id": sid, **v})
        for sid, a in sorted(lane_results[lane]["ambiguous"].items()):
            sheet["ambiguous"].append({"id": sid, **a})
    sheet["verdicts"].sort(key=lambda e: (e["lane"], e["id"]))
    sheet["ambiguous"].sort(key=lambda e: (e["lane"], e["id"]))
    (REPO / "scripts" / "cie_verdict_fill_verdicts.yaml").write_text(
        yaml.safe_dump(sheet, sort_keys=False, allow_unicode=True, width=100))

    # ---------------- manifest
    mpath = SL / "manifest.json"
    manifest = json.loads(mpath.read_text())
    for lane in ZERO_LANES:
        row = manifest["courses"].get(lane)
        if not row:
            continue
        d = sidecars[lane]
        t = d["totals"]
        row["items"] = t["items"]
        row["items_with_codes"] = t["items_with_codes"]
        row["by_kind"] = t["by_kind"]
        row["coded_by_kind"] = t["coded_by_kind"]
        row["pending_refs"] = d["anchors"]["pending_refs"]
        row["verdict"] = {
            "lane": LANE_ID, "resolved_ids": fill_summary[lane]["resolved_ids"],
            "by_tier": fill_summary[lane]["by_tier"],
            "pending_reasons": fill_summary[lane]["pending_reasons"],
        }
    manifest["cie_verdict"] = {
        "lane": LANE_ID, "applied_utc": STAMP, "directive": DIRECTIVE,
        "base_commit": "fea58c8a",
        "lanes": len(ZERO_LANES),
        "resolved_ids_total": sum(s["resolved_ids"] for s in fill_summary.values()),
        "code_entries_added_total": sum(s["code_entries_added"] for s in fill_summary.values()),
        "tier_policy": dict(sorted(TIERS.items())),
        "note": ("operator-verdict fill on the 25 honest-zero lanes; authoritative by "
                 "construction (AGENT.md rule 1); unresolved stay pending (rule 3); "
                 "the ACCEPTED review states and gate provenance are preserved"),
    }
    mpath.write_text(json.dumps(manifest, indent=1, ensure_ascii=False) + "\n")

    # ---------------- machine record + summary record
    machine = {
        "lane": LANE_ID, "generated_utc": STAMP, "directive": DIRECTIVE,
        "base_commit": "fea58c8a", "method": METHOD, "tiers": sorted(TIERS),
        "rules": {
            "V1_name_text_identity": "norm(name) == norm(point text), unique in pool",
            "V2_name_phrase_identity": "token-bounded name phrase in exactly one point text",
            "V3_subsection_head_identity": "head == artifact-stripped single-point subsection title",
            "V4_settext_title_identity": "note-name segment == quoted set-text title, unique",
            "V5_topic_scoped_phrase_identity": "topic-scoped disambiguation of a phrase ambiguity",
        },
        "lanes": fill_summary,
    }
    (REPORTS / "T_SPECS_CIE_VERDICT_1_FILL.json").write_text(
        json.dumps(machine, indent=1, ensure_ascii=False) + "\n")

    tot_res = sum(s["resolved_ids"] for s in fill_summary.values())
    tot_codes = sum(s["code_entries_added"] for s in fill_summary.values())
    tot_pend = sum(s["pending_ids"] for s in (sidecars[l]["anchors"]["verdict"] for l in ZERO_LANES))
    print(f"LANES {len(ZERO_LANES)}  resolved_ids {tot_res}  code_entries {tot_codes}  pending_ids {tot_pend}")
    for lane in ZERO_LANES:
        s = fill_summary[lane]
        print(f"  {lane:62s} res={s['resolved_ids']:4d} codes={s['code_entries_added']:5d} "
              f"tiers={s['by_tier']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
