# Task 6: Scraping Structured Data 
# Import Selenium, Webdriver_manager, pandas, json
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import pandas as pd
import json 

# Load webpage 
driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

try:
    driver.get("https://owasp.org/www-project-top-ten/")

    # Get link for top 10
    top_10 = driver.find_element(By.CSS_SELECTOR, "section.page-body a")
    href = top_10.get_attribute("href")

    # Switch to new file 
    driver.get(href)

    # Pull top 10
    top_10_list = []

    lists = driver.find_elements(By.XPATH,'//h3[@id="top-102025-list"]/following-sibling::ol[1]//a')

    for list in lists:
        title = list.text
        href = list.get_attribute("href")

        top_10_list.append({"Title": title, "HREF Link": href})

    print(top_10_list)
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
finally:
    driver.quit()

# Create a owasp_top_10.csv
df = pd.DataFrame(top_10_list)
df.to_csv('owasp_top_10.csv', index=False)
