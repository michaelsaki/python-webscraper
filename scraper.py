import requests
from bs4 import BeautifulSoup

# Make a request to the website
response = requests.get("http://quotes.toscrape.com")

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find all quotes on the page
quotes = soup.find_all("span", {"class": "text"})

# Print each quote
for i, quote in enumerate(quotes):
    print(f"Quote {i + 1}: {quote.text}")
