#!/usr/bin/env python3
"""Export the ADR-037 official-paper corpus into the syllabai-hub question-set
format (syllabai.sme-exam-questions/1.1 compatible, contract-additive).

Reads  : <repo>/Official-ExamQuestion/igcse-chemistry-19/<series>/4CH1-<paper>/topic.json
         the CURRENT hub content/igcse-chemistry-19/questions.json (28 SME sets)
Writes : <out>/content/igcse-chemistry-19/questions.json  (SME sets + 32 official sets)
Papers : EXAMQ_EXPORT_PAPERS env ("1C", "2C", or "1C,2C" default)

Contract notes (src/lib/contracts.ts in syllabai-hub):
- QuestionPart: id/order/questionType/marks/commandWord/specPointIds/
  specPointCodes/problemMd/solutionMd/choices?/sourcePaper? — this exporter
  ADDS markPoints[] + assets[] (added to the zod contract in the same PR).
- Unknown keys are stripped by zod; every required field is emitted exactly.
- Shared figure references (assets[].shared + ref_part) resolve to the owning
  part's/stem asset's PNG (same rawUrl) — the hub pattern embeds images as
  markdown, so shared figures inline the same URL.
"""
import json, glob, os, sys, hashlib
from pathlib import Path

# repo-relative (F15 portability): works from any checkout of syllabai-resources
CORPUS = str(Path(__file__).resolve().parents[1] / "Official-ExamQuestion" / "igcse-chemistry-19")
HUB_CURRENT = sys.argv[2] if len(sys.argv) > 2 else "/tmp/hub-chem-questions.json"
OUT = sys.argv[1] if len(sys.argv) > 1 else "/tmp/hub-stage"
RAW = "https://raw.githubusercontent.com/SyllabAI/syllabai-resources/main/Official-ExamQuestion/igcse-chemistry-19"
SERIES_LABEL = {"01": "January", "06": "June", "11": "November"}
OFFICIAL_SLUG_PREFIX = "official-4ch1-"


def series_label(series):
    year, mm = series.split("-")
    return f"{SERIES_LABEL.get(mm, mm)} {year}"


def part_slug(pn):
    return pn.replace("(", "-").replace(")", "")


PAPER = os.environ.get("EXAMQ_EXPORT_PAPERS", "1C,2C")


def raw_url(series, paper, rel_path):
    return f"{RAW}/{series}/4CH1-{paper}/{rel_path}"


def resolve_asset_path(a, by_id):
    """Shared refs point at the owner's PNG (same file); stem ids too."""
    if a.get("path"):
        return a["path"]
    ref = a.get("ref_part")
    if ref and ref in by_id:
        return by_id[ref].get("path")
    return None


