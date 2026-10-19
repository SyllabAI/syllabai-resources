#!/usr/bin/env python3
"""c29_k0_check.py — T-C29 K0 gate machine-verification for igcse-maths-a.

K0 is gate (i)-(iv) of the C28 per-subject commissioning playbook
(graph/reports/C28_MULTI_SUBJECT_EXPANSION_SPEC.md §6):
  (i)   parsed bundle exists, parse_report ALL_PASS
  (ii)  notes corpus secured for the qual
  (iii) operator commissioning directive names the qual
  (iv)  scope estimate via the batch-forecast model

This checker machine-verifies (i), (ii) and (iv) against the live repo, and
records (iii) as an intake fact (the directive itself is operator-owned and
lives in the commissioning record). It is READ-ONLY with respect to the
graph, the corpus and the parsed plane: it writes only its own report
(graph/reports/C29_K0_CHECK.json).

Sparse-workspace note: this session's checkout may not materialize
SME-RevisionNotes/ (the C28-F1 precedent). Reads are disk-first with a
`git show HEAD:` fallback; every read records which method served it, so the
evidence chain is explicit either way.

Hub mirror gate (G4) is optional: pass --hub-repo pointing at a syllabai-web
(syllabai-hub) checkout with content/ materialized to cross-check the hub
content bundle against the upstream corpus. Without it G4 is SKIP, not FAIL.

Usage:
    python3 scripts/c29_k0_check.py [--hub-repo /path/to/syllabai-hub]
    # emits graph/reports/C29_K0_CHECK.json; exit 0 iff all enabled gates PASS
"""
from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent
QUAL = "igcse-maths-a"
COURSE = "igcse-maths-a-18-higher"
REPORT = Path(REPO / "graph" / "reports" / "C29_K0_CHECK.json")

# --- the scope-estimate model (C28 spec §6-K0(iv), sourced from the §16
# --- sanctioned projection + the chemistry program's observed actuals) -------
PILOT_NODES_PER_SP = 2.4
PILOT_EDGES_PER_SP = 2.75
PILOT_HELD_PER_SP = 1.0
ADJUSTED_NODES_PER_SP = 1.0   # observed discipline-adjusted actuals (C28 §6)
ADJUSTED_EDGES_PER_SP = 1.6
SP_PER_BATCH = 12             # the sanctioned §16 batch shape

SP_BASE = 188  # unique official_codes (242 parsed rows, both tiers, deduped)


class R:
    """disk-first / git-fallback reader with provenance tracking."""

    def __init__(self):
        self.methods: dict[str, str] = {}

    def read_bytes(self, rel: str) -> bytes:
        p = REPO / rel
        if p.is_file():
            self.methods[rel] = "disk"
            return p.read_bytes()
        out = subprocess.run(
            ["git", "-C", str(REPO), "show", f"HEAD:{rel}"],
            capture_output=True)
        if out.returncode != 0:
            raise FileNotFoundError(rel)
        self.methods[rel] = "git-show"
        return out.stdout

    def read_json(self, rel: str):
        return json.loads(self.read_bytes(rel).decode("utf-8"))

    def read_text(self, rel: str) -> str:
        return self.read_bytes(rel).decode("utf-8")


