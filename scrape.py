from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.headless = True  # Running in headless mode
driver = webdriver.Chrome(options=options)

try:

    # URL 1:
    driver.get("")
    # buffer period
    time.sleep(5)
    # capture
    driver.save_screenshot("capture1.png")
    # pieces:
    example_element = driver.find_element(By.CLASS_NAME, "example-class")
    print(example_element.text)


finally:

    driver.quit()
