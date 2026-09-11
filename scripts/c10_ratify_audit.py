#!/usr/bin/env python3
"""
T-C10 — ratification reconciliation audit (read-only; round-5 dual-batch
edition).

Executes the operator-advisor's procedural condition before the staged
batches are run, extended after the round-5 exhaustive review to cover BOTH
staged promotion batches:

    "Perform one final machine-verifiable reconciliation of the
     ratification targets against the review sheet, proving exact
     note->SpecificationPoint identity and proving no target promotes an
     unreviewed mapping." (round 3)

    "I would not run the 61-item ratification command yet … remove/rework
     these two mappings, regenerate the gates, and then we can do the
     final exact-target reconciliation before ratification." (round 4)

    Operator instruction (2026-09-11): "Ratify the 59 and promote 150" —
    §11's option (b) resolved as one controlled promotion of the 150
    round-5 CONFIRMs, staged as sheet §13 by scripts/c10_round5_batch.py.

Method — independent sides, all read from the repo as it stands:

  A. REVIEW RECORD   scripts/c10_pr_review_verdicts.py (round-3 verdict
                     data) + scripts/c10_round4_rejects.py (round-4
                     supersession record): assemble the 59 reviewed
                     survivors, resolve against the decisions store.
  A5. ROUND-5 RECORD graph/reports/C10_ROUND5_REVIEW.json — the 150
                     round-5 CONFIRM pairs with exact note keys.
  B. ROUND-4 RECORD  scripts/c10_round4_rejects.py — the 2 REJECT entries.
  C. RATIFY COMMANDS the ```bash blocks in PHASE2_PR_REVIEW_SHEET.md §12
                     (59-spec) and §13 (150-spec) — parsed with shlex and
                     resolved with the PRODUCTION resolver
                     (c10_promote.load_all + c10_promote.resolve_targets).
  D. DECISIONS STORE scripts/c10_decisions/S*.json — the 209 mappings.

Phases (--phase pre, default: the pre-execution reconciliation; --phase
post: the executed-state verification):

PRE:
  C1  review record resolves to 59 distinct CONFIRM pairs (61 round-3
      minus the 2 round-4 REJECTs); no unresolved/dupes
  C1b round-4 REJECT records well-formed AND removed from the store
  C1c round-5 record: 150 pairs, idx 1..150, all CONFIRM, distinct, all
      present in the store by exact (note, code) identity, pre-review SHA
      c6454c9 an ancestor of HEAD
  C2  sheet §12 contains exactly 59 distinct --map specs
  C2b sheet §13 contains exactly 150 distinct --map specs
  C3  production resolver resolves all 59 specs unambiguously
  C3b production resolver resolves all 150 specs unambiguously (bare CODE
      only where the code lives on exactly one note)
  C4a every surviving reviewed pair is staged by §12 (completeness)
  C4b every §12 staged target is a reviewed pair (no unreviewed promotion)
  C4c no round-4 REJECTed pair is staged
  C4d §13 staged pairs == exactly the 150 round-5 CONFIRM pairs (bijection)
  C4e §12 ∩ §13 = empty AND §12 ∪ §13 = the whole 209-mapping store (each
      mapping staged for ratification exactly once)
  C5  pre-state: 0 promoted anywhere, all 209 SUGGESTED — the two batches
      are exactly 209 promotions and 0 no-ops
  C6  store shape: 112 notes / 209 mappings / high 176 / medium 32 / low 1
  C7  corpus-architecture stat: 68/112 notes carry 2+ codes
  C8  VLM archive: 29 verdict JSONs (21 round-3/4 + 8 round-5), codes
      matching the P6a queue and the round-5 verification set exactly
  C9  git provenance: HEAD descends from the pushed round-5 state c90f5ae,
      tree clean apart from this change-set's own artifacts

POST (after both staged commands have been executed):
  E1  executed state: 209/209 HUMAN_VALIDATED, every block well-formed
      with validated_by == operator and validated_date == 2026-09-11,
      zero SUGGESTED mappings left
  E2  promoted set == §12 ∪ §13 staged targets (exact bijection, 209)
  E3  store shape unchanged by promotion: 112 / 209 / 176-32-1
  E4  round-5 text reconciliation: all 150 evidence quotes retained
      exactly; 148 rationales byte-identical to the review record; the 2
      recorded corrections (4CH1-1.1, 4CH1-1.19) applied verbatim
  E5  VLM archive: 29 verdict JSONs as in pre C8
  E6  git provenance: HEAD descends from c90f5ae; the only dirty paths are
      the expected execution paths (decisions, note front matter, the
      regenerated coverage report) plus this audit's own artifacts
  E7  note bodies byte-identical to the round-5 review state c90f5ae for
      all 112 corpus notes (promotion touches front matter only)

Read-only: nothing in c10_decisions/, notes/ or the sheet is modified.
Writes graph/reports/C10_RATIFICATION_AUDIT.json + .md only.

Usage: python3 scripts/c10_ratify_audit.py [--phase pre|post]
"""
from __future__ import annotations

