import pytest
from app.py import is_valid_url, screenshot

@pytest.mark.parametrize("url, expected", [
    ("https://www.example.com", True),
    ("http://invalidurl", False),
    ("https://www.google.com", True),
    ("ftp://example.com", False)
])
def test_is_valid_url(url, expected):
    assert is_valid_url(url) == expected


@pytest.mark.parametrize("url", [
    "https://www.example.com",
    "https://www.google.com",
    "https://www.github.com"
])
def test_screenshot(url):
    screenshot(url)
    # Perform additional assertions if necessary


def test_screenshot_invalid_url():
    with pytest.raises(SystemExit):
        screenshot("http://invalidurl")


def test_screenshot_no_arguments():
    with pytest.raises(SystemExit):
        screenshot()


def test_screenshot_multiple_arguments():
    with pytest.raises(SystemExit):
        screenshot("https://www.example.com", "https://www.google.com")
