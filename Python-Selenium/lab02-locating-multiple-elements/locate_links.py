from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

# Configure Chrome options for EC2/Linux
options = Options()
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")

# ChromeDriver path
service = Service("/usr/bin/chromedriver")

# Launch browser
driver = webdriver.Chrome(service=service, options=options)

# Open webpage
driver.get("https://example.com")

# Locate all hyperlinks
links = driver.find_elements(By.TAG_NAME, "a")

# Print link details
for link in links:
    print("Text:", link.text)
    print("URL :", link.get_attribute("href"))
    print("-" * 50)

# Count links
print(f"Total number of links found: {len(links)}")

# Close browser
driver.quit()
