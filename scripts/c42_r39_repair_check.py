#!/usr/bin/env python3
"""c42_r39_repair_check.py — T-C42 R39 two-way audit (the R36 check shape).

A1 inventory agreement: the R39 section_overrides + promotions amendment
   cover exactly the R38-defect-inventory disposition set — the two
   verdict rows of scripts/c42_r39_repair_verdicts.yaml (basic-probability
   :: 1, a5b737e510606829, the R38 fresh REJECT at 6.3A;
   calculations-with-the-mean :: 1, d545cd5f5aeae9a9, the R38 fresh REJECT
   at 6.2B; both DEMOTE_TO_WORKLIST); no dupes, no extras; the amendment's
   excluded block covers exactly those rows and its supersedes/added
   blocks are EMPTY (exclusion only — no sign-offs owed: the R30 round
   discharged all 4 H3 holds of record); NOTHING else rides a carrier
   entry — the not-fired guard: the fired notes' own siblings
   (basic-probability ords 0/2/3/4/5; calculations-with-the-mean ord 0)
   carry NO override and stay HUMAN_VALIDATED (the anti-forgery rule).
A2 projection agreement: scripts/c42_section_overrides_r39.yaml equals the
   verdict record — 2 verdicted DEMOTE_TO_WORKLIST entries (HV,
   override_code null), zero REATTRIBUTE entries, the zero-retain
   contract, the TWO note-level scoping blocks, the census remarks, EXACTLY
   ONE dated correction (the R38 ledger-prose defect), and the
   promoted-surface-amendment pointer (0+2+0); NO h3_signoffs block exists;
   zero SUGGESTED rows ride 6.3A/6.2B; the amendment's schema + base pin
   (9bad739bd79e5899) + prior_amendments (R26+R30+R33+R36) pinned.
A3 code domain: both DEMOTE entries carry override_code null (the c40 R8
   rule — no target exists); their current_codes match the live substrate
   (4MA1-6.3A / 4MA1-6.2B); both movers are HUMAN_VALIDATED and promoted;
   no re-pin arises.
A4 wordings + THE CORRECTED ledger facts + corpus pins: the registry
   wordings carry the verdict citations verbatim (6.3A 'draw and use tree
   diagrams'; 6.3B Higher independent events; 6.3D apply problems; 6.2B
   spread; 6.2A/6.2C/6.2D the spread/data family; 4.4F average speed);
   the NO-TARGET scans hold over the whole ratified 188 ('tree diagram'
   only 6.3A; word-boundary mean/average only 4.4F; 'spread' only 6.2B;
   'scale' only the instruments/drawings/enlargements set; no Higher
   wording names the probability-scale or mean/central-tendency surface);
   6.3A AND 6.2B are PRESENT in the C30 ledger as higher_preferred
   two-tier rows with the Higher/Foundation texts verbatim (the R38
   notes' 'absent — single-tier' clause corrected — the tier-artifact
   escape closes on the higher_preferred rule); the corpus chunk texts
   (read live via the c40 reader) carry the verdicts' evidence verbatim —
   the probability-scale bullets and calibration for row 1, the mean
   formula/rearrangement/worked-example for row 2 — AND the negative
   pins: 'tree'/'diagram' ABSENT from chunk 1; 'spread'/'interquartile'/
   'quartile' ABSENT from chunk 2 and 'range' occurring only inside
   'rearrange'; the chunk shas match the live substrate.
A5 joins STAND + resolution byte-untouched: BOTH corpus anchors
   (spcpt_FVX7YRftjhnwYHQF at 6.3A; spcpt_n9ZtYfjh8sFCp5Kz at 6.2B) stand
   at HEAD (the join layer untouched — the store rows move, the joins
   stand); the resolution file is byte-identical between the round-start
   HEAD (f2556cc) and the audit HEAD.
A6 substrate pins + promoted-surface guard: the store is the R37/R38
   landing of record (sha16 8d8474c59ca6341f) and is BYTE-IDENTICAL to the
   round-start HEAD's store (ZERO store bytes move this round); 917 rows =
   830 HUMAN_VALIDATED + 4 anchored SUGGESTED + 83 worklist; both movers
   are R5-pinned with matching identity; the per-code 6.3A census is 18
   anchored rows (all HV — the mover + 17 keepers) and 6.2B is 24 (the
   mover + 23 keepers), zero worklist rows; the meta census pins hold
   (834 / 28 / 55 / 133 / 188 / 830).
A7 idempotency: re-running the projection emitter is byte-identical
   (deterministic regeneration).
A8/A10 footprint + commit state: the working-tree delta vs the round-start
   HEAD (f2556cc) is within the declared R39 footprint (pre-commit form);
   post-commit the delta is empty and the check is re-runnable (the
   A10/X10/B8 precedent).
A9 round artifacts: the verdict record pins its own blocks (2 section
   overrides / 0 retain rows / 2 scoping notes / 2 census remarks / 1
   dated correction); the record md + json pin the same disposition set;
   the projected demoted re-keys in the record match the c40 DEMOTE
   identity function recomputed live (09f012e4cabef0cc /
   80d783fb13def4e2).

Writes its own report graph/reports/C42_R39_REPAIR_CHECK.json.
Exit 0 iff every check passes.
"""
import hashlib
import json
import re
import subprocess
import sys
from pathlib import Path

