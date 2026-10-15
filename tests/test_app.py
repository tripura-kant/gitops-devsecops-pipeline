import json
import threading
import urllib.error
import urllib.request
from http.server import HTTPServer

import pytest

from app.app import HealthCheckHandler


@pytest.fixture(scope="module")
def port():
    srv = HTTPServer(("127.0.0.1", 0), HealthCheckHandler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    yield srv.server_address[1]
    srv.shutdown()
    srv.server_close()


def test_healthcheck_returns_200(port):
    r = urllib.request.urlopen(f"http://127.0.0.1:{port}/healthcheck")
    assert r.status == 200
    assert json.loads(r.read()) == {"status": "healthy"}


def test_unknown_path_returns_404(port):
    with pytest.raises(urllib.error.HTTPError) as e:
        urllib.request.urlopen(f"http://127.0.0.1:{port}/nope")
    assert e.value.code == 404