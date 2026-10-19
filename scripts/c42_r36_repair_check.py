#!/usr/bin/env python3
"""c42_r36_repair_check.py — T-C42 R36 two-way audit (the R33 check shape).

A1 inventory agreement: the R36 section_overrides + promotions amendment
   cover exactly the R35-defect-inventory disposition set — the single
   verdict row of scripts/c42_r36_repair_verdicts.yaml (basic-percentages
   :: 4, a107f5041769fdd9, the R35 fresh REJECT at 1.6F, disposition
   DEMOTE_TO_WORKLIST); no dupes, no extras; the amendment's excluded block
   covers exactly that row and its supersedes/added blocks are EMPTY
   (exclusion only — no DEMOTE-less supersedes, no sign-offs owed: the R30
   round discharged all 4 H3 holds of record); NOTHING else rides a carrier
   entry — the not-fired guard: basic-percentages ords 0/1/2/3 and the
   reverse-percentages trio carry NO override (the anti-forgery rule).
A2 projection agreement: scripts/c42_section_overrides_r36.yaml equals the
   verdict record — 1 verdicted DEMOTE_TO_WORKLIST entry (HV, override_code
   null), zero REATTRIBUTE entries, the zero-retain contract, the
   note-level scoping block, the census remarks, an EMPTY dated-corrections
   block, and the promoted-surface-amendment pointer (0+1+0); NO
   h3_signoffs block exists; zero SUGGESTED rows ride 1.6F; the amendment's
   schema + base pin (9bad739bd79e5899) + prior_amendments
   (R26+R30+R33) pinned.
A3 code domain: the DEMOTE entry carries override_code null (the c40 R8
   rule — no target exists); its current_code matches the live substrate
   (4MA1-1.6F); the mover is HUMAN_VALIDATED; no re-pin arises.
A4 wordings + ledger facts + corpus pins: the registry wordings carry the
   verdict citations verbatim (1.6F 'use reverse percentages'; 1.6C the
   converse; 1.6E simple percentage problems); the NO-TARGET negative scan
   holds over the whole ratified 188 (the only express+percentage wording
   is 1.6C; no wording names the express-one-number-as-a-percentage
   surface); 1.6F is ABSENT from the C30 ledger (single-tier; the
   tier-artifact escape closed); the corpus chunk text (read live via the
   c40 reader) carries the verdict's evidence verbatim — the heading, the
   forward method bullets, 'So 7 is 35% of 20', the deposit worked example
   with 0.125 and 12.5 — AND the negative pins: the 'reverse percentage'
   fragment, the 1.6C converse fragment and the reverse-surface vocabulary
   are ABSENT from the chunk; the chunk sha matches the live substrate.
A5 joins STAND + resolution byte-untouched: the note's corpus anchor
   (spcpt_FHRjdMc6tvRR553q at 4MA1-1.6F) stands at HEAD (the join layer
   untouched — the store rows move, the joins stand); the resolution file
   is byte-identical between the round-start HEAD (4c5c42e) and the audit
   HEAD.
A6 substrate pins + promoted-surface guard: the store is the R34/R35
   landing of record (sha16 9174915650d49f4a) and is BYTE-IDENTICAL to the
   round-start HEAD's store (ZERO store bytes move this round); 917 rows =
   831 HUMAN_VALIDATED + 4 anchored SUGGESTED + 82 worklist; the mover is
   R5-pinned at 1.6F with matching identity; the per-code 1.6F census is
   6 anchored rows (all HV — the mover + the 5 keepers), zero worklist
   rows; the meta census pins hold (835 / 27 / 55 / 133 / 188).
A7 idempotency: re-running the projection emitter is byte-identical
   (deterministic regeneration).
A8/A10 footprint + commit state: the working-tree delta vs the round-start
   HEAD (4c5c42e) is within the declared R36 footprint (pre-commit form);
   post-commit the delta is empty and the check is re-runnable (the
   C8/X10 precedent).
A9 round artifacts: the verdict record pins its own blocks (1 section
   override / 0 retain rows / 1 scoping note / 2 census remarks); the
   record md + json pin the same disposition set; the projected demoted
   re-key in the record matches the c40 DEMOTE identity function
   recomputed live (8254a7fc75ad2946).

Writes its own report graph/reports/C42_R36_REPAIR_CHECK.json.
Exit 0 iff every check passes.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "graph/reports/C42_R36_REPAIR_CHECK.json"
VERDICTS = REPO / "scripts/c42_r36_repair_verdicts.yaml"
OVERRIDES = REPO / "scripts/c42_section_overrides_r36.yaml"
AMENDMENT = REPO / "scripts/c42_r36_promotions_amendment.yaml"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
REGISTRY = REPO / "graph/igcse-maths-a/specification_points.yaml"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"
JOIN = REPO / ("Official-Specifications/parsed/_derived/notes-join/"
               "igcse-maths-a-18-higher.json")
PROMOTIONS = REPO / "scripts/c42_r5_promotions.yaml"
REC_MD = REPO / "graph/reports/C42_R36_RESOLUTION_REPAIR_RECORD.md"
REC_JSON = REPO / "graph/reports/C42_R36_RESOLUTION_REPAIR_RECORD.json"
RES_GIT = "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json"
STORE_GIT = "graph/igcse-maths-a/spec_chunk_mappings.yaml"
ROUND_START = "4c5c42e"

NOTE_PATH = ("notes/1-numbers-and-the-number-system/"
             "percentages/basic-percentages.json")
MOVER = "a107f5041769fdd9"
MOVER_ORD = 4
MOVER_CODE = "4MA1-1.6F"
MOVER_SHA = "d4947ba63e47dd1f"
ANCHOR_ID = "spcpt_FHRjdMc6tvRR553q"
PROJECTED_DEMOTE_ID = "8254a7fc75ad2946"

# the fired inventory + the zero-movement continuity set
MOVERS = {MOVER: MOVER_ORD}
NOT_FIRED = {"0bbe42313181c4c9": 0, "9eba720edf8767e2": 1,
             "f6d18b1df73d73de": 2, "24f7c615715385b1": 3,
             "0712e32bdab4b9c2": 0, "b50465d5a341e0d6": 1,
             "f581371fd0524930": 2}
KEEPERS = {"0bbe42313181c4c9", "24f7c615715385b1",
           "0712e32bdab4b9c2", "b50465d5a341e0d6", "f581371fd0524930"}

FOOTPRINT = [
    "scripts/c42_r36_repair_verdicts.yaml",
    "scripts/c42_r36_override_projection.py",
    "scripts/c42_r36_repair_check.py",
    "scripts/c42_section_overrides_r36.yaml",
    "scripts/c42_r36_promotions_amendment.yaml",
    "graph/reports/C42_R36_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R36_RESOLUTION_REPAIR_RECORD.json",
    "graph/reports/C42_R36_REPAIR_CHECK.json",
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
    """Markdown-insensitive squash: c40.norm then whitespace-stripped
    lowercase — corpus pins match through **bold**, links and LaTeX."""
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
    sup = amd["supersedes_code"]
    exc = amd["excluded"]
    added = amd["added"]
    retains = set(ver.get("retain_rulings") or {}) - {"contract"}

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
        if e["action"] != "DEMOTE_TO_WORKLIST":
            die(f"A1: {m} action drift")
        if srow["chunk"]["ordinal"] != ordn or \
                srow["note_path"] != NOTE_PATH:
            die(f"A1: {m} note::ordinal identity drift")
        if srow["validation_status"] != "HUMAN_VALIDATED":
            die(f"A1: {m} is not HUMAN_VALIDATED")
    if sup or len(exc) != 1 or added:
        die("A1: amendment shape drifted — 0 supersedes + 1 excluded + "
            "0 added expected (exclusion only)")
    x = exc[0]
    if x.get("mapping_id") != MOVER or x.get("note_path") != NOTE_PATH or \
            x.get("chunk_ordinal") != MOVER_ORD or \
            x.get("pinned_code") != MOVER_CODE or \
            x.get("disposition") != "DEMOTE_TO_WORKLIST":
        die(f"A1: excluded entry identity drift: {x}")
    if MOVER not in promo_pins:
        die("A1: mover not R5-pinned")
    if promo_pins[MOVER].get("spec_code") != MOVER_CODE:
        die("A1: mover pin code drift")
    for m, ordn in NOT_FIRED.items():
        if m in ovr_entries:
            die(f"A1: NOT-FIRED row {m} (ord {ordn}) carries an override — "
                f"the anti-forgery rule")
        srow = rows_by_id.get(m)
        if srow is None or srow.get("validation_status") != "HUMAN_VALIDATED":
            die(f"A1: not-fired row {m} drifted from the anchored surface")
    ok("A1_inventory_agreement",
       "overrides == verdicts == the single fired row a107f5041769fdd9 "
       "(basic-percentages::4, DEMOTE_TO_WORKLIST); amendment 0 supersedes "
       "+ 1 exclusion + 0 additions with the identity pinned; the "
       "not-fired guard holds across basic-percentages ords 0-3 and the "
       "reverse-percentages trio (all HV)")

    # ---- A2 projection agreement --------------------------------------------------
    acts = sorted(e["action"] for e in ovr_entries.values())
    if acts != ["DEMOTE_TO_WORKLIST"]:
        die(f"A2: unexpected action mix {acts}")
    for e in ovr_entries.values():
        v = v_by_mid[e["mapping_id"]]
        if e["action"] != v["disposition"] \
                or (e.get("override_code") or None) != (v.get("override_code") or None) \
                or e["current_code"] != v["current_code"]:
            die(f"A2: map/verdict drift on {e['mapping_id']}")
    if "h3_signoffs" in ovr or "h3_signoffs" in ver:
        die("A2: no h3_signoffs block expected this round (zero owed)")
    if retains:
        die(f"A2: retain rulings expected EMPTY: {sorted(retains)}")
    scoping = ovr.get("note_level_scoping") or []
    if scoping != ver["note_level_scoping"] or len(scoping) != 1:
        die("A2: note-level scoping block drifted")
    if scoping and scoping[0].get("note_slug") != "basic-percentages":
        die("A2: scoping note slug drift")
    if ovr.get("dated_corrections") != []:
        die("A2: dated corrections expected EMPTY this round")
    if not ovr.get("census_remarks") or len(ovr["census_remarks"]) < 2:
        die("A2: census remarks missing")
    psa = ovr.get("promoted_surface_amendment") or {}
    if psa.get("amendment_file") != "scripts/c42_r36_promotions_amendment.yaml" \
            or psa.get("base_file_untouched") is not True \
            or psa.get("supersedes") != 0 or psa.get("excluded") != 1 \
            or psa.get("added") != 0:
        die("A2: promoted-surface-amendment pointer drifted")
    if amd.get("schema") != "c42-r31-promotions-amendment/1.0" \
            or amd.get("base_file_sha256_16") != "9bad739bd79e5899" \
            or amd.get("prior_amendments") != \
            ["scripts/c42_r26_promotions_amendment.yaml",
             "scripts/c42_r30_promotions_amendment.yaml",
             "scripts/c42_r33_promotions_amendment.yaml"]:
        die("A2: amendment schema/base/prior-amendment pins drifted")
    sugg_16 = [m for m, r in rows_by_id.items()
               if r.get("validation_status") == "SUGGESTED"
               and r.get("spec_code") == MOVER_CODE]
    if sugg_16:
        die(f"A2: SUGGESTED rows ride {MOVER_CODE}: {sugg_16}")
    # the ord-3 continuity: standing via the carry chain, not re-litigated
    r3 = rows_by_id["24f7c615715385b1"]
    if r3.get("validation_status") != "HUMAN_VALIDATED" or \
            r3.get("spec_code") != MOVER_CODE:
        die("A2: the ord-3 sibling's standing continuity drifted")
    ok("A2_projection_agreement",
       "map == verdicts (1 HV DEMOTE, override_code null); retains empty; "
       "scoping/remarks pinned; zero sign-off blocks; zero SUGGESTED rows "
       "on 1.6F; the ord-3 sibling stands untouched (the carry chain, the "
       "anti-forgery rule); amendment schema + base pin + prior-amendments "
       "(R26+R30+R33) pinned")

    # ---- A3 code domain -------------------------------------------------------------
    e = ovr_entries[MOVER]
    srow = rows_by_id[MOVER]
    if e.get("override_code") is not None:
        die("A3: the DEMOTE entry carries an override_code — the c40 R8 "
            "rule forbids it (no target exists)")
    if v_by_mid[MOVER].get("override_code") is not None:
        die("A3: the DEMOTE verdict carries an override_code")
    if srow["spec_code"] != e["current_code"] != MOVER_CODE:
        die(f"A3: current_code drift on {MOVER}")
    if srow.get("validation_status") != "HUMAN_VALIDATED":
        die(f"A3: {MOVER} status drift")
    if MOVER_CODE not in points:
        die("A3: the current code is not a ratified-188 member")
    ok("A3_code_domain",
       "DEMOTE carries no target (the c40 R8 rule; the no-target fact "
       "live-verified in A4); current 4MA1-1.6F matches the live "
       "substrate; the mover HUMAN_VALIDATED; no re-pin arises")

    # ---- A4 wordings + ledger facts + corpus pins --------------------------------------
    w16f = reg_pts["4MA1-1.6F"].get("official_wording") or ""
    w16c = reg_pts["4MA1-1.6C"].get("official_wording") or ""
    w16e = reg_pts["4MA1-1.6E"].get("official_wording") or ""
    if squash(w16f) != squash("use reverse percentages"):
        die("A4: 1.6F wording drifted")
    if squash(w16c) != squash("express a percentage as a fraction and as "
                              "a decimal"):
        die("A4: 1.6C wording drifted")
    if squash(w16e) != squash("solve simple percentage problems, including "
                              "percentage increase and decrease"):
        die("A4: 1.6E wording drifted")
    # the NO-TARGET negative scan over the whole ratified 188
    hits = sorted(p["code"] for p in reg["specification_points"]
                  if "express" in (p.get("official_wording") or "").lower()
                  and "percentage" in (p.get("official_wording") or "").lower())
    if hits != ["4MA1-1.6C"]:
        die(f"A4: no-target fact drifted: express+percentage hits {hits}")
    for p in reg["specification_points"]:
        w = (p.get("official_wording") or "").lower()
        if "as a percentage of another" in w or \
                "one number as a percentage" in w:
            die(f"A4: no-target fact drifted: {p['code']} names the surface")
    if "1.6F" in led_rows:
        die("A4: 1.6F expected ABSENT from the C30 ledger (single-tier — "
            "the tier-artifact escape closed)")
    # corpus pins: the verdict's evidence verbatim in the chunk
    pins = [
        "How do I express one number as a percentage of another?",
        "Start by writing one number as a fraction of the other",
        "decimal equivalent of this fraction",
        "denominator of 100",
        "Rewrite this as a percentage",
        "So 7 is 35% of 20",
        "Express the deposit as a percentage of the price of the trip",
        "0.125",
        "12.5",
    ]
    t = chunk_text(MOVER_ORD)
    ns = nsq(t)
    for needle in pins:
        if nsq(needle) not in ns:
            die(f"A4: corpus pin missing: {needle!r}")
    # negative pins: 1.6F's own surface and the converse must be ABSENT
    for frag in ("reverse percentage", "use reverse percentages",
                 "express a percentage as a fraction",
                 "original amount"):
        if nsq(frag) in ns:
            die(f"A4: the chunk unexpectedly carries {frag!r}")
    # the mover's chunk sha matches the live substrate (the mechanical layer)
    if c40.sha16(t) != srow["chunk"]["sha256_16"] or \
            srow["chunk"]["sha256_16"] != MOVER_SHA:
        die(f"A4: chunk sha drift on {MOVER}")
    ok("A4_wordings_ledger_corpus",
       "registry wordings verbatim (1.6F / 1.6C / 1.6E); the no-target "
       "negative scan holds over the ratified 188 (only 1.6C carries "
       "express+percentage — the converse); 1.6F ABSENT from the C30 "
       "ledger (single-tier); corpus pins verified live via the c40 reader "
       "(the heading + the forward method bullets + 'So 7 is 35% of 20' + "
       "the 0.125/12.5 deposit example); negative pins hold ('reverse "
       "percentage' and the converse fragment absent); chunk sha matches "
       "the substrate (d4947ba63e47dd1f)")

    # ---- A5 joins STAND + resolution byte-untouched -------------------------------------
    join_rows = {r["anchor_id"]: r for r in join["joins"]}
    jr = join_rows.get(ANCHOR_ID)
    if jr is None or jr.get("store_row_code") != MOVER_CODE:
        got = (jr or {}).get("store_row_code")
        die(f"A5: join row for {ANCHOR_ID} does not stand at {MOVER_CODE} "
            f"(got {got})")
    if jr.get("note_path") != NOTE_PATH:
        die("A5: the note anchor's note_path drifted")
    res_start = git_bytes(f"{ROUND_START}:{RES_GIT}")
    res_head = git_bytes(f"HEAD:{RES_GIT}")
    if res_start != res_head:
        die("A5: resolution file drifted between the round-start HEAD and HEAD")
    ok("A5_joins_resolution",
       f"the basic-percentages corpus anchor {ANCHOR_ID} stands at 1.6F at "
       f"HEAD (the join layer untouched); resolution file byte-identical "
       f"{ROUND_START} -> HEAD")

    # ---- A6 substrate pins + promoted-surface guard ---------------------------------------
    store_live = STORE.read_bytes()
    if sha16(store_live) != "9174915650d49f4a":
        die("A6: store sha drifted from the R34/R35-of-record landing")
    if git_bytes(f"{ROUND_START}:{STORE_GIT}") != store_live:
        die("A6: ZERO-store-bytes violated — the store differs from the "
            "round-start HEAD")
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
        die(f"A6: store is not the R34/R35-of-record state (917 = 831 HV + 4 "
            f"anchored SUGGESTED + 82 worklist, got {len(rows_by_id)} = "
            f"{len(hv)} + {len(sugg_anch)} + {len(worklist)})")
    pin = promo_pins.get(MOVER)
    if pin is None:
        die("A6: mover not pinned in the R5 promotions file")
    if (pin.get("spec_code") != srow["spec_code"]
            or pin.get("note_path") != srow["note_path"]
            or pin.get("chunk_ordinal") != srow["chunk"]["ordinal"]):
        die("A6: promotions pin identity drift on the mover")
    fam = [r for r in store["rows"]
           if r.get("spec_code") == MOVER_CODE and "chunk" in r]
    if len(fam) != 6:
        die(f"A6: per-code 1.6F census drifted: {len(fam)} (want 6)")
    if {r["mapping_id"] for r in fam} != {MOVER} | KEEPERS:
        die("A6: the 1.6F anchored set is not the mover + the 5 keepers")
    for r in fam:
        if r.get("validation_status") != "HUMAN_VALIDATED":
            die(f"A6: {r['mapping_id']} anchored row not HUMAN_VALIDATED")
        if r.get("worklist_reason"):
            die(f"A6: {r['mapping_id']} carries a worklist_reason")
    meta = store.get("meta") or {}
    for k, want in (("rows_anchored", 835),
                    ("rows_worklist_anchor_unresolved", 27),
                    ("rows_worklist_unmapped_sps", 55),
                    ("sp_codes_covered", 133),
                    ("promoted_rows", 831),
                    ("registry_size", 188)):
        if meta.get(k) != want:
            die(f"A6: meta census pin {k} drifted: {meta.get(k)} (want {want})")
    ok("A6_substrate_pins",
       "store at the R34/R35-of-record state (sha 9174915650d49f4a) and "
       "byte-identical to the round-start HEAD (ZERO store bytes move this "
       "round); 917 = 831 + 4 + 82; the mover R5-pinned at 1.6F with "
       "matching identity; per-code 1.6F census 6 all HV (the mover + the "
       "5 keepers), zero worklist rows; the meta census pins hold")

    # ---- A9 round artifacts + the projected demoted re-key -------------------------------
    if len(v_by_mid) != 1 or retains:
        die("A9: verdict record blocks drifted")
    if len(ver["note_level_scoping"]) != 1 or \
            len(ver["census_remarks"]) != 2 or \
            ver["dated_corrections"] != []:
        die("A9: verdict record scoping/remarks/corrections blocks drifted")
    if rec.get("baseline", {}).get("store_sha16") != sha16(store_live):
        die("A9: record baseline store pin drifted")
    rec_ids = sorted(i["mapping_id"] for i in rec["inventory"]["rows"])
    if rec_ids != sorted(ovr_entries):
        die("A9: record inventory != the disposition set")
    want = hashlib.sha256(
        f"demoted|{NOTE_PATH}|{MOVER_ORD}".encode("utf-8")).hexdigest()[:16]
    if rec.get("projected_rekeys", {}).get(MOVER) != want or want != \
            PROJECTED_DEMOTE_ID:
        die(f"A9: projected demoted re-key drift: {want}")
    md = REC_MD.read_text(encoding="utf-8")
    if MOVER not in md or "DEMOTE_TO_WORKLIST" not in md or \
            PROJECTED_DEMOTE_ID not in md:
        die("A9: the record md does not pin the disposition set")
    ok("A9_round_artifacts",
       "record md + json pinned; the projected demoted re-key matches the "
       "c40 DEMOTE identity function recomputed live "
       f"({PROJECTED_DEMOTE_ID})")

    # ---- A7 idempotency -----------------------------------------------------------------
    h1 = sha16(OVERRIDES.read_bytes()), sha16(AMENDMENT.read_bytes())
    subprocess.run([sys.executable,
                    str(REPO / "scripts/c42_r36_override_projection.py")],
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
           f"R36 footprint (pre-commit form)")
    else:
        dirty = git(["status", "--porcelain"]).strip()
        if dirty:
            die(f"A10: post-commit tree is dirty: {dirty[:200]}")
        ok("A10_committed_clean",
           f"HEAD {head[:8]} is the round commit; tree clean; the check "
           f"re-runs committed-clean (the C8/X10 precedent)")

    # ---- report ---------------------------------------------------------------------------------
    out = {
        "schema": "c42-r36-repair-check/1.0",
        "task": "T-C42",
        "stage": "r36-operator-delegate-disposition-check",
        "round": "R36",
        "round_start": ROUND_START,
        "audited_head": head,
        "baseline_store_sha256_16": sha16(store_live),
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
    print(f"c42_r36_repair_check: {out['result']} ({len(CHECKS)}/{len(CHECKS)}) "
          f"-> {OUT.relative_to(REPO)}")
    return 0


def nsq_exists(p: Path, needle: str) -> bool:
    return needle in p.read_text(encoding="utf-8")


if __name__ == "__main__":
    sys.exit(main())
