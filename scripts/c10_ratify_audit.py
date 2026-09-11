#!/usr/bin/env python3
"""
T-C10 — pre-ratification reconciliation audit (read-only; round-4 edition).

Executes the operator-advisor's procedural condition before the staged
batch is run, re-targeted after the fourth review round:

    "Perform one final machine-verifiable reconciliation of the
     ratification targets against the review sheet, proving exact
     note->SpecificationPoint identity and proving no target promotes an
     unreviewed mapping." (round 3)

    "I would not run the 61-item ratification command yet … remove/rework
     these two mappings, regenerate the gates, and then we can do the
     final exact-target reconciliation before ratification." (round 4)

The round-4 rework (commit 49a0478, `scripts/c10_round4_rejects.py`)
removed the two rejected mappings; the staged batch is now the 59-spec
command in PHASE2_PR_REVIEW_SHEET.md §12 (§11 is ON HOLD). This audit
proves that batch is exactly the round-4-surviving reviewed set.

Method — four independent sides, all read from the repo as it stands:

  A. REVIEW RECORD   scripts/c10_pr_review_verdicts.py (round-3 verdict
                     data) + scripts/c10_round4_rejects.py (round-4
                     supersession record, ROUND4_REJECTS): assemble the
                     reviewed pairs, skip the two rejected, resolve the
                     59 survivors against the decisions store.
  B. ROUND-4 RECORD  scripts/c10_round4_rejects.py — the 2 REJECT entries
                     with verdicts, findings and dispositions.
  C. RATIFY COMMAND  the ```bash block in PHASE2_PR_REVIEW_SHEET.md §12 —
                     the exact artifact the operator will copy — parsed
                     with shlex and resolved with the PRODUCTION resolver
                     (c10_promote.load_all + c10_promote.resolve_targets),
                     so the audit proves what the promoter would actually
                     do, including its refuse-on-ambiguity behaviour.
  D. DECISIONS STORE scripts/c10_decisions/S*.json — the 209 mappings.

Checks:
  C1  review record resolves to 59 distinct CONFIRM (code, note) pairs
      (61 round-3 pairs minus the 2 round-4 REJECTs); no unresolved /
      duplicate fragments
  C1b round-4 REJECT records well-formed (verdict REJECT, non-empty
      finding + disposition) AND the removal is executed: each rejected
      code is ABSENT from its note's mappings in the store, and both
      notes still exist with >= 1 mapping
  C2  sheet §12 contains exactly 59 distinct --map specs
  C3  production resolver resolves all 59 specs unambiguously to
      59 distinct (code, note) pairs (bare CODE specs allowed only
      where the code lives on exactly one note — no code-wide promotion)
  C4a every surviving reviewed pair is staged by the command
      (completeness)
  C4b every staged target is a reviewed pair (no unreviewed promotion)
  C4c no rejected pair is staged (the two REJECTs are outside the batch)
  C5  pre-state: 0 promoted anywhere, all 209 SUGGESTED — the batch
      will be exactly 59 promotions and 0 no-ops
  C6  store shape: 112 notes / 209 mappings / high 176 / medium 32 /
      low 1
  C7  corpus-architecture stat: 68/112 notes carry 2+ codes
  C8  VLM archive: 21 verdict JSONs, codes exactly matching the P6a queue
  C9  git provenance: HEAD is the round-4 rework commit (49a0478),
      tree clean

Read-only: nothing in c10_decisions/, notes/ or the sheet is modified.
Writes graph/reports/C10_RATIFICATION_AUDIT.json + .md only.

Usage: python3 scripts/c10_ratify_audit.py
"""
from __future__ import annotations

import json
import shlex
import subprocess
import sys
import datetime
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))

import c10_pr_review_verdicts as VR  # noqa: E402  (round-3 review record)
import c10_round4_rejects as R4  # noqa: E402  (round-4 supersession record)
import c10_promote  # noqa: E402  (production promoter)

