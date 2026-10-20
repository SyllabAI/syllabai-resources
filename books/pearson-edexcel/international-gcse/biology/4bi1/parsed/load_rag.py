#!/usr/bin/env python3
"""Generic RAG ingestion helper for edexcel_igcse_biology_chunks_v1.jsonl.

Corpus format: JSONL, one flat 15-key object per line (PARSE_STANDARD point
6 grammar): id, book_title, author, unit_no, unit_name, chapter_no,
chapter_title, section, content_type, book_pages, pdf_pages, char_count,
text — plus text_original + llm_repaired on polished chunks.

NOTE (errata E-002 lineage): the physics lane's load_rag.py reads a
c["metadata"] wrapper its own corpus does not use; this loader matches the
actual flat format. Use THIS file as the reference pattern.

Optional deps:  pip install chromadb   (for the Chroma example)
                pip install langchain-core (for the LangChain example)
"""
import json
import os

JSONL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "edexcel_igcse_biology_chunks_v1.jsonl")

# --------------------------------------------------------------- 1. plain
def load_raw():
    """Return list of flat chunk dicts (15-key grammar)."""
    with open(JSONL_PATH, encoding="utf-8") as f:
        return [json.loads(line) for line in f]

def load_filtered(include_types=None, exclude_types=None, min_chars=200):
    """Filter chunks by content_type and size.
    include_types: e.g. {'body', 'key_point', 'learning_objectives'}
    exclude_types: e.g. {'index', 'answers', 'divider'}  (recommended default)
    """
    include_types = set(include_types or [])
    exclude_types = set(exclude_types or [])
    out = []
    for c in load_raw():
        ct = c["content_type"]
        if include_types and ct not in include_types:
            continue
        if ct in exclude_types:
            continue
        if len(c["text"]) < min_chars:
            continue
        out.append(c)
    return out

# --------------------------------------------------------------- 2. Chroma
def ingest_chroma(persist_dir="./chroma_biology", batch=100):
    """Upsert all chunks into a local persistent Chroma collection."""
    import chromadb
    client = chromadb.PersistentClient(path=persist_dir)
    col = client.get_or_create_collection(
        name="edexcel_igcse_biology",
        metadata={"hnsw:space": "cosine"})
    chunks = load_filtered(exclude_types={"index", "divider", "back_cover"})
    for i in range(0, len(chunks), batch):
        part = chunks[i:i + batch]
        metas = []
        for c in part:
            m = {k: v for k, v in c.items() if k != "text" and v is not None}
            metas.append(m)
        col.upsert(ids=[c["id"] for c in part],
                   documents=[c["text"] for c in part],
                   metadatas=metas)
        print(f"upserted {i + len(part)}/{len(chunks)}")
    print(f"done -> {persist_dir}")

# --------------------------------------------------------------- 3. LangChain
def load_langchain():
    """Yield LangChain Document objects (works with any retriever)."""
    from langchain_core.documents import Document
    for c in load_filtered(exclude_types={"index", "divider", "back_cover"}):
        yield Document(page_content=c["text"], metadata=c)

# --------------------------------------------------------------- 4. LlamaIndex
def load_llamaindex():
    """Yield LlamaIndex TextNode objects (works with any retriever)."""
    from llama_index.core.schema import TextNode
    for c in load_filtered(exclude_types={"index", "divider", "back_cover"}):
        yield TextNode(text=c["text"], id_=c["id"], metadata=c)

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "stats"
    if target == "chroma":
        ingest_chroma()
    else:
        allc = load_raw()
        print(f"total chunks: {len(allc)}")
        print(f"total chars : {sum(c['char_count'] for c in allc)}")
        by_type = {}
        for c in allc:
            by_type.setdefault(c["content_type"], 0)
            by_type[c["content_type"]] += 1
        for k, v in sorted(by_type.items(), key=lambda x: -x[1]):
            print(f"  {k:22s} {v}")
        print("\nusage: python load_rag.py [stats|chroma]")
