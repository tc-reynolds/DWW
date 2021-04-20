import constants
import api_handler
from datetime import date, datetime
from dateutil.parser import parse
import threading
from threading import Thread, ThreadError
from factories.logger_factory import LoggerFactory
from scrapers.JSPScraper import WebScraper
import config
import os


class ScraperFactory:

    def read_date_range(state, chem_scrape):
        start_date = ""
        state_filename = constants.DATE_STATE_FILENAME.replace("STATE_NAME", chem_scrape + "_" + state)
        try:
            with open(state_filename, "r") as state_file:
                start_date = state_file.readline()
                if str(start_date) == '':
                    return (config.START_DATE, config.END_DATE)
                start_date = parse(start_date)
                start_date = start_date.date()
                return start_date, config.END_DATE
        except:
            return (config.START_DATE, config.END_DATE)

    @staticmethod
    def copper_lead_scraper(state, url, filetype):
        chem_scrape = 'COPPER_LEAD'
        # Read in existing data for duplicate check
        save_location = constants.COPPER_LEAD_SAVE_LOCATION + state + filetype
        log_location = constants.COPPER_LEAD_LOG_LOCATION + state + '.log'
        log_name = state + '_copper_lead'
        logger = LoggerFactory.build_logger(log_name, log_location)
        api_endpoint = api_handler.get_copper_lead_call(state)
        expected_headers = constants.COPPER_LEAD_HEADERS
        csv_headers = constants.CSV_COPPER_LEAD
        date_ranges = ScraperFactory.read_date_range(state, chem_scrape)
        web_scraper = WebScraper(url, expected_headers, csv_headers,
                                 chem_scrape, save_location, logger,
                                 date_ranges, api_endpoint, state)
        return web_scraper

    @staticmethod
    def chem_scraper_arizona():
        pass

    @staticmethod
    def chem_scraper(state, url, filetype):
        save_location = constants.CHEM_SAVE_LOCATION + state + filetype
        log_location = constants.CHEM_LOG_LOCATION + state + '.log'
        log_name = state + '_copper_lead'
        logger = LoggerFactory.build_logger(log_name, log_location)
        chem_scrape = 'CHEM'
        api_endpoint = api_handler.get_chem_call(state)
        expected_headers = constants.CHEM_HEADERS
        csv_headers = constants.CSV_CHEM
        date_ranges = ScraperFactory.read_date_range(state, chem_scrape)
        web_scraper = WebScraper(url, expected_headers, csv_headers,
                                 chem_scrape, save_location, logger,
                                 date_ranges, api_endpoint, state)
        return web_scraper

    @staticmethod
    def coli_scraper(state, url, filetype):
        chem_scrape = 'COLI'
        # Read in existing data for duplicate check
        save_location = constants.COLI_SAVE_LOCATION + state + filetype
        log_location = constants.COLI_LOG_LOCATION + state + '.log'
        log_name = state + '_copper_lead'
        logger = LoggerFactory.build_logger(log_name, log_location)

        api_endpoint = api_handler.get_coli_call(state)
        expected_headers = constants.COLIFORM_HEADERS
        csv_headers = constants.CSV_COLIFORM
        date_ranges = ScraperFactory.read_date_range(state, chem_scrape)
        web_scraper = WebScraper(url, expected_headers, csv_headers,
                                 chem_scrape, save_location, logger,
                                 date_ranges, api_endpoint, state)
        return web_scraper
