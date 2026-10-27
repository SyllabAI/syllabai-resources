#!/usr/bin/env python3
"""
T-C41 — c41_maths_a_promote.py: operator-only promotion of EXACT authored-edge
identities to HUMAN_VALIDATED for igcse-maths-a (the c11_promote.py §18
mechanism instantiated for the maths-a Lane C surface).

Promotion path (graph/reports/C11_ARCHITECTURE.md §18; the C39 verdict record's
own designation of this round as "a separate operator gate"):

  operator command  ->  scripts/c41_maths_a_promotions.yaml  (this tool, the
  only writer)  ->  scripts/c41_maths_a_promotion_apply.py  (the gated merge
  point, G13 convention)  ->  graph/igcse-maths-a/concept_edges carries
  HUMAN_VALIDATED + validated_by/validated_date on exactly the promoted edges.

The AI decision records (c33..c38_maths_a_batch0*_decisions.yaml) are NEVER
touched. Promotions live in their own operator-side record; the applier merges
deterministically. Hand-edits of the graph are rejected by the promotion check
(c41_maths_a_promotion_check.py — the c11.13 analog).

Hard properties (all fail closed):
  * exact identity only — each --edge spec must be 'SOURCE RELATION TARGET'
    (3 whitespace-separated tokens); wildcards, partial specs, and promotion
    by node or relation type alone are rejected;
  * only existing AUTHORED semantic edges are promotable (PART_OF is derived;
    the 45 held candidates are not edges and are never promotable — a held
    match aborts with its id);
  * evidence is pre-verified before anything is written (every anchor quote
    must byte-verify in its cited file — T-C10 norm());
  * attribution gate — validated_by matching AI-name patterns fails closed
    (the promotions record may never carry AI attribution);
  * DC-04 aware — the store-side identity 4MA1-CON-INDEX-LAWS-SIMPLE-CASES
    (the C39 emission-time namespace disambiguation) maps back to the
    decision-record identity 4MA1-CON-INDEX-LAWS for authored-index lookup;
  * idempotent — re-promoting the same identity is a reported no-op;
  * deterministic — the promotions file is a pure operator-side record;
    the applier re-run is byte-identical.

Usage (the T-C41 round — all 73 authored semantic edges, the operator's
2026-10-02 zai-web directive "run the §18 HUMAN_VALIDATED promotion round over
the 73 edges"; identities enumerated from the landed store):
  python3 scripts/c41_maths_a_promote.py --edge 'SRC REL TGT' ... \
      --review-ref graph/reports/C39_K2C_CONSOLIDATED_OPERATOR_REVIEW.md \
      --by operator --date 2026-10-02

Exit 0 = promotions recorded + applier green (unless --no-apply).
"""
from __future__ import annotations

import argparse
import datetime
import os
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
DECISION_FILES = [f"c{32 + n}_maths_a_batch0{n}_decisions.yaml" for n in range(1, 7)]
PROMOTIONS = HERE / "c41_maths_a_promotions.yaml"

RELATIONS = {"REQUIRES_PREREQUISITE", "WRONG_ANSWER_PATTERN", "REMEDIATED_BY"}
BANDS = {"high", "medium", "low"}
PROV_KEYS = ("tier", "model_version", "extraction_pass", "generated_date",
             "derivation_method")
RE_ISO_DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
AI_NAME_RE = re.compile(r"glm|super\s*z|gpt|claude|openai|anthropic|\bai\b"
                        r"|llm|agent|model|bot", re.I)
# DC-04 (C39 apply record): store-side identity -> decision-record identity
DC04_REVERSE = {"4MA1-CON-INDEX-LAWS-SIMPLE-CASES": "4MA1-CON-INDEX-LAWS"}

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


