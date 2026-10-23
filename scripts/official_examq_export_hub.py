#!/usr/bin/env python3
"""Export the ADR-037 official-paper corpus into the syllabai-hub question-set
format (syllabai.sme-exam-questions/1.1 compatible, contract-additive).

Reads  : <repo>/Official-ExamQuestion/igcse-chemistry-19/<series>/4CH1-<paper>/topic.json
         the CURRENT hub content/igcse-chemistry-19/questions.json (28 SME sets)
Writes : <out>/content/igcse-chemistry-19/questions.json  (SME sets + official sets)
Papers : 1C + 2C (16 series each) + 1CR + 2CR (11 R-series each, the F-178
         R-VARIANT tranches). Official slugs: official-4ch1-<paper>-<series>.

Export gates (fail-closed, v4 of this script — the G-E law archived on PR #27,
landed in wave 12; F44 adds the per-paper topicSlug namespace + G-E1b identity
closure; F51 adds the data-cut stamping law G-E5):
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
  G-E5  the data-cut law (F51; runs first, whenever a manifest is staged):
        the run declares --source-cut main@<40-hex> — the resources commit
        whose corpus it consumes; every consumed staging topics file must be
        content-identical to that cut's committed topic.json (modulo the
        generated_utc/generator converter header — the data plane must match
        canonicalized byte-exact), and the declared cut is then STAMPED into
        the staged manifest's importSource.ref. 'importSource.ref stays' is
        retired: the pin once under-claimed at the exporter-of-record commit
        (bf8d56c3) while the run consumed 855cddcf — the wrinkle v2
        PIN-TIGHTEN-1 (fc7a5dc2) closed by hand and filed as this follow-up.
Deterministic; no LLM in the loop.

wave-15 additions (v5, UX doctrine — best experience, non-verbatim presentation
sanctioned; values never invented):
  F-W15-1  stem restore: every upstream stem_md is restored to the question's
           first part (427 stems were silently dropped by every prior exporter
           version — the single largest official-vs-SME rendering gap). Stems
           pass through the eyeballed STEM-RESTORE.json ledger (drop-tail /
           authored rebuild / figure promotion) plus mechanical cleaning
           (control chars, bullet/step reflow). Splice-guard: a stem whose
           text is already folded into part 1 is not duplicated.
  F-W15-2  mark-scheme furniture strip: trailing "Question/Answer Notes Marks"
           MS-table header lines are stripped from solutionMd/markPoints.
  F-W15-3  RETIRED before ship (wave-15 review): the hub renders single
           newlines as soft breaks (react-markdown, no remark-breaks), so
           joining them was render-identical byte noise — and it disturbed
           the wave-14 verbatim-transcription pins (e.g. 2019-06 3(d)(ii)).
           Line breaks stay as extracted; only junk lines are removed.
  F-W15-4  honest stub note: the "pending scan / queued for human verification"
           process jargon is replaced with learner-facing copy (the wave-13
           CROP-REVIEW verdicts are settled; the queue language was stale).

Contract notes (src/lib/contracts.ts in syllabai-hub):
- QuestionPart: id/order/questionType/marks/commandWord/specPointIds/
  specPointCodes/problemMd/solutionMd/choices?/sourcePaper? — this exporter
  ADDS markPoints[] + assets[] (added to the zod contract in the same PR).
- Unknown keys are stripped by zod; every required field is emitted exactly.
- Shared figure references (assets[].shared + ref_part) resolve to the owning
  part's/stem asset's PNG (same rawUrl) — the hub pattern embeds images as
  markdown, so shared figures inline the same URL.

wave-20 additions (v6, stem-figure tranche):
  F-W20-1  stem figures inline: STEM-RESTORE.json entries may carry
           stemFigures (converter-rendered crop assets, flagged stem_figure)
           and stemFigureRef (an already-cropped asset id). Assets flagged
           stem_figure on the question's FIRST part render INSIDE the stem
           block — right after the stem prose, before the part text — instead
           of the end-of-problemMd figure slot; assets targeted at a later
           part (the 2019-06 2C bond-energy tables for 5(a)(i)) render in
           that part's normal figure slot.
  F-W20-2  flattened label-soup cuts: entry.dropSpan [from, to) removes the
           mid-stem flattened figure-label run (both anchors verbatim,
           fail-closed); entry.dropTail removes the tail from a verbatim
           anchor (the soup the crop now serves visually). These apply to
           keep-verdict stems before mechanical cleaning.
"""
import json, glob, os, re, subprocess, sys, hashlib
from pathlib import Path

