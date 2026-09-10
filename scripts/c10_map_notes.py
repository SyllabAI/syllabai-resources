#!/usr/bin/env python3
"""
T-C10 (Phase 2) — revision-note -> spec-point mapping applier.

Applies the AI mapping decisions (scripts/c10_decisions/S*.json) to the 112
SME notes' YAML front matter as the `spec_map:` block, with HARD gates
before anything is written:

  G1  coverage   — every walked note has a decision record; 112 == 112
  G2  registry   — every mapped code exists in the 182-point registry
                   (graph/specification_points.yaml); no foreign curriculum
                   codes can therefore exist, but codes are also regex-gated
                   to the 4CH1-* namespace
  G3  evidence   — every AI_SUGGESTED mapping's evidence quote appears
                   VERBATIM in the note file after normalisation (markdown
                   emphasis / HTML sub-sup tags / links / whitespace /
                   curly-quote variants). Anti-hallucination gate.
  G4  vocabulary — confidence in {high, medium, low}; no duplicate codes
                   within a note; >= 1 mapping per note
  G5  integrity  — note BODY is byte-identical after injection (only the
                   front matter gains spec_map); front matter still parses
                   as YAML; existing FM keys untouched
  G6  idempotent — a spec_map block already present is replaced cleanly
  G7  promotion  — optional per-mapping `validation` blocks in the decisions
                   JSON are validated (status exactly HUMAN_VALIDATED,
                   non-empty validated_by, validated_date as YYYY-MM-DD) and
                   carried into the front matter. Promotions live in the
                   decisions files, NEVER as hand-edits on note front matter
                   (the applier regenerates front matter from decisions and
                   would silently revert hand edits). Without a validation
                   block a mapping stays validation_status: SUGGESTED.

Cross-subsection mappings (a note mapping to a point outside its PROVIDER
slug-anchored subsection) are ALLOWED but recorded and reported for PR
review attention — they are flags, not failures.

The deterministic subsection anchor itself is recomputed from the source
URL slug (PROVIDER tier, validation_status SUGGESTED — the git PR is the
human gate, per KNOWLEDGE_GRAPH_CONTEXT.md §8A.7 / §8A.4).

Outputs:
  - 112 note files with spec_map in front matter
  - graph/reports/PHASE2_MAPPING_COVERAGE.md (coverage + PR review guide)
  - graph/reports/PHASE2_SPOT_CHECK_SHEET.md (20 sampled mappings)

The spot-check sheet is an ISSUED review artifact: once it carries an
operator review record it is NOT regenerated on re-runs (the operator's
verdicts are keyed to its numbered entries). Force regeneration only with
`--regen-spot-check` (this discards the review record - a fresh sheet must
then be re-issued and re-reviewed).

Usage: python3 scripts/c10_map_notes.py [--dry-run] [--regen-spot-check]
"""
from __future__ import annotations

import argparse
import hashlib
import json
import random
import re
import sys
import unicodedata
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from c10_worksheets import (  # noqa: E402
    NOTES_ROOT, REPO, GRAPH, SECTION_LETTERS,
    front_matter_split, parse_slug, walk_notes,
)

DECISION_DIR = HERE / "c10_decisions"
REPORTS = GRAPH / "reports"
MODEL_VERSION = "GLM (Super Z agent, z.ai)"
MAPPED_DATE = "2026-09-11"
CONFIDENCE_VOCAB = {"high", "medium", "low"}
RE_4CH1_CODE = re.compile(r"^4CH1-S\d(\.\d{1,2}C?)?$|^4CH1-\d\.\d{1,2}C?$")

