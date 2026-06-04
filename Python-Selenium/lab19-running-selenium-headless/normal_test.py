from selenium import webdriver
from time import time

driver = webdriver.Chrome()

start_time = time()

driver.get("https://www.example.com")

end_time = time()

print("Page Title:", driver.title)
print(f"Normal Mode Load Time: {end_time - start_time:.2f} seconds")

driver.quit()
