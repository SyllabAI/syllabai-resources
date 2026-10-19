#!/usr/bin/env python3
"""c42_r33_repair_check.py — T-C42 R33 two-way audit (the R30 check shape).

A1 inventory agreement: the R33 section_overrides + promotions amendment
   cover exactly the R32-defect-inventory disposition set — the 3 verdict
   rows of scripts/c42_r33_repair_verdicts.yaml (rounding-and-estimation
   ords 6/7/8, the 1.8B -> 1.8D re-home batch: the fired R32 fresh REJECT
   ord 8 + the adjudicated siblings ords 6 and 7); no dupes, no extras;
   the amendment's 3 supersedes cover exactly the 3 HUMAN_VALIDATED movers
   and its excluded/added blocks are EMPTY (supersedes only — no DEMOTEs,
   no sign-offs owed: the R30 round discharged all 4 H3 holds of record);
   the 2 retain rulings ride NO carrier entry (zero movement); the
   rounding-half method rows (ords 1-4) carry NO override (not in the
   fired inventory — the anti-forgery rule).
A2 projection agreement: scripts/c42_section_overrides_r33.yaml equals the
   verdict record — 3 verdicted REATTRIBUTE entries (all HV, override_code
   4MA1-1.8D), zero DEMOTE entries, the 2 retain rulings, the SPLIT
   note-level scoping block, the census remarks, an EMPTY
   dated-corrections block, and the promoted-surface-amendment pointer
   (3+0+0); NO h3_signoffs block exists (the discharge continuity: the 3
   R30 sign-off rows verify HUMAN_VALIDATED of record and the re-homed
   drawing ord 0 stays SUGGESTED at 3.3I); zero SUGGESTED rows ride 1.8B
   or 1.8D.
A3 code domain: every REATTRIBUTE override_code is a canonical-188 member,
   differs from current_code, equals 4MA1-1.8D; every current_code matches
   the live substrate (4MA1-1.8B); all 3 movers HUMAN_VALIDATED.
A4 wordings + ledger facts + corpus pins: the registry wordings carry the
   verdict citations verbatim (1.8B 'round to a given number of significant
   figures or decimal places'; 1.8D 'use estimation to evaluate
   approximations to numerical calculations'); the C30 ledger facts hold —
   1.8B and 1.8D BOTH ABSENT (Higher-only/single-tier; the tier-artifact
   escape closed); the corpus chunk texts (read live via the c40 reader)
   carry the verdicts' evidence verbatim — ord 6 the estimation-purpose
   quotes, ord 7 the estimation-method quotes incl. the given-degree
   deferral, ord 8 the evaluation tables + the over/under worked example,
   ord 5 the 3-s.f. worked example + the direction-in-context rulings (the
   RETAIN basis), ord 0 heading-only 21 chars — AND the negative pins: the
   1.8B wording fragment is absent from ords 6/7/8, the 1.8D fragment is
   absent from ord 5; the movers' chunk shas match the live substrate.
A5 joins STAND + resolution byte-untouched: the note's own anchor
   (spcpt_p8zkdCF8QVvDZyVX at 4MA1-1.8B) and the related-calculations
   anchor (spcpt_crKbmb6wVjM4yPJh at 4MA1-1.8D, the R10 STANDING join)
   stand at HEAD (the join layer untouched — the store rows move, the
   joins stand); the resolution file is byte-identical between the
   round-start HEAD (d8853ec) and the audit HEAD.
A6 substrate pins + promoted-surface guard: the store is the R32-of-record
   state (sha16 4aeb73e1575f9586; 917 rows = 831 HUMAN_VALIDATED + 4
   anchored SUGGESTED + 82 worklist); the 3 movers are R5-pinned at
   4MA1-1.8B with matching identities; the per-code censuses are 1.8B = 9
   anchored rows (all HV — the note's 9) and 1.8D = 3 anchored rows (all
   HV — the related-calculations ords 0/1/3); zero SUGGESTED rows on
   either code; no 1.8B or 1.8D row carries a worklist_reason.
A7 idempotency: re-running the projection emitter is byte-identical
   (deterministic regeneration).
A8/A10 footprint + commit state: the working-tree delta vs the round-start
   HEAD (d8853ec) is within the declared R33 footprint (pre-commit form);
   post-commit the delta is empty and the check is re-runnable (the
   C8/X10 precedent).
A9 round artifacts: the verdict record pins its own blocks (3 section
   overrides / 2 retain rulings / 1 scoping note / 2 census remarks) and
   the record md + json pin the same disposition set; the projected
   re-key ids in the record match the c40 identity function recomputed
   live (8f22e1623c025e18 / bb44385407a47188 / 68c165d51b56047a).

Writes its own report graph/reports/C42_R33_REPAIR_CHECK.json.
Exit 0 iff every check passes.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "graph/reports/C42_R33_REPAIR_CHECK.json"
VERDICTS = REPO / "scripts/c42_r33_repair_verdicts.yaml"
OVERRIDES = REPO / "scripts/c42_section_overrides_r33.yaml"
AMENDMENT = REPO / "scripts/c42_r33_promotions_amendment.yaml"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
REGISTRY = REPO / "graph/igcse-maths-a/specification_points.yaml"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"
JOIN = REPO / ("Official-Specifications/parsed/_derived/notes-join/"
               "igcse-maths-a-18-higher.json")
PROMOTIONS = REPO / "scripts/c42_r5_promotions.yaml"
REC_MD = REPO / "graph/reports/C42_R33_RESOLUTION_REPAIR_RECORD.md"
REC_JSON = REPO / "graph/reports/C42_R33_RESOLUTION_REPAIR_RECORD.json"
RES_GIT = "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json"
ROUND_START = "d8853ec"

NOTE_PATH = ("notes/1-numbers-and-the-number-system/"
             "rounding-estimation-and-bounds/rounding-and-estimation.json")

# the fired inventory + the zero-movement continuity set
MOVERS = {"7169cc1735d43642": 8, "a7c0585948a3e06e": 6,
          "b5c13a3e2908b8d1": 7}
RETAIN_ROWS = {"38ca995fa13cd5bb": 5, "8051d57122e682f7": 0}
NOT_FIRED = {"ea1e00fd2aa484ad": 1, "ba9cb33680c338a4": 2,
             "e7b9b7d3cbbdbbd6": 3, "a1510bc4ed0196b2": 4}
# the R30 discharge, verified landed (the H3 continuity)
DISCHARGED_HV = ["1dfc65df88b35d69", "2d44bcf00f589c18",
                 "56905a113334dcd1"]
DISCHARGED_SUGG = {"51885591ddc420cf": "4MA1-3.3I"}
PROJECTED_REKEYS = {"7169cc1735d43642": "68c165d51b56047a",
                    "a7c0585948a3e06e": "8f22e1623c025e18",
                    "b5c13a3e2908b8d1": "bb44385407a47188"}

FOOTPRINT = [
    "scripts/c42_r33_repair_verdicts.yaml",
    "scripts/c42_r33_override_projection.py",
    "scripts/c42_r33_repair_check.py",
    "scripts/c42_section_overrides_r33.yaml",
    "scripts/c42_r33_promotions_amendment.yaml",
    "graph/reports/C42_R33_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R33_RESOLUTION_REPAIR_RECORD.json",
    "graph/reports/C42_R33_REPAIR_CHECK.json",
]

CHECKS = []


def ok(name, detail):
    CHECKS.append({"check": name, "ok": True, "detail": detail})
    print(f"  PASS {name}: {detail}")


def die(msg):
    print(f"FAIL-CLOSED: {msg}", file=sys.stderr)
    sys.exit(1)


def sha16(data) -> str:
    b = data.encode("utf-8") if isinstance(data, str) else data
    return hashlib.sha256(b).hexdigest()[:16]


def squash(s: str) -> str:
    import re
    return re.sub(r"\s+", "", s or "").lower()


def nsq(s: str) -> str:
    """Markdown-insensitive squash: c40.norm (the corpus convention) then
    whitespace-stripped lowercase — corpus pins match through **bold**,\
    links and LaTeX wrappers."""
    return squash(c40_norm_cache["fn"](s or ""))


c40_norm_cache = {"fn": (lambda x: x)}


def git(args) -> str:
    return subprocess.run(["git", "-C", str(REPO)] + args,
                          capture_output=True, text=True, check=True).stdout


def git_bytes(rev_path: str) -> bytes:
    return subprocess.run(["git", "-C", str(REPO), "show", rev_path],
                          capture_output=True, check=True).stdout


def main() -> int:
    for p in (VERDICTS, OVERRIDES, AMENDMENT, STORE, REGISTRY, LEDGER, JOIN,
              PROMOTIONS, REC_MD, REC_JSON):
        if not p.exists():
            die(f"required artifact missing: {p.relative_to(REPO)}")

    ver = yaml.safe_load(VERDICTS.read_text(encoding="utf-8"))
    ovr = yaml.safe_load(OVERRIDES.read_text(encoding="utf-8"))
    amd = yaml.safe_load(AMENDMENT.read_text(encoding="utf-8"))
    store = yaml.safe_load(STORE.read_text(encoding="utf-8"))
    reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
    points = {p["code"] for p in reg["specification_points"]}
    reg_pts = {p["code"]: p for p in reg["specification_points"]}
    ledger = json.loads(LEDGER.read_text(encoding="utf-8"))
    led_rows = {r["official_code"]: r for r in ledger["rows"]}
    join = json.loads(JOIN.read_text(encoding="utf-8"))
    promo = yaml.safe_load(PROMOTIONS.read_text(encoding="utf-8"))
    promo_pins = {e["row"]["mapping_id"]: e["row"]
                  for e in promo["promotions"]}
    rec = json.loads(REC_JSON.read_text(encoding="utf-8"))

    rows_by_id = {r["mapping_id"]: r for r in store["rows"]}
    v_by_mid = {v["mapping_id"]: v
                for v in ver["section_overrides"].values()}
    ovr_entries = {e["mapping_id"]: e for e in ovr["overrides"]}
    sup = {e["mapping_id"]: e for e in amd["supersedes_code"]}
    exc = amd["excluded"]
    added = amd["added"]
    retains = set(ver["retain_rulings"]) - {"contract"}
    retain_ids = {ver["retain_rulings"][k]["mapping_id"] for k in retains}

    # ---- the corpus reader (the c40 convention: disk-first / git-fallback) --
    sys.path.insert(0, str(REPO / "scripts"))
    import c40_maths_a_chunk_sp_substrate as c40  # noqa
    c40_norm_cache["fn"] = c40.norm
    r_reader = c40.R()
    _, notes = c40.load_corpus(r_reader)
    by_note, _ = c40.span_chunks(notes)
    idx = {(n["manifest"]["path"], c["ordinal"]): c["text"]
           for n in notes for c in by_note[n["manifest"]["path"]]}

    def chunk_text(ordn) -> str:
        t = idx.get((NOTE_PATH, ordn))
        if t is None:
            die(f"corpus chunk {NOTE_PATH}::{ordn} not found by the c40 "
                f"reader")
        return t

    # ---- A1 inventory agreement ------------------------------------------------
    if sorted(ovr_entries) != sorted(v_by_mid):
        die("A1: override ids != verdict ids")
    if sorted(ovr_entries) != sorted(MOVERS):
        die(f"A1: disposition set drifted: {sorted(ovr_entries)}")
    for m, ordn in MOVERS.items():
        e = ovr_entries[m]
        srow = rows_by_id[m]
        if e["action"] != "REATTRIBUTE" or e["override_code"] != "4MA1-1.8D":
            die(f"A1: {m} action/target drift")
        if srow["chunk"]["ordinal"] != ordn or \
                srow["note_path"] != NOTE_PATH:
            die(f"A1: {m} note::ordinal identity drift")
        if srow["validation_status"] != "HUMAN_VALIDATED":
            die(f"A1: {m} is not HUMAN_VALIDATED")
    if sorted(sup) != sorted(MOVERS) or exc or added:
        die("A1: amendment shape drifted — 3 supersedes + 0 excluded + "
            "0 added expected (supersedes only)")
    for m in MOVERS:
        if m not in promo_pins:
            die(f"A1: mover {m} not R5-pinned")
        if promo_pins[m].get("spec_code") != "4MA1-1.8B":
            die(f"A1: mover {m} pin code drift")
    movers = set(ovr_entries)
    if retain_ids & movers:
        die("A1: retain rows must ride NO map entry")
    if sorted(retain_ids) != sorted(RETAIN_ROWS):
        die("A1: retain set drifted")
    for m, ordn in RETAIN_ROWS.items():
        if rows_by_id[m]["chunk"]["ordinal"] != ordn or \
                rows_by_id[m]["spec_code"] != "4MA1-1.8B":
            die(f"A1: retain row {m} identity drift")
    for m, ordn in NOT_FIRED.items():
        if m in movers:
            die(f"A1: NOT-FIRED row {m} (ord {ordn}) carries an override — "
                f"the anti-forgery rule")
    ok("A1_inventory_agreement",
       "overrides == verdicts == the 3-row 1.8B -> 1.8D re-home batch (the "
       "fired ord 8 + adjudicated ords 6/7); amendment 3 supersedes + 0 "
       "exclusions + 0 additions; retains ride no carrier (zero movement); "
       "the rounding-half ords 1-4 untouched")

    # ---- A2 projection agreement --------------------------------------------------
    acts = sorted(e["action"] for e in ovr_entries.values())
    if acts != ["REATTRIBUTE"] * 3:
        die(f"A2: unexpected action mix {acts}")
    for e in ovr_entries.values():
        v = v_by_mid[e["mapping_id"]]
        if e["action"] != v["disposition"] \
                or (e["override_code"] or None) != (v.get("override_code") or None) \
                or e["current_code"] != v["current_code"]:
            die(f"A2: map/verdict drift on {e['mapping_id']}")
    if "h3_signoffs" in ovr:
        die("A2: no h3_signoffs block expected this round (zero owed)")
    if len(retains) != 2:
        die("A2: expected exactly 2 retain rulings")
    scoping = ovr.get("note_level_scoping") or []
    if scoping != ver["note_level_scoping"] or len(scoping) != 1:
        die("A2: note-level scoping block drifted")
    if scoping and scoping[0].get("note_slug") != "rounding-and-estimation":
        die("A2: scoping note slug drift")
    if ovr.get("dated_corrections") != []:
        die("A2: dated corrections expected EMPTY this round")
    if not ovr.get("census_remarks") or len(ovr["census_remarks"]) < 2:
        die("A2: census remarks missing")
    psa = ovr.get("promoted_surface_amendment") or {}
    if psa.get("amendment_file") != "scripts/c42_r33_promotions_amendment.yaml" \
            or psa.get("base_file_untouched") is not True \
            or psa.get("supersedes") != 3 or psa.get("excluded") != 0 \
            or psa.get("added") != 0:
        die("A2: promoted-surface-amendment pointer drifted")
    if amd.get("schema") != "c42-r31-promotions-amendment/1.0" \
            or amd.get("base_file_sha256_16") != "9bad739bd79e5899" \
            or amd.get("prior_amendments") != \
            ["scripts/c42_r26_promotions_amendment.yaml",
             "scripts/c42_r30_promotions_amendment.yaml"]:
        die("A2: amendment schema/base/prior-amendment pins drifted")
    # the discharge continuity: the 3 R30 sign-off rows HV of record, the
    # re-homed hold SUGGESTED at 3.3I, zero SUGGESTED rows on 1.8B/1.8D
    for m in DISCHARGED_HV:
        if rows_by_id[m].get("validation_status") != "HUMAN_VALIDATED":
            die(f"A2: discharged sign-off row {m} not HV of record")
    for m, code in DISCHARGED_SUGG.items():
        r = rows_by_id.get(m)
        if r is None:
            die(f"A2: re-homed hold {m} not found in the live substrate")
        if r.get("validation_status") != "SUGGESTED" or \
                r.get("spec_code") != code:
            die(f"A2: re-homed hold {m} drifted from SUGGESTED@{code}")
    sugg_18 = [m for m, r in rows_by_id.items()
               if r.get("validation_status") == "SUGGESTED"
               and r.get("spec_code") in ("4MA1-1.8B", "4MA1-1.8D")]
    if sugg_18:
        die(f"A2: SUGGESTED rows ride 1.8B/1.8D: {sugg_18}")
    ok("A2_projection_agreement",
       "map == verdicts (3 REATTRIBUTE, all HV, all -> 1.8D); retains/"
       "scoping/remarks pinned; zero sign-off blocks; the R30 discharge "
       "verified landed (3 HV + 1 SUGGESTED@3.3I); zero SUGGESTED rows on "
       "1.8B/1.8D; amendment schema + base pin + prior-amendments pinned")

    # ---- A3 code domain -------------------------------------------------------------
    for m, e in ovr_entries.items():
        srow = rows_by_id.get(m)
        if srow is None:
            die(f"A3: {m} not in the live substrate")
        if srow["spec_code"] != e["current_code"] != "4MA1-1.8B" and \
                srow["spec_code"] != e["current_code"]:
            die(f"A3: current_code drift on {m}")
        if e["current_code"] != "4MA1-1.8B":
            die(f"A3: {m} current is not 1.8B")
        if e["override_code"] not in points:
            die(f"A3: target {e['override_code']} outside the ratified 188")
        if e["override_code"] == e["current_code"]:
            die(f"A3: target equals current on {m}")
        if srow.get("validation_status") != "HUMAN_VALIDATED":
            die(f"A3: {m} status drift")
    ok("A3_code_domain",
       "3 targets = 4MA1-1.8D, canonical-188 member, distinct from the "
       "1.8B currents; currents match the live substrate; all 3 movers "
       "HUMAN_VALIDATED")

    # ---- A4 wordings + ledger facts + corpus pins --------------------------------------
    w18b = reg_pts["4MA1-1.8B"].get("official_wording") or ""
    w18d = reg_pts["4MA1-1.8D"].get("official_wording") or ""
    if squash(w18b) != squash("round to a given number of significant "
                              "figures or decimal places"):
        die("A4: 1.8B wording drifted")
    if squash(w18d) != squash("use estimation to evaluate approximations "
                              "to numerical calculations"):
        die("A4: 1.8D wording drifted")
    for bare in ("1.8B", "1.8D"):
        if bare in led_rows:
            die(f"A4: {bare} expected ABSENT from the C30 ledger "
                f"(single-tier — the tier-artifact escape closed)")
    # corpus pins: the verdicts' evidence verbatim in the chunks
    pins = {
        6: ["approximations for difficult calculations",
            "estimate a calculation to check your answers",
            "much bigger or smaller than your estimated value"],
        7: ["Round each number in the question to a sensible degree, then "
            "perform the calculation",
            "The general rule is to round numbers to 1 significant figure",
            "The exam question will usually tell you what to round each "
            "number to",
            "Avoid rounding values to zero"],
        8: ["Overestimate", "Underestimate", "Not easy to tell",
            "whether the estimate is an overestimate or an underestimate",
            "This is an overestimate as the numerator was rounded up and "
            "the denominator was rounded down"],
        5: ["Round the following numbers to 3 significant figures",
            "round up, to 4 adults", "round down, to 4 crates",
            "2 530 457 to 3 significant figures"],
    }
    texts = {}
    for ordn, needles in pins.items():
        t = chunk_text(ordn)
        texts[ordn] = t
        ns = nsq(t)
        for needle in needles:
            if nsq(needle) not in ns:
                die(f"A4: ord {ordn} corpus pin missing: {needle!r}")
    # negative pins: the wordings' fragments must NOT cross the split
    for ordn in (6, 7, 8):
        if nsq("significant figures or decimal places") in nsq(texts[ordn]):
            die(f"A4: ord {ordn} unexpectedly carries 1.8B's wording")
    if nsq("evaluate approximations") in nsq(texts[5]):
        die("A4: ord 5 unexpectedly carries 1.8D's wording fragment")
    # heading-only ord 0 (21 chars, text == heading)
    t0 = chunk_text(0)
    if len(t0) != 21 or nsq(t0) != nsq("Rounding & estimation"):
        die(f"A4: ord 0 heading-only shape drifted: {len(t0)} chars")
    # the movers' chunk shas match the live substrate (the mechanical layer)
    for m, ordn in MOVERS.items():
        if c40.sha16(texts[ordn]) != rows_by_id[m]["chunk"]["sha256_16"]:
            die(f"A4: chunk sha drift on {m} (ord {ordn})")
    for m, ordn in RETAIN_ROWS.items():
        if c40.sha16(chunk_text(ordn)) != \
                rows_by_id[m]["chunk"]["sha256_16"]:
            die(f"A4: chunk sha drift on retain row {m} (ord {ordn})")
    ok("A4_wordings_ledger_corpus",
       "registry wordings verbatim (1.8B / 1.8D); ledger: 1.8B + 1.8D both "
       "ABSENT (single-tier); corpus pins verified live (ord 6 purpose / "
       "ord 7 method + deferral / ord 8 evaluation tables + worked example "
       "/ ord 5 the 3-s.f. worked example + direction rulings); negative "
       "pins hold across the split; ord 0 heading-only 21 chars; chunk shas "
       "match the substrate")

    # ---- A5 joins STAND + resolution byte-untouched -------------------------------------
    join_rows = {r["anchor_id"]: r for r in join["joins"]}
    for aid, want in [("spcpt_p8zkdCF8QVvDZyVX", "4MA1-1.8B"),
                      ("spcpt_crKbmb6wVjM4yPJh", "4MA1-1.8D")]:
        jr = join_rows.get(aid)
        if jr is None or jr.get("store_row_code") != want:
            got = (jr or {}).get("store_row_code")
            die(f"A5: join row for {aid} does not stand at {want} (got {got})")
    if join_rows["spcpt_p8zkdCF8QVvDZyVX"].get("note_path") != NOTE_PATH:
        die("A5: the note anchor's note_path drifted")
    res_start = git_bytes(f"{ROUND_START}:{RES_GIT}")
    res_head = git_bytes(f"HEAD:{RES_GIT}")
    if res_start != res_head:
        die("A5: resolution file drifted between the round-start HEAD and HEAD")
    ok("A5_joins_resolution",
       "the note's 1.8B anchor + the related-calculations 1.8D R10 STANDING "
       "anchor stand at HEAD (the join layer untouched); resolution file "
       "byte-identical d8853ec -> HEAD")

    # ---- A6 substrate pins + promoted-surface guard ---------------------------------------
    if sha16(STORE.read_bytes()) != "4aeb73e1575f9586":
        die("A6: store sha drifted from the R31/R32-of-record landing")
    hv = {m for m, r in rows_by_id.items()
          if r.get("validation_status") == "HUMAN_VALIDATED"}
    sugg_anch = {m for m, r in rows_by_id.items()
                 if r.get("validation_status") == "SUGGESTED"
                 and r.get("spec_code") and "chunk" in r}
    sugg_all = {m for m, r in rows_by_id.items()
                if r.get("validation_status") == "SUGGESTED"}
    worklist = sugg_all - sugg_anch  # unresolved-span (no spec_code) +
    # uncovered-SP DEFER rows (spec_code + worklist_reason, no chunk)
    if len(rows_by_id) != 917 or len(hv) != 831 or len(sugg_anch) != 4 \
            or len(worklist) != 82:
        die(f"A6: store is not the R32-of-record state (917 = 831 HV + 4 "
            f"anchored SUGGESTED + 82 worklist, got {len(rows_by_id)} = "
            f"{len(hv)} + {len(sugg_anch)} + {len(worklist)})")
    for m in MOVERS:
        pin = promo_pins.get(m)
        srow = rows_by_id[m]
        if pin is None:
            die(f"A6: {m} not pinned in the R5 promotions file")
        if (pin.get("spec_code") != srow["spec_code"]
                or pin.get("note_path") != srow["note_path"]
                or pin.get("chunk_ordinal") != srow["chunk"]["ordinal"]):
            die(f"A6: promotions pin identity drift on {m}")
    n18b = [r for r in store["rows"]
            if r.get("spec_code") == "4MA1-1.8B" and "chunk" in r]
    n18d = [r for r in store["rows"]
            if r.get("spec_code") == "4MA1-1.8D" and "chunk" in r]
    if len(n18b) != 9 or len(n18d) != 3:
        die(f"A6: per-code censuses drifted: 1.8B={len(n18b)} (want 9), "
            f"1.8D={len(n18d)} (want 3)")
    if {r["mapping_id"] for r in n18b} != set(MOVERS) | set(RETAIN_ROWS) \
            | set(NOT_FIRED):
        die("A6: the 1.8B anchored set is not the note's 9 rows")
    if {r["mapping_id"] for r in n18d} != \
            {"2eda8a36597b4cc4", "915aa344930d5c08", "ff18544a0e877b96"}:
        die("A6: the 1.8D anchored set is not the related-calculations trio")
    for r in n18b + n18d:
        if r.get("validation_status") != "HUMAN_VALIDATED":
            die(f"A6: {r['mapping_id']} anchored row not HUMAN_VALIDATED")
        if r.get("worklist_reason"):
            die(f"A6: {r['mapping_id']} carries a worklist_reason")
    ok("A6_substrate_pins",
       "store at the R32-of-record state (sha 4aeb73e1575f9586; 917 = 831 + "
       "4 + 82); 3 movers R5-pinned at 1.8B with matching identities; "
       "per-code censuses 1.8B = 9 / 1.8D = 3, all HV, zero worklist rows")

    # ---- A9 round artifacts + projected re-keys ---------------------------------------------
    if len(v_by_mid) != 3 or len(retains) != 2:
        die("A9: verdict record blocks drifted")
    if len(ver["note_level_scoping"]) != 1 or \
            len(ver["census_remarks"]) != 2 or \
            ver["dated_corrections"] != []:
        die("A9: verdict record scoping/remarks/corrections blocks drifted")
    if rec.get("baseline", {}).get("store_sha256_16") != sha16(STORE.read_bytes()):
        die("A9: record baseline store pin drifted")
    rec_ids = sorted(o["mapping_id"] for o in rec["section_overrides"])
    if rec_ids != sorted(ovr_entries):
        die("A9: record section_overrides != the disposition set")
    sha16f, normf = c40.sha16, c40.norm
    for o in rec["section_overrides"]:
        srow = rows_by_id[o["mapping_id"]]
        want = sha16f(f"{srow['note_path']}|{o['target']}|"
                      f"{normf(srow['evidence_quote'])}")
        if o["projected_new_id"] != want:
            die(f"A9: projected re-key drift on {o['mapping_id']}")
        if PROJECTED_REKEYS[o["mapping_id"]] != want:
            die(f"A9: projected re-key != the recorded pin on "
                f"{o['mapping_id']}")
    ok("A9_round_artifacts",
       "record md + json pinned; the projected re-key ids match the c40 "
       "identity function recomputed live and the recorded pins "
       "(8f22e1623c025e18 / bb44385407a47188 / 68c165d51b56047a)")

    # ---- A7 idempotency -----------------------------------------------------------------
    h1 = sha16(OVERRIDES.read_bytes()), sha16(AMENDMENT.read_bytes())
    subprocess.run([sys.executable,
                    str(REPO / "scripts/c42_r33_override_projection.py")],
                   capture_output=True, check=True)
    h2 = sha16(OVERRIDES.read_bytes()), sha16(AMENDMENT.read_bytes())
    if h1 != h2:
        die("A7: deterministic regeneration drifted")
    ok("A7_idempotency",
       "override map + promotions amendment byte-identical re-runs")

    # ---- A8/A10 footprint + commit state ---------------------------------------------------
    head = git(["rev-parse", "HEAD"]).strip()
    if head.startswith(ROUND_START):
        changed = [ln[3:].strip() for ln in
                   git(["status", "--porcelain"]).splitlines() if ln.strip()]
        outside = [c for c in changed if c not in FOOTPRINT
                   and not any(c.endswith(f" -> {f}") for f in FOOTPRINT)]
        if outside:
            die(f"A8: working-tree delta outside the declared footprint: "
                f"{outside[:5]}...")
        ok("A8_footprint_precommit",
           f"delta vs {ROUND_START} is exactly the declared {len(FOOTPRINT)}-file "
           f"R33 footprint (pre-commit form)")
    else:
        dirty = git(["status", "--porcelain"]).strip()
        if dirty:
            die(f"A10: post-commit tree is dirty: {dirty[:200]}")
        ok("A10_committed_clean",
           f"HEAD {head[:8]} is the round commit; tree clean; the check "
           f"re-runs committed-clean (the C8/X10 precedent)")

    # ---- report ---------------------------------------------------------------------------------
    out = {
        "schema": "c42-r33-repair-check/1.0",
        "task": "T-C42",
        "stage": "r33-operator-delegate-dispositions-check",
        "round": "R33",
        "round_start": ROUND_START,
        "audited_head": head,
        "baseline_store_sha256_16": sha16(STORE.read_bytes()),
        "override_map_sha256_16": sha16(OVERRIDES.read_bytes()),
        "amendment_sha256_16": sha16(AMENDMENT.read_bytes()),
        "verdicts_sha256_16": sha16(VERDICTS.read_bytes()),
        "record_sha256_16": sha16(REC_JSON.read_bytes()),
        "checks": CHECKS,
        "passed": len(CHECKS),
        "total": len(CHECKS),
        "result": "ALL PASS",
    }
    OUT.write_text(json.dumps(out, indent=2, ensure_ascii=False) + "\n",
                   encoding="utf-8")
    print(f"c42_r33_repair_check: {out['result']} ({len(CHECKS)}/{len(CHECKS)}) "
          f"-> {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
