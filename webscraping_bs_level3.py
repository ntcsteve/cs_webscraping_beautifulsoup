import requests
from bs4 import BeautifulSoup

# urls
base_url = "http://books.toscrape.com/catalogue/page-"
first_url = "http://books.toscrape.com/catalogue/page-1.html"
next_page = "http://books.toscrape.com/catalogue/page-2.html"

# loop counter to start from 0
count = 0

# only the first 3 urls
for page in range(1, 4):

    new_url = base_url + str(page) + ".html"
    r = requests.get(new_url)
    c = r.content
    soup = BeautifulSoup(c, "html.parser")

    # find all the right class
    all_details = soup.find_all("article", {"class": "product_pod"})

    for item in all_details:

        # identify and extract everything
        Title = item.find("h3").text.strip()
        Price = item.find("p", {"class": "price_color"}).text.strip()
        Stock = item.find("p", {"class": "instock availability"}).text.strip()

        # show all the relevant content
        count += 1
        print("Book {} ".format(count))
        print(Title)
        print(Price)
        print(Stock)
