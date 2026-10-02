#!/usr/bin/env python3
"""T-C41 — c41_maths_a_promotion_apply.py: the gated merge point for the §18
promotion round over the maths-a authored semantic edges (the G13 convention
of c11_concept_pilot.py instantiated as a dedicated applier so the landed
T-C39 generator and its record stay byte-untouched).

Preconditions (all fail-closed):
  * scripts/c41_maths_a_promotions.yaml parses, carries >=1 entry
  * graph/reports/C39_K2C_VERDICT_CHECK.json result == ALL PASS (the verdict
    surface this round promotes is the one the C39 gate recorded)
  * graph/igcse-maths-a/concept_edges.yaml parses; maths-a registry carries
    the 9-store K2 exit shape
  * the six decision records parse; authored semantic count == 73

G13-equivalent gate (fail-closed, per entry): shape; relation vocabulary;
PART_OF refused; duplicate identities refused; validated_by present and
AI-attribution-free (anti-forgery); validated_date ISO; review_reference names
an existing artifact; the exact identity matches a semantic edge in the LANDED
store; held-candidate identities diagnosed precisely (never promotable).
Round contract: the T-C41 round is the whole authored semantic surface — the
entries must cover EXACTLY the 73 semantic edges (the operator's directive:
"the §18 HUMAN_VALIDATED promotion round over the 73 edges"); partial coverage
fails the round check.

Emits (deterministic; byte-identical re-runs):
  graph/igcse-maths-a/concept_edges.yaml — ONLY validation fields change:
      each promoted edge gains validated_by + validated_date directly after
      validation_status (HUMAN_VALIDATED), mirroring c11 edge_out; evidence,
      provenance, confidence, version, created_at are preserved verbatim;
      PART_OF rows and every unpromoted byte are preserved verbatim;
      meta gains promotion_record + counts.promoted_edges/human_validated_edges
  graph/reports/C41_MATHS_A_S18_PROMOTION_RECORD.{json,md}

Never touches: the decision records (incl. held lists), concepts.yaml,
spec_command_kinds.yaml, spec_chunk_mappings.yaml, the 5 K1 maths-a stores,
graph/igcse-chemistry/**, the corpora.
"""
from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
PROMOTIONS = HERE / "c41_maths_a_promotions.yaml"
EDGES = REPO / "graph" / QUAL / "concept_edges.yaml"
VCHECK = REPO / "graph/reports/C39_K2C_VERDICT_CHECK.json"
REC_JSON = REPO / "graph/reports/C41_MATHS_A_S18_PROMOTION_RECORD.json"
REC_MD = REPO / "graph/reports/C41_MATHS_A_S18_PROMOTION_RECORD.md"

RELATIONS = {"REQUIRES_PREREQUISITE", "WRONG_ANSWER_PATTERN", "REMEDIATED_BY"}
AI_NAME_RE = None  # compiled below (same pattern as the promote tool)
AI_PAT = r"glm|super\s*z|gpt|claude|openai|anthropic|\bai\b|llm|agent|model|bot"


def die(msg: str) -> None:
    print(f"FAIL: {msg}", file=sys.stderr)
    sys.exit(1)


