import requests
from bs4 import BeautifulSoup
import pandas

first_url = "http://books.toscrape.com/catalogue/page-1.html"
base_url = "http://books.toscrape.com/catalogue/page-"
next_page = "http://books.toscrape.com/catalogue/page-2.html"

# create a list called records - we will use it for pandas
records = []

for page in range(1, 4):

    new_url = base_url + str(page) + ".html"
    r = requests.get(new_url)
    c = r.content

    soup = BeautifulSoup(c, "html.parser")
    all_details = soup.find_all("article", {"class": "product_pod"})

    for item in all_details:

        # create a dictionary called listings - we will export it to records
        listings = {}

        listings["Title"] = item.find("h3").text.strip()
        listings["Price"] = item.find("p", {"class": "price_color"}).text.strip()
        listings["Stock"] = item.find("p", {"class": "instock availability"}).text.strip()

        # exporting the dictionary (listings) into the list (records)
        records.append(listings)
        print("Before Pandas ...")
        print(listings)

# using pandas for data analysis and manipulation
df = pandas.DataFrame(records)
print("After Pandas ...")
print(df)