def die(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def normed_file(rel: str):
    p = REPO / rel
    if not p.exists():
        # the sparse workspace keeps non-checkout paths in git only
        r = subprocess_run_git(rel)
        return r
    return norm(p.read_text(encoding="utf-8"))


def subprocess_run_git(rel: str):
    import subprocess
    r = subprocess.run(["git", "-C", str(REPO), "show", f"HEAD:{rel}"],
                       capture_output=True, text=True)
    if r.returncode != 0:
        return None
    return norm(r.stdout)


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
        die(f"--edge {spec!r}: unknown relation {rel!r} (the maths-a "
            f"vocabulary: {sorted(RELATIONS)})")
    if not src.startswith("4MA1-") or not tgt.startswith("4MA1-"):
        die(f"--edge {spec!r}: endpoints must be 4MA1-* codes")
    return src, rel, tgt


def main() -> int:
    ap = argparse.ArgumentParser(description="T-C41 maths-a exact-edge-identity "
                                             "promotion (operator-only)")
    ap.add_argument("--edge", action="append", required=True, metavar="'SRC REL TGT'",
                    help="exact authored-edge identity (repeatable)")
    ap.add_argument("--review-ref",
                    default="graph/reports/C39_K2C_CONSOLIDATED_OPERATOR_REVIEW.md",
                    help="review artifact that ratified the edge(s)")
    ap.add_argument("--by", default="operator", help="validator identity")
    ap.add_argument("--date", default=datetime.date.today().isoformat(),
                    help="promotion date (YYYY-MM-DD)")
    ap.add_argument("--no-apply", action="store_true",
                    help="record the promotions only; skip the applier")
    args = ap.parse_args()

    if not RE_ISO_DATE.match(args.date):
        die(f"--date must be YYYY-MM-DD, got {args.date!r}")
    if not args.by or AI_NAME_RE.search(args.by):
        die(f"--by {args.by!r} fails the attribution gate: promotion is "
            f"operator-only and AI self-attribution is forbidden (fail closed)")
    if not args.review_ref:
        die("--review-ref must name the review artifact that ratified the edge")

    edges, held = [], []
    edge_source = {}   # decision-record identity -> decision record it came from
    for name in DECISION_FILES:
        d = yaml.safe_load((HERE / name).read_text(encoding="utf-8"))
        for _e in (d.get("edges") or []):
            edge_source[(_e["source"], _e["relation"], _e["target"])] = name
        edges.extend(d.get("edges") or [])
        held.extend(d.get("held") or [])
    authored = {(e["source"], e["relation"], e["target"]): e for e in edges}

    def held_hint(src: str, rel: str, tgt: str):
        s, t = src.removeprefix("4MA1-"), tgt.removeprefix("4MA1-")
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
        dec_key = (DC04_REVERSE.get(src, src), rel, DC04_REVERSE.get(tgt, tgt))
        if (src, rel, tgt) in authored:
            e = authored[(src, rel, tgt)]
        elif dec_key in authored:
            e = authored[dec_key]
        else:
            hit = held_hint(src, rel, tgt) or held_hint(*dec_key)
            if hit:
                die(f"no authored edge matches {src} {rel} {tgt}: this "
                    f"identity is held candidate {hit} — held/rejected "
                    f"candidates are NOT promotable (they are not edges; "
                    f"re-author the decision record after operator review)")
            die(f"no authored edge matches the exact identity "
                f"{src} {rel} {tgt} — promotion operates on existing "
                f"authored-edge identities only")
        where = f"edge {src} -[{rel}]-> {tgt}"
        anchors = e.get("evidence") or []
        if not anchors:
            die(f"{where}: the edge carries no evidence — fail closed "
                f"(malformed or missing evidence is not promotable)")
        for a in anchors:
            if not isinstance(a, dict) or a.get("kind") not in ("NOTE", "SPEC", "MARK_SCHEME"):
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
        if not e.get("derivation") and not prov.get("derivation_method"):
            die(f"{where}: derivation missing — fail closed")
        conf = e.get("conf") or e.get("confidence") or "high"
        if conf not in BANDS:
            die(f"{where}: confidence {conf!r} not in bands")

    # ---- load existing promotions (idempotence) -----------------------------
    if PROMOTIONS.exists():
        promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    else:
        promo = {"meta": {"task": "T-C41", "stage": "s18-promotion"},
                 "promotions": []}
    entries = promo.get("promotions") or []
    existing = {(p["edge"]["source"], p["edge"]["relation"],
                 p["edge"]["target"]): p for p in entries}

    promoted, noop, promoted_tuples = [], [], []
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
        promoted_tuples.append((src, rel, tgt))

    if promoted:
        entries.sort(key=lambda p: (p["edge"]["relation"], p["edge"]["source"],
                                    p["edge"]["target"]))
        promo["promotions"] = entries
        meta = promo.setdefault("meta", {})
        meta.update({
            "task": "T-C41", "stage": "s18-promotion",
            "contract": "graph/reports/C11_ARCHITECTURE.md §18; the C39 verdict "
                        "record's promotion_authorization (the exact-identity §18 "
                        "promotion round as the separate operator gate)",
            "operator_directive": ("fire K2-B (chunk substrate), run the §18 "
                                   "HUMAN_VALIDATED promotion round over the 73 "
                                   "edges — 2026-10-02, zai-web"),
            "decision_record": ", ".join(sorted(
                {f"scripts/{edge_source[(DC04_REVERSE.get(s, s), r, DC04_REVERSE.get(t2, t2))] if (DC04_REVERSE.get(s, s), r, DC04_REVERSE.get(t2, t2)) in edge_source else edge_source[(s, r, t2)]}"
                 for s, r, t2 in promoted_tuples})),
            "tool": "scripts/c41_maths_a_promote.py",
            "generated_date": meta.get("generated_date") or args.date,
        })
        promo_text = (
            "# T-C41 promotion record — operator ratifications of exact edge "
            "identities (igcse-maths-a).\n# Written ONLY by "
            "scripts/c41_maths_a_promote.py; see graph/reports/C11_ARCHITECTURE.md "
            "§18. Hand-editing is forbidden.\n"
            + yaml.safe_dump(promo, allow_unicode=True, sort_keys=False, width=100))
        yaml.safe_load(promo_text)  # fail-closed: parse before replacing the record
        _tmp = PROMOTIONS.with_suffix(".yaml.tmp")
        _tmp.write_text(promo_text, encoding="utf-8")
        os.replace(_tmp, PROMOTIONS)  # atomic: no truncated promotion record
        print(f"promotions recorded: {PROMOTIONS.name} "
              f"({len(promoted)} new, {len(noop)} no-op)")
        for m in promoted:
            print("PROMOTED", m)
    for m in noop:
        print("-", m)
    if not promoted and not noop:
        print("nothing to do")
        return 0

    if args.no_apply:
        print("next: the §18 promotion lands in graph/igcse-maths-a/concept_edges "
              "after scripts/c41_maths_a_promotion_apply.py runs (G13-convention "
              "gate validates every promotion entry)")
        return 0
    r = subprocess.run([sys.executable, str(HERE / "c41_maths_a_promotion_apply.py")],
                       cwd=REPO)
    if r.returncode != 0:
        print("NOTE: the applier rejected the state — the promotions file "
              "retains the entries above and the promotion check will flag the "
              "graph/promotions mismatch; fix the underlying evidence or "
              "revert the promotions file via git.", file=sys.stderr)
    return r.returncode


if __name__ == "__main__":
    sys.exit(main())
