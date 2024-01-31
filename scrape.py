import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options = Options()
options.headless = True  # Running in headless mode
driver = webdriver.Chrome(options=options)

# Relative path to the DATASTORE folder from the script's current directory
folder_path = os.path.join('.', 'DATASTORE', 'NHL', 'ACTIONNETWORK')

try:
    driver.get("https://www.actionnetwork.com/nhl/public-betting")

    # Wait for the table to load
    driver.implicitly_wait(10)

    # Ensure the specified folder exists; if not, create it
    os.makedirs(folder_path, exist_ok=True)

    # Locate the table using its CSS class
    table = driver.find_element(By.CSS_SELECTOR, "table.css-1uek3nh.epxndxd0")

    # Define the full path for the screenshot file
    screenshot_path = os.path.join(folder_path, 'AN-NHL.png')

    # Take a screenshot of just the table element and save it to the specified folder
    table.screenshot(screenshot_path)

finally:
    driver.quit()
