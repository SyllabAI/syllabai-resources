# Cambridge IGCSE Chemistry (0620) — Student Book Intake (2026-10-21)

**Status:** SOURCE (wave-2 retry, T-MIG-141 run-002) — parse lane NOT started.
Scaffold per `books/README.md` §5 (copy of `physics/4ph1/`).

## Book of this lane

### Cambridge IGCSE Chemistry Coursebook, Fourth edition (with CD-ROM variant scan)

- **Title:** Cambridge IGCSE Chemistry Coursebook, Fourth edition
- **Authors:** Richard Harwood, Ian Lodge
- **Publisher / year:** Cambridge University Press, 2014 (endorsed by Cambridge International Examinations; supports 0620 for first examination 2016)
- **ISBN:** print 978-1107615028; this scan's family = 978-1107615038 (the "with CD-ROM" variant of the same 4th edition)
- **Identity proof:** OCR of the cover ("ENDORSED BY CAMBRIDGE … Harwood and Ian Lodge … Cambridge IGCSE® Chemistry Coursebook") + contents-page OCR (ch.10 Organic chemistry section listing)
- **File:** `source/student-book.pdf`
- **Pages:** 362 (full copy; matches the 4th edition's bibliographic count and the dokumen.pub 360 [362] metadata for the same scan)
- **Bytes:** 74,425,338
- **sha256:** `7a499f6cfdf8f4ebbe5c6026e03edbb4b6e0d297a5996f058f76ea2bf810d1b8`
- **Quality:** image-only (Mac OS X Quartz PDFContext re-render; zero real text layer — every page carries only an "RM.DL.BOOKS GROUPS" watermark string as text) → OCR route required. DISCLOSED DEFECT: the per-page "RM.DL.BOOKS GROUPS" third-party watermark is present on scanned pages (same class as the 9701 ad-watermark defect; the parse lane must strip it from the text bank and the page images carry it only as a text object, not burned into the images).
- **Provenance:** Library Genesis mirror `libgen.vg` `/ads.php?md5=8afe8a392719b858943d34732c54906f` → `/get.php?…` (single-session key; the 88 MB sibling md5 `adff421806dfa20c26e6013f31c4f844` rate-limited at 80.7/~88 MB and was abandoned — local partial only, not committed)

## Sourcing history of this lane (2026-10-21 retry)

| Attempt | Source | Result |
|---|---|---|
| 1 | papacambridge CDN direct URL (`ebooks.papacambridge.com/…/cambridge igcse chemistry coursebook (fourth edition) - public - 20 .pdf`, 32,310,654 B) | **REJECTED — 69 pp preview** (p1 even leaks "Cambers & Sibley: IGCSE Physics" print markup); re-proves the wave-1 papacambridge preview finding for their CDN URL class |
| 2 | chemistry.com.pk 5th-ed page (479 pp, 107 MB) | links JS-gated; curl blocked; jina reader IP-blocked — NOT retrieved (5th ed stays the upgrade candidate) |
| 3 | dokumen.pub 4th-ed page (360 [362] pp, 72 MB) | pages readable but `/download/` is Cloudflare-challenged — not retrievable from this sandbox |
| 4 | XtremePapers thread 53249 (84.3 MB attachment) | attachments login-walled (HTTP 403 for guests) |
| 5 | **libgen.vg mirror (this README's copy)** | **SOURCED — full 362 pp copy** |

## Course binding (planned)

v2 hub course `cie-igcse-chemistry-23` · specKey grammar `cambridge-international/igcse/chemistry/0620` (hub wiring lands at the serving lane).

## Upgrade candidates

- CUP **5th edition** (Harwood, Millington & Lodge, 2021, ISBN 978-1108951609, 479 pp) — the current-syllabus (2023–2027) edition; chemistry.com.pk hosts it but all found links are JS-gated.
- Hodder **Earl & Wilford 3rd edition** (taleem360 `cambridge-igcse-chemistry-3rd-edition-pdf-v7v`, direct link `f=784b1189` captured 2026-10-21) — alternative endorsed title, kept as a documented fallback.

## Next steps

1. Parse lane per `books/README.md` §5 phases 0–10 (quality gate: the same 8 points; strip the RM.DL watermark text at parse time).
2. Serving lane (TEXTBOOK doc + book_chapters + slices manifest + T-C20 flip) — note the hub `bookCorpusPathForCourse` one-pdf law is satisfied (single-book course).
3. Update `books/CATALOG.md` tracker in the same commit as each state change.
