#!/usr/bin/env python3
"""
T-C11 — c11_promote.py: operator-only promotion of EXACT authored-edge
identities to HUMAN_VALIDATED (c10_promote pattern, decisions-side).

Promotion path (graph/reports/C11_ARCHITECTURE.md §18):

  operator command  ->  scripts/c11_promotions.yaml  (this tool, the only
  writer)  ->  gated generator re-run (c11_concept_pilot.py G13)  ->
  graph/concept_edges.yaml carries HUMAN_VALIDATED + validated_by/date.

The AI decision record (scripts/c11_pilot_decisions.yaml) is NEVER touched:
it is the frozen pilot snapshot. Promotions live in their own operator-side
record; the generator merges both deterministically. Hand-edits of the graph
are reverted by re-runs and rejected by graph_check (c11.10).

Hard properties (all fail closed, all negative-tested in
scripts/c11_promote_test.py):
  * exact identity only — each --edge spec must be 'SOURCE RELATION TARGET'
    (3 whitespace-separated tokens); wildcards, partial specs, and promotion
    by node or relation type alone are rejected;
  * only existing AUTHORED semantic edges are promotable (PART_OF is derived;
    held/rejected candidates are not edges and are never promotable);
  * evidence is pre-verified before anything is written (every anchor quote
    must byte-verify in its cited file — T-C10 norm());
  * the generator re-run is the authoritative gate: malformed or missing
    evidence, AI self-attribution, unknown identities — all abort with the
    promotions file left auditable (the checker flags any graph/promotions
    mismatch, so a failed apply cannot silently pass);
  * idempotent — re-promoting the same identity is a reported no-op;
  * deterministic — promotion state is a pure function of
    (decision record, promotions file); regeneration is byte-identical.

Usage:
  python3 scripts/c11_promote.py \
      --edge '4CH1-CON-MOLAR-MASS REQUIRES_PREREQUISITE 4CH1-CON-MOLE' \
      [--review-ref 'graph/reports/C11_PILOT_REVIEW_SHEET.md §3.2 row 2'] \
      [--by operator] [--date 2026-09-11] [--no-apply]

Exit 0 = promotions recorded + generator green (unless --no-apply).
"""
from __future__ import annotations

import argparse
import datetime
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
# Session-47 (§16 batch 1, 2026-09-12): the decision-record REGISTRY (same
# list as the generator's) — promotion resolves exact authored-edge
# identities and held-candidate rejections over the MERGED surface, so §18
# promotions work identically for pilot and batch edges.
# Session-49 (batch 2): the registry grows by c11_batch2_decisions.yaml
DECISION_FILES = ["c11_pilot_decisions.yaml", "c11_batch1_decisions.yaml",
                  "c11_batch2_decisions.yaml"]
PROMOTIONS = HERE / "c11_promotions.yaml"

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

# T-C10 norm() convention (shared anti-hallucination normalisation; same as
# c11_concept_pilot.py / graph_check.py / c10_map_notes.py)
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


def die(msg: str) -> "None":
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def load_yaml(path: Path):
    try:
        return yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as e:
        die(f"{path.name} does not parse: {e}")


def normed_file(rel: str):
    p = REPO / rel
    if not p.exists():
        return None
    return norm(p.read_text(encoding="utf-8"))


def parse_edge_spec(spec: str):
    """Exact identity: exactly 3 whitespace-separated tokens."""
    toks = spec.split()
    if len(toks) != 3:
        die(f"--edge {spec!r} is not an exact identity: the spec must be "
            f"'SOURCE RELATION TARGET' (3 whitespace-separated tokens). "
            f"Wildcards, partial specs, and promotion by node or relation "
            f"type alone are not supported (fail closed).")
    src, rel, tgt = toks
    if rel not in RELATIONS:
        die(f"--edge {spec!r}: unknown relation {rel!r} (vocabulary: "
            f"{sorted(RELATIONS)})")
    if rel == "PART_OF":
        die(f"--edge {spec!r}: PART_OF edges are DERIVED from node "
            f"attachments and are not promotable via this pathway (node "
            f"promotion is a separate identity decision, expansion round).")
    if not src.startswith("4CH1-") or not tgt.startswith("4CH1-"):
        die(f"--edge {spec!r}: endpoints must be 4CH1-* codes")
    return src, rel, tgt


