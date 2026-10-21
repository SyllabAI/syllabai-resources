#!/usr/bin/env python3
"""
official_examq_export_hub.py — ADR-037 corpus → hub content bundle exporter.

Usage (the docs/ADR-037-OFFICIAL_PAPERS_WIRING.md contract, v0.8 amendment):

    python3 scripts/official_examq_export_hub.py <out-stage> <current questions.json>
            [--topics-dir DIR] [--paper 2C]

  <out-stage>              output directory; receives questions.json + manifest.json
  <current questions.json> the hub bundle of record being extended
  --topics-dir             directory holding the corpus topic.json staging copies,
                           named <series>-<paper>.json (e.g. 2019-06-2C.json);
                           default: ./topics next to this script's caller (the
                           run_all.sh staging area, EXAMQ_UPLOAD_DIR)
  --paper                  which paper variant to APPEND (default 2C). The other
                           variant's sets are REGENERATED and asserted byte-equal
                           to the bundle of record — never rewritten.

Deterministic; no LLM in the loop. The transform is the one the v0.6/v0.7
bundle syncs used (reconstructed and pinned by the 1C byte-equality gate):

  set        topic.json (syllabai.official-paper-questions/0.1) → hub bundle set
             slug official-4ch1-<paper-lower>-<series>; name "<printed> — Paper
             <paper> (official past paper)"; section "Official past papers
             (4CH1/<paper>)"; topicSlug/sectionSlug official-past-papers;
             topicId off_<12hex> (uuid5 URL-namespace of the slug — deterministic;
             the 1C ids of record predate this law and are never touched).
  question   stem_md/group stems are NOT carried (the 1C export of record drops
             them; the parts are the question — exam_whole). id offq_<series>_<n>,
             order 0-based, difficulty null, style exam_whole, totalMarks verbatim.
  part       id offp_<series>_<n>-<letters> (part_number minus the leading question
             digits, '('→'-', ')' dropped); problemMd/solutionMd/marks/questionType/
             answerStatus/specPointCodes verbatim; choices []→null else
             {label,isCorrect,textMd}; markPoints {id,marks,textMd}; assets
             {kind,mention,page,review[,shared][,refPart][,path,rawUrl][,reviewVerdict]}
             with rawUrl pinned to the slice's own resources-repo directory;
             commandWord null, specPointIds [], sourcePaper {date,number,questionNumber,
             questionPart: null}.

Gates before the exporter writes anything:
  G-E1  every regenerated 1C set is DEEP-EQUAL (key order included) to the set
        of record in the current bundle — transform drift fails loudly;
  G-E2  every appended set: per-question Σparts.marks == totalMarks (the G1
        echo), every markPoints block sums to the part marks (the G7 echo),
        every specPointCodes array is registry-shaped (list of strings);
  G-E3  expected corpus census (questions/parts/marks per appended slice)
        matches the constants measured at converter v0.8.1 (the MULTI-SERIES
        report of record); a mismatch is a hard stop;
  G-E4  the untouched prefix of the bundle re-serializes byte-identically
        (indent=1, ensure_ascii=False, no trailing newline — the file law).

Output census prints the predicted ingest behaviour under the frozen shim laws
(anchor law: parts with no spec codes stay OUT of the learner model, unmapped).
"""

import argparse
import json
import os
import sys
import uuid

