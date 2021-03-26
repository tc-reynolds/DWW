import utils
from utils import clean_data_unit, ascii_encoding, clean_html, remove_duplicates_two_ids, remove_duplicates_one_id
import time
from bs4 import BeautifulSoup
import subprocess
import requests

import numpy as np

import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import constants


class Web_Scraper:
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

    def get_html_requests(self, start, end):
        url = utils.url_with_date(start, end, self.url, self.api_endpoint)
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
        except requests.exceptions.ConnectionError as e:
            self.logger.error(e)
            self.logger.error("No connection can be made.... Exiting...")
            exit()


    def get_html_curl(self, start, end):
        # Scrapes HTML, here you put the selenium crawling:
        url = utils.url_with_date(start, end, self.url, self.api_endpoint)
        # print(url)
        self.logger.info("Scraping dates: " + start + " to " + end)
        self.logger.info("URL: " + url)
        result = subprocess.run(['curl', '-s', url], stdout=subprocess.PIPE)
        try:
            raw_html = result.stdout.decode('utf-8')
        except:
            raw_html = result.stdout.decode('latin-1')
            self.logger.error('EXCEPTION: HTML encoded in latin-1...')
        self.logger.info("Removing non-ascii characters...")
        ascii_only_html = ascii_encoding(raw_html)
        html = clean_html(ascii_only_html)
        self.logger.info("HTML clean....")
        return html

    def get_html_selenium(self, start, end, api_endpoint):
        if driver.session_id is None:
            driver.start_client()
        url = utils.url_with_date(start, end, self.url, api_endpoint)
        driver.get(url)
        self.logger.info("Scraping dates: " + start + " to " + end)
        self.logger.info("URL: " + url)
        html = driver.execute_script("return document.documentElement.outerHTML ")
        # driver.close()
        return html

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
            new_header = clean_data_unit(ele.text)
            for expected_header in self.expected_headers:
                if new_header in expected_header:
                    parsed_headers.append(expected_header)
                    break;
        if self.chem_scrape == 'CHEM':
            parsed_headers.append("SampleHref")
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
        #Removes all duplicates, builds unique id for each row of data
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

    def build_analyte_df(self, data_rows):
        self.logger.info("Building dataframe...")
        header_row = data_rows.pop(0)
        headers = header_row.find_all('td')
        headers = self.clean_headers(headers)
        self.logger.info("Headers received.")
        analytes = self.clean_analytes(data_rows)
        if len(self.id_list) > 0 and len(analytes) > 0:
            analytes = self.parse_duplicate_analytes(headers, analytes)
        self.logger.info("Num unique samples: " + str(len(analytes)))
        analyte_df = pd.DataFrame(analytes)
        if analyte_df.empty is False:
            # print(analytes[0])
            # print(headers)
            analyte_df.columns = headers
            self.logger.info(analyte_df.columns)
        self.logger.info("Dataframe built.")
        return analyte_df

    def read_csv(self):
        try:
            db = pd.read_csv(self.save_location, header=None)
            return db
        except pd.errors.EmptyDataError:
            self.logger.error(self.save_location, " is empty")
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

    def scrape(self):
        #Starts all scraping for object across date range
        for start, end in self.date_ranges:
            # Uncomment below code to switch from curl to selenium for web scraping
            # html = get_html_selenium(start, end)
            # html = self.get_html_curl(start, end)
            html = self.get_html_requests(start, end)
            data_rows = self.get_rows(html)
            if len(data_rows) > 0:
                analyte_df = self.build_analyte_df(data_rows)
                if analyte_df.empty is False:
                    analyte_df.to_csv(self.save_location, mode='a', header=False)
            else:
                self.logger.info("No unique data found...")
            self.logger.info("Sleeping 1 seconds...")
            time.sleep(1)
        self.logger.info("Scraping finished....")
