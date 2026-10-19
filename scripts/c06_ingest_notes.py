#!/usr/bin/env python3
"""T-C06 staged ingestion driver: POST the converted canonical notes to the
syllabai-core canonical-document endpoint.

Endpoint: POST {CORE_BASE_URL}/api/v1/teacher/content/documents?kind=EXTERNAL_NOTES
Auth:     bearer token of a TEACHER/ADMIN account (env INGEST_TOKEN; never
          printed, never committed).
Dedup:    core resolves documents by source checksum — re-running is an
          idempotent no-op for already-ingested notes (duplicate=true).

Dry run is the DEFAULT: pass --execute to actually POST. Every response is
recorded to the run log. The payload this script consumes is the committed
SME-RevisionNotes/<tranche>/canonical/ directory (BUNDLE_MANIFEST.json is the
sha256 spine: the script verifies each file's checksum before POSTing).

Usage:
  python3 c06_ingest_notes.py <canonical-dir>                # dry run
  python3 c06_ingest_notes.py <canonical-dir> --execute      # real POSTs
"""
import hashlib
import json
import os
import sys
import time
import urllib.error
import urllib.request

BASE = os.environ.get("CORE_BASE_URL", "")
TOKEN = os.environ.get("INGEST_TOKEN", "")


def post_canonical(path, kind="EXTERNAL_NOTES", tries=3):
    body = open(path, "rb").read()
    url = f"{BASE}/api/v1/teacher/content/documents?kind={kind}"
    last = None
    for i in range(tries):
        req = urllib.request.Request(url, data=body, method="POST",
                                     headers={"Authorization": f"Bearer {TOKEN}",
                                              "Content-Type": "application/json",
                                              "User-Agent": "t-c06-notes-ingestion/1.0"})
        try:
            with urllib.request.urlopen(req, timeout=60) as r:
                return json.loads(r.read().decode())
        except urllib.error.HTTPError as e:
            detail = e.read().decode()[:400]
            if e.code < 500 or i == tries - 1:
                return {"http_error": e.code, "detail": detail}
            last = e
        except Exception as e:  # transient network — retry
            last = e
            time.sleep(1.5 * (i + 1))
    return {"error": str(last)}


def main():
    canonical_dir = sys.argv[1]
    execute = "--execute" in sys.argv
    manifest = json.load(open(os.path.join(canonical_dir, "BUNDLE_MANIFEST.json")))
    print(f"bundle: {manifest['notes']} notes | engine {manifest['engine']} "
          f"{manifest['engine_version']} | schema {manifest['canonical_schema']} "
          f"| pinned {manifest['pinned_resources_commit'][:12]}")
    if not execute:
        print("DRY RUN (pass --execute to POST). Verifying checksums only:")
    elif not BASE or not TOKEN:
        sys.exit("CORE_BASE_URL and INGEST_TOKEN are required with --execute")

    ok = dup = fail = 0
    log = []
    for entry in sorted(manifest["entries"], key=lambda e: e["note_path"]):
        name = os.path.basename(entry["note_path"])[:-3] + ".canonical.json"
        path = os.path.join(canonical_dir, name)
        digest = hashlib.sha256(open(path, "rb").read()).hexdigest()
        if digest != entry["canonical_sha256"]:
            fail += 1
            log.append({"note": name, "result": "CHECKSUM_MISMATCH"})
            print(f"  CHECKSUM MISMATCH {name}")
            continue
        if not execute:
            ok += 1
            continue
        result = post_canonical(path)
        if "http_error" in result or "error" in result:
            fail += 1
            print(f"  FAIL {entry['note_id']}: {result}")
            log.append({"note": name, "result": result})
        elif result.get("duplicate"):
            dup += 1
            log.append({"note": name, "result": "duplicate",
                        "document_id": result.get("documentId")})
        else:
            ok += 1
            log.append({"note": name, "result": "created",
                        "document_id": result.get("documentId"),
                        "chunks": result.get("chunks")})
        if (ok + dup) % 40 == 0:
            print(f"  posted {ok + dup}/{manifest['notes']}")
        time.sleep(0.3)  # gentle on the free-tier runtime
    print(f"DONE: created={ok} duplicate={dup} failed={fail}")
    if execute:
        out = os.path.join(canonical_dir, "INGESTION_RUN_LOG.json")
        with open(out, "w") as f:
            json.dump({"created": ok, "duplicate": dup, "failed": fail,
                       "responses": log}, f, indent=1)
        print(f"run log: {out}")
    return 1 if fail else 0


if __name__ == "__main__":
    sys.exit(main())
