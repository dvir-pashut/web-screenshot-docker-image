from pyvirtualdisplay import Display
from selenium import webdriver
from time import sleep

display = Display(visible=0, size=(1920, 1080))
display.start()


driver = webdriver.Firefox()
driver.get('https://www.python.org')
sleep(1)

driver.get_screenshot_as_file("screenshot.png")
driver.quit()
print("end...")