#!/usr/bin/env python3
"""Three-way reconciliation for the YCH12 SB2 v2 LLM-polish landing (L-024 law).

Runs AFTER merge_llm_ych12.py on the workspace corpus, BEFORE any repo copy.
Exit non-zero unless ALL PASS. Checks (R = reconciliation):
  R1  every evidence-ok id: corpus text == repair text AND text_original == pristine text
  R2  every evidence-rejected/error id: corpus text == pristine text, no llm_repaired flag
  R3  text_original discipline: llm_repaired set == evidence-ok set (double-apply /
      clobber-replay detector — catches the R-013 failure mode: text_original != pristine)
  R4  untouched discipline: chunks without an ok repair byte-identical to pristine
      (no text_original key, same char_count, same text)
  R5  anchor drift: serving-critical fields identical to pristine (same keys as merge)
  R6  evidence ids all belong to the staged ids file; no orphan repairs

v2-lane convention (T-PARSE-YCH12-2): paths via env, same surface as
merge/audit/validate. Repo-resident since CONT-V2-5 (R-013's own action:
lane tooling must not live only in the sandbox workspace).
"""
import json, os, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

CORPUS = os.environ.get("YCH12_CORPUS", "/home/z/my-project/data/ych12_sb2/out/edexcel_ial_chemistry_ych12_sb2_chunks_v1.jsonl")
PRISTINE = os.environ.get("YCH12_PRISTINE", "/home/z/my-project/data/ych12_sb2/out/edexcel_ial_chemistry_ych12_sb2_chunks_v1.pristine")
REPAIRS = os.environ.get("YCH12_REPAIRS", "/home/z/my-project/data/ych12_sb2/llm_repairs_ych12.jsonl")
IDS = os.environ.get("YCH12_IDS", "/home/z/my-project/data/ych12_sb2/llm_repair_ids_ych12.json")
BASELINE = os.environ.get("YCH12_BASELINE", "")  # optional: pre-round landed corpus for net-new count

ANCHOR_KEYS = ("id", "unit_no", "chapter_no", "content_type",
               "pdf_pages", "book_pages", "section", "unit_name", "chapter_title")


def load(path):
    m = {}
    for line in open(path, encoding="utf-8"):
        if line.strip():
            c = json.loads(line)
            m[c["id"]] = c
    return m


corpus = load(CORPUS)
pristine = load(PRISTINE)
repairs = {}
for line in open(REPAIRS, encoding="utf-8"):
    if line.strip():
        r = json.loads(line)
        repairs[r["id"]] = r  # latest wins, same law as merge
staged = set(json.load(open(IDS, encoding="utf-8")))

ok_ids = {i for i, r in repairs.items() if r["status"] == "ok"}
fails = []


def fail(check, msg):
    fails.append((check, msg))


# R1 + R2 + R3 + R4 against the pristine snapshot
applied_now = 0
for cid, c in corpus.items():
    p = pristine.get(cid)
    if p is None:
        fail("R5", f"{cid}: missing from pristine")
        continue
    r = repairs.get(cid)
    if r and r["status"] == "ok":
        applied_now += 1
        if c.get("text") != r["text"]:
            fail("R1", f"{cid}: corpus text != repair text")
        if c.get("text_original") != p["text"]:
            fail("R3", f"{cid}: text_original != pristine (clobber/double-apply class)")
        if not c.get("llm_repaired"):
            fail("R3", f"{cid}: ok repair but llm_repaired flag missing")
    else:
        if c.get("llm_repaired"):
            fail("R2", f"{cid}: llm_repaired but no ok repair in evidence")
        if c.get("text") != p["text"]:
            fail("R4", f"{cid}: text changed without ok repair")
        if "text_original" in c:
            fail("R4", f"{cid}: text_original present without ok repair")
        if c.get("char_count") != len(p["text"]):
            fail("R4", f"{cid}: char_count drift on untouched chunk")
    for k in ANCHOR_KEYS:
        if c.get(k) != p.get(k):
            fail("R5", f"{cid}: anchor field {k} drifted")

# R6: evidence hygiene
orphans = set(repairs) - staged
if orphans:
    fail("R6", f"{len(orphans)} repair ids not in staged ids file (e.g. {sorted(orphans)[:3]})")
missing_corpus = {i for i in ok_ids if i not in corpus}
if missing_corpus:
    fail("R6", f"{len(missing_corpus)} ok ids absent from corpus (e.g. {sorted(missing_corpus)[:3]})")

# net-new vs the landed baseline (previous round's corpus), if provided
net_new = None
if BASELINE and os.path.exists(BASELINE):
    base = load(BASELINE)
    prev = {i for i, c in base.items() if c.get("llm_repaired")}
    net_new = len(ok_ids - prev)
    overlap = len(ok_ids & prev)
    print(f"net-new vs baseline: {net_new}  overlap (re-applied from pristine): {overlap}")

print(f"corpus: {len(corpus)}  pristine: {len(pristine)}  evidence: {len(repairs)} records, "
      f"{len(ok_ids)} ok / {len(repairs) - len(ok_ids)} rejected+error")
print(f"applied in corpus now: {applied_now}")

if fails:
    print(f"RECONCILIATION FAIL ({len(fails)}):")
    for check, msg in fails[:30]:
        print(f"  {check}  {msg}")
    sys.exit(1)
print("RECONCILIATION ALL PASS")
