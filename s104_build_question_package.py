#!/usr/bin/env python3
"""s104 — build the SME Exam Question corpus package for the SyllabAI backend.

Source: SME-ExamQuestion/igcse-chemistry-19 (Save My Exams, operator-attested)
Output: a versioned ZIP package:
    package.json  — questions in the sme-question-package/1.0 format
    assets/<file> — every image referenced by problem/solution markdown

Mapping rules (deterministic, zero-LLM — see ADR-026):
  * single-MCQ question            -> MCQ_SINGLE (stem=problem_md, options)
  * pure structured question       -> STRUCTURED (stem="", one part per SME part)
  * mixed / multi-MCQ question     -> SPLIT: each MCQ part its own MCQ_SINGLE
                                      (ref -pN), structured parts one STRUCTURED
                                      (ref -s). Parts carry their own context.
  * difficulty  easy->2 medium->3 hard->4          (difficulty_source=SME)
  * expected time  MCQ 90s; structured 60+60*marks (deterministic formula)
  * primary topic = KG subtopic owning the plurality of part SP codes;
    secondary topics = the rest (question_topics)
  * spec points    = ordered unique part codes; first PRIMARY, rest SECONDARY;
    provenance AI_VALIDATED (operator-delegated 2026-09-17 resolution)
  * part labels    = source_paper.question_part when present else a,b,c...

Fail-closed: an asset referenced but absent from the corpus aborts the build.
"""
from __future__ import annotations

import json
import re
import sys
import zipfile
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml

SPARSE = Path("/home/z/my-project/work/sme-sparse/SME-ExamQuestion/igcse-chemistry-19")
OUT = Path("/home/z/my-project/work/sme-igcse-corpus/dist/sme-question-package.zip")
GRAPH = Path("/home/z/my-project/work/syllabai-resources/graph")
PACKAGE_VERSION = "1.0"

DIFFICULTY = {"easy": 2, "medium": 3, "hard": 4}
IMG = re.compile(r"!\[[^\]]*\]\(assets/([^)\s]+)\)")
SAFE_NAME = re.compile(r"^[A-Za-z0-9][A-Za-z0-9 ._()-]{0,255}$")


def load_graph():
    t = yaml.safe_load((GRAPH / "topics.yaml").read_text())
    sub_by_code = {s["code"]: set(s["spec_points"]) for s in t["subtopics"]}
    code2sub = {}
    for sc, sps in sub_by_code.items():
        for c in sps:
            code2sub.setdefault(c, sc)
    # fallback placement: SME topic ordinal within section -> KG subtopic
    # ordinal (letter order within the same parent section)
    sub_by_parent = {}
    for s in t["subtopics"]:
        sub_by_parent.setdefault(s["parent"], []).append(s["code"])
    for v in sub_by_parent.values():
        v.sort()
    return sub_by_code, code2sub, sub_by_parent


def norm_command(w):
    if not w:
        return None
    w = w.strip().lower()
    return None if w in ("multiple", "") else w[:30]


def part_label(i, sp, taken):
    """Real SME label when present, valid and unused; else the next unused
    letter. Uniqueness is load-bearing (uq_question_part)."""
    lbl = (sp or {}).get("question_part")
    if lbl and re.fullmatch(r"[a-h]{1,3}(\([ivx]+\))?", str(lbl)) and str(lbl) not in taken:
        taken.add(str(lbl))
        return str(lbl)[:12]
    c = chr(ord("a") + i)
    while c in taken:
        c = chr(ord(c) if ord(c) < 122 else 97)  # wrap-safe-ish; corpus max 7 parts
        c = c + "x" if c == "z" else c
        break
    # simple deterministic uniquifier: next letter not taken
    base = chr(ord("a") + i)
    cand, n = base, 2
    while cand in taken:
        cand = f"{base}{n}"
        n += 1
    taken.add(cand)
    return cand[:12]