# repo-relative (F15 portability): works from any checkout of syllabai-resources
REPO_ROOT = str(Path(__file__).resolve().parents[1])
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


STEM_LEDGER_PATH = os.path.join(REPO_ROOT, "Official-ExamQuestion", "STEM-RESTORE.json")

# F-W15-2: a solution line made only of MS-table header furniture (the answer
# grid's column headers leak into the extracted cell text). Tokens are matched
# after stripping glue digits ("3Answer" → "Answer").
FURNITURE_WORDS = {"question", "number", "answer", "notes", "marks",
                   "additional", "guidance", "total", "for"}


def _is_furniture_line(line):
    toks = [t for t in re.split(r"[^A-Za-z]+", line) if t]
    return bool(toks) and all(t.lower().lstrip("0123456789") in FURNITURE_WORDS for t in toks)


def strip_furniture(sol):
    """F-W15-2: drop trailing furniture lines (up to 4) + a trailing
    'Total for Question N = M marks' line, from the end only."""
    if not sol:
        return sol
    lines = sol.rstrip().splitlines()
    n = 0
    while lines and n < 4:
        last = lines[-1].strip()
        if _is_furniture_line(last) or re.fullmatch(r"Total\s+\d+", last):
            lines.pop()
            n += 1
            continue
        if re.fullmatch(r"Total\s+for\s+Question\s+\d+\s*=\s*\d+\s*marks", last):
            lines.pop()
            n += 1
            continue
        break
    return "\n".join(lines).rstrip() if n else sol


def _bulletize(stem):
    """F-W15-1 cleaning: flattened method bullet runs (• / ●) become markdown
    bullets; 'Step N' runs become one line per step; control chars are
    stripped. Only fires on ≥2 occurrences so prose never splits."""
    s = re.sub(r"[\x00-\x08\x0b-\x1f]", "", stem).replace("\t", " ")
    for b in ("\u2022", "\u25cf"):
        if s.count(f" {b} ") >= 1:
            parts = [x.strip() for x in s.split(b) if x.strip()]
            if len(parts) >= 3:
                s = parts[0] + "\n" + "\n".join(f"- {p}" for p in parts[1:])
                break
    if len(re.findall(r"\bStep\s+\d+\b", s)) >= 2:
        s = re.sub(r"(?<!^)(?<!\n)\s*(\bStep\s+\d+\b)", r"\n\1", s)
    return s


SOLUTION_ENRICH_PATH = os.path.join(REPO_ROOT, "Official-ExamQuestion", "SOLUTION-ENRICH.json")


def load_enrichment_ledger():
    """F-W20-3: the authored worked-answer ledger (wave-20 Part C). Optional:
    an absent ledger means every part serves its MS-derived solution."""
    if not os.path.exists(SOLUTION_ENRICH_PATH):
        return {}
    doc = json.load(open(SOLUTION_ENRICH_PATH))
    return doc.get("entries", {})


def load_stem_ledger():
    if not os.path.exists(STEM_LEDGER_PATH):
        raise ExportGateError(
            f"F-W15-1: stem ledger missing at {STEM_LEDGER_PATH} — the wave-15 "
            "stem restore runs with the eyeballed ledger of record (STEM-RESTORE.json)")
    return json.load(open(STEM_LEDGER_PATH))


