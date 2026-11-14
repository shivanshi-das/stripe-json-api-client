from fastapi import FastAPI
from fastapi.responses import JSONResponse
from pydantic import BaseModel, Field
from .client import fetch_endpoints

app = FastAPI()
hits = []
class Request(BaseModel):
    paths: list[str] = Field(max_length=20)

@app.get("/fixture/record")
def record():
    hits.append("/fixture/record")
    return {"label": "hello", "count": 7}

@app.get("/fixture/list")
def items():
    hits.append("/fixture/list")
    return [1, 2, 3]

@app.get("/fixture/missing")
def missing():
    hits.append("/fixture/missing")
    return JSONResponse(status_code=404, content={"error": "missing"})

@app.post("/fetch")
def fetch(request: Request):
    hits.clear()
    responses = fetch_endpoints("http://127.0.0.1:8765", request.paths)
    return {"responses": responses, "requested_paths": list(hits)}
