#!/usr/bin/env python3
"""gh_api — minimal GitHub REST helper for SyllabAI corpus uploads.
Token comes from the GH_TOKEN environment variable; never hardcoded."""
import json
import os
import urllib.request

TOKEN = os.environ.get("GH_TOKEN", "")
OWNER = "SyllabAI"
REPO = "syllabai-resources"
BASE = f"https://api.github.com/repos/{OWNER}/{REPO}"


def api(path):
    return f"{BASE}/{path}"


def _req(path, method="GET", body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(api(path), data=data, method=method, headers={
        "Authorization": f"token {TOKEN}",
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
    })
    with urllib.request.urlopen(req) as r:
        return json.loads(r.read().decode())


def get(path):
    return _req(path)


def post(path, body):
    return _req(path, "POST", body)


def patch(path, body):
    return _req(path, "PATCH", body)


def get_branch(name):
    """Return {commit: {sha, commit: {tree: {sha}}}} shape for a branch name."""
    ref = get(f"git/refs/heads/{name}")
    sha = ref["object"]["sha"] if "object" in ref else ref["commit"]["sha"]
    commit = get(f"git/commits/{sha}")
    return {"commit": {"sha": sha, "commit": {"tree": {"sha": commit["tree"]["sha"]}}}}