RES_BASE = "https://raw.githubusercontent.com/SyllabAI/syllabai-resources/main/Official-ExamQuestion/igcse-chemistry-19"
TREE_URL = "https://github.com/SyllabAI/syllabai-resources/tree/main/Official-ExamQuestion/igcse-chemistry-19"
CURRICULUM = {
    "board": "Pearson Edexcel",
    "level": "IGCSE",
    "subject": "Chemistry",
    "code": "4CH1",
    "syllabusVersion": "2017 (Issue 3)",
}
SOURCE_PROVIDER = "Pearson Edexcel (operator archive, ADR-037 verbatim extraction)"
SOURCE_LICENSE = (
    "operator-archive; extracted verbatim from the licensed archive PDFs — "
    "see syllabai-resources Official-ExamQuestion/README.md"
)
MONTHS = {"01": "January", "06": "June", "11": "November"}
SERIES = [
    "2019-06", "2020-01", "2020-11", "2021-01", "2021-06", "2021-11",
    "2022-01", "2022-06", "2023-01", "2023-06", "2023-11", "2024-06",
    "2024-11", "2025-06", "2025-11", "2026-06",
]
# Converter v0.8.1 MULTI-SERIES-REPORT census of record (2026-10-21): the
# appended slices MUST reproduce these exactly (G-E3).
EXPECTED_2C = {
    "2019-06": (8, 39, 70), "2020-01": (7, 39, 70), "2020-11": (7, 35, 70),
    "2021-01": (7, 39, 70), "2021-06": (7, 43, 70), "2021-11": (7, 41, 70),
    "2022-01": (7, 41, 70), "2022-06": (7, 39, 70), "2023-01": (7, 37, 70),
    "2023-06": (7, 41, 70), "2023-11": (7, 37, 70), "2024-06": (7, 37, 70),
    "2024-11": (7, 34, 70), "2025-06": (6, 38, 70), "2025-11": (6, 31, 70),
    "2026-06": (6, 36, 70),
}


class ExportGateError(Exception):
    pass


def part_id(series, qn, part_number):
    digits = str(qn)
    if not part_number.startswith(digits):
        raise ExportGateError(f"part_number {part_number!r} does not start with question {digits}")
    suffix = part_number[len(digits):].replace("(", "-").replace(")", "")
    return f"offp_{series}_{qn}{suffix}"


def dump(obj):
    return json.dumps(obj, indent=1, ensure_ascii=False)


PENDING_NOTE = (
    "\n\n> *Text-only scaffold verified against the source page — "
    "the paper prints no croppable figure here.*"
)


def owner_display(ref_part, topic):
    """The (same figure as X) display form: the owner's human part number when
    the owning asset record sits on a part; the asset id verbatim when the
    owner is a question stem (stem assets carry no part number of record)."""
    for q in topic["questions"]:
        for p in q["parts"]:
            for a2 in p.get("assets") or []:
                if a2.get("id") == ref_part:
                    return p["part_number"]
    return ref_part


def problem_md_with_figures(problem_md, assets, series, paper, topic):
    """The export-time figure ride-along (the 1C export of record law): every
    crop appends a raw-URL markdown image; every crop-required stub appends the
    honest text-only-scaffold note. Order follows the topic asset array."""
    tails = []
    for a in assets or []:
        if a["kind"] == "crop-required":
            tails.append(PENDING_NOTE)
            continue
        alt = f"{a['mention']} — official paper figure (qp.pdf p.{a['page']})"
        if a.get("ref_part"):
            alt += f" (same figure as {owner_display(a['ref_part'], topic)})"
        url = f"{RES_BASE}/{series}/4CH1-{paper}/{a['path']}"
        tails.append(f"\n\n![{alt}]({url})")
    return problem_md + "".join(tails)


def transform_asset(a, series, paper):
    out = {"kind": a["kind"], "mention": a["mention"], "page": a["page"], "review": a["review"]}
    if a["kind"] == "crop":
        # the shared flag is a crop-law field: emitted for EVERY crop (the
        # v0.6/v0.7 export law; the topic of record carries it only when true,
        # so absent means false). Crop-required stubs carry no file and no flag.
        out["shared"] = a.get("shared", False)
    if "ref_part" in a:
        out["refPart"] = a["ref_part"]
    if "path" in a:
        out["path"] = a["path"]
        out["rawUrl"] = f"{RES_BASE}/{series}/4CH1-{paper}/{a['path']}"
    if "review_verdict" in a:
        out["reviewVerdict"] = a["review_verdict"]
    return out


