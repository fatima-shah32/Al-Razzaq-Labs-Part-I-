from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome for headless EC2 execution
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

try:
    # Open webpage
    driver.get("https://www.wikipedia.org")

    print("Page Title:", driver.title)

    # Scroll to bottom of page
    driver.execute_script(
        "window.scrollTo(0, document.body.scrollHeight);"
    )

    print("Scrolled to bottom")

    time.sleep(2)

    # Locate element
    element = driver.find_element(By.CSS_SELECTOR, "div.central-featured")

    # Scroll element into view
    driver.execute_script(
        "arguments[0].scrollIntoView();",
        element
    )

    print("Element scrolled into view")

    # Validate visibility
    assert element.is_displayed(), \
        "Element is not visible on the page."

    print("Visibility check passed")

    # Capture screenshot
    driver.save_screenshot("scroll_result.png")

    print("Screenshot saved successfully!")

finally:
    driver.quit()
