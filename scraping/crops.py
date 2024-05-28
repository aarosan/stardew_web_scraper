import requests
from bs4 import BeautifulSoup

# Function to scrape data from home page
def scrape_page(url):

    # Send a GET request to the website
    r = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(r.content, 'html.parser')

    # Uncomment to print the HTML content
    # print(soup.prettify())
   
    # Find the table with class 'wikitable' and id 'navbox'
    table = soup.find('table', class_='wikitable', id='navbox')

    # Initialize a list to store titles
    crops = []

    seasons = {"Spring", "Summer", "Fall", "Winter"}

    if table:
        # Find all <a> elements within the table
        a_tags = table.find_all('a')

        # Loop through each <a> element
        for a_tag in a_tags:
            # Get the 'title' attribute of the <a> element
            crop = a_tag.get('title')
            if crop and crop not in seasons:  
                crops.append(crop)
    else:
        print("Table not found")
    
    for crop in crops:
        print(crop)

    return crops

