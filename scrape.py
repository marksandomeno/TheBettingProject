from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
options.headless = True  # Running in headless mode
driver = webdriver.Chrome(options=options)

try:

    # URL 1:
    driver.get("https://www.actionnetwork.com/nhl/public-betting")
    # buffer period
    time.sleep(5)
    # capture
    driver.save_screenshot("capture1.png")

    # Get the HTML from url
    html_content = driver.page_source
    # Save the HTML content to a file
    with open("page_source.html", "w", encoding="utf-8") as file:
        file.write(html_content)

    # This is how we would fetch a specific ids contents from the capture.
    example_element = driver.find_element(By.CLASS_NAME, "example-class")
    print(example_element.text)


finally:

    driver.quit()
