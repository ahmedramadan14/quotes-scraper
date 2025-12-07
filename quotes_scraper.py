import requests
from bs4 import BeautifulSoup

url = "https://quotes.toscrape.com/"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

for quote in soup.find_all("div", class_="quote"):
    text = quote.find("span", class_="text").text
    author = quote.find("small", class_="author").text
    tags = [tag.text for tag in quote.find_all("a", class_="tag")]

    print("Quote:", text)
    print("Author:", author)
    print("Tags:", tags)
    print("-" * 40)
