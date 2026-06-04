from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

driver.implicitly_wait(10)

try:
    # Open demo site
    driver.get("https://example.com")

    print("Page Title:", driver.title)

    # Validate page title
    assert "Example Domain" in driver.title

    # Find all links
    links = driver.find_elements(By.TAG_NAME, "a")

    print(f"Links Found: {len(links)}")

    # Screenshot
    driver.save_screenshot("search_results.png")

    print("Test Passed Successfully!")

except Exception as e:
    print("Test Failed:", repr(e))

finally:
    driver.quit()