def main() -> int:
    ap = argparse.ArgumentParser(description="T-C11 exact-edge-identity "
                                             "promotion (operator-only)")
    ap.add_argument("--edge", action="append", required=True, metavar="'SRC REL TGT'",
                    help="exact authored-edge identity (repeatable)")
    ap.add_argument("--review-ref", default="graph/reports/C11_PILOT_REVIEW_SHEET.md",
                    help="review artifact that ratified the edge(s)")
    ap.add_argument("--by", default="operator", help="validator identity")
    ap.add_argument("--date", default=datetime.date.today().isoformat(),
                    help="promotion date (YYYY-MM-DD)")
    ap.add_argument("--no-apply", action="store_true",
                    help="record the promotions only; skip the generator re-run")
    args = ap.parse_args()

    if not RE_ISO_DATE.match(args.date):
        die(f"--date must be YYYY-MM-DD, got {args.date!r}")
    if not args.by or AI_NAME_RE.search(args.by):
        die(f"--by {args.by!r} fails the attribution gate: promotion is "
            f"operator-only and AI self-attribution is forbidden (fail closed)")
    if not args.review_ref:
        die("--review-ref must name the review artifact that ratified the edge")

    edges, held = [], []
    for name in DECISION_FILES:
        d = load_yaml(HERE / name)
        edges.extend(d.get("edges") or [])
        held.extend(d.get("held") or [])

    authored = {(e["source"], e["relation"], e["target"]): e for e in edges}

    def held_hint(src: str, rel: str, tgt: str):
        """Held-candidate texts are written in the compact no-prefix form
        (e.g. 'REQUIRES_PREREQUISITE(CON-GAS-VOL-CALC, CON-MOLE)')."""
        s, t = src.removeprefix("4CH1-"), tgt.removeprefix("4CH1-")
        for h in held:
            cand = str(h.get("candidate", ""))
            if s in cand and t in cand and rel in cand:
                return h.get("id")
        return None

    targets = [parse_edge_spec(s) for s in args.edge]
    if len(set(targets)) != len(targets):
        die("duplicate --edge identities in one command")

    # ---- pre-verification (fail closed BEFORE anything is written) ----------
    for src, rel, tgt in targets:
        key = (src, rel, tgt)
        if key not in authored:
            hit = held_hint(src, rel, tgt)
            if hit:
                die(f"no authored edge matches {src} {rel} {tgt}: this "
                    f"identity is held candidate {hit} — held/rejected "
                    f"candidates are NOT promotable (they are not edges; "
                    f"re-author the decision record after operator review)")
            die(f"no authored edge matches the exact identity "
                f"{src} {rel} {tgt} — promotion operates on existing "
                f"authored-edge identities only")
        e = authored[key]
        where = f"edge {src} -[{rel}]-> {tgt}"
        anchors = e.get("evidence") or []
        if not anchors:
            die(f"{where}: the edge carries no evidence — fail closed "
                f"(malformed or missing evidence is not promotable)")
        for a in anchors:
            if not isinstance(a, dict) or a.get("kind") not in ANCHOR_KINDS:
                die(f"{where}: malformed evidence anchor {a!r} — fail closed")
            relf, quote = a.get("file"), a.get("quote")
            if not relf or not quote:
                die(f"{where}: evidence anchor missing file/quote — fail closed")
            body = normed_file(relf)
            if body is None:
                die(f"{where}: evidence file missing: {relf} — fail closed")
            if norm(quote) not in body:
                die(f"{where}: evidence quote does NOT byte-verify in {relf} "
                    f"— fail closed :: {quote[:70]!r}")
        prov = e.get("provenance") or {}
        for k in PROV_KEYS:
            if not prov.get(k):
                die(f"{where}: provenance.{k} missing — fail closed")
        if e.get("confidence") not in BANDS:
            die(f"{where}: confidence {e.get('confidence')!r} not in bands")

    # ---- load existing promotions (idempotence) -----------------------------
    promo = load_yaml(PROMOTIONS) if PROMOTIONS.exists() else {
        "meta": {"task": "T-C11", "stage": "pilot-promotion"},
        "promotions": []}
    entries = promo.get("promotions") or []
    existing = {(p["edge"]["source"], p["edge"]["relation"],
                 p["edge"]["target"]): p for p in entries}

    promoted, noop = [], []
    for src, rel, tgt in targets:
        if (src, rel, tgt) in existing:
            p = existing[(src, rel, tgt)]
            noop.append(f"{src} {rel} {tgt} (already promoted by "
                        f"{p.get('validated_by')} on {p.get('validated_date')})")
            continue
        entries.append({
            "edge": {"source": src, "relation": rel, "target": tgt},
            "validated_by": args.by,
            "validated_date": args.date,
            "review_reference": args.review_ref,
        })
        promoted.append(f"{src} {rel} {tgt}")

    if promoted:
        entries.sort(key=lambda p: (p["edge"]["source"], p["edge"]["relation"],
                                    p["edge"]["target"]))
        promo["promotions"] = entries
        meta = promo.setdefault("meta", {})
        meta.update({
            "task": "T-C11", "stage": "pilot-promotion",
            "contract": "graph/reports/C11_ARCHITECTURE.md §18",
            "decision_record": "scripts/c11_pilot_decisions.yaml",
            "tool": "scripts/c11_promote.py",
            "generated_date": meta.get("generated_date") or args.date,
        })
        PROMOTIONS.write_text(
            "# T-C11 promotion record — operator ratifications of exact edge "
            "identities.\n# Written ONLY by scripts/c11_promote.py; see "
            "graph/reports/C11_ARCHITECTURE.md §18. Hand-editing is forbidden.\n"
            + yaml.safe_dump(promo, allow_unicode=True, sort_keys=False, width=100),
            encoding="utf-8")
        print(f"promotions recorded: {PROMOTIONS.name}")
        for m in promoted:
            print("PROMOTED", m)
    for m in noop:
        print("-", m)
    if not promoted and not noop:
        print("nothing to do")
        return 0

    if args.no_apply:
        print("next: graph/concept_edges.yaml carries the promotion after the "
              "gated generator re-run (G13 validates every promotion entry)")
        return 0
    r = subprocess.run([sys.executable, str(HERE / "c11_concept_pilot.py")],
                       cwd=REPO)
    if r.returncode != 0:
        print("NOTE: the generator rejected the state — the promotions file "
              "retains the entries above and graph_check will flag the "
              "graph/promotions mismatch; fix the underlying evidence or "
              "revert the promotions file via git.", file=sys.stderr)
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
