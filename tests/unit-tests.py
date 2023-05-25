import pytest
from app import is_valid_url, screenshot

@pytest.mark.parametrize("url, expected", [
    ("https://www.example.com", True),
    ("http://invalidurl", False),
    ("https://www.google.com", True),
    ("ftp://example.com", False)
])
def test_is_valid_url(url, expected):
    assert is_valid_url(url) == expected
