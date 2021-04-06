import utils
from utils import clean_data_unit, ascii_encoding,\
    clean_html, remove_duplicates_two_ids, \
    remove_duplicates_one_id, clean_data_unit_no_spaces
import constants
import HTML_Scraper
import time
from bs4 import BeautifulSoup


import pandas as pd


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
        self.html_scraper = HTML_Scraper()
        # self.id_list = []

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


    def clean_headers(self, headers, expected_headers):
        # Provide header list
        parsed_headers = []
        for ele in headers:
            new_header = clean_data_unit_no_spaces(ele.text)
            for expected_header in expected_headers:
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

    def remove_duplicate_analytes(self, headers, analytes):
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
            self.logger.info("Sleeping .5 seconds...")
            time.sleep(.5)
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
            url = utils.url_with_date(start, end, self.url, self.api_endpoint)
            # Uncomment below code to switch from curl to selenium for web scraping
            # html = get_html_selenium(url)
            # html = self.get_html_curl(url)
            html = self.html_scraper.get_html_requests(url, first_try=True)
            if html is False:
                continue
            data_rows = self.get_rows(html)
            if len(data_rows) > 0:
                headers, analytes = self.remove_markup(data_rows, self.expected_headers)
                if len(self.id_list) > 0 and len(analytes) > 0:
                    analytes = self.remove_duplicate_analytes(headers, analytes)
                if self.chem_scrape == 'CHEM':
                    self.logger.info("Storing href links...")
                    analytes = self.store_href_table(headers, analytes)
                self.write_to_csv(headers, analytes, self.save_location)
            self.logger.info("Sleeping 1 seconds...")
            time.sleep(1)

        self.logger.info("Scraping finished....")
