import requests
from bs4 import BeautifulSoup

URL = "https://stardewvalleywiki.com/Stardew_Valley_Wiki"
r = requests.get(URL)

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(r.content, 'html.parser')

# Find and print the title of the webpage
title = soup.title.string
print(f"Title of the webpage: {title}")
