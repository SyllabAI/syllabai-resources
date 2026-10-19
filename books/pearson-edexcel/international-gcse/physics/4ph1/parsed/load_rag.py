#!/usr/bin/env python3
"""Generic RAG ingestion helper for edexcel_igcse_physics_chunks_v1.jsonl.

The JSONL is universally compatible: one JSON object per line with
{"id", "text", "metadata"}. Below are ready-to-run patterns for the most
common stacks. Pick ONE depending on your engine.

Optional deps:  pip install chromadb   (for the Chroma example)
                pip install langchain-core (for the LangChain example)
"""
import json
import os

JSONL_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                          "edexcel_igcse_physics_chunks_v1.jsonl")

# --------------------------------------------------------------- 1. plain
def load_raw():
    """Return list of dicts: [{'id', 'text', 'metadata': {...}}, ...]"""
    with open(JSONL_PATH, encoding="utf-8") as f:
        return [json.loads(line) for line in f]

def load_filtered(include_types=None, exclude_types=None, min_chars=200):
    """Filter chunks by content_type and size.
    include_types: e.g. {'body', 'key_point', 'worked_example'}
    exclude_types: e.g. {'index', 'answers', 'divider'}  (recommended default)
    """
    include_types = set(include_types or [])
    exclude_types = set(exclude_types or [])
    out = []
    for c in load_raw():
        ct = c["metadata"]["content_type"]
        if include_types and ct not in include_types:
            continue
        if ct in exclude_types:
            continue
        if len(c["text"]) < min_chars:
            continue
        out.append(c)
    return out

# --------------------------------------------------------------- 2. Chroma
def ingest_chroma(persist_dir="./chroma_physics", batch=100):
    """Upsert all chunks into a local persistent Chroma collection."""
    import chromadb
    client = chromadb.PersistentClient(path=persist_dir)
    col = client.get_or_create_collection(
        name="edexcel_igcse_physics",
        metadata={"hnsw:space": "cosine"})
    chunks = load_filtered(exclude_types={"index", "divider"})
    for i in range(0, len(chunks), batch):
        part = chunks[i:i + batch]
        metas = []
        for c in part:
            m = dict(c["metadata"])
            m = {k: v for k, v in m.items() if v is not None}
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
    for c in load_filtered(exclude_types={"index", "divider"}):
        yield Document(page_content=c["text"], metadata=c["metadata"])

# --------------------------------------------------------------- 4. LlamaIndex
def load_llamaindex():
    """Yield LlamaIndex TextNode objects."""
    from llama_index.core.schema import TextNode
    for c in load_filtered(exclude_types={"index", "divider"}):
        yield TextNode(text=c["text"], id_=c["id"], metadata=c["metadata"])

if __name__ == "__main__":
    import sys
    target = sys.argv[1] if len(sys.argv) > 1 else "stats"
    if target == "chroma":
        ingest_chroma()
    else:
        allc = load_raw()
        print(f"total chunks: {len(allc)}")
        print(f"total chars : {sum(c['metadata']['char_count'] for c in allc)}")
        by_type = {}
        for c in allc:
            by_type.setdefault(c["metadata"]["content_type"], 0)
            by_type[c["metadata"]["content_type"]] += 1
        for k, v in sorted(by_type.items(), key=lambda x: -x[1]):
            print(f"  {k:22s} {v}")
        print("\nusage: python load_rag.py [stats|chroma]")
