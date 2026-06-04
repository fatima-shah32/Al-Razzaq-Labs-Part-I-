from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time
import os

# Chrome options (safe for EC2/Linux headless execution)
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

try:
    # Open website
    driver.get("https://www.example.com")

    print("Page Title:", driver.title)

    # ---- Screenshot 1: Basic Screenshot ----
    screenshot_file = "screenshot.png"
    driver.save_screenshot(screenshot_file)

    print(f"Screenshot saved: {screenshot_file}")

    # ---- Screenshot 2: Timestamped Screenshot ----
    timestamp = time.strftime("%Y%m%d-%H%M%S")
    timestamped_file = f"screenshot_{timestamp}.png"

    driver.save_screenshot(timestamped_file)

    print(f"Timestamped screenshot saved: {timestamped_file}")

    # ---- Verify File Creation ----
    assert os.path.exists(screenshot_file), "Basic screenshot not found!"
    assert os.path.exists(timestamped_file), "Timestamped screenshot not found!"

    print("File verification successful!")

except Exception as e:
    print("Test Failed:", e)

finally:
    driver.quit()
    print("Browser closed.")
