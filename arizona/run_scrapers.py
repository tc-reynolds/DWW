from ArizonaScraper import Web_Scraper
import sys
import constants
import api_handler
import utils
from datetime import date

if __name__ == '__main__':
    date_ranges = utils.date_range(date(1999, 3, 5), date(2020, 12, 30))
    state = 'Tennessee'
    filetype = '.csv'
    url = api_handler.get_url(state)
    print(state)
    print(url)
    if len(sys.argv) == 1:
        print("Call program passed with argument of either CHEM or COLI ")
        print("EXAMPLE: python3 ArizonaScraper.py CHEM")
        exit()
    if "COLI" in sys.argv[1]:
        print("COLI SCRAPE")
        chem_scrape = False
        # Read in existing data for duplicate check
        save_location = constants.COLI_SAVE_LOCATION + state + filetype
        api_endpoint = api_handler.get_coli_call(state)
        expected_headers = constants.COLIFORM_HEADERS
        csv_headers = constants.CSV_COLIFORM
        web_scraper = Web_Scraper(url, expected_headers, csv_headers,
                                  chem_scrape, save_location, date_ranges, api_endpoint)
        web_scraper.scrape()
    elif "CHEM" in sys.argv[1]:
        print("CHEM SCRAPE")
        save_location = constants.CHEM_SAVE_LOCATION + state + filetype
        chem_scrape = True
        api_endpoint = api_handler.get_chem_call(state)
        expected_headers = constants.CHEM_HEADERS
        csv_headers = constants.CSV_CHEM
        web_scraper = Web_Scraper(url, expected_headers, csv_headers,
                                  chem_scrape, save_location, date_ranges, api_endpoint)
        web_scraper.scrape()
    elif "LEAD_COPPER":
        pass
    else:
        print("Execute program with argument of either CHEM, COLI, or LEAD_COPPER ")
        print("EXAMPLE: python3 ArizonaScraper.py CHEM")
        exit()
