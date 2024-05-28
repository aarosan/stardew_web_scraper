import requests
from bs4 import BeautifulSoup

# Function to scrape data from home page
def scrape_page(url):
    # Send a GET request to the website
    r = requests.get(url)


    soup = BeautifulSoup(r.content, 'html.parser')
    farm_animals = []

    # Find all <span> elements with class 'toctext'
    spans = soup.find_all('span', class_='toctext')

    # Extract the text from each <span> and add it to the list if it contains the word 'tree'
    for span in spans[24:]:
        text = span.get_text(strip=True)
        if not any(word in text.lower() for word in ['animals', 'hutch', 'bugs', 'history', 'reference']):
            farm_animals.append(text)

        # if 'tree' in text.lower():
            # fruit_trees.append(text)

    for farm_animal in farm_animals:
        print(farm_animal)

    return farm_animals