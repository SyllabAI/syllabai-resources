#!/usr/bin/env python3
"""
T-C11 session 45 — c11_verdict_apply.py: §7 decision-record re-authoring that
applies the operator's session-44 verdicts (scripts/c11_review_verdicts.yaml)
to the REVIEW-STATE layer of scripts/c11_pilot_decisions.yaml.

Scope (the §7 / §8 sanctioned re-authoring pathway — session-41 precedent):
  * E-08  (REACTING-MASS REQUIRES_PREREQUISITE EQ-SYMBOL):   new operator_decision HOLD block
  * E-26  (MOLAR-GAS-VOL EXPLAINED_BY AVOGADRO-LAW):         PENDING (session 41) -> HOLD (session 44)
  * E-29  (MIS-EQ-SUBSCRIPT REMEDIATED_BY CONSERVATION-MASS): PENDING (session 41) -> HOLD (session 44)
  * N-08  (AVOGADRO-CONST): enrichment-scoping operator_decision CONFIRM block
  * N-27  (AVOGADRO-LAW):   enrichment-scoping operator_decision CONFIRM block
  * N-14  (THEOR-YIELD):    alias disposition — 'maximum yield' moves from
    `aliases` (the corpus-evidenced / merge-input track) to the NEW marked
    field `retrieval_only_aliases` (retrieval-only / unevidenced track, the
    operator's RETRIEVAL_EXEMPT dual-track policy) + an operator_decision
    block recording the disposition constraints.

What this script NEVER does:
  * never sets validation_status (blocks are review state only, §7; they are
    not in EDGE_KEYS/NODE_KEYS and never reach graph/*.yaml);
  * never promotes anything (§18 promotions live in
    scripts/c11_promotions.yaml, written only by scripts/c11_promote.py);
  * never touches evidence quotes, provenance, confidence, held candidates.

Fail-closed: every edit is anchored on byte-exact pre-state text; any drift,
duplication or missing anchor aborts BEFORE the file is written.
"""
from __future__ import annotations

import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
DEC = HERE / "c11_pilot_decisions.yaml"

E08 = ("4CH1-CON-REACTING-MASS", "REQUIRES_PREREQUISITE", "4CH1-CON-EQ-SYMBOL")
E26 = ("4CH1-CON-MOLAR-GAS-VOL", "EXPLAINED_BY", "4CH1-CON-AVOGADRO-LAW")
E29 = ("4CH1-MIS-EQ-SUBSCRIPT", "REMEDIATED_BY", "4CH1-CON-CONSERVATION-MASS")
N08, N27, N14 = "4CH1-CON-AVOGADRO-CONST", "4CH1-CON-AVOGADRO-LAW", "4CH1-CON-THEOR-YIELD"


