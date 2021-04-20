import api_handler
from config import START_DATE, END_DATE
import utils
from factories.scraper_factory import ScraperFactory
import constants
import config
import os.path
from os import path

class ScrapeService:
    def __init__(self, master_logger, filetype):
        self.master_logger = master_logger
        self.filetype = filetype

    def scrape_copper_lead(self, state, url):
        self.master_logger.info("COPPER/LEAD SCRAPE %s", state)
        web_scraper = ScraperFactory.copper_lead_scraper(state, url, self.filetype)
        web_scraper.scrape()

    def scrape_chem(self, state, url):
        self.master_logger.info("CHEM SCRAPE %s", state)
        web_scraper = ScraperFactory.chem_scraper(state, url, self.filetype)
        web_scraper.scrape()


    def scrape_coli(self, state, url):
        self.master_logger.info("COLI SCRAPE %s", state)
        web_scraper = ScraperFactory.coli_scraper(state, url, self.filetype)
        web_scraper.scrape()


    def scrape_state(self, state, state_dict, url):
        # if state_dict[api_handler.coli] is not None:
        #     self.scrape_coli(state, url)
        # if state_dict[api_handler.chem] is not None:
        #     self.scrape_chem(state, url)
        if state_dict[api_handler.copper_lead] is not None:
            self.scrape_copper_lead(state, url)