# Task 1: Review robots.txt to Ensure Policy Compliance

# Task 2: Understanding HTML and the DOM for the Durham Library Site

# Find HTML Element for a single entry
# li.row.cp-search-result-item

# Find title
# span.title-content

# Find author
# a.author-link

# Find format and publish year
# div.cp-format-info span.display-info-primary

# Task 3: Write a Program to Extract this Data 

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
    driver.get("https://durhamcounty.bibliocommons.com/v2/search?query=learning%20spanish&searchType=smart")

    # Store results 
    results = []

    #Get results
    search_result = driver.find_element(By.CSS_SELECTOR, "section.cp-search-results")

    search_results = search_result.find_elements(By.CSS_SELECTOR, "li.row.cp-search-result-item")

    for single_HTML in search_results:
        # Title
        title = single_HTML.find_element(By.CSS_SELECTOR, "span.title-content").text

        # Author
        authors = single_HTML.find_elements(By.CSS_SELECTOR, "a.author-link")

        author_text = "; ".join(author.text for author in authors)

        # Format & publish year
        format_publish = single_HTML.find_element(By.CSS_SELECTOR, "div.cp-format-info span.display-info-primary").text

        # Create book
        book = {"Title":title, 
                "Authors":author_text, 
                "Format_Publish_Year":format_publish}

        # Add each book to the results 
        results.append(book)        
except Exception as e:
    print(f"Error: {type(e).__name__}: {e}")
finally:
    driver.quit()

# Create the DataFrame and Print 
df = pd.DataFrame(results)
print(df)

# Task 4: Write out The Data
# Create a get_books.csv
df.to_csv('get_books.csv', index=False)

# Create a get_books.json
df.to_json('get_books.json', orient='index')