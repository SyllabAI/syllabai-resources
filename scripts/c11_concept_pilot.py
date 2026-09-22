#!/usr/bin/env python3
"""
T-C11 — c11_concept_pilot.py: deterministic, gated generator for the pilot
concept / prerequisite / misconception graph (4CH1 Section 1, slice 1.25–1.36).

Contract: graph/reports/C11_ARCHITECTURE.md (§10 Deterministic generation
contract). Single sources of truth: the decision-record REGISTRY — the pilot
record scripts/c11_pilot_decisions.yaml first, then each authorized §16
expansion-batch record with its own extraction_pass id (session-47, batch 1:
scripts/c11_batch1_decisions.yaml; architecture §8: expansion passes add
nodes via new decision records). Emits, fail-closed, after ALL gates pass:

  graph/igcse-chemistry/concepts          — CONCEPT + MISCONCEPTION nodes (all records)
  graph/igcse-chemistry/concept_edges     — derived PART_OF + authored semantic edges
  graph/igcse-chemistry/spec_command_kinds — frozen-guide §8 command-kind tags (24 SPs)

Gates (each hard-fails, naming the record and the violated rule):

  G01 schema        — required keys/types/vocabularies on every record
  G02 namespace     — every code in the 4CH1-* namespace; no foreign codes
  G03 evidence      — every quote byte-verifies (T-C10 norm) in its cited file
  G04 attachment    — every spec_points entry has a SPEC-anchor (quote ⊆
                      official wording of that SP) or a NOTE-anchor whose file
                      HUMAN_VALIDATED-maps to that SP (T-C10 crosscheck)
  G05 scope         — attachments/practicals inside the OWNING record's scope
                      (registry slices are disjoint); no node attaches to
                      4CH1-4.15 (negative control rule 1)
  G06 endpoints     — every edge endpoint resolves in the merged node universe
                      (all-record concepts ∪ all-record SPs ∪ practicals)
  G07 edge-anchors  — every authored edge has an admissible anchor: NOTE whose
                      file HUMAN_VALIDATED-maps to an SP attached to the source
                      (or the source practical's SP) or to the target concept;
                      or SPEC (quote ⊆ an attached SP's wording); or MARK_SCHEME
                      for misconception-family relations only (rule 2/§11)
  G08 structure     — no self-edges; no duplicate (source, relation, target);
                      relation/type discipline (misconception edges from
                      MISCONCEPTION nodes with matching pattern_class; targets
                      CONCEPT; EXPLAINED_BY concept→concept); REQUIRES_PREREQUISITE
                      acyclic
  G09 confidence    — derivation_method caps the admissible band (§6)
  G10 anti-forgery  — no validation_status HUMAN_VALIDATED anywhere in the
                      decision record; generated records are SUGGESTED or
                      REVIEW_REQUIRED only (with ambiguity_note)
  G11 misconception — pattern_class present; remediation_evidence present and
                      byte-verified (100% of misconceptions source-quoted)
  G12 command-kinds — exactly the union of all record scopes (each SP tagged
                      exactly once across records); guide_class in vocabulary;
                      verb matches the registry's leading_verb
  G13 promotions    — the operator-side promotion record
                      (scripts/c11_promotions.yaml, written only by
                      scripts/c11_promote.py) is schema-validated and each
                      entry must resolve to EXACTLY one authored edge identity;
                      AI self-attribution fails closed; held candidates and
                      PART_OF are not promotable. Matched edges are emitted
                      HUMAN_VALIDATED + validated_by/validated_date (evidence,
                      provenance and confidence preserved verbatim).

Determinism: pinned dates, sorted emission, no clock reads, no git reads, no
randomness. A second run over unchanged decisions AND an unchanged promotions
file is byte-identical (zero promotions emits the exact pre-promotion bytes).

Usage: python3 scripts/c11_concept_pilot.py [--dry-run]
Exit 0 = all gates green + files written (unless --dry-run).
"""
from __future__ import annotations

import re
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import graph_paths as GP  # C28 §3.2 path registry — single source of ratified store paths

import json
import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
# Session-55 repair (2026-09-22, dated): the C28 stage-2 migration moved the
# ratified stores to graph/igcse-chemistry/ (b3bca02); this generator still
# read/wrote the pre-migration root layout and has been dark since. All store
# I/O resolves through the C28 registry (graph_paths.py) — no gate changed.
sys.path.insert(0, str(HERE))
import graph_paths as GP  # noqa: E402  # C28 §3.2 path registry
GRAPH = GP.qual_dir()  # the qual's ratified store dir (registry-resolved)
NOTES = REPO / "Chemistry IGCSE Revision Notes"
PROMOTIONS = HERE / "c11_promotions.yaml"
# Session-47 (§16 batch 1, 2026-09-12): the decision-record REGISTRY. The
# pilot record is first; each authorized §16 expansion batch appends its own
# record with its own extraction_pass id. All listed records are MANDATORY —
# a missing registry member is a fail-closed abort (the graph must
# regenerate from its full registry; test sandboxes must stage it whole).
# Session-49 (§16 batch 2, 2026-09-12): the registry grows by the batch-2
# record (extraction_pass c11-s16-batch-2, commissioned by the operator's
# 'run batch 2') — same fail-closed contract, same disjoint-slice rule.
# Session-51 (§16 batch 3, 2026-09-12): the registry grows by the batch-3
# record (extraction_pass c11-s16-batch-3, commissioned by the operator's
# session-51 move-forward directive — the full S1 remainder 1.37–1.60C in
# one batch, 24 SPs + PR-04) — same fail-closed contract, same
# disjoint-slice rule.
# Session-53 (§16 batch 4, 2026-09-13): the registry grows by the batch-4
# record (extraction_pass c11-s16-batch-4, commissioned by the operator's
# session-53 batch-4 directive — Section 3 Physical Chemistry 3.1–3.22C,
# 22 SPs + PR-09/PR-10/PR-11, under the session-52 cross-slice boundary
# ruling) — same fail-closed contract, same disjoint-slice rule.
# Session-55 (§16 batch 5, 2026-09-22): the registry grows by the batch-5
# record (S2 Inorganic first slice, 4CH1-2.1-2.14) — the operator's "run
# batch 5" directive; same per-batch operator gate before any promotion.
# Session-57 (§16 batch 6, 2026-09-22): the registry grows by the batch-6
# record (S2 Inorganic second slice, 4CH1-2.15-2.27) — the operator's
# "commission batch 6" directive; same fail-closed contract, same
# disjoint-slice rule, same per-batch operator gate before any promotion.
DECISION_RECORDS = ["c11_pilot_decisions.yaml", "c11_batch1_decisions.yaml",
                    "c11_batch2_decisions.yaml", "c11_batch3_decisions.yaml",
                    "c11_batch4_decisions.yaml", "c11_batch5_decisions.yaml",
                    "c11_batch6_decisions.yaml"]
