import time
import urllib.request
import urllib.error
from typing import Dict, Any
from urllib.parse import urlparse


def is_valid_url(url: str) -> bool:
    try:
        parsed = urlparse(url)
        return parsed.scheme in ("http", "https") and bool(parsed.netloc)
    except Exception:
        return False


def probe_url(url: str, timeout: float = 5.0) -> Dict[str, Any]:
    if not is_valid_url(url):
        return {"ok": False, "status_code": None, "latency_ms": None, "error": "Invalid URL"}
    start = time.perf_counter()
    try:
        req = urllib.request.Request(url, method="GET", headers={"User-Agent": "TornadoUI-Diagnostics/1.0"})
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            status_code = getattr(resp, "status", None) or resp.getcode()
            latency_ms = round((time.perf_counter() - start) * 1000, 2)
            return {"ok": 200 <= status_code < 400, "status_code": status_code, "latency_ms": latency_ms, "error": None}
    except urllib.error.HTTPError as e:
        latency_ms = round((time.perf_counter() - start) * 1000, 2)
        return {"ok": False, "status_code": e.code, "latency_ms": latency_ms, "error": str(e)}
    except Exception as e:
        latency_ms = round((time.perf_counter() - start) * 1000, 2)
        return {"ok": False, "status_code": None, "latency_ms": latency_ms, "error": str(e)}
