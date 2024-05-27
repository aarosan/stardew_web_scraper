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

    # Print the HTML content
    # print(soup.prettify())
   
    # Find the table with class 'wikitable' and id 'navbox'
    table = soup.find('table', class_='wikitable', id='navbox')

    # Initialize a list to store titles
    titles = []

    seasons = {"Spring", "Summer", "Fall", "Winter"}

    if table:
        # Find all <a> elements within the table
        a_tags = table.find_all('a')

        # Loop through each <a> element
        for a_tag in a_tags:
            # Get the 'title' attribute of the <a> element
            title = a_tag.get('title')
            if title and title not in seasons:  # Ensure the title is not None and not a season
                titles.append(title)
    else:
        print("Table not found")

    return titles