RE_ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
AI_NAME_RE = re.compile(r"glm|super\s*z|gpt|claude|openai|anthropic|\bai\b"
                        r"|llm|agent|model|bot", re.I)

NEGATIVE_CONTROL = "4CH1-4.15"

FAMILIES = {"CONCEPT", "MISCONCEPTION"}
PATTERN_CLASSES = {"ERRONEOUS_BELIEF", "WRONG_ANSWER_PATTERN"}
ROLES = {"CORE", "SUPPORTING", "ENRICHMENT"}
RELATIONS = {"PART_OF", "REQUIRES_PREREQUISITE", "RELATED_TO", "MISCONCEPTION_OF",
             "EXPLAINED_BY", "REMEDIATED_BY", "COMMONLY_CONFUSED_WITH",
             "WRONG_ANSWER_PATTERN"}
MISCONCEPTION_RELATIONS = {"MISCONCEPTION_OF", "WRONG_ANSWER_PATTERN", "REMEDIATED_BY"}
ANCHOR_KINDS = {"NOTE", "SPEC", "MARK_SCHEME"}
BANDS = {"high": 3, "medium": 2, "low": 1}
DERIVATION_CAPS = {
    "SPEC_VERBATIM": "high",
    "DEFINITIONAL_DEPENDENCY": "high",
    "USED_WITHOUT_RETEACHING": "high",
    "EXPLICIT_TEACH_SEQUENCE": "high",
    "SINGLE_SOURCE_CAUSAL_TEACHING": "high",
    "ASSESSMENT_DOCUMENTED": "high",
    "EXAMINER_TIP_EXPLICIT": "high",
    "TEACH_SEQUENCE_WITHIN_NOTE": "medium",
    "IMPLICIT_USE": "medium",
    "EXAMINER_TIP_IMPLIED": "low",
    "RELATED_RESIDUAL": "medium",
}
GUIDE_CLASSES = {"KNOW_TERM", "EXPLAIN_HOW", "CALCULATE", "DESCRIBE_EXPERIMENT",
                 "REPRESENT_DIAGRAM", "UNDERSTAND_RELATION", "PRODUCE_EQUATION"}
STATES = {"SUGGESTED", "REVIEW_REQUIRED"}
NODE_KEYS = ["code", "family", "pattern_class", "title", "aliases",
             "retrieval_only_aliases", "spec_points",
             "evidence", "remediation_evidence", "provenance", "confidence",
             "validation_status", "version", "created_at", "damage_flags"]
NODE_MANDATORY = ["code", "family", "title", "aliases", "provenance", "confidence",
                  "validation_status", "version", "created_at", "damage_flags"]
EDGE_KEYS = ["source", "relation", "target", "evidence", "provenance", "confidence",
             "validation_status", "ambiguity_note", "role", "version", "created_at"]
EDGE_MANDATORY = ["source", "relation", "target", "evidence", "provenance",
                  "confidence", "validation_status", "version", "created_at"]