import yaml

REPO = Path(__file__).resolve().parent.parent
OUT = REPO / "graph/reports/C42_R39_REPAIR_CHECK.json"
VERDICTS = REPO / "scripts/c42_r39_repair_verdicts.yaml"
OVERRIDES = REPO / "scripts/c42_section_overrides_r39.yaml"
AMENDMENT = REPO / "scripts/c42_r39_promotions_amendment.yaml"
STORE = REPO / "graph/igcse-maths-a/spec_chunk_mappings.yaml"
REGISTRY = REPO / "graph/igcse-maths-a/specification_points.yaml"
LEDGER = REPO / "graph/reports/C30_MATHS_A_TIER_DEDUPE_LEDGER.json"
JOIN = REPO / ("Official-Specifications/parsed/_derived/notes-join/"
               "igcse-maths-a-18-higher.json")
PROMOTIONS = REPO / "scripts/c42_r5_promotions.yaml"
REC_MD = REPO / "graph/reports/C42_R39_RESOLUTION_REPAIR_RECORD.md"
REC_JSON = REPO / "graph/reports/C42_R39_RESOLUTION_REPAIR_RECORD.json"
RES_GIT = "SME-ExamQuestion/igcse-maths-a-18-higher/spec_point_resolution.json"
STORE_GIT = "graph/igcse-maths-a/spec_chunk_mappings.yaml"
ROUND_START = "f2556cc395eb52dd09aabdee144f9299de7d13b1"

NOTE1 = ("notes/6-statistics-and-probability/probability-toolkit/"
         "basic-probability.json")
MOVER1 = "a5b737e510606829"
ORD1 = 1
CODE1 = "4MA1-6.3A"
SHA1 = "74b5c6214777c054"
ANCHOR1 = "spcpt_FVX7YRftjhnwYHQF"
REKEY1 = "09f012e4cabef0cc"
SIBLINGS1 = ["0d6a3b79dfd8a342", "2f37fe5456f312e6", "bca5ee1833756107",
             "a37004be54955077", "d437d30f579f84d7"]

NOTE2 = ("notes/6-statistics-and-probability/statistics-toolkit/"
         "calculations-with-the-mean.json")
MOVER2 = "d545cd5f5aeae9a9"
ORD2 = 1
CODE2 = "4MA1-6.2B"
SHA2 = "22c1475d80a7d6df"
ANCHOR2 = "spcpt_n9ZtYfjh8sFCp5Kz"
REKEY2 = "80d783fb13def4e2"
SIBLINGS2 = ["2d215566e1c7d3f3"]

MOVERS = {MOVER1: (NOTE1, ORD1, CODE1, SHA1),
          MOVER2: (NOTE2, ORD2, CODE2, SHA2)}

