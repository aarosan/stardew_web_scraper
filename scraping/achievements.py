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

    # Find the table with class 'wikitable sortable'
    table = soup.find('table', class_='wikitable sortable')

    # Initialize a list to store achievements
    achievements = []

    if table:
        # Find all rows in the table body, skipping the header row
        rows = table.find('tbody').find_all('tr')[1:]

        # Loop through each row
        for row in rows:
            # Find all <td> elements in the row
            tds = row.find_all('td')

            # Check if there are enough <td> elements
            if len(tds) >= 6:
                # Extract the required data
                name = tds[2].text.strip()
                description = tds[3].text.strip()
                reward = tds[5].text.strip()

                # Create a dictionary for the achievement
                achievement = {
                    'name': name,
                    'description': description,
                    'reward': reward
                }

                # Add the dictionary to the list
                achievements.append(achievement)
    else:
        print("Table not found")

    for achievement in achievements:
        print(achievement)

    return achievements

