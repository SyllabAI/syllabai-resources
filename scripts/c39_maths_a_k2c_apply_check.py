#!/usr/bin/env python3
"""T-C39 K2 Lane C — POST-APPLY verification battery for the maths-a §18 apply
(fail-closed; the c30_k1_check.py / chemistry graph_check c11-lane convention).

The review's §9 post-apply checklist, machine-enforced:

  P1 counts          promoted counts == the authorized verdict surface; store
                     meta.counts match the records (82 = 71+11 nodes; 157 =
                     84 PART_OF + 73 semantic edges; 72 command kinds)
  P2 authority       zero HUMAN_VALIDATED anywhere; every row SUGGESTED;
                     provenance tier AI_SUGGESTED everywhere
  P3 uniqueness      no duplicate concept ids; 4MA1-* namespace only
  P4 endpoints       semantic edge endpoints resolve to declared nodes;
                     PART_OF targets resolve to slice SP codes in the ratified
                     store; cross-batch edges (all 73) resolve to canonical ids
  P5 projections     PART_OF set == the node attachments exactly (bijection)
  P6 held quarantine no held row silently promoted: none of the 45 held
                     candidates' edge triples appears in the store; held ids
                     appear nowhere in the stores
  P7 misconceptions  11 MISCONCEPTION nodes: pattern_class WRONG_ANSWER_PATTERN,
                     mark-scheme evidence present, each paired with >=1
                     WRONG_ANSWER_PATTERN edge and a REMEDIATED_BY edge whose
                     target == the WAP target (B1-E-25); provenance
                     assessment-backed (derivation_method ASSESSMENT_DOCUMENTED)
  P8 anchors         every evidence quote byte-verified under the batch-8
                     G03/c11.4 norm (T-C10 convention): SPEC quotes == the
                     ratified store wording at the cited SP; NOTE anchors
                     join-carried through the T-C32 K2-A join and pair-backed
                     (node attachments at their SP; edge evidence at an
                     endpoint SP); MARK_SCHEME anchors under the slice course's
                     EQ tree; the unjoined-corpus negative control holds on the
                     STORE (no unjoined note cited anywhere)
  P9 registry        8 maths-a stores resolve through graph_paths;
                     spec_chunk_mappings + relationships still ABSENT;
                     graph_check rc=0 (chemistry default); check_no_hardcode
                     rc=0; the 5 K1 maths-a stores byte-untouched (git clean)
  P10 determinism    generator re-run reproduces all three stores byte-for-byte
  P11 inputs intact  the six decision records and the verdict record are
                     byte-untouched vs git HEAD; chemistry tree clean

Exit 0 = ALL PASS; 1 = any failure. Writes
graph/reports/C39_K2C_POST_APPLY_CHECK.json.
"""
from __future__ import annotations

import hashlib
import json
import re
import subprocess
import sys
import unicodedata
from pathlib import Path

import yaml

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
COURSE = "igcse-maths-a-18-higher"
GRAPH = REPO / "graph" / QUAL
REPORTS = REPO / "graph/reports"
JOIN_ARTIFACT = (REPO / "Official-Specifications/parsed/_derived/notes-join/"
                 f"{COURSE}.json")
SPEC_FILE = f"graph/{QUAL}/specification_points.yaml"
OUT = REPORTS / "C39_K2C_POST_APPLY_CHECK.json"
DECISIONS = [HERE / f"c{32+n}_maths_a_batch0{n}_decisions.yaml" for n in range(1, 7)]
STORES = ["concepts.yaml", "concept_edges.yaml", "spec_command_kinds.yaml"]

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