# ----------------------------------------------------------------- helpers --
_TRANS = {ord("‘"): "'", ord("’"): "'", ord("“"): '"', ord("”"): '"',
          ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def norm(s: str) -> str:
    """Normalisation shared by the evidence gate: apply to BOTH the note text
    and the evidence quote, then substring-match. Never used to rewrite files."""
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")                                # markdown escapes
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)          # links -> text
    s = re.sub(r"<[^>]+>", "", s)                           # HTML tags
    s = re.sub(r"[*_`#>]+", "", s)                          # emphasis/heading/quote
    s = s.translate(_TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def load_registry():
    data = yaml.safe_load((GRAPH / "specification_points.yaml").read_text(encoding="utf-8"))
    topics = yaml.safe_load((GRAPH / "topics.yaml").read_text(encoding="utf-8"))
    code2sub = {p["code"]: p["subsection"] for p in data["specification_points"]}
    sub_titles = {st["code"]: st.get("title") or st.get("title_md")
                  for st in topics.get("subtopics", [])}
    return code2sub, sub_titles


def load_decisions():
    decisions = {}
    for f in sorted(DECISION_DIR.glob("S*.json")):
        decisions.update(json.loads(f.read_text(encoding="utf-8")))
    return decisions


def fm_bounds(text: str):
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        return None
    for i in range(1, len(lines)):
        if lines[i].strip() == "---":
            return 0, i
    return None


def strip_existing_spec_map(fm_lines):
    """Remove an existing top-level spec_map block (idempotency)."""
    out, in_block = [], False
    for ln in fm_lines:
        if not in_block and re.match(r"^spec_map:\s*$", ln):
            in_block = True
            continue
        if in_block:
            # block continues while indented or blank; stops at next key
            if re.match(r"^[A-Za-z_][\w-]*:", ln) or ln.strip() == "---":
                in_block = False
            else:
                continue
        out.append(ln)
    return out


RE_ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")


def valid_validation_block(val):
    """G7: a decisions-side promotion block must be exactly this shape."""
    return (isinstance(val, dict)
            and val.get("validation_status") == "HUMAN_VALIDATED"
            and str(val.get("validated_by", "")).strip() != ""
            and RE_ISO_DATE.match(str(val.get("validated_date", ""))))


def build_spec_map(sub_code, group_slug, mappings):
    sps = []
    for m in mappings:
        prov = {
            "tier": "AI_SUGGESTED",
            "confidence": m["confidence"],
            "model_version": MODEL_VERSION,
            "evidence": m["evidence"],
            "rationale": m["rationale"],
            "validation_status": "SUGGESTED",
        }
        val = m.get("validation")
        if val is not None:
            # G7 gates the shape; here we just carry it through.
            if valid_validation_block(val):
                prov["validation_status"] = "HUMAN_VALIDATED"
                prov["validated_by"] = str(val["validated_by"])
                prov["validated_date"] = str(val["validated_date"])
        sps.append({
            "code": m["code"],
            "provenance": prov,
        })
    block = {
        "spec_map": {
            "curriculum_code": "4CH1-2017",
            "phase": 2,
            "subsection": sub_code,
            "subsection_provenance": {
                "tier": "PROVIDER",
                "signal": "source-url-slug",
                "slug": group_slug,
                "validation_status": "SUGGESTED",
            },
            "spec_points": sps,
            "mapped_date": MAPPED_DATE,
            "mapper": "scripts/c10_map_notes.py (decisions: scripts/c10_decisions/)",
        }
    }
    text = yaml.safe_dump(block, allow_unicode=True, sort_keys=False,
                          default_flow_style=False, width=100)
    return text.rstrip("\n") + "\n"


# -------------------------------------------------------------------- main --
def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--regen-spot-check", action="store_true",
                    help="force regeneration of PHASE2_SPOT_CHECK_SHEET.md "
                         "(discards any operator review record on it)")
    args = ap.parse_args()

    code2sub, sub_titles = load_registry()
    decisions = load_decisions()
    notes = walk_notes()

    failures, flags, stats = [], [], {"mappings": 0, "notes": 0,
                                      "by_conf": {"high": 0, "medium": 0, "low": 0},
                                      "cross_sub": 0}

    # ---- G1 coverage
    walked = {n["path"] for n in notes}
    decided = set(decisions.keys())
    if walked != decided:
        for p in sorted(walked - decided):
            failures.append(f"G1 note without decisions: {p}")
        for p in sorted(decided - walked):
            failures.append(f"G1 decision for unknown note: {p}")

    # ---- per-note gates + injection
    changed = 0
    for n in notes:
        rel = n["path"]
        dec = decisions.get(rel)
        if not dec:
            continue
        path = REPO / rel
        text = path.read_text(encoding="utf-8")
        bounds = fm_bounds(text)
        if not bounds:
            failures.append(f"G5 no front matter: {rel}")
            continue
        start, close = bounds
        body = "".join(text.splitlines(keepends=True)[close + 1:])

        mappings = dec.get("mappings", [])
        # ---- G4 vocabulary / duplicates / >=1
        if not mappings:
            failures.append(f"G4 zero mappings: {rel}")
        codes = [m["code"] for m in mappings]
        if len(codes) != len(set(codes)):
            failures.append(f"G4 duplicate codes: {rel}")
        for m in mappings:
            if m.get("confidence") not in CONFIDENCE_VOCAB:
                failures.append(f"G4 bad confidence {m.get('confidence')!r}: {rel}")
            if not m.get("evidence"):
                failures.append(f"G4 empty evidence: {rel} {m.get('code')}")
            if not m.get("rationale"):
                failures.append(f"G4 empty rationale: {rel} {m.get('code')}")
            # ---- G7 promotion block shape (carried by build_spec_map)
            if m.get("validation") is not None \
                    and not valid_validation_block(m["validation"]):
                failures.append(
                    f"G7 invalid validation block: {m.get('code')} :: {rel} "
                    "(need validation_status HUMAN_VALIDATED + validated_by "
                    "+ validated_date YYYY-MM-DD; anything else must be "
                    "omitted, leaving the mapping SUGGESTED)")
        # ---- G2 registry
        for c in codes:
            if c not in code2sub:
                failures.append(f"G2 code not in 182-registry: {c} ({rel})")
            elif not RE_4CH1_CODE.match(c):
                failures.append(f"G2 code fails namespace regex: {c} ({rel})")

        # ---- deterministic PROVIDER anchor
        parsed = parse_slug(n["url"]) if n["url"] else None
        if not parsed:
            failures.append(f"G2 unparseable source URL: {rel}")
            continue
        sec, grp, group_slug, note_slug, _ = parsed
        sub_code = f"4CH1-S{sec}-{SECTION_LETTERS[grp - 1]}"

        # ---- cross-subsection flags
        for c in codes:
            if c in code2sub and code2sub[c] != sub_code:
                stats["cross_sub"] += 1
                flags.append((rel, c, sub_code, code2sub[c]))

        # ---- G3 evidence gate
        norm_text = norm(text)
        for m in mappings:
            if norm(m["evidence"]) not in norm_text:
                failures.append(
                    f"G3 evidence quote NOT found in note: {m['code']} :: "
                    f"{m['evidence'][:70]!r} :: {rel}")

        # ---- injection
        fm_lines = text.splitlines(keepends=True)[1:close]
        fm_lines = strip_existing_spec_map(fm_lines)
        block_text = build_spec_map(sub_code, group_slug, mappings)
        new_fm = "".join(fm_lines) + block_text
        new_text = "---\n" + new_fm + "---\n" + body
        # ---- G5 integrity: body identical, FM parses, keys preserved
        if fm_bounds(new_text) is None:
            failures.append(f"G5 broken FM after injection: {rel}")
            continue
        try:
            fm_dict = yaml.safe_load(new_fm)
        except yaml.YAMLError as e:
            failures.append(f"G5 FM yaml error: {rel}: {e}")
            continue
        if "spec_map" not in fm_dict:
            failures.append(f"G5 spec_map missing after injection: {rel}")
            continue
        old_keys = set(yaml.safe_load("".join(fm_lines)) or {}) - {"spec_map"}
        new_keys = set(fm_dict) - {"spec_map"}
        if old_keys != new_keys:
            failures.append(f"G5 FM keys changed: {rel}")
        if hash(body) != hash("".join(new_text.splitlines(keepends=True)[fm_bounds(new_text)[1] + 1:])):
            failures.append(f"G5 body changed: {rel}")

        if not args.dry_run:
            path.write_text(new_text, encoding="utf-8")
            changed += 1
        stats["notes"] += 1
        stats["mappings"] += len(mappings)
        for m in mappings:
            stats["by_conf"][m["confidence"]] += 1

    if failures:
        print(f"T-C10 APPLY FAILED — {len(failures)} gate failure(s):")
        for f in failures[:60]:
            print("  -", f)
        if len(failures) > 60:
            print(f"  ... and {len(failures) - 60} more")
        sys.exit(1)

    promoted = sum(1 for d in decisions.values() for m in d["mappings"]
                   if m.get("validation", {}).get("validation_status")
                   == "HUMAN_VALIDATED")
    print(f"{'DRY-RUN ' if args.dry_run else ''}ALL GATES GREEN")
    print(f"notes mapped: {stats['notes']}  mappings: {stats['mappings']} "
          f"(high {stats['by_conf']['high']} / medium {stats['by_conf']['medium']} "
          f"/ low {stats['by_conf']['low']}; promoted HUMAN_VALIDATED: "
          f"{promoted})")
    print(f"cross-subsection mappings (PR-review flags): {stats['cross_sub']}")
    for rel, c, note_sub, pt_sub in flags:
        print(f"  FLAG {c}: note anchored {note_sub} but point in {pt_sub} :: {Path(rel).name}")

    if not args.dry_run:
        write_reports(stats, flags, decisions, code2sub, sub_titles, notes,
                      regen_spot_check=args.regen_spot_check)
        print("reports written: graph/reports/PHASE2_MAPPING_COVERAGE.md; "
              "spot-check sheet written or preserved (see notice above)")


