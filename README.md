# Request API Endpoints

This is a FastPrep practice adapter. The report names Python HTTP endpoints but supplies no original repository, schemas or acceptance rules. Java is an equivalent practice adapter.

## Start here

Choose **Run Project** to run the native suite in `tests/` and the HTTP suite in `fastprep_tests/http/test_endpoints.py`. The starter intentionally fails the non-empty request cases. Choose one failure, trace it into `app/client.py`, make one focused change, save, and run again.

## Goal and expected behavior

Implement requests against the supplied endpoints. For this exercise, assume GET requests, decoded JSON, one output per input path, input ordering, repeated requests, and preservation of the supplied 404 body. An empty list makes no requests. These are explicitly authored practice rules, not recovered interview requirements.

## Task files

- `app/client.py` contains the unfinished client.
- `app/main.py` supplies the local fixture server and the client entry point.
- `fastprep_tests/http/test_endpoints.py` contains the three HTTP acceptance cases; `contract.json` declares their count. The native suite is also visible and included in Run Project.

## FastPrep practice environment

Python 3.11, FastAPI and pytest run in the released FastPrep runtime. **Run Project** launches the service on `127.0.0.1:8765` and runs all visible checks. No external service or credential is needed.

`POST /fetch` accepts `{"paths": ["/fixture/record", "/fixture/list", "/fixture/missing"]}`. It returns `{"responses": [{"path": "...", "status": 200, "body": {}}], "requested_paths": ["..."]}`. The supplied controller records actual fixture requests so the visible tests check transport behavior.

The only input paths are the three above; there are 0 to 20 paths. `/fixture/record` returns status 200 and `{"label":"hello","count":7}`; `/fixture/list` returns 200 and `[1,2,3]`; `/fixture/missing` returns 404 and `{"error":"missing"}`. Implementations may use the standard HTTP libraries already available. The `base_url`/`baseUrl` argument selects the supplied loopback server.

## Reconstruction provenance

No original repository paths or framework were supplied. Every path, fixture, JSON shape, HTTP method, error convention and test here is authored scaffolding. The retained question capture says “HTTP requests”; a prior summary says “HTML requests.” The direct capture and endpoint/Python context support the HTTP interpretation. No Bikemap, contact enrichment, replay, pagination, payment or other domain is inferred.

---

## Running locally (added, not part of FastPrep)

FastPrep's runtime provides `fastprep_blackbox` and starts the server for you. Locally, `fastprep_blackbox.py` and `conftest.py` stand in for that: pytest starts the app on `127.0.0.1:8765` automatically.

```
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pytest -v
```

`requests` was added to `requirements.txt` for local use. FastPrep's own runtime doesn't install it, so on FastPrep only the standard library (`urllib`) works.
