import undetected_chromedriver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.common.exceptions import NoSuchElementException

# Initialize the undetected_chromedriver
driver = undetected_chromedriver.Chrome()
'''open csv file'''
ds = pd.read_csv('laptop_details_startech.csv')
specification = []

short_description = []

for laptops in ds['Model_link']:
    driver.get(laptops)
    time.sleep(5)
    '''Specification'''
    spec = driver.find_element(By.CLASS_NAME, 'data-table')
    specification.append(spec.text)
    print(spec.text)
    '''Short description'''
    s_desc = driver.find_element(By.CLASS_NAME, 'full-description')
    short_description.append(s_desc.text)
    print(s_desc.text)

data = {'Model_Name': ds['Model_Name'], 'Model_link': ds['Model_link'],
        'Specification': specification, 'Short_Description': short_description}
df = pd.DataFrame(data)
df.to_csv('all_laptop_data_startech.csv', index=False)

# Close the web driver
driver.quit()