REPORTS = HERE.parent / "graph" / "reports"
SHEET = REPORTS / "PHASE2_PR_REVIEW_SHEET.md"
JSON_OUT = REPORTS / "C10_RATIFICATION_AUDIT.json"
MD_OUT = REPORTS / "C10_RATIFICATION_AUDIT.md"
EXPECTED_HEAD = "49a0478"

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

# ---------------------------------------------------------------------------
# C1b. round-4 records well-formed + the removals are actually executed
# ---------------------------------------------------------------------------
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

# ---------------------------------------------------------------------------
# C. the staged §12 command, parsed from the on-disk sheet
# ---------------------------------------------------------------------------
text = SHEET.read_text(encoding="utf-8")
sec = text.split("## 12. Round 4", 1)[1]
bash = sec.split("```bash", 1)[1].split("```", 1)[0]
joined = bash.replace("\\\n", " ")
tokens = shlex.split(joined)
specs = [t for i, t in enumerate(tokens) if i > 0 and tokens[i - 1] == "--map"]
by = tokens[tokens.index("--by") + 1] if "--by" in tokens else None
date = tokens[tokens.index("--date") + 1] if "--date" in tokens else None

check("C2", "sheet §12 stages exactly 59 distinct --map specs",
      len(specs) == 59 and len(set(specs)) == 59,
      f"{len(specs)} specs, {len(set(specs))} distinct; "
      f"--by {by!r} --date {date!r}")

# resolve with the PRODUCTION resolver — SystemExit means the promoter
# itself would refuse (no mapping / ambiguous), which is a FAIL here
resolver_fail = None
targets = []
try:
    targets = c10_promote.resolve_targets(store, specs)
except SystemExit as e:
    resolver_fail = str(e)
staged = [(m["code"], n) for n, m in targets]
bare = [s for s in specs if "@" not in s]
frag_specs = [s for s in specs if "@" in s]

check("C3", "production resolver resolves all 59 specs unambiguously "
      "(no code-wide promotion)",
      resolver_fail is None and len(staged) == 59 and len(set(staged)) == 59,
      (f"{len(bare)} bare CODE specs (each code on exactly one note), "
       f"{len(frag_specs)} CODE@FRAGMENT specs; 59 distinct (code, note) "
       f"targets" + (f"; PROMOTER WOULD REFUSE: {resolver_fail}"
                     if resolver_fail else "")))

# ---------------------------------------------------------------------------
# C4/C5. bijection + safety
# ---------------------------------------------------------------------------
a_minus_b = sorted(f"{c} @ {Path(n).stem}" for c, n in reviewed - set(staged))
b_minus_a = sorted(f"{c} @ {Path(n).stem}" for c, n in set(staged) - reviewed)

check("C4a", "every surviving reviewed pair is staged by the command "
      "(completeness)",
      not a_minus_b,
      f"{59 - len(a_minus_b)}/59 staged" + (f"; MISSING: {a_minus_b}"
                                            if a_minus_b else ""))
check("C4b", "every staged target is a reviewed pair (no unreviewed "
      "promotion)",
      not b_minus_a,
      f"{59 - len(b_minus_a)}/59 reviewed" + (f"; UNREVIEWED: {b_minus_a}"
                                              if b_minus_a else ""))

staged_rejects = sorted(f"{c} @ {Path(n).stem}"
                        for c, n in set(staged) & rejected)
check("C4c", "no round-4 REJECTed pair is staged (both live outside the "
      "batch)",
      not staged_rejects,
      "staged ∩ rejected = ∅" if not staged_rejects
      else f"REJECTED BUT STAGED: {staged_rejects}")

promoted_now = [k for k, m in all_pairs.items()
                if isinstance(m.get("validation"), dict)
                and m["validation"].get("validation_status") == "HUMAN_VALIDATED"]
