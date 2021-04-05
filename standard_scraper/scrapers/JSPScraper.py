import utils
from utils import clean_data_unit, ascii_encoding,\
    clean_html, remove_duplicates_two_ids, \
    remove_duplicates_one_id, clean_data_unit_no_spaces
import time
from bs4 import BeautifulSoup
import subprocess
import requests
from requests.exceptions import ConnectionError, ChunkedEncodingError
import numpy as np
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from urllib3.exceptions import ProtocolError
from http.client import IncompleteRead

import pandas as pd
import constants


class WebScraper:
    # driver = utils.initial_driver()
    def __init__(self, url, expected_headers, csv_headers, chem_scrape, save_location, logger, date_ranges, api_endpoint):
        self.url = url
        self.expected_headers = expected_headers
        self.csv_headers = csv_headers
        self.chem_scrape = chem_scrape
        self.logger = logger
        self.save_location = save_location
        self.date_ranges = date_ranges
        self.api_endpoint = api_endpoint
        self.id_list = self.read_historical()
        # self.id_list = []
    def get_html_requests(self, url, first_try):
        self.logger.info("URL: " + url)
        try:
            result = requests.get(url)
            status_code = result.status_code
            if status_code == 200:
                html = clean_html(result.text)
                return html
            else:
                self.logger.error("Bad HTTP Response: %s", status_code)
                exit()
        except (ConnectionError,ChunkedEncodingError,
                ProtocolError,IncompleteRead) as e:
            #Retry after sleep for 2 seconds, if retry fails, exit
            if first_try:
                self.logger.error(e)
                self.logger.warning("First try connecting... Trying again...")
                self.handle_connection_error(url, first_try=False, error=e)
            else:
                self.logger.error(e)



    def get_html_curl(self, url):
        # Scrapes HTML, here you put the selenium crawling:
        self.logger.info("URL: " + url)
        result = subprocess.run(['curl', '-s', url], stdout=subprocess.PIPE)
        try:
            raw_html = result.stdout.decode('utf-8')
        except:
            raw_html = result.stdout.decode('latin-1')
            self.logger.warning('HTML encoded in latin-1...')
        self.logger.info("Removing non-ascii characters...")
        ascii_only_html = ascii_encoding(raw_html)
        html = clean_html(ascii_only_html)
        self.logger.info("HTML clean....")
        return html

    def get_html_selenium(self, url):
        if driver.session_id is None:
            driver.start_client()
        driver.get(url)
        self.logger.info("URL: " + url)
        html = driver.execute_script("return document.documentElement.outerHTML ")
        # driver.close()
        return html

    def handle_connection_error(self, url, first_try, error):
        self.logger.info("Handling exception for connection...")
        self.logger.info(f"First Try: {first_try!s}")
        if first_try:
            self.logger.warning("No connection made, retrying....")
            time.sleep(2)
            self.get_html_requests(url, first_try=False)
        else:
            self.logger.error(error)
            self.logger.error("No connection can be made.... Exiting...")
            exit()

    def get_rows(self, html):
        rows = []
        try:
            self.logger.info("Reading rows...")
            soup = BeautifulSoup(html, 'html.parser')
            table = soup.select_one('#AutoNumber8')
            self.logger.info("Table found.")
            rows = table.findAll(lambda tag: tag.name == 'tr')
            self.logger.info("Rows read.")
        except:
            self.logger.error("ERROR: No data found, no rows to parse")
        return rows


    def clean_headers(self, headers):
        # Provide header list
        parsed_headers = []
        for ele in headers:
            new_header = clean_data_unit_no_spaces(ele.text)
            for expected_header in self.expected_headers:
                if new_header in expected_header:
                    parsed_headers.append(expected_header)
                    break;
        self.logger.info(parsed_headers)
        return parsed_headers

    def build_row(self, cols):
        clean_row = []
        href = ''
        for i, ele in enumerate(cols):
            data = clean_data_unit(ele.text)
            if self.chem_scrape == 'CHEM':
                if ele.a is not None:
                    href = self.url + "JSP/" + ele.a['href']
                    href = href.replace(' ', '')
            if data or i < len(self.expected_headers) - 1:
                if data == '':
                    data = 'NULL'
                clean_row.append(data)
        if self.chem_scrape == 'CHEM':
            clean_row.append(href)
        return clean_row

    def clean_analytes(self, rows):
        self.logger.info("Cleaning data...")
        analytes = []
        for row in rows:
            cols = row.find_all('td')
            clean_row = self.build_row(cols)
            analytes.append(clean_row)
        return analytes

    def parse_duplicate_analytes(self, headers, analytes):
        #Remove all duplicates, build unique id for each row of data
        if self.chem_scrape == 'CHEM':
            id1 = headers.index(constants.LAB_SAMPLE)
            analytes = remove_duplicates_one_id(self.id_list, analytes, id1)
        elif self.chem_scrape == 'COPPER_LEAD':
            id1 = headers.index(constants.WATER_SYSTEMS_NO)
            id2 = headers.index(constants.ANALYTE)
            analytes = remove_duplicates_two_ids(self.id_list, analytes, id1, id2)
        elif self.chem_scrape == 'COLI':
            id1 = headers.index(constants.LAB_SAMPLE)
            id2 = headers.index(constants.ANALYTE_CODE)
            analytes = remove_duplicates_two_ids(self.id_list, analytes, id1, id2)
        return analytes

    def remove_markup(self, data_rows):
        #Removes HTML from rows and headers
        header_row = data_rows.pop(0)
        headers = header_row.find_all('td')
        headers = self.clean_headers(headers)
        self.logger.info("Headers received.")
        analytes = self.clean_analytes(data_rows)
        return headers, analytes

    def build_analyte_df(self, headers, analytes):
        self.logger.info("Num unique samples: " + str(len(analytes)))
        analyte_df = pd.DataFrame(analytes)
        if analyte_df.empty is False:
            analyte_df.columns = headers
            self.logger.info(analyte_df.columns)
        self.logger.info("Dataframe built.")
        return analyte_df

    def read_csv(self):
        try:
            db = pd.read_csv(self.save_location, header=None)
            return db
        except pd.errors.EmptyDataError:
            self.logger.error("%s is empty", self.save_location)
            return None
        except IOError:
            self.logger.error("File does not exist")
            return None

    def read_historical(self):
        self.logger.info("Reading historical data to check for duplicates...")
        db = self.read_csv()
        id_list = []
        if db is not None:
            if db.empty is False:
                db.columns = self.csv_headers
                if self.chem_scrape == 'CHEM':
                    id_list = db[constants.LAB_SAMPLE]
                elif self.chem_scrape == 'COPPER_LEAD':
                    water_system_no = db[constants.WATER_SYSTEMS_NO]
                    analyte_name = db[constants.ANALYTE]
                    id_list = [str(i) + str(j) for i, j in zip(water_system_no, analyte_name)]
                elif self.chem_scrape == 'COLI':
                    lab_sample = db[constants.LAB_SAMPLE]
                    analyte_code = db[constants.ANALYTE_CODE]
                    id_list = [str(i) + str(j) for i, j in zip(lab_sample, analyte_code)]
                self.logger.info("Num Duplicates to check: " + str(len(id_list)))

        return id_list

    def clean_href_data(self, href_analytes, lab_sample_value):
        for i, analyte_row in enumerate(href_analytes):
            analyte_row = [data.strip() for i, data in enumerate(analyte_row)
                           if i < len(constants.CHEM_HREF_HEADERS) - 1]
            for j, data in enumerate(analyte_row):
                if data == '':
                    analyte_row[j] = 'NULL'
            analyte_row.insert(0, lab_sample_value)
            for k in range(len(analyte_row), len(constants.CHEM_HREF_HEADERS)):
                analyte_row.append('NULL')
            href_analytes[i] = analyte_row
        return href_analytes


    def store_href_table(self, headers, analytes):
        total_href_analytes = []
        href_headers = []
        for i, row in enumerate(analytes):
            url = row[len(row) - 1]
            analytes[i].pop()
            html = self.get_html_requests(url, first_try=True)
            href_rows = self.get_rows(html)
            href_headers, href_analytes = self.remove_markup(href_rows)
            ls_index = self.expected_headers.index(constants.LAB_SAMPLE)
            lab_sample_value = analytes[i][ls_index]
            href_analytes = self.clean_href_data(href_analytes, lab_sample_value)
            total_href_analytes.extend(href_analytes)
            save_location = self.save_location.replace('Chem_', 'Chem_Table_')
            time.sleep(1)
        if len(total_href_analytes) > 0:
            self.write_to_csv(constants.CHEM_HREF_HEADERS, total_href_analytes, save_location)
        return analytes


    def write_to_csv(self, headers, analytes, save_location):
        if len(analytes) > 0:
            analyte_df = self.build_analyte_df(headers, analytes)
            if analyte_df.empty is False:
                analyte_df.to_csv(save_location, mode='a', header=False)
        else:
            self.logger.info("No unique data found...")

    def scrape(self):
        #Starts all scraping for object across date range
        for start, end in self.date_ranges:
            url = utils.url_with_date(start, end, self.url, self.api_endpoint)
            # Uncomment below code to switch from curl to selenium for web scraping
            # html = get_html_selenium(url)
            # html = self.get_html_curl(url)
            html = self.get_html_requests(url, first_try=True)
            data_rows = self.get_rows(html)
            headers, analytes = self.remove_markup(data_rows)
            if len(self.id_list) > 0 and len(analytes) > 0:
                analytes = self.parse_duplicate_analytes(headers, analytes)
            if self.chem_scrape == 'CHEM':
                self.logger.info("Storing href_links")
                analytes = self.store_href_table(headers, analytes)

            self.write_to_csv(headers, analytes, self.save_location)

            self.logger.info("Sleeping 1 seconds...")
            time.sleep(1)
        self.logger.info("Scraping finished....")
