#!/usr/bin/env python3
"""T-C11 — c11_s16_authorization_check.py: integrity validation for the
OPERATOR-OWNED §16 authorization record scripts/c11_s16_authorization.yaml
(session 46, 2026-09-12).

Fail-closed gate for the §16 authorization layer. Validates:

  A. record schema: required sections; decision AUTHORIZED; authorized_by
     exactly 'operator' (anti-forgery: AI-name patterns fail closed,
     mirroring the §18 attribution rule); authorized_date 2026-09-12; the
     operator statement recorded verbatim; scope unlocked + not_authorized
     present; preconditions snapshot; the invariant disciplines present;
  B. authorization-only payload: the record carries NO promotion payload —
     no promotions block, no per-identity verdict rows, no HUMAN_VALIDATED
     fields. It grants a gate, never identities (mirrors verdict-check D3);
  C. cross-file consistency: the §16 gate report carries the dated
     session-46 authorization note referencing this record and item 4 is
     DONE (all four blockers settled — the live marker replaced); the
     architecture §16 carries the dated session-46 amendment; the batch
     forecast status reflects the authorization;
  D. live-state invariants (robust to future batch growth): every one of
     the 28 session-44 CONFIRM triples is HUMAN_VALIDATED in the live graph
     and present in the promotion store (subset, operator attribution
     only); the 3 operator HOLD edges (E-08/E-26/E-29) and the RR edge are
     NOT promoted and still present — the frozen pilot dispositions the
     authorization explicitly preserves; 4CH1-4.15 zero attachments.

Exit 0 = all checks pass; exit 1 = any failure (all printed).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
GRAPH = REPO / "graph"
REPORTS = GRAPH / "reports"

AUTHZ = HERE / "c11_s16_authorization.yaml"
VERDICTS = HERE / "c11_review_verdicts.yaml"
EDGES = GRAPH / "concept_edges.yaml"
NODES = GRAPH / "concepts.yaml"
PROMOTIONS = HERE / "c11_promotions.yaml"
GATE_REPORT = REPORTS / "C11_S16_GATE_REPORT.md"
ARCHITECTURE = REPORTS / "C11_ARCHITECTURE.md"
FORECAST = REPORTS / "C11_BATCH_FORECAST.json"

RR_TRIPLE = "4CH1-CON-GAS-VOL-CALC REQUIRES_PREREQUISITE 4CH1-CON-AVOGADRO-LAW"
OPERATOR_STATEMENT = "Okay, I authorize"
AI_NAME_PATTERNS = ("gpt", "chatgpt", "claude", "anthropic", "glm", "z.ai",
                    "openai", "copilot", "gemini", "deepseek", "ai ", "agent")

fails = []


def check(name: str, cond: bool, detail: str = ""):
    print(("PASS  " if cond else "FAIL  ") + name + (f"  {detail}" if detail else ""))
    if not cond:
        fails.append(name)


def triple(e: dict) -> str:
    return f"{e['source']} {e['relation']} {e['target']}"


auth = yaml.safe_load(AUTHZ.read_text(encoding="utf-8"))
vd = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
edges_doc = yaml.safe_load(EDGES.read_text(encoding="utf-8"))
nodes_doc = yaml.safe_load(NODES.read_text(encoding="utf-8"))
promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
gate_text = GATE_REPORT.read_text(encoding="utf-8")
arch_text = ARCHITECTURE.read_text(encoding="utf-8")
forecast = yaml.safe_load(FORECAST.read_text(encoding="utf-8"))

# ---------------------------------------------------------------------------
# A. record schema
# ---------------------------------------------------------------------------
check("A1 record sections present",
      all(k in auth for k in ("meta", "authorization")),
      f"top keys = {sorted(auth.keys())}")
a = auth.get("authorization", {})
check("A2 decision AUTHORIZED", a.get("decision") == "AUTHORIZED",
      f"decision = {a.get('decision')!r}")
by = a.get("authorized_by", "")
check("A3 authorized_by exactly operator (anti-forgery)",
      by == "operator" and not any(p in by.lower() for p in AI_NAME_PATTERNS),
      f"authorized_by = {by!r}")
check("A4 authorized_date 2026-09-12",
      a.get("authorized_date") == "2026-09-12",
      f"authorized_date = {a.get('authorized_date')!r}")
check("A5 operator statement recorded verbatim",
      a.get("operator_statement_verbatim") == OPERATOR_STATEMENT,
      f"statement = {a.get('operator_statement_verbatim')!r}")
check("A6 statement context names the item-4 decision it answers",
      "item 4" in a.get("statement_context", "")
      and "explicit authorization" in a.get("statement_context", ""),
      "")
scope = a.get("scope", {})
check("A7 scope.unlocked present and names the item-14 batching shape",
      "item-14" in scope.get("unlocked", "")
      and "operator gate" in scope.get("unlocked", "")
      and "14 batches" in scope.get("unlocked", ""),
      "")
check("A8 scope.not_authorized present with the frozen exclusions",
      all(s in scope.get("not_authorized", "") for s in
          ("DB writes", "E-08/E-26/E-29", "4CH1-4.15", "anti-forgery")),
      "")
snap = a.get("preconditions_snapshot", {})
check("A9 preconditions snapshot records the session-45 decision basis",
      snap.get("resources_head") == "08f5ec9"
      and snap.get("tracker_head") == "8cdc2fe"
      and "28 HUMAN_VALIDATED" in snap.get("pilot_live_state", ""),
      "")
invariants = a.get("invariants", [])
required_disciplines = (
    "per-batch operator gate", "OD-1", "OD-2", "FC-1..FC-4", "4CH1-4.15",
    "PART_OF node promotion", "AI attribution forbidden",
    "deterministic regeneration", "no DB writes",
)
inv_text = " | ".join(invariants)
check("A10 the nine invariant disciplines present",
      len(invariants) >= 8 and all(d in inv_text for d in required_disciplines),
      f"n_invariants = {len(invariants)} (OD-1/OD-2 share one item)")

# ---------------------------------------------------------------------------
# B. authorization-only payload (no identity grants)
# ---------------------------------------------------------------------------
raw_auth_text = AUTHZ.read_text(encoding="utf-8")
check("B1 no promotions block in the record",
      "promotions:" not in raw_auth_text and "edge_verdicts:" not in raw_auth_text
      and "node_verdicts:" not in raw_auth_text,
      "")
check("B2 no HUMAN_VALIDATED-granting fields in the record",
      "validated_by" not in raw_auth_text
      and "validation_status: HUMAN_VALIDATED" not in raw_auth_text,
      "")

# ---------------------------------------------------------------------------
# C. cross-file consistency (dated session-46 notes, historical preserved)
# ---------------------------------------------------------------------------
check("C1 gate report carries the session-46 authorization note",
      "Session-46" in gate_text and "AUTHORIZED" in gate_text
      and "c11_s16_authorization.yaml" in gate_text,
      "")
check("C2 gate report item 4 settled — all four blockers DONE, live marker replaced",
      "REMAINS THE SOLE BLOCKER" not in gate_text
      and gate_text.count("DONE session") >= 4
      and "DONE session 46" in gate_text,
      f"'DONE session' count = {gate_text.count('DONE session')}")
check("C3 architecture §16 carries the dated session-46 amendment",
      "§16" in arch_text and "Session-46" in arch_text
      and "c11_s16_authorization.yaml" in arch_text
      and "authorized" in arch_text.lower(),
      "")
fstat = str(forecast.get("s16_projection", {}).get("status", ""))
check("C4 batch forecast status reflects the authorization",
      "AUTHORIZED" in fstat and "2026-09-12" in fstat and "session 46" in fstat,
      f"status = {fstat!r}")

# ---------------------------------------------------------------------------
# D. live-state invariants (robust to future batch growth)
# ---------------------------------------------------------------------------
confirm_triples = {r["triple"] for r in vd["edge_verdicts"] if r["verdict"] == "CONFIRM"}
hold_triples = {r["triple"] for r in vd["edge_verdicts"] if r["verdict"] == "HOLD"}
check("D0 verdict record basis intact (28 CONFIRM / 3 HOLD)",
      len(confirm_triples) == 28 and len(hold_triples) == 3,
      f"confirms = {len(confirm_triples)}, holds = {len(hold_triples)}")

edges = edges_doc["edges"]
sem = [e for e in edges if e.get("relation") != "PART_OF"]
live_hv = {triple(e) for e in sem if e.get("validation_status") == "HUMAN_VALIDATED"}
live_non_hv = {triple(e) for e in sem if e.get("validation_status") != "HUMAN_VALIDATED"}

check("D1 the 28 pilot CONFIRM identities remain HUMAN_VALIDATED (permanence)",
      confirm_triples <= live_hv,
      f"missing = {sorted(confirm_triples - live_hv)[:3]}")
promo_triples = {triple(p["edge"]) for p in promo.get("promotions", [])}
promo_by = {p.get("validated_by") for p in promo.get("promotions", [])}
check("D2 the 28 pilot promotions remain in the store with operator attribution",
      confirm_triples <= promo_triples and promo_by == {"operator"},
      f"store entries = {len(promo_triples)}, attribution = {promo_by}")
check("D3 the 3 operator HOLD edges stay un-promoted",
      hold_triples <= live_non_hv and not (hold_triples & live_hv),
      f"promoted HOLDs = {sorted(hold_triples & live_hv)}")
rr_edges = [e for e in sem if triple(e) == RR_TRIPLE]
check("D4 the RR edge stays present and un-promoted (operator HOLD)",
      len(rr_edges) == 1 and rr_edges[0].get("validation_status") != "HUMAN_VALIDATED",
      f"status = {rr_edges[0].get('validation_status') if rr_edges else 'ABSENT'}")

nodes = nodes_doc["nodes"]
n415 = [n for n in nodes
        if any(sp.get("code") == "4CH1-4.15" for sp in n.get("spec_points", []))]
e415 = [e for e in edges if any("4.15" in ev.get("file", "")
                                for ev in e.get("evidence", []))]
check("D5 negative control 4CH1-4.15: zero node/edge attachments",
      len(n415) == 0 and len(e415) == 0,
      f"nodes = {len(n415)}, edges = {len(e415)}")

# ---------------------------------------------------------------------------
print()
if fails:
    print(f"c11_s16_authorization_check: {len(fails)} FAILURE(S): " + "; ".join(fails))
    sys.exit(1)
print("c11_s16_authorization_check: ALL PASS — the §16 expansion is authorized by "
      "explicit operator decision (2026-09-12, verbatim statement recorded), the "
      "record is authorization-only (no identity grants), the governance reports "
      "carry the dated session-46 notes, and the frozen pilot dispositions the "
      "authorization preserves are intact (28 promotions permanent, 3 HOLDs + RR "
      "un-promoted, 4.15 uncovered).")
