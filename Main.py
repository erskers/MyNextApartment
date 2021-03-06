#!/usr/bin/python
from Apartment import Apartment
from Scraper import Scraper
#from CostCalculator import CostCalculator


if __name__ == '__main__':
    property_type = "bostadsratt"
    property_filter = "&rooms_min=2&rooms_max=2.5&price_min=3000000&price_max=4500000"
    url = "https://www.hemnet.se/bostader?item_types%5B%5D=" +property_type+property_filter
    testurl = "https://www.hemnet.se/bostader?location_ids%5B%5D=925968&item_types%5B%5D=bostadsratt&rooms_min=2&rooms_max=2.5&price_min=2500000&price_max=4500000"

    scraper = Scraper(testurl)
    apartments = scraper.apartments
    for apartment in apartments:
        print "--------------------"
        print apartment.address
        print apartment.price
        print apartment.rent
        print apartment.info