import argparse
import datetime
import json
import shlex
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import c10_pr_review_verdicts as VR  # noqa: E402  (round-3 review record)
import c10_round4_rejects as R4  # noqa: E402  (round-4 supersession record)
import c10_promote  # noqa: E402  (production promoter)

REPORTS = HERE.parent / "graph" / "reports"
SHEET = REPORTS / "PHASE2_PR_REVIEW_SHEET.md"
REVIEW5 = REPORTS / "C10_ROUND5_REVIEW.json"
JSON_OUT = REPORTS / "C10_RATIFICATION_AUDIT.json"
MD_OUT = REPORTS / "C10_RATIFICATION_AUDIT.md"
ROUND5_BASE = "c90f5ae"   # pushed round-5 review state (this audit's base)
PRE_REVIEW_BASE = "c6454c9"  # round-5 pre-review SHA pinned in the record
EXPECTED_BY = "operator"
EXPECTED_DATE = "2026-09-11"

# this audit is additive-only: its own artifacts + the round-5 staging
# change-set (§13 staging, audit extension, coverage-template text, README)
# must not count as pre-existing dirtiness — none of them touch the
# decisions store, the notes or the review records
SELF_ARTIFACTS = {
    "scripts/c10_ratify_audit.py",
    "scripts/c10_round5_rework.py",
    "scripts/c10_round5_batch.py",
    "scripts/c10_map_notes.py",
    "scripts/README.md",
    "graph/reports/C10_RATIFICATION_AUDIT.json",
    "graph/reports/C10_RATIFICATION_AUDIT.md",
    "graph/reports/PHASE2_PR_REVIEW_SHEET.md",
}

checks = []


def check(cid, name, ok, detail=""):
    checks.append({"id": cid, "name": name, "status": "PASS" if ok else "FAIL",
                   "detail": detail})
    print(f"[{'PASS' if ok else 'FAIL'}] {cid} {name}"
          + (f" — {detail}" if detail else ""))
    return ok


# ---------------------------------------------------------------------------
# D. load the store (production loader — also proves cross-file key uniqueness)
# ---------------------------------------------------------------------------
store = c10_promote.load_all()  # note -> {file, file_data, mappings}
all_pairs = {}  # (code, note) -> mapping
for note, d in store.items():
    for m in d["mappings"]:
        key = (m["code"], note)
        if key in all_pairs:
            sys.exit(f"FAIL: duplicate (code, note) pair in store: {key}")
        all_pairs[key] = m


def resolve_review_fragment(code: str, frag: str) -> str | None:
    """Side-A resolver: unique note whose STEM contains frag and carries code."""
    hits = [n for n, d in store.items()
            if any(m["code"] == code for m in d["mappings"])
            and frag.lower() in Path(n).stem.lower()]
    return hits[0] if len(hits) == 1 else None


# the round-4 rejected pairs (full note paths, matching store keys)
rejected = {(r["code"], r["note"]) for r in R4.ROUND4_REJECTS}


def match_reject(code: str, frag: str) -> tuple[str, str] | None:
    """Round-4 supersession matcher: does this round-3 entry name a
    rejected pair? (fragment matched case-insensitively against the
    rejected note's stem.)"""
    for c, n in rejected:
        if c == code and frag.lower() in Path(n).stem.lower():
            return (c, n)
    return None


# ---------------------------------------------------------------------------
# A/B. the reviewed set: round-3 record minus the round-4 supersessions,
#      assembled exactly as the sheet generator defines it (queue origin
#      tracked for the report)
# ---------------------------------------------------------------------------
pairs_origin: dict[tuple[str, str], str] = {}
unresolved: list[str] = []
dupes: list[str] = []
superseded: list[tuple[str, str]] = []
bad_verdicts: list[str] = []


def add_pair(code: str, frag: str, origin: str):
    note = resolve_review_fragment(code, frag)
    if note is None:
        unresolved.append(f"{code} @ {frag}")
        return
    key = (code, note)
    if key in pairs_origin:
        dupes.append(f"{code} @ {Path(note).stem} (from {origin}; "
                     f"already {pairs_origin[key]})")
        return
    pairs_origin[key] = origin


for x in VR.P1 + VR.P2 + VR.P5 + VR.P3:
    rej = match_reject(x["code"], x["note"])
    if rej is not None:
        # round-4 supersession: this round-3 CONFIRM was REJECTed and its
        # mapping removed — it must NOT resolve (the code is gone from the
        # note) and must NOT be staged; record it as superseded instead.
        superseded.append(rej)
        continue
    if not x["verdict"].strip().upper().startswith("CONFIRM"):
        bad_verdicts.append(f"{x['code']} @ {x['note']}: {x['verdict']}")
    add_pair(x["code"], x["note"], "P1/P2/P5/P3")
add_pair("4CH1-1.17", "Relative atomic mass", "P4 S1-c high")
for code, frag, _s, _d in VR.P6A:
    if not any(c == code and frag.lower() in n.lower()
               for c, n in pairs_origin):
        add_pair(code, frag, "P6a diagram queue")
