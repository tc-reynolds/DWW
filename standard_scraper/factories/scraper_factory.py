import constants
import api_handler
from datetime import date
import threading
from threading import Thread, ThreadError
from factories.logger_factory import LoggerFactory
from scrapers.JSPScraper import WebScraper
import os

class ScraperFactory:

    @staticmethod
    def copper_lead_scraper(state, url, date_ranges, filetype):
        chem_scrape = 'COPPER_LEAD'
        # Read in existing data for duplicate check
        save_location = constants.COPPER_LEAD_SAVE_LOCATION + state + filetype
        log_location = constants.COPPER_LEAD_LOG_LOCATION + state + '.log'
        log_name = state + '_copper_lead'
        logger = LoggerFactory.build_logger(log_name, log_location)

        api_endpoint = api_handler.get_copper_lead_call(state)
        expected_headers = constants.COPPER_LEAD_HEADERS
        csv_headers = constants.CSV_COPPER_LEAD
        web_scraper = WebScraper(url, expected_headers, csv_headers,
                                 chem_scrape, save_location, logger,
                                 date_ranges, api_endpoint, state)
        return web_scraper

    @staticmethod
    def chem_scraper_arizona():
        pass
    @staticmethod
    def chem_scraper(state, url, date_ranges, filetype):
        save_location = constants.CHEM_SAVE_LOCATION + state + filetype
        log_location = constants.CHEM_LOG_LOCATION + state + '.log'
        log_name = state + '_copper_lead'
        logger = LoggerFactory.build_logger(log_name, log_location)
        chem_scrape = 'CHEM'
        api_endpoint = api_handler.get_chem_call(state)
        expected_headers = constants.CHEM_HEADERS
        csv_headers = constants.CSV_CHEM
        web_scraper = WebScraper(url, expected_headers, csv_headers,
                                 chem_scrape, save_location, logger,
                                 date_ranges, api_endpoint, state)
        return web_scraper

    @staticmethod
    def coli_scraper(state, url, date_ranges, filetype):
        chem_scrape = 'COLI'
        # Read in existing data for duplicate check
        save_location = constants.COLI_SAVE_LOCATION + state + filetype
        log_location = constants.COLI_LOG_LOCATION + state + '.log'
        log_name = state + '_copper_lead'
        logger = LoggerFactory.build_logger(log_name, log_location)

        api_endpoint = api_handler.get_coli_call(state)
        expected_headers = constants.COLIFORM_HEADERS
        csv_headers = constants.CSV_COLIFORM
        web_scraper = WebScraper(url, expected_headers, csv_headers,
                                 chem_scrape, save_location, logger,
                                 date_ranges, api_endpoint, state)
        return web_scraper

