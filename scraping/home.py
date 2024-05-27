import requests
from bs4 import BeautifulSoup

# Function to scrape data from home page
def scrape_page(url):
    # Send a GET request to the website
    r = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    # Uncomment if/else statement below to start returnin parsed data to main.py
    # if r.status_code == 200:
    #     soup = BeautifulSoup(r.content, 'html.parser')
    #     title = soup.title.string
    #     return {"url": url, "title": title}
    # else:
    #     print(f"Failed to retrieve the webpage: {url}")
    #     return None

    soup = BeautifulSoup(r.content, 'html.parser')
    title = soup.title.string
    return {'Home Page Title': title}