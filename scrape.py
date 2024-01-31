from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
from PIL import Image
import io
import requests
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os

options = Options()
options.headless = True  # Running in headless mode
driver = webdriver.Chrome(options=options)

try:
    driver.get("https://www.actionnetwork.com/nhl/public-betting")
    time.sleep(5)  # buffer period

    # Get scroll height.
    last_height = driver.execute_script("return document.body.scrollHeight")

    # The offset to keep track of how much we've scrolled.
    offset = 0
    # Store the screenshots here
    parts = []

    # Scroll and take multiple screenshots.
    while offset < last_height:
        # Scroll to next offset.
        driver.execute_script(f"window.scrollTo(0, {offset});")
        time.sleep(1)  # Wait for the page to load.

        # Create a screenshot.
        # Get PNG byte string of screenshot.
        png = driver.get_screenshot_as_png()
        # Use PIL to open byte string as an image object.
        im = Image.open(io.BytesIO(png))

        # Save only the visible window (as it will include the top part of the next view).
        if offset + im.size[1] >= last_height:
            # Last portion of the webpage; may not need the full height.
            parts.append(im.crop((0, 0, im.size[0], last_height - offset)))
        else:
            parts.append(im)

        # Move the offset to the next portion of the webpage.
        offset += im.size[1]

    # Stitch images together.
    total_height = sum(part.size[1] for part in parts)
    full_image = Image.new('RGB', (parts[0].size[0], total_height))
    offset = 0
    for part in parts:
        full_image.paste(part, (0, offset))
        offset += part.size[1]

    # Save the full image
    full_image.save(os.path.join(
        'DATASTORE/NHL/ACTIONNETWORK', 'AN-NHL-CAPTURE.png'))


finally:
    driver.quit()