# --- T-C10 norm() convention (copied verbatim from scripts/c10_map_notes.py;
#     the shared anti-hallucination normalisation: NFC, strip markdown escapes/
#     links/HTML tags/emphasis, translate dashes/quotes, collapse whitespace) ---
_TRANS = {ord("–"): "-", ord("—"): "-", ord("″"): '"', ord("′"): "'"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFC", s)
    s = s.replace("\\", "")
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    s = re.sub(r"<[^>]+>", "", s)
    s = re.sub(r"[*_`#>]+", "", s)
    s = s.translate(_TRANS)
    s = re.sub(r"\s+", " ", s)
    return s.strip()


class Gates:
    def __init__(self):
        self.failures = []
        self.counts = {}

    def fail(self, msg):
        self.failures.append(msg)

    @property
    def ok(self):
        return not self.failures


G = Gates()


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        print(f"FATAL: {path} does not parse: {e}", file=sys.stderr)
        sys.exit(1)


# ---------------------------------------------------------------------------
# Load inputs (session-47: the decision-record REGISTRY — pilot first, then
# each authorized §16 batch record; fail-closed if any member is missing)
_missing = [n for n in DECISION_RECORDS if not (HERE / n).exists()]
if _missing:
    print(f"FATAL: decision record(s) missing from the registry: {_missing} "
          f"(registry: {DECISION_RECORDS})", file=sys.stderr)
    sys.exit(1)
recs = []
for _name in DECISION_RECORDS:
    _d = load_yaml(HERE / _name) or {}
    _m = _d.get("meta") or {}
    for _k in ("task", "stage", "extraction_pass", "generated_date",
               "model_version", "curriculum_code", "scope", "contract"):
        if not _m.get(_k):
            print(f"FATAL: scripts/{_name}: meta.{_k} missing", file=sys.stderr)
            sys.exit(1)
    _sc = _m["scope"] or {}
    if not _sc.get("spec_points"):
        print(f"FATAL: scripts/{_name}: meta.scope.spec_points empty",
              file=sys.stderr)
        sys.exit(1)
    recs.append({"name": _name, "path": f"scripts/{_name}", "dec": _d,
                 "stage": _m["stage"], "pass": _m["extraction_pass"],
                 "date": _m["generated_date"],
                 "sps": list(_sc["spec_points"]),
                 "practicals": list(_sc.get("practicals") or [])})

# registry discipline (session-47): slices are DISJOINT — no SP and no
# practical may be claimed by two records (overlap would double-cover a
# spec point and double-derive its PART_OF set)
_sps_owner, _pr_owner = {}, {}
for _r in recs:
    for _sp in _r["sps"]:
        if _sp in _sps_owner:
            G.fail(f"G05 registry: spec point {_sp} claimed by both "
                   f"{_sps_owner[_sp]} and {_r['name']}")
        _sps_owner[_sp] = _r["name"]
    for _p in _r["practicals"]:
        if _p in _pr_owner:
            G.fail(f"G05 registry: practical {_p} claimed by both "
                   f"{_pr_owner[_p]} and {_r['name']}")
        _pr_owner[_p] = _r["name"]

ALL_SPS = [sp for r in recs for sp in r["sps"]]
ALL_PRACTICALS = [p for r in recs for p in r["practicals"]]
dec = recs[0]["dec"]  # pilot record (historical references below)

sp_data = load_yaml(GRAPH / "specification_points.yaml")
pr_data = load_yaml(GRAPH / "practicals.yaml")
# Operator-side promotion record (§18): written ONLY by scripts/c11_promote.py.
# Missing file = zero promotions = byte-identical pre-promotion output.
promo_raw = (load_yaml(PROMOTIONS) if PROMOTIONS.exists()
             else {"promotions": []})
promotions = (promo_raw or {}).get("promotions") or []
# T-C19 attachment-promotion record (the expansion round c11_promote.py names):
# concept->SP PART_OF rows are DERIVED from node attachments, so their promotion
# lives in its own operator-side record, written ONLY by scripts/c19_promote.py.
# Missing file = zero c19 promotions = byte-identical emission (the G13 property).
C19_PROMOTIONS = HERE / "c19_promotions.yaml"
c19_raw = (load_yaml(C19_PROMOTIONS) if C19_PROMOTIONS.exists()
           else {"promotions": []})
c19_promotions = (c19_raw or {}).get("promotions") or []

spec_by_code = {sp["code"]: sp for sp in sp_data["specification_points"]}
practical_by_code = {p["code"]: p for p in pr_data["practicals"]}

# --- T-C10 mapping index: note file -> set of HUMAN_VALIDATED SP codes ---
def note_mappings():
    idx = {}
    for f in NOTES.rglob("*.md"):
        text = f.read_text(encoding="utf-8")
        m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
        if not m:
            continue
        try:
            fm = yaml.safe_load(m.group(1))
        except yaml.YAMLError:
            continue
        sm = (fm or {}).get("spec_map") or {}
        for sp in sm.get("spec_points", []):
            prov = sp.get("provenance") or {}
            if prov.get("validation_status") == "HUMAN_VALIDATED":
                idx.setdefault(str(f.relative_to(REPO)), set()).add(sp["code"])
    return idx


TC10 = note_mappings()
G.counts["tc10_validated_mappings"] = sum(len(v) for v in TC10.values())
if G.counts["tc10_validated_mappings"] != 209:
    G.fail(f"G04 pre-state: expected 209 HUMAN_VALIDATED T-C10 mappings, "
           f"found {G.counts['tc10_validated_mappings']} (T-C10 baseline changed?)")

# --- evidence file cache (normed) ---
_ev_cache = {}


def normed_file(rel: str):
    if rel not in _ev_cache:
        p = REPO / rel
        if not p.exists():
            _ev_cache[rel] = None
        else:
            _ev_cache[rel] = norm(p.read_text(encoding="utf-8"))
    return _ev_cache[rel]


def quote_ok(rel: str, quote: str) -> bool:
    # Session-55 repair (2026-09-22, dated): frozen decision records carry the
    # historical root-form SPEC anchor path (the pre-migration store path);
    # the C28 registry legacy_map resolves it to the canonical store location
    # (C28 P5 — records stay historical, checkers resolve; one resolver for
    # all checkers).
    rel = GP.resolve_rel(rel)
    body = normed_file(rel)
    if body is not None and norm(quote) in body:
        return True
    # T-C23: quotes from the retired OCR lineage are admissible exactly where
    # the C23 swap record re-anchored them (auditable old->new mapping; the
    # definitive store no longer contains the pre-swap wording bytes)
    if rel == GP.store_rel("specification_points"):
        for _sp, _old in _C23_REANCHORED:
            if _old == quote:
                return True
    return False


def spec_anchor_text(sp) -> str:
    """Definitive anchor text (T-C23): official wording + PDF bullets."""
    t = sp["official_wording"]
    b = sp.get("official_bullets")
    if b:
        t += " " + " ".join(b)
    return t


# Session-55 repair (2026-09-22, dated): the swap record lives in the SHARED
# graph/reports/ — resolved through the registry (pre-migration this was
# REPO/graph/reports via GRAPH.parent, which the stage-2 move broke).
_C23_RECORD = GP.reports_dir() / "C23_DEFINITIVE_SWAP_RECORD.json"
_C24_RECORD = GP.reports_dir() / "C24_STORE_RESPACE_RECORD.json"
_C23_REANCHORED: set = set()
_C23_NEW: dict = {}
if _C23_RECORD.exists():
    try:
        _rec = json.loads(_C23_RECORD.read_text())
        for _r in _rec.get("adjudications", {}).get("quote_reanchors", []):
            _C23_REANCHORED.add((_r.get("sp"), _r.get("old_quote")))
            _C23_NEW[(_r.get("sp"), _r.get("old_quote"))] = _r.get("new_quote")


    except Exception:
        _C23_REANCHORED = set()

# Session-55 repair (2026-09-22, dated): the C24 respace lane (immutable
# record) re-anchored the C23 new_quotes a second time (glyph normalization
# '( M r )' -> '(Mr)'); the stores were repaired in place and the generator
# was not re-run after C24, so the drift went unnoticed until the post-C28
# registry-resolved re-run. The re-anchor chain composes C23 -> C24 — both
# immutable records read, neither edited (C28 P5).
if _C24_RECORD.exists():
    try:
        _rec24 = json.loads(_C24_RECORD.read_text())
        for _r in _rec24.get("quote_reanchors", []):
            _k = (_r.get("sp"), _r.get("old_quote"))
            _C23_REANCHORED.add(_k)
            _C23_NEW[_k] = _r.get("new_quote")
    except Exception:
        pass


def spec_wording_has(code: str, quote: str) -> bool:
    sp = spec_by_code.get(code)
    if sp is None:
        return False
    if norm(quote) in norm(spec_anchor_text(sp)):
        return True
    # T-C23: frozen decision-record quotes from the retired OCR lineage are
    # admissible exactly where the C23 swap record re-anchored that quote on
    # that SP (auditable old->new mapping in the swap record)
    return (code, quote) in _C23_REANCHORED


def anchor_ok(anchor, where: str):
    kind = anchor.get("kind")
    rel = anchor.get("file")
    quote = anchor.get("quote")
    if kind not in ANCHOR_KINDS:
        G.fail(f"G01 {where}: anchor kind {kind!r} not in {sorted(ANCHOR_KINDS)}")
        return False
    if not rel or not quote:
        G.fail(f"G01 {where}: anchor missing file/quote")
        return False
    if not quote_ok(rel, quote):
        G.fail(f"G03 {where}: quote NOT found in {rel} :: {quote[:70]!r}")
        return False
    return True


def note_maps_to(rel: str, sp_code: str) -> bool:
    return sp_code in TC10.get(rel, set())


# ---------------------------------------------------------------------------
# G01/G02 schema + namespace on nodes (session-47: merged over the record
# registry; per-record determinism fields — version/created_at/extraction_pass
# are validated against the OWNING record's meta)
nodes = [n for r in recs for n in (r["dec"].get("nodes") or [])]
node_rec = {}
for r in recs:
    for n in (r["dec"].get("nodes") or []):
        node_rec[n.get("code")] = r
node_codes = set()
for n in nodes:
    where = f"node {n.get('code', '?')}"
    for k in NODE_MANDATORY:
        if k not in n:
            G.fail(f"G01 {where}: missing key {k!r}")
    code = n.get("code")
    if not isinstance(code, str) or not code.startswith("4CH1-"):
        G.fail(f"G02 {where}: code not in 4CH1-* namespace")
    if code in node_codes:
        G.fail(f"G01 {where}: duplicate node code")
    node_codes.add(code)
    if n.get("family") not in FAMILIES:
        G.fail(f"G01 {where}: family {n.get('family')!r} not in {sorted(FAMILIES)}")
    if n.get("validation_status") not in STATES:
        G.fail(f"G10 {where}: validation_status {n.get('validation_status')!r} "
               f"(generation may emit SUGGESTED/REVIEW_REQUIRED only)")
    if n.get("confidence") not in BANDS:
        G.fail(f"G01 {where}: confidence {n.get('confidence')!r} not in {sorted(BANDS)}")
    # G14 dual-track alias discipline (operator alias policy RETRIEVAL_EXEMPT,
    # session 44, applied session 45): retrieval_only_aliases is the marked
    # unevidenced track — a term may sit on exactly one track, never both,
    # and never as corpus-evidenced terminology.
    ro = n.get("retrieval_only_aliases")
    if ro is not None:
        if not isinstance(ro, list) or not all(
                isinstance(a, str) and a.strip() for a in ro):
            G.fail(f"G14 {where}: retrieval_only_aliases must be a list of "
                   f"non-empty strings")
        overlap = {str(a).casefold() for a in ro} \
            & {str(a).casefold() for a in (n.get("aliases") or [])}
        if overlap:
            G.fail(f"G14 {where}: dual-track violation — {sorted(overlap)} "
                   f"present in BOTH aliases and retrieval_only_aliases")
    r = node_rec.get(n.get("code"))
    if n.get("version") != 1 or n.get("created_at") != r["date"]:
        G.fail(f"G01 {where}: version/created_at must be 1/{r['date']!r} "
               f"(determinism, record {r['name']})")
    prov = n.get("provenance") or {}
    for k in ("tier", "model_version", "extraction_pass", "derivation_method",
              "derivation_notes", "upstream", "generated_date"):
        if not prov.get(k):
            G.fail(f"G01 {where}: provenance.{k} missing")
    if prov.get("tier") != "AI_SUGGESTED":
        G.fail(f"G01 {where}: provenance.tier must be AI_SUGGESTED")
    if prov.get("extraction_pass") != r["pass"]:
        G.fail(f"G01 {where}: extraction_pass mismatch with meta "
               f"(record {r['name']})")
    if prov.get("derivation_method") not in DERIVATION_CAPS:
        G.fail(f"G01 {where}: derivation_method {prov.get('derivation_method')!r} "
               f"not in the controlled vocabulary")
    # G09 confidence cap
    cap = DERIVATION_CAPS.get(prov.get("derivation_method"))
    if cap and BANDS.get(n.get("confidence"), 0) > BANDS[cap]:
        G.fail(f"G09 {where}: confidence {n.get('confidence')!r} exceeds cap "
               f"{cap!r} for derivation_method {prov.get('derivation_method')!r}")

    if n.get("family") == "MISCONCEPTION":
        if n.get("pattern_class") not in PATTERN_CLASSES:
            G.fail(f"G01 {where}: pattern_class {n.get('pattern_class')!r} required")
        rem = n.get("remediation_evidence") or []
        if not rem:
            G.fail(f"G11 {where}: misconception without remediation_evidence")
        for a in rem:
            anchor_ok(a, f"{where} remediation")
        for a in n.get("evidence") or []:
            anchor_ok(a, where)
        if not (n.get("evidence")):
            G.fail(f"G11 {where}: misconception without (named-source) evidence")
    else:
        if n.get("pattern_class") is not None:
            G.fail(f"G01 {where}: pattern_class only on MISCONCEPTION nodes")
        if n.get("remediation_evidence") is not None:
            G.fail(f"G01 {where}: remediation_evidence only on MISCONCEPTION nodes")

# G05 scope + G04 attachment rule on CONCEPT nodes
for n in nodes:
    if n.get("family") != "CONCEPT":
        continue
    where = f"node {n['code']}"
    r = node_rec[n["code"]]
    atts = n.get("spec_points") or []
    if not atts:
        G.fail(f"G01 {where}: CONCEPT without spec_points attachment")
    for att in atts:
        aw = f"{where} @ {att.get('code')}"
        sp_code = att.get("code")
        role = att.get("role")
        if sp_code not in r["sps"]:
            if sp_code == NEGATIVE_CONTROL:
                G.fail(f"G05 {aw}: NEGATIVE CONTROL — no node may attach to "
                       f"4CH1-4.15 (no validated T-C10 coverage exists)")
            else:
                G.fail(f"G05 {aw}: spec point outside the owning record's "
                       f"scope ({r['name']})")
        if role not in ROLES:
            G.fail(f"G01 {aw}: role {role!r} not in {sorted(ROLES)}")
        anchors = att.get("evidence") or []
        if not anchors:
            G.fail(f"G04 {aw}: attachment without evidence")
        ok = False
        for a in anchors:
            if not anchor_ok(a, aw):
                continue
            if a["kind"] == "SPEC":
                if spec_wording_has(sp_code, a["quote"]):
                    ok = True
            elif a["kind"] == "NOTE":
                if note_maps_to(a["file"], sp_code):
                    ok = True
            else:
                G.fail(f"G04 {aw}: MARK_SCHEME anchor inadmissible for concept "
                       f"attachment (assessment evidence is misconception-class only)")
        if not ok:
            G.fail(f"G04 {aw}: no anchor resolves to the SP — need a SPEC quote "
                   f"inside its official wording or a NOTE whose T-C10 mapping to "
                   f"this SP is HUMAN_VALIDATED")

# command kinds G12 (session-47: merged over the record registry; the union
# of all record scopes must be tagged exactly once across records)
cks = [c for r in recs for c in (r["dec"].get("command_kinds") or [])]
ck_codes = [c.get("code") for c in cks]
if sorted(ck_codes) != sorted(ALL_SPS):
    G.fail(f"G12 command-kind tags must cover exactly the union of all "
           f"record scopes ({len(ALL_SPS)} SPs)")
ck_rec = {}
for r in recs:
    for c in (r["dec"].get("command_kinds") or []):
        if c.get("code") in ck_rec:
            G.fail(f"G12 registry: command-kind tag for {c.get('code')} is "
                   f"duplicated across {ck_rec[c.get('code')]['name']} and "
                   f"{r['name']}")
        ck_rec[c.get("code")] = r
for c in cks:
    where = f"command_kind {c.get('code')}"
    if c.get("code") not in ck_rec[c.get("code")]["sps"]:
        G.fail(f"G12 {where}: tag outside its own record's scope")
for c in cks:
    where = f"command_kind {c.get('code')}"
    if c.get("guide_class") not in GUIDE_CLASSES:
        G.fail(f"G12 {where}: guide_class {c.get('guide_class')!r}")
    if c.get("verb") != spec_by_code.get(c.get("code"), {}).get("leading_verb"):
        G.fail(f"G12 {where}: verb must equal the registry leading_verb")
    for k in ("verb", "guide_class", "demanded_substance"):
        if not c.get(k):
            G.fail(f"G12 {where}: missing {k!r}")

# ---------------------------------------------------------------------------
# G06/G07/G08 on authored edges (session-47: merged over the record
# registry; per-record determinism + extraction_pass; the universe spans all
# records' nodes, SPs and practicals)
edges = [e for r in recs for e in (r["dec"].get("edges") or [])]
edge_rec = {}
for r in recs:
    for e in (r["dec"].get("edges") or []):
        edge_rec[(e.get("source"), e.get("relation"), e.get("target"))] = r
universe = node_codes | set(ALL_SPS) | set(ALL_PRACTICALS)
node_by_code = {n["code"]: n for n in nodes}


def attached_sps(code: str):
    n = node_by_code.get(code)
    if n and n.get("family") == "CONCEPT":
        return {a["code"] for a in n["spec_points"]}
    if code in practical_by_code:
        return {practical_by_code[code]["spec_point"]}
    return set()


edge_seen = set()
prereq_adj = {}
for e in edges:
    src, rel, tgt = e.get("source"), e.get("relation"), e.get("target")
    where = f"edge {src} -[{rel}]-> {tgt}"
    for k in EDGE_MANDATORY:
        if k not in e:
            G.fail(f"G01 {where}: missing key {k!r}")
    if rel not in RELATIONS or rel == "PART_OF":
        G.fail(f"G01 {where}: relation must be a non-PART_OF member of the vocabulary")
    if src == tgt:
        G.fail(f"G08 {where}: self-edge")
    key = (src, rel, tgt)
    if key in edge_seen:
        G.fail(f"G08 {where}: duplicate edge")
    edge_seen.add(key)
    for end in (src, tgt):
        if end not in universe:
            G.fail(f"G06 {where}: endpoint {end!r} not in the merged node "
                   f"universe")
    if e.get("validation_status") not in STATES:
        G.fail(f"G10 {where}: validation_status {e.get('validation_status')!r}")
    if e.get("validation_status") == "REVIEW_REQUIRED" and not e.get("ambiguity_note"):
        G.fail(f"G01 {where}: REVIEW_REQUIRED requires ambiguity_note")
    if e.get("confidence") not in BANDS:
        G.fail(f"G01 {where}: confidence {e.get('confidence')!r}")
    er = edge_rec.get(key)
    if e.get("version") != 1 or e.get("created_at") != er["date"]:
        G.fail(f"G01 {where}: version/created_at must be 1/{er['date']!r} "
               f"(determinism, record {er['name']})")
    prov = e.get("provenance") or {}
    for k in ("tier", "model_version", "extraction_pass", "derivation_method",
              "derivation_notes", "upstream", "generated_date"):
        if not prov.get(k):
            G.fail(f"G01 {where}: provenance.{k} missing")
    if prov.get("tier") != "AI_SUGGESTED":
        G.fail(f"G01 {where}: provenance.tier must be AI_SUGGESTED")
    if prov.get("extraction_pass") != er["pass"]:
        G.fail(f"G01 {where}: extraction_pass mismatch with meta "
               f"(record {er['name']})")
    cap = DERIVATION_CAPS.get(prov.get("derivation_method"))
    if prov.get("derivation_method") not in DERIVATION_CAPS:
        G.fail(f"G01 {where}: derivation_method {prov.get('derivation_method')!r} "
               f"not in the controlled vocabulary")
    elif BANDS.get(e.get("confidence"), 0) > BANDS[cap]:
        G.fail(f"G09 {where}: confidence {e.get('confidence')!r} exceeds cap {cap!r}")

    # relation discipline
    src_n, tgt_n = node_by_code.get(src), node_by_code.get(tgt)
    if rel in MISCONCEPTION_RELATIONS:
        if not (src_n and src_n.get("family") == "MISCONCEPTION"):
            G.fail(f"G08 {where}: source must be a MISCONCEPTION-family node")
        want = "ERRONEOUS_BELIEF" if rel == "MISCONCEPTION_OF" else "WRONG_ANSWER_PATTERN"
        if src_n and rel in ("MISCONCEPTION_OF", "WRONG_ANSWER_PATTERN") \
                and src_n.get("pattern_class") != want:
            G.fail(f"G08 {where}: pattern_class {src_n.get('pattern_class')!r} does "
                   f"not match relation {rel} (frozen triple distinction)")
        if not (tgt_n and tgt_n.get("family") == "CONCEPT"):
            G.fail(f"G08 {where}: target must be a CONCEPT")
    elif rel == "EXPLAINED_BY":
        if not (src_n and src_n.get("family") == "CONCEPT" and tgt_n
                and tgt_n.get("family") == "CONCEPT"):
            G.fail(f"G08 {where}: EXPLAINED_BY must be CONCEPT -> CONCEPT")
    elif rel == "REQUIRES_PREREQUISITE":
        if src not in node_codes and src not in ALL_PRACTICALS:
            G.fail(f"G08 {where}: source must be a concept or a practical")
        if not (tgt_n and tgt_n.get("family") == "CONCEPT"):
            G.fail(f"G08 {where}: target must be a CONCEPT (prerequisites are concepts)")
        prereq_adj.setdefault(src, set()).add(tgt)
    elif rel in ("RELATED_TO", "COMMONLY_CONFUSED_WITH"):
        if not (src_n and tgt_n and src_n.get("family") == "CONCEPT"
                and tgt_n.get("family") == "CONCEPT"):
            G.fail(f"G08 {where}: {rel} must be CONCEPT -> CONCEPT")
        if not prov.get("relation_class_rationale"):
            G.fail(f"G08 {where}: {rel} requires relation_class_rationale in provenance")

    # G07 edge anchor admissibility
    anchors = e.get("evidence") or []
    if not anchors:
        G.fail(f"G07 {where}: edge without evidence")
    ok = False
    for a in anchors:
        if not anchor_ok(a, where):
            continue
        if a["kind"] == "MARK_SCHEME":
            if rel in MISCONCEPTION_RELATIONS:
                ok = True
            else:
                G.fail(f"G07 {where}: MARK_SCHEME anchor inadmissible for {rel} "
                       f"(assessment evidence is misconception-class only)")
        elif a["kind"] == "SPEC":
            sps = attached_sps(src) | attached_sps(tgt)
            if any(spec_wording_has(sp, a["quote"]) for sp in sps):
                ok = True
        elif a["kind"] == "NOTE":
            covered = attached_sps(src) | attached_sps(tgt)
            if any(note_maps_to(a["file"], sp) for sp in covered):
                ok = True
    if not ok:
        G.fail(f"G07 {where}: no anchor is admissible — every NOTE anchor's file "
               f"must HUMAN_VALIDATED-map to an SP attached to the source or "
               f"target concept (or the source practical's SP)")


# G08 acyclicity of REQUIRES_PREREQUISITE (concept endpoints only)
def has_cycle(adj):
    WHITE, GREY, BLACK = 0, 1, 2
    color = {k: WHITE for k in adj}
    found = []

    def dfs(u, stack):
        color[u] = GREY
        for v in sorted(adj.get(u, ())):
            if color.get(v, BLACK) == GREY:
                found.append(stack + [v])
            elif color.get(v, BLACK) == WHITE:
                dfs(v, stack + [v])
        color[u] = BLACK

    for u in sorted(adj):
        if color[u] == WHITE:
            dfs(u, [u])
    return found


cycles = has_cycle(prereq_adj)
if cycles:
    G.fail(f"G08 REQUIRES_PREREQUISITE cycle detected: {cycles[0]}")

# held list sanity (rendered into review artifacts, not the graph) —
# session-47: merged across the registry, ids unique across records
held = [h for r in recs for h in (r["dec"].get("held") or [])]
_held_owner = {}
for h in held:
    if h.get("id") in _held_owner:
        G.fail(f"G01 registry: held id {h.get('id')!r} duplicated across "
               f"records")
    _held_owner[h.get("id")] = True
for h in held:
    for k in ("id", "status", "candidate", "evidence", "reason"):
        if not h.get(k):
            G.fail(f"G01 held {h.get('id', '?')}: missing {k!r}")
    if h.get("status") not in ("held", "rejected"):
        G.fail(f"G01 held {h.get('id')}: status must be held|rejected")

# ---------------------------------------------------------------------------
# G13 promotions — the operator-side promotion record (architecture §18).
# Written ONLY by scripts/c11_promote.py; this gate is the fail-closed merge
# point. Zero promotions => emission is byte-identical to the pre-promotion
# contract (frozen pilot snapshot).
promo_index = {}
for i, p in enumerate(promotions):
    where = f"G13 promotion[{i}]"
    if not isinstance(p, dict):
        G.fail(f"{where}: entry must be a mapping, got {type(p).__name__}")
        continue
    edge = p.get("edge")
    if not isinstance(edge, dict):
        G.fail(f"{where}: 'edge' must be a mapping {{source, relation, target}}")
        continue
    src, rel, tgt = edge.get("source"), edge.get("relation"), edge.get("target")
    for k, v in (("source", src), ("relation", rel), ("target", tgt)):
        if not isinstance(v, str) or not v.strip():
            G.fail(f"{where}: edge.{k} missing/empty — exact identity required")
    if not (isinstance(src, str) and isinstance(rel, str) and isinstance(tgt, str)):
        continue
    key = (src, rel, tgt)
    if rel not in RELATIONS:
        G.fail(f"{where}: unknown relation {rel!r}")
        continue
    if rel == "PART_OF":
        G.fail(f"{where}: PART_OF is derived — not promotable via this pathway")
        continue
    if key in promo_index:
        G.fail(f"{where}: duplicate promotion for {src} {rel} {tgt}")
        continue
    by, dt = p.get("validated_by"), p.get("validated_date")
    if not isinstance(by, str) or not by.strip():
        G.fail(f"{where}: validated_by missing — promotion is operator-only")
    elif AI_NAME_RE.search(by):
        G.fail(f"{where}: validated_by {by!r} fails the attribution gate — "
               f"AI cannot promote (anti-forgery; G10's operator-only rule)")
    if not isinstance(dt, str) or not RE_ISO_DATE.match(dt or ""):
        G.fail(f"{where}: validated_date must be YYYY-MM-DD, got {dt!r}")
    ref = p.get("review_reference")
    if not isinstance(ref, str) or not ref.strip():
        G.fail(f"{where}: review_reference must name the ratifying review "
               f"artifact")
    else:
        first = ref.split()[0]
        if first.endswith((".md", ".json", ".yaml")) and not (REPO / first).exists():
            G.fail(f"{where}: review_reference file not found: {first}")
    if key not in edge_seen:
        # precise diagnosis for identities that are not authored edges
        # (held-candidate texts use the compact no-prefix form)
        s_, t_ = src.removeprefix("4CH1-"), tgt.removeprefix("4CH1-")
        hit = next((h.get("id") for h in held
                    if s_ in str(h.get("candidate", ""))
                    and t_ in str(h.get("candidate", ""))
                    and rel in str(h.get("candidate", ""))), None)
        if hit:
            G.fail(f"{where}: {src} {rel} {tgt} is held candidate {hit} — "
                   f"held/rejected candidates are not promotable (they are "
                   f"not edges; re-author the decision record instead)")
        else:
            G.fail(f"{where}: no authored edge matches the exact identity "
                   f"{src} {rel} {tgt} — promotion operates on existing "
                   f"authored-edge identities only")
        continue
    promo_index[key] = p

# ---------------------------------------------------------------------------
# G19 attachment promotions — the T-C19 operator-side record (the expansion
# round named by c11_promote.py's PART_OF refusal). Same fail-closed discipline
# as G13: shape, attribution (AI self-attribution forbidden), ISO date, a
# review artifact that exists, exact attachment identity (a CONCEPT node's
# declared spec_points entry), no duplicates. Zero c19 entries => emission is
# byte-identical to the pre-T-C19 contract.
c19_index = {}
node_by_code = {n.get("code"): n for n in nodes}
for i, p in enumerate(c19_promotions):
    where = f"G19 attachment-promotion[{i}]"
    if not isinstance(p, dict):
        G.fail(f"{where}: entry must be a mapping, got {type(p).__name__}")
        continue
    att = p.get("attachment")
    if not isinstance(att, dict):
        G.fail(f"{where}: 'attachment' must be a mapping {{concept, spec_point}}")
        continue
    con, spc = att.get("concept"), att.get("spec_point")
    for k, v in (("concept", con), ("spec_point", spc)):
        if not isinstance(v, str) or not v.strip():
            G.fail(f"{where}: attachment.{k} missing/empty — exact identity required")
    if not (isinstance(con, str) and isinstance(spc, str)):
        continue
    key = (con, spc)
    if key in c19_index:
        G.fail(f"{where}: duplicate promotion for {con} PART_OF {spc}")
        continue
    by, dt = p.get("validated_by"), p.get("validated_date")
    if not isinstance(by, str) or not by.strip():
        G.fail(f"{where}: validated_by missing — promotion is operator-only")
    elif AI_NAME_RE.search(by):
        G.fail(f"{where}: validated_by {by!r} fails the attribution gate — "
               f"AI cannot promote (anti-forgery; operator-only rule)")
    if not isinstance(dt, str) or not RE_ISO_DATE.match(dt or ""):
        G.fail(f"{where}: validated_date must be YYYY-MM-DD, got {dt!r}")
    ref = p.get("review_reference")
    if not isinstance(ref, str) or not ref.strip():
        G.fail(f"{where}: review_reference must name the ratifying review artifact")
    else:
        first = ref.split()[0]
        if first.endswith((".md", ".json", ".yaml")) and not (REPO / first).exists():
            G.fail(f"{where}: review_reference file not found: {first}")
    n = node_by_code.get(con)
    if n is None:
        G.fail(f"{where}: no CONCEPT node matches {con} — attachment promotion "
               f"operates on existing node attachments only")
    elif n.get("family") != "CONCEPT":
        G.fail(f"{where}: {con} is not a CONCEPT node — attachments exist only "
               f"on CONCEPT nodes")
    else:
        declared = {s.get("code") for s in (n.get("spec_points") or [])}
        if spc not in declared:
            G.fail(f"{where}: {con} declares no attachment to {spc} — "
                   f"attachment promotion operates on existing attachments only")
    c19_index[key] = p

# ---------------------------------------------------------------------------
# Emit
def emit(path: Path, meta: dict, key: str, records: list, header: str):
    lines = [header]
    doc = {"meta": meta, key: records}
    body = yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100,
                          default_flow_style=False)
    path.write_text(lines[0] + "\n" + body, encoding="utf-8")


