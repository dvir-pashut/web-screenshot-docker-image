'''
this is a python script
'''
import sys
from time import sleep
from pyvirtualdisplay import Display
from selenium import webdriver


URL = sys.argv[1]

display = Display(visible=0, size=(1920, 1080))
display.start()


driver = webdriver.Firefox()
driver.get('https://www.python.org')
sleep(1)

driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("end...")