for code, frag, _c, _d in VR.P6B:
    if not any(c == code and frag.lower() in n.lower()
               for c, n in pairs_origin):
        add_pair(code, frag, "P6b missing figures")

reviewed = set(pairs_origin)  # the round-4-surviving CONFIRM set

P6A_OK = {"OK", "OK (prior)", "FLAG→OK"}  # (prior) = carried spot-check
p6a_ok = all(s in P6A_OK for _c, _f, s, _d in VR.P6A)
p6b_ok = all(c == "PASS" for _c, _f, c, _d in VR.P6B)


# ---------------------------------------------------------------------------
# A5. the round-5 review record
# ---------------------------------------------------------------------------
r5 = json.loads(REVIEW5.read_text(encoding="utf-8"))
r5_pairs_list = r5["reviewed_pairs"]
r5_pairs = [(p["code"], p["note"]) for p in r5_pairs_list]
r5_by_key = {(p["code"], p["note"]): p for p in r5_pairs_list}


# ---------------------------------------------------------------------------
# C. the staged sheet commands, parsed from the on-disk sheet
# ---------------------------------------------------------------------------
def parse_sheet_specs(text: str, heading: str):
    """Extract the --map specs from a staged sheet section's bash block."""
    if heading not in text:
        sys.exit(f"FAIL: sheet section not found: {heading!r}")
    sec = text.split(heading, 1)[1]
    bash = sec.split("```bash", 1)[1].split("```", 1)[0]
    tokens = shlex.split(bash.replace("\\\n", " "))
    specs = [t for i, t in enumerate(tokens) if i > 0 and tokens[i - 1] == "--map"]
    by = tokens[tokens.index("--by") + 1] if "--by" in tokens else None
    date = tokens[tokens.index("--date") + 1] if "--date" in tokens else None
    return specs, by, date


def resolve_or_fail(specs: list[str]):
    """Resolve with the PRODUCTION resolver — SystemExit means the promoter
    itself would refuse (no mapping / ambiguous), which is a FAIL here."""
    try:
        targets = c10_promote.resolve_targets(store, specs)
        return [(m["code"], n) for n, m in targets], None
    except SystemExit as e:
        return None, str(e)


# ---------------------------------------------------------------------------
# git helpers
# ---------------------------------------------------------------------------
def git(*args) -> subprocess.CompletedProcess:
    return subprocess.run(["git", *args], cwd=HERE.parent,
                          capture_output=True, text=True, timeout=30)


def git_head() -> str:
    try:
        return git("rev-parse", "--short", "HEAD").stdout.strip()
    except Exception:
        return ""


def git_descends(base: str) -> bool:
    r = git("merge-base", "--is-ancestor", base, "HEAD")
    return r.returncode == 0


def git_status() -> str:
    try:
        return git("status", "--porcelain").stdout
    except Exception:
        return ""


def body_of(text: str) -> str:
    """The note body: everything after the closing --- of the front matter."""
    lines = text.split("\n")
    if lines and lines[0].strip() == "---":
        for i in range(1, len(lines)):
            if lines[i].strip() == "---":
                return "\n".join(lines[i + 1:])
    return text


# ---------------------------------------------------------------------------
# shared facts
# ---------------------------------------------------------------------------
n_notes = len(store)
n_maps = len(all_pairs)
conf = {"high": 0, "medium": 0, "low": 0}
for m in all_pairs.values():
    conf[m["confidence"]] = conf.get(m["confidence"], 0) + 1
multi = sum(1 for d in store.values()
            if len({m["code"] for m in d["mappings"]}) >= 2)

vlm_dir = HERE / "c10_vlm_results"
vlm_codes = {p.stem for p in vlm_dir.glob("*.json")}
r5_vlm_codes = set(r5["vlm_verifications"].keys())
p6a_codes = {c for c, _f, _s, _d in VR.P6A}
expected_vlm = p6a_codes | {f"round5-{c}" for c in r5_vlm_codes}

sheet_text = SHEET.read_text(encoding="utf-8")
s12_specs, s12_by, s12_date = parse_sheet_specs(sheet_text, "## 12. Round 4")
s13_specs, s13_by, s13_date = parse_sheet_specs(sheet_text, "## 13. Round 5")
staged12, resolver_fail12 = resolve_or_fail(s12_specs)
staged13, resolver_fail13 = resolve_or_fail(s13_specs)

promoted_now = {k for k, m in all_pairs.items()
                if isinstance(m.get("validation"), dict)
                and m["validation"].get("validation_status") == "HUMAN_VALIDATED"}


