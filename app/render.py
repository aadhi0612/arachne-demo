import requests


def build_url(base, **params):
    """Build a request URL offline (no network)."""
    return requests.Request("GET", base, params=params).prepare().url