def export_series(series, paper):
    tp = f"{CORPUS}/{series}/4CH1-{paper}/topic.json"
    tj = json.load(open(tp))
    # asset id -> asset (for shared-ref resolution)
    by_id = {}
    for q in tj["questions"]:
        for p in q["parts"]:
            for a in p.get("assets") or []:
                by_id[a["id"]] = a

    questions = []
    for qi, q in enumerate(tj["questions"]):
        qnum = str(q["question_number"])
        parts = []
        for p in q["parts"]:
            marks = int(p["marks"]) if p.get("marks") is not None else 0
            assets_out, figures_md = [], []
            for a in p.get("assets") or []:
                rel = resolve_asset_path(a, by_id)
                entry = {
                    "kind": a.get("kind"),
                    "mention": a.get("mention"),
                    "page": a.get("page"),
                    "review": bool(a.get("review")),
                    "shared": bool(a.get("shared")),
                }
                if a.get("ref_part"):
                    entry["refPart"] = a["ref_part"]
                if a.get("kind") == "crop" and rel:
                    entry["path"] = rel
                    entry["rawUrl"] = raw_url(series, paper, rel)
                    cap = f"{a.get('mention', 'figure')} — official paper figure (qp.pdf p.{a.get('page')})"
                    if a.get("shared"):
                        cap += f" (same figure as {a.get('ref_part')})"
                    figures_md.append(f"![{cap}]({entry['rawUrl']})")
                elif a.get("kind") == "crop-required":
                    figures_md.append(
                        "> *Figure pending scan — this scaffold is printed in the paper; "
                        "the crop is queued for human verification.*")
                assets_out.append(entry)
            problem_md = (p.get("problem_md") or "").strip()
            if figures_md:
                problem_md += "\n\n" + "\n\n".join(figures_md)
            sol = p.get("solution_md") or None
            mp = [{"id": x["id"], "marks": x["marks"], "textMd": x["text_md"]}
                  for x in (p.get("mark_points") or [])]
            choices = None
            if p.get("question_type") == "multiple_choice" and p.get("choices"):
                ch = p["choices"]
                if isinstance(ch, str):
                    ch = json.loads(ch)
                choices = [{"label": c["label"], "isCorrect": bool(c.get("is_correct")),
                            "textMd": c.get("text_md", "")} for c in ch]
            parts.append({
                "id": f"offp_{series}_{part_slug(p['part_number'])}",
                "order": len(parts),
                "questionType": p.get("question_type"),
                "marks": marks,
                "commandWord": None,
                "specPointIds": [],
                "specPointCodes": list(p.get("spec_point_codes") or []),
                "problemMd": problem_md,
                "solutionMd": sol,
                "markPoints": mp,
                "assets": assets_out,
                "answerStatus": p.get("answer_status"),
                "choices": choices,
                "sourcePaper": {
                    "date": series_label(series),
                    "number": f"4CH1/{paper}",
                    "questionNumber": int(qnum) if qnum.isdigit() else None,
                    "questionPart": None,
                },
            })
        questions.append({
            "id": f"offq_{series}_{part_slug(qnum)}",
            "order": qi,
            "difficulty": None,
            "style": "exam_whole",
            "totalMarks": int(q["total_marks"]) if q.get("total_marks") is not None else sum(x["marks"] for x in parts),
            "parts": parts,
        })

    return {
        "topicId": "off_" + hashlib.sha1(series.encode()).hexdigest()[:12],
        "slug": OFFICIAL_SLUG_PREFIX + paper.lower() + "-" + series,
        "name": f"{series_label(series)} — Paper {paper} (official past paper)",
        "setName": "Official Past Paper",
        "topicSlug": "official-past-papers",
        "section": f"Official past papers (4CH1/{paper})",
        "sectionSlug": "official-past-papers",
        "curriculum": {
            "board": "Pearson Edexcel",
            "level": "IGCSE",
            "subject": "Chemistry",
            "code": "4CH1",
            "syllabusVersion": "2017 (Issue 3)",
        },
        "source": {
            "provider": "Pearson Edexcel (operator archive, ADR-037 verbatim extraction)",
            "license": "operator-archive; extracted verbatim from the licensed archive PDFs — see syllabai-resources Official-ExamQuestion/README.md",
            "pageUrl": f"https://github.com/SyllabAI/syllabai-resources/tree/main/Official-ExamQuestion/igcse-chemistry-19/{series}/4CH1-{paper}",
        },
        "schema": "syllabai.official-paper-questions/0.1",
        "relatedNoteIds": [],
        "questions": questions,
    }


def main():
    hub = json.load(open(HUB_CURRENT))
    kept = [t for t in hub if not t["slug"].startswith(OFFICIAL_SLUG_PREFIX)]
    papers = [x.strip() for x in PAPER.split(",")]
    official = [export_series(s, paper)
                for paper in papers
                for s in ["2019-06", "2020-01", "2020-11", "2021-01", "2021-06", "2021-11",
                          "2022-01", "2022-06", "2023-01", "2023-06", "2023-11", "2024-06",
                          "2024-11", "2025-06", "2025-11", "2026-06"]]
    out = kept + official
    dest = os.path.join(OUT, "content/igcse-chemistry-19")
    os.makedirs(dest, exist_ok=True)
    json.dump(out, open(os.path.join(dest, "questions.json"), "w"), indent=1, ensure_ascii=False)
    n_sets = len(official)
    n_q = sum(len(t["questions"]) for t in official)
    n_p = sum(len(q["parts"]) for t in official for q in t["questions"])
    n_mp = sum(len(p["markPoints"]) for t in official for q in t["questions"] for p in q["parts"])
    n_fig = sum(1 for t in official for q in t["questions"] for p in q["parts"]
                for a in p["assets"] if a["kind"] == "crop")
    n_stub = sum(1 for t in official for q in t["questions"] for p in q["parts"]
                 for a in p["assets"] if a["kind"] == "crop-required")
    print(f"sets: {len(kept)} SME kept + {n_sets} official | questions: {n_q} | parts: {n_p} "
          f"| markPoints: {n_mp} | figure crops: {n_fig} | honest stubs: {n_stub}")
    print(f"written: {dest}/questions.json")


if __name__ == "__main__":
    main()