staged_ok_state = all(all_pairs[k].get("validation") is None
                      or all_pairs[k]["validation"].get("validation_status")
                      == "SUGGESTED" for k in set(staged) if k in all_pairs)
check("C5", "pre-state: 0 promoted / all 209 SUGGESTED — batch = exactly 59 "
      "promotions, 0 no-ops",
      len(promoted_now) == 0 and staged_ok_state and set(staged) <= set(all_pairs),
      f"promoted on disk: {len(promoted_now)}; all 59 targets in SUGGESTED "
      f"state: {staged_ok_state}")

# ---------------------------------------------------------------------------
# C6/C7/C8. store shape, corpus stat, VLM archive
# ---------------------------------------------------------------------------
n_notes = len(store)
n_maps = len(all_pairs)
conf = {"high": 0, "medium": 0, "low": 0}
for m in all_pairs.values():
    conf[m["confidence"]] = conf.get(m["confidence"], 0) + 1
multi = sum(1 for d in store.values()
            if len({m["code"] for m in d["mappings"]}) >= 2)

check("C6", "store shape: 112 notes / 209 mappings / 176 high / 32 medium / "
      "1 low",
      n_notes == 112 and n_maps == 209 and conf["high"] == 176
      and conf["medium"] == 32 and conf["low"] == 1,
      f"{n_notes} notes / {n_maps} mappings / {conf}")

check("C7", "corpus stat: 68/112 notes carry 2+ codes (contributory "
      "many-to-many is the corpus shape)",
      multi == 68, f"{multi}/112")

vlm_dir = HERE / "c10_vlm_results"
vlm_codes = {p.stem.replace(".json", "") for p in vlm_dir.glob("*.json")}
p6a_codes = {c for c, _f, _s, _d in VR.P6A}
check("C8", "VLM archive: 21 verdict JSONs with codes matching the P6a "
      "queue exactly",
      len(vlm_codes) == 21 and vlm_codes == p6a_codes,
      f"{len(vlm_codes)} files; sym-diff: "
      f"{sorted(vlm_codes ^ p6a_codes) or 'none'}")

# ---------------------------------------------------------------------------
# C9. git provenance
# ---------------------------------------------------------------------------
head = dirty = ""
try:
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                          cwd=HERE.parent, capture_output=True, text=True,
                          timeout=15).stdout.strip()
    st = subprocess.run(["git", "status", "--porcelain"], cwd=HERE.parent,
                        capture_output=True, text=True,
                        timeout=15).stdout
    # this audit is additive-only: its own artifacts (script + 2 reports)
    # must not count as pre-existing dirtiness
    self_artifacts = {"scripts/c10_ratify_audit.py",
                      "graph/reports/C10_RATIFICATION_AUDIT.json",
                      "graph/reports/C10_RATIFICATION_AUDIT.md"}
    foreign = [ln for ln in st.splitlines()
               if ln[3:].strip() not in self_artifacts]
    dirty = "clean" if not foreign else f"dirty ({len(foreign)} foreign files: {[ln[3:].strip() for ln in foreign]})"
except Exception as e:  # git not decisive — don't fail the audit on it
    dirty = f"unavailable ({e})"
check("C9", f"git provenance: HEAD {EXPECTED_HEAD}… (round-4 rework commit), "
      f"tree clean",
      head.startswith(EXPECTED_HEAD) and dirty == "clean",
      f"HEAD {head or 'unknown'}, tree {dirty}")

# note files exist on disk for every staged target
missing_files = [n for _c, n in set(staged) if not (HERE.parent / n).exists()]
if missing_files:
    check("C10", "staged note files exist on disk", False,
          f"missing: {missing_files[:3]}")

# ---------------------------------------------------------------------------
# verdict + artifacts
# ---------------------------------------------------------------------------
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

