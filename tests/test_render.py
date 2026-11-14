from app.render import build_url


def test_build_url():
    assert build_url("https://example.com/search", q="spider", page=2) == "https://example.com/search?q=spider&page=2"
