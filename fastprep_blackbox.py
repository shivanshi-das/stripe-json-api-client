"""Local stand-in for FastPrep's runtime-provided fastprep_blackbox module."""
import json
import urllib.request
from urllib.error import HTTPError

BASE_URL = "http://127.0.0.1:8765"


def api_request(method, path, body=None):
    data = json.dumps(body).encode() if body is not None else None
    req = urllib.request.Request(
        BASE_URL + path, data=data, method=method,
        headers={"Content-Type": "application/json"},
    )
    try:
        with urllib.request.urlopen(req, timeout=10) as r:
            return r.status, json.loads(r.read() or b"null")
    except HTTPError as e:
        return e.code, json.loads(e.read() or b"null")
