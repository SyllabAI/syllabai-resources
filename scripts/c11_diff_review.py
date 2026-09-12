#!/usr/bin/env python3
"""
T-C11 — c11_diff_review.py: diff-based batch approval front-end for the
pending §18 edge promotions (operator tooling; read-only until approve).

Problem it solves
-----------------
The pilot's remaining operator actions are per-row verdicts on 31 SUGGESTED
authored edges + 29 nodes (C11_OPERATOR_DECISIONS.json). Reading the review
sheet row-by-row and invoking c11_promote.py once per identity is slow. This
tool presents every pending item as the EXACT diff approval would apply to
graph/concept_edges.yaml, and turns an operator verdict into one batched
c11_promote.py invocation (a single gated generator re-run).

Presentation fidelity (the core property)
-----------------------------------------
The preview is NOT an approximation. The simulator re-emits
graph/concept_edges.yaml using the generator's own serialization contract
(yaml.safe_dump, sort_keys=False, width=100, allow_unicode=True, same header)
with the §18 promotion transformation applied:

  * validation_status: SUGGESTED -> HUMAN_VALIDATED
  * validated_by / validated_date inserted at validation_status's position
  * meta.promotion_record appended (only when promotions exist)
  * counts.promoted_edges / counts.human_validated_edges appended

Before showing ANY diff the tool re-emits the UNMODIFIED document and
byte-compares it to the file on disk; a mismatch (hand-edit, drift) is a hard
refusal. What the operator reads is byte-identical to what the gated G13
re-run will write — verified against a real c11_promote + generator run.

Approval pathway (unchanged, no gate bypassed)
----------------------------------------------
`approve` performs c11_promote.py's own pre-verifications (exact identity,
authored-only, held-candidate rejection, evidence byte-verification,
provenance completeness, attribution gate) and then invokes c11_promote.py
ONCE for the whole batch (single generator re-run = single G13 gate pass).
This tool never writes scripts/c11_promotions.yaml, never writes graph/*.
The 2 PENDING operator-decision edges are excluded from batch verbs unless
--include-pending is given (C11_OPERATOR_DECISIONS: "not promotable until
the operator explicitly decides" — the flag IS the explicit decision, and it
is recorded in the review_reference bundle). Nodes have no promotion pathway
yet (§18); they are presented for information only.

Usage
-----
  python3 scripts/c11_diff_review.py list
  python3 scripts/c11_diff_review.py show <id|#idx>... | all
  python3 scripts/c11_diff_review.py export [--out graph/reports/....md]
  python3 scripts/c11_diff_review.py approve <id|#idx>... [--dry-run]
  python3 scripts/c11_diff_review.py approve --all [--except <id|#idx>...]
                                           [--include-pending] [--dry-run]
                                           --by <operator> [--date YYYY-MM-DD]

  id = full edge identity 'SRC REL TGT' (preferred) or #N from `list`.

Exit 0 = success; 1 = fail-closed refusal (all reasons printed); 2 = usage.
"""
from __future__ import annotations

import argparse
import datetime
import difflib
import hashlib
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent

# Session-47 (§16 batch 1, 2026-09-12): the decision-record REGISTRY (pilot
# first, then each authorized §16 batch record) — same list as the
# generator's. The §18 front-end enumerates pending items over the MERGED
# authored-edge surface: the operator's batch-1 approval surface is exactly
# the batch-1 SUGGESTED edges.
# Session-49 (batch 2): the registry grows by c11_batch2_decisions.yaml
# Session-51 (batch 3): the registry grows by c11_batch3_decisions.yaml
# (the full S1 remainder batch, operator-commissioned session 51)
DECISION_FILES = ["c11_pilot_decisions.yaml", "c11_batch1_decisions.yaml",
                  "c11_batch2_decisions.yaml", "c11_batch3_decisions.yaml"]
PROMOTIONS = HERE / "c11_promotions.yaml"
GRAPH_EDGES = REPO / "graph" / "concept_edges.yaml"
GRAPH_NODES = REPO / "graph" / "concepts.yaml"
SPEC_POINTS = REPO / "graph" / "specification_points.yaml"

# Same vocabulary / gates as scripts/c11_promote.py (kept in lockstep).
RELATIONS = {"PART_OF", "REQUIRES_PREREQUISITE", "RELATED_TO", "MISCONCEPTION_OF",
             "EXPLAINED_BY", "REMEDIATED_BY", "COMMONLY_CONFUSED_WITH",
             "WRONG_ANSWER_PATTERN"}
ANCHOR_KINDS = {"NOTE", "SPEC", "MARK_SCHEME"}
BANDS = {"high", "medium", "low"}
PROV_KEYS = ("tier", "model_version", "extraction_pass", "derivation_method",
             "derivation_notes", "upstream", "generated_date")
RE_ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
AI_NAME_RE = re.compile(r"glm|super\s*z|gpt|claude|openai|anthropic|\bai\b"
                        r"|llm|agent|model|bot", re.I)

