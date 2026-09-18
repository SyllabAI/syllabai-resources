#!/usr/bin/env python3
"""
sme_spcpt_apply_to_map.py — merge AI_VALIDATED spcpt->4CH1 resolution records
(SME-ExamQuestion/<course>/spec_point_point_resolution.json) into the course's
spec_point_map.json mappings for ids that regime-A scoring left unmapped.

Provenance rules:
- Every merged entry carries: tier derived from the resolver's similarity
  (1.0 -> T1_verbatim, >=0.93 -> T2_near, else T4_fuzzy + review flag),
  the resolver's method verbatim, and a `resolution` sub-object with
  similarity / cross_check / source pointer.
- Adjudicated cases keep their adjudications-yaml reference.
- Merged ids are removed from `unmapped`; nothing is silently dropped.
- Idempotent: re-running after a merge is a no-op.
"""
import json, sys, datetime
from pathlib import Path

BASE = Path("/home/z/my-project/download/syllabai-resources")
COURSE = sys.argv[1] if len(sys.argv) > 1 else "igcse-chemistry-19"
EQ = BASE / "SME-ExamQuestion" / COURSE
MAP_F = EQ / "spec_point_map.json"
RES_F = EQ / "spec_point_resolution.json"
QUAL_PREFIX = "4CH1"
OFFICIAL_PREFIX = "IGCSE_CHEMISTRY"

now = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

mp = json.loads(MAP_F.read_text(encoding="utf-8"))
res = json.loads(RES_F.read_text(encoding="utf-8"))
res_by_id = {r["id"]: r for r in res["resolved"]}
mappings = mp.get("mappings", {})
unmapped = mp.get("unmapped", [])
flags = mp.get("flags", [])

unmapped_ids = {u["spcpt_id"] for u in unmapped}
already = [i for i in unmapped_ids if i in mappings]
if already:
    print("idempotency: already merged", len(already), "-> cleaning unmapped only")
to_merge = sorted(i for i in unmapped_ids if i not in mappings)
print(f"unmapped={len(unmapped_ids)} to_merge={len(to_merge)} mappings_before={len(mappings)}")

missing_res = [i for i in to_merge if i not in res_by_id]
if missing_res:
    print("FATAL: no resolution record for:", missing_res)
    sys.exit(1)

def tier_for(sim):
    if sim >= 1.0:
        return "T1_verbatim", None
    if sim >= 0.93:
        return "T2_near", None
    return "T4_fuzzy", ("resolver similarity %.4f below T2 threshold; confirmed by "
                        "sme_spcpt_resolve cross-check (code_in_note_codes); see "
                        "scripts/sme_spcpt_adjudications.yaml / VALIDATION.md" % sim)

merged, new_flags = [], []
for sid in to_merge:
    r = res_by_id[sid]
    code = r["resolved_code"]
    assert code.startswith(QUAL_PREFIX + "-"), (sid, code)
    oc = code.split("-", 1)[1]
    tier, flag_reason = tier_for(r["similarity"])
    method = r.get("method") or "definition_text_join"
    # normalize resolver method vocabulary to the map's (method semantics preserved)
    method = {"definition-match": "definition_text_join",
              "definition-match+note-codes": "definition_text_join+note_codes",
              "name-context": "adjudicated_context_join"}.get(method, method)
    entry = {
        "official_id": f"{OFFICIAL_PREFIX}:{oc}",
        "official_code": oc,
        "tier": tier,
        "score": round(r["similarity"], 4),
        "unit": None,
        "method": method,
        "resolution": {
            "source": "SME-ExamQuestion/%s/spec_point_resolution.json" % COURSE,
            "validation": res.get("validation"),
            "cross_check": r.get("cross_check"),
        },
    }
    mappings[sid] = entry
    merged.append((sid, code, tier, method, r["similarity"]))
    if flag_reason:
        flags.append({"spcpt_id": sid, "official_id": entry["official_id"],
                      "flag": flag_reason})

unmapped = [u for u in unmapped if u["spcpt_id"] not in mappings]

# ---- pass 2: resolution ids missing from the map entirely ----
# (e.g. empty-definition points regime-A never scored; adjudicated separately)
for sid in sorted(set(res_by_id) - set(mappings)):
    r = res_by_id[sid]
    code = r["resolved_code"]
    assert code.startswith(QUAL_PREFIX + "-"), (sid, code)
    oc = code.split("-", 1)[1]
    empty_def = not (r.get("sme_definition") or "").strip()
    if empty_def:
        tier, method = "T4_fuzzy", "adjudicated_context_join"
        flag_reason = ("SME provides no definition; resolved via page context + "
                       "note-code cross-check; adjudicated in "
                       "scripts/sme_spcpt_adjudications.yaml (empty-definition-"
                       "name-match)")
    else:
        tier, flag_reason = tier_for(r["similarity"])
        method = "definition_text_join"
    entry = {
        "official_id": f"{OFFICIAL_PREFIX}:{oc}",
        "official_code": oc,
        "tier": tier,
        "score": round(r["similarity"], 4),
        "unit": None,
        "method": method,
        "resolution": {
            "source": "SME-ExamQuestion/%s/spec_point_resolution.json" % COURSE,
            "validation": res.get("validation"),
            "cross_check": r.get("cross_check"),
        },
    }
    mappings[sid] = entry
    merged.append((sid, code, tier, method, r["similarity"]))
    if flag_reason:
        flags.append({"spcpt_id": sid, "official_id": entry["official_id"],
                      "flag": flag_reason})
    print(f"pass2 merged: {sid} -> {code} tier={tier} method={method}")

mp["mappings"] = mappings
mp["unmapped"] = unmapped
mp["flags"] = flags
mp["resolution_merge"] = {
    "merged_utc": now,
    "source_file": "SME-ExamQuestion/%s/spec_point_resolution.json" % COURSE,
    "source_schema": res.get("schema"),
    "source_validation": res.get("validation"),
    "merged_count": len(merged),
    "note": ("Regime-A (difflib) scoring left these ids unmapped as "
             "'merged/paraphrased beyond safe threshold'; the dedicated resolver "
             "(sme_spcpt_harvest -> sme_spcpt_resolve -> sme_spcpt_verify) resolved "
             "them with token-containment/F1 + subsection boost and note-code "
             "cross-check. Entries carry the resolver's evidence verbatim."),
}

MAP_F.write_text(json.dumps(mp, indent=1, ensure_ascii=False), encoding="utf-8")

# ---- self-verification ----
after = json.loads(MAP_F.read_text(encoding="utf-8"))
assert len(after["mappings"]) == len(mappings)
assert not ({u["spcpt_id"] for u in after["unmapped"]} & set(after["mappings"]))
idx = json.loads((EQ / "spec_point_index.json").read_text(encoding="utf-8"))
n_index = len(idx["spec_points"])
print(f"merged={len(merged)} mappings={len(after['mappings'])} (index={n_index}) "
      f"unmapped={len(after['unmapped'])} flags={len(after['flags'])}")
tiers = {}
for _, _, t, _, _ in merged:
    tiers[t] = tiers.get(t, 0) + 1
print("tier distribution of merged:", tiers)
for sid, code, t, m, s in merged:
    if t != "T1_verbatim":
        print(f"  non-T1: {sid} -> {code} tier={t} sim={s} method={m}")
assert len(after["mappings"]) == n_index, \
    "map covers %d of %d indexed SME spec points" % (len(after["mappings"]), n_index)
print("OK: map now covers all %d indexed SME spec points" % n_index)
