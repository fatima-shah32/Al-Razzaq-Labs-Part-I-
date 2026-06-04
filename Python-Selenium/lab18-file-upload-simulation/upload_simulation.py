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
    html_file = os.path.abspath("upload_page.html")
    driver.get(f"file://{html_file}")

    # Locate file input
    file_input = driver.find_element(By.ID, "fileInput")

    # Absolute path of test file
    test_file = os.path.abspath("sample.txt")

    # Upload file
    file_input.send_keys(test_file)

    time.sleep(2)

    # Verify selected file
    selected_file = file_input.get_attribute("value")

    print("Selected File:", selected_file)

    if "sample.txt" in selected_file:
        print("File Upload Simulation Successful!")
    else:
        print("File Upload Simulation Failed!")

    # Screenshot
    driver.save_screenshot("upload_result.png")

finally:
    driver.quit()