TRANS = {ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def norm(s: str) -> str:
    """T-C10 norm() convention (shared anti-hallucination normalisation)."""
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate(TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


def die(msgs) -> "None":
    if isinstance(msgs, str):
        msgs = [msgs]
    for m in msgs:
        print(f"FAIL: {m}", file=sys.stderr)
    sys.exit(1)


def ekey(e) -> str:
    return f"{e['source']} {e['relation']} {e['target']}"


# ---------------------------------------------------------------------------
# State loading + consistency
# ---------------------------------------------------------------------------
def load_state(base: Path = REPO) -> dict:
    """Load all inputs read-only. base is injectable for tests."""
    g_edges = base / "graph" / "concept_edges.yaml"
    g_nodes = base / "graph" / "concepts.yaml"
    g_spec = base / "graph" / "specification_points.yaml"
    # session-47: the decision-record REGISTRY (fail closed if any member is
    # missing — the graph must be reconcilable against its full registry)
    decisions_list = [base / "scripts" / f for f in DECISION_FILES]
    promotions = base / "scripts" / "c11_promotions.yaml"

    missing = [str(p.relative_to(base)) for p in
               [g_edges, g_nodes, g_spec, *decisions_list] if not p.exists()]
    if missing:
        die(f"required inputs missing: {', '.join(missing)}")

    dec = {"edges": [], "nodes": [], "held": [], "meta": {}}
    for dp in decisions_list:
        d = yaml.safe_load(dp.read_text(encoding="utf-8")) or {}
        dec.setdefault("edges", []).extend(d.get("edges") or [])
        dec.setdefault("nodes", []).extend(d.get("nodes") or [])
        dec.setdefault("held", []).extend(d.get("held") or [])
        dec.setdefault("meta", {})[str(dp.name)] = d.get("meta") or {}
    graph = yaml.safe_load(g_edges.read_text(encoding="utf-8"))
    nodes_doc = yaml.safe_load(g_nodes.read_text(encoding="utf-8"))
    spec = yaml.safe_load(g_spec.read_text(encoding="utf-8"))

    promo_raw = (yaml.safe_load(promotions.read_text(encoding="utf-8"))
                 if promotions.exists() else None)
    promo_entries = (promo_raw or {}).get("promotions") or []
    promoted = {(p["edge"]["source"], p["edge"]["relation"], p["edge"]["target"])
                for p in promo_entries}

    spec_by_code = {p["code"]: p for p in spec.get("specification_points", [])}
    nodes = nodes_doc.get("nodes", [])
    nodes_by_code = {n["code"]: n for n in nodes}

    st = {"base": base, "dec": dec, "graph": graph, "nodes": nodes,
          "nodes_by_code": nodes_by_code, "spec_by_code": spec_by_code,
          "promoted": promoted, "promo_count": len(promo_entries),
          "graph_text": g_edges.read_text(encoding="utf-8")}
    st["failures"] = consistency_failures(st)
    return st


def consistency_failures(st: dict) -> list:
    """Decision record <-> graph cross-checks (drift = hard refusal)."""
    fails = []
    authored = st["dec"].get("edges", [])
    g_authored = [e for e in st["graph"].get("edges", [])
                  if e["relation"] != "PART_OF"]
    a_ids = {ekey(e) for e in authored}
    g_ids = {ekey(e) for e in g_authored}
    if a_ids != g_ids:
        fails.append("authored-edge identity sets diverge between decision "
                     f"record and graph (only-in-decisions: "
                     f"{sorted(a_ids - g_ids)}; only-in-graph: "
                     f"{sorted(g_ids - a_ids)})")
    status_dec = {ekey(e): e["validation_status"] for e in authored}
    status_g = {ekey(e): e["validation_status"] for e in g_authored}
    # session-45 fix: model the §18 sanctioned transition. The decision
    # record is FROZEN and keeps SUGGESTED (anti-forgery G10/c11.13 — it can
    # never carry HUMAN_VALIDATED); the graph carries HUMAN_VALIDATED ONLY
    # through a promotion-store entry (st["promoted"], §18). Therefore
    # (dec=SUGGESTED, graph=HUMAN_VALIDATED, promoted) is CONSISTENT, not
    # drift. The forgery direction — graph HUMAN_VALIDATED with NO promotion
    # entry — still fails (as does any HUMAN_VALIDATED in the decisions).
    drifted = {}
    for k in a_ids & g_ids:
        sd, sg = status_dec[k], status_g[k]
        if sd == sg:
            continue
        if (sd == "SUGGESTED" and sg == "HUMAN_VALIDATED"
                and tuple(k.split()) in st["promoted"]):
            continue
        drifted[k] = (sd, sg)
    if drifted:
        fails.append(f"validation_status drifted decisions-vs-graph: {drifted}")
    n_dec, n_graph = len(st["dec"].get("nodes", [])), len(st["nodes"])
    if n_dec != n_graph:
        fails.append(f"node count drifted: decisions={n_dec} graph={n_graph}")
    return fails


def fingerprint(st: dict) -> str:
    lines = sorted(f"{e['source']}|{e['relation']}|{e['target']}|"
                   f"{e['validation_status']}"
                   for e in st["dec"].get("edges", []))
    lines.append(f"promotions={st['promo_count']}")
    lines.append(f"nodes={len(st['nodes'])}")
    return hashlib.sha256("\n".join(lines).encode()).hexdigest()[:12]


# ---------------------------------------------------------------------------
# Pending-item enumeration
# ---------------------------------------------------------------------------
def actionable_edges(st: dict) -> list:
    """All authored edges that still need an operator verdict, sorted by
    identity. Each item: identity/edge/actionable/flag/note/already_promoted."""
    out = []
    for e in sorted(st["dec"].get("edges", []), key=ekey):
        ident = ekey(e)
        od = e.get("operator_decision") or {}
        verdict = od.get("verdict")
        note = None
        if tuple(ident.split()) in st["promoted"]:
            continue  # already promoted — not pending
        if e["validation_status"] == "REVIEW_REQUIRED":
            note = (f"decided: operator {verdict or '?'} "
                    f"({od.get('decided_date', '')}) — stays REVIEW_REQUIRED, "
                    f"not promotable (§18)")
            out.append({"identity": ident, "edge": e, "actionable": False,
                        "flag": "DECIDED", "note": note})
            continue
        if e["validation_status"] != "SUGGESTED":
            out.append({"identity": ident, "edge": e, "actionable": False,
                        "flag": "OTHER", "note": f"status "
                        f"{e['validation_status']!r} is not actionable here"})
            continue
        if verdict == "PENDING":
            out.append({"identity": ident, "edge": e, "actionable": True,
                        "flag": "PENDING",
                        "note": "operator_decision block PENDING "
                                "(medium-confidence judgment; requires "
                                "--include-pending = the explicit decision)"})
            continue
        if verdict in ("REJECT", "HOLD"):
            out.append({"identity": ident, "edge": e, "actionable": False,
                        "flag": "DECIDED", "note": f"operator {verdict} "
                        f"({od.get('decided_date', '')})"})
            continue
        out.append({"identity": ident, "edge": e, "actionable": True,
                    "flag": None, "note": None})
    return out


def pending_items(st: dict) -> list:
    return [it for it in actionable_edges(st) if it["actionable"]]


def node_items(st: dict) -> list:
    """Nodes awaiting verdicts — informational (no §18 pathway yet)."""
    return [n for n in sorted(st["nodes"], key=lambda x: x["code"])
            if n["validation_status"] == "SUGGESTED"]


def spec_refs(st: dict, code: str) -> list:
    """Spec-point attachments for a node code; or the point itself."""
    n = st["nodes_by_code"].get(code)
    if n:
        return [(a["code"], a.get("role", ""),
                 st["spec_by_code"].get(a["code"], {}).get("official_wording",
                                                           ""))
                for a in n.get("spec_points", [])]
    if code in st["spec_by_code"]:
        p = st["spec_by_code"][code]
        return [(code, "", p.get("official_wording", ""))]
    return []


# ---------------------------------------------------------------------------
# Diff simulation (generator's own emission contract)
# ---------------------------------------------------------------------------
DUMP_KW = dict(allow_unicode=True, sort_keys=False, width=100,
               default_flow_style=False)


def split_header(text: str):
    idx = text.index("\nmeta:\n")
    return text[:idx + 1], text[idx + 1:]


def roundtrip_guard(st: dict) -> None:
    """Byte-fidelity guard: load->dump of the CURRENT file must reproduce it.
    Otherwise the simulation would lie — hard refusal."""
    header, body = split_header(st["graph_text"])
    doc = yaml.safe_load(body)
    if yaml.safe_dump(doc, **DUMP_KW) != body:
        die("graph/concept_edges.yaml is not byte-reproducible under the "
            "generator's serialization contract (hand-edit or foreign "
            "writer suspected). Refusing to preview diffs that could not "
            "be trusted. Restore the generated file via the gated "
            "generator re-run.")


def promote_edge_rec(e: dict, by: str, date: str) -> dict:
    """§18 transformation, keys kept in the generator's emission order."""
    rec = {}
    for k, v in e.items():
        if k == "validation_status":
            rec[k] = "HUMAN_VALIDATED"
            rec["validated_by"] = by
            rec["validated_date"] = date
        else:
            rec[k] = v
    return rec


def simulate_promotion(st: dict, batch: list, by: str, date: str):
    """Apply §18 to the loaded document; return (old_text, new_text)."""
    doc = yaml.safe_load(split_header(st["graph_text"])[1])
    batch_set = {tuple(i.split()) for i in batch}
    changed = 0
    for idx, e in enumerate(doc["edges"]):
        if (e["source"], e["relation"], e["target"]) in batch_set:
            # replace (not update) so the validated_by/date keys land at
            # validation_status's position, exactly like the generator's
            # edge_out() emission order
            doc["edges"][idx] = promote_edge_rec(e, by, date)
            changed += 1
    if changed != len(batch_set):
        die(f"simulation mismatch: {changed} of {len(batch_set)} batch "
            f"identities found in graph/concept_edges.yaml")
    meta = doc["meta"]
    counts = meta["counts"]
    counts["promoted_edges"] = sum(1 for e in doc["edges"]
                                   if e["validation_status"] == "HUMAN_VALIDATED")
    counts["human_validated_edges"] = counts["promoted_edges"]
    meta["promotion_record"] = "scripts/c11_promotions.yaml"
    header = split_header(st["graph_text"])[0]
    return st["graph_text"], header + yaml.safe_dump(doc, **DUMP_KW)


def diff_lines(old: str, new: str, n: int = 3):
    return list(difflib.unified_diff(old.splitlines(keepends=True),
                                     new.splitlines(keepends=True),
                                     fromfile="graph/concept_edges.yaml (before)",
                                     tofile="graph/concept_edges.yaml (after)",
                                     n=n))


# --- manual hunk construction ----------------------------------------------
# The §18 transformation is exactly known, so hunks are constructed directly
# (git-style canonical rendering) instead of relying on difflib's anchoring,
# which can group the status replacement + insertions differently from
# git's xdiff. Net file content is identical either way; this is about the
# operator being able to diff the preview against `git diff` 1:1.
CTX = 3


def _find_edge_status_line(old_lines: list, identity: str):
    """Line index of the edge's `validation_status:` in the graph file."""
    src, rel, tgt = identity.split()
    starts = [i for i, l in enumerate(old_lines)
              if l.rstrip("\n") == f"- source: {src}"]
    for s in starts:
        e = next((j for j in range(s + 1, len(old_lines))
                  if old_lines[j].startswith("- source: ")), len(old_lines))
        blk = old_lines[s:e]
        if f"  relation: {rel}\n" in blk and f"  target: {tgt}\n" in blk:
            j = next(k for k in range(s, e)
                     if old_lines[k].rstrip("\n") ==
                     "  validation_status: SUGGESTED")
            return j
    return None


def _fmt_hunk(a_start: int, a_count: int, b_start: int, b_count: int,
              body: list, old_lines: list, start_idx: int) -> list:
    fn = _funcname(old_lines, start_idx)
    tail = f" {fn}" if fn else ""
    return [f"@@ -{a_start},{a_count} +{b_start},{b_count} @@{tail}\n"] + body


def _funcname(old_lines: list, start_idx: int) -> str:
    """git's default function-context line: nearest preceding line that
    starts with [A-Za-z_$] (here: the top-level `meta:` / `edges:` keys)."""
    for k in range(start_idx, -1, -1):
        if re.match(r"[A-Za-z_$]", old_lines[k]):
            return old_lines[k].rstrip("\n")
    return ""


def edge_hunk_manual(st: dict, identity: str, by: str, date: str,
                     offset: int = 0) -> list:
    """Git-style hunk: `validation_status: SUGGESTED` replaced in place by
    HUMAN_VALIDATED + validated_by + validated_date, with CTX context.
    offset = cumulative new-file line drift caused by earlier hunks."""
    old_lines = st["graph_text"].splitlines(keepends=True)
    j = _find_edge_status_line(old_lines, identity)
    if j is None:
        die(f"{identity}: SUGGESTED block not found in "
            f"graph/concept_edges.yaml — cannot render the preview")
    before = old_lines[max(0, j - CTX):j]
    after = old_lines[j + 1:j + 1 + CTX]
    first = j - len(before)              # 0-based index of first hunk line
    body = [" " + l for l in before]
    body.append("-" + old_lines[j])
    body.append("+  validation_status: HUMAN_VALIDATED\n")
    body.append(f"+  validated_by: {by}\n")
    body.append(f"+  validated_date: '{date}'\n")
    body += [" " + l for l in after]
    return _fmt_hunk(first + 1, len(before) + 1 + len(after),
                     first + 1 + offset, len(before) + 3 + len(after),
                     body, old_lines, first)


def meta_hunk_delta(st: dict) -> int:
    """Net new-file line delta of the meta hunk for the CURRENT state:
    3 in the pre-promotion state (two counts + promotion_record inserted),
    0 in the post-promotion state (counts changed in place 28 -> 28+k; the
    promotion_record already exists). Session-47 fix: the edge hunks'
    new-file offsets must match the meta hunk's real net delta."""
    old_lines = st["graph_text"].splitlines(keepends=True)
    has_promoted = any(l.rstrip("\n").startswith("    promoted_edges: ")
                       for l in old_lines)
    return 0 if has_promoted else 3


def meta_hunk_manual(st: dict, k_batch: int) -> list:
    """Git-style hunk for the file-level changes: counts.promoted_edges /
    human_validated_edges after review_required_edges, and
    meta.promotion_record just before the top-level `edges:` key."""
    old_lines = st["graph_text"].splitlines(keepends=True)
    n_rr = sum(1 for e in st["graph"]["edges"]
               if e["validation_status"] == "REVIEW_REQUIRED")
    i = next(k for k, l in enumerate(old_lines)
             if l.rstrip("\n") == f"    review_required_edges: {n_rr}")
    j = next(k for k, l in enumerate(old_lines) if l.rstrip("\n") == "edges:")
    if j <= i:
        die("unexpected graph layout: `edges:` precedes counts — refusing "
            "to render the meta preview")
    # session-47 fix: the live graph may ALREADY carry promotions (the
    # session-45 state: counts.promoted_edges=28 + meta.promotion_record).
    # In that state the generator's G13 re-run OVERWRITES the counts (one
    # occurrence each) and keeps the existing promotion_record — so the
    # preview must be a CHANGE hunk, not an insertion (the old code rendered
    # duplicate keys, which is not what the gated apply writes).
    old_n = next((int(l.split(":")[1]) for l in old_lines
                  if l.rstrip("\n").startswith("    promoted_edges: ")), None)
    if old_n is not None:
        # post-promotion state: change 28 -> 28 + k_batch (promotion_record
        # already present — nothing inserted for it)
        k2 = next(kk for kk, l in enumerate(old_lines)
                  if l.rstrip("\n") == f"    human_validated_edges: {old_n}")
        lo, hi = min(i, k2), max(i, k2) + 1
        before = old_lines[lo - CTX:lo] or old_lines[:lo]
        after = old_lines[hi:hi + CTX]
        first = lo - len(before)
        body = [" " + l for l in before]
        body.append(f"-    promoted_edges: {old_n}\n")
        body.append(f"-    human_validated_edges: {old_n}\n")
        body.append(f"+    promoted_edges: {old_n + k_batch}\n")
        body.append(f"+    human_validated_edges: {old_n + k_batch}\n")
        body += [" " + l for l in after]
        a_count = len(before) + 2 + len(after)
        return _fmt_hunk(first + 1, a_count, first + 1, a_count + 2,
                         body, old_lines, first)

    # pre-promotion state (original behavior): insert the promotion keys
    before = old_lines[max(0, i - CTX + 1):i + 1]
    mid = old_lines[i + 1:j]                       # (normally empty)
    after = old_lines[j:j + CTX]
    first = i - len(before) + 1          # 0-based index of first hunk line
    body = [" " + l for l in before]
    body.append(f"+    promoted_edges: {k_batch}\n")
    body.append(f"+    human_validated_edges: {k_batch}\n")
    body += [" " + l for l in mid]
    body.append("+  promotion_record: scripts/c11_promotions.yaml\n")
    body += [" " + l for l in after]
    a_count = len(before) + len(mid) + len(after)
    return _fmt_hunk(first + 1, a_count, first + 1, a_count + 3,
                     body, old_lines, first)


def edge_hunks(st: dict, identity: str, by: str, date: str):
    """(edge hunks, meta hunks) for a single promotion. The meta hunk is
    positioned earlier in the file and always precedes the edge hunk, so the
    edge hunk carries the +3 new-file offset the meta hunk introduces."""
    return edge_hunk_manual(st, identity, by, date,
                            offset=meta_hunk_delta(st)), \
        meta_hunk_manual(st, 1)


def batch_hunks(st: dict, batch: list, by: str, date: str) -> list:
    """All hunks for a batch, in git's file order: the meta hunk first,
    then one hunk per promoted edge in file position order, each carrying
    the cumulative new-file offset (+3 meta, +2 per edge)."""
    old_lines = st["graph_text"].splitlines(keepends=True)
    located = []
    for ident in batch:
        j = _find_edge_status_line(old_lines, ident)
        if j is None:
            die(f"{ident}: SUGGESTED block not found in "
                f"graph/concept_edges.yaml — cannot render the preview")
        located.append((j, ident))
    located.sort()
    out = list(meta_hunk_manual(st, len(set(batch))))
    off = meta_hunk_delta(st)
    for _j, ident in located:
        out += edge_hunk_manual(st, ident, by, date, offset=off)
        off += 2
    return out


# ---------------------------------------------------------------------------
# Pre-verification (mirrors c11_promote.py; fail closed BEFORE anything)
# ---------------------------------------------------------------------------
def preverify(st: dict, items: list, include_pending: bool) -> list:
    fails = []
    held = st["dec"].get("held", [])
    authored = {ekey(e): e for e in st["dec"].get("edges", [])}
    base: Path = st["base"]
    for it in items:
        ident, e = it["identity"], it["edge"]
        where = f"edge {ident}"
        if ident not in authored:
            # held-candidate diagnosis ONLY for non-authored identities —
            # exactly c11_promote.py's / G13's structure (session-45 fix:
            # the substring hint fired on AUTHORED edges too, where it can
            # only produce false positives — an identity is either authored
            # or a held candidate, never both; e.g. CONFIRM edge
            # CON-EMP-MOL-CALC -> CON-MOLE was mis-flagged as HELD-06 because
            # 'CON-MOLE' is a substring of HELD-06's 'CON-MOLE-MASS-CONV')
            s_, t_ = (e["source"].removeprefix("4CH1-"),
                      e["target"].removeprefix("4CH1-"))
            hit = next((h.get("id") for h in held
                        if s_ in str(h.get("candidate", ""))
                        and t_ in str(h.get("candidate", ""))
                        and e["relation"] in str(h.get("candidate", ""))),
                       None)
            if hit:
                fails.append(f"{where}: is held candidate {hit} — "
                             f"held/rejected candidates are not promotable")
                continue
            fails.append(f"{where}: not an authored edge")
            continue
        if e["relation"] == "PART_OF":
            fails.append(f"{where}: PART_OF is derived — not promotable (§18)")
            continue
        if e["validation_status"] == "REVIEW_REQUIRED":
            fails.append(f"{where}: REVIEW_REQUIRED is not promotable")
            continue
        if e["validation_status"] != "SUGGESTED":
            fails.append(f"{where}: status {e['validation_status']!r} not "
                         f"promotable")
            continue
        od = e.get("operator_decision") or {}
        if od.get("verdict") == "PENDING" and not include_pending:
            fails.append(f"{where}: operator_decision PENDING — excluded by "
                         f"default; pass --include-pending to record the "
                         f"explicit operator decision")
        anchors = e.get("evidence") or []
        if not anchors:
            fails.append(f"{where}: no evidence — fail closed")
        for a in anchors:
            if not isinstance(a, dict) or a.get("kind") not in ANCHOR_KINDS:
                fails.append(f"{where}: malformed evidence anchor {a!r}")
                continue
            relf, quote = a.get("file"), a.get("quote")
            if not relf or not quote:
                fails.append(f"{where}: anchor missing file/quote")
                continue
            p = base / relf
            if not p.exists():
                fails.append(f"{where}: evidence file missing: {relf}")
                continue
            if norm(quote) not in norm(p.read_text(encoding="utf-8")):
                fails.append(f"{where}: evidence quote does NOT byte-verify "
                             f"in {relf} :: {quote[:70]!r}")
        prov = e.get("provenance") or {}
        for k in PROV_KEYS:
            if not prov.get(k):
                fails.append(f"{where}: provenance.{k} missing — fail closed")
        if e.get("confidence") not in BANDS:
            fails.append(f"{where}: confidence {e.get('confidence')!r} not "
                         f"in bands")
    return fails


# ---------------------------------------------------------------------------
# Presentation helpers
# ---------------------------------------------------------------------------
def short_sp(wording: str, n: int = 96) -> str:
    w = re.sub(r"\s+", " ", wording).strip()
    return w if len(w) <= n else w[:n - 3] + "..."


def item_context(st: dict, it: dict) -> list:
    """Human context lines: endpoints -> node titles + spec wording."""
    e = it["edge"]
    out = []
    for code in (e["source"], e["target"]):
        n = st["nodes_by_code"].get(code)
        if n:
            out.append(f"node {code} — {n['title']} ({n['family']})")
        for sp_code, role, wording in spec_refs(st, code):
            tag = f" [{role}]" if role else ""
            out.append(f"  spec {sp_code}{tag}: {short_sp(wording)}")
    return out


def evidence_lines(e: dict) -> list:
    out = []
    for a in e.get("evidence") or []:
        q = a["quote"]
        if len(q) > 110:
            q = q[:107] + "..."
        out.append(f"    - `{a['kind']}` {Path(a['file']).name} — \"{q}\"")
    return out


def resolve_ids(st: dict, ids: list) -> list:
    """'#N' (1-based, from `list`) or full identity -> identity strings."""
    pend = pending_items(st)
    out = []
    for raw in ids:
        raw = raw.strip()
        idx_form = raw[1:] if raw.startswith("#") else raw
        if idx_form.isdigit():
            # bare 'N' (shell-friendly: a leading '#' starts a bash comment)
            i = int(idx_form)
            if not 1 <= i <= len(pend):
                die(f"index {raw} out of range (1..{len(pend)}); re-run "
                    f"`list` — indices are state-dependent")
            out.append(pend[i - 1]["identity"])
        else:
            toks = raw.split()
            if len(toks) != 3 or toks[1] not in RELATIONS:
                die(f"{raw!r} is not an exact identity ('SRC REL TGT') or "
                    f"#N index")
            out.append(" ".join(toks))
    seen, dedup = set(), []
    for i in out:
        if i not in seen:
            seen.add(i)
            dedup.append(i)
    return dedup


# ---------------------------------------------------------------------------
# Subcommands
# ---------------------------------------------------------------------------
def cmd_list(st: dict, args) -> int:
    if st["failures"]:
        # session-47 fix: pass the LIST (die wraps single strings itself);
        # unpacking multiple failures crashed with TypeError instead of
        # printing the refusal reasons — fail-closed behavior restored
        die(st["failures"])
    act = actionable_edges(st)
    pend = [it for it in act if it["actionable"]]
    print(f"T-C11 pending §18 promotions — state {fingerprint(st)} "
          f"(baseline promo_count={st['promo_count']})")
    print(f"actionable: {len(pend)}  "
          f"(clean {sum(1 for i in pend if not i['flag'])} / "
          f"pending-flagged {sum(1 for i in pend if i['flag'])})  "
          f"not-actionable: {len(act) - len(pend)}  "
          f"nodes-awaiting-pathway: {len(node_items(st))}")
    print()
    for i, it in enumerate(pend, 1):
        e = it["edge"]
        flag = f"  [{it['flag']}]" if it["flag"] else ""
        print(f"#{i:>2}  {it['identity']}")
        print(f"     confidence={e['confidence']}  "
              f"method={e['provenance']['derivation_method']}{flag}")
    for it in act:
        if not it["actionable"]:
            print(f"  --  {it['identity']}  [{it['flag']}] {it['note']}")
    print()
    print("next: show <#n|identity|all> · export · approve [--all] [--dry-run]")
    return 0


def cmd_show(st: dict, args) -> int:
    if st["failures"]:
        # session-47 fix: pass the LIST (die wraps single strings itself);
        # unpacking multiple failures crashed with TypeError instead of
        # printing the refusal reasons — fail-closed behavior restored
        die(st["failures"])
    roundtrip_guard(st)
    if args.all:
        idents = [it["identity"] for it in pending_items(st)]
    else:
        if not args.ids:
            die("show needs ids or --all")
        idents = resolve_ids(st, args.ids)
    by = "operator"
    date = args.date or datetime.date.today().isoformat()
    print(f"preview date for validated_date: {date} "
          f"(pass --date to pin)")
    for ident in idents:
        it = next((x for x in pending_items(st) if x["identity"] == ident),
                  None)
        if it is None:
            die(f"{ident}: not a pending actionable edge (see `list`)")
        e = it["edge"]
        print("=" * 78)
        print(f"EDGE  {ident}   [{e['confidence']}/{it['flag'] or 'clean'}]")
        for ln in item_context(st, it):
            print(f"  {ln}")
        prov = e["provenance"]
        print(f"  derivation: {prov['derivation_method']} — "
              f"{short_sp(prov['derivation_notes'], 150)}")
        for ln in evidence_lines(e):
            print(f"  {ln}")
        od = e.get("operator_decision")
        if od:
            print(f"  operator_decision: {od.get('verdict')} — "
                  f"{short_sp(od.get('note', ''), 150)}")
        eh, mh = edge_hunks(st, ident, by, date)
        print("-" * 78)
        print("  diff if approved (validated_by/date shown for the batch):")
        sys.stdout.writelines(eh)
        if idents[-1] == ident:
            sys.stdout.writelines(mh)
    return 0


def cmd_export(st: dict, args) -> int:
    if st["failures"]:
        # session-47 fix: pass the LIST (die wraps single strings itself);
        # unpacking multiple failures crashed with TypeError instead of
        # printing the refusal reasons — fail-closed behavior restored
        die(st["failures"])
    roundtrip_guard(st)
    date = args.date
    out = Path(args.out) if args.out else \
        st["base"] / "graph" / "reports" / f"C11_DIFF_REVIEW_{date}.md"
    # session-48 fix: a relative --out is resolved against the repo root (the
    # default path's convention). Previously a relative --out crashed the
    # bundle render at the --review-ref line (relative_to mismatch) — the
    # flag had only ever been exercised via the default absolute path.
    if not out.is_absolute():
        out = st["base"] / out
    pend = pending_items(st)
    act = actionable_edges(st)
    by = "operator"
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"],
                          cwd=st["base"], capture_output=True,
                          text=True).stdout.strip() or "unknown"
    L = []
    L.append(f"# C11 Diff Review Bundle — pending §18 edge promotions "
             f"(generated {date})")
    L.append("")
    L.append(f"- baseline commit: `{head}`")
    L.append(f"- state fingerprint: `{fingerprint(st)}` "
             f"(promo_count={st['promo_count']})")
    L.append(f"- actionable: {len(pend)} edges "
             f"(clean {sum(1 for i in pend if not i['flag'])} / "
             f"pending-flagged {sum(1 for i in pend if i['flag'])}); "
             f"not-actionable: {len(act) - len(pend)}; nodes awaiting a "
             f"pathway: {len(node_items(st))}")
    L.append("- preview fidelity: simulator re-emits graph/concept_edges.yaml "
             "under the generator's own serialization contract with a "
             "byte-identity guard — what you read is what G13 will write.")
    L.append("")
    L.append("## Batch approval")
    L.append("")
    L.append("```bash")
    L.append("cd work/syllabai-resources && python3 scripts/c11_diff_review.py "
             "approve \\")
    for it in pend:
        if not it["flag"]:
            L.append(f"  '{it['identity']}' \\")
    L.append(f"  --by <operator> --date {date} "
             f"--review-ref {out.relative_to(st['base'])}")
    L.append("```")
    L.append("")
    L.append("Pending-flagged (PENDING operator_decision) edges are excluded "
             "from the command above; approving them additionally requires "
             "`--include-pending` — that flag records the explicit decision "
             "this bundle presents.")
    L.append("")
    L.append("## Index")
    L.append("")
    L.append("| # | identity | confidence | flag |")
    L.append("|---|----------|------------|------|")
    for i, it in enumerate(pend, 1):
        L.append(f"| {i} | `{it['identity']}` | {it['edge']['confidence']} | "
                 f"{it['flag'] or ''} |")
    L.append("")
    L.append("## Pending items — the exact diff each approval applies")
    L.append("")
    for i, it in enumerate(pend, 1):
        e = it["edge"]
        L.append(f"### {i}. `{it['identity']}` "
                 f"[{e['confidence']}{', ' + it['flag'] if it['flag'] else ''}]")
        L.append("")
        for ln in item_context(st, it):
            L.append(f"- {ln}")
        prov = e["provenance"]
        L.append(f"- derivation: {prov['derivation_method']} — "
                 f"{prov['derivation_notes']}")
        for ln in evidence_lines(e):
            L.append(ln[4:])  # strip CLI indent
        od = e.get("operator_decision")
        if od:
            L.append(f"- operator_decision: **{od.get('verdict')}** — "
                     f"{od.get('note', '')}")
        L.append("")
        L.append("```diff")
        eh, mh = edge_hunks(st, it["identity"], by, date)
        L.extend("".join(eh).rstrip("\n").split("\n"))
        L.append("```")
        L.append("")
    L.append("## File-level meta hunks (once, for the whole batch)")
    L.append("")
    L.append("```diff")
    if pend:
        L.extend("".join(meta_hunk_manual(st, len(pend))).rstrip("\n").split("\n"))
    L.append("```")
    L.append("")
    L.append("## Not actionable (decided or ineligible)")
    L.append("")
    for it in act:
        if not it["actionable"]:
            L.append(f"- `{it['identity']}` [{it['flag']}] {it['note']}")
    L.append("")
    L.append("## Nodes awaiting verdicts — no §18 pathway yet (informational)")
    L.append("")
    L.append("| node | title | family | spec points (role) | confidence |")
    L.append("|------|-------|--------|--------------------|------------|")
    for n in node_items(st):
        sps = "; ".join(f"{c} ({r})" if r else c
                        for c, r, _w in spec_refs(st, n["code"]))
        L.append(f"| `{n['code']}` | {n['title']} | {n['family']} | {sps} | "
                 f"{n['confidence']} |")
    L.append("")
    out.write_text("\n".join(L) + "\n", encoding="utf-8")
    print(f"diff-review bundle written: {out.relative_to(st['base'])} "
          f"({len(pend)} pending items)")
    return 0


def cmd_approve(st: dict, args) -> int:
    if st["failures"]:
        # session-47 fix: pass the LIST (die wraps single strings itself);
        # unpacking multiple failures crashed with TypeError instead of
        # printing the refusal reasons — fail-closed behavior restored
        die(st["failures"])
    roundtrip_guard(st)
    if not args.by:
        die("approve requires --by <operator identity> (attribution gate; "
            "AI identities are rejected — promotion is operator-only)")
    if AI_NAME_RE.search(args.by):
        die(f"--by {args.by!r} fails the attribution gate: promotion is "
            f"operator-only (AI self-attribution forbidden)")
    if not RE_ISO_DATE.match(args.date):
        die(f"--date must be YYYY-MM-DD, got {args.date!r}")

    if args.all and args.except_ids:
        die("--all and --except are mutually exclusive")
    if args.all:
        sel = [it for it in pending_items(st)
               if args.include_pending or not it["flag"]]
        if args.all and not sel:
            die("nothing selectable: no actionable edges "
                "(or only pending-flagged; pass --include-pending)")
    elif args.except_ids:
        excl = set(resolve_ids(st, args.except_ids))
        sel = [it for it in pending_items(st)
               if it["identity"] not in excl
               and (args.include_pending or not it["flag"])]
    else:
        if not args.ids:
            die("approve needs ids, --all, or --except")
        sel = []
        pend = {it["identity"]: it for it in pending_items(st)}
        for ident in resolve_ids(st, args.ids):
            it = pend.get(ident)
            if it is None:
                die(f"{ident}: not a pending actionable edge (see `list`)")
            sel.append(it)

    batch = [it["identity"] for it in sel]
    if len(set(batch)) != len(batch):
        die("duplicate identities in the batch")
    fails = preverify(st, sel, args.include_pending)
    if fails:
        die(*fails)

    ref = args.review_ref or \
        f"graph/reports/C11_DIFF_REVIEW_{args.date}.md"
    ref_path = st["base"] / ref
    if not args.dry_run and not ref_path.exists():
        die(f"review_reference {ref} does not exist — run "
            f"`python3 scripts/c11_diff_review.py export --date {args.date}` "
            f"first (the bundle is the ratifying artifact G13 checks for)")

    print(f"batch: {len(batch)} edge promotion(s)  by={args.by}  "
          f"date={args.date}  review_ref={ref}  state={fingerprint(st)}")
    sys.stdout.writelines(batch_hunks(st, batch, args.by, args.date))
    cmd = [sys.executable, str(HERE / "c11_promote.py")]
    for ident in batch:
        cmd += ["--edge", ident]
    cmd += ["--by", args.by, "--date", args.date, "--review-ref", ref]
    print("$ " + " ".join(cmd))
    if args.dry_run:
        print("dry-run: nothing executed; the gated apply is the command "
              "above (single c11_promote invocation = single G13 re-run)")
        return 0
    r = subprocess.run(cmd, cwd=st["base"])
    if r.returncode != 0:
        print("NOTE: c11_promote/generator rejected the state — nothing was "
              "changed by THIS tool; inspect the promotions file and revert "
              "via git if needed (fail-closed as designed).", file=sys.stderr)
    return r.returncode


# ---------------------------------------------------------------------------
def main(argv=None) -> int:
    ap = argparse.ArgumentParser(
        description="T-C11 diff-based batch approval for §18 edge promotions")
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("list", help="pending items summary")
    p.set_defaults(fn=cmd_list)

    p = sub.add_parser("show", help="full context + exact diff per item")
    p.add_argument("ids", nargs="*", metavar="id|#idx")
    p.add_argument("--all", action="store_true")
    p.add_argument("--date", default=None,
                   help="validated_date to preview (default: today)")
    p.set_defaults(fn=cmd_show)

    p = sub.add_parser("export", help="write the diff-review bundle (.md)")
    p.add_argument("--out", default=None)
    p.add_argument("--date", default=datetime.date.today().isoformat())
    p.set_defaults(fn=cmd_export)

    p = sub.add_parser("approve", help="batch-approve via one c11_promote run")
    p.add_argument("ids", nargs="*", metavar="id|#idx")
    p.add_argument("--all", action="store_true",
                   help="approve every clean actionable edge")
    p.add_argument("--except", dest="except_ids", nargs="*",
                   metavar="id|#idx",
                   help="approve everything except these (clean set only)")
    p.add_argument("--include-pending", action="store_true",
                   help="also select operator_decision=PENDING edges "
                        "(records the explicit operator decision)")
    p.add_argument("--by", default=None, help="operator identity (required)")
    p.add_argument("--date", default=datetime.date.today().isoformat())
    p.add_argument("--review-ref", default=None,
                   help="ratifying artifact (default: the export bundle)")
    p.add_argument("--dry-run", action="store_true",
                   help="print diffs + the exact command; execute nothing")
    p.set_defaults(fn=cmd_approve)

    args = ap.parse_args(argv)
    st = load_state(REPO)
    return args.fn(st, args)


if __name__ == "__main__":
    sys.exit(main())
