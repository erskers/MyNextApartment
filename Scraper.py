import requests
from bs4 import BeautifulSoup
from Apartment import Apartment


class Scraper:
    apartments = []

    def __init__(self, url):
        raw_listings = scrape_site(url)
        apartments = parse_apartments(raw_listings)


def scrape_site(url):
    page_response = requests.get(url, timeout=5)
    page_content = BeautifulSoup(page_response.text, "html.parser")
    '''
    listing-card listing-card--normal
    class="listing-card__description-text listing-card__description-text--normal"
    '''
    listings = []
    raw_fetch = page_content.find_all('div', attrs={'class': 'listing-card listing-card--normal'})
    for listing in raw_fetch:
        item = " ".join(listing.text.split())
        listings.append(item)
    return listings


def parse_apartments(raw_listings):

    for listing in raw_listings:
        print listing
    return []