def sha16(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()[:16]


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--hub-repo", default=None)
    args = ap.parse_args()
    r = R()
    gates: dict[str, dict] = {}

    def gate(g: str, ok: bool, detail: dict) -> None:
        gates[g] = {"status": "PASS" if ok else "FAIL", **detail}

    # ---- G1: K0(i) parsed bundle + parse_report ----------------------------
    d: dict = {}
    ok = True
    try:
        pr = r.read_json(f"Official-Specifications/parsed/{QUAL}/parse_report.json")
        files = ["spec_points.json", "topics.json", "practicals.json",
                 "assessment_objectives.json", "command_words.json",
                 "equations.json",
                 "international-gcse-in-mathematics-spec-a.parsed.json"]
        missing = [f for f in files
                   if not (REPO / f"Official-Specifications/parsed/{QUAL}" / f).is_file()]
        g = pr["gates"]
        counts = pr["counts"]["international-gcse-in-mathematics-spec-a.parsed.json"]
        d["parse_report_gates"] = g
        d["missing_bundle_files"] = missing
        d["counts"] = counts
        sp = r.read_json(f"Official-Specifications/parsed/{QUAL}/spec_points.json")
        rows = sp if isinstance(sp, list) else sp.get("spec_points", [])
        codes: dict[str, int] = {}
        for row in rows:
            codes[row["official_code"]] = codes.get(row["official_code"], 0) + 1
        flagged = sorted(row["official_code"] for row in rows if row.get("flags"))
        d["rows"] = len(rows)
        d["unique_official_codes"] = len(codes)
        d["flagged"] = flagged
        pdf_sha1 = rows[0]["provenance"]["pdf_sha1"]
        d["pdf_sha1"] = pdf_sha1
        ok = (not missing and g.get("ALL_PASS") is True
              and all(g.get(k) is True for k in
                      ("G1_schema_present", "G2_ids_unique",
                       "G3_provenance_complete", "G4_id_prefix_valid"))
              and counts["spec_points"] == 242 and counts["flagged"] == 8
              and counts["topics"] == 18 and counts["subsections"] == 78
              and counts["practicals"] == 0
              and len(codes) == SP_BASE and len(flagged) == 8)
        d["pins"] = {
            "parse_report_sha256_16": sha16(r.read_bytes(
                f"Official-Specifications/parsed/{QUAL}/parse_report.json")),
            "spec_points_sha256_16": sha16(r.read_bytes(
                f"Official-Specifications/parsed/{QUAL}/spec_points.json")),
        }
    except Exception as e:  # noqa: BLE001
        ok, d["error"] = False, repr(e)
    gate("G1_k0_i_parsed_bundle", ok, d)

    # ---- G2: K0(ii) notes corpus secured (upstream, in-repo) ----------------
    d = {}
    ok = True
    try:
        base = f"SME-RevisionNotes/{COURSE}"
        man = json.loads(r.read_bytes(f"{base}/manifest.json"))
        c = man["counts"]
        d["manifest_counts"] = c
        d["manifest_schema"] = man.get("schema")
        listing = subprocess.run(
            ["git", "-C", str(REPO), "ls-tree", "-r", "--name-only",
             "HEAD", base], capture_output=True, text=True).stdout.split()
        # NOTE: ls-tree reports the committed tree (sparse-checkout-proof)
        n_json = sum(1 for f in listing if f.startswith(f"{base}/notes/")
                     and f.endswith(".json"))
        n_md = sum(1 for f in listing if f.startswith(f"{base}/notes/")
                   and f.endswith(".md"))
        d["note_json_files"] = n_json
        d["note_md_files"] = n_md
        readme = r.read_text("SME-RevisionNotes/README.md")
        row = [ln for ln in readme.splitlines()
               if ln.startswith(f"| {COURSE} ")]
        d["readme_row"] = row[0] if row else None
        sample = json.loads(subprocess.run(
            ["git", "-C", str(REPO), "show",
             f"HEAD:{base}/notes/1-numbers-and-the-number-system/"
             f"compound-interest-and-depreciation/compound-interest.json"],
            capture_output=True).stdout)
        d["sample_note_schema"] = sample.get("schema")
        d["sample_note_course"] = sample.get("course_slug")
        lic = r.read_text("LICENSE-DATA.md")
        d["license_amendment_present"] = (
            "Amendment 2026-09-17" in lic and "Save My Exams" in lic)
        ok = (man.get("schema") == "syllabai.sme-revision-notes-course/1.0"
              and c["pages_expected"] == 191 and c["pages_scraped"] == 191
              and c["fetch_failures"] == 0 and c["asset_failures"] == 0
              and c["assets"] == 389 and c["spec_point_links"] == 203
              and n_json == 191 and n_md == 191
              and sample.get("schema") == "syllabai.sme-revision-note/1.0"
              and sample.get("course_slug") == COURSE
              and bool(row) and d["license_amendment_present"])
        d["pins"] = {
            "manifest_sha256_16": sha16(r.read_bytes(f"{base}/manifest.json")),
            "license_sha256_16": sha16(r.read_bytes("LICENSE-DATA.md")),
        }
    except Exception as e:  # noqa: BLE001
        ok, d["error"] = False, repr(e)
    gate("G2_k0_ii_notes_corpus_secured", ok, d)

    # ---- G3: K0(iii) directive intake recorded ------------------------------
    # The directive is operator-owned text; this gate only asserts that the
    # commissioning record exists in the working tree and names the qual
    # (the record is authored in the same commit as this checker).
    d = {}
    ok = True
    try:
        rec = (REPO / "graph" / "reports"
               / "C29_IGCSE_MATHS_A_K0_COMMISSIONING_RECORD.md").read_text(
                   encoding="utf-8")
        d["record_present"] = True
        d["names_qual"] = QUAL in rec
        d["names_task"] = "T-C29" in rec
        d["directive_quoted"] = "commission K0/T-C29 for igcse-maths-a" in rec
        ok = d["names_qual"] and d["names_task"] and d["directive_quoted"]
    except FileNotFoundError:
        ok, d = False, {"record_present": False}
    gate("G3_k0_iii_operator_directive", ok, d)

    # ---- G4: hub mirror cross-check (optional) ------------------------------
    d = {}
    if args.hub_repo:
        ok = True
        try:
            hm = json.loads((Path(args.hub_repo) / "content" / COURSE
                             / "manifest.json").read_text(encoding="utf-8"))
            hc = hm["counts"]
            d["hub_counts"] = hc
            d["hub_curriculum"] = hm["curriculum"]
            d["import_source"] = hm.get("importSource")
            d["upstream_schemas"] = hm.get("importSource", {}).get(
                "upstreamSchemas")
            ok = (hc["sections"] == 6 and hc["topics"] == 39
                  and hc["specPoints"] == SP_BASE and hc["notes"] == 191
                  and hc["questions"] == 2703 and hc["flashcards"] == 999
                  and hm["curriculum"]["code"] == "4MA1"
                  and "syllabai.sme-revision-note/1.0"
                  in (d["upstream_schemas"] or []))
            d["pins"] = {"hub_manifest_sha256_16": sha16(
                (Path(args.hub_repo) / "content" / COURSE / "manifest.json")
                .read_bytes())}
        except Exception as e:  # noqa: BLE001
            ok, d["error"] = False, repr(e)
        gate("G4_hub_mirror_agreement", ok, d)
    else:
        gate("G4_hub_mirror_agreement", True, {"status": "SKIP",
                                               "reason": "no --hub-repo given"})

    # ---- G5: K0(iv) scope estimate recomputation ----------------------------
    d = {}
    try:
        est = {
            "sp_base": SP_BASE,
            "pilot_model": {
                "nodes": round(PILOT_NODES_PER_SP * SP_BASE),
                "authored_edges": round(PILOT_EDGES_PER_SP * SP_BASE),
                "held": round(PILOT_HELD_PER_SP * SP_BASE)},
            "discipline_adjusted": {
                "nodes": round(ADJUSTED_NODES_PER_SP * SP_BASE),
                "authored_edges": round(ADJUSTED_EDGES_PER_SP * SP_BASE)},
            "batches_at_12sp": -(-SP_BASE // SP_PER_BATCH),
        }
        d["estimate"] = est
        d["model_inputs"] = {
            "pilot_nodes_per_sp": PILOT_NODES_PER_SP,
            "pilot_authored_edges_per_sp": PILOT_EDGES_PER_SP,
            "pilot_held_per_sp": PILOT_HELD_PER_SP,
            "adjusted_nodes_per_sp": ADJUSTED_NODES_PER_SP,
            "adjusted_authored_edges_per_sp": ADJUSTED_EDGES_PER_SP,
            "sp_per_batch": SP_PER_BATCH,
            "provenance": ("graph/reports/C28_MULTI_SUBJECT_EXPANSION_SPEC.md "
                           "§6-K0(iv) (the §16 sanctioned pilot ratios and the "
                           "chemistry program's observed discipline-adjusted "
                           "actuals)")},
        ok = (est["pilot_model"]["nodes"] == 451
              and est["pilot_model"]["authored_edges"] == 517
              and est["pilot_model"]["held"] == 188
              and est["discipline_adjusted"]["nodes"] == 188
              and est["discipline_adjusted"]["authored_edges"] == 301
              and est["batches_at_12sp"] == 16
              and est["sp_base"] == G1_unique_codes(r))
    except Exception as e:  # noqa: BLE001
        ok, d["error"] = False, repr(e)
    gate("G5_k0_iv_scope_estimate", ok, d)

    # ---- G6: P3 folder discipline — K0 creates no ratified-plane state ------
    d = {}
    try:
        tree = subprocess.run(
            ["git", "-C", str(REPO), "ls-tree", "--name-only", "HEAD", "graph/"],
            capture_output=True, text=True).stdout.split()
        registry = r.read_text("scripts/graph_paths.yaml")
        d["graph_dirs"] = tree
        d["registry_has_maths_a_qual"] = (
            "  igcse-maths-a:" in registry)
        d["derived_has_maths_a_concepts"] = _exists(
            f"Official-Specifications/parsed/_derived/graph/{QUAL}/concepts.yaml")
        ok = ("graph/igcse-chemistry" in tree
              and "graph/igcse-maths-a" not in tree
              and not d["registry_has_maths_a_qual"]
              and not d["derived_has_maths_a_concepts"])
    except Exception as e:  # noqa: BLE001
        ok, d["error"] = False, repr(e)
    gate("G6_p3_folder_discipline", ok, d)

    result = {
        "schema": "syllabai.c29-k0-check/1.0",
        "task": "T-C29 K0 commissioning — igcse-maths-a (course "
                "igcse-maths-a-18-higher, 4MA1 Higher)",
        "generated_utc": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "head": subprocess.run(["git", "-C", str(REPO), "rev-parse", "HEAD"],
                               capture_output=True, text=True).stdout.strip(),
        "gates": gates,
        "read_methods": r.methods,
        "all_pass": all(g["status"] in ("PASS", "SKIP")
                        for g in gates.values())
        and gates["G4_hub_mirror_agreement"]["status"] != "FAIL",
    }
    REPORT.write_text(json.dumps(result, indent=1) + "\n", encoding="utf-8")
    for name, g in gates.items():
        print(f"{g['status']:4}  {name}")
    print(f"ALL_PASS = {result['all_pass']}  ->  {REPORT}")
    return 0 if result["all_pass"] else 1


def _exists(rel: str) -> bool:
    out = subprocess.run(["git", "-C", str(REPO), "cat-file", "-e",
                          f"HEAD:{rel}"], capture_output=True)
    return out.returncode == 0


def G1_unique_codes(r: R) -> int:
    sp = r.read_json(f"Official-Specifications/parsed/{QUAL}/spec_points.json")
    rows = sp if isinstance(sp, list) else sp.get("spec_points", [])
    return len({row["official_code"] for row in rows})


if __name__ == "__main__":
    sys.exit(main())