def topic_placement(codes, code2sub):
    subs = [code2sub[c] for c in codes if c in code2sub]
    if not subs:
        return None, []
    primary = Counter(subs).most_common(1)[0][0]
    secondary = [s for s in dict.fromkeys(subs) if s != primary]
    return primary, secondary


    # (see load_graph return)
    pass

def build2():
    sub_by_code, code2sub, sub_by_parent = load_graph()
    eq_root = SPARSE
    topics = sorted(eq_root.glob("*/"))                     # 4 sections
    questions = []
    assets = {}
    problems = []

    def asset_add(name):
        if name in assets:
            return
        # assets live per-topic: search the whole course tree (names unique)
        hits = list(eq_root.rglob(name))
        if not hits:
            problems.append(f"missing asset {name}")
            return
        assets[name] = hits[0]

    for sec in topics:
        for tf in sorted(sec.glob("*/topic.json")):
            slug = tf.parent.name
            d = json.loads(tf.read_text())
            for q in d["questions"]:
                base_ref = f"sme-eq-{slug}-q{q['order']}"
                codes = []
                for p in q["parts"]:
                    for c in (p.get("spec_point_codes") or []):
                        if c not in codes:
                            codes.append(c)
                primary, secondary = topic_placement(codes, code2sub)
                if primary is None:
                    # deterministic fallback: topic ordinal -> KG subtopic;
                    # SP mappings stay empty (never guessed)
                    sec_n = slug.split("-")[0]
                    top_n = int(slug.split("-")[1])
                    subs = sub_by_parent.get(f"4CH1-S{sec_n}", [])
                    if not (1 <= top_n <= len(subs)):
                        problems.append(f"{base_ref}: no codes and no structural fallback")
                        continue
                    primary, secondary, codes = subs[top_n - 1], [], []
                diff = DIFFICULTY[q["difficulty"]]
                srcs = [p.get("source_paper") for p in q["parts"]]
                qpaper = srcs[0] if all(s == srcs[0] for s in srcs) and (srcs[0] or {}).get("number") else None

                mcq_parts = [p for p in q["parts"] if p["question_type"] == "multiple_choice"]
                st_parts = [p for p in q["parts"] if p["question_type"] == "structured"]

                def spoints():
                    return [{"code": c, "role": "PRIMARY" if i == 0 else "SECONDARY",
                             "provenance": "AI_VALIDATED"} for i, c in enumerate(codes)]

                def collect_assets(md_list):
                    for md in md_list:
                        for m in IMG.finditer(md or ""):
                            asset_add(m.group(1))

                # ---- split rule ----
                if len(q["parts"]) == 1 and mcq_parts:
                    p = q["parts"][0]
                    collect_assets([p["problem_md"], p["solution_md"]])
                    questions.append({
                        "externalRef": base_ref,
                        "questionType": "MCQ_SINGLE",
                        "stem": p["problem_md"],
                        "marks": p["marks"],
                        "difficulty": diff,
                        "difficultySource": "SME",
                        "expectedTimeSeconds": 90,
                        "commandWord": norm_command(p.get("command_word")),
                        "primaryTopicCode": primary,
                        "secondaryTopicCodes": secondary,
                        "specPoints": spoints(),
                        "sourcePaper": qpaper,
                        "smeSet": q.get("set_slug"),
                        "smeDifficulty": q["difficulty"],
                        "options": [{"label": c["label"], "text": c["text_md"],
                                     "isCorrect": bool(c["is_correct"])}
                                    for c in p.get("choices", [])],
                        "solutionMd": p["solution_md"],
                        "parts": [],
                    })
                else:
                    if mcq_parts:
                        for n, p in enumerate(mcq_parts, 1):
                            collect_assets([p["problem_md"], p["solution_md"]])
                            questions.append({
                                "externalRef": f"{base_ref}-p{n}",
                                "questionType": "MCQ_SINGLE",
                                "stem": p["problem_md"],
                                "marks": p["marks"],
                                "difficulty": diff,
                                "difficultySource": "SME",
                                "expectedTimeSeconds": 90,
                                "commandWord": norm_command(p.get("command_word")),
                                "primaryTopicCode": primary,
                                "secondaryTopicCodes": secondary,
                                "specPoints": spoints(),
                                "sourcePaper": p.get("source_paper"),
                                "smeSet": q.get("set_slug"),
                                "smeDifficulty": q["difficulty"],
                                "options": [{"label": c["label"], "text": c["text_md"],
                                             "isCorrect": bool(c["is_correct"])}
                                            for c in p.get("choices", [])],
                                "solutionMd": p["solution_md"],
                                "parts": [],
                            })
                    if st_parts:
                        total = sum(p["marks"] for p in st_parts)
                        collect_assets([p["problem_md"] for p in st_parts] +
                                       [p["solution_md"] for p in st_parts])
                        taken_labels: set = set()
                        questions.append({
                            "externalRef": base_ref + ("-s" if mcq_parts else ""),
                            "questionType": "STRUCTURED",
                            "stem": "",
                            "marks": total,
                            "difficulty": diff,
                            "difficultySource": "SME",
                            "expectedTimeSeconds": 60 + 60 * total,
                            "commandWord": norm_command(q["parts"][0].get("command_word")),
                            "primaryTopicCode": primary,
                            "secondaryTopicCodes": secondary,
                            "specPoints": spoints(),
                            "sourcePaper": qpaper,
                            "smeSet": q.get("set_slug"),
                            "smeDifficulty": q["difficulty"],
                            "options": [],
                            "solutionMd": None,
                            "parts": [{"label": part_label(i, p.get("source_paper"), taken_labels),
                                       "prompt": p["problem_md"],
                                       "marks": p["marks"],
                                       "commandWord": norm_command(p.get("command_word")),
                                       "solutionMd": p["solution_md"]}
                                      for i, p in enumerate(st_parts)],
                        })

    if problems:
        print("BUILD ABORTED — problems:", file=sys.stderr)
        for p in problems:
            print("  -", p, file=sys.stderr)
        sys.exit(1)

    questions.sort(key=lambda q: q["externalRef"])
    refs = [q["externalRef"] for q in questions]
    assert len(refs) == len(set(refs)), "duplicate externalRef"
    for q in questions:
        if q["questionType"] == "MCQ_SINGLE":
            assert any(o["isCorrect"] for o in q["options"]) and \
                   sum(o["isCorrect"] for o in q["options"]) == 1, q["externalRef"]
        else:
            assert q["parts"], q["externalRef"]
            assert sum(p["marks"] for p in q["parts"]) == q["marks"], q["externalRef"]

    pkg = {
        "packageVersion": PACKAGE_VERSION,
        "corpusVersion": "sme-eq-igcse-chemistry-19",
        "generatedAt": datetime.now(timezone.utc).isoformat(),
        "source": "Save My Exams (operator-attested; LICENSE-DATA.md Amendment 2026-09-17)",
        "counts": {
            "questions": len(questions),
            "mcq": sum(1 for q in questions if q["questionType"] == "MCQ_SINGLE"),
            "structured": sum(1 for q in questions if q["questionType"] == "STRUCTURED"),
            "marks": sum(q["marks"] for q in questions),
            "assets": len(assets),
            "specPointCodes": len({s["code"] for q in questions for s in q["specPoints"]}),
        },
        "questions": questions,
    }

    OUT.parent.mkdir(parents=True, exist_ok=True)
    with zipfile.ZipFile(OUT, "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("package.json", json.dumps(pkg, ensure_ascii=False, indent=1))
        for name in sorted(assets):
            z.writestr(f"assets/{name}", assets[name].read_bytes())

    print(json.dumps(pkg["counts"], indent=1))
    print(f"package: {OUT} ({OUT.stat().st_size/1e6:.1f} MB)")
    return pkg


if __name__ == "__main__":
    build2()
