import requests
from bs4 import BeautifulSoup

# Function to scrape data from home page
def scrape_page(url):
    # Send a GET request to the website
    r = requests.get(url)

    # Parse the HTML content using BeautifulSoup

    soup = BeautifulSoup(r.content, 'html.parser')

    monsters = []  

    a_tags = soup.find_all('a')

    # Debug: Print the total number of <a> tags found
    # print(f"Total <a> tags found: {len(a_tags)}")

    # Debug: Print the <a> tags within the specified range
    # for i, a_tag in enumerate(a_tags[170:248], start=170):
    #     print(f"{i}: {a_tag}")

    # Loop through each <a> element within the specified range
    for a_tag in a_tags[170:248]:
        # Get the 'title' attribute of the <a> element
        monster = a_tag.get('title')
        if monster:
            monsters.append(monster)

    # Print the villagers for debugging
    for monster in monsters:
        print(monster)

    return monsters
    

# Example URL for testing
url = "https://stardewvalleywiki.com/Monsters"
scrape_page(url)