"""Full-book Docling parse for the 4PH1 PHYSICS book, per-page checkpointed JSON.

Usage: python3 scripts/docling_full_physics.py FROM TO     (1-based, inclusive)
Skips pages whose JSON already exists (resume-safe).
Writes data/physics/docling_pages/page_XXX.json per page.
Offset: book_page = pdf_page - 10 (probed 2026-10-19: PDF 13 = book 3 ch1 opener;
        PDF 144 header prints '134').
"""
import os, sys, json, time, resource, gc

os.environ.setdefault("HF_HUB_OFFLINE", "1")
os.environ.setdefault("TRANSFORMERS_OFFLINE", "1")
os.environ.setdefault("TOKENIZERS_PARALLELISM", "false")
os.environ.setdefault("OMP_NUM_THREADS", "2")
os.environ.setdefault("MKL_NUM_THREADS", "2")

PDF = "/home/z/my-project/data/physics/student-book.pdf"
OUT_DIR = "/home/z/my-project/data/physics/docling_pages"
OFFSET = 10
ARTIFACTS = os.environ.get("DOCLING_ARTIFACTS_PATH", "")
os.makedirs(OUT_DIR, exist_ok=True)

from docling.document_converter import DocumentConverter, PdfFormatOption
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions, RapidOcrOptions
from docling.datamodel.accelerator_options import AcceleratorOptions


def build_converter(formula: bool = True) -> DocumentConverter:
    opts = PdfPipelineOptions()
    opts.do_ocr = True
    opts.ocr_options = RapidOcrOptions(lang=["en"])
    opts.accelerator_options = AcceleratorOptions(num_threads=2, device="cpu")
    opts.do_table_structure = True
    opts.do_formula_enrichment = formula
    if ARTIFACTS:
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
    conv_nof = None  # lazy retry converter (formula enrichment off)
    t_start = time.time()
    n_done = 0
    for pno in todo:
        t0 = time.time()
        rec = None
        try:
            res = conv.convert(PDF, page_range=(pno, pno))
            rec = page_json(res.document, pno)
        except Exception as e1:  # known 2.33 bug: CodeFormula crash on some regions
            print(f"page {pno} retry-noforumla ({str(e1)[:80]})", flush=True)
            try:
                if conv_nof is None:
                    conv_nof = build_converter(formula=False)
                res = conv_nof.convert(PDF, page_range=(pno, pno))
                rec = page_json(res.document, pno)
                rec["formula_enrichment"] = False
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
