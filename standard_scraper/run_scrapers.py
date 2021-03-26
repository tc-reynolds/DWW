from JSPScraper import Web_Scraper
import sys
import constants
import api_handler
import utils
from datetime import date
import threading
from threading import Thread, ThreadError
import logging
import os

date_ranges = utils.date_range(date(1999, 3, 5), date(2020, 12, 30))
filetype = '.csv'


def scrape_copper_lead(state, url):
    master_logger.info("COPPER/LEAD SCRAPE %s", state)
    chem_scrape = 'COPPER_LEAD'
    # Read in existing data for duplicate check
    save_location = constants.COPPER_LEAD_SAVE_LOCATION + state + filetype
    log_location = constants.COPPER_LEAD_LOG_LOCATION + state + '.log'
    logger = build_logger(state, log_location, 'copper_lead')

    api_endpoint = api_handler.get_copper_lead_call(state)
    expected_headers = constants.COPPER_LEAD_HEADERS
    csv_headers = constants.CSV_COPPER_LEAD
    web_scraper = Web_Scraper(url, expected_headers, csv_headers,
                              chem_scrape, save_location, logger,
                              date_ranges, api_endpoint)
    web_scraper.scrape()


def scrape_chem(state, url):
    master_logger.info("CHEM SCRAPE %s", state)
    save_location = constants.CHEM_SAVE_LOCATION + state + filetype
    log_location = constants.CHEM_LOG_LOCATION + state + '.log'
    logger = build_logger(state, log_location, 'chem')
    chem_scrape = 'CHEM'
    api_endpoint = api_handler.get_chem_call(state)
    expected_headers = constants.CHEM_HEADERS
    csv_headers = constants.CSV_CHEM
    web_scraper = Web_Scraper(url, expected_headers, csv_headers,
                              chem_scrape, save_location, logger,
                              date_ranges, api_endpoint)
    web_scraper.scrape()


def scrape_coli(state, url):
    master_logger.info("COLI SCRAPE %s", state)
    chem_scrape = 'COLI'
    # Read in existing data for duplicate check
    save_location = constants.COLI_SAVE_LOCATION + state + filetype
    log_location = constants.COLI_LOG_LOCATION + state + '.log'
    logger = build_logger(state, log_location, 'coli')

    api_endpoint = api_handler.get_coli_call(state)
    expected_headers = constants.COLIFORM_HEADERS
    csv_headers = constants.CSV_COLIFORM
    web_scraper = Web_Scraper(url, expected_headers, csv_headers,
                              chem_scrape, save_location, logger,
                              date_ranges, api_endpoint)
    web_scraper.scrape()


def scrape_state(state, state_dict, url):
    # if state_dict[api_handler.coli] is not None:
    #     scrape_coli(state, url)
    if state_dict[api_handler.chem] is not None:
        scrape_chem(state, url)
    # if state_dict[api_handler.copper_lead] is not None:
    #     scrape_copper_lead(state, url)

def build_log_handler(log_location):
    #Handles log formatting and timestamping
    formatter = logging.Formatter(fmt='%(asctime)s %(levelname)-8s %(message)s',
                                  datefmt='%Y-%m-%d %H:%M:%S')
    handler = logging.FileHandler(log_location, mode='w')
    handler.setFormatter(formatter)
    return handler

def build_master_logger():

    logger = logging.getLogger('master_logger')
    logger.setLevel(logging.INFO)
    logger.addHandler(build_log_handler(constants.MASTER_LOG))
    return logger

def build_logger(state, log_location, type):
    #Builds logger object for whatever state you are crawling
    #With convention ; Florida_Chem_logger as the unique name.
    logger_name = state + '_' + type + '_logger'
    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.INFO)
    logger.addHandler(build_log_handler(log_location))
    return logger


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

def check_dirs():
    #If you don't have logging or data directories locally, this generates them for you
    dir_ls = [
        constants.DATA_DIR,
        constants.LOG_DIR,
        constants.COPPER_LEAD_LOG_DIR,
        constants.CHEM_LOG_DIR,
        constants.COLI_LOG_DIR,
        constants.COPPER_LEAD_DATA_DIR,
        constants.CHEM_DATA_DIR,
        constants.COLI_DATA_DIR,
        constants.MASTER_LOG_DIR
    ]
    for dir in dir_ls:
        if not os.path.exists(dir):
            os.makedirs(os.path.normpath(dir))

def single_state(states, state):
    url = api_handler.get_url(state)
    scrape_state(state, states[state], url)

check_dirs()
master_logger = build_master_logger()
if __name__ == '__main__':
    states = api_handler.jsp_states
    # single_state(states, 'Texas')
    start_threading(states)
