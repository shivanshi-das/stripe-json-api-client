from fastprep_blackbox import api_request

def fetch(paths):
    status, body = api_request("POST", "/fetch", {"paths": paths})
    assert status == 200
    return body

def test_request_object_and_array_endpoints():
    result = fetch(["/fixture/record", "/fixture/list"])
    assert result == {"responses": [
        {"path": "/fixture/record", "status": 200, "body": {"label": "hello", "count": 7}},
        {"path": "/fixture/list", "status": 200, "body": [1, 2, 3]}],
        "requested_paths": ["/fixture/record", "/fixture/list"]}

def test_preserve_repetitions_order_and_error_body():
    paths = ["/fixture/missing", "/fixture/record", "/fixture/missing"]
    result = fetch(paths)
    assert result["requested_paths"] == paths
    assert result["responses"] == [
        {"path": "/fixture/missing", "status": 404, "body": {"error": "missing"}},
        {"path": "/fixture/record", "status": 200, "body": {"label": "hello", "count": 7}},
        {"path": "/fixture/missing", "status": 404, "body": {"error": "missing"}}]

def test_empty_endpoint_list():
    assert fetch([]) == {"responses": [], "requested_paths": []}
