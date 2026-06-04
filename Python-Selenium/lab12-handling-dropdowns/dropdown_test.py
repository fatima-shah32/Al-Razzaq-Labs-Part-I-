from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import os

# Chrome options (safe for EC2/Linux)
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

driver = webdriver.Chrome(options=options)

try:
    # Open local HTML file
    file_path = "file://" + os.path.abspath("dropdown.html")
    driver.get(file_path)

    print("Page Title:", driver.title)

    # Locate dropdown
    dropdown = driver.find_element(By.ID, "dropdown-example")

    # Create Select object
    select = Select(dropdown)

    # Select by visible text
    select.select_by_visible_text("Option 2")
    print("Selected by visible text: Option 2")

    # Select by value
    select.select_by_value("3")
    print("Selected by value: Option 3")

    # Get currently selected option
    selected_option = select.first_selected_option
    print("Final Selected Option:", selected_option.text)

    # Assertion check
    assert selected_option.text == "Option 3", "Dropdown selection failed!"

    print("Test Passed Successfully!")

except Exception as e:
    print("Test Failed:", e)

finally:
    driver.quit()
