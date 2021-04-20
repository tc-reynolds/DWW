import utils
from utils import clean_data_unit, ascii_encoding,\
    clean_html, clean_data_unit_no_spaces
import constants
from scrapers.HTML_Scraper import HTML_Scraper
import time
from bs4 import BeautifulSoup


import pandas as pd

class WebScraper:
    # driver = utils.initial_driver()
    def __init__(self, url, expected_headers, csv_headers, chem_scrape, save_location, logger, date_ranges, api_endpoint, state):
        self.url = url
        self.expected_headers = expected_headers
        self.csv_headers = csv_headers
        self.chem_scrape = chem_scrape
        self.logger = logger
        self.save_location = save_location
        self.api_endpoint = api_endpoint
        self.state = state
        self.id_list = self.read_historical()
        self.last_date_scraped = date_ranges[0]
        self.date_ranges = utils.date_range(self.last_date_scraped, date_ranges[1])
        self.html_scraper = HTML_Scraper(self.logger)

    def save_last_scraped_date(self):
        state_filename = constants.DATE_STATE_FILENAME.replace("STATE_NAME", self.chem_scrape + "_" + self.state)
        self.logger.info(state_filename)
        file1 = open(state_filename, "w")  # write mode
        file1.write(str(self.last_date_scraped))
        self.logger.info("LATEST DATE SCRAPED: %s", self.last_date_scraped)
        file1.close()



    def remove_duplicate_analytes(self, headers, analytes):
        #Remove all duplicates, build unique id for each row of data
        is_empty = False
        analytes = utils.list_comparison(self.id_list, analytes, self.logger)
        if len(analytes) == 0:
            is_empty = True
        return analytes, is_empty

    def remove_markup(self, data_rows, expected_headers):
        #Removes HTML from rows and headers
        header_row = data_rows.pop(0)
        headers = header_row.find_all('td')
        headers = self.clean_headers(headers, expected_headers)
        self.logger.info("Headers received.")
        analytes = self.clean_analytes(data_rows)
        return headers, analytes

    def build_analyte_df(self, headers, analytes):
        analyte_df = pd.DataFrame(analytes)
        if analyte_df.empty is False:
            self.logger.info(headers)
            analyte_df.columns = headers
            self.logger.info(analyte_df.columns)
        self.logger.info("Dataframe built.")
        return analyte_df

    def read_csv(self):
        try:
            db = pd.read_csv(self.save_location, header=None)
            with open(self.save_location) as f:
                reader = csv.reader(f)
                db = list(reader)
                return db
        except pd.errors.EmptyDataError:
            self.logger.error("%s is empty", self.save_location)
            return None
        except IOError:
            self.logger.error("File does not exist")
            return None

    def read_historical(self):
        self.logger.info("Reading historical data to check for duplicates...")
        id_list = self.read_csv()
        if id_list is not None:
            self.logger.info("Num Duplicates to check: " + str(len(id_list)))
            for i, row in enumerate(id_list):
                id_list[i] = str(row[1:])
        else:
            id_list = []
        return id_list

    def clean_href_data(self, href_analytes, lab_sample_value):
        for i, analyte_row in enumerate(href_analytes):
            analyte_row = [data.strip() for i, data in enumerate(analyte_row)
                           if i < len(constants.CHEM_HREF_HEADERS) - 1]
            for j, data in enumerate(analyte_row):
                if data == '':
                    analyte_row[j] = 'NULL'
            analyte_row.insert(0, lab_sample_value)
            #Fill null if no data found or row mismatch.
            for k in range(len(analyte_row), len(constants.CHEM_HREF_HEADERS)):
                analyte_row.append('NULL')
            href_analytes[i] = analyte_row
        return href_analytes

    def build_href_analytes(self, href_rows, lab_sample_value):
        href_headers, href_analytes = self.remove_markup(href_rows, constants.CHEM_HREF_HEADERS)
        self.logger.info("Num HREF analytes found; %s", str(len(href_analytes)))
        href_analytes = self.clean_href_data(href_analytes, lab_sample_value)
        return href_headers, href_analytes


    def store_href_table(self, headers, analytes):
        self.logger.info("Looping through hrefs to store CHEM tables..")
        total_href_analytes = []
        href_headers = []
        self.logger.info("%s links to process...", str(len(analytes)))
        for i, row in enumerate(analytes):
            self.logger.info("%s links left...", str(len(analytes) - i))
            url = analytes[i].pop()
            html = self.html_scraper.get_html_requests(url, first_try=True)
            if html is False:
                continue
            href_rows = self.get_rows(html)
            if len(href_rows) > 0:
                lab_sample_index = self.expected_headers.index(constants.LAB_SAMPLE)
                lab_sample_num = analytes[i][lab_sample_index]
                href_headers, href_analytes = self.build_href_analytes(href_rows, lab_sample_num)
                total_href_analytes.extend(href_analytes)
            self.logger.info("Sleeping .1 seconds...")
            time.sleep(.1)
        self.logger.info("Total number of HREF analytes; %s", str(len(total_href_analytes)))
        if len(total_href_analytes) > 0:
            save_location = self.save_location.replace('Chem_', 'Chem_Table_')
            self.write_to_csv(constants.CHEM_HREF_HEADERS, total_href_analytes, save_location)
        return analytes

    def write_to_csv(self, headers, analytes, save_location):
        self.logger.info("Writing to %s", save_location)
        self.logger.info("Num unique samples: " + str(len(analytes)))
        if len(analytes) > 0:
            analyte_df = self.build_analyte_df(headers, analytes)
            if analyte_df.empty is False:
                analyte_df.to_csv(save_location, mode='a', header=False)
        else:
            self.logger.info("No unique data found...")

    def scrape(self):
        #Starts all scraping for object across date range
        for start, end in self.date_ranges:
            self.logger.info("Sleeping 1 seconds...")
            self.last_date_scraped = start
            self.save_last_scraped_date()
            time.sleep(1)
            url = utils.url_with_date(start, end, self.url, self.api_endpoint)
            html = self.html_scraper.get_html_requests(url, first_try=True)
            if html is False:
                continue
            data_rows = self.get_rows(html)
            if len(data_rows) > 0:
                headers, analytes = self.remove_markup(data_rows, self.expected_headers)
                if len(self.id_list) > 0 and len(analytes) > 0:
                    self.logger.info("Total samples: " + str(len(analytes)))
                    analytes, is_empty = self.remove_duplicate_analytes(headers, analytes)
                    self.logger.info("Num unique samples: " + str(len(analytes)))
                    if is_empty:
                        continue
                    if self.chem_scrape == 'CHEM':
                        self.logger.info("Storing href links...")
                        analytes = self.store_href_table(headers, analytes)
                    self.write_to_csv(headers, analytes, self.save_location)


        self.logger.info("Scraping finished....")
