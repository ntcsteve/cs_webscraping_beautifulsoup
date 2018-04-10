import requests
from bs4 import BeautifulSoup

request = requests.get("http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html")
content = request.content
soup = BeautifulSoup(content, "html.parser")

# identify and extract everything
title = soup.find("h1").text.strip()
price = soup.find("p", {"class": "price_color"}).text.strip()
stock = soup.find("p", {"class": "instock availability"}).text.strip()

# show all the relevant content
print(title)
print(price)
print(stock)
