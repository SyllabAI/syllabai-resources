#!/usr/bin/env python3
"""
T-C10 — pre-ratification reconciliation audit (read-only).

Executes the operator-advisor's one procedural condition before the staged
61-mapping batch is run:

    "Perform one final machine-verifiable reconciliation of the 61
     ratification targets against the review sheet, proving exact
     note->SpecificationPoint identity and proving no target promotes an
     unreviewed mapping."

Method — three independent sides, all read from the repo as it stands:

  A. REVIEW RECORD   scripts/c10_pr_review_verdicts.py (the machine-readable
                     verdict data behind PHASE2_PR_REVIEW_SHEET.md): assemble
                     the 61 reviewed (code, note-fragment) pairs and resolve
                     each against the decisions store (unique stem match).
  B. RATIFY COMMAND  the ```bash block in graph/reports/PHASE2_PR_REVIEW_SHEET.md
                     §11 — the exact artifact the operator will copy — parsed
                     with shlex and resolved with the PRODUCTION resolver
                     (c10_promote.load_all + c10_promote.resolve_targets), so
                     the audit proves what the promoter would actually do,
                     including its refuse-on-ambiguity behaviour.
  C. DECISIONS STORE scripts/c10_decisions/S*.json — the 211 mappings.

Checks:
  C1  review record resolves to 61 distinct (code, note) pairs,
      every verdict is CONFIRM (P6b: PASS) — zero REJECT / HOLD
  C2  sheet §11 contains exactly 61 distinct --map specs
  C3  production resolver resolves all 61 specs unambiguously to
      61 distinct (code, note) pairs (bare CODE specs allowed only
      where the code lives on exactly one note — no code-wide promotion)
  C4a every reviewed pair is staged by the command (completeness)
  C4b every staged target is a reviewed pair (no unreviewed promotion)
  C5  pre-state: 0 promoted anywhere, all 211 SUGGESTED — the batch
      will be exactly 61 promotions and 0 no-ops
  C6  store shape: 112 notes / 211 mappings / high 176 / medium 34 / low 1
  C7  corpus-architecture stat: 69/112 notes carry 2+ codes
  C8  VLM archive: 21 verdict JSONs, codes exactly matching the P6a queue
  C9  git provenance: HEAD is the reviewed commit (0ec4c89), tree clean

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

import c10_pr_review_verdicts as VR  # noqa: E402  (review record)
import c10_promote  # noqa: E402  (production promoter)

REPORTS = HERE.parent / "graph" / "reports"
SHEET = REPORTS / "PHASE2_PR_REVIEW_SHEET.md"
JSON_OUT = REPORTS / "C10_RATIFICATION_AUDIT.json"
MD_OUT = REPORTS / "C10_RATIFICATION_AUDIT.md"
EXPECTED_HEAD = "0ec4c89"

checks = []


def check(cid, name, ok, detail=""):
    checks.append({"id": cid, "name": name, "status": "PASS" if ok else "FAIL",
                   "detail": detail})
    print(f"[{'PASS' if ok else 'FAIL'}] {cid} {name}"
          + (f" — {detail}" if detail else ""))
    return ok


# ---------------------------------------------------------------------------
# C. load the store (production loader — also proves cross-file key uniqueness)
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


# ---------------------------------------------------------------------------
# A. the reviewed set, assembled from the verdict data exactly as the sheet
#    generator defines it (queue origin tracked for the report)
# ---------------------------------------------------------------------------
pairs_origin: dict[tuple[str, str], str] = {}
unresolved: list[str] = []
dupes: list[str] = []


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

reviewed = set(pairs_origin)

verdict_strings = ([x["verdict"] for x in VR.P1 + VR.P2 + VR.P5 + VR.P3]
                   + ["CONFIRM"])  # the P4 S1-c addition
P6A_OK = {"OK", "OK (prior)", "FLAG→OK"}  # (prior) = carried spot-check
all_confirm = (all(v.strip().upper().startswith("CONFIRM")
                   for v in verdict_strings)
               and all(s in P6A_OK for _c, _f, s, _d in VR.P6A)
               and all(c == "PASS" for _c, _f, c, _d in VR.P6B))
bad_verdicts = [v for v in verdict_strings
                if not v.strip().upper().startswith("CONFIRM")]

check("C1", "review record resolves to 61 distinct reviewed pairs, all CONFIRM",
      len(reviewed) == 61 and all_confirm and not unresolved and not dupes,
      (f"{len(reviewed)} pairs; verdicts scanned: "
       f"{len(P1 := VR.P1) + len(VR.P2) + len(VR.P5) + len(VR.P3) + 1} "
       f"+ {len(VR.P6A)} P6a + {len(VR.P6B)} P6b"
       + (f"; UNRESOLVED: {unresolved}" if unresolved else "")
       + (f"; DUPES: {dupes}" if dupes else "")
       + (f"; NON-CONFIRM VERDICTS: {bad_verdicts}" if bad_verdicts else "")))

# ---------------------------------------------------------------------------
# B. the staged §11 command, parsed from the on-disk sheet
# ---------------------------------------------------------------------------
text = SHEET.read_text(encoding="utf-8")
sec = text.split("## 11. Staged operator ratification", 1)[1]
bash = sec.split("```bash", 1)[1].split("```", 1)[0]
joined = bash.replace("\\\n", " ")
tokens = shlex.split(joined)
specs = [t for i, t in enumerate(tokens) if i > 0 and tokens[i - 1] == "--map"]
by = tokens[tokens.index("--by") + 1] if "--by" in tokens else None
date = tokens[tokens.index("--date") + 1] if "--date" in tokens else None

check("C2", "sheet §11 stages exactly 61 distinct --map specs",
      len(specs) == 61 and len(set(specs)) == 61,
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

check("C3", "production resolver resolves all 61 specs unambiguously "
      "(no code-wide promotion)",
      resolver_fail is None and len(staged) == 61 and len(set(staged)) == 61,
      (f"{len(bare)} bare CODE specs (each code on exactly one note), "
       f"{len(frag_specs)} CODE@FRAGMENT specs; 61 distinct (code, note) "
       f"targets" + (f"; PROMOTER WOULD REFUSE: {resolver_fail}"
                     if resolver_fail else "")))

# ---------------------------------------------------------------------------
# C4/C5. bijection + safety
# ---------------------------------------------------------------------------
a_minus_b = sorted(f"{c} @ {Path(n).stem}" for c, n in reviewed - set(staged))
b_minus_a = sorted(f"{c} @ {Path(n).stem}" for c, n in set(staged) - reviewed)

check("C4a", "every reviewed pair is staged by the command (completeness)",
      not a_minus_b,
      f"{61 - len(a_minus_b)}/61 staged" + (f"; MISSING: {a_minus_b}"
                                            if a_minus_b else ""))
check("C4b", "every staged target is a reviewed pair (no unreviewed "
      "promotion)",
      not b_minus_a,
      f"{61 - len(b_minus_a)}/61 reviewed" + (f"; UNREVIEWED: {b_minus_a}"
                                              if b_minus_a else ""))

promoted_now = [k for k, m in all_pairs.items()
                if isinstance(m.get("validation"), dict)
                and m["validation"].get("validation_status") == "HUMAN_VALIDATED"]
staged_ok_state = all(all_pairs[k].get("validation") is None
                      or all_pairs[k]["validation"].get("validation_status")
                      == "SUGGESTED" for k in set(staged) if k in all_pairs)
check("C5", "pre-state: 0 promoted / all 211 SUGGESTED — batch = exactly 61 "
      "promotions, 0 no-ops",
      len(promoted_now) == 0 and staged_ok_state and set(staged) <= set(all_pairs),
      f"promoted on disk: {len(promoted_now)}; all 61 targets in SUGGESTED "
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

check("C6", "store shape: 112 notes / 211 mappings / 176 high / 34 medium / "
      "1 low",
      n_notes == 112 and n_maps == 211 and conf["high"] == 176
      and conf["medium"] == 34 and conf["low"] == 1,
      f"{n_notes} notes / {n_maps} mappings / {conf}")

check("C7", "corpus stat: 69/112 notes carry 2+ codes (contributory "
      "many-to-many is the corpus shape)",
      multi == 69, f"{multi}/112")

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
                        timeout=15).stdout.strip()
    # this audit is additive-only: its own artifacts (script + 2 reports)
    # must not count as pre-existing dirtiness
    self_artifacts = {"scripts/c10_ratify_audit.py",
                      "graph/reports/C10_RATIFICATION_AUDIT.json",
                      "graph/reports/C10_RATIFICATION_AUDIT.md"}
    foreign = [ln for ln in st.splitlines()
               if ln[3:].strip() not in self_artifacts]
    dirty = "clean" if not foreign else f"dirty ({len(foreign)} foreign files)"
except Exception as e:  # git not decisive — don't fail the audit on it
    dirty = f"unavailable ({e})"
check("C9", f"git provenance: HEAD {EXPECTED_HEAD}…, tree clean",
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
               "verdict": "CONFIRM (AI review pass 2026-09-11)"}
              for c, n in sorted(reviewed)]

report = {
    "audit": "T-C10 pre-ratification reconciliation (read-only)",
    "generated": datetime.date.today().isoformat(),
    "operator_advisor_condition": (
        "machine-verifiable reconciliation of the 61 ratification targets "
        "against the review sheet: exact note->SpecificationPoint identity, "
        "no unreviewed mapping promoted"),
    "repo_head": head or "unknown",
    "sheet": str(SHEET.relative_to(HERE.parent)),
    "verdict": verdict,
    "checks": checks,
    "stats": {"notes": n_notes, "mappings": n_maps, "confidence": conf,
              "promoted_before": len(promoted_now),
              "notes_with_2plus_codes": multi, "vlm_files": len(vlm_codes),
              "command_specs": len(specs),
              "bare_code_specs": len(bare), "fragment_specs": len(frag_specs),
              "command_by": by, "command_date": date},
    "reviewed_pairs": pairs_json,
    "conclusion": (
        "The staged 61-spec c10_promote.py batch in PHASE2_PR_REVIEW_SHEET.md "
        "§11 promotes exactly the 61 AI-reviewed CONFIRM mappings — exact "
        "(note, code) identity proven, zero unreviewed or code-wide "
        "promotions, zero ambiguity, store pre-state 0 promoted / 211 "
        "SUGGESTED. The operator may execute the batch as staged." )
        if verdict == "PASS" else
        "DISCREPANCIES FOUND — see checks; do not run the batch until fixed.",
}

JSON_OUT.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8")

md = ["<!-- c10-ratify-audit-" + datetime.date.today().isoformat() + " -->",
      f"# T-C10 — Pre-Ratification Reconciliation Audit "
      f"({datetime.date.today().isoformat()}) — **{verdict}**", "",
      "Read-only audit executing the operator-advisor's condition before "
      "the staged batch: generator `scripts/c10_ratify_audit.py` "
      "(machine record: `C10_RATIFICATION_AUDIT.json`).", "",
      "| # | check | status | detail |", "|---|---|---|---|"]
for c in checks:
    md.append(f"| {c['id']} | {c['name']} | **{c['status']}** | "
              f"{c['detail'][:160]} |")
md += ["", "## The 61 exact ratification identities", "",
       "Every pair below is an AI-reviewed CONFIRM (review record: "
       "`scripts/c10_pr_review_verdicts.py`, rendered in "
       "PHASE2_PR_REVIEW_SHEET.md §2–§8) and resolves, via the production "
       "`c10_promote.py` resolver, to exactly the staged §11 spec:", "",
       "| # | code | note (stem) | queue | confidence |", "|---:|---|---|---|---|"]
for i, p in enumerate(pairs_json, 1):
    md.append(f"| {i} | {p['code']} | {p['note_stem']} | {p['queue']} | "
              f"{p['confidence']} |")
md += ["", report["conclusion"], "",
       f"Provenance: repo HEAD `{head or 'unknown'}` (the commit the "
       f"advisor reviewed); tree {dirty} before this audit's report files.",
       "", "After the operator runs the §11 command, those 61 mappings "
       "become HUMAN_VALIDATED (validated_by `operator`) — a distinct state "
       "from this AI CONFIRM, per the provenance chain.", ""]
MD_OUT.write_text("\n".join(md), encoding="utf-8")

print(f"\nVERDICT: {verdict}")
print(f"report: {JSON_OUT.relative_to(HERE.parent)}")
print(f"report: {MD_OUT.relative_to(HERE.parent)}")
sys.exit(0 if verdict == "PASS" else 1)
