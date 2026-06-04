from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options

options = Options()

# 🔥 REQUIRED for EC2
options.add_argument("--headless=new")
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")
options.add_argument("--disable-gpu")
options.add_argument("--remote-debugging-port=9222")

# Use system chromedriver
service = Service("/usr/bin/chromedriver")

driver = webdriver.Chrome(service=service, options=options)

driver.get("https://www.google.com")

print("Title:", driver.title)

driver.quit()