def restore_stem(q, series, paper, ledger, by_part_num):
    """F-W15-1: cleaned stem markdown for a question, or None. Authored ledger
    verdicts win; everything else passes mechanical cleaning. Splice-guard:
    stems already folded into part 1 by the converter are not duplicated.
    wave-20 (F-W20-2): entry.dropSpan / entry.dropTail cut the flattened
    figure-label soup BEFORE verdict handling; both anchors verbatim."""
    stem = (q.get("stem_md") or "").strip()
    if not stem:
        return None
    qnum = str(q["question_number"])
    entry = ledger.get("verdicts", {}).get(f"{series}/4CH1-{paper}:Q{qnum}")
    first_md = (q["parts"][0].get("problem_md") or "") if q["parts"] else ""
    norm = lambda s: re.sub(r"\s+", " ", s).strip()
    if norm(stem)[:60] and norm(stem)[:60] in norm(first_md):
        return None  # splice-guard: converter already folded this stem into part 1
    if entry:
        span = entry.get("dropSpan")
        if span:
            a_from, a_to = span
            i, j = stem.find(a_from), stem.find(a_to)
            if i < 0 or j < 0 or j <= i:
                raise ExportGateError(
                    f"F-W20-2: dropSpan anchors not found/ordered in stem of "
                    f"{series}/4CH1-{paper} Q{qnum}: {a_from[:50]!r} -> {a_to[:50]!r}")
            stem = (stem[:i].rstrip() + " " + stem[j:].lstrip()).strip()
        tail = entry.get("dropTail")
        if tail:
            if tail not in stem:
                raise ExportGateError(
                    f"F-W20-2: dropTail anchor not found in stem of "
                    f"{series}/4CH1-{paper} Q{qnum}: {tail[:60]!r}")
            stem = stem[:stem.index(tail)].rstrip()
            stem = re.sub(r"[\s]*[-\u2013\u2014.:;]?$", "", stem)
    if entry and entry.get("verdict") == "replace":
        anchor = entry.get("dropTailFrom")
        if anchor:
            if anchor not in stem:
                raise ExportGateError(
                    f"F-W15-1: dropTailFrom anchor not found in stem of "
                    f"{series}/4CH1-{paper} Q{qnum}: {anchor[:60]!r}")
        md = entry["stemMd"]
        fig_part = entry.get("inlineFigureFrom")
        if fig_part:
            a = by_part_num.get(fig_part)
            crop = next((x for x in (a or {}).get("assets", [])
                         if x.get("kind") == "crop" and resolve_asset_path(x, {})), None) if a else None
            if not crop:
                raise ExportGateError(
                    f"F-W15-1: inlineFigureFrom {fig_part} on "
                    f"{series}/4CH1-{paper} Q{qnum} has no resolvable crop asset")
            url = raw_url(series, paper, resolve_asset_path(crop, {}))
            cap = f"{crop.get('mention', 'figure')} — official paper figure (qp.pdf p.{crop.get('page')})"
            md = md.replace("{{FIG:" + fig_part + "}}", f"![{cap}]({url})")
        if "{{FIG:" in md:
            raise ExportGateError(
                f"F-W15-1: unresolved FIG placeholder in authored stem of "
                f"{series}/4CH1-{paper} Q{qnum}")
        return md.strip()
    if entry and entry.get("verdict") == "drop-tail":
        tail = entry.get("tail")
        if tail and tail not in stem:
            raise ExportGateError(
                f"F-W15-1: drop-tail anchor not found in stem of "
                f"{series}/4CH1-{paper} Q{qnum}: {tail[:60]!r}")
        if tail:
            stem = stem[:stem.index(tail)].rstrip()
            stem = re.sub(r"[\s]*[-–—.:;]?$", "", stem)
        return _bulletize(stem).strip()
    # unledgered (or keep-verdict) stems: mechanical cleaning only
    return _bulletize(stem).strip() or None


