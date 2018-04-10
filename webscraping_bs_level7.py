from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time
import pandas

# optional argument for Chrome Driver - ensure Chrome is configured for full screen
options = webdriver.ChromeOptions()
options.add_argument("--start-fullscreen")
driver = webdriver.Chrome(chrome_options=options)

# navigate to the right webpage
driver.get('https://www.fuelcheck.nsw.gov.au/app')

search_text = driver.find_element_by_id("txtbxSuburbPostCode")
search_text.send_keys("SYDNEY (2000)")
search_text.send_keys(Keys.ENTER)
search_text.send_keys(Keys.ENTER)

dropdown_text = driver.find_element_by_xpath("//button[@id='selectFuel']")
dropdown_text.click()

P95 = driver.find_element_by_css_selector('[for="P95"]')
P95.click()

filter = driver.find_element_by_id("fuelFilter")
filter.click()

time.sleep(4)
search_button = driver.find_element_by_css_selector(".search-button")
search_button.click()

time.sleep(6)
source = driver.page_source

soup = BeautifulSoup(source, "html.parser")
all_details = soup.select("#show-data .result-item")

count = 0

# create a list called records - we will use it for pandas
records = []

for item in all_details:

    # create a dictionary called listings - we will export it to records
    listings = {}

    listings["Price"] = item.select_one(".price b").text.strip()
    listings["Vendor"] = item.select_one(".station b").text.strip()
    listings["Address"] = item.select_one(".tiny").text.strip()

    # exporting the dictionary (listings) into the list (records)
    records.append(listings)
    print("Before Pandas ...")
    print(listings)

# using pandas for data analysis and manipulation
df = pandas.DataFrame(records)
print("After Pandas ...")
print(df)

time.sleep(6)
driver.close()
