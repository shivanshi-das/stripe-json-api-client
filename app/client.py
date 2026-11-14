import requests
def fetch_endpoints(base_url, paths):
    """Request each supplied path and return its path, HTTP status and decoded JSON body."""
    # TODO: implement the HTTP endpoint client. The fixture service is already supplied.
    responses = []
    for path in paths:
        response = requests.get(f"{base_url}{path}")
        resp_dict = {}
        resp_dict["path"] = f"{path}"
        resp_dict["status"] = response.status_code
        resp_dict["body"] = response.json()
        responses.append(resp_dict)
    return responses