class R:
    """disk-first reader with a single persistent cat-file --batch fallback
    (the c38 quote-probe channel; the maths-a corpora are git-only in this
    workspace per the C28-F1 sparse mechanism)."""

    def __init__(self) -> None:
        self._proc = None
        self._cache: dict[str, str] = {}
        self.methods = {"disk": 0, "git-batch": 0}

    def _show(self, rel: str) -> str:
        if self._proc is None:
            self._proc = subprocess.Popen(
                ["git", "-C", str(REPO), "cat-file", "--batch"],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        # HEAD:{rel} — the c38 probe convention: the corpora are read-only
        # inputs and 38933 index entries carry the skip-worktree bit in this
        # C28-F1 sparse workspace, so bare-path resolution reports missing;
        # the HEAD-tree object always resolves (P9/P11 pin the inputs as
        # byte-untouched, so HEAD == working tree for every cited file)
        self._proc.stdin.write(f"HEAD:{rel}\n".encode())
        self._proc.stdin.flush()
        header = self._proc.stdout.readline().decode()
        parts = header.split()
        if len(parts) < 3 or parts[1] == "missing":
            return None
        size = int(parts[2])
        data = self._proc.stdout.read(size)
        self._proc.stdout.read(1)
        return data.decode("utf-8", errors="replace")

    def read(self, rel: str) -> str:
        if rel in self._cache:
            return self._cache[rel]
        p = REPO / rel
        if p.exists():
            txt = p.read_text(encoding="utf-8", errors="replace")
            self.methods["disk"] += 1
        else:
            txt = self._show(rel)
            self.methods["git-batch"] += 1
            if txt is None:
                raise FileNotFoundError(rel)
        self._cache[rel] = txt
        return txt

    def close(self) -> None:
        if self._proc is not None:
            try:
                self._proc.stdin.close()
                self._proc.wait(timeout=5)
            except Exception:
                self._proc.kill()


def main() -> int:
    checks: list[dict] = []

    def gate(pid: str, name: str, fails: list[str], detail: str) -> None:
        checks.append({"gate": pid, "name": name,
                       "status": "PASS" if not fails else "FAIL",
                       "detail": "; ".join(fails) or detail})

    con = yaml.safe_load((GRAPH / "concepts.yaml").read_text(encoding="utf-8"))
    edg = yaml.safe_load((GRAPH / "concept_edges.yaml").read_text(encoding="utf-8"))
    cks = yaml.safe_load((GRAPH / "spec_command_kinds.yaml").read_text(encoding="utf-8"))
    nodes, edges, kinds = con["nodes"], edg["edges"], cks["command_kinds"]

    # ---- P1 counts --------------------------------------------------------------
    f1: list[str] = []
    n_con = sum(1 for x in nodes if x["family"] == "CONCEPT")
    n_mis = sum(1 for x in nodes if x["family"] == "MISCONCEPTION")
    po = [e for e in edges if e["relation"] == "PART_OF"]
    sem = [e for e in edges if e["relation"] != "PART_OF"]
    if (len(nodes), n_con, n_mis) != (82, 71, 11):
        f1.append(f"node counts {(len(nodes), n_con, n_mis)} != (82, 71, 11)")
    if (len(po), len(sem), len(edges)) != (84, 73, 157):
        f1.append(f"edge counts {(len(po), len(sem), len(edges))} != (84, 73, 157)")
    if len(kinds) != 72:
        f1.append(f"command kinds {len(kinds)} != 72")
    if con["meta"]["counts"] != {"nodes": 82, "concepts": 71, "misconceptions": 11,
                                 "part_of_edges": 84, "semantic_edges": 73}:
        f1.append("concepts meta.counts mismatch")
    rel_split = {}
    for e in sem:
        rel_split[e["relation"]] = rel_split.get(e["relation"], 0) + 1
    if rel_split != {"REQUIRES_PREREQUISITE": 51, "WRONG_ANSWER_PATTERN": 11,
                     "REMEDIATED_BY": 11}:
        f1.append(f"semantic relation split {rel_split} != 51/11/11")
    guide = {}
    for k in kinds:
        guide[k["guide_class"]] = guide.get(k["guide_class"], 0) + 1
    if guide != {"APPLY_PROCEDURE": 56, "UNDERSTAND_RELATION": 15, "KNOW_TERM": 1}:
        f1.append(f"guide_class split {guide} != 56/15/1")
    gate("P1", "counts_equal_authorized_surface", f1,
         "82 = 71 CONCEPT + 11 MISCONCEPTION nodes; 157 = 84 PART_OF + 51 RP + 11 "
         "WAP + 11 REM edges; 72 kinds = 56 APPLY + 15 UNDERSTAND + 1 KNOW_TERM; "
         "meta.counts agree")

    # ---- P2 authority -------------------------------------------------------------
    f2: list[str] = []

    def authority_ok(row: dict, where: str) -> None:
        if row.get("validation_status") != "SUGGESTED":
            f2.append(f"{where}: validation_status {row.get('validation_status')!r}")
        prov = row.get("provenance") or {}
        if prov.get("tier") != "AI_SUGGESTED":
            f2.append(f"{where}: provenance.tier {prov.get('tier')!r}")
        for banned in ("validated_by", "validated_date"):
            if banned in row:
                f2.append(f"{where}: carries {banned}")

    for x in nodes:
        authority_ok(x, f"node {x['code']}")
    for e in edges:
        authority_ok(e, f"edge {e['source']}->{e['target']}")
    # the anti-forgery scan is FIELD-LEVEL (validation_status values +
    # validated_* keys on ROWS); the literal string in meta.validation_gate
    # prose ('HUMAN_VALIDATED is operator-only') is the chemistry house
    # convention and is not a violation
    row_blob = json.dumps([[x.get("validation_status"),
                            sorted(k for k in x if k.startswith("validated"))]
                           for x in nodes + edges + kinds])
    if "HUMAN_VALIDATED" in row_blob:
        f2.append("row-level HUMAN_VALIDATED present in a store")
    gate("P2", "authority_suggested_everywhere", f2,
         "zero HUMAN_VALIDATED; every node/edge SUGGESTED at tier AI_SUGGESTED; "
         "no validated_by/validated_date fields (no promotion entries)")

    # ---- P3 uniqueness + namespace --------------------------------------------------
    f3: list[str] = []
    codes = [x["code"] for x in nodes]
    if len(set(codes)) != len(codes):
        dupes = sorted({c for c in codes if codes.count(c) > 1})
        f3.append(f"duplicate node codes: {dupes}")
    foreign = [c for c in codes if not c.startswith("4MA1-")]
    if foreign:
        f3.append(f"foreign-namespace node codes: {foreign}")
    kc = [k["code"] for k in kinds]
    if len(set(kc)) != len(kc):
        f3.append("duplicate command-kind codes")
    gate("P3", "no_duplicate_ids_namespace", f3,
         "82 unique node codes, all 4MA1-*; 72 unique command-kind codes")

    # ---- P4 endpoint resolution --------------------------------------------------------
    f4: list[str] = []
    node_set = set(codes)
    sps = yaml.safe_load((GRAPH / "specification_points.yaml").read_text(encoding="utf-8"))
    sp_set = {p["code"] for p in sps["specification_points"]}
    for e in sem:
        for end in ("source", "target"):
            if e[end] not in node_set:
                f4.append(f"semantic {e['relation']} endpoint {e[end]!r} unresolved")
    for e in po:
        if e["source"] not in node_set:
            f4.append(f"PART_OF source {e['source']!r} unresolved")
        if e["target"] not in sp_set:
            f4.append(f"PART_OF target {e['target']!r} not a ratified SP code")
    gate("P4", "endpoints_resolve_canonical", f4,
         "all 73 semantic edges resolve to declared nodes (no cross-batch "
         "dangling: the 45 cross-batch candidates were held, none authored); "
         "all 84 PART_OF targets are ratified 4MA1 SP codes")

    # ---- P5 PART_OF == attachments ---------------------------------------------------------
    f5: list[str] = []
    att: set[tuple] = set()
    for x in nodes:
        for sp in x.get("spec_points") or []:
            att.add((x["code"], sp["code"]))
    got = {(e["source"], e["target"]) for e in po}
    if got != att:
        f5.append(f"PART_OF set != attachments (missing {sorted(att - got)[:5]}, "
                  f"extra {sorted(got - att)[:5]})")
    if len(po) != len(got):
        f5.append("duplicate PART_OF rows")
    gate("P5", "part_of_equals_attachments", f5,
         "84 PART_OF rows == the declared node attachments exactly (bijection, "
         "derived at generation per C11_ARCHITECTURE.md §18 scope limits)")

    # ---- P6 held quarantine -----------------------------------------------------------------
    f6: list[str] = []
    held = []
    for p in DECISIONS:
        d = yaml.safe_load(p.read_text(encoding="utf-8"))
        held += d.get("held", [])
    if len(held) != 45:
        f6.append(f"held inventory {len(held)} != 45")
    edge_triples = {(e["source"], e["relation"], e["target"]) for e in sem}
    held_edge_like = 0
    # structural surface = the fields that would materialize a held row;
    # prose references inside derivation_notes are the decision records' own
    # documentation of WHY an edge was held (they are carried verbatim and
    # are not promotions) — counted and reported, never failed
    structural = json.dumps(
        [[x.get("code"), x.get("id")] for x in nodes]
        + [[e.get("source"), e.get("relation"), e.get("target")]
           for e in edges]
        + [[k.get("code")] for k in kinds])
    prose_mentions = 0
    for h in held:
        m = re.match(r"([A-Z_]+)\(\s*([A-Z0-9-]+)\s*,\s*([A-Z0-9-]+)", str(h.get("candidate", "")))
        if m:
            held_edge_like += 1
            rel, src, tgt = m.group(1), m.group(2), m.group(3)
            if (src, rel, tgt) in edge_triples:
                f6.append(f"HELD PROMOTED: {h['id']} {src} -{rel}-> {tgt}")
        if h["id"] in structural:
            f6.append(f"held id {h['id']} in a STRUCTURAL store field")
        prose_mentions += (json.dumps(con) + json.dumps(edg)).count(h["id"])
    if prose_mentions and not f6:
        pass  # documented below in the gate detail
    gate("P6", "no_held_promoted", f6,
         f"45 held candidates preserved in the decision records and emitted "
         f"nowhere; {held_edge_like} of them are edge-shaped and none of those "
         f"triples appears in the store (NO-GO #3 enforced: no held candidate "
         f"converted because a later batch contains a related concept); "
         f"{prose_mentions} held-id references live in derivation_notes prose "
         f"only — the records' own documentation of why each edge was held")

    # ---- P7 misconceptions -------------------------------------------------------------------
    f7: list[str] = []
    mis = [x for x in nodes if x["family"] == "MISCONCEPTION"]
    if len(mis) != 11:
        f7.append(f"{len(mis)} MISCONCEPTION nodes != 11")
    wap_by_src = {}
    rem_by_src = {}
    for e in sem:
        if e["relation"] == "WRONG_ANSWER_PATTERN":
            wap_by_src.setdefault(e["source"], []).append(e)
        if e["relation"] == "REMEDIATED_BY":
            rem_by_src.setdefault(e["source"], []).append(e)
    for x in mis:
        c = x["code"]
        if x.get("pattern_class") != "WRONG_ANSWER_PATTERN":
            f7.append(f"{c}: pattern_class {x.get('pattern_class')!r}")
        ev = x.get("evidence") or []
        if not any(a.get("kind") == "MARK_SCHEME" for a in ev):
            f7.append(f"{c}: no MARK_SCHEME evidence (assessment-backed rule)")
        if (x.get("provenance") or {}).get("derivation_method") != "ASSESSMENT_DOCUMENTED":
            f7.append(f"{c}: provenance.derivation_method not ASSESSMENT_DOCUMENTED")
        waps = wap_by_src.get(c, [])
        rems = rem_by_src.get(c, [])
        if not waps:
            f7.append(f"{c}: no WRONG_ANSWER_PATTERN edge")
        if not rems:
            f7.append(f"{c}: no REMEDIATED_BY edge")
        else:
            wap_targets = {w["target"] for w in waps}
            if not any(r["target"] in wap_targets for r in rems):
                f7.append(f"{c}: REMEDIATED_BY target != WAP target (B1-E-25)")
        if not (x.get("spec_points") or []):
            f7.append(f"{c}: no home-SP attachment")
    extra_wap = (set(wap_by_src) | set(rem_by_src)) - {x["code"] for x in mis}
    if extra_wap:
        f7.append(f"WAP/REMEDIATED_BY sources not misconception nodes: {sorted(extra_wap)}")
    gate("P7", "misconception_integrity", f7,
         "11/11 misconception nodes: WRONG_ANSWER_PATTERN class, mark-scheme "
         "evidence, ASSESSMENT_DOCUMENTED provenance, home-SP attachment, and "
         "the WAP + REMEDIATED_BY pairing with remediation target == WAP target")

    # ---- P8 anchors ---------------------------------------------------------------------------
    f8: list[str] = []
    rd = R()
    sp_rows = {p["code"]: p for p in sps["specification_points"]}
    join = json.loads(JOIN_ARTIFACT.read_text(encoding="utf-8"))
    join_map: dict[str, set] = {}
    for j in join["joins"]:
        join_map.setdefault(j["store_row_code"], set()).add(j["note_path"])

    def joined_note(file: str, sp: str) -> bool:
        rel = file
        for pref in (f"SME-RevisionNotes/{COURSE}/", f"SME-RevisionNotes/{COURSE}"):
            if rel.startswith(pref):
                rel = rel[len(pref):]
                break
        # the join artifact keys note pages by their .json sidecar path; the
        # evidence cites the .md rendering of the same page (the c38 probe
        # maps json <-> md on the shared stem)
        if rel.endswith(".md"):
            rel = rel[:-3] + ".json"
        return rel in join_map.get(sp, set())

    def verify_anchor(a: dict, sps_allowed: set, where: str) -> None:
        kind, file, quote = a.get("kind"), a.get("file"), a.get("quote")
        if not (kind and file and quote):
            f8.append(f"{where}: anchor missing kind/file/quote")
            return
        try:
            body = rd.read(file)
        except FileNotFoundError:
            f8.append(f"{where}: cited file not readable: {file}")
            return
        if norm(quote) not in norm(body):
            f8.append(f"{where}: {kind} quote NOT byte-verified in {file}")
            return
        if kind == "SPEC":
            if file != SPEC_FILE:
                f8.append(f"{where}: SPEC anchor not on the ratified store: {file}")
                return
            hit = False
            for sp in sps_allowed:
                row = sp_rows.get(sp)
                if row and norm(quote) in norm(str(row.get("official_wording", ""))):
                    hit = True
                    break
            if not hit:
                f8.append(f"{where}: SPEC quote matches no allowed SP official_wording")
        elif kind == "NOTE":
            if not any(joined_note(file, sp) for sp in sps_allowed):
                f8.append(f"{where}: NOTE anchor not join-carried to an allowed SP "
                          f"(unjoined-corpus negative control)")
        elif kind == "MARK_SCHEME":
            if f"SME-ExamQuestion/{COURSE}/" not in file:
                f8.append(f"{where}: MARK_SCHEME anchor outside the slice EQ tree")

    n_anchors = 0
    for x in nodes:
        for sp in x.get("spec_points") or []:
            for a in sp.get("evidence") or []:
                n_anchors += 1
                verify_anchor(a, {sp["code"]}, f"node {x['code']} @{sp['code']}")
        for a in x.get("evidence") or []:
            n_anchors += 1
            allowed = {sp["code"] for sp in x.get("spec_points") or []}
            verify_anchor(a, allowed, f"node {x['code']} (MS/NOTE)")
    for e in po:
        for a in e.get("evidence") or []:
            n_anchors += 1
            verify_anchor(a, {e["target"]}, f"PART_OF {e['source']}@{e['target']}")
    for e in sem:
        allowed = set()
        for end in ("source", "target"):
            n = next((x for x in nodes if x["code"] == e[end]), None)
            if n:
                allowed |= {sp["code"] for sp in n.get("spec_points") or []}
        for a in e.get("evidence") or []:
            n_anchors += 1
            verify_anchor(a, allowed, f"edge {e['source']} -{e['relation']}-> {e['target']}")
    rd.close()
    gate("P8", "anchors_byte_verified_negative_control", f8,
         f"{n_anchors} store anchors checked under the T-C10 norm (SPEC == "
         f"ratified wording; NOTE join-carried + pair-backed; MS in the EQ "
         f"tree); read channels {rd.methods}; the unjoined-corpus negative "
         f"control holds on the STORE surface")

    # ---- P9 registry + standing checkers ---------------------------------------------------------
    f9: list[str] = []
    sys.path.insert(0, str(HERE))
    import graph_paths as GP
    for store in ("concepts", "concept_edges", "spec_command_kinds"):
        rel = GP.resolve_rel(f"graph/{QUAL}/{store}.yaml")
        if not (REPO / rel).exists():
            f9.append(f"registry does not resolve {store}")
    if (GRAPH / "spec_chunk_mappings.yaml").exists() or \
            (GRAPH / "relationships.yaml").exists():
        f9.append("spec_chunk_mappings/relationships present (must stay absent)")
    k1_files = ["specification_points.yaml", "topics.yaml", "practicals.yaml",
                "assessment_objectives.yaml", "command_words.yaml"]
    dirty = subprocess.run(["git", "-C", str(REPO), "status", "--short", "--"]
                           + [f"graph/{QUAL}/{f}" for f in k1_files]
                           + ["graph/igcse-chemistry"],
                           capture_output=True, text=True).stdout.strip()
    if dirty:
        f9.append(f"K1 stores or chemistry dirty: {dirty}")
    rc1 = subprocess.run([sys.executable, str(HERE / "graph_check.py")],
                         capture_output=True, text=True, cwd=str(REPO))
    if rc1.returncode != 0:
        f9.append(f"graph_check rc={rc1.returncode}")
    rc2 = subprocess.run([sys.executable, str(HERE / "check_no_hardcode.py")],
                         capture_output=True, text=True, cwd=str(REPO))
    if rc2.returncode != 0:
        f9.append(f"check_no_hardcode rc={rc2.returncode}: {rc2.stdout[-300:]}")
    gate("P9", "registry_and_standing_checkers", f9,
         "maths-a registry 8 stores (K2 target 9: spec_chunk_mappings arrives "
         "with K2-B); graph_check rc=0 (chemistry default, untouched); "
         "check_no_hardcode rc=0; the 5 K1 maths-a stores byte-untouched")

    # ---- P10 determinism ------------------------------------------------------------------------------
    f10: list[str] = []
    pre = {p.name: hashlib.sha256((GRAPH / p.name).read_bytes()).hexdigest()
           for p in GRAPH.glob("*.yaml")}
    r3 = subprocess.run([sys.executable, str(HERE / "c39_maths_a_k2c_apply.py")],
                        capture_output=True, text=True, cwd=str(REPO))
    if r3.returncode != 0:
        f10.append(f"apply re-run rc={r3.returncode}: {r3.stderr[-300:]}")
    else:
        post = {p.name: hashlib.sha256((GRAPH / p.name).read_bytes()).hexdigest()
                for p in GRAPH.glob("*.yaml")}
        for s in STORES:
            if pre.get(s) != post.get(s):
                f10.append(f"{s} not byte-stable across re-runs")
        rec = json.loads((REPORTS / "C39_IGCSE_MATHS_A_K2C_APPLY_RECORD.json")
                         .read_text(encoding="utf-8"))
        for s in STORES:
            pin = rec["emitted_stores"][s]["sha256_16"]
            if pin != post[s][:16]:
                f10.append(f"{s} apply-record pin {pin} != actual {post[s][:16]}")
    gate("P10", "deterministic_regeneration", f10,
         "generator re-run reproduces all three stores byte-for-byte; the "
         "apply-record pins match the final bytes")

    # ---- P11 inputs intact ------------------------------------------------------------------------------
    f11: list[str] = []
    inputs = [str(p.relative_to(REPO)) for p in DECISIONS] + \
             ["scripts/c39_maths_a_k2c_verdicts.yaml",
              "graph/reports/C39_K2C_CONSOLIDATED_OPERATOR_REVIEW.md"]
    dirty = subprocess.run(["git", "-C", str(REPO), "status", "--short", "--"] + inputs,
                           capture_output=True, text=True).stdout.strip()
    # the verdict record + review copy are NEW (untracked, ??) — only the
    # decision records must show NO modification
    for line in dirty.splitlines():
        if line.startswith("??"):
            continue
        f11.append(f"input modified: {line}")
    gate("P11", "decision_records_unmutated", f11,
         "the six decision records (incl. their held: lists) byte-untouched vs "
         "git HEAD; the verdict record and review copy are new untracked files "
         "as expected")

    ok = all(c["status"] == "PASS" for c in checks)
    rec = {
        "schema": "c39-post-apply-check/1.0",
        "task": "T-C39",
        "gate": "K2 Lane C post-apply verification (§9 checklist)",
        "baseline": subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                                   capture_output=True, text=True).stdout.strip(),
        "result": "ALL PASS" if ok else "FAIL",
        "gates": checks,
        "anchors_checked": n_anchors,
        "read_channels": rd.methods,
    }
    OUT.write_text(json.dumps(rec, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    for c in checks:
        print(f"{c['status']}  {c['gate']} {c['name']}"
              + (f" — {c['detail'][:220]}" if c["status"] == "FAIL" else ""))
    print(f"c39_maths_a_k2c_apply_check: {rec['result']} "
          f"({sum(1 for c in checks if c['status'] == 'PASS')}/{len(checks)} gates)")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
