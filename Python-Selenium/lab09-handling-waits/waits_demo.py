from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Chrome options (safe for EC2/Linux)
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

    # ----------------------------
    # ✅ TASK 1: IMPLICIT WAIT
    # ----------------------------
    driver.implicitly_wait(5)

    # Example element lookup (safe demo)
    try:
        element = driver.find_element(By.TAG_NAME, "h1")
        print("Implicit Wait Element Found:", element.text)
    except Exception as e:
        print("Implicit wait element not found:", e)

    # ----------------------------
    # ✅ TASK 2: EXPLICIT WAIT
    # ----------------------------

    wait = WebDriverWait(driver, 10)

    element_explicit = wait.until(
        EC.presence_of_element_located((By.TAG_NAME, "h1"))
    )

    print("Explicit Wait Element Found:", element_explicit.text)

    # Click condition example (safe fallback demo)
    clickable = wait.until(
        EC.element_to_be_clickable((By.TAG_NAME, "h1"))
    )

    print("Element is clickable (simulation)")
    clickable.click()

    print("Test Passed Successfully!")

except Exception as e:
    print("Test Failed:", e)

finally:
    driver.quit()
    print("Browser closed.")
