#!/usr/bin/env python3
"""Export the ADR-037 official-paper corpus into the syllabai-hub question-set
format (syllabai.sme-exam-questions/1.1 compatible, contract-additive).

Reads  : <repo>/Official-ExamQuestion/igcse-chemistry-19/<series>/4CH1-<paper>/topic.json
         the CURRENT hub content/igcse-chemistry-19/questions.json (28 SME sets)
Writes : <out>/content/igcse-chemistry-19/questions.json  (SME sets + 32 official sets)
Papers : EXAMQ_EXPORT_PAPERS env ("1C", "2C", or "1C,2C" default)

Export gates (fail-closed, v3 of this script — the G-E law archived on PR #27,
landed in wave 12; F44 adds the per-paper topicSlug namespace + G-E1b identity
closure):
  G-E1  every regenerated set is compared against the bundle of record.
        Default: ANY delta fails the export (the reproducibility law — running
        the exporter of record against its own bundle must be a no-op).
        A content wave passes --expected-deltas <census.json>; the printed
        census (new/gone/changed part ids per slug) must EQUAL it exactly.
  G-E2  per-question sum(parts.marks) == totalMarks; every markPoints block
        sums to the part marks; specPointCodes is a list of strings.
  G-E3  per-slice census (questions/parts/marks) must equal the recorded
        MULTI-SERIES-REPORT constants for BOTH papers (hard stop on drift).
  G-E4  the SME prefix of the bundle re-serializes byte-identically (the
        official-papers export never touches the SME corpus of record).
Deterministic; no LLM in the loop.

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


def export_series(series, paper, topic=None):
    if topic is None:
        tp = f"{CORPUS}/{series}/4CH1-{paper}/topic.json"
        topic = json.load(open(tp))
    tj = topic
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
        # F44: topicSlug := the set's own canonical slug (the per-paper ref
        # namespace of record — v2 0776f8dea7, operator-ordered "path 1 — fix":
        # one shared topicSlug with per-set restarting orders collided 12 base
        # refs and the frozen package-global seenRefs gate refused the bundle).
        "topicSlug": OFFICIAL_SLUG_PREFIX + paper.lower() + "-" + series,
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


# G-E3 census of record — generated from MULTI-SERIES-REPORT.json @ converter
# v0.10.0 (wave 12: 2019-06 1C recovered through the F41 OCR layer).
# (questions, parts, marks) per slice; a mismatch is a hard stop.
EXPECTED_CENSUS = {
    "1C": {
        "2019-06": (15, 64, 110),
        "2020-01": (10, 60, 110),
        "2020-11": (10, 64, 110),
        "2021-01": (11, 53, 110),
        "2021-06": (10, 54, 110),
        "2021-11": (11, 67, 110),
        "2022-01": (11, 65, 110),
        "2022-06": (10, 57, 110),
        "2023-01": (12, 60, 110),
        "2023-06": (10, 55, 110),
        "2023-11": (10, 66, 110),
        "2024-06": (10, 56, 110),
        "2024-11": (11, 56, 110),
        "2025-06": (10, 49, 110),
        "2025-11": (10, 59, 110),
        "2026-06": (9, 56, 110),
    },
    "2C": {
        "2019-06": (8, 39, 70),
        "2020-01": (7, 39, 70),
        "2020-11": (7, 35, 70),
        "2021-01": (7, 39, 70),
        "2021-06": (7, 43, 70),
        "2021-11": (7, 41, 70),
        "2022-01": (7, 41, 70),
        "2022-06": (7, 39, 70),
        "2023-01": (7, 37, 70),
        "2023-06": (7, 41, 70),
        "2023-11": (7, 37, 70),
        "2024-06": (7, 37, 70),
        "2024-11": (7, 34, 70),
        "2025-06": (6, 38, 70),
        "2025-11": (6, 31, 70),
        "2026-06": (6, 36, 70),
    },
}

ALL_SERIES = ["2019-06", "2020-01", "2020-11", "2021-01", "2021-06", "2021-11",
              "2022-01", "2022-06", "2023-01", "2023-06", "2023-11", "2024-06",
              "2024-11", "2025-06", "2025-11", "2026-06"]


class ExportGateError(Exception):
    pass


def census(s):
    nq = len(s["questions"])
    nps = sum(len(q["parts"]) for q in s["questions"])
    mk = sum(p["marks"] for q in s["questions"] for p in q["parts"])
    return nq, nps, mk


def is_official(t):
    """F44: official sets are identified by their slug prefix, never by
    topicSlug (which is the set's own slug since the per-paper namespace
    law) — the old topicSlug=='official-past-papers' filter silently
    selected zero sets after that law landed."""
    return t.get("slug", "").startswith(OFFICIAL_SLUG_PREFIX)


# G-E1b: set-level identity fields — a law, not a wave artifact (F44). The
# part census cannot see these; the topicSlug namespace drift rode exactly
# this blind spot. Any drift fails with no disclosure path: a real namespace
# change must land in the exporter of record and the bundle in the same
# reviewed PR.
IDENTITY_FIELDS = ("topicId", "slug", "name", "setName", "topicSlug",
                   "section", "sectionSlug", "curriculum", "source",
                   "schema", "relatedNoteIds")


def part_map(s):
    return {p["id"]: p for q in s["questions"] for p in q["parts"]}


def run_gates(out_sets, raw_bundle_bytes, expected_deltas_path, topics_src):
    """G-E1..G-E4 against the bundle of record. topics_src(series, paper) -> topic dict."""
    by_slug = {t.get("slug"): t for t in json.loads(raw_bundle_bytes)}
    # ---- G-E3: census constants (cheap, run first) ----
    for paper in ("1C", "2C"):
        for series in ALL_SERIES:
            s = next(t for t in out_sets if t["slug"] == f"official-4ch1-{paper.lower()}-{series}")
            c = census(s)
            exp = EXPECTED_CENSUS[paper][series]
            if c != exp:
                raise ExportGateError(f"G-E3 {series}/{paper}: census {c} != expected {exp}")
    print(f"G-E3 ok: 32 slices match the v0.10.0 MULTI-SERIES constants "
          f"({sum(census(t)[2] for t in out_sets if is_official(t))} marks)")
    # ---- G-E2: sum laws ----
    for t in out_sets:
        if not is_official(t):
            continue
        for q in t["questions"]:
            if sum(p["marks"] for p in q["parts"]) != q["totalMarks"]:
                raise ExportGateError(f"G-E2 part-sum violation in {t['slug']} {q['id']}")
            for p in q["parts"]:
                msum = sum(m["marks"] for m in (p.get("markPoints") or []))
                if p.get("markPoints") and msum != p["marks"]:
                    raise ExportGateError(f"G-E2 markPoints sum {msum} != {p['marks']} at {p['id']}")
                if not all(isinstance(c, str) for c in (p.get("specPointCodes") or [])):
                    raise ExportGateError(f"G-E2 spec codes not strings at {p['id']}")
    print("G-E2 ok: part-sum, markPoints sum-law and spec-code shapes hold on all official sets")
    # ---- G-E1: regenerate vs bundle of record ----
    census_rows = {"new": {}, "gone": {}, "changed": {}}
    ident_drift = []
    for paper in ("1C", "2C"):
        for series in ALL_SERIES:
            slug = f"official-4ch1-{paper.lower()}-{series}"
            rebuilt = export_series(series, paper, topics_src(series, paper))
            of_record = by_slug.get(slug)
            if of_record is None:
                raise ExportGateError(f"G-E1: bundle of record lacks {slug}")
            for f in IDENTITY_FIELDS:
                if json.dumps(rebuilt.get(f), sort_keys=True) != json.dumps(of_record.get(f), sort_keys=True):
                    ident_drift.append(f"{slug}: {f}")
            rp, op = part_map(rebuilt), part_map(of_record)
            new_ids = sorted(set(rp) - set(op))
            gone_ids = sorted(set(op) - set(rp))
            changed = sorted(pid for pid in set(rp) & set(op)
                             if json.dumps(rp[pid], sort_keys=True) != json.dumps(op[pid], sort_keys=True))
            if new_ids:
                census_rows["new"].setdefault(slug, []).extend(new_ids)
            if gone_ids:
                census_rows["gone"].setdefault(slug, []).extend(gone_ids)
            if changed:
                census_rows["changed"].setdefault(slug, []).extend(changed)
    flat = {k: {s: v for s, v in d.items() if v} for k, d in census_rows.items()}
    n_delta = sum(len(v) for d in flat.values() for v in d.values())
    if n_delta == 0:
        print("G-E1 ok: regeneration is a byte-level no-op against the bundle of record")
    else:
        if not expected_deltas_path:
            for k in ("new", "gone", "changed"):
                for slug, ids in flat[k].items():
                    for pid in ids:
                        print(f"  DELTA {k}: {slug} {pid}")
            raise ExportGateError(
                f"G-E1: {n_delta} deltas vs the bundle of record with no --expected-deltas "
                f"census (the reproducibility law: an exporter of record run against its own "
                f"bundle must be a no-op; a content wave must disclose its census)")
        expected = json.load(open(expected_deltas_path))
        if json.dumps(flat, sort_keys=True) != json.dumps(expected, sort_keys=True):
            raise ExportGateError("G-E1: delta census != --expected-deltas (the printed "
                                  "DELTA listing above shows the fresh census; regenerate "
                                  "the disclosure file only after eyeballing every class)")
        print(f"G-E1 ok: {n_delta} deltas match the disclosed wave census exactly")
    if ident_drift:
        for d in ident_drift:
            print(f"  IDENTITY DRIFT {d}")
        raise ExportGateError("G-E1b: set-level identity drift vs the bundle of record "
                              "(identity fields are a law, not a wave artifact — a real "
                              "namespace change must land in the exporter of record and the "
                              "bundle in the same reviewed PR)")
    print("G-E1b ok: set-level identity fields byte-equal on all 32 official sets")
    # ---- G-E4: the SME prefix is never touched ----
    first_off = raw_bundle_bytes.find(b'"topicId": "off_')
    if first_off == -1:
        raise ExportGateError("G-E4: no official block found in the bundle of record")
    out_bytes = json.dumps(out_sets, indent=1, ensure_ascii=False).encode()
    if out_bytes[:first_off] != raw_bundle_bytes[:first_off]:
        for i in range(first_off):
            if out_bytes[i] != raw_bundle_bytes[i]:
                raise ExportGateError(
                    f"G-E4: SME prefix diverges at byte {i}: "
                    f"{raw_bundle_bytes[max(0, i - 60):i + 60]!r} vs "
                    f"{out_bytes[max(0, i - 60):i + 60]!r}")
        raise ExportGateError("G-E4: SME prefix length drift")
    print(f"G-E4 ok: SME prefix byte-identical ({first_off} bytes)")


def main():
    import argparse
    ap = argparse.ArgumentParser()
    ap.add_argument("out_stage")
    ap.add_argument("current_questions")
    ap.add_argument("--topics-dir", default=None,
                    help="dir holding <series>-<paper>.json staging copies of the corpus topics")
    ap.add_argument("--expected-deltas", default=None,
                    help="disclosed delta census for a content wave (default: zero deltas)")
    ap.add_argument("--manifest", default=None,
                    help="manifest.json beside the bundle of record; staged with bumped note")
    args = ap.parse_args()
    topics_dir = args.topics_dir or os.path.join(os.getcwd(), "topics")

    def topics_src(series, paper):
        return json.load(open(os.path.join(topics_dir, f"{series}-{paper}.json")))

    raw = open(args.current_questions, "rb").read()
    hub = json.loads(raw)
    kept = [t for t in hub if not t["slug"].startswith(OFFICIAL_SLUG_PREFIX)]
    official = [export_series(s, paper, topics_src(s, paper))
                for paper in ("1C", "2C") for s in ALL_SERIES]
    out = kept + official

    run_gates(out, raw, args.expected_deltas, topics_src)

    dest = os.path.join(args.out_stage, "content", "igcse-chemistry-19")
    os.makedirs(dest, exist_ok=True)
    with open(os.path.join(dest, "questions.json"), "wb") as f:
        f.write(json.dumps(out, indent=1, ensure_ascii=False).encode())
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
    if args.manifest and os.path.exists(args.manifest):
        manifest = json.load(open(args.manifest))
        official_n = sum(1 for t in out if is_official(t))
        manifest["importSource"]["note"] = (
            "ADR-037 converter v0.11.0 corpus (merged main): wave-14 closes the last three "
            "honest review items, corpus review queue now empty. F48 PUA->Unicode pass: all "
            "23 symbol-font PUA chars in the source text layer map to real Unicode from "
            "evidence (font trace + page render per glyph - arrows, Delta x2, equilibrium, "
            "Sigma, check, bullets, degree, times, divide, minus, bond rule); served corpus "
            "text is PUA-free and fail-closed on unmapped chars (C56 pins absence + nine "
            "mappings). F46 deep-indent roman MS rows: 2023-11 1C 6(c)(ii)/6(d)(ii) link "
            "(G5 66/66), their (i)-blocks lose the absorbed rows. F47 MS-LINK-OVERRIDES "
            "ledger: 2019-06 1C 3(d)(ii) MS-image answer cell human-adjudicated as verbatim "
            "tick-table transcription (C52/C57). Four page anchors restored by the cleaner "
            "text (2021-06 2C 7(c)(i), 2022-06 2C 5(c)(ii), 2025-06 2C 6(a)(ii), 2026-06 1C "
            "7(a)(ii)). This bundle reconciles to the corpus of record on one part: "
            "3(d)(ii) serves the verbatim transcription (the previously staged interpretive "
            "summary + ms-image asset is superseded; sourcePage 7 restored). "
            f"{official_n} official sets (16x1C + 16x2C), {n_q} questions, {n_p} parts, all "
            "spec-tagged (1C wave 2 + 2C wave 1).")
        os.makedirs(args.out_stage, exist_ok=True)
        with open(os.path.join(args.out_stage, "manifest.json"), "wb") as f:
            f.write(json.dumps(manifest, indent=1, ensure_ascii=False).encode())
        print(f"manifest staged (importSource.ref stays; note bumped to the v0.11.0 wave description)")
    print(f"written: {dest}/questions.json")


if __name__ == "__main__":
    main()
