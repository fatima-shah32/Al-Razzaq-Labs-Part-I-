from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

# Headless Chrome (safe for EC2/Linux)
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

driver = webdriver.Chrome(options=options)

try:
    # -------------------------
    # Task 3: Open Web Page
    # -------------------------
    driver.get("https://www.python.org")

    # -------------------------
    # Task 4: Check Page Title
    # -------------------------
    page_title = driver.title
    print("Page Title:", page_title)

    expected_title = "Welcome to Python.org"

    assert expected_title in page_title, \
        f"Title mismatch! Expected: {expected_title}, Got: {page_title}"

    print("Title Verification Passed")

    # -------------------------
    # Task 5: Locate Element
    # -------------------------
    element = driver.find_element(By.XPATH, "//a[text()='Downloads']")

    actual_text = element.text
    expected_text = "Downloads"

    print("Element Text:", actual_text)

    assert actual_text == expected_text, \
        f"Text mismatch! Expected: {expected_text}, Got: {actual_text}"

    print("Element Verification Passed")

    # -------------------------
    # Success Message
    # -------------------------
    print("Test Passed Successfully!")

except Exception as e:
    print("Test Failed:", e)

finally:
    driver.quit()
    print("Browser closed.")