def die(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def sq(s: str) -> str:
    """Single-quoted YAML scalar with '' escaping (file house style)."""
    return "'" + s.replace("'", "''") + "'"


def _ends_block(l: str) -> bool:
    """A line that terminates a record block: the next '- ' record, a
    column-0 comment (section separator), or any column-0 key (e.g. 'edges:')."""
    s = l.strip()
    return bool(s) and (l.startswith("- ") or l.startswith("#")
                        or not l.startswith(" "))


def find_edge_block(lines: list, src: str, rel: str, tgt: str):
    """(start, end) line indexes of the authored-edge block, end exclusive."""
    for i, l in enumerate(lines):
        if (l.rstrip("\n") == f"- source: {src}"
                and lines[i + 1].rstrip("\n") == f"  relation: {rel}"
                and lines[i + 2].rstrip("\n") == f"  target: {tgt}"):
            j = i + 1
            while j < len(lines) and not _ends_block(lines[j]):
                j += 1
            return i, j
    die(f"edge block not found: {src} {rel} {tgt}")


def find_node_block(lines: list, code: str):
    for i, l in enumerate(lines):
        if l.rstrip("\n") == f"- code: {code}":
            j = i + 1
            while j < len(lines) and not _ends_block(lines[j]):
                j += 1
            return i, j
    die(f"node block not found: {code}")


def block_has_od(lines: list, start: int, end: int) -> bool:
    return any(l.rstrip("\n") == "  operator_decision:"
               for l in lines[start:end])


# --- the new operator_decision blocks (session-44 decisions, session-45 applied) ---

OD_E08 = """  operator_decision:
    verdict: HOLD
    decided_by: operator
    decided_date: '2026-09-12'
    review_reference: 'scripts/c11_review_verdicts.yaml (session 44, row E-08)'
    reasons:
    - 'Granularity problem: evidence supports interpreting/using a balanced equation, but does not necessarily support the broader EQ-SYMBOL concept as currently modeled, particularly if that node includes writing/balancing the equation.'
    note: 'Operator HOLD (session 44, 2026-09-12), recorded verbatim in scripts/c11_review_verdicts.yaml row E-08; applied here session 45 via the sanctioned §7 re-authoring pathway. The edge stays SUGGESTED in the graph and is NOT eligible for promotion.'
""".splitlines(keepends=True)

OD_E26 = """  operator_decision:
    verdict: HOLD
    decided_by: operator
    decided_date: '2026-09-12'
    review_reference: 'scripts/c11_review_verdicts.yaml (session 44, row E-26)'
    reasons:
    - 'Do not promote the EXPLAINED_BY -> AVOGADRO-LAW relationship merely from general scientific knowledge.'
    - 'The current evidence does not establish that explanatory relationship strongly enough.'
    note: 'Operator HOLD (session 44, 2026-09-12), settling the session-41 PENDING medium-confidence presentation (FP-1: the anchored quote supports molar-volume -> formula-triangle, not law -> molar-volume; the law -> molar-volume link rests on section adjacency). The edge stays SUGGESTED in the graph and is NOT eligible for promotion. Block updated from PENDING to HOLD session 45 via the sanctioned §7 re-authoring pathway.'
""".splitlines(keepends=True)

OD_E29 = """  operator_decision:
    verdict: HOLD
    decided_by: operator
    decided_date: '2026-09-12'
    review_reference: 'scripts/c11_review_verdicts.yaml (session 44, row E-29)'
    reasons:
    - 'Do not promote REMEDIATED_BY -> CONSERVATION-MASS merely because conservation of mass is conceptually relevant.'
    - 'The source evidence does not explicitly establish that remediation relationship strongly enough.'
    note: 'Operator HOLD (session 44, 2026-09-12), settling the session-41 PENDING medium-confidence presentation (the tip corrective argument is substance-identity, not conservation; CON-CONSERVATION-MASS was the best available in-slice approximation). The edge stays SUGGESTED in the graph and is NOT eligible for promotion. Block updated from PENDING to HOLD session 45 via the sanctioned §7 re-authoring pathway.'
""".splitlines(keepends=True)

OD_N08 = f"""  operator_decision:
    verdict: CONFIRM
    decided_by: operator
    decided_date: '2026-09-12'
    review_reference: 'scripts/c11_review_verdicts.yaml (session 44, row N-08)'
    reasons:
    - 'CONFIRM as an enrichment concept: useful to the concept model but not itself necessarily an explicit demanded concept in 4CH1-1.27.'
    note: 'Operator enrichment scoping (session 44, 2026-09-12): the node keeps its ENRICHMENT role @ 4CH1-1.27. Do NOT convert this enrichment note into a stronger syllabus-authority claim. Node confirmation is review state only (nodes have no §18 promotion pathway — deferred to the expansion round) and this block is never emitted into graph/*.yaml. Applied session 45 via the sanctioned §7 re-authoring pathway.'
""".splitlines(keepends=True)

OD_N27 = f"""  operator_decision:
    verdict: CONFIRM
    decided_by: operator
    decided_date: '2026-09-12'
    review_reference: 'scripts/c11_review_verdicts.yaml (session 44, row N-27)'
    reasons:
    - 'CONFIRM as an enrichment concept: the corpus substantively teaches the idea, while the exact 1.35C wording does not necessarily explicitly demand the named law.'
    note: 'Operator enrichment scoping (session 44, 2026-09-12): the node keeps its ENRICHMENT role @ 4CH1-1.35C. Do NOT convert this enrichment note into a stronger syllabus-authority claim. Node confirmation is review state only (nodes have no §18 promotion pathway — deferred to the expansion round) and this block is never emitted into graph/*.yaml. Applied session 45 via the sanctioned §7 re-authoring pathway.'
""".splitlines(keepends=True)

OD_N14 = f"""  operator_decision:
    verdict: CONFIRM
    decided_by: operator
    decided_date: '2026-09-12'
    review_reference: 'scripts/c11_review_verdicts.yaml (session 44, node N-14 + alias_dispositions)'
    reasons:
    - 'CONFIRM the node under ratified OD-1 (yield triple stays split).'
    - 'Alias disposition KEEP: maximum yield is NOT present in the source corpus phrase evidence (0 occurrences — session-43 alias audit); it remains only as a retrieval-only synonym/alias, explicitly marked retrieval-only / unevidenced.'
    note: 'Operator alias disposition (session 44, 2026-09-12), applied session 45 via the sanctioned §7 re-authoring pathway: the alias moved from aliases (the corpus-evidenced / merge-input track) to retrieval_only_aliases (the marked retrieval-only track — the RETRIEVAL_EXEMPT dual-track alias policy). Do NOT claim that the corpus teaches or uses the phrase; do NOT add it to evidence quotes; do NOT alter the source note; not data corruption; the alias must never be used as evidence for a graph relationship. Re-evidencing or dropping the alias is an operator-only decision.'
""".splitlines(keepends=True)

HEADER_NOTE = """
#
# OPERATOR DECISIONS (session 44, applied session 45, 2026-09-12): the
# operator's review verdicts for the pilot surface live in
# scripts/c11_review_verdicts.yaml (operator-owned): 28 edge CONFIRM /
# 3 HOLD @ E-08 / E-26 / E-29 / 0 REJECT; 29 node CONFIRM; OD-1 + OD-2
# RATIFIED; alias policy RETRIEVAL_EXEMPT; 'maximum yield' KEEP
# retrieval-only/unevidenced. Session 45 applied them: the 28 confirmed
# edges were promoted via the §18 pathway (scripts/c11_promotions.yaml —
# the ONLY HUMAN_VALIDATED source; never this record); the 3 HOLDs are
# recorded below as operator_decision HOLD blocks (E-08 added; E-26/E-29
# updated from the session-41 PENDING presentations); the N-08/N-27
# enrichment scoping and the THEOR-YIELD alias disposition (maximum yield
# -> retrieval_only_aliases) are recorded as operator_decision blocks.
# Node CONFIRMs are review state only (no §18 node pathway). These blocks
# are never emitted into graph/*.yaml and can never carry HUMAN_VALIDATED.
""".splitlines(keepends=True)

HEADER_ANCHOR = ("# remains exclusively the c11_promotions.yaml / "
                 "c11_promote.py pathway (§18).\n")


def main() -> int:
    text = DEC.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)

    # ---- pre-state assertions (fail closed BEFORE any edit) ----------------
    if text.count("  aliases: [maximum yield]") != 1:
        die(f"pre-state: expected exactly 1 'aliases: [maximum yield]' line, "
            f"found {text.count('  aliases: [maximum yield]')}")
    if "retrieval_only_aliases" in text:
        die("pre-state: retrieval_only_aliases already present (double-apply?)")

    for src, rel, tgt in (E08, E26, E29):
        s, e = find_edge_block(lines, src, rel, tgt)
        od = block_has_od(lines, s, e)
        if (src, rel, tgt) == E08 and od:
            die("pre-state: E-08 already carries an operator_decision block")
        if (src, rel, tgt) in (E26, E29) and not od:
            die(f"pre-state: {src} {rel} {tgt} lost its session-41 PENDING block")
    for code in (N08, N27, N14):
        s, e = find_node_block(lines, code)
        if block_has_od(lines, s, e):
            die(f"pre-state: node {code} already carries an operator_decision "
                f"block (double-apply?)")

    dec = yaml.safe_load(text)
    if len(dec["edges"]) != 32 or len(dec["nodes"]) != 29 \
            or len(dec.get("held", [])) != 13:
        die("pre-state: unexpected store shape (32/29/13 expected)")
    if any(x.get("validation_status") == "HUMAN_VALIDATED"
           for x in dec["edges"] + dec["nodes"]):
        die("pre-state: HUMAN_VALIDATED in the decision record (anti-forgery)")
    for src, rel, tgt in (E08, E26, E29):
        s, e = find_edge_block(lines, src, rel, tgt)
        if not any(l.rstrip("\n") == "  validation_status: SUGGESTED"
                   for l in lines[s:e]):
            die(f"pre-state: {src} {rel} {tgt} is not SUGGESTED")

    # ---- edits (applied bottom-up so line indexes stay valid) --------------
    # 1. header note
    if text.count(HEADER_ANCHOR) != 1:
        die("edit 1: header anchor not unique")
    idx = next(i for i, l in enumerate(lines) if l == HEADER_ANCHOR)
    lines = lines[:idx + 1] + HEADER_NOTE + lines[idx + 1:]

    # 2. THEOR-YIELD alias -> retrieval_only_aliases (+ OD block)
    #    (insert the OD block FIRST at the block end, then split the alias
    #    line — splitting shifts the block end by +1)
    s, e = find_node_block(lines, N14)
    lines = lines[:e] + OD_N14 + lines[e:]
    ai = next(i for i, l in enumerate(lines)
              if l == "  aliases: [maximum yield]\n")
    lines[ai] = "  aliases: []\n  retrieval_only_aliases: [maximum yield]\n"

    # 3. N-27 / N-08 enrichment blocks
    for code, od in ((N27, OD_N27), (N08, OD_N08)):
        s, e = find_node_block(lines, code)
        lines = lines[:e] + od + lines[e:]

    # 4. E-29 / E-26 PENDING -> HOLD; E-08 new HOLD
    for (src, rel, tgt), od in ((E29, OD_E29), (E26, OD_E26), (E08, OD_E08)):
        s, e = find_edge_block(lines, src, rel, tgt)
        oi = next((i for i in range(s, e)
                   if lines[i].rstrip("\n") == "  operator_decision:"), None)
        if oi is not None:
            # sanity: the block being replaced must be the PENDING presentation
            # (exactly one operator_decision key inside this edge block)
            if sum(1 for k in range(s, e)
                   if lines[k].rstrip("\n") == "  operator_decision:") != 1:
                die(f"edit 4: {src} {rel} {tgt} carries more than one "
                    f"operator_decision key — refusing")
            lines = lines[:oi] + od + lines[e:]   # replace the whole OD block
        else:
            lines = lines[:e] + od + lines[e:]    # append at block end

    # ---- post-state validation ------------------------------------------------
    new_text = "".join(lines)
    # text-level duplicate-key guard (PyYAML silently keeps the LAST duplicate
    # key, so parse-level checks alone cannot catch this corruption class)
    if "    verdict: PENDING" in new_text:
        die("post-state: a PENDING verdict survived (replacement failed)")
    for (src, rel, tgt) in (E08, E26, E29):
        s2, e2 = find_edge_block(lines, src, rel, tgt)
        n_od = sum(1 for k in range(s2, e2)
                   if lines[k].rstrip("\n") == "  operator_decision:")
        if n_od != 1:
            die(f"post-state: {src} {rel} {tgt} carries {n_od} "
                f"operator_decision keys (expected exactly 1)")
    dec2 = yaml.safe_load(new_text)
    if len(dec2["edges"]) != 32 or len(dec2["nodes"]) != 29 \
            or len(dec2.get("held", [])) != 13:
        die("post-state: store shape changed (32/29/13 expected)")

    def edge_od(src, rel, tgt):
        return next(e["operator_decision"] for e in dec2["edges"]
                    if (e["source"], e["relation"], e["target"]) == (src, rel, tgt))

    def node_od(code):
        return next(n["operator_decision"] for n in dec2["nodes"]
                    if n["code"] == code)

    checks = [
        (edge_od(*E08)["verdict"] == "HOLD", "E-08 HOLD"),
        (edge_od(*E26)["verdict"] == "HOLD", "E-26 HOLD (was PENDING)"),
        (edge_od(*E29)["verdict"] == "HOLD", "E-29 HOLD (was PENDING)"),
        (node_od(N08)["verdict"] == "CONFIRM", "N-08 CONFIRM enrichment"),
        (node_od(N27)["verdict"] == "CONFIRM", "N-27 CONFIRM enrichment"),
        (node_od(N14)["verdict"] == "CONFIRM", "N-14 CONFIRM + alias disposition"),
        (node_od(N14) is not None
         and next(n for n in dec2["nodes"] if n["code"] == N14)["aliases"] == []
         and next(n for n in dec2["nodes"]
                  if n["code"] == N14)["retrieval_only_aliases"]
         == ["maximum yield"], "N-14 dual-track alias split"),
    ]
    for ok, name in checks:
        if not ok:
            die(f"post-state: {name} failed")

    if any(x.get("validation_status") == "HUMAN_VALIDATED"
           for x in dec2["edges"] + dec2["nodes"]):
        die("post-state: HUMAN_VALIDATED leaked into the decision record")
    # evidence/provenance/confidence untouched: every authored edge must still
    # carry the exact same non-review fields as before
    key = lambda e: (e["source"], e["relation"], e["target"])
    strip = lambda e: {k: v for k, v in e.items() if k != "operator_decision"}
    before = {key(e): strip(e) for e in dec["edges"]}
    after = {key(e): strip(e) for e in dec2["edges"]}
    if before != after:
        die("post-state: authored-edge non-review fields drifted")
    nb = {n["code"]: {k: v for k, v in n.items() if k not in
                      ("operator_decision", "aliases", "retrieval_only_aliases")}
          for n in dec["nodes"]}
    na = {n["code"]: {k: v for k, v in n.items() if k not in
                      ("operator_decision", "aliases", "retrieval_only_aliases")}
          for n in dec2["nodes"]}
    if nb != na:
        die("post-state: node non-review fields drifted")
    if sum(1 for n in dec2["nodes"] if n["code"] != N14
           and n.get("aliases") != next(m.get("aliases")
                                        for m in dec["nodes"]
                                        if m["code"] == n["code"])):
        die("post-state: unexpected alias change on other nodes")

    DEC.write_text(new_text, encoding="utf-8")
    print("APPLIED (§7 re-authoring, session 45):")
    print("  E-08  operator_decision HOLD (new, session-44 verdict)")
    print("  E-26  operator_decision PENDING -> HOLD (session-44 verdict)")
    print("  E-29  operator_decision PENDING -> HOLD (session-44 verdict)")
    print("  N-08  operator_decision CONFIRM (enrichment scoping)")
    print("  N-27  operator_decision CONFIRM (enrichment scoping)")
    print("  N-14  alias 'maximum yield' -> retrieval_only_aliases (dual-track)")
    print("        + operator_decision CONFIRM (alias disposition KEEP)")
    print("  header: session-44/45 operator-decisions note")
    print("next: extend NODE_KEYS in c11_concept_pilot.py to emit "
          "retrieval_only_aliases, then re-run the generator.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
