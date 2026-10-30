# AUDIT-2026-10-30-pua-mapping-pass-close — the PUA mapping pass: verification close

**Order:** "the PUA mapping pass" (the carried open item, F121 carry-overs) ·
verification-only wave — **zero corpus bytes, zero converter/exporter changes, zero
v2 contact** · branch `t-oeq-pua-close-1` · bases: resources main `e606043e8`
(the F121 merge, PR #232), v2 main `c5e8101f0`

## The order, resolved

The "PUA mapping pass" was carried as an open item since the wave-22-era AGENTS
list ("PUA mapping pass for any future series") and re-carried by the F121 wave.
Forensics at the current heads (verify-don't-trust) resolve it: **the pass was
ALREADY LANDED of record, and no residual PUA exists on any plane.** What remained
was the close: independent re-proof at the current cut + retiring the stale open
line so no future wave re-carries it.

### The of-record pass (already landed)

- **F48** (wave-14, 2026-10-22): the evidenced `PUA_MAP` normalization at text
  ingest — every mapping decided from a PDF font trace + page render, eyeballed,
  never guessed; **fail-closed: an unmapped PUA char ABORTS the run**
  (`normalize_pua` raises `ValueError` — a new symbol font must earn an evidenced
  entry, it must never silently leak into served content). LEDGER row F48;
  canary **C56** (corpus-wide PUA absence + eleven mapping pins).
- **F52** (2CR wave): the evidenced non-PUA confusable normalization U+01FB → Δ
  (MyriadPro-It italic-Delta artifact), applied before the PUA gate on both G2
  sides; canary **C65**.
- **Physics tranche** (F64/F66/F69 era, 2026-10-26): 4PH1 corpus PUA census +
  5 evidenced mappings; canary **C74** guards the tranche.
- **Maths-B tranches** (run-004 union + tranche-2 completion, 2026-10-25): the
  T-MIG-141 glyph-normalization table of record (sha256 1fdd4b4a) merged in —
  the map is declared **table.v1-complete** with the `_PUA_SEQ` sequence-first
  pre-pass. Final map size at the current cut: **128 evidenced entries**.

### The fresh evidence (this close, at `e606043e8` / v2 `c5e8101f0`)

| leg | result |
| --- | --- |
| Corpus census (independent, this wave) | **0 PUA** across all **714** text files under `Official-ExamQuestion/` at main (520 JSON + 192 MD + 2 scripts; the 1,316 skipped paths are **all PNGs** — benchmark receipts + crop assets; zero text files skipped) |
| Served hub census (this wave) | **0 PUA** in `official-papers.json` (4,246,344 B), `questions.json` (2,605,409 B), `manifest.json` at v2 main — the served surfaces are PUA-free of record |
| Canary battery (`check_canaries.py`, fresh) | **214/214 hold** — C56 (corpus-wide PUA-free + 11 mapping pins), C65 (U+01FB absence + ΔH pins), C74 (physics tranche guard), C78 (BEL) all PASS |
| Fail-closed negative test | **3/3 unmapped probes abort**: U+E0BC, U+F1FF, U+E123 → `ValueError: unmapped PUA char … add an evidenced PUA_MAP entry (font trace + page render) before running` |
| Mapping spot checks | **11/11**: F0B4→×, F0B8→÷, F044→Δ, F083→⇌, F0B0→°, F0FC→✓, F022→→, F0E5→Σ, F8E7→─, F097→•, F0AE→→ |
| Furniture drops | F0A2 (dotted answer-line rule) and F0C0 (cover pentagons) map to empty — removed, never leaked |
| F52 confusable | `ǻH` → `ΔH` (U+01FB → U+0394) |
| Sequence-first law | SEQ-A (F075 shaft run + F072 head) → one `→`; SEQ-B (F067 run) → one `→`; standalone F072 stays Δ |
| Fast path | PUA-free strings pass through **byte-identical**; chemistry lane state: `ACTIVE_PUA_OVERRIDES` empty, spec code `4ch1` |

Negative-test harness: `scripts/pua_negative_test.py` (zero network; imports the
converter of record at the current cut). Census artifacts: the wave's working
records `pua-pass/pua-census-corpus.json` + `pua-census-hub.json` (session-local;
the census is one `git cat-file` + scan of the pinned tree — re-derivable from
the heads of record).

## Standing decisions honored

- **No corpus bytes moved** — the corpus is already clean; there is nothing to patch.
- **No converter/exporter change** — F48/F52 + tranches stand as the mechanism of
  record; re-opening the map without a new evidenced glyph would be ceremony.
- **No v2 contact** — the served bundle is already PUA-free; no disclosure, no
  re-export, no hub sync (a byte-level no-op wave).
- The only of-record edits are documentation: the stale "Residual PUA mapping"
  open-work line retires to its CLOSED form (keeping the standing law for
  future series), plus this receipt.

## Verdict

**The PUA mapping pass item is CLOSED of record** — the pass landed as F48/F52 +
the physics/maths-B tranches (128 evidenced entries, table.v1-complete, fail-closed
abort on unmapped PUA); the corpus and the served hub carry ZERO PUA at the current
heads (independent census + 214/214 canaries + negative tests, this wave). The
standing law for any future series is unchanged: a new symbol-font glyph must earn
an evidenced `PUA_MAP` entry (font trace + page render) as a disclosed `notation`
edit under ADR-039; unmapped PUA refuses the run.
