'''

Capture a screenshot of the webpage at the given URL and save it locally.

syntax:
    python3 app.py <url>

Returns:
    None

'''
import sys
from time import sleep
import requests
from pyvirtualdisplay import Display
from selenium import webdriver


def is_valid_url(url):
    '''
    Check if the URL is valid by sending a HEAD request.

    Args:
        url (str): The URL to check.

    Returns:
        bool: True if the URL is valid, False otherwise.
    '''
    try:
        response = requests.head(url, timeout=10)
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False

def screenshot(url):
    '''
    Capture a screenshot of the webpage at the given URL.

    Args:
        url (str): The URL of the webpage to capture.

    Returns:
        None

    '''
    if not is_valid_url(url):
        print("Invalid URL:", url)
        return

    display = Display(visible=0, size=(1920, 1080))
    display.start()

    driver = webdriver.Firefox()
    driver.get(url)
    sleep(1)

    driver.get_screenshot_as_file("screenshot.png")
    driver.quit()


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please provide a URL as an argument.")
        sys.exit(1)
    if len(sys.argv) > 2:
        print("please provide only one URL")
        sys.exit(1)
    URL = sys.argv[1]

    screenshot(URL)