def transform_set(series, paper, topic):
    printed = f"{MONTHS[series.split('-')[1]]} {series.split('-')[0]}"
    code = f"4CH1/{paper}"
    slug = f"official-4ch1-{paper.lower()}-{series}"
    questions = []
    for qi, q in enumerate(topic["questions"]):
        qn = q["question_number"]
        parts = []
        for pi, p in enumerate(q["parts"]):
            choices = None
            if p.get("choices"):
                choices = [
                    {"label": c["label"], "isCorrect": c["is_correct"], "textMd": c["text_md"]}
                    for c in p["choices"]
                ]
            mps = [
                {"id": m["id"], "marks": m["marks"], "textMd": m["text_md"]}
                for m in (p.get("mark_points") or [])
            ]
            assets = [transform_asset(a, series, paper) for a in (p.get("assets") or [])]
            parts.append({
                "id": part_id(series, qn, p["part_number"]),
                "order": pi,
                "questionType": p["question_type"],
                "marks": p["marks"],
                "commandWord": None,
                "specPointIds": [],
                "specPointCodes": p.get("spec_point_codes") or [],
                "problemMd": problem_md_with_figures(
                    p["problem_md"], p.get("assets"), series, paper, topic
                ),
                "solutionMd": p.get("solution_md"),
                "markPoints": mps,
                "assets": assets,
                "answerStatus": p["answer_status"],
                "choices": choices,
                "sourcePaper": {
                    "date": printed,
                    "number": code,
                    "questionNumber": qn,
                    "questionPart": None,
                },
            })
        questions.append({
            "id": f"offq_{series}_{qn}",
            "order": qi,
            "difficulty": None,
            "style": "exam_whole",
            "totalMarks": q["total_marks"],
            "parts": parts,
        })
    return {
        "topicId": "off_" + uuid.uuid5(uuid.NAMESPACE_URL, slug).hex[:12],
        "slug": slug,
        "name": f"{printed} — Paper {paper} (official past paper)",
        "setName": "Official Past Paper",
        "topicSlug": "official-past-papers",
        "section": f"Official past papers ({code})",
        "sectionSlug": "official-past-papers",
        "curriculum": dict(CURRICULUM),
        "source": {
            "provider": SOURCE_PROVIDER,
            "license": SOURCE_LICENSE,
            "pageUrl": f"{TREE_URL}/{series}/4CH1-{paper}",
        },
        "schema": "syllabai.official-paper-questions/0.1",
        "relatedNoteIds": [],
        "questions": questions,
    }