def export_series(series, paper, topic=None, stem_ledger=None, enrich=None):
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
        # F-W15-1: the printed stem is restored to the question's first part
        by_part_num = {p["part_number"]: p for p in q["parts"]}
        stem_md = restore_stem(q, series, paper, stem_ledger or {}, by_part_num)
        # F-W20-1: stem-level figures render inside the stem block
        stem_figs_md = []
        s_entry = (stem_ledger or {}).get("verdicts", {}).get(f"{series}/4CH1-{paper}:Q{qnum}") or {}
        ref = (s_entry.get("stemFigureRef") or {}).get("asset")
        if ref:
            ra = by_id.get(ref)
            if ra is None:
                # F28 collapse: the owner record may exist only as a share-ref
                # whose ref_part names the stem asset (its path IS the owner's
                # PNG) — resolve through the share-ref's path.
                ra = next((a for a in by_id.values() if a.get("ref_part") == ref), None)
            rpath = resolve_asset_path(ra, by_id) if ra else None
            if not ra or ra.get("kind") != "crop" or not rpath:
                raise ExportGateError(
                    f"F-W20-1: stemFigureRef {ref} on {series}/4CH1-{paper} Q{qnum} "
                    f"does not resolve to a real crop asset")
            url = raw_url(series, paper, rpath)
            cap = f"{ra.get('mention', 'figure')} — official paper figure (qp.pdf p.{ra.get('page')})"
            stem_figs_md.append(f"![{cap}]({url})")
        first_assets = (q["parts"][0].get("assets") or []) if q["parts"] else []
        for a in first_assets:
            if not a.get("stem_figure") or a.get("kind") != "crop":
                continue
            rel = resolve_asset_path(a, by_id)
            if not rel:
                raise ExportGateError(
                    f"F-W20-1: stem figure {a['id']} on {series}/4CH1-{paper} Q{qnum} "
                    f"has no resolvable path")
            url = raw_url(series, paper, rel)
            cap = f"{a.get('mention', 'figure')} — official paper figure (qp.pdf p.{a.get('page')})"
            stem_figs_md.append(f"![{cap}]({url})")
        parts = []
        for p in q["parts"]:
            marks = int(p["marks"]) if p.get("marks") is not None else 0
            assets_out, figures_md = [], []
            for a in p.get("assets") or []:
                # F-W20-1: stem figures on the FIRST part render in the stem
                # block (stem_figs_md above) — their crop record still rides
                # assets[] for the metadata, but the end-of-part figure slot
                # must not duplicate the inline stem image.
                is_stem_fig = a.get("stem_figure") and len(parts) == 0
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
                    if not is_stem_fig:
                        figures_md.append(f"![{cap}]({entry['rawUrl']})")
                elif a.get("kind") == "crop-required":
                    # F-W15-4: learner-facing copy — the wave-13 CROP-REVIEW
                    # verdicts settled these as honest blank-scaffold stubs;
                    # the old 'pending scan / queued for verification' line
                    # described a queue that no longer exists.
                    figures_md.append(
                        "> *No printed figure accompanies this part — in the paper "
                        "you would draw the diagram (or label the apparatus) in the "
                        "answer space provided.*")
                assets_out.append(entry)
            problem_md = (p.get("problem_md") or "").strip()
            if len(parts) == 0 and stem_md:
                # F-W20-1: stem prose, then its figures, then the part text
                problem_md = stem_md + "\n\n" + (("\n\n".join(stem_figs_md) + "\n\n") if stem_figs_md else "") + problem_md
            if figures_md:
                problem_md += "\n\n" + "\n\n".join(figures_md)
            sol = p.get("solution_md") or None
            if sol:
                # F-W15-2: trailing MS-grid furniture lines off (visible junk).
                # F-W15-3 retired: no reflow — single newlines render as soft
                # breaks, and the verbatim cell structure is wave-14-pinned.
                sol = strip_furniture(sol) or None
            # F-W20-3: authored worked answers replace the terse MS cell as the
            # learner-facing solutionMd; the MS text itself stays verbatim in
            # mark_points (marking is never authored). Ledger-only: a part
            # without a reviewed entry keeps its MS-derived solution.
            e_entry = (enrich or {}).get(f"{series}-{paper}:{part_slug(p['part_number'])}")
            if e_entry and e_entry.get("review") == "authored-r0" and e_entry.get("solutionMd"):
                sol = e_entry["solutionMd"]
            mp = [{"id": x["id"], "marks": x["marks"],
                   "textMd": strip_furniture(x["text_md"])}
                  for x in (p.get("mark_points") or [])]
            choices = None
            if p.get("question_type") == "multiple_choice" and p.get("choices"):
                ch = p["choices"]
                if isinstance(ch, str):
                    ch = json.loads(ch)
                choices = [{"label": c["label"], "isCorrect": bool(c.get("is_correct")),
                            "textMd": c.get("text_md", "")} for c in ch]
            parts.append({
                # wave-15 id-collision fix: the paper code is part of the
                # identity — offp_<series>_<part> collided across 1C/2C/1CR/2CR
                # of the same series (631 duplicated ids), cross-wiring saved
                # MCQ answers and typed-answer drafts between papers.
                "id": f"offp_{series}_{paper.lower()}_{part_slug(p['part_number'])}",
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
            "id": f"offq_{series}_{paper.lower()}_{part_slug(qnum)}",
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
    # 1CR tranche (converter v0.12.0 corpus; MULTI-SERIES-REPORT of record):
    # (questions, parts, marks) — every set carries its printed 110/110.
    "1CR": {
        "2019-06": (10, 55, 110),
        "2020-01": (11, 59, 110),
        "2020-11": (10, 63, 110),
        "2021-01": (10, 58, 110),
        "2022-01": (11, 59, 110),
        "2022-06": (11, 57, 110),
        "2023-01": (10, 57, 110),
        "2023-06": (11, 59, 110),
        "2024-06": (12, 57, 110),
        "2025-06": (11, 55, 110),
        "2026-06": (11, 57, 110),
    },
    # 2CR tranche (converter v0.13.0 corpus; MULTI-SERIES-REPORT of record):
    # (questions, parts, marks) — every set carries its printed 70/70.
    "2CR": {
        "2019-06": (7, 40, 70),
        "2020-01": (7, 38, 70),
        "2020-11": (7, 36, 70),
        "2021-01": (8, 45, 70),
        "2022-01": (7, 35, 70),
        "2022-06": (7, 40, 70),
        "2023-01": (8, 40, 70),
        "2023-06": (7, 38, 70),
        "2024-06": (7, 38, 70),
        "2025-06": (7, 38, 70),
        "2026-06": (7, 35, 70),
    },
}

ALL_SERIES = ["2019-06", "2020-01", "2020-11", "2021-01", "2021-06", "2021-11",
              "2022-01", "2022-06", "2023-01", "2023-06", "2023-11", "2024-06",
              "2024-11", "2025-06", "2025-11", "2026-06"]
# F-178 R-VARIANT tranche 1 (footer-verified 22/22, tracker PR #32): the 1CR
# paper exists for exactly these 11 of the 16 series (2021-06/2021-11/2023-11/
# 2024-11/2025-11 never printed a 1CR; 2020-06 never ran at all — COVID).
R1CR_SERIES = ["2019-06", "2020-01", "2020-11", "2021-01", "2022-01", "2022-06",
               "2023-01", "2023-06", "2024-06", "2025-06", "2026-06"]
PAPER_SERIES = {"1C": ALL_SERIES, "2C": ALL_SERIES,
                "1CR": R1CR_SERIES, "2CR": R1CR_SERIES}   # same 11 series print 2CR
PAPERS = tuple(PAPER_SERIES)   # both F-178 R-variant tranches now convert


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


# F51 (exporter v4): the data-cut law. The hub manifest's importSource.ref is
# the pin the v2 per-course pin law serves — PIN-TIGHTEN-1 (v2 fc7a5dc2) proved
# the wrinkle class: the ref once named the exporter-of-record commit (F44's
# landing bf8d56c3) while the run actually consumed a later cut (855cddcf).
# The exporter now stamps the DECLARED data cut and proves the consumed staging
# copies ARE that cut, fail-closed, no disclosure path (identity is a law — the
# G-E1b precedent). Content-identity modulo the converter header:
# generated_utc/generator are the converter's own identity (its version law),
# not the data cut's; the data plane must match canonicalized byte-exact.
SOURCE_CUT_RE = re.compile(r"^main@[0-9a-f]{40}$")
CUT_VOLATILE_HEADER = ("generated_utc", "generator")


def parse_source_cut(value):
    if not SOURCE_CUT_RE.match(value or ""):
        raise ValueError(
            f"--source-cut must be main@<40-hex commit sha> (got {value!r}) — "
            f"the declared data cut is the resources commit whose corpus the run consumes")
    return value


def _cut_topic_bytes(source_cut, rel_path):
    # the pin of record is 'main@<40-hex>' (manifest form); git wants the bare
    # rev — 'main@<hex>' is not valid rev syntax (the '@' would start a reflog
    # expression), so translate before handing it to git.
    rev = source_cut.split("@", 1)[1] if "@" in source_cut else source_cut
    proc = subprocess.run(
        ["git", "-C", REPO_ROOT, "show", f"{rev}:{rel_path}"],
        capture_output=True)
    if proc.returncode != 0:
        raise ExportGateError(
            f"G-E5: cannot read {rel_path} at the declared data cut {source_cut} "
            f"(git show failed: {proc.stderr.decode(errors='replace').strip()[:200]})")
    return proc.stdout


def _topic_data_plane(raw_bytes):
    d = json.loads(raw_bytes)
    return {k: v for k, v in d.items() if k not in CUT_VOLATILE_HEADER}


def verify_source_cut(topics_dir, source_cut):
    """G-E5: every consumed staging topics file must BE the declared data cut.
    Content-identity vs <cut>:Official-ExamQuestion/.../topic.json modulo the
    converter header. Fail-closed, no disclosure path — a runner whose staging
    copies are not the declared cut must re-stage or declare the cut the copies
    actually are; it can no longer stamp a pin the data cannot prove."""
    checked = 0
    for paper in PAPERS:
        for series in PAPER_SERIES[paper]:
            staged_path = os.path.join(topics_dir, f"{series}-{paper}.json")
            if not os.path.exists(staged_path):
                raise ExportGateError(
                    f"G-E5: staging topics file missing for {series}/{paper}: "
                    f"{staged_path} (stage the declared cut's corpus topics first)")
            staged = _topic_data_plane(open(staged_path, "rb").read())
            rel = f"Official-ExamQuestion/igcse-chemistry-19/{series}/4CH1-{paper}/topic.json"
            at_cut = _topic_data_plane(_cut_topic_bytes(source_cut, rel))
            if json.dumps(staged, sort_keys=True) != json.dumps(at_cut, sort_keys=True):
                raise ExportGateError(
                    f"G-E5: staging topics for {series}/{paper} are NOT the declared "
                    f"data cut {source_cut} (content drift beyond the converter header; "
                    f"re-stage from {source_cut} or declare the cut the copies are)")
            checked += 1
    print(f"G-E5 ok: {checked}/{checked} staging topics content-identical to the "
          f"declared data cut {source_cut} (modulo the converter header)")


def run_gates(out_sets, raw_bundle_bytes, expected_deltas_path, topics_src, allow_new_official=False, stem_ledger=None, enrich=None):
    """G-E1..G-E4 against the bundle of record. topics_src(series, paper) -> topic dict.
    allow_new_official: a legitimate append wave may add official sets absent from
    the bundle of record — their full part ids are disclosed in the 'new' census
    class (the exporter refuses silently-dropped new sets either way)."""
    by_slug = {t.get("slug"): t for t in json.loads(raw_bundle_bytes)}
    # ---- G-E3: census constants (cheap, run first) ----
    n_slices = 0
    for paper in PAPERS:
        for series in PAPER_SERIES[paper]:
            s = next(t for t in out_sets if t["slug"] == f"official-4ch1-{paper.lower()}-{series}")
            c = census(s)
            exp = EXPECTED_CENSUS[paper][series]
            if c != exp:
                raise ExportGateError(f"G-E3 {series}/{paper}: census {c} != expected {exp}")
            n_slices += 1
    print(f"G-E3 ok: {n_slices} slices match the MULTI-SERIES constants of record "
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
    n_common = 0
    for paper in PAPERS:
        for series in PAPER_SERIES[paper]:
            slug = f"official-4ch1-{paper.lower()}-{series}"
            rebuilt = export_series(series, paper, topics_src(series, paper), stem_ledger, enrich)
            of_record = by_slug.get(slug)
            if of_record is None:
                if not allow_new_official:
                    raise ExportGateError(
                        f"G-E1: bundle of record lacks {slug} (an append wave must run "
                        f"with --allow-new-official and disclose its census)")
                census_rows["new"][slug] = sorted(p["id"] for q in rebuilt["questions"] for p in q["parts"])
                continue
            n_common += 1
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
    # wave-19 rename-wave shape: a disclosure carrying idRenames explains an
    # id-identity wave — gone ids must BE the map's keys, new ids its values,
    # and the content census (keyed by the NEW ids, id key excluded) must equal
    # the disclosure's 'changed'. One disclosure of record, both tools read it
    # (the CI hands the same file to the exporter and the verify harness).
    rename_ok = False
    if n_delta and expected_deltas_path:
        expected_probe = json.load(open(expected_deltas_path))
        if "idRenames" in expected_probe:
            rename_n = content_n = 0
            for paper in PAPERS:
                for series in PAPER_SERIES[paper]:
                    slug = f"official-4ch1-{paper.lower()}-{series}"
                    rebuilt = export_series(series, paper, topics_src(series, paper), stem_ledger, enrich)
                    of_record = by_slug[slug]
                    smap = expected_probe["idRenames"].get(slug)
                    if not smap:
                        raise ExportGateError(f"G-E1: rename disclosure lacks {slug}")
                    qmap, pmap = smap.get("questions", {}), smap.get("parts", {})
                    for oq, rq in zip(of_record["questions"], rebuilt["questions"]):
                        if len(oq["parts"]) != len(rq["parts"]):
                            raise ExportGateError(f"G-E1: {slug} {oq['id']}: part count drift under a rename disclosure")
                        if qmap.get(oq["id"]) != rq["id"]:
                            raise ExportGateError(
                                f"G-E1: {slug}: question rename mismatch {oq['id']} -> {qmap.get(oq['id'])!r} "
                                f"(regenerated {rq['id']})")
                        for oprt, rprt in zip(oq["parts"], rq["parts"]):
                            if pmap.get(oprt["id"]) != rprt["id"]:
                                raise ExportGateError(
                                    f"G-E1: {slug}: part rename mismatch {oprt['id']} -> {pmap.get(oprt['id'])!r} "
                                    f"(regenerated {rprt['id']})")
                            rename_n += 1
                            ck = {k for k in (set(oprt) | set(rprt)) - {"id"}
                                  if json.dumps(oprt.get(k), sort_keys=True) != json.dumps(rprt.get(k), sort_keys=True)}
                            if ck:
                                content_n += 1
                                if rprt["id"] not in expected_probe.get("changed", {}).get(slug, []):
                                    raise ExportGateError(
                                        f"G-E1: content delta {slug} {rprt['id']} ({sorted(ck)}) "
                                        f"missing from the rename disclosure's 'changed' census")
            disc_changed_n = sum(len(v) for v in expected_probe.get("changed", {}).values())
            if content_n != disc_changed_n:
                raise ExportGateError(
                    f"G-E1: rename-disclosure content census {disc_changed_n} != fresh {content_n} "
                    f"(regenerate the disclosure only after eyeballing every class)")
            print(f"G-E1 ok: rename disclosure verified — {rename_n} ids renamed, "
                  f"{content_n} content deltas match the disclosed 'changed' census exactly")
            rename_ok = True
            n_delta = 0
    if n_delta == 0:
        if not rename_ok:
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
    print(f"G-E1b ok: set-level identity fields byte-equal on all {n_common} common official sets")
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
    ap.add_argument("--allow-new-official", action="store_true",
                    help="append wave: official sets absent from the bundle of record are "
                         "disclosed in the 'new' census class instead of refusing")
    ap.add_argument("--manifest", default=None,
                    help="manifest.json beside the bundle of record; staged with bumped note")
    ap.add_argument("--source-cut", default=None,
                    help="the data cut this run consumes, main@<40-hex> (F51: REQUIRED "
                         "with --manifest — stamped into importSource.ref and proven by "
                         "G-E5 against the staging copies)")
    args = ap.parse_args()
    topics_dir = args.topics_dir or os.path.join(os.getcwd(), "topics")
    source_cut = None
    if args.manifest and not args.source_cut:
        ap.error("--source-cut main@<40-hex> is REQUIRED with --manifest (F51: the "
                 "manifest's importSource.ref must name the data cut the run consumes "
                 "— 'importSource.ref stays' is retired; see v2 PIN-TIGHTEN-1)")
    if args.source_cut and not args.manifest:
        ap.error("--source-cut is only meaningful with --manifest (it stamps importSource.ref)")
    if args.source_cut:
        try:
            source_cut = parse_source_cut(args.source_cut)
        except ValueError as exc:
            ap.error(str(exc))
        verify_source_cut(topics_dir, source_cut)

    def topics_src(series, paper):
        return json.load(open(os.path.join(topics_dir, f"{series}-{paper}.json")))

    raw = open(args.current_questions, "rb").read()
    hub = json.loads(raw)
    kept = [t for t in hub if not t["slug"].startswith(OFFICIAL_SLUG_PREFIX)]
    stem_ledger = load_stem_ledger()
    enrich = load_enrichment_ledger()
    official = [export_series(s, paper, topics_src(s, paper), stem_ledger, enrich)
                for paper in PAPERS for s in PAPER_SERIES[paper]]
    out = kept + official

    run_gates(out, raw, args.expected_deltas, topics_src, args.allow_new_official,
              stem_ledger, enrich)

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
        # F51: the pin law — the staged manifest names the data cut the run
        # consumed (G-E5-proven above), never a stale or tool-identity ref.
        manifest["importSource"]["ref"] = source_cut
        manifest["importSource"]["note"] = (
            "ADR-037 converter v0.14.1 corpus (wave-22, F62): solution enrichment tranche 2 - "
            "the corpus is COMPLETE: 1,332 authored SME-style worked answers added "
            "(SOLUTION-ENRICH.json 1,275 -> 2,607; every solution-bearing part of the 54 "
            "official sets now carries an authored, verifier-clean worked answer; the 217 "
            "repair-flagged tranche-1 drafts were re-authored from evidence). The F60/F62 "
            "value-fidelity review pass is the committed harness "
            "scripts/official_examq_enrich_verify.py (F-W22-1..5: mark-point furniture/artifact "
            "strips, case-corrected symbol/label coverage routes, decimal-safe numeric "
            "tokeniser, M-label evidence reads, uppercase-only marker jargon; full 2,607-entry "
            "ledger re-verified 0 problems), C71 pins min_entries 2607. Serving delta: "
            "solutionMd on 1,341 parts (1,332 tranche-2 + 9 tranche-1 repairs) + the F62 "
            "MCQ re-key of 2020-01 2CR 1(b)(i) to C "
            "(MCQ-KEYS.json paper-scoped adjudication, converter v0.14.1); MS cells and mark "
            "points stay verbatim - marking is never authored. Wave-15 UX doctrine governs: "
            "best learner experience, values never invented. "
            f"{official_n} official sets (16x1C + 16x2C + R-variants), {n_q} questions, {n_p} parts, all "
            "spec-tagged.")
        os.makedirs(args.out_stage, exist_ok=True)
        with open(os.path.join(args.out_stage, "manifest.json"), "wb") as f:
            f.write(json.dumps(manifest, indent=1, ensure_ascii=False).encode())
        print(f"manifest staged (importSource.ref stamped to the declared data cut "
              f"{source_cut} — G-E5-proven; note text is the per-wave hardcode of "
              f"record: bump it in the same reviewed PR as the wave)")
    print(f"written: {dest}/questions.json")


if __name__ == "__main__":
    main()