def run_pre() -> None:
    check("C1", "review record: 61 round-3 pairs, 2 round-4 REJECTs -> 59 "
          "distinct CONFIRM pairs",
          len(reviewed) == 59 and len(superseded) == 2
          and set(superseded) == rejected and not unresolved and not dupes
          and not bad_verdicts and p6a_ok and p6b_ok,
          (f"{len(reviewed)} CONFIRM pairs; superseded: "
           f"{len(superseded)} (== R4.ROUND4_REJECTS); verdicts scanned: "
           f"{len(VR.P1) + len(VR.P2) + len(VR.P5) + len(VR.P3) - 2} "
           f"+ 1 P4 + {len(VR.P6A)} P6a + {len(VR.P6B)} P6b"
           + (f"; UNRESOLVED: {unresolved}" if unresolved else "")
           + (f"; DUPES: {dupes}" if dupes else "")
           + (f"; NON-CONFIRM VERDICTS: {bad_verdicts}" if bad_verdicts else "")))

    # C1b. round-4 records well-formed + the removals are actually executed
    reject_records_ok = (len(R4.ROUND4_REJECTS) == 2
                         and all(r.get("verdict") == "REJECT"
                                 and r.get("finding", "").strip()
                                 and r.get("disposition", "").strip()
                                 and r.get("spec", "").strip()
                                 for r in R4.ROUND4_REJECTS))
    removal_problems = []
    for code, note in sorted(rejected):
        if note not in store:
            removal_problems.append(f"note missing from store: {note}")
            continue
        codes_now = {m["code"] for m in store[note]["mappings"]}
        if code in codes_now:
            removal_problems.append(f"{code} STILL PRESENT on {Path(note).stem}")
        if not codes_now:
            removal_problems.append(f"{Path(note).stem} has zero mappings left")
    kept_ok = {Path(n).stem: sorted({m["code"] for m in store[n]["mappings"]})
               for _c, n in rejected}

    check("C1b", "round-4 REJECTs well-formed and REMOVED from the store "
          "(both notes keep >= 1 mapping)",
          reject_records_ok and not removal_problems,
          "; ".join(f"{stem} keeps {codes}" for stem, codes in kept_ok.items())
          + (f"; PROBLEMS: {removal_problems}" if removal_problems else ""))

    # C1c. round-5 record reconciles with the store
    idx_ok = sorted(p["idx"] for p in r5_pairs_list) == list(range(1, 151))
    distinct_ok = len(set(r5_pairs)) == 150
    in_store_ok = all(k in all_pairs for k in r5_pairs)
    anc_ok = git_descends(PRE_REVIEW_BASE)
    corr_ok = len(r5["corrected_rationales"]) == 2
    # corrections must reference real reviewed pairs with the flag set
    corr_ref_ok = all(
        any(p["idx"] == c["idx"] and p["code"] == c["code"]
            and p.get("rationale_correction")
            for p in r5_pairs_list)
        for c in r5["corrected_rationales"])
    check("C1c", "round-5 record: 150 pairs, idx 1..150, all CONFIRM, "
          "distinct, all in store by exact identity; pre-review SHA "
          f"{PRE_REVIEW_BASE} an ancestor of HEAD",
          len(r5_pairs) == 150
          and all(p["verdict"] == "CONFIRM" for p in r5_pairs_list)
          and idx_ok and distinct_ok and in_store_ok and anc_ok
          and corr_ok and corr_ref_ok,
          f"150 pairs ({len(r5_pairs)}); distinct {distinct_ok}; "
          f"in-store {in_store_ok}; pre-review ancestor {anc_ok}; "
          f"{len(r5['corrected_rationales'])} corrections referenced")

    # C2. §12 stages exactly 59 specs
    check("C2", "sheet §12 stages exactly 59 distinct --map specs",
          len(s12_specs) == 59 and len(set(s12_specs)) == 59,
          f"{len(s12_specs)} specs, {len(set(s12_specs))} distinct; "
          f"--by {s12_by!r} --date {s12_date!r}")

    # C2b. §13 stages exactly 150 specs
    check("C2b", "sheet §13 stages exactly 150 distinct --map specs",
          len(s13_specs) == 150 and len(set(s13_specs)) == 150,
          f"{len(s13_specs)} specs, {len(set(s13_specs))} distinct; "
          f"--by {s13_by!r} --date {s13_date!r}")

    # C3 / C3b. production resolver
    bare12 = [s for s in s12_specs if "@" not in s]
    frag12 = [s for s in s12_specs if "@" in s]
    check("C3", "production resolver resolves all 59 specs unambiguously "
          "(no code-wide promotion)",
          resolver_fail12 is None and staged12 is not None
          and len(staged12) == 59 and len(set(staged12)) == 59,
          (f"{len(bare12)} bare CODE specs (each code on exactly one note), "
           f"{len(frag12)} CODE@FRAGMENT specs; 59 distinct (code, note) "
           f"targets" + (f"; PROMOTER WOULD REFUSE: {resolver_fail12}"
                         if resolver_fail12 else "")))

    bare13 = [s for s in s13_specs if "@" not in s]
    frag13 = [s for s in s13_specs if "@" in s]
    # bare codes allowed only where the code lives on exactly one note
    bare_wide = [s for s in bare13
                 if sum(1 for n, d in store.items()
                        if any(m["code"] == s for m in d["mappings"])) > 1]
    check("C3b", "production resolver resolves all 150 specs unambiguously "
          "(bare CODE only where the code lives on exactly one note)",
          resolver_fail13 is None and staged13 is not None
          and len(staged13) == 150 and len(set(staged13)) == 150
          and not bare_wide,
          (f"{len(bare13)} bare CODE specs, {len(frag13)} CODE@FRAGMENT "
           f"specs; 150 distinct (code, note) targets"
           + (f"; PROMOTER WOULD REFUSE: {resolver_fail13}"
              if resolver_fail13 else "")
           + (f"; BARE-BUT-AMBIGUOUS: {bare_wide}" if bare_wide else "")))

    # C4a/C4b/C4c. §12 bijection + safety
    a_minus_b = sorted(f"{c} @ {Path(n).stem}" for c, n in reviewed - set(staged12))
    b_minus_a = sorted(f"{c} @ {Path(n).stem}" for c, n in set(staged12) - reviewed)
    check("C4a", "every surviving reviewed pair is staged by §12 "
          "(completeness)",
          not a_minus_b,
          f"{59 - len(a_minus_b)}/59 staged" + (f"; MISSING: {a_minus_b}"
                                                if a_minus_b else ""))
    check("C4b", "every §12 staged target is a reviewed pair (no unreviewed "
          "promotion)",
          not b_minus_a,
          f"{59 - len(b_minus_a)}/59 reviewed" + (f"; UNREVIEWED: {b_minus_a}"
                                                  if b_minus_a else ""))
    staged_rejects = sorted(f"{c} @ {Path(n).stem}"
                            for c, n in set(staged12) & rejected)
    check("C4c", "no round-4 REJECTed pair is staged (both live outside the "
          "batch)",
          not staged_rejects,
          "staged ∩ rejected = ∅" if not staged_rejects
          else f"REJECTED BUT STAGED: {staged_rejects}")

    # C4d. §13 == the 150 round-5 CONFIRMs
    d_miss = sorted(f"{c} @ {Path(n).stem}"
                    for c, n in set(r5_pairs) - set(staged13))
    d_extra = sorted(f"{c} @ {Path(n).stem}"
                     for c, n in set(staged13) - set(r5_pairs))
    check("C4d", "§13 staged pairs == exactly the 150 round-5 CONFIRM pairs "
          "(bijection)",
          staged13 is not None and not d_miss and not d_extra,
          f"{150 - len(d_miss)}/150 round-5 pairs staged"
          + (f"; MISSING: {d_miss[:3]}" if d_miss else "")
          + (f"; NOT-A-ROUND-5-PAIR: {d_extra[:3]}" if d_extra else ""))

    # C4e. disjoint + union = whole store
    inter = set(staged12) & set(staged13) if staged12 and staged13 else set()
    union = (set(staged12) | set(staged13)) if staged12 and staged13 else set()
    union_gap = sorted(f"{c} @ {Path(n).stem}" for c, n in set(all_pairs) - union)
    union_extra = sorted(f"{c} @ {Path(n).stem}" for c, n in union - set(all_pairs))
    check("C4e", "§12 ∩ §13 = ∅ and §12 ∪ §13 = the whole 209-mapping store "
          "(each mapping staged exactly once)",
          not inter and len(union) == 209 and union == set(all_pairs),
          f"union {len(union)}/209; overlap {len(inter)}"
          + (f"; UNSTAGED: {union_gap[:3]}" if union_gap else "")
          + (f"; NOT-IN-STORE: {union_extra[:3]}" if union_extra else ""))

    # C5. pre-state
    if staged12 is None or staged13 is None:
        staged_ok_state = False
    else:
        staged_ok_state = all(
            all_pairs[k].get("validation") is None
            or all_pairs[k]["validation"].get("validation_status") == "SUGGESTED"
            for k in set(staged12) | set(staged13) if k in all_pairs)
    check("C5", "pre-state: 0 promoted / all 209 SUGGESTED — the batches are "
          "exactly 209 promotions, 0 no-ops",
          len(promoted_now) == 0 and staged_ok_state
          and (set(staged12) | set(staged13)) <= set(all_pairs)
          if staged12 and staged13 else False,
          f"promoted on disk: {len(promoted_now)}; all 209 targets in "
          f"SUGGESTED state: {staged_ok_state}")

    # C6/C7. store shape + corpus stat
    check("C6", "store shape: 112 notes / 209 mappings / 176 high / 32 medium / "
          "1 low",
          n_notes == 112 and n_maps == 209 and conf["high"] == 176
          and conf["medium"] == 32 and conf["low"] == 1,
          f"{n_notes} notes / {n_maps} mappings / {conf}")
    check("C7", "corpus stat: 68/112 notes carry 2+ codes (contributory "
          "many-to-many is the corpus shape)",
          multi == 68, f"{multi}/112")

    # C8. VLM archive
    check("C8", "VLM archive: 29 verdict JSONs (21 round-3/4 + 8 round-5) "
          "with codes matching the P6a queue and the round-5 set exactly",
          len(vlm_codes) == 29 and vlm_codes == expected_vlm,
          f"{len(vlm_codes)} files; sym-diff: "
          f"{sorted(vlm_codes ^ expected_vlm) or 'none'}")

    # C9. git provenance
    st = git_status()
    foreign = [ln[3:].strip() for ln in st.splitlines()
               if ln[3:].strip() not in SELF_ARTIFACTS]
    check("C9", f"git provenance: HEAD descends from the pushed round-5 "
          f"state {ROUND5_BASE}, tree clean apart from this change-set",
          git_descends(ROUND5_BASE) and not foreign,
          f"HEAD {git_head() or 'unknown'}; dirty-foreign: "
          f"{foreign[:3] or 'none'}")

    # note files exist on disk for every staged target
    missing_files = []
    if staged12 and staged13:
        missing_files = [n for _c, n in set(staged12) | set(staged13)
                         if not (HERE.parent / n).exists()]
    if missing_files:
        check("C10", "staged note files exist on disk", False,
              f"missing: {missing_files[:3]}")


