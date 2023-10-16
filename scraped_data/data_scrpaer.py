import undetected_chromedriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException


'''Configure ChromeDriver'''
driver = undetected_chromedriver.Chrome()

# Create an empty list to store the links
links_list = []

for page_ranges in range(1, 100+1):
    url = f"https://www.newegg.com/p/pl?d=laptop&page={page_ranges}"
    driver.get(url)
    time.sleep(5)
    '''All web elements'''
    main_body = driver.find_element(By.XPATH, '/html/body')

    all_lists = main_body.find_elements(By.CLASS_NAME, "item-cells-wrap")
    for listed in all_lists:
        laptops = listed.find_elements(By.CLASS_NAME, "item-cell")
        for laptop in laptops:
            link = laptop.find_element(By.TAG_NAME, 'a')
            laptop_details_link = link.get_attribute("href")
            print(laptop_details_link)
            links_list.append(laptop_details_link)

# Create a DataFrame using pandas
df = pd.DataFrame({'Links': links_list})

# Save the DataFrame to a CSV file
df.to_csv('laptop_links.csv', index=False)
