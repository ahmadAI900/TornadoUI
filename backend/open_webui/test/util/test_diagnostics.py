from open_webui.utils.diagnostics import is_valid_url, probe_url


def test_is_valid_url():
    assert is_valid_url("https://example.com") is True
    assert is_valid_url("http://localhost:8080") is True
    assert is_valid_url("not a url") is False
    assert is_valid_url("ftp://example.com") is False


def test_probe_url_invalid():
    res = probe_url("invalid")
    assert res["ok"] is False
    assert res["error"] == "Invalid URL"
