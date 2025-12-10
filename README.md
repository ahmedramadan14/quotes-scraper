# Quotes Scraper

A simple Python script that scrapes quotes, authors, and tags from [Quotes to Scrape](https://quotes.toscrape.com/) using Python, Requests, and BeautifulSoup.

## Features

* Extracts all quotes from the main page.
* Retrieves the author of each quote.
* Collects associated tags for each quote.
* Prints the results in a clean and readable format.

## Installation

1. Clone this repository:

```bash
git clone https://github.com/ahmedramadan14/quotes-scraper.git
```

2. Navigate to the project folder:

```bash
cd quotes-scraper
```

3. Install required Python packages (if not already installed):

```bash
pip install requests beautifulsoup4
```

## Usage

Run the script using Python:

```bash
python quotes_scraper.py
```

## Output

You will see output like:

```
Quote: “The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”
Author: Albert Einstein
Tags: ['change', 'deep-thoughts', 'thinking', 'world']
----------------------------------------
```

## Contributing

Feel free to fork this repository and submit pull requests.

## License

This project is open source and available under the MIT License.
