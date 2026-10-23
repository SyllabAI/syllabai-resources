# Student Book OCR Runbook — Unlimited-OCR (baidu/Unlimited-OCR)

Decision record + execution guide for converting the 383-page image-only
Student Book PDF (`edexcel-international-gcse-9-1-chemistry-student-book-pdf-free.pdf`)
to CMC-shaped Markdown. This replaces ocr.z.ai for this book (too large for
the service).

## 1. Pilot verdict — STRONG YES (5 pages, 2026-09-10)

Tested via the official Hugging Face demo Space (ZeroGPU A10G, `base` mode,
200 DPI). Evidence in `student-book-pilot/`:

| Book page | Content stress | Result |
|---|---|---|
| 51 | titration masses table, empirical formula | HTML table perfect, `\( H_2O \)` subscript correct |
| 74 | full display equations + state symbols | `\[ 2 \mathrm{H}_{2}\mathrm{O}_{2} (\mathrm{aq}) \rightarrow ... \]` — states preserved |
| 75 | learning objectives = spec 1.38 ion list | `Cu \( ^{2+} \)`, `\( CO_{3}^{2-} \)`, `\( (NH_{4})_{2}SO_{4} \)` — charge+subscript both correct |
| 76 | key-point boxes, figure captions | structure + reading order clean |
| 78 | dot-and-cross diagrams, lattice text | `Li \( ^{+} \)`, `\(\mathrm{CaCl}_2\)` correct |

**Side-by-side vs ocr.z.ai (same content, the spec conversion):**
- ocr.z.ai: `CO32-` / `Ag+，Cu2+` / CJK punctuation leaks
- Unlimited-OCR: `\( CO_{3}^{2-} \)` / `Cu \( ^{2+} \)`

**Known residual damage (lint-owned, not hand-fixed):**
- state symbol `(l)` sometimes read as `()` or `(1)` — deterministic regex check
- occasional `Aᵣ` → `A,` (subscript r lost) — check against spec symbols
- figure bodies NOT extracted (placeholders `![](images/N.jpg)` in order) —
  extraction happens at ingest from page PNGs / raw `<|det|>` bbox sidecar
- headings/headers/footers inline (book page number, unit banner lines) —
  strip at ingest

## 2. Execution paths

### Path A (RECOMMENDED for the full 383 pages): rented GPU + official vLLM image

Any host with Docker + an NVIDIA GPU ≥ 16 GB (A10G / L4 / A100 / 4090).
Rent by the hour (vast.ai / runpod / lambda); estimated **30–60 min of GPU
time at concurrency 4–8** — a few dollars total.

```bash
# on the rented GPU host
docker run --rm --gpus all --network host --ipc host \
  vllm/vllm-openai:unlimited-ocr \
  baidu/Unlimited-OCR \
  --trust-remote-code \
  --logits_processors vllm.model_executor.models.unlimited_ocr:NGramPerReqLogitsProcessor \
  --no-enable-prefix-caching \
  --mm-processor-cache-gb 0
# server listens on :8000

# from this repo (CPU side — can be your laptop)
python3 scripts/c05_book_ocr.py \
  --backend vllm --base-url http://<gpu-host>:8000/v1 \
  --range 1-383 --concurrency 8 \
  --pdf edexcel-international-gcse-9-1-chemistry-student-book-pdf-free.pdf \
  --out student-book
```

Interrupted? Re-run the same command — `manifest.json` is the checkpoint,
done pages are skipped, failed pages retried.

### Path B: Hugging Face demo Space (pilots / small batches only)

```bash
python3 scripts/c05_book_ocr.py --backend space --range 83-90 --out student-book
```

**Empirically confirmed limit (2026-09-10):** anonymous ZeroGPU quota ran out
after ~8 single-page calls. With a logged-in HF token it rises somewhat; HF
PRO (~$9/mo) more. Fine for sampling, NOT for 383 pages in one go.

### Path C: your own GPU (≥ 12–16 GB VRAM)

Transformers route per the repo README (bf16). Slowest per-page but free if
you already have the card; `c05_book_ocr.py --backend space` shape can be
re-pointed, or use the repo's own `infer.py`.

## 3. Output shape (CMC v1.0)

```
student-book/
  manifest.json          page -> {book_page, chapter, status, sha256, chars}
  pages/page-NNN.md      CMC front matter (source_type: textbook, pdf/book
                         page, unit, chapter, ocr tool/date, status: raw_ocr)
                         + body (LaTeX notation, HTML tables, figure
                         placeholders)
  raw/page-NNN.raw.txt   vllm only: raw model output WITH <|det|> bboxes —
                         the figure-extraction source
  pages-assets/*.png     200 DPI page renders — figure crop source
```

- `book_page = pdf_page − 9` (verified on this scan; `--offset` to override)
- Chapter map (29 chapters, 4 units) is built into the script and stamped per
  page; chapter-level file assembly happens at ingest (T-C06), so page-map
  corrections never require re-OCR
- Do **not** hand-fix the `(l)`/`A,` damage — the ingestion lint flags it for
  review with page provenance intact

## 4. Ingest implications (registered for T-C06)

1. LaTeX → HTML `<sub>/<sup>` normalization is a deterministic transform
   (KaTeX-style scanner), not AI interpretation — safe for the converter
2. Figure extraction: crop page PNGs by `<|det|>` image bboxes from
   `raw/*.raw.txt`, name `fig-<book-page>-<seq>.png`, replace placeholders
3. The 192-page 2-up PDF is now redundant — keep only as a text-layer
   cross-check

## 5. Path D (EXECUTED 2026-10-24): publisher text-layer extraction

No GPU available in the ops sandbox, so the full book is now machine-readable
via the 2-up PDF's embedded text layer (the "redundant" cross-check PDF):

```bash
python3 scripts/c05_book_textlayer.py            # -> student-book-textlayer/
python3 scripts/c06_ingest_book.py --selftest    # 12/12 fixture assertions
python3 scripts/c06_ingest_book.py \
  --src student-book-textlayer/pages \
  --out student-book-ingest                      # chapter assembly + report
```

Result (2026-10-24): 378/378 text slots extracted (868 KB), 5 genuinely
image-only slots (2-up spreads 7 and 82 = book pages 4-5 and 154-155 —
verified image-only in the publisher layer itself, OCR-owned), 30 chapter
files assembled, double-run byte-identical. Page keys match the c05 output
keying (1-up pdf page numbers) so the Unlimited-OCR run supersedes the text
layer page-for-page via `c06_ingest_book.py --src student-book/pages
--fallback student-book-textlayer/pages` when it lands.

Honest status: `text_layer` everywhere — the publisher layer has NO LaTeX
(unicode sub/sup only, normalized to HTML by the ingest), figure-caption
ghosting and glyph garbage (`PIHi&`-class) flagged by the ingest lint
(146 digit/letter + 9 garbled + 40 Aᵣ-suspect findings recorded, NOT
hand-fixed). OCR-path validated separately against the 5 committed pilot
pages re-wrapped as `student-book-pilot/pages/` (fixture builder:
`scripts/c06_pilot_pages_fixture.py`): 53 inline + 8 display math
converted, state-symbol and Aᵣ damage flagged exactly per §1.

Path B quota note (2026-10-24): anonymous ZeroGPU quota observed exhausted
("90s requested vs. 0s left") — full-book OCR still requires Path A (rented
GPU) or an HF token with fresh quota. `c05_book_ocr.py` manifest checkpoint
is in place; re-run the same command to resume.
