# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
from Apartment import Apartment


class Scraper:
    apartments = []

    def __init__(self, url):
        raw_listings = scrape_site(url)
        self.apartments = parse_apartments(raw_listings)


def scrape_site(url):
    page_response = requests.get(url, timeout=5)
    page_content = BeautifulSoup(page_response.text, "html.parser")
    listings = []
    raw_fetch = page_content.find_all('div', attrs={'class': 'listing-card listing-card--normal'})
    for listing in raw_fetch:
        line = listing.text.replace("  ", "")
        line = remove_dup_newline(line)
        if line != '\n':
            item = line
            listings.append(item)
    return listings


def remove_dup_newline(txt):
    while '\n\n' in txt:
        txt=txt.replace('\n\n','\n')
        txt = txt.replace('\n \n', '\n')
    return txt


def parse_apartments(raw_listings):
    apartments = []
    for line in raw_listings:
        items = line.splitlines()
        items.pop(0)
        items.pop(0)
        if items[0] == u'LägenhetLägenhet':
            items.pop(0)

        address = items[0]
        city = items[1]
        price = int(items[2].replace(u'\xa0', '').replace('kr', ''))
        size = items[3]
        rooms = items[4]
        rent = int(items[5].replace(u'kr/mån', '').replace(u'\xa0', ''))
        info = items[7]
        apartment = Apartment(address, price, size, rent, city, rooms, info)
        apartments.append(apartment)
    return apartments
