import requests
from bs4 import BeautifulSoup

request = requests.get("http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html")
content = request.content
soup = BeautifulSoup(content, "html.parser")

# identifying the right class to scrape
element_price = soup.find("p", {"class": "price_color"})

# what's the difference without text and strip ?
print(element_price)

# strip all the whitespaces
string_price = element_price.text.strip()

# what's the difference with text and strip ?
# print(string_price)

# strip out the irrelevant details
price_without_symbols = string_price[1:]

# simple data manipulation before exporting the data out
# print(price_without_symbols)