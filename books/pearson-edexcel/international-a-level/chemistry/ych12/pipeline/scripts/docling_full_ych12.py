"""Full-book Docling parse for IAL Chemistry SB2 (Curtis/Murgatroyd/Scott), per-page checkpointed JSON.

Usage: venv-python docling_full_ych12.py FROM TO     (1-based, inclusive)
Skips pages whose JSON already exists (resume-safe).
Writes data/ych12_sb2/docling_pages/page_XXX.json per page.

Page law (probe 2026-10-25, 4-way confirmed):
  book_page = pdf_page - 12   (roman front matter = pdf - 0, ii..xiii = PDF 2..13; i absent)
  - PDF 3 header 'iii' (CONTENTS), PDF 13 header 'xiii' (ASSESSMENT OVERVIEW cont.)
  - TOC: TOPIC 11 = book 2 -> opener renders on PDF 14
  - printed header digits: PDF 311 prints '299' (INDEX), PDF 320 prints '308' (graph-paper end leaf)
  Book page 1 does not exist in the PDF (print blank omitted, YCH11/YPH11 law class);
  arabic starts at book 2 = PDF 14. L-021: TOC's INDEX 299 promise present -> copy COMPLETE.

Lane deviation from the playbook ladder (formula ON -> OFF -> error), identical to YCH11 r0:
docling 2.33.0's formula rung is dead code here — its CodeFormula integration emits EMPTY
formula text (YCH11 METHOD D-7, L-019/L-020), so the base corpus runs formula OFF and display
equations go through the verbatim manual-transcription rescue. Layout/tables unaffected.
"""
import os, sys, json, time, resource, gc

os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
os.environ.setdefault("OMP_NUM_THREADS", "2")
os.environ.setdefault("MKL_NUM_THREADS", "2")

PDF = "/home/z/my-project/data/ych12_sb2/student-book-2-original.pdf"
OUT_DIR = "/home/z/my-project/data/ych12_sb2/docling_pages"
OFFSET = int(os.environ.get("YCH12_OFFSET", "12"))
ARTIFACTS = os.environ.get("DOCLING_ARTIFACTS_PATH") or None  # None -> docling default cache (auto-download on first convert)
os.makedirs(OUT_DIR, exist_ok=True)

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, RapidOcrOptions, AcceleratorOptions


def build_converter() -> DocumentConverter:
    opts = PdfPipelineOptions()
    opts.do_ocr = True
    opts.ocr_options = RapidOcrOptions(lang=["en"])
    opts.accelerator_options = AcceleratorOptions(num_threads=2, device="cpu")
    opts.do_table_structure = True
    opts.do_formula_enrichment = False  # see module docstring: 2.33 formula text is empty either way
    opts.artifacts_path = ARTIFACTS
    return DocumentConverter(format_options={InputFormat.PDF: PdfFormatOption(pipeline_options=opts)})


def page_json(doc, page_no: int) -> dict:
    from docling_core.types.doc import TableItem, PictureItem, TextItem
    texts = []
    for item, _level in doc.iterate_items():
        bbox = None
        prov = getattr(item, "prov", None)
        if prov:
            p = prov[0]
            bb = p.bbox
            bbox = [round(bb.l, 1), round(bb.t, 1), round(bb.r, 1), round(bb.b, 1)]
        if isinstance(item, TableItem):
            try:
                md = item.export_to_markdown(doc)
            except Exception:
                md = ""
            texts.append({"label": "table", "text": md, "bbox": bbox})
        elif isinstance(item, PictureItem):
            texts.append({"label": "picture", "text": "", "bbox": bbox})
        elif isinstance(item, TextItem):
            texts.append({"label": str(item.label), "text": item.text or "", "bbox": bbox})
        else:
            texts.append({"label": str(item.label), "text": getattr(item, "text", "") or "", "bbox": bbox})
    return {"pdf_page": page_no, "book_page": page_no - OFFSET, "items": texts}


def main():
    frm, to = int(sys.argv[1]), int(sys.argv[2])
    todo = [p for p in range(frm, to + 1) if not os.path.exists(f"{OUT_DIR}/page_{p:03d}.json")]
    if not todo:
        print(f"[skip] pages {frm}-{to} already done")
        return
    conv = build_converter()
    t_start = time.time()
    n_done = 0
    for pno in todo:
        t0 = time.time()
        rec = None
        try:
            res = conv.convert(PDF, page_range=(pno, pno))
            rec = page_json(res.document, pno)
        except Exception as e1:  # transient 2.33 crashes: one clean retry, then error record
            print(f"page {pno} retry ({str(e1)[:80]})", flush=True)
            time.sleep(2)
            try:
                res = conv.convert(PDF, page_range=(pno, pno))
                rec = page_json(res.document, pno)
            except Exception as e2:
                rec = {"pdf_page": pno, "book_page": pno - OFFSET, "items": [],
                       "error": str(e2)[:200]}
                print(f"page {pno} ERROR {str(e2)[:120]}", flush=True)
        with open(f"{OUT_DIR}/page_{pno:03d}.json", "w") as f:
            json.dump(rec, f, ensure_ascii=False)
        n_done += 1
        peak = resource.getrusage(resource.RUSAGE_SELF).ru_maxrss / 1024
        print(f"page {pno} ok  {time.time() - t0:.1f}s  peakRSS={peak:.0f}MB  items={len(rec['items'])}", flush=True)
        try:
            del res
        except NameError:
            pass
        gc.collect()
    total = time.time() - t_start
    print(f"[batch {frm}-{to}] {n_done} pages in {total:.0f}s ({total / max(1, n_done):.1f}s/page)", flush=True)


if __name__ == "__main__":
    main()