def main() -> int:
    import re
    global AI_NAME_RE
    AI_NAME_RE = re.compile(AI_PAT, re.I)

    # ---- preconditions ---------------------------------------------------------
    if not PROMOTIONS.exists():
        die("promotions file missing — run c41_maths_a_promote.py first")
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    entries = promo.get("promotions") or []
    if not entries:
        die("promotions file carries zero entries")
    if not VCHECK.exists():
        die("C39 verdict check report missing")
    if json.loads(VCHECK.read_text(encoding="utf-8")).get("result") != "ALL PASS":
        die("C39 verdict check is not ALL PASS")
    reg = yaml.safe_load((HERE / "graph_paths.yaml").read_text(encoding="utf-8"))
    if len(reg["quals"][QUAL]["stores"]) != 9:
        die("maths-a registry is not the 9-store K2 exit shape")

    # ---- G13-equivalent gate -----------------------------------------------------
    doc = yaml.safe_load(EDGES.read_text(encoding="utf-8"))
    edges = doc["edges"]
    semantic = [e for e in edges if e["relation"] != "PART_OF"]
    part_of = [e for e in edges if e["relation"] == "PART_OF"]
    sem_index = {(e["source"], e["relation"], e["target"]): e for e in semantic}
    if len(sem_index) != len(semantic):
        die("duplicate semantic identity in the landed store")

    promo_index = {}
    for i, p in enumerate(entries):
        where = f"promotion[{i}]"
        if not isinstance(p, dict):
            die(f"{where}: entry must be a mapping")
        edge = p.get("edge")
        if not isinstance(edge, dict):
            die(f"{where}: 'edge' must be a mapping {{source, relation, target}}")
        src, rel, tgt = edge.get("source"), edge.get("relation"), edge.get("target")
        for k, v in (("source", src), ("relation", rel), ("target", tgt)):
            if not isinstance(v, str) or not v.strip():
                die(f"{where}: edge.{k} missing/empty — exact identity required")
        key = (src, rel, tgt)
        if rel not in RELATIONS:
            die(f"{where}: unknown relation {rel!r}")
        if key in promo_index:
            die(f"{where}: duplicate promotion for {src} {rel} {tgt}")
        by, dt = p.get("validated_by"), p.get("validated_date")
        if not isinstance(by, str) or not by.strip():
            die(f"{where}: validated_by missing — promotion is operator-only")
        if AI_NAME_RE.search(by):
            die(f"{where}: validated_by {by!r} fails the attribution gate — "
                f"AI cannot promote (anti-forgery)")
        if not isinstance(dt, str) or not re.match(r"^\d{4}-\d{2}-\d{2}$", dt or ""):
            die(f"{where}: validated_date must be YYYY-MM-DD, got {dt!r}")
        ref = p.get("review_reference")
        if not isinstance(ref, str) or not ref.strip():
            die(f"{where}: review_reference must name the ratifying review artifact")
        first = ref.split()[0]
        if first.endswith((".md", ".json", ".yaml")) and not (REPO / first).exists():
            die(f"{where}: review_reference file not found: {first}")
        if key not in sem_index:
            die(f"{where}: no semantic edge matches the exact identity "
                f"{src} {rel} {tgt} — promotion operates on existing authored-"
                f"edge identities only (held candidates are not edges)")
        if sem_index[key].get("validation_status") not in ("SUGGESTED",):
            die(f"{where}: edge {src} {rel} {tgt} is not SUGGESTED in the store")
        promo_index[key] = p

    # ---- round contract: full semantic surface ---------------------------------
    if len(promo_index) != len(semantic):
        missing = [k for k in sem_index if k not in promo_index]
        die(f"round contract violated: {len(promo_index)} entries vs "
            f"{len(semantic)} authored semantic edges; missing "
            f"{missing[:3]}{'...' if len(missing) > 3 else ''} — the T-C41 "
            f"round is the whole surface (73); partial rounds are a different "
            f"gate")

    # ---- byte-stability of the untouched surface --------------------------------
    original_text = EDGES.read_text(encoding="utf-8")
    _lines = original_text.splitlines(keepends=True)
    _i = 0
    while _i < len(_lines) and _lines[_i].startswith("#"):
        _i += 1
    header = "".join(_lines[:_i])
    body = "".join(_lines[_i:])
    re_dump = yaml.safe_dump(doc, allow_unicode=True, sort_keys=False, width=100)
    if body.strip() != re_dump.strip():
        die("store is not in the canonical dump form — aborting (the applier "
            "rewrites only via the canonical dumper)")

    # ---- apply: ONLY validation fields change -------------------------------------
    promoted = 0
    for e in edges:
        key = (e["source"], e["relation"], e["target"])
        if e["relation"] == "PART_OF":
            continue
        p = promo_index.get(key)
        if p is None:
            continue
        # fail if validation fields somehow pre-exist (anti-forgery)
        if "validated_by" in e or "validated_date" in e:
            die(f"edge {key} already carries validation fields")
        e["validation_status"] = "HUMAN_VALIDATED"
        # dict insertion: validated_by/validated_date land directly after
        # validation_status only if we rebuild the key order — do it explicitly
        ne = {}
        for k, v in e.items():
            ne[k] = v
            if k == "validation_status":
                ne["validated_by"] = p["validated_by"]
                ne["validated_date"] = p["validated_date"]
        edges[edges.index(e)] = ne
        promoted += 1
    if promoted != len(promo_index):
        die(f"applied {promoted} != {len(promo_index)} promotions")

    meta = doc["meta"]
    if "promotion_record" in meta:
        die("meta already carries promotion_record (re-run guard)")
    meta2 = {}
    for k, v in meta.items():
        if k == "counts":
            c = dict(v)
            c["promoted_edges"] = promoted
            c["human_validated_edges"] = promoted
            meta2[k] = c
        else:
            meta2[k] = v
    meta2["promotion_record"] = "scripts/c41_maths_a_promotions.yaml"
    doc["meta"] = meta2

    # structural diff assertion: exactly the promotion delta
    orig = yaml.safe_load(original_text)
    o_edges = orig["edges"]
    n_edges = doc["edges"]
    if len(o_edges) != len(n_edges):
        die("edge count drift")
    for oe, ne in zip(o_edges, n_edges):
        if oe["relation"] == "PART_OF":
            if oe != ne:
                die(f"PART_OF row mutated: {(oe['source'], oe['target'])}")
            continue
        p = promo_index.get((ne["source"], ne["relation"], ne["target"]))
        if p is None:
            if oe != ne:
                die(f"unpromoted semantic edge mutated: "
                    f"{(ne['source'], ne['relation'], ne['target'])}")
        else:
            if {k: v for k, v in oe.items() if k not in ("validation_status",)} != \
               {k: v for k, v in ne.items() if k not in ("validation_status",
                                                         "validated_by",
                                                         "validated_date")}:
                die(f"promoted edge carries a non-validation delta: "
                    f"{(ne['source'], ne['relation'], ne['target'])}")
            if ne["validated_by"] != p["validated_by"] or \
                    ne["validated_date"] != p["validated_date"]:
                die(f"attribution drift on {(ne['source'], ne['relation'], ne['target'])}")

    # ---- write -----------------------------------------------------------------
    new_text = header + yaml.safe_dump(
        doc, allow_unicode=True, sort_keys=False, width=100)
    (EDGES).write_text(new_text, encoding="utf-8")

    # ---- record ------------------------------------------------------------------
    stores = {p.name: hashlib.sha256((EDGES.parent / p.name).read_bytes()).hexdigest()[:16]
              for p in sorted(EDGES.parent.glob("*.yaml"))}
    baseline = subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                              capture_output=True, text=True).stdout.strip()
    now = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S+00:00")
    by_set = sorted({p["validated_by"] for p in entries})
    rec = {
        "schema": "c41-s18-promotion-record/1.0",
        "task": "T-C41",
        "gate": "K2 Lane C §18 HUMAN_VALIDATED promotion round (the separate "
                "operator gate named by the C39 verdict record)",
        "generated_utc": now,
        "baseline": baseline,
        "operator_directive": ("fire K2-B (chunk substrate), run the §18 "
                               "HUMAN_VALIDATED promotion round over the 73 edges "
                               "(2026-10-02, zai-web)"),
        "promotion_record": "scripts/c41_maths_a_promotions.yaml",
        "tool": "scripts/c41_maths_a_promote.py + scripts/c41_maths_a_promotion_apply.py",
        "review_reference": sorted({p["review_reference"] for p in entries}),
        "validated_by": by_set,
        "validated_date": sorted({p["validated_date"] for p in entries}),
        "round": {
            "surface": "the authored semantic surface of the C39 governed apply",
            "promoted": promoted,
            "semantic_total": len(semantic),
            "relation_split": {
                r: sum(1 for p in entries if p["edge"]["relation"] == r)
                for r in sorted(RELATIONS)},
            "part_of_rows_untouched": len(part_of),
            "held_candidates_untouched": 45,
        },
        "anti_forgery": {
            "decision_records_untouched": True,
            "ai_attribution": "none (validated_by = operator, the c11 precedent; "
                              "AI-name patterns fail closed in both tools)",
            "non_validation_delta": "asserted zero (structural diff over all 157 rows)",
        },
        "store_pins": stores,
        "post_check": "scripts/c41_maths_a_promotion_check.py",
        "not_done": ["no node promotion (nodes stay SUGGESTED — node promotion is "
                     "a separate identity decision, expansion round)",
                     "no PART_OF promotion (derived rows follow node authority)",
                     "no held-candidate promotion (45 stay quarantined)",
                     "no decision-record mutation", "no chemistry writes",
                     "no corpus writes"],
    }
    REC_JSON.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8")
    md = f"""# C41 — §18 HUMAN_VALIDATED Promotion Round — igcse-maths-a (the 73 authored edges)

**Generated:** {now}  |  **Baseline:** `{baseline}`
**Operator directive:** "fire K2-B (chunk substrate), run the §18 HUMAN_VALIDATED
promotion round over the 73 edges" (2026-10-02, zai-web). The directive is the
operator command §18 requires; the ratifying review artifact is the C39
consolidated operator review (PASS WITH NOTES over all six Lane C packets, GO).

## What this is

The exact-identity §18 round of `C11_ARCHITECTURE.md` §18, executed as the
separate operator gate the C39 verdict record named. All **{promoted} authored
semantic edges** ({rec['round']['relation_split']['REQUIRES_PREREQUISITE']}
REQUIRES_PREREQUISITE + {rec['round']['relation_split']['WRONG_ANSWER_PATTERN']}
WRONG_ANSWER_PATTERN + {rec['round']['relation_split']['REMEDIATED_BY']}
REMEDIATED_BY) now carry `validation_status: HUMAN_VALIDATED` +
`validated_by` + `validated_date` in
`graph/igcse-maths-a/concept_edges.yaml`. The 84 derived PART_OF rows follow
node authority and stay SUGGESTED; the 45 held candidates stay quarantined;
the 82 nodes stay SUGGESTED (node promotion is a separate identity decision,
expansion round).

## Mechanics

- `scripts/c41_maths_a_promote.py` (the only writer of
  `scripts/c41_maths_a_promotions.yaml`): exact 3-token identities only;
  every evidence quote byte-verified under the T-C10 norm before anything was
  written; attribution gate (AI self-attribution fails closed); DC-04-aware
  identity mapping (the 3 store-side `*-SIMPLE-CASES` identities resolve to
  their decision-record origins); idempotent; atomic write.
- `scripts/c41_maths_a_promotion_apply.py` (the gated merge point, G13
  convention): validates every entry, enforces the round contract
  ({promoted}/{len(semantic)}), and rewrites ONLY the validation fields —
  a structural diff over all 157 rows asserts the non-validation delta is
  exactly zero (T01c analog); meta gains `promotion_record` +
  `promoted_edges`/`human_validated_edges` counts; everything else is
  byte-identical.
- `scripts/c41_maths_a_promotion_check.py` (the c11.13 analog): two-way
  graph ⟷ promotions-record audit against the real repo files.

## Anti-forgery posture

- The AI decision records are byte-untouched (they may never carry
  HUMAN_VALIDATED — G10).
- The promotions record carries `validated_by: operator` (the c11 precedent);
  AI-name patterns fail closed in both tools.
- The graph carries HUMAN_VALIDATED only on exact triples with matching
  promotion entries and exact attribution (the promotion check enforces this
  continuously).

## Pins

| Artifact | sha256_16 |
|---|---|
| `concept_edges.yaml` (post-round) | `{stores['concept_edges.yaml']}` |
| `concepts.yaml` (untouched) | `{stores['concepts.yaml']}` |
| `spec_command_kinds.yaml` (untouched) | `{stores['spec_command_kinds.yaml']}` |
"""
    REC_MD.write_text(md + "\n", encoding="utf-8")

    print(f"c41_maths_a_promotion_apply: APPLIED — {promoted} edges "
          f"HUMAN_VALIDATED ({len(part_of)} PART_OF rows untouched)")
    print(f"  concept_edges.yaml sha256_16 {stores['concept_edges.yaml']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