def run_post() -> None:
    # E1. executed state
    bad_blocks = []
    for k, m in all_pairs.items():
        val = m.get("validation")
        if not (isinstance(val, dict)
                and val.get("validation_status") == "HUMAN_VALIDATED"
                and val.get("validated_by") == EXPECTED_BY
                and val.get("validated_date") == EXPECTED_DATE):
            bad_blocks.append(f"{k[0]} @ {Path(k[1]).stem}")
    check("E1", f"executed state: 209/209 HUMAN_VALIDATED, every block "
          f"validated_by {EXPECTED_BY!r} + {EXPECTED_DATE!r}, zero SUGGESTED",
          len(promoted_now) == 209 and not bad_blocks,
          f"promoted {len(promoted_now)}/209"
          + (f"; MALFORMED: {bad_blocks[:3]}" if bad_blocks else ""))

    # E2. promoted set == staged union
    union = (set(staged12) | set(staged13)) if staged12 and staged13 else None
    check("E2", "promoted set == §12 ∪ §13 staged targets (exact bijection)",
          union is not None and promoted_now == union,
          f"staged union {len(union) if union else 0}; promoted "
          f"{len(promoted_now)}; sym-diff "
          f"{len(promoted_now ^ union) if union else 'n/a'}")

    # E3. store shape unchanged by promotion
    check("E3", "store shape unchanged by promotion: 112 / 209 / 176-32-1",
          n_notes == 112 and n_maps == 209 and conf["high"] == 176
          and conf["medium"] == 32 and conf["low"] == 1,
          f"{n_notes} notes / {n_maps} mappings / {conf}")

    # E4. round-5 text reconciliation
    text_problems = []
    # build the correction map from the reviewed pairs (idx + code identity)
    corrections = {}
    for c in r5["corrected_rationales"]:
        for p in r5_pairs_list:
            if p["idx"] == c["idx"] and p["code"] == c["code"]:
                corrections[(p["code"], p["note"])] = c["corrected_rationale"]
    for k in r5_pairs:
        m = all_pairs.get(k)
        if m is None:
            text_problems.append(f"{k[0]} @ {Path(k[1]).stem}: not in store")
            continue
        if k in corrections:
            if m["rationale"] != corrections[k]:
                text_problems.append(f"{k[0]}: correction NOT applied verbatim")
        elif m["rationale"] != r5_by_key[k]["rationale"]:
            text_problems.append(f"{k[0]}: rationale drifted")
        if m["evidence"] != r5_by_key[k]["evidence"]:
            text_problems.append(f"{k[0]}: evidence quote altered")
    check("E4", "round-5 text reconciliation: all 150 evidence quotes "
          "retained exactly; 148 rationales byte-identical; the 2 recorded "
          "corrections (4CH1-1.1, 4CH1-1.19) applied verbatim",
          not text_problems,
          f"{len(corrections)} corrections verified"
          + (f"; PROBLEMS: {text_problems[:4]}" if text_problems else ""))

    # E5. VLM archive
    check("E5", "VLM archive: 29 verdict JSONs as in the pre-execution audit",
          len(vlm_codes) == 29 and vlm_codes == expected_vlm,
          f"{len(vlm_codes)} files; sym-diff: "
          f"{sorted(vlm_codes ^ expected_vlm) or 'none'}")

    # E6. git provenance — only expected execution paths may be dirty
    st = git_status()
    dirty = [ln[3:].strip() for ln in st.splitlines()]
    unexpected = []
    for p in dirty:
        if p in SELF_ARTIFACTS:
            continue
        if p.startswith("scripts/c10_decisions/S") and p.endswith(".json"):
            continue
        if p.startswith("Chemistry IGCSE Revision Notes/") and p.endswith(".md"):
            continue
        if p == "graph/reports/PHASE2_MAPPING_COVERAGE.md":
            continue
        unexpected.append(p)
    check("E6", "git provenance: HEAD descends from the round-5 state; only "
          "expected execution paths are dirty (decisions / note front "
          "matter / coverage report) + this audit's own artifacts",
          git_descends(ROUND5_BASE) and not unexpected,
          f"HEAD {git_head() or 'unknown'}; unexpected: "
          f"{unexpected[:3] or 'none'}")

    # E7. note bodies byte-identical to the round-5 review state
    body_drift = []
    notes_root = HERE.parent / "Chemistry IGCSE Revision Notes"
    note_files = sorted(p for p in notes_root.rglob("*.md")
                        if "assets" not in p.parts)
    if len(note_files) != 112:
        body_drift.append(f"corpus note count {len(note_files)} != 112")
    for p in note_files:
        rel = str(p.relative_to(HERE.parent))
        r = git("show", f"{ROUND5_BASE}:{rel}")
        if r.returncode != 0:
            body_drift.append(f"{Path(rel).stem}: not in {ROUND5_BASE}")
            continue
        if body_of(p.read_text(encoding="utf-8")) != body_of(r.stdout):
            body_drift.append(f"{Path(rel).stem}: BODY CHANGED")
    check("E7", "note bodies byte-identical to the round-5 review state "
          f"{ROUND5_BASE} (promotion touches front matter only)",
          not body_drift,
          f"{len(note_files)} notes compared"
          + (f"; DRIFT: {body_drift[:3]}" if body_drift else ""))