def build_meta(kind: str, counts: dict) -> dict:
    # session-47: the emitted store meta is a pure function of the record
    # registry (pilot first, then each authorized §16 batch). stage/scope
    # describe the merged store; extraction_pass + decision_record list
    # every contributing record; generated = the newest record date.
    meta = {
        "task": "T-C11",
        "stage": "+".join(r["stage"] for r in recs),
        "curriculum_code": "4CH1-2017",
        "phase": 3,
        "scope": ("PILOT_SLICE_1_25_1_36 (architecture §14) + S16_BATCH_1 "
                  "SLICE_1_1_1_12 (architecture §16; authorized 2026-09-12, "
                  "scripts/c11_s16_authorization.yaml; per-batch operator "
                  "gate before any promotion) + S16_BATCH_2 SLICE_1_13_1_24 "
                  "(architecture §16; batch 2 commissioned 2026-09-12; same "
                  "per-batch operator gate)"),
        "spec_points": ALL_SPS,
        "practicals": ALL_PRACTICALS,
        "negative_control": NEGATIVE_CONTROL,
        "generator": "scripts/c11_concept_pilot.py",
        "decision_record": [r["path"] for r in recs],
        "extraction_pass": [r["pass"] for r in recs],
        "model_version": recs[0]["dec"]["meta"]["model_version"],
        "contract": "graph/reports/C11_ARCHITECTURE.md",
        "generated": max(r["date"] for r in recs),
        "provenance_default": "AI_SUGGESTED",
        "validation_gate": "operator review (pilot: graph/reports/"
                           "C11_PILOT_REVIEW_SHEET.md; batch 1: graph/reports/"
                           "C11_BATCH1_REVIEW_SHEET.md; batch 2: graph/reports/"
                           "C11_BATCH2_REVIEW_SHEET.md) — no promotion from "
                           "generation; HUMAN_VALIDATED is operator-only",
        "edge_vocabulary": "V2 knowledge_edges enum + COMMONLY_CONFUSED_WITH + "
                            "WRONG_ANSWER_PATTERN (frozen §8A.11 triple distinction; "
                            "V2 projection documented in C11_ARCHITECTURE.md §13)",
        "counts": counts,
    }
    if promo_index and kind == "edges":
        # present ONLY on the edges file and ONLY when promotions exist —
        # zero promotions keeps the emission byte-identical to the frozen
        # pilot snapshot; nodes/command-kinds are never promotable here
        meta["promotion_record"] = "scripts/c11_promotions.yaml"
    if c19_index and kind == "edges":
        # T-C19: same additivity contract for the attachment-promotion record
        meta["attachment_promotion_record"] = "scripts/c19_promotions.yaml"
    return meta


