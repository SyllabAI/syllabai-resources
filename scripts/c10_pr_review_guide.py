#!/usr/bin/env python3
"""
T-C10 (Phase 2) — PR front-matter review guide generator.

Emits `graph/reports/PHASE2_PR_REVIEW_GUIDE.md`: the work order for the
remaining operator gate (the git PR review that promotes mappings from
`validation_status: SUGGESTED` to HUMAN_VALIDATED), operationalising the
operator's review priorities (2026-09-11):

  1. 4CH1-4.15 — verify the remapped mapping/evidence
  2. the 1 low-confidence mapping
  3. the 34 medium-confidence mappings (unusual/cross-subsection first)
  4. the flagged 4CH1-1.17 cross-subsection mapping
  5. confirm no mapping relies on a concept taught only in another note
  6. confirm diagram-dependent mappings are not accepted solely from
     textual evidence

Everything is computed deterministically from the decisions JSON, the
182-point registry, and the note files (image-reference resolution). The
priority-5/6 scans are regex heuristics that ASSIST the reviewer — they are
not gates; semantic judgment stays human (the 4.15 lesson).

Issue 2 (2026-09-11, same day): the operator's SME-architecture
clarification made the mapping CONTRACT explicit — Save My Exams Revision
Notes are instructional containers (a page covers at least one subtopic and
often groups several spec points; one point's content can equally be split
across pages), so mappings are **contributory many-to-many relationships**,
not per-point sole-coverage claims. §0.0 states the contract; §5's review
question, §6b's missing-figure rules and §7's closure criterion were
reworded accordingly.

Usage: python3 scripts/c10_pr_review_guide.py
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from c10_worksheets import NOTES_ROOT, REPO, GRAPH  # noqa: E402

REPORTS = GRAPH / "reports"
DATE = "2026-09-11"

IMG_RE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")

# non-content images (site branding / author photos / avatars) — not eyeball
# targets for semantic review
NON_CONTENT_RE = re.compile(
    r"(lucy|stewart|avatar|logo|banner|favicon|BW-300)", re.I)

# note's PROVIDER-anchored subsection, derived from its corpus path
# ("Chemistry IGCSE Revision Notes/{sec}. .../{letter}. .../note.md");
# the worksheets hard-gated 28/28 path groups == spec subsections and the
# validator pins front-matter subsection == slug-derived subsection
NOTE_SUB_RE = re.compile(
    r"^Chemistry IGCSE Revision Notes/(\d+)\.[^/]+/([a-z])\. ")


def note_subsection(rel):
    m = NOTE_SUB_RE.match(rel)
    return f"4CH1-S{m.group(1)}-{m.group(2)}" if m else None

# priority-5: explicit cross-note deferral language in a rationale
P5_RE = re.compile(
    r"(?:\bnote\b\s+(?:carries|carried|covers|is the)\b"
    r"|\bnotes?\b\s+[^.]{0,15}\b(?:carries|covers)\b"
    r"|\blives in\b|\bare in the\b|\balso in the\b"
    r"|\bcarried separately\b|\bcontinues in\b"
    r"|\bdedicated\b[^.]{0,30}\bnote\b)",
    re.I,
)
# priority-6: rationale leans on a visual (not plain textual tables)
P6_RE = re.compile(r"\b(diagram|graph|pie chart|displayed formulae?)\b", re.I)


def load_all():
    decisions = {}
    for f in sorted((HERE / "c10_decisions").glob("S*.json")):
        decisions.update(__import__("json").loads(f.read_text(encoding="utf-8")))
    reg = yaml.safe_load((GRAPH / "specification_points.yaml").read_text(encoding="utf-8"))
    wording = {p["code"]: p["official_wording"] for p in reg["specification_points"]}
    code2sub = {p["code"]: p["subsection"] for p in reg["specification_points"]}
    return decisions, wording, code2sub


def note_images(rel):
    """Return (resolved, missing) image refs of a note."""
    text = (REPO / rel).read_text(encoding="utf-8")
    resolved, missing = [], []
    for alt, ref in IMG_RE.findall(text):
        if ref.startswith("http"):
            continue
        local = re.sub(r"^\.\./\.\./", "", ref).split("#")[0]
        target = NOTES_ROOT / local
        (resolved if target.exists() else missing).append((alt, ref, local))
    return resolved, missing


def maps_of(decisions):
    out = []
    for note, d in decisions.items():
        for m in d["mappings"]:
            out.append((note, m))
    return out


def mapping_contract_stats(decisions):
    """Measured many-to-many shape of the mapping corpus."""
    from collections import defaultdict
    pts = defaultdict(int)
    for _n, m in maps_of(decisions):
        pts[m["code"]] += 1
    n_notes = len(decisions)
    n_pts = len(pts)
    multi_notes = sum(1 for d in decisions.values() if len(d["mappings"]) > 1)
    multi_pts = sum(1 for c in pts if pts[c] > 1)
    return n_notes, n_pts, multi_notes, multi_pts


def esc(s, n=110):
    s = s.replace("|", "\\|").replace("\n", " ")
    return (s[: n - 1] + "…") if len(s) > n else s


def block(note, m, wording):
    """Full review block for one mapping."""
    lines = [
        f"- code: **{m['code']}** (confidence **{m['confidence']}**)",
        f"- note: `{note}`",
        f"- spec: “{esc(wording.get(m['code'], ''), 160)}”",
        f"- evidence: “{esc(m['evidence'], 160)}”",
        f"- rationale: {esc(m['rationale'], 220)}",
    ]
    val = m.get("validation")
    if isinstance(val, dict) and val.get("validation_status") == "HUMAN_VALIDATED":
        lines.append(f"- status: **HUMAN_VALIDATED** (promoted by "
                     f"{val.get('validated_by')} on {val.get('validated_date')}) "
                     "— confirmed; nothing left to review here")
    _, missing = note_images(note)
    if P6_RE.search(m["rationale"]) and missing:
        lines.append("- ⚠ missing figure in this note: "
                     + ", ".join(f"`{r}`" for _, r, _ in missing))
    return "\n".join(lines)


def main() -> int:
    decisions, wording, code2sub = load_all()
    all_maps = maps_of(decisions)

    low = [(n, m) for n, m in all_maps if m["confidence"] == "low"]
    med = [(n, m) for n, m in all_maps if m["confidence"] == "medium"]
    p5 = [(n, m) for n, m in all_maps if P5_RE.search(m["rationale"])]
    p6a = [(n, m) for n, m in all_maps if P6_RE.search(m["rationale"])]

    # notes with unresolved image refs -> every mapping on them is P6b
    p6b_notes = {}
    for note in decisions:
        _, missing = note_images(note)
        if missing:
            p6b_notes[note] = missing

    def code_key(item):
        n, m = item
        c = m["code"]
        sec = int(c.split("-")[1].split(".")[0])
        return (sec, float(c.split("-")[1].rstrip("C")))

    # priority-3 ordering: P5-flagged first, then 1.17, then registry order
    med_p5 = [x for x in med if any(x[1]["code"] == mm["code"] and x[0] == nn
                                    for nn, mm in p5)]
    med_rest = [x for x in med if x not in med_p5]
    med_sorted = (med_p5 + [x for x in med_rest if x[1]["code"] == "4CH1-1.17"]
                  + sorted((x for x in med_rest if x[1]["code"] != "4CH1-1.17"),
                           key=code_key))

    L = []
    A = L.append
    A("# Phase 2 (T-C10) — PR Front-Matter Review Guide")
    A("")
    A(f"Generated {DATE} by `scripts/c10_pr_review_guide.py` (deterministic: "
      "decisions JSON + 182-point registry + note image-resolution scan).")
    A("")
    A("**Status context:** the operator spot-check is CLOSED (19/20 confirmed, "
      "1 rejected and remapped — verdicts and the review record live on "
      "`PHASE2_SPOT_CHECK_SHEET.md`, which is locked against regeneration). "
      "T-C10 is **implementation-complete but not yet HUMAN_VALIDATED**: this "
      "guide is the work order for the remaining gate, the git PR front-matter "
      "review, in the operator's stated priority order (2026-09-11).")
    A("")

    # ---------------- mechanics ----------------
    n_notes, n_pts, multi_notes, multi_pts = mapping_contract_stats(decisions)
    A("## 0. Review mechanics and promotion protocol")
    A("")
    A("0. **The mapping contract (what a `spec_map` mapping asserts).** The "
      "source corpus is Save My Exams Revision Notes: a note page covers at "
      "least one subtopic and often groups several specification points, and "
      "one point's content can equally be split across pages. The T-C10 graph "
      "is therefore **many-to-many by design** (measured: "
      f"{multi_notes}/{n_notes} notes carry 2+ spec points; "
      f"{multi_pts}/{n_pts} spec points are covered by 2–3 notes). A mapping "
      "asserts: *this note provides substantive instructional coverage "
      "contributing to that specification point* — NOT that this note "
      "independently teaches the entire point. The aggregate set of mappings "
      "for a point establishes the point's coverage. Reject a mapping only "
      "when: (a) the note does not substantively support the mapped point "
      "(e.g. it supplies only a premise where the point demands a causal "
      "relationship); (b) the cited evidence does not support the claimed "
      "relationship; (c) the mapping is outside the 4CH1 scope; or (d) the "
      "rationale materially misrepresents the note. Contributory is not a "
      "free pass: where the spec wording IS an explanatory relationship "
      "(4.15: *explain how combustion of impurities results in SO₂*), the "
      "mapped note must itself carry the relationship — premises and "
      "consequences may live in sibling notes, the explanation may not.")
    A("1. **Unit of review** = one `spec_map.spec_points[]` entry in a note's "
      "front matter: `code` + `provenance.confidence` + `provenance.evidence` "
      "+ `provenance.rationale`. Open the note, read the block, open the spec "
      "wording (below or `graph/specification_points.yaml`).")
    A("2. **The three standing lessons**: (a) *evidence-existence is not "
      "semantic validity* — the quote existing in the note does not show the "
      "note teaches what the point demands (the 4.15 case, operator "
      "spot-check); (b) *diagram-dependent mappings need eyes on the "
      "diagram*, not just the text (the 1.52C case, operator spot-check); "
      "(c) *contributory ≠ free pass* — distributed coverage is legitimate, "
      "but the substantive content of the mapped point must be in THIS note, "
      "not merely its premise or consequence elsewhere (the mapping contract, "
      "§0.0; operator's SME-architecture clarification, 2026-09-11).")
    A("3. **CONFIRMED → promotion (decisions-side, never note hand-edits):** "
      "add a `validation` block to that mapping's entry in "
      "`scripts/c10_decisions/S*.json`:")
    A("   ```")
    A('   "validation": {"validation_status": "HUMAN_VALIDATED",')
    A('                     "validated_by": "operator",')
    A('                     "validated_date": "2026-09-11"}')
    A("   ```")
    A("   then re-run `python3 scripts/c10_map_notes.py` — or use the batch "
      "helper `scripts/c10_promote.py`, which edits the decisions and "
      "re-runs the applier in one step. The front matter is regenerated "
      "carrying the promotion; note bodies stay byte-identical. "
      "Hand-edits on note front matter are the WRONG route: the applier "
      "regenerates front matter from the decisions and would silently "
      "revert them on the next rework re-run. The `tier` stays "
      "`AI_SUGGESTED` forever (origin is immutable); only the review state "
      "changes. The validator accepts exactly `SUGGESTED` (clean — no "
      "stray promotion fields) or `HUMAN_VALIDATED` (with `validated_by` "
      "+ `validated_date`); anything else fails, and a promoted mapping "
      "with the tier flipped is still caught (premature authority).")
    A("4. **REJECT → rework:** edit `scripts/c10_decisions/S*.json` (remove or "
      "re-map with in-note evidence) and re-run `python3 "
      "scripts/c10_map_notes.py` — all hard gates re-validate, the locked "
      "spot-check sheet is preserved. Precedent: `scripts/c10_rework_415.py`.")
    A("")

    # ---------------- P1 ----------------
    A("## 1. Priority 1 — the remapped 4CH1-4.15")
    A("")
    A("The one mapping changed by the spot-check rework. Verify the note now "
      "teaches the point's causal relationship in-note.")
    A("")
    for note, m in all_maps:
        if m["code"] == "4CH1-4.15":
            A(block(note, m, wording))
    A("")
    A("Review question: read the **whole note**, not just the evidence "
      "sentence. The note's “From sulfur dioxide” subsection carries the 4.15 "
      "relationship in-note (**combustion of fossil fuels → sulfur dioxide**); "
      "the impurity premise (“All these fuels contain … small quantities of "
      "sulfur”) is NOT in this note — it lives in the sibling combustion note "
      "(same subsection 4CH1-S4-b). Under the mapping contract (§0.0) that is "
      "a legitimate distributed coverage: the point's explanation is here, "
      "its premise is one page away. Confirm if (a) the causal relationship "
      "is genuinely taught in this note, and (b) the rationale honestly names "
      "where the premise lives. The rejected combustion-note mapping failed "
      "exactly the mirror-image test: it had the premise without the "
      "relationship — under §0.0 that is a rejection, not a partial pass.")
    A("")

    # ---------------- P2 ----------------
    A("## 2. Priority 2 — the 1 low-confidence mapping")
    A("")
    for note, m in low:
        A(block(note, m, wording))
        is_p5 = any(nn == note and mm["code"] == m["code"] for nn, mm in p5)
        if is_p5:
            A("- ⚠ also a priority-5 flag: the rationale's “the dedicated "
              "terminology note covers 1.4 fully” wording misframes the "
              "mapping as a deferral. Under the mapping contract (§0.0) the "
              "question is whether THIS note's own teaching — it defines "
              "“the liquid is called the solvent” and uses solute / "
              "saturated solution operationally in its solubility-curve "
              "discussion — is substantive contributory coverage of 1.4 "
              "(the Solutions note carries the four-term definitions table "
              "as a separate 1.4 mapping, also in S1-a). If yes, confirm and "
              "rework the rationale to contributory wording; reject only if "
              "the note merely used the vocabulary without teaching any of "
              "the four terms.")
    A("")

    # ---------------- P3 ----------------
    A(f"## 3. Priority 3 — the {len(med_sorted)} medium-confidence mappings")
    A("")
    A("Ordered: priority-5-flagged first, then the cross-subsection flag "
      "(1.17), then registry order. `P5` = cross-note deferral flag "
      "(§5); `P6` = diagram-dependent (§6); `XSUB` = cross-subsection.")
    A("")
    A("| # | code | note | evidence | flags |")
    A("|---|---|---|---|---|")
    for i, (note, m) in enumerate(med_sorted, 1):
        flags = []
        if any(nn == note and mm["code"] == m["code"] for nn, mm in p5):
            flags.append("P5")
        if any(nn == note and mm["code"] == m["code"] for nn, mm in p6a):
            flags.append("P6")
        if code2sub.get(m["code"]) != note_subsection(note):
            flags.append("XSUB")
        A(f"| {i} | {m['code']} | {esc(Path(note).stem, 45)} | "
          f"{esc(m['evidence'], 60)} | {', '.join(flags) or '—'} |")
    A("")

    # ---------------- P4 ----------------
    A("## 4. Priority 4 — the 4CH1-1.17 cross-subsection flag")
    A("")
    A("1.17 is mapped on TWO notes. Only one of them is the actual "
      "cross-subsection case (note anchored to a different subsection than "
      "the point's registry subsection); the other is the ordinary "
      "in-subsection mapping and is listed for contrast.")
    A("")
    for note, m in all_maps:
        if m["code"] == "4CH1-1.17":
            A(block(note, m, wording))
            nsub, psub = note_subsection(note), code2sub.get("4CH1-1.17")
            if nsub == psub:
                A(f"- subsections: note anchored **{nsub}** = point's registry "
                  f"subsection **{psub}** — in-subsection, the mechanical "
                  "default (not the flag).")
            else:
                A(f"- subsections: note anchored **{nsub}** but point sits in "
                  f"**{psub}** — **the cross-subsection flag**: the note is "
                  "anchored by its source-URL slug to its own subsection, "
                  "yet opens by teaching this point's content before moving "
                  "on; legitimate but the least mechanical mapping in the "
                  "batch.")
            A("")

    # ---------------- P5 ----------------
    A("## 5. Priority 5 — cross-note deferral candidates (semantic completeness)")
    A("")
    A("Computed scan: rationales containing explicit deferral language "
      "(“the dedicated … note carries …”, “lives in”, “are in the”, "
      "“carried separately”, …). For each, the review question (mapping "
      "contract, §0.0): **does this note provide substantive instructional "
      "coverage of the mapped point, with evidence that accurately "
      "represents that coverage?** Coverage may be distributed across "
      "multiple notes; another note providing additional or complementary "
      "coverage is not itself a reason to reject this mapping. Reject only "
      "when the note does not substantively support the mapped point, the "
      "evidence does not support the claimed relationship, the mapping is "
      "outside the 4CH1 scope, or the rationale materially misrepresents the "
      "note. The 4.15 lesson still applies inside this test: a mapping that "
      "supplies only the premise of a point whose spec wording is an "
      "explanatory relationship is NOT substantive coverage of that "
      "relationship. A deliberate split across two notes (definition here, "
      "calculation there; table here, bands there) is usually legitimate "
      "content architecture — the reviewer decides, mapping by mapping.")
    A("")
    for note, m in sorted(p5, key=code_key):
        conf_mark = " **(low — priority 2)**" if m["confidence"] == "low" else ""
        remap_mark = " **(the 4.15 remap — priority 1; 'carried separately' " \
                     "refers to 4.16's acid-rain content, not to 4.15)**" \
            if m["code"] == "4CH1-4.15" else ""
        A(f"- **{m['code']}** [{m['confidence']}] — "
          f"`{Path(note).stem}`{conf_mark}{remap_mark}")
        A(f"  - rationale: {esc(m['rationale'], 200)}")
    A("")

    # ---------------- P6 ----------------
    A("## 6. Priority 6 — diagram-dependent mappings (visual verification queue)")
    A("")
    A("Computed scan: mappings whose rationale leans on a diagram / graph / "
      "pie chart / displayed formulae. The textual evidence quote alone is "
      "**not sufficient** for these — eyeball the referenced image in the "
      "note. Image paths below resolve in the corpus.")
    A("")
    A("### 6a. Visual eyeball queue (images resolve)")
    A("")
    vlm_done = {"4CH1-1.52C": "machine-verified 2026-09-11 (VLM: 2-D regular "
               "ion array + labelled delocalised electrons) — operator may "
               "re-eyeball"}
    for note, m in sorted(p6a, key=code_key):
        if note in p6b_notes:
            continue  # handled in 6b
        resolved, _ = note_images(note)
        imgs = [r for _, r, _ in resolved if not NON_CONTENT_RE.search(r)]
        imgs_txt = ", ".join(f"`{Path(r).name}`" for r in imgs[:6])
        if len(imgs) > 6:
            imgs_txt += f", … (+{len(imgs) - 6} more)"
        imgs_txt = imgs_txt or "—"
        mark = vlm_done.get(m["code"], "")
        A(f"- **{m['code']}** [{m['confidence']}] — `{Path(note).stem}` "
          f"{('— ' + mark) if mark else ''}")
        A(f"  - rationale: {esc(m['rationale'], 150)}")
        A(f"  - images: {imgs_txt}")
    A("")
    A("### 6b. Missing figures — mapping leans on a visual that is NOT in the corpus")
    A("")
    A("Three notes carry `figure-missing` markers (download failed during "
      "clipping; tracked since the corpus-repair pass). Classify each "
      "mapping deterministically:")
    A("")
    A("- **PASS** — the surviving text alone provides substantive coverage "
      "of the point; the figure was supplementary reinforcement. Promote on "
      "the textual evidence.")
    A("- **HOLD** — the figure is necessary to verify the claimed "
      "instructional content (e.g. the point requires interpreting a specific "
      "visual, or the mapping's rationale leans on the diagram). The mapping "
      "is NOT validated until the image is recovered; leave it "
      "`SUGGESTED` and list it in the image-recovery queue.")
    A("- **REJECT/REWORK** — the surviving text does not actually support "
      "the point and the missing figure was carrying the mapping: remove or "
      "re-map.")
    A("")
    for note, missing in p6b_notes.items():
        A(f"- **`{Path(note).stem}`** — missing: "
          f"{', '.join(f'`{r}`' for _, r, _ in missing)}")
        for m in decisions[note]["mappings"]:
            leans = "**leans on visuals**" if P6_RE.search(m["rationale"]) \
                else "textual evidence"
            A(f"  - {m['code']} [{m['confidence']}] ({leans}) — "
              f"evidence: “{esc(m['evidence'], 90)}”")
    A("")

    # ---------------- pass criteria ----------------
    A("## 7. Pass criteria and what follows")
    A("")
    A("The PR review passes when every mapping designated for human review "
      "in this guide has a **terminal decision** — **confirmed** (promoted "
      "to HUMAN_VALIDATED via the §0.3 protocol; `scripts/c10_promote.py` "
      "batches it), **rejected-and-reworked** (decisions edit + gated re-run, "
      "§0.4), or **held** (§6b image-recovery queue) — and the gate suite is "
      "green afterwards (`graph_check.py` 9/9, `c10_negative_test.py` 10 "
      "classes + positive control, applier ALL GREEN, coverage contract "
      "intact: 182/182 points, zero-coverage queue EMPTY).")
    A("")
    A("**What T-C10 closure means — stated honestly.** Mappings OUTSIDE this "
      "guide's review set were validated deterministically (applier hard "
      "gates + `graph_check.py`) and sampled by the operator's 20-mapping "
      "spot-check (19/20 confirmed, 1 reworked). They remain `tier: "
      "AI_SUGGESTED` / `validation_status: SUGGESTED` and MUST NOT be "
      "represented as human-validated. T-C10 therefore closes as: **"
      "risk-prioritized human validation of the mapping corpus complete — "
      "reviewed set HUMAN_VALIDATED, remainder AI_SUGGESTED in force.** It is "
      "a mapping-validity gate, not a claim that all 211 mappings were "
      "individually human-inspected; specification-point-level coverage "
      "adequacy across the aggregate is a separate corpus audit, deliberately "
      "deferred to the coverage checks ahead of T-C11 (Phase 3 "
      "concept/prerequisite/misconception graph — see `TODO.md`).")
    A("")

    out = REPORTS / "PHASE2_PR_REVIEW_GUIDE.md"
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    cross = [(n, m["code"]) for n, m in all_maps
             if code2sub.get(m["code"]) != note_subsection(n)]
    print(f"written: {out}")
    print(f"  P1: 4.15 remap | P2: {len(low)} low | P3: {len(med_sorted)} medium "
          f"(P5-flagged first: {len(med_p5)}) | P5: {len(p5)} candidates | "
          f"P6a: {len([1 for n, m in p6a if n not in p6b_notes])} | "
          f"P6b: {len(p6b_notes)} notes with missing figures | "
          f"XSUB (generic scan): {len(cross)} -> "
          + ", ".join(f"{c} @{Path(n).stem[:30]}" for n, c in cross))
    return 0


if __name__ == "__main__":
    sys.exit(main())