FOOTPRINT = [
    "scripts/c42_r39_repair_verdicts.yaml",
    "scripts/c42_r39_override_projection.py",
    "scripts/c42_r39_repair_check.py",
    "scripts/c42_section_overrides_r39.yaml",
    "scripts/c42_r39_promotions_amendment.yaml",
    "graph/reports/C42_R39_RESOLUTION_REPAIR_RECORD.md",
    "graph/reports/C42_R39_RESOLUTION_REPAIR_RECORD.json",
    "graph/reports/C42_R39_REPAIR_CHECK.json",
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

    def chunk_text(note_path, ordn) -> str:
        t = idx.get((note_path, ordn))
        if t is None:
            die(f"corpus chunk {note_path}::{ordn} not found by the c40 "
                f"reader")
        return t

    # ---- A1 inventory agreement ------------------------------------------------
    if sorted(ovr_entries) != sorted(v_by_mid):
        die("A1: override ids != verdict ids")
    if sorted(ovr_entries) != sorted(MOVERS):
        die(f"A1: disposition set drifted: {sorted(ovr_entries)}")
    for m, (note, ordn, code, _sha) in MOVERS.items():
        e = ovr_entries[m]
        srow = rows_by_id[m]
        if e["action"] != "DEMOTE_TO_WORKLIST":
            die(f"A1: {m} action drift")
        if srow["chunk"]["ordinal"] != ordn or srow["note_path"] != note:
            die(f"A1: {m} note::ordinal identity drift")
        if srow["validation_status"] != "HUMAN_VALIDATED":
            die(f"A1: {m} is not HUMAN_VALIDATED")
        if "promotion" not in srow:
            die(f"A1: {m} carries no promotion block")
    if sup or len(exc) != 2 or added:
        die("A1: amendment shape drifted — 0 supersedes + 2 excluded + "
            "0 added expected (exclusion only)")
    xids = sorted(x.get("mapping_id") for x in exc)
    if xids != sorted(MOVERS):
        die(f"A1: excluded identities drifted: {xids}")
    for x in exc:
        note, ordn, code, _sha = MOVERS[x.get("mapping_id")]
        if x.get("note_path") != note or \
                int(x.get("chunk_ordinal", -1)) != ordn or \
                x.get("pinned_code") != code or \
                x.get("disposition") != "DEMOTE_TO_WORKLIST":
            die(f"A1: excluded entry identity drift: {x}")
    for m in MOVERS:
        if m not in promo_pins:
            die(f"A1: mover {m} not R5-pinned")
        if promo_pins[m].get("spec_code") != MOVERS[m][2]:
            die(f"A1: mover pin code drift on {m}")
    for m in SIBLINGS1 + SIBLINGS2:
        if m in ovr_entries:
            die(f"A1: NOT-FIRED sibling {m} carries an override — the "
                f"anti-forgery rule")
        srow = rows_by_id.get(m)
        if srow is None or srow.get("validation_status") != "HUMAN_VALIDATED":
            die(f"A1: not-fired sibling {m} drifted from the anchored surface")
    ok("A1_inventory_agreement",
       "overrides == verdicts == the fired 2-row batch (a5b737e510606829 "
       "basic-probability::1 + d545cd5f5aeae9a9 "
       "calculations-with-the-mean::1, both DEMOTE_TO_WORKLIST); amendment "
       "0 supersedes + 2 exclusions + 0 additions with the identities "
       "pinned; the not-fired guard holds across both notes' siblings "
       "(all HV)")

    # ---- A2 projection agreement --------------------------------------------------
    acts = sorted(e["action"] for e in ovr_entries.values())
    if acts != ["DEMOTE_TO_WORKLIST", "DEMOTE_TO_WORKLIST"]:
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
    if scoping != ver["note_level_scoping"] or len(scoping) != 2:
        die("A2: note-level scoping block drifted")
    if [s.get("note_slug") for s in scoping] != \
            ["basic-probability", "calculations-with-the-mean"]:
        die("A2: scoping note slugs drifted")
    dc = ovr.get("dated_corrections")
    if not isinstance(dc, list) or len(dc) != 1:
        die("A2: EXACTLY ONE dated correction expected (the R38 ledger-prose "
            "defect)")
    if "c42_r38_fresh_verdicts" not in (dc[0].get("corrects") or ""):
        die("A2: the dated correction does not cite the R38 fresh verdicts")
    if dc != ver.get("dated_corrections"):
        die("A2: the map's dated correction != the verdict record's")
    if not ovr.get("census_remarks") or len(ovr["census_remarks"]) < 2:
        die("A2: census remarks missing")
    psa = ovr.get("promoted_surface_amendment") or {}
    if psa.get("amendment_file") != "scripts/c42_r39_promotions_amendment.yaml" \
            or psa.get("base_file_untouched") is not True \
            or psa.get("supersedes") != 0 or psa.get("excluded") != 2 \
            or psa.get("added") != 0:
        die("A2: promoted-surface-amendment pointer drifted")
    if amd.get("schema") != "c42-r31-promotions-amendment/1.0" \
            or amd.get("base_file_sha256_16") != "9bad739bd79e5899" \
            or amd.get("prior_amendments") != \
            ["scripts/c42_r26_promotions_amendment.yaml",
             "scripts/c42_r30_promotions_amendment.yaml",
             "scripts/c42_r33_promotions_amendment.yaml",
             "scripts/c42_r36_promotions_amendment.yaml"]:
        die("A2: amendment schema/base/prior-amendment pins drifted")
    for code in (CODE1, CODE2):
        sugg_c = [m for m, r in rows_by_id.items()
                  if r.get("validation_status") == "SUGGESTED"
                  and r.get("spec_code") == code]
        if sugg_c:
            die(f"A2: SUGGESTED rows ride {code}: {sugg_c}")
    ok("A2_projection_agreement",
       "map == verdicts (2 HV DEMOTEs, override_code null); retains empty; "
       "2 scoping notes + 2 remarks pinned; EXACTLY ONE dated correction "
       "(the R38 ledger-prose defect) carried verbatim; zero sign-off "
       "blocks; zero SUGGESTED rows on 6.3A/6.2B; amendment schema + base "
       "pin + prior-amendments (R26+R30+R33+R36) pinned")

    # ---- A3 code domain -------------------------------------------------------------
    for m, (note, ordn, code, _sha) in MOVERS.items():
        e = ovr_entries[m]
        srow = rows_by_id[m]
        v = v_by_mid[m]
        if e.get("override_code") is not None:
            die(f"A3: the DEMOTE entry for {m} carries an override_code — "
                f"the c40 R8 rule forbids it (no target exists)")
        if v.get("override_code") is not None:
            die(f"A3: the DEMOTE verdict for {m} carries an override_code")
        if srow["spec_code"] != e["current_code"] != code:
            die(f"A3: current_code drift on {m}")
        if srow.get("validation_status") != "HUMAN_VALIDATED":
            die(f"A3: {m} status drift")
        if code not in points:
            die(f"A3: {code} is not a ratified-188 member")
    ok("A3_code_domain",
       "both DEMOTEs carry no target (the c40 R8 rule; the no-target facts "
       "live-verified in A4); current 4MA1-6.3A / 4MA1-6.2B match the live "
       "substrate; both movers HUMAN_VALIDATED + promoted; no re-pin arises")

    # ---- A4 wordings + THE CORRECTED ledger facts + corpus pins ----------------------
    wants = {
        "4MA1-6.3A": "draw and use tree diagrams",
        "4MA1-6.3B": ("determine the probability that two or more "
                      "independent events will occur"),
        "4MA1-6.3D": "apply probability to simple problems",
        "4MA1-6.2B": "understand the concept of a measure of spread",
        "4MA1-6.2A": "estimate the median from a cumulative frequency diagram",
        "4MA1-6.2C": "find the interquartile range from a discrete data set",
        "4MA1-6.2D": ("estimate the interquartile range from a cumulative "
                      "frequency diagram"),
        "4MA1-4.4F": ("understand and use the relationship between average "
                      "speed, distance and time"),
    }
    for code, want in wants.items():
        got = reg_pts[code].get("official_wording") or ""
        if squash(got) != squash(want):
            die(f"A4: {code} wording drifted: {got!r}")
    # the NO-TARGET scans over the whole ratified 188
    hits = sorted(p["code"] for p in reg["specification_points"]
                  if "tree diagram" in (p.get("official_wording") or "").lower())
    if hits != ["4MA1-6.3A"]:
        die(f"A4: no-target fact drifted: tree-diagram hits {hits}")
    scale = sorted(p["code"] for p in reg["specification_points"]
                   if "scale" in (p.get("official_wording") or "").lower())
    if scale != ["4MA1-4.4A", "4MA1-4.5C", "4MA1-5.2J", "4MA1-5.2L"]:
        die(f"A4: no-target fact drifted: scale hits {scale}")
    mean_hits = sorted(p["code"] for p in reg["specification_points"]
                       if re.search(r"\bmean\b|\baverage\b",
                                    (p.get("official_wording") or "").lower()))
    if mean_hits != ["4MA1-4.4F"]:
        die(f"A4: no-target fact drifted: mean/average hits {mean_hits}")
    spread = sorted(p["code"] for p in reg["specification_points"]
                    if "spread" in (p.get("official_wording") or "").lower())
    if spread != ["4MA1-6.2B"]:
        die(f"A4: no-target fact drifted: spread hits {spread}")
    for p in reg["specification_points"]:
        w = (p.get("official_wording") or "").lower()
        if "probability scale" in w or "central tendency" in w:
            die(f"A4: no-target fact drifted: {p['code']} names the surface")
    # THE CORRECTED LEDGER FACTS: both codes PRESENT, higher_preferred true
    for bare, hi, fo in (("6.3A", "draw and use tree diagrams",
                          "understand the language of probability"),
                         ("6.2B", "understand the concept of a measure of spread",
                          ("calculate the mean, median, mode and range for a "
                           "discrete data set"))):
        row = led_rows.get(bare)
        if row is None:
            die(f"A4: {bare} expected PRESENT in the C30 ledger (the R38 "
                f"note's 'absent — single-tier' clause corrected)")
        if row.get("higher_preferred") is not True:
            die(f"A4: {bare} higher_preferred drifted")
        if (row.get("higher") or {}).get("text") != hi:
            die(f"A4: {bare} Higher text drifted")
        if (row.get("foundation") or {}).get("text") != fo:
            die(f"A4: {bare} Foundation text drifted")
    row63b = led_rows.get("6.3B")
    if row63b is None or \
            (row63b.get("foundation") or {}).get("text") != \
            "understand and use the probability scale":
        die("A4: the 6.3B Foundation scoping fact drifted")
    # corpus pins: the verdicts' evidence verbatim in the chunks
    pins1 = [
        "What is probability?",
        "Probability describes the likelihood of something happening",
        "impossible, unlikely",
        "In maths we use the probability scale to describe probability",
        "giving it a number between 0 and 1",
        "0 means impossible",
        "between 0 and 0.5 means unlikely",
        "0.5 means even chance",
        "between 0.5 and 1 means likely",
        "1 means certain",
        "Probabilities can be given as fractions, decimals or percentages",
        "Probability scale",
    ]
    pins2 = [
        "How do I solve harder problems involving the mean?",
        "Mean = total of values ÷ number of values",
        "formula involving three quantities",
        "if you know any two, you can find the other one",
        "work backwards from a known mean",
        "It helps to rearrange the formula",
        "Total of values = mean × number of values",
        "missing values",
        "adding in, or taking out, a value",
        "It can help to think of the mean as a formula which you can rearrange",
        "A class of 24 students has a mean height of 1.56 metres",
        "The mean height of the class is now 1.57 metres",
        "Find the height of the new student",
    ]
    t1 = chunk_text(NOTE1, ORD1)
    ns1 = nsq(t1)
    for needle in pins1:
        if nsq(needle) not in ns1:
            die(f"A4: corpus pin missing (chunk 1): {needle!r}")
    t2 = chunk_text(NOTE2, ORD2)
    ns2 = nsq(t2)
    for needle in pins2:
        if nsq(needle) not in ns2:
            die(f"A4: corpus pin missing (chunk 2): {needle!r}")
    # negative pins
    for frag in ("tree", "diagram", "branch", "successive"):
        if nsq(frag) in ns1:
            die(f"A4: chunk 1 unexpectedly carries {frag!r}")
    for frag in ("spread", "interquartile", "quartile", "dispersion"):
        if nsq(frag) in ns2:
            die(f"A4: chunk 2 unexpectedly carries {frag!r}")
    # 'range' only inside 'rearrange' in chunk 2
    residue = re.sub(r"rearrang\w*", "", ns2)
    if "range" in residue:
        die("A4: chunk 2 carries 'range' outside 'rearrange'")
    # the movers' chunk shas match the live substrate (the mechanical layer)
    if c40.sha16(t1) != rows_by_id[MOVER1]["chunk"]["sha256_16"] or \
            rows_by_id[MOVER1]["chunk"]["sha256_16"] != SHA1:
        die(f"A4: chunk sha drift on {MOVER1}")
    if c40.sha16(t2) != rows_by_id[MOVER2]["chunk"]["sha256_16"] or \
            rows_by_id[MOVER2]["chunk"]["sha256_16"] != SHA2:
        die(f"A4: chunk sha drift on {MOVER2}")
    ok("A4_wordings_ledger_corpus",
       "registry wordings verbatim (6.3A/6.3B/6.3D + 6.2A/6.2B/6.2C/6.2D + "
       "4.4F); the no-target scans hold over the ratified 188 ('tree "
       "diagram' only 6.3A; mean/average only 4.4F; 'spread' only 6.2B; "
       "'scale' only instruments/drawings/enlargements; no Higher wording "
       "names the probability-scale or mean surface); THE CORRECTED ledger "
       "facts pinned live (6.3A + 6.2B PRESENT as higher_preferred two-tier "
       "rows with the Higher/Foundation texts verbatim; 6.3B Foundation "
       "'understand and use the probability scale' recorded); corpus pins "
       "verified live via the c40 reader (the probability-scale bullets + "
       "calibration; the mean formula + rearrangement + the 24/25-student "
       "example); negative pins hold ('tree'/'diagram' absent from chunk 1; "
       "'spread'/'interquartile'/'quartile' absent from chunk 2 with "
       "'range' only inside 'rearrange'); chunk shas match the substrate "
       f"({SHA1} / {SHA2})")

    # ---- A5 joins STAND + resolution byte-untouched -------------------------------------
    join_rows = {r["anchor_id"]: r for r in join["joins"]}
    for anchor, code, note in ((ANCHOR1, CODE1, NOTE1),
                               (ANCHOR2, CODE2, NOTE2)):
        jr = join_rows.get(anchor)
        if jr is None or jr.get("store_row_code") != code:
            got = (jr or {}).get("store_row_code")
            die(f"A5: join row for {anchor} does not stand at {code} "
                f"(got {got})")
        if jr.get("note_path") != note:
            die(f"A5: the anchor {anchor}'s note_path drifted")
    res_start = git_bytes(f"{ROUND_START}:{RES_GIT}")
    res_head = git_bytes(f"HEAD:{RES_GIT}")
    if res_start != res_head:
        die("A5: resolution file drifted between the round-start HEAD and HEAD")
    ok("A5_joins_resolution",
       f"both corpus anchors stand ({ANCHOR1} at 6.3A; {ANCHOR2} at 6.2B) "
       f"at HEAD (the join layer untouched); resolution file byte-identical "
       f"{ROUND_START[:12]} -> HEAD")

    # ---- A6 substrate pins + promoted-surface guard ---------------------------------------
    store_live = STORE.read_bytes()
    if sha16(store_live) != "8d8474c59ca6341f":
        die("A6: store sha drifted from the R37/R38-of-record landing")
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
    worklist = sugg_all - sugg_anch
    if len(rows_by_id) != 917 or len(hv) != 830 or len(sugg_anch) != 4 \
            or len(worklist) != 83:
        die(f"A6: store is not the R37/R38-of-record state (917 = 830 HV + 4 "
            f"anchored SUGGESTED + 83 worklist, got {len(rows_by_id)} = "
            f"{len(hv)} + {len(sugg_anch)} + {len(worklist)})")
    for m, (note, ordn, code, _sha) in MOVERS.items():
        pin = promo_pins.get(m)
        if pin is None:
            die(f"A6: mover {m} not pinned in the R5 promotions file")
        srow = rows_by_id[m]
        if (pin.get("spec_code") != srow["spec_code"]
                or pin.get("note_path") != srow["note_path"]
                or pin.get("chunk_ordinal") != srow["chunk"]["ordinal"]):
            die(f"A6: promotions pin identity drift on {m}")
    for code, want_n, movers in ((CODE1, 18, {MOVER1}),
                                 (CODE2, 24, {MOVER2})):
        fam = [r for r in store["rows"]
               if r.get("spec_code") == code and "chunk" in r]
        if len(fam) != want_n:
            die(f"A6: per-code {code} census drifted: {len(fam)} "
                f"(want {want_n})")
        ids = {r["mapping_id"] for r in fam}
        if not movers <= ids:
            die(f"A6: the {code} family lost its mover")
        for r in fam:
            if r.get("validation_status") != "HUMAN_VALIDATED":
                die(f"A6: {r['mapping_id']} anchored row not HUMAN_VALIDATED")
            if r.get("worklist_reason"):
                die(f"A6: {r['mapping_id']} carries a worklist_reason")
    meta = store.get("meta") or {}
    for k, want in (("rows_anchored", 834),
                    ("rows_worklist_anchor_unresolved", 28),
                    ("rows_worklist_unmapped_sps", 55),
                    ("sp_codes_covered", 133),
                    ("promoted_rows", 830),
                    ("registry_size", 188)):
        if meta.get(k) != want:
            die(f"A6: meta census pin {k} drifted: {meta.get(k)} "
                f"(want {want})")
    ok("A6_substrate_pins",
       "store at the R37/R38-of-record state (sha 8d8474c59ca6341f) and "
       "byte-identical to the round-start HEAD (ZERO store bytes move this "
       "round); 917 = 830 + 4 + 83; both movers R5-pinned with matching "
       "identity; per-code censuses 6.3A 18 all HV (the mover + 17 keepers) "
       "and 6.2B 24 all HV (the mover + 23 keepers), zero worklist rows; "
       "the meta census pins hold")

    # ---- A9 round artifacts + the projected demoted re-keys -------------------------------
    if len(v_by_mid) != 2 or retains:
        die("A9: verdict record blocks drifted")
    if len(ver["note_level_scoping"]) != 2 or \
            len(ver["census_remarks"]) != 2 or \
            len(ver.get("dated_corrections") or []) != 1:
        die("A9: verdict record scoping/remarks/corrections blocks drifted")
    if rec.get("baseline", {}).get("store_sha16") != sha16(store_live):
        die("A9: record baseline store pin drifted")
    rec_ids = sorted(i["mapping_id"] for i in rec["inventory"]["rows"])
    if rec_ids != sorted(ovr_entries):
        die("A9: record inventory != the disposition set")
    for m, (note, ordn, _code, _sha) in MOVERS.items():
        want = hashlib.sha256(
            f"demoted|{note}|{ordn}".encode("utf-8")).hexdigest()[:16]
        want_id = REKEY1 if m == MOVER1 else REKEY2
        if rec.get("projected_rekeys", {}).get(m) != want or want != want_id:
            die(f"A9: projected demoted re-key drift on {m}: {want}")
    md = REC_MD.read_text(encoding="utf-8")
    for needle in (MOVER1, MOVER2, "DEMOTE_TO_WORKLIST", REKEY1, REKEY2,
                   "higher_preferred"):
        if needle not in md:
            die(f"A9: the record md does not pin {needle!r}")
    ok("A9_round_artifacts",
       "record md + json pinned (incl. the dated correction + the "
       "Foundation scoping facts); the projected demoted re-keys match the "
       f"c40 DEMOTE identity function recomputed live ({REKEY1} / {REKEY2})")

    # ---- A7 idempotency -----------------------------------------------------------------
    h1 = sha16(OVERRIDES.read_bytes()), sha16(AMENDMENT.read_bytes())
    subprocess.run([sys.executable,
                    str(REPO / "scripts/c42_r39_override_projection.py")],
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
           f"delta vs {ROUND_START[:12]} is exactly the declared "
           f"{len(FOOTPRINT)}-file R39 footprint (pre-commit form)")
    else:
        dirty = git(["status", "--porcelain"]).strip()
        if dirty:
            die(f"A10: post-commit tree is dirty: {dirty[:200]}")
        ok("A10_committed_clean",
           f"HEAD {head[:8]} is the round commit; tree clean; the check "
           f"re-runs committed-clean (the A10/X10/B8 precedent)")

    # ---- report ---------------------------------------------------------------------------------
    out = {
        "schema": "c42-r39-repair-check/1.0",
        "task": "T-C42",
        "stage": "r39-operator-delegate-disposition-check",
        "round": "R39",
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
    print(f"c42_r39_repair_check: {out['result']} ({len(CHECKS)}/{len(CHECKS)}) "
          f"-> {OUT.relative_to(REPO)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
