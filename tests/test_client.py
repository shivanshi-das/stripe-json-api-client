from app.client import fetch_endpoints

def test_empty_client_input_needs_no_server():
    assert fetch_endpoints("http://127.0.0.1:8765", []) == []

