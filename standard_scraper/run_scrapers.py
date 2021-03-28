from scrapers.JSPScraper import WebScraper
from factories import scraper_factory, logger_factory
import sys
import constants
import api_handler
import utils
from datetime import date
import threading
from threading import Thread, ThreadError
import os

date_ranges = utils.date_range(date(1999, 3, 5), date(2020, 12, 30))
filetype = '.csv'


def scrape_copper_lead(state, url):
    master_logger.info("COPPER/LEAD SCRAPE %s", state)
    web_scraper = scraper_factory.copper_lead_scraper(state, url, date_ranges, filetype)
    web_scraper.scrape()

def scrape_chem(state, url):
    master_logger.info("CHEM SCRAPE %s", state)
    web_scraper = scraper_factory.chem_scraper(state, url, date_ranges, filetype)
    web_scraper.scrape()


def scrape_coli(state, url):
    master_logger.info("COLI SCRAPE %s", state)
    web_scraper = scraper_factory.coli_scraper(state, url, date_ranges, filetype)
    web_scraper.scrape()


def scrape_state(state, state_dict, url):
    if state_dict[api_handler.coli] is not None:
        scrape_coli(state, url)
    if state_dict[api_handler.chem] is not None:
        scrape_chem(state, url)
    if state_dict[api_handler.copper_lead] is not None:
        scrape_copper_lead(state, url)





def start_threading(states):
    #Handles multiple states running at a time
    for state in states:
        master_logger.info("Crawling: %s", state)
        url = api_handler.get_url(state)
        try:
            scraper_thread = Thread(name=state, target=scrape_state, args=(state, states[state], url,))
            scraper_thread.start()
        except ThreadError as te:
            master_logger.error(te.with_traceback())
        while threading.active_count() > 10:
            if threading.active_count() == 0:
                break


def single_state(states, state):
    url = api_handler.get_url(state)
    scrape_state(state, states[state], url)

utils.check_dirs()
master_logger = logger_factory.build_master_logger()
if __name__ == '__main__':
    states = api_handler.jsp_states
    single_state(states, 'Texas')
    # start_threading(states)