def write_reports(stats, flags, decisions, code2sub, sub_titles, notes,
                  regen_spot_check=False):
    REPORTS.mkdir(parents=True, exist_ok=True)
    # coverage per point
    point_notes = {}
    note_subs = {}
    for n in notes:
        dec = decisions[n["path"]]
        parsed = parse_slug(n["url"])
        sec, grp, group_slug, note_slug, _ = parsed
        sub = f"4CH1-S{sec}-{SECTION_LETTERS[grp - 1]}"
        note_subs[n["path"]] = (sub, group_slug)
        for m in dec["mappings"]:
            point_notes.setdefault(m["code"], []).append(
                (m["confidence"], Path(n["path"]).stem))
    covered = len(point_notes)
    promoted = sum(1 for d in decisions.values() for m in d["mappings"]
                   if m.get("validation", {}).get("validation_status")
                   == "HUMAN_VALIDATED")

    lines = ["# Phase 2 (T-C10) — Revision-Note to Spec-Point Mapping Coverage",
             "",
             f"Generated {MAPPED_DATE} by `scripts/c10_map_notes.py` from "
             "`scripts/c10_decisions/S*.json` (AI mapping pass, GLM Super Z agent).",
             "",
             "## 1. Method",
             "",
             "1. **PROVIDER anchor (deterministic, zero-LLM):** each note's Save My Exams "
             "source URL embeds a spec-aligned topic-group slug "
             "(`…/1-5-chemical-formulae-equations-calculations/…`) which maps 1:1 onto the "
             "28 4CH1 subsections (verified programmatically: 28/28 groups, ordering exact). "
             "This subsection anchor is a source fact stored at PROVIDER tier.",
             "2. **AI_SUGGESTED point-level mapping:** an LLM pass (GLM, Super Z agent) read "
             "each note's headings/excerpt/body against the full 182-point registry and "
             "proposed point-level mappings, each carrying an evidence quote, a confidence "
             "(high/medium/low), a rationale, and the model version.",
             "3. **Hard gates (all green):** every mapped code is in the 182-point registry "
             "(hence no foreign/4CH0 codes possible); every evidence quote was verified to "
             "appear verbatim in the note (anti-hallucination); every note has ≥1 mapping; "
             "the note BODY was left byte-identical (front matter only).",
             "4. **Human validation:** nothing here is authoritative. Every mapping carries "
             "`validation_status: SUGGESTED`. The git PR review of the front-matter diff IS "
             "the HUMAN_VALIDATED gate (operator workflow, §8A.4 four tiers).",
             "",
             "## 2. Totals",
             "",
             f"- Notes mapped: **{stats['notes']} / 112**",
             f"- Total mappings: **{stats['mappings']}** "
             f"(high {stats['by_conf']['high']} · medium {stats['by_conf']['medium']} · "
             f"low {stats['by_conf']['low']})",
             f"- Spec points with ≥1 direct note mapping: **{covered} / 182**",
             f"- Cross-subsection mappings (flagged for PR attention): {stats['cross_sub']}",
             f"- Promoted to HUMAN_VALIDATED so far: **{promoted} / {stats['mappings']}** "
             "(PR review in progress; see `PHASE2_PR_REVIEW_GUIDE.md`)",
             "",
             "## 3. Zero-coverage queue (points with no direct note mapping)",
             "",
             "The Phase 3/4 enrichment queue handed to the Student Book / question-mapping "
             "phases. If this list is empty, the 112 SME notes cover every 4CH1 spec point "
             "at point level.",
             ""]
    zero = [c for c in sorted(code2sub) if c not in point_notes]
    if zero:
        for c in zero:
            lines.append(f"- {c} ({sub_titles.get(code2sub[c], '')})")
    else:
        lines.append("- **EMPTY — all 182 points have ≥1 AI_SUGGESTED note mapping.** "
                     "Phase 3/4 enrichment should still review *quality* (e.g. "
                     "poly(tetrafluoroethene) is not among the addition-polymer note's "
                     "worked examples — see the note's rationale).")
    lines += ["", "## 4. Per-subsection mapping table", "",
              "| Subsection | SME group | Notes | Mappings | Points covered |",
              "|---|---|---|---|---|"]
    sub_stats = {}
    for n in notes:
        sub, group = note_subs[n["path"]]
        d = sub_stats.setdefault(sub, {"group": group, "notes": 0, "maps": 0, "pts": set()})
        d["notes"] += 1
        d["maps"] += len(decisions[n["path"]]["mappings"])
        d["pts"].update(m["code"] for m in decisions[n["path"]]["mappings"])
    for sub in sorted(sub_stats, key=lambda s: (int(s.split("-")[1][1]), s.split("-")[2])):
        d = sub_stats[sub]
        n_pts = len(d["pts"])
        lines.append(f"| {sub} {sub_titles.get(sub, '')} | `{d['group']}` | "
                     f"{d['notes']} | {d['maps']} | {n_pts} |")
    # per-point detail
    lines += ["", "## 5. Per-point coverage detail", ""]
    for c in sorted(point_notes, key=lambda c: (int(c.split("-")[1].split(".")[0]),
                                                float(c.split("-")[1].rstrip("C")))):
        entries = ", ".join(f"{stem} ({conf})" for conf, stem in sorted(point_notes[c]))
        lines.append(f"- **{c}**: {len(point_notes[c])} note(s) — {entries}")
    # cross-subsection flags
    lines += ["", "## 6. PR review guide", "",
              "1. Review the front-matter diff of this commit — each note's `spec_map:` "
              "block is a small, self-contained review unit (code + confidence + evidence "
              "quote + rationale). The full work order in the operator's stated "
              "priority order is `graph/reports/PHASE2_PR_REVIEW_GUIDE.md` "
              "(remapped 4.15 first, then the low/medium set, then the semantic "
              "completeness and diagram-verification scans).",
              "2. Start with **medium/low** confidence mappings and the cross-subsection "
              "flags below — they are the ones where the mapping judgment is least "
              "mechanical.",
              "3. Spot-check status (2026-09-11): the 20-sample sheet "
              "(`graph/reports/PHASE2_SPOT_CHECK_SHEET.md`) was operator-reviewed — "
              "19 confirmed (1 of them after machine visual verification of the "
              "metallic-lattice diagram), 1 rejected and remapped (4CH1-4.15, see the "
              "sheet's review record).",
              "4. Approve/adjust via the PR: a confirmed mapping is promoted by adding "
              "a `validation` block (HUMAN_VALIDATED + validated_by + validated_date) "
              "to its entry in `scripts/c10_decisions/S*.json` and re-running the "
              "gated applier — `scripts/c10_promote.py` batches this. The note front "
              "matter is then regenerated carrying `validation_status: "
              "HUMAN_VALIDATED`. NEVER hand-edit the front matter for promotion: the "
              "applier regenerates it from decisions and would silently revert the "
              "edit on the next rework re-run.",
              "5. **Evidence-existence is not semantic validity.** The automated G3 gate "
              "proves a mapping's evidence quote exists verbatim in the note; it cannot "
              "prove the quote covers the spec point's semantics. The 4.15 case is the "
              "canonical example: a true quote (fuel sulfur impurities) that never "
              "established the impurity -> combustion -> sulfur-dioxide causal chain the "
              "point demands. Read every mapping as *does this note teach what the point "
              "asks*, not as *does this sentence exist*.",
              ""]
    if flags:
        lines.append("### Cross-subsection mappings (flagged)")
        lines.append("")
        for rel, c, note_sub, pt_sub in flags:
            lines.append(f"- `{c}` — note anchored in {note_sub} (slug), point sits in "
                         f"{pt_sub}: {Path(rel).name}")
    else:
        lines.append("No cross-subsection mappings in this batch.")
    (REPORTS / "PHASE2_MAPPING_COVERAGE.md").write_text("\n".join(lines) + "\n",
                                                        encoding="utf-8")

    # spot-check sheet: 20 random mappings. An issued sheet carrying an
    # operator review record is an immutable review artifact - never
    # silently regenerated (verdicts are keyed to its numbered entries).
    sheet = REPORTS / "PHASE2_SPOT_CHECK_SHEET.md"
    if sheet.exists() and not regen_spot_check:
        existing = sheet.read_text(encoding="utf-8")
        if "operator-review-locked" in existing:
            print("NOTICE: PHASE2_SPOT_CHECK_SHEET.md carries an operator "
                  "review record - preserved (use --regen-spot-check to "
                  "discard and re-issue)")
            return
    rng = random.Random(20260911)
    all_maps = []
    for n in notes:
        for m in decisions[n["path"]]["mappings"]:
            all_maps.append((n, m))
    sample = rng.sample(all_maps, 20)
    sl = ["# Phase 2 (T-C10) — Spot-Check Sheet (20 sampled mappings)",
          "",
          f"Generated {MAPPED_DATE}. For the operator PR review: verify each sampled "
          "mapping by opening the note (path below) and checking (a) the evidence quote "
          "exists in the note, (b) the note substantively teaches the mapped spec point.",
          ""]
    for i, (n, m) in enumerate(sample, 1):
        sl.append(f"## {i}. {m['code']} ← {Path(n['path']).stem}")
        sl.append(f"- note: `{n['path']}`")
        sl.append(f"- confidence: **{m['confidence']}**")
        sl.append(f"- spec statement: {sub_titles.get(code2sub[m['code']], '')} "
                  f"(see graph/specification_points.yaml {m['code']})")
        sl.append(f"- evidence quote: “{m['evidence']}”")
        sl.append(f"- AI rationale: {m['rationale']}")
        sl.append(f"- verdict: ☐ CONFIRMED ☐ REJECT (edit front matter) ☐ UNSURE")
        sl.append("")
    sheet.write_text("\n".join(sl) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()
