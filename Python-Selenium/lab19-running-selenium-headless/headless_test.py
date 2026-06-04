from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import time

# Configure Chrome Headless
chrome_options = Options()
chrome_options.add_argument("--headless=new")
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--disable-gpu")

# Launch browser
driver = webdriver.Chrome(options=chrome_options)

# Measure page load time
start_time = time()

driver.get("https://www.example.com")

end_time = time()

# Print page title
print("Page Title:", driver.title)

# Print load time
print(f"Headless Mode Load Time: {end_time - start_time:.2f} seconds")

# Capture screenshot
driver.save_screenshot("screenshot.png")

print("Screenshot saved successfully!")

# Close browser
driver.quit()