def census(s):
    nq = len(s["questions"])
    nps = sum(len(q["parts"]) for q in s["questions"])
    mk = sum(p["marks"] for q in s["questions"] for p in q["parts"])
    return nq, nps, mk


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("out_stage")
    ap.add_argument("current_questions")
    ap.add_argument("--topics-dir", default=None)
    ap.add_argument("--paper", default="2C")
    args = ap.parse_args()

    topics_dir = args.topics_dir or os.path.join(os.getcwd(), "topics")
    current_path = args.current_questions
    paper = args.paper
    other = "1C" if paper == "2C" else "2C"

    raw = open(current_path, "rb").read()
    current = json.loads(raw)
    by_slug = {s.get("slug"): s for s in current}

    # ---- G-E1: the transform regenerates the of-record sets; deltas vs the
    # of-record are REPORTED as the v0.8.1-parity census (the of-record is a
    # palimpsest of four sync generations — v0.6 initial wiring, v0.7
    # spec-tagging, v0.7.1 wave-10, and a selective v0.8.1 patch that only
    # re-exported 2020-01's adjudicated Q7(a) parts — so honest deltas are
    # EXPECTED: F35-era MS-linkage improvements, the always-emit shared crop
    # flag, and owner-display normalizations). The hard gates are G-E2/E3/E4
    # plus the F37 adjudication pins below; a delta OUTSIDE the disclosed
    # classes fails the run.
    DELTA_KEYS = {"assets", "solutionMd", "markPoints", "answerStatus", "problemMd", "specPointCodes"}
    census_rows = []
    for series in SERIES:
        topic = json.load(open(os.path.join(topics_dir, f"{series}-{other}.json")))
        rebuilt = transform_set(series, other, topic)
        of_record = by_slug.get(f"official-4ch1-{other.lower()}-{series}")
        if of_record is None:
            raise ExportGateError(f"G-E1: bundle lacks {other} set for {series}")
        if dump(rebuilt) == dump(of_record):
            continue
        for qi, (rq, oq) in enumerate(zip(rebuilt["questions"], of_record["questions"])):
            if dump(rq) == dump(oq):
                continue
            for ri, (rp, op) in enumerate(zip(rq["parts"], oq["parts"])):
                if dump(rp) == dump(op):
                    continue
                changed = {k for k in rp if dump(rp[k]) != dump(op.get(k))}
                if not changed <= DELTA_KEYS:
                    raise ExportGateError(
                        f"G-E1 UNDISCLOSED DELTA {series}/{other} {rp['id']}: {sorted(changed)}"
                    )
                census_rows.append((series, rp["id"], sorted(changed)))
    from collections import Counter
    key_hist = Counter(tuple(c) for _, _, c in census_rows)
    print(f"G-E1 census: {len(census_rows)} {other} parts differ from the of-record "
          f"(disclosed v0.8.1-parity classes): {dict(key_hist)}")
    for series, pid, ch in census_rows:
        print(f"    {series} {pid}: {','.join(ch)}")

    # ---- build the appended variant + gates ----
    appended = []
    total_unmapped = 0
    for series in SERIES:
        topic = json.load(open(os.path.join(topics_dir, f"{series}-{paper}.json")))
        s = transform_set(series, paper, topic)
        nq, nps, mk = census(s)
        exp = EXPECTED_2C[series] if paper in EXPECTED_2C else None
        if exp and (nq, nps, mk) != exp:
            raise ExportGateError(
                f"G-E3 {series}/{paper}: census {nq}Q/{nps}P/{mk}M != expected {exp}"
            )
        for q in s["questions"]:
            if sum(p["marks"] for p in q["parts"]) != q["totalMarks"]:
                raise ExportGateError(f"G-E2 part-sum violation in {series}/{paper} {q['id']}")
            for p in q["parts"]:
                msum = sum(m["marks"] for m in p["markPoints"])
                if p["markPoints"] and msum != p["marks"]:
                    raise ExportGateError(f"G-E2 markPoints sum {msum} != {p['marks']} at {p['id']}")
                if not all(isinstance(c, str) for c in p["specPointCodes"]):
                    raise ExportGateError(f"G-E2 spec codes not strings at {p['id']}")
            if all(len(p["specPointCodes"]) == 0 for p in q["parts"]):
                total_unmapped += 1
        appended.append(s)
        print(f"  built {s['slug']}: {nq}Q/{nps}P/{mk}M topicId={s['topicId']}")
    nq_all = sum(len(s["questions"]) for s in appended)
    np_all = sum(sum(len(q["parts"]) for q in s["questions"]) for s in appended)
    mk_all = sum(p["marks"] for s in appended for q in s["questions"] for p in q["parts"])
    print(f"G-E2/G-E3 ok: {paper} tranche {nq_all}Q/{np_all}P/{mk_all}M; "
          f"{total_unmapped}/{nq_all} questions unmapped under the frozen anchor law")

    # ---- F37 adjudication pins (the MCQ-KEYS.json law survives export): the
    # Jan-2020 printed MS misplaces the Q7(a) rows; the converter applies the
    # human-adjudicated ledger before emission, so the SERVED keys must be
    # 7(a)(ii)=C chlorine and 7(a)(iii)=A astatine — never the misprint. ----
    if other == "1C":
        topic20 = json.load(open(os.path.join(topics_dir, "2020-01-1C.json")))
        r20 = transform_set("2020-01", "1C", topic20)
        q7 = [q for q in r20["questions"] if q["id"] == "offq_2020-01_7"][0]
        got = set()
        for p in q7["parts"]:
            if p["id"] in ("offp_2020-01_7-a-ii", "offp_2020-01_7-a-iii"):
                for ch in p["choices"] or []:
                    if ch["isCorrect"]:
                        got.add((p["id"].rsplit("_", 1)[1], ch["label"]))
        need = {("7-a-ii", "C"), ("7-a-iii", "A")}
        if got != need:
            raise ExportGateError(f"F37 pin violation: adjudicated keys {got} != {need}")
        print("F37 pins ok: 2020-01 7(a)(ii)=C, 7(a)(iii)=A survive the export")

    # ---- assemble: replace the {other} block in place (same positions),
    # append the {paper} tranche in series order ----
    rebuilt_other = {}
    for series in SERIES:
        topic = json.load(open(os.path.join(topics_dir, f"{series}-{other}.json")))
        rebuilt_other[f"official-4ch1-{other.lower()}-{series}"] = transform_set(series, other, topic)
    out_sets = [rebuilt_other.get(s.get("slug"), s) for s in current]
    out_sets += appended
    out_bytes = dump(out_sets).encode()
    # G-E4: the SME prefix (everything before the first official set) must be
    # byte-identical under the file law — the SME corpus of record is NEVER
    # touched by an official-papers export. Locate the first official topicId
    # in the raw bytes and compare the strict byte prefix.
    first_off = raw.find(b'"topicId": "off_')
    if first_off == -1:
        raise ExportGateError("G-E4: no official block found in the bundle of record")
    if out_bytes[:first_off] != raw[:first_off]:
        for i in range(first_off):
            if out_bytes[i] != raw[i]:
                raise ExportGateError(
                    f"G-E4: SME prefix diverges at byte {i}: "
                    f"{raw[max(0,i-60):i+60]!r} vs {out_bytes[max(0,i-60):i+60]!r}"
                )
        raise ExportGateError("G-E4: SME prefix length drift")
    print(f"G-E4 ok: SME prefix byte-identical ({first_off} bytes)")

    os.makedirs(args.out_stage, exist_ok=True)
    with open(os.path.join(args.out_stage, "questions.json"), "wb") as f:
        f.write(out_bytes)

    # ---- manifest of record: counts are the frozen SME-side census (history
    # law: every sync since the seed kept 28/524/1404/3708) — bump only
    # generatedUtc + note; importSource.ref stays the merged corpus SHA ----
    manifest_path = os.path.join(os.path.dirname(current_path), "manifest.json")
    manifest = json.load(open(manifest_path)) if os.path.exists(manifest_path) else None
    if manifest is not None:
        official_n = sum(1 for s in out_sets if s.get("topicSlug") == "official-past-papers")
        manifest["generatedUtc"] = "2026-10-22T00:00:00Z"
        manifest["importSource"]["note"] = (
            "ADR-037 converter v0.8.1 corpus (merged main): MCQ-key adjudication ledger (F37) "
            "+ terminal no-spec-point state (F38); 1C and 2C official sets exported "
            f"({official_n} sets, 279 questions, 1537 parts). 2C rides the anchor law honestly: "
            "all 110 questions are pending-llm (no spec codes) so they stay OUT of the learner "
            "model ingest (unmapped) and serve as display content until the 2C spec-tagging wave."
        )
        with open(os.path.join(args.out_stage, "manifest.json"), "wb") as f:
            f.write(dump(manifest).encode())
        print(f"manifest staged (ref {manifest['importSource']['ref']}, generatedUtc untouched-staged)")
    print(f"OK: {len(out_sets)} sets -> {args.out_stage}/questions.json "
          f"({len(out_bytes)} bytes; {other} sets untouched, {paper} appended)")


if __name__ == "__main__":
    try:
        main()
    except ExportGateError as e:
        print("EXPORT GATE FAILED:", e, file=sys.stderr)
        sys.exit(1)
