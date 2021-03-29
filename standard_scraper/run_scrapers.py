from scrapers.JSPScraper import WebScraper
from factories.scraper_factory import ScraperFactory
from factories.logger_factory import LoggerFactory
import sys
import constants
import api_handler
import utils
from datetime import date
import threading
from threading import Thread, ThreadError
import os
import time

date_ranges = utils.date_range(date(1999, 3, 5), date(2020, 12, 30))
filetype = '.csv'


def scrape_copper_lead(state, url):
    master_logger.info("COPPER/LEAD SCRAPE %s", state)
    web_scraper = ScraperFactory.copper_lead_scraper(state, url, date_ranges, filetype)
    web_scraper.scrape()

def scrape_chem(state, url):
    master_logger.info("CHEM SCRAPE %s", state)
    web_scraper = ScraperFactory.chem_scraper(state, url, date_ranges, filetype)
    web_scraper.scrape()


def scrape_coli(state, url):
    master_logger.info("COLI SCRAPE %s", state)
    web_scraper = ScraperFactory.coli_scraper(state, url, date_ranges, filetype)
    web_scraper.scrape()


def scrape_state(state, state_dict, url):
    if state_dict[api_handler.coli] is not None:
        scrape_coli(state, url)
    if state_dict[api_handler.chem] is not None:
        scrape_chem(state, url)
    if state_dict[api_handler.copper_lead] is not None:
        scrape_copper_lead(state, url)

def remove_dead_threads(my_threads):
    for t in my_threads:
        if not t.is_alive():
            # get results from thread
            t.handled = True
            master_logger.info("Thread has ended and been removed...%s", t)
            my_threads.remove(t)
            del t
    return my_threads
def start_threading(states):
    #Handles multiple states running at a time
    my_threads = []
    for state in states:
        master_logger.info("Crawling: %s", state)
        url = api_handler.get_url(state)
        try:
            scraper_thread = Thread(name=state, target=scrape_state, args=(state, states[state], url,))
            scraper_thread.start()
            my_threads.append(scraper_thread)
        except ThreadError as te:
            master_logger.error(te.with_traceback())
        timer_start = time.monotonic()
        while threading.active_count() > 10:
            timer_end = time.monotonic() - timer_start
            if timer_end > 30:
                my_threads = remove_dead_threads(my_threads)
                timer_start = time.monotonic()
        if len(my_threads) == 0:
            master_logger.info("All threads finished...Exiting...")
            exit()


def single_state(states, state):
    url = api_handler.get_url(state)
    scrape_state(state, states[state], url)

#Checks whether required directories exist
#If not, create them.
utils.check_dirs()
master_logger = LoggerFactory.build_logger('master', constants.MASTER_LOG)
if __name__ == '__main__':
    states = api_handler.jsp_states
    # single_state(states, 'Texas')
    start_threading(states)
