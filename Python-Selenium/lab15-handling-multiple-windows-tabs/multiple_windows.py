from selenium import webdriver
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
    # Open first website
    driver.get("https://www.python.org")

    print("First Tab")
    print("Title:", driver.title)
    print("URL:", driver.current_url)

    # Open second tab
    driver.switch_to.new_window("tab")
    driver.get("https://www.selenium.dev")

    # Open third tab
    driver.switch_to.new_window("tab")
    driver.get("https://www.wikipedia.org")

    # Get all window handles
    handles = driver.window_handles

    print(f"\nTotal Open Tabs: {len(handles)}\n")

    # Iterate through tabs
    for index, handle in enumerate(handles, start=1):
        driver.switch_to.window(handle)

        print(f"Tab {index}")
        print("Title:", driver.title)
        print("URL:", driver.current_url)
        print("-" * 50)

    # Screenshot of current tab
    driver.save_screenshot("multiple_tabs.png")

    print("\nScreenshot saved successfully!")

    time.sleep(2)

finally:
    driver.quit()