# ---------------------------------------------------------------------------
# verdict + artifacts
# ---------------------------------------------------------------------------
def main() -> int:
    ap = argparse.ArgumentParser(description="T-C10 ratification audit")
    ap.add_argument("--phase", choices=["pre", "post"], default="pre",
                    help="pre: reconcile the staged batches before "
                         "execution (default); post: verify the executed "
                         "state after both commands ran")
    args = ap.parse_args()

    if args.phase == "pre":
        run_pre()
    else:
        run_post()

    verdict = ("PASS" if all(c["status"] == "PASS" for c in checks) else "FAIL")

    pairs_json = [{"code": c, "note": n, "note_stem": Path(n).stem,
                   "queue": pairs_origin[(c, n)],
                   "confidence": all_pairs[(c, n)]["confidence"],
                   "verdict": "CONFIRM (AI review pass 2026-09-11; "
                              "round-4 survivor)"}
                  for c, n in sorted(reviewed)]
    rejects_json = [{"code": r["code"], "note": r["note"],
                     "note_stem": Path(r["note"]).stem,
                     "verdict": "REJECT (round 4, 2026-09-11)",
                     "disposition": r["disposition"]}
                    for r in R4.ROUND4_REJECTS]
    r5_json = [{"code": p["code"], "note": p["note"],
                "note_stem": Path(p["note"]).stem,
                "confidence": p["confidence"],
                "verdict": "CONFIRM (round-5 exhaustive review, 2026-09-11)"}
               for p in r5_pairs_list]

    report = {
        "audit": (f"T-C10 ratification reconciliation (read-only; round-5 "
                  f"dual-batch edition, phase={args.phase})"),
        "generated": datetime.date.today().isoformat(),
        "phase": args.phase,
        "operator_instruction": "Ratify the 59 and promote 150 (2026-09-11)",
        "operator_advisor_condition": (
            "round 3: machine-verifiable reconciliation of the ratification "
            "targets against the review sheet — exact note->SpecificationPoint "
            "identity, no unreviewed mapping promoted. Round 4 added: remove/"
            "rework the two rejected mappings, regenerate the gates, then the "
            "final exact-target reconciliation before ratification. Round 5 "
            "added: the 150-spec §13 batch staged from C10_ROUND5_REVIEW.json "
            "must reconcile identically before execution, and the executed "
            "state must verify afterwards (--phase post)."),
        "repo_head": git_head() or "unknown",
        "sheet": str(SHEET.relative_to(HERE.parent)),
        "verdict": verdict,
        "checks": checks,
        "stats": {"notes": n_notes, "mappings": n_maps, "confidence": conf,
                  "promoted": len(promoted_now),
                  "notes_with_2plus_codes": multi, "vlm_files": len(vlm_codes),
                  "s12_specs": len(s12_specs), "s13_specs": len(s13_specs),
                  "s12_by": s12_by, "s12_date": s12_date,
                  "s13_by": s13_by, "s13_date": s13_date,
                  "round4_rejected": len(rejected),
                  "round5_pairs": len(r5_pairs),
                  "round5_corrections": len(r5["corrected_rationales"])},
        "reviewed_pairs": pairs_json,
        "round5_pairs": r5_json,
        "rejected_pairs": rejects_json,
        "conclusion": "",
    }

    if args.phase == "pre":
        report["conclusion"] = (
            "Both staged batches are exactly the AI-reviewed sets: §12 "
            "promotes exactly the 59 round-4-surviving CONFIRMs (both "
            "round-4 REJECTs proven removed from the store and absent from "
            "the command), §13 promotes exactly the 150 round-5 CONFIRMs, "
            "the two batches are disjoint and cover the whole 209-mapping "
            "store exactly once, and the pre-state is 0 promoted / 209 "
            "SUGGESTED. The operator may execute §12 then §13 as staged."
        ) if verdict == "PASS" else \
            "DISCREPANCIES FOUND — see checks; do not run the batches until fixed."
    else:
        report["conclusion"] = (
            "Execution verified: the store now carries 209/209 "
            "HUMAN_VALIDATED mappings (validated_by operator, 2026-09-11), "
            "the promoted set is exactly §12 ∪ §13, store shape is "
            "unchanged, all 150 round-5 evidence quotes are retained, the 2 "
            "recorded rationale corrections are applied verbatim, and all "
            "112 note bodies are byte-identical to the round-5 review "
            "state. T-C10's human-validation gate is discharged."
        ) if verdict == "PASS" else \
            "EXECUTION DISCREPANCIES FOUND — see checks; investigate before any further change."

    JSON_OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")

    md = ["<!-- c10-ratify-audit-" + datetime.date.today().isoformat() + " -->",
          f"# T-C10 — Ratification Reconciliation Audit "
          f"({datetime.date.today().isoformat()}, phase: {args.phase}) — "
          f"**{verdict}**", "",
          "Read-only audit executing the operator-advisor's condition "
          "(rounds 3-5) over BOTH staged batches — §12 (59-spec, round-4 "
          "survivors) and §13 (150-spec, round-5 CONFIRMs, staged from "
          "`C10_ROUND5_REVIEW.json`); generator `scripts/c10_ratify_audit.py` "
          "(machine record: `C10_RATIFICATION_AUDIT.json`). Operator "
          "instruction: \"Ratify the 59 and promote 150\" (2026-09-11).", "",
          "| # | check | status | detail |", "|---|---|---|---|"]
    for c in checks:
        md.append(f"| {c['id']} | {c['name']} | **{c['status']}** | "
                  f"{c['detail'][:160]} |")
    md += ["", "## The 59 §12 ratification identities (round-4 survivors)", "",
           "Every pair below is an AI-reviewed CONFIRM that survived the "
           "round-4 supersession (review record: "
           "`scripts/c10_pr_review_verdicts.py` + "
           "`scripts/c10_round4_rejects.py`, rendered in "
           "PHASE2_PR_REVIEW_SHEET.md §2–§8 + §12) and resolves, via the "
           "production `c10_promote.py` resolver, to exactly the staged §12 "
           "spec:", "",
           "| # | code | note (stem) | queue | confidence |", "|---:|---|---|---|---|"]
    for i, p in enumerate(pairs_json, 1):
        md.append(f"| {i} | {p['code']} | {p['note_stem']} | {p['queue']} | "
                  f"{p['confidence']} |")
    md += ["", "## The 150 §13 ratification identities (round-5 CONFIRMs)", "",
           "Every pair below is a round-5 exhaustive-review CONFIRM "
           "(150 CONFIRM / 0 REJECT / 0 HOLD, frozen guide §0.0 + §8 "
           "contract; row-level detail with evidence, spec wording and "
           "findings: `PHASE2_ROUND5_REVIEW_SHEET.md` §4 / "
           "`C10_ROUND5_REVIEW.json`):", "",
           "| # | code | note (stem) | confidence |", "|---:|---|---|---|"]
    for i, p in enumerate(r5_json, 1):
        md.append(f"| {i} | {p['code']} | {p['note_stem']} | "
                  f"{p['confidence']} |")
    md += ["", "## The 2 round-4 rejections (proven outside the batches)", "",
           "| code | note (stem) | verdict | disposition |", "|---|---|---|---|"]
    for r in rejects_json:
        md.append(f"| {r['code']} | {r['note_stem']} | **{r['verdict']}** | "
                  f"{r['disposition'][:120]} |")
    md += ["", report["conclusion"], "",
           f"Provenance: repo HEAD `{git_head() or 'unknown'}` (descends from "
           f"the round-5 review state `{ROUND5_BASE}`; round-5 pre-review SHA "
           f"`{PRE_REVIEW_BASE}`).",
           ""]
    if args.phase == "pre":
        md += ["After the operator runs §12 then §13, all 209 mappings "
               "become HUMAN_VALIDATED (validated_by `operator`, "
               "2026-09-11) — re-run this audit with `--phase post` to "
               "machine-verify the executed state (identity bijection, "
               "store shape, evidence retention, note-body integrity).", ""]
    else:
        md += ["Post-execution verification complete: the promotion-only "
               "invariant holds (note bodies byte-identical, evidence "
               "retained, shape unchanged) and the human-validation gate "
               "for the whole 209-mapping store is discharged. 4CH1-4.15 "
               "remains an honest zero-coverage corpus gap (T-C11 input).", ""]
    MD_OUT.write_text("\n".join(md), encoding="utf-8")

    print(f"\nVERDICT: {verdict} (phase: {args.phase})")
    print(f"report: {JSON_OUT.relative_to(HERE.parent)}")
    print(f"report: {MD_OUT.relative_to(HERE.parent)}")
    return 0 if verdict == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
