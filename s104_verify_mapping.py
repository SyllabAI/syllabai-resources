#!/usr/bin/env python3
"""Session 104 v2: VERIFY SME igcse-chemistry-19 mapping (fixed parsers).

A. EQ parts -> spec_point_codes all in the official 182 registry; id<->code consistency.
B. EQ structural integrity: MCQ exactly-one-correct, marks sums, difficulty, source_paper.
C. RN pages -> spec_point_codes in registry; cross-check vs legacy_spec_map (human-validated).
D. Topic join: each SME topic's referenced codes -> exactly one KG subtopic (4CH1-S?-?).
"""
import json
from collections import Counter, defaultdict
from pathlib import Path

import yaml

BASE = Path("/home/z/my-project/work/sme-igcse-corpus")
GRAPH = Path("/home/z/my-project/work/syllabai-resources/graph")

def load_registry():
    g = yaml.safe_load((GRAPH / "specification_points.yaml").read_text())
    return {s["code"] for s in g["specification_points"]}

def load_subtopics():
    t = yaml.safe_load((GRAPH / "topics.yaml").read_text())
    subs = {s["code"]: set(s["spec_points"]) for s in t["subtopics"]}
    titles = {s["code"]: s["title"] for s in t["subtopics"]}
    return subs, titles

def main():
    registry = load_registry()
    subs, sub_titles = load_subtopics()
    print(f"registry: {len(registry)} codes | KG subtopics: {len(subs)}")

    # ---------- A+B: EQ ----------
    topics = sorted((BASE / "eq" / "sections").glob("*/*/topic.json"))
    tot_q = tot_parts = tot_mcq = tot_struct = tot_marks = 0
    bad_codes = Counter()
    ids_wo_codes = codes_wo_ids = 0
    multi_corr = zero_corr = no_choices = 0
    qmarks_bad = 0
    diff = Counter()
    sp_ref = set()
    topic_codes = {}          # topic_slug -> Counter(subtopic)
    src_paper = Counter()

    for tf in topics:
        slug = tf.parent.name
        d = json.load(open(tf))
        for q in d["questions"]:
            tot_q += 1
            diff[q["difficulty"]] += 1
            psum = 0
            for p in q["parts"]:
                tot_parts += 1
                m = p.get("marks") or 0
                tot_marks += m
                psum += m
                ids = p.get("spec_point_ids") or []
                codes = p.get("spec_point_codes") or []
                if ids and not codes: ids_wo_codes += 1
                if codes and not ids: codes_wo_ids += 1
                for c in codes:
                    sp_ref.add(c)
                    if c not in registry: bad_codes[c] += 1
                if p["question_type"] == "multiple_choice":
                    tot_mcq += 1
                    ch = p.get("choices") or []
                    if not ch: no_choices += 1
                    n = sum(1 for c in ch if c["is_correct"])
                    if n == 0: zero_corr += 1
                    elif n > 1: multi_corr += 1
                else:
                    tot_struct += 1
                sp = (p.get("source_paper") or {})
                src_paper["real" if sp.get("number") else "none"] += 1
            if q.get("total_marks") is not None and psum != q["total_marks"]:
                qmarks_bad += 1
        # topic join accumulation
        cc = Counter()
        for q in d["questions"]:
            for p in q["parts"]:
                for c in (p.get("spec_point_codes") or []):
                    for sc, spset in subs.items():
                        if c in spset:
                            cc[sc] += 1
                            break
        topic_codes[slug] = cc

    print("\n===== A. EQ SPEC-POINT MAPPING =====")
    print(f"questions {tot_q} | parts {tot_parts} (mcq {tot_mcq} / structured {tot_struct}) | marks {tot_marks}")
    print(f"ids-without-codes: {ids_wo_codes} | codes-without-ids: {codes_wo_ids}")
    print(f"codes NOT in 182 registry: {dict(bad_codes) if bad_codes else 'NONE — ALL VALID'}")
    print(f"distinct codes referenced: {len(sp_ref)}/182 | unreferenced: {len(registry - sp_ref)}")
    print(f"source_paper: {dict(src_paper)}")

    print("\n===== B. EQ STRUCTURE =====")
    print(f"difficulty {dict(diff)}")
    print(f"MCQ 0-correct {zero_corr} | >1-correct {multi_corr} | no-choices {no_choices}")
    print(f"questions part-marks != total: {qmarks_bad}")

    print("\n===== D. TOPIC JOIN (SME slug -> KG subtopic via SP containment) =====")
    bad_join = 0
    joins = {}
    for slug, cc in sorted(topic_codes.items()):
        if not cc:
            print(f"  {slug}: NO CODES")
            bad_join += 1
            continue
        dominant, n = cc.most_common(1)[0]
        total = sum(cc.values())
        purity = n / total
        if len(cc) > 1 or purity < 0.999:
            print(f"  {slug}: SPLIT {dict(cc)}")
            bad_join += 1
        joins[slug] = dominant
    print(f"clean 1:1 joins: {len(joins) - bad_join}/{len(joins)} | problematic: {bad_join}")
    # coverage: all 28 KG subtopics reached?
    reached = set(joins.values())
    print(f"KG subtopics reached: {len(reached)}/28 | unreached: {[s for s in subs if s not in reached]}")

    # ---------- C: RN ----------
    notes = sorted((BASE / "rn" / "notes").glob("**/*.json"))
    rn_ids = set()
    rn_bad = Counter()
    rn_ref = set()
    unmapped = []
    legacy_agree = legacy_total = 0
    figs = blocks_n = 0
    legacy_map_present = 0
    for nf in notes:
        d = json.load(open(nf))
        rid = d["note_id"]
        assert rid not in rn_ids, f"duplicate {rid}"
        rn_ids.add(rid)
        codes = d.get("spec_point_codes") or []
        for c in codes:
            rn_ref.add(c)
            if c not in registry: rn_bad[c] += 1
        if not codes: unmapped.append(str(nf.name))
        lsm = d.get("legacy_spec_map") or {}
        lsp = lsm.get("spec_points") or {}
        if lsp:
            legacy_map_present += 1
            # legacy shape: {code: {...}} presumably
            lc = {e["code"] for e in lsp if isinstance(e, dict) and e.get("code")}
            nc = set(codes)
            legacy_total += 1
            if lc == nc: legacy_agree += 1
        st = d.get("stats") or {}
        figs += st.get("figures") or 0
        blocks_n += st.get("blocks") or 0

    print("\n===== C. REVISION NOTES =====")
    print(f"pages {len(notes)} | unique rn_* ids {len(rn_ids)}")
    print(f"pages with codes: {len(notes) - len(unmapped)} | unmapped: {len(unmapped)} {unmapped[:5]}")
    print(f"codes NOT in registry: {dict(rn_bad) if rn_bad else 'NONE — ALL VALID'}")
    print(f"distinct codes referenced: {len(rn_ref)} | blocks {blocks_n} | figures {figs}")
    print(f"legacy_spec_map present: {legacy_map_present}/{len(notes)} | exact set agreement codes vs legacy: {legacy_agree}/{legacy_total}")

    # RN topic join: each note's codes -> KG subtopic, note path topic
    note_join_bad = 0
    for nf in notes:
        d = json.load(open(nf))
        codes = d.get("spec_point_codes") or []
        cc = Counter()
        for c in codes:
            for sc, spset in subs.items():
                if c in spset: cc[sc] += 1; break
        if len(cc) > 1:
            note_join_bad += 1
    print(f"RN pages spanning >1 KG subtopic (subtopic-granular, expected for some): {note_join_bad}")

if __name__ == "__main__":
    main()
