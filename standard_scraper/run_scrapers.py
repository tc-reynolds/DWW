from scrapers.JSPScraper import WebScraper
from factories.scraper_factory import ScraperFactory
from factories.logger_factory import LoggerFactory
import sys
import constants
import api_handler
import utils
from datetime import date
from services.scrape_service import ScrapeService
from services.threading_service import ThreadService
import threading
from threading import Thread, ThreadError
import os
import time


#Checks whether required directories exist
#If not, create them.
utils.check_dirs()
states = api_handler.jsp_states

master_logger = LoggerFactory.build_logger('master', constants.MASTER_LOG)
filetype = '.csv'
scrape_service = ScrapeService(master_logger, filetype)
threading_service = ThreadService(states, master_logger, scrape_service)
def single_state(states, state):
    url = api_handler.get_url(state)
    scrape_service.scrape_state(state, states[state], url)

def all_states(states):
    threading_service.start_threading(states)

if __name__ == '__main__':
    single_state(states, 'Arizona')
    # all_states(states)

