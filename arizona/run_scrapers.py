from ArizonaScraper import Web_Scraper
import sys
import constants
import api_handler
import utils
from datetime import date
import threading
from threading import Thread, ThreadError

date_ranges = utils.date_range(date(1999, 3, 5), date(2020, 12, 30))
filetype = '.csv'


def scrape_copper_lead(state, url):
    print("COPPER/LEAD SCRAPE")
    chem_scrape = False
    # Read in existing data for duplicate check
    save_location = constants.COPPER_LEAD_SAVE_LOCATION + state + filetype
    log_location = constants.COPPER_LEAD_LOG_LOCATION + state + '.log'

    api_endpoint = api_handler.get_copper_lead_call(state)
    expected_headers = constants.COPPER_LEAD_HEADERS
    csv_headers = constants.CSV_COPPER_LEAD
    web_scraper = Web_Scraper(url, expected_headers, csv_headers,
                              chem_scrape, save_location, log_location,
                              date_ranges, api_endpoint)
    web_scraper.scrape()

def scrape_chem(state, url):
    print("CHEM SCRAPE")
    save_location = constants.CHEM_SAVE_LOCATION + state + filetype
    log_location = constants.CHEM_LOG_LOCATION + state + '.log'
    chem_scrape = True
    api_endpoint = api_handler.get_chem_call(state)
    expected_headers = constants.CHEM_HEADERS
    csv_headers = constants.CSV_CHEM
    web_scraper = Web_Scraper(url, expected_headers, csv_headers,
                              chem_scrape, save_location, log_location,
                              date_ranges, api_endpoint)
    web_scraper.scrape()


def scrape_coli(state, url):
    print("COLI SCRAPE")
    chem_scrape = False
    # Read in existing data for duplicate check
    save_location = constants.COLI_SAVE_LOCATION + state + filetype
    log_location = constants.COLI_LOG_LOCATION + state + '.log'

    api_endpoint = api_handler.get_coli_call(state)
    expected_headers = constants.COLIFORM_HEADERS
    csv_headers = constants.CSV_COLIFORM
    web_scraper = Web_Scraper(url, expected_headers, csv_headers,
                              chem_scrape, save_location, log_location,
                              date_ranges, api_endpoint)
    web_scraper.scrape()

def scrape_state(state, state_dict, url):
    # if state_dict[api_handler.coli] is not None:
    #     scrape_coli(state, url)
    # if state_dict[api_handler.chem] is not None:
    #     scrape_chem(state, url)
    if state_dict[api_handler.copper_lead] is not None:
        scrape_copper_lead(state, url)


if __name__ == '__main__':
    states = api_handler.jsp_states
    key = 'Delaware'
    url = api_handler.get_url(key)
    scrape_state(key, states[key], url)

    #
    # for state in states:
    #     url = api_handler.get_url(state)
    #     # scrape_state(state, states[state], url)
    #     try:
    #         scraper_thread = Thread(target=scrape_state, args=(state, states[state], url,))
    #         scraper_thread.start()
    #     except ThreadError as te:
    #         print(te.with_traceback())
    #     while threading.active_count() > 10:
    #         pass
    #     print(state)