def node_out(n):
    rec = {k: n.get(k) for k in NODE_KEYS if n.get(k) is not None}
    return rec


def edge_out(e, role=None):
    rec = {}
    promo = promo_index.get((e.get("source"), e.get("relation"), e.get("target")))
    for k in EDGE_KEYS:
        if k == "role":
            if role:
                rec["role"] = role
        elif k == "validation_status":
            if promo:
                # §18: promotion adds ONLY the validation fields; evidence,
                # provenance, confidence, ambiguity_note are preserved verbatim
                rec["validation_status"] = "HUMAN_VALIDATED"
                rec["validated_by"] = promo["validated_by"]
                rec["validated_date"] = promo["validated_date"]
            elif e.get(k) is not None:
                rec["validation_status"] = e.get(k)
        elif e.get(k) is not None:
            rec[k] = e.get(k)
    return rec


if not G.ok:
    print(f"FAIL: {len(G.failures)} gate failure(s):", file=sys.stderr)
    for f in G.failures:
        print(f"  - {f}", file=sys.stderr)
    sys.exit(1)

# derived PART_OF edges
part_of = []
for n in sorted([n for n in nodes if n.get("family") == "CONCEPT"],
                key=lambda x: x["code"]):
    for att in n["spec_points"]:
        rec = {
            "source": n["code"],
            "relation": "PART_OF",
            "target": att["code"],
            "role": att["role"],
            "evidence": att["evidence"],
            "provenance": dict(n["provenance"]),
            "confidence": n["confidence"],
            "validation_status": n["validation_status"],
            "ambiguity_note": None,
            "version": 1,
            "created_at": node_rec[n["code"]]["date"],
        }
        # T-C19: an operator-validated attachment row carries HUMAN_VALIDATED on
        # the EDGE only (the mapping is human-confirmed; the concept NODE keeps
        # its own status — scope guard: nodes are never promoted by this lane).
        # Promotion adds ONLY the validation fields, mirroring edge_out's §18
        # behavior; evidence/provenance/confidence are preserved verbatim and
        # provenance.tier stays AI_SUGGESTED (origin is immutable).
        c19p = c19_index.get((n["code"], att["code"]))
        if c19p:
            rec["validation_status"] = "HUMAN_VALIDATED"
            rec["validated_by"] = c19p["validated_by"]
            rec["validated_date"] = c19p["validated_date"]
        part_of.append(rec)

