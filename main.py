import pymongo
import importlib

# Connect to MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["stardew_info"]

def main():
    # URLs for the different pages on the wiki
    page_urls = {
        "home": "https://stardewvalleywiki.com/Stardew_Valley_Wiki",
        # "crops": "https://stardewvalleywiki.com/Crops",
        # "farm_animals": "https://stardewvalleywiki.com/Animals",
        # "fruit_trees": "https://stardewvalleywiki.com/Fruit_Trees",
        # "monsters": "https://stardewvalleywiki.com/Monsters",
        "villagers": "https://stardewvalleywiki.com/Villagers",
        # "achievements": "https://stardewvalleywiki.com/Achievements",
    }

    # Dynamically import the scrape_page function from each module in the scraping directory
    for page in page_urls:
        module_name = f"scraping.{page}"
        module = importlib.import_module(module_name)
        scrape_page_func = getattr(module, "scrape_page")
        
        # Scrape data from the page and store it in the database
        scraped_data = scrape_page_func(page_urls[page])
        # print(scraped_data)

        # Insert scraped data into MongoDB collection

        # if scraped_data:
            # collection = db[page]
            # collection.insert_one(scraped_data)

if __name__ == "__main__":
    main()