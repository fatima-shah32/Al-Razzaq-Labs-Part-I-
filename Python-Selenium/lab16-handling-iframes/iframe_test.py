from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import os
import time

# Configure Chrome for EC2/Linux
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

try:
    # Open local HTML page
    html_file = os.path.abspath("iframe_demo.html")
    driver.get(f"file://{html_file}")

    print("Page Title:", driver.title)

    # Switch to iframe by index
    driver.switch_to.frame(0)

    print("Switched to iFrame")

    # Locate text field inside iframe
    name_field = driver.find_element(By.ID, "nameField")
    name_field.send_keys("Fatima")

    print("Text entered successfully")

    # Locate and click button
    submit_button = driver.find_element(By.ID, "submitButton")
    submit_button.click()

    print("Button clicked successfully")

    # Return to main page
    driver.switch_to.default_content()

    print("Returned to main page context")

    # Verify main page heading
    heading = driver.find_element(By.TAG_NAME, "h1")

    assert heading.is_displayed()

    print("Main page verification successful")

    # Screenshot
    driver.save_screenshot("iframe_result.png")

    print("Screenshot saved successfully!")

    time.sleep(2)

finally:
    driver.quit()