authored = [edge_out(e) for e in edges]
all_edges = part_of + authored
order = {r: i for i, r in enumerate(["PART_OF", "REQUIRES_PREREQUISITE", "EXPLAINED_BY",
                                     "RELATED_TO", "COMMONLY_CONFUSED_WITH",
                                     "MISCONCEPTION_OF", "WRONG_ANSWER_PATTERN",
                                     "REMEDIATED_BY"])}
all_edges.sort(key=lambda e: (order[e["relation"]], e["source"], e["target"]))

counts_nodes = {
    "nodes": len(nodes),
    "concepts": sum(1 for n in nodes if n.get("family") == "CONCEPT"),
    "misconceptions": sum(1 for n in nodes if n.get("family") == "MISCONCEPTION"),
    "part_of_edges": len(part_of),
    "semantic_edges": len(authored),
}
counts_edges = {
    "edges": len(all_edges),
    **{f"{r.lower()}_edges": sum(1 for e in all_edges if e["relation"] == r)
       for r in sorted(order)},
    "review_required_edges": sum(1 for e in all_edges
                                 if e["validation_status"] == "REVIEW_REQUIRED"),
}
if promo_index:
    counts_edges["promoted_edges"] = sum(
        1 for e in all_edges if e["validation_status"] == "HUMAN_VALIDATED")
    counts_edges["human_validated_edges"] = counts_edges["promoted_edges"]
