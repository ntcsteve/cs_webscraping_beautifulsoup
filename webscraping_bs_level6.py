from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

# optional argument for Chrome Driver - ensure Chrome is configured for full screen
options = webdriver.ChromeOptions()
options.add_argument("--start-fullscreen")
driver = webdriver.Chrome(chrome_options=options)

# navigate to the right webpage
driver.get('https://www.fuelcheck.nsw.gov.au/app')

# find the ID element called txtbxSuburbPostCode and enter the keyword into the textbox
search_text = driver.find_element_by_id("txtbxSuburbPostCode")
search_text.send_keys("SYDNEY (2000)")
search_text.send_keys(Keys.ENTER)
search_text.send_keys(Keys.ENTER)

# find the XPATH and select the dropdown list
dropdown_text = driver.find_element_by_xpath("//button[@id='selectFuel']")
dropdown_text.click()

# find the CSS selector P95 and select it
P95 = driver.find_element_by_css_selector('[for="P95"]')
P95.click()

# find the ID element called fuelFilter and click it
filter = driver.find_element_by_id("fuelFilter")
filter.click()

# waiting for the web page to load for 4s
time.sleep(4)

# find the CSS selector .search-button and select it
search_button = driver.find_element_by_css_selector(".search-button")
search_button.click()

# waiting for the web page to load for 6s
time.sleep(6)

# using page_source - gets the source of the current page.
source = driver.page_source

soup = BeautifulSoup(source, "html.parser")
all_details = soup.select("#show-data .result-item")

count = 0
for item in all_details:

    # extract all the data we need
    Price = item.select_one(".price b")
    Vendor = item.select_one(".station b")
    Address = item.select_one(".tiny")

    count += 1
    # examples where we want specific content from the page
    print("Station {} ".format(count))
    print("Price - $" + Price.text.strip())
    print("Vendor - " + Vendor.text.strip())
    print("Address - " + Address.text.strip())

time.sleep(6)
driver.close()