report = {
    "audit": "T-C10 pre-ratification reconciliation (read-only; round 4)",
    "generated": datetime.date.today().isoformat(),
    "operator_advisor_condition": (
        "round 3: machine-verifiable reconciliation of the ratification "
        "targets against the review sheet — exact note->SpecificationPoint "
        "identity, no unreviewed mapping promoted. Round 4 added: remove/"
        "rework the two rejected mappings, regenerate the gates, then the "
        "final exact-target reconciliation before ratification — both "
        "discharged here against the 59-spec sheet §12 batch"),
    "repo_head": head or "unknown",
    "sheet": str(SHEET.relative_to(HERE.parent)),
    "verdict": verdict,
    "checks": checks,
    "stats": {"notes": n_notes, "mappings": n_maps, "confidence": conf,
              "promoted_before": len(promoted_now),
              "notes_with_2plus_codes": multi, "vlm_files": len(vlm_codes),
              "command_specs": len(specs),
              "bare_code_specs": len(bare), "fragment_specs": len(frag_specs),
              "command_by": by, "command_date": date,
              "round4_rejected": len(rejected)},
    "reviewed_pairs": pairs_json,
    "rejected_pairs": rejects_json,
    "conclusion": (
        "The staged 59-spec c10_promote.py batch in PHASE2_PR_REVIEW_SHEET.md "
        "§12 promotes exactly the 59 round-4-surviving AI-reviewed CONFIRM "
        "mappings — exact (note, code) identity proven, zero unreviewed or "
        "code-wide promotions, zero ambiguity, both round-4 REJECTs proven "
        "removed from the store and absent from the command, store "
        "pre-state 0 promoted / 209 SUGGESTED. The operator may execute "
        "the §12 batch as staged.")
        if verdict == "PASS" else
        "DISCREPANCIES FOUND — see checks; do not run the batch until fixed.",
}

JSON_OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")

md = ["<!-- c10-ratify-audit-" + datetime.date.today().isoformat() + " -->",
      f"# T-C10 — Pre-Ratification Reconciliation Audit "
      f"({datetime.date.today().isoformat()}) — **{verdict}**", "",
      "Read-only audit executing the operator-advisor's condition (round 3, "
      "re-targeted after round 4) before the staged §12 batch: generator "
      "`scripts/c10_ratify_audit.py` (machine record: "
      "`C10_RATIFICATION_AUDIT.json`).", "",
      "| # | check | status | detail |", "|---|---|---|---|"]
for c in checks:
    md.append(f"| {c['id']} | {c['name']} | **{c['status']}** | "
              f"{c['detail'][:160]} |")
md += ["", "## The 59 exact ratification identities", "",
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
md += ["", "## The 2 round-4 rejections (proven outside the batch)", "",
       "| code | note (stem) | verdict | disposition |", "|---|---|---|---|"]
for r in rejects_json:
    md.append(f"| {r['code']} | {r['note_stem']} | **{r['verdict']}** | "
              f"{r['disposition'][:120]} |")
md += ["", report["conclusion"], "",
       f"Provenance: repo HEAD `{head or 'unknown'}` (the round-4 rework "
       f"commit, carrying the two removals and the green gates); tree "
       f"{dirty} before this audit's report files.",
       "", "After the operator runs the §12 command, those 59 mappings "
       "become HUMAN_VALIDATED (validated_by `operator`) — a distinct state "
       "from this AI CONFIRM, per the provenance chain. The 150 mappings "
       "outside the reviewed set remain SUGGESTED (risk-tiered validation "
       "state, guide §7), and 4CH1-4.15 remains an honest zero-coverage "
       "corpus gap (T-C11 input).", ""]
MD_OUT.write_text("\n".join(md), encoding="utf-8")

print(f"\nVERDICT: {verdict}")
print(f"report: {JSON_OUT.relative_to(HERE.parent)}")
print(f"report: {MD_OUT.relative_to(HERE.parent)}")
sys.exit(0 if verdict == "PASS" else 1)
