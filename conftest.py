"""Local only: start the FastAPI app on 127.0.0.1:8765 for the test session."""
import socket
import threading
import time

import pytest
import uvicorn

from app.main import app


@pytest.fixture(scope="session", autouse=True)
def server():
    config = uvicorn.Config(app, host="127.0.0.1", port=8765, log_level="warning")
    srv = uvicorn.Server(config)
    t = threading.Thread(target=srv.run, daemon=True)
    t.start()
    for _ in range(50):
        try:
            socket.create_connection(("127.0.0.1", 8765), timeout=0.2).close()
            break
        except OSError:
            time.sleep(0.1)
    yield
    srv.should_exit = True
    t.join(timeout=5)
