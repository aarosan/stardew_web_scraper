import requests
from bs4 import BeautifulSoup

# Function to scrape data from home page
def scrape_page(url):

    # Send a GET request to the website
    r = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(r.content, 'html.parser')

    # Initialize a list to store achievements
    fruit_trees = []

    # Find all <span> elements with class 'toctext'
    spans = soup.find_all('span', class_='toctext')

    # Extract the text from each <span> and add it to the list if it contains the word 'tree'
    for span in spans:
        text = span.get_text(strip=True)
        if 'tree' in text.lower():  # Check if 'tree' is in the text, case insensitive
            fruit_trees.append(text)

    for fruit_tree in fruit_trees:
        print(fruit_tree)

    return fruit_trees