counts_ck = {"spec_points": len(cks)}

dry = "--dry-run" in sys.argv
HDR = ("# SyllabAI 4CH1 concept graph (pilot + §16 batches 1-2) — T-C11, "
       "graph-as-code (KNOWLEDGE_GRAPH_CONTEXT.md §8A.14, C11_ARCHITECTURE.md §10)\n"
       "# Generated by scripts/c11_concept_pilot.py from the decision-record "
       "registry:\n"
       + "".join(f"#   {r['path']} (extraction_pass {r['pass']})\n" for r in recs)
       + "# DO NOT hand-edit: re-run the script. Provenance tier AI_SUGGESTED; "
       "validation gate = operator review (see meta.validation_gate).\n"
       f"# Generation dates pinned per record; store date "
       f"{max(r['date'] for r in recs)} (deterministic contract; "
       "byte-identical re-runs).\n")

def _c23_apply_quote_map(records, is_node):
    """T-C23: emit the definitive (re-anchored) SPEC quotes for entries the
    C23 swap record re-anchored; frozen decision records stay untouched."""
    if not _C23_NEW:
        return records
    for r in records:
        pairs = ([(a.get("code"), a.get("evidence"))
                  for a in r.get("spec_points") or []]
                 if is_node else [(r.get("target"), r.get("evidence"))])
        for sp, evs in pairs:
            for a in evs or []:
                if (a.get("kind") == "SPEC"
                        and a.get("file") == GP.store_rel("specification_points")):
                    # Session-55 repair (dated): the re-anchor chain composes
                    # C23 -> C24 — iterate to fixpoint (bounded) so a C24
                    # re-anchor OF a C23 new_quote applies in one emission.
                    q = a.get("quote")
                    for _ in range(4):
                        key = (sp, q)
                        if key not in _C23_NEW:
                            break
                        q = _C23_NEW[key]
                    a["quote"] = q
    return records


