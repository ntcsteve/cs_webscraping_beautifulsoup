import requests
from bs4 import BeautifulSoup

# request the right URL - using Scott Pilgrim as an example
request = requests.get("http://books.toscrape.com/catalogue/scott-pilgrims-precious-little-life-scott-pilgrim-1_987/index.html")

# we want all the content in the requested URL
content = request.content

# using html.parser - all batteries included
soup = BeautifulSoup(content, "html.parser")

# doing a quick test if we are getting all the content
print(soup.prettify())
