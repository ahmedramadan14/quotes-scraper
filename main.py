import requests
from bs4 import BeautifulSoup
import csv

url = "https://quotes.toscrape.com/"
soup = BeautifulSoup(requests.get(url).text, "html.parser")

# create or open a CSV file to write the quotes
with open("quotes.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Quote ", " Author ", " Tags "]) 

    for quote in soup.find_all("div", class_="quote"):
        text = quote.find("span", class_="text").text
        author = quote.find("small", class_="author").text
        tags = ", ".join(tag.text for tag in quote.find_all("a", class_="tag"))

        
        writer.writerow([text, author, tags])

        # Print the quote, author, and tags to the console ( optional )
        print("Quote:", text)
        print("Author:", author)
        print("Tags:", tags)
        print("-" * 40)
