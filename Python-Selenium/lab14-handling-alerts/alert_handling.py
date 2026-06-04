from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time

# Configure Chrome for EC2/Linux
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

try:
    # Open test website
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")

    print("Website opened successfully")

    # Trigger alert
    alert_button = driver.find_element(
        By.XPATH,
        "//button[text()='Click for JS Alert']"
    )

    alert_button.click()

    print("Alert triggered")

    # Switch to alert
    alert = driver.switch_to.alert

    # Read alert text
    alert_text = alert.text
    print("Alert Text:", alert_text)

    # Accept alert
    alert.dismiss()

    print("Alert accepted successfully")

    # Screenshot after alert handling
    driver.save_screenshot("alert_result.png")

    print("Screenshot saved successfully")

    time.sleep(2)

finally:
    driver.quit()