def canonicalize_anchor_files(records, is_node):
    """Session-55 repair (2026-09-22, dated): the frozen decision records
    carry the historical root-form SPEC anchor path (C28 P5 — records stay
    historical); the EMITTED stores carry the canonical registry-resolved
    path (the C28 stage-2 canonicalized form). Resolve every anchor file
    through the registry legacy_map before emission so the C23 quote-map
    matches and the stores stay canonical. Pure function of the records +
    registry (determinism preserved)."""
    for r in records:
        if is_node:
            ev_groups = ([a.get("evidence") or []
                          for a in r.get("spec_points") or []]
                         + [r.get("evidence") or []]
                         + [r.get("remediation_evidence") or []])
        else:
            ev_groups = [r.get("evidence") or []]
        for evs in ev_groups:
            for a in evs:
                if a.get("file"):
                    a["file"] = GP.resolve_rel(a["file"])
    return records


if not dry:
    canonicalize_anchor_files(nodes, True)
    canonicalize_anchor_files(all_edges, False)
    emit(GRAPH / "concepts.yaml", build_meta("nodes", counts_nodes), "nodes",
         [_c23_apply_quote_map([node_out(n)], True)[0]
          for n in sorted(nodes, key=lambda x: (x["family"], x["code"]))],
         HDR)
    emit(GRAPH / "concept_edges.yaml", build_meta("edges", counts_edges), "edges",
         _c23_apply_quote_map(all_edges, False), HDR)
    emit(GRAPH / "spec_command_kinds.yaml", build_meta("command_kinds", counts_ck),
         "command_kinds",
         sorted(cks, key=lambda x: x["code"]), HDR)

_rec_sum = ", ".join(f"{r['name']} ({len(r['dec'].get('nodes') or [])} nodes)"
                     for r in recs)
print(f"ALL GATES GREEN ({len(nodes)} nodes / {len(all_edges)} edges "
      f"[{len(part_of)} PART_OF + {len(authored)} semantic] / "
      f"{len(cks)} command kinds / {len(held)} held; records: {_rec_sum})"
      + (f" / {len(promo_index)} promoted edge(s) HUMAN_VALIDATED (operator "
         f"promotions, §18)" if promo_index else
         " / 0 promoted (HUMAN_VALIDATED is operator-only)"))
print(f"T-C10 crosscheck: 209/209 HUMAN_VALIDATED mappings indexed; "
      f"negative control {NEGATIVE_CONTROL}: 0 attachments"
      + ("" if dry else f"\nwrote graph/igcse-chemistry/concepts, graph/igcse-chemistry/concept_edges, "
                        f"graph/igcse-chemistry/spec_command_kinds"))
