import utils
from utils import clean_data_unit, ascii_encoding, clean_html, remove_coli_duplicates, remove_chem_duplicates
# import requests
from datetime import timedelta, date
import time
from bs4 import BeautifulSoup
import subprocess
from statistics import median
import re
from tqdm import tqdm
import sys

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


date_ranges = utils.date_range(date(2016, 3, 5), date(2020, 12, 30))
id_list = []
expected_headers = []
driver = utils.initial_driver()


def get_html_curl(start, end, api_endpoint):
    # Scrapes HTML, here you put the selenium crawling:
    url = utils.url_with_date(start, end, constants.ARIZONA_URL, api_endpoint)
    print("Scraping dates: " + start + " to " + end)
    print("URL: " + url)
    result = subprocess.run(['curl', '-s', url], stdout=subprocess.PIPE)
    try:
        raw_html = result.stdout.decode('utf-8')
    except:
        raw_html = result.stdout.decode('latin-1')
        print('EXCEPTION: HTML encoded in latin-1...')
    print("Removing non-ascii characters...")
    ascii_only_html = ascii_encoding(raw_html)
    html = clean_html(ascii_only_html)
    print("HTML clean....")
    return html


def get_html_selenium(start, end):
    url = utils.url_with_date(start, end, constants.ARIZONA_URL, api_endpoint)
    driver.get(url)
    print("Scraping dates: " + start + " to " + end)
    print("URL: " + url)
    html = driver.execute_script("return document.documentElement.outerHTML ")
    return html


def get_rows(html):
    print("Reading rows...")
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.select_one('#AutoNumber8')
    print("Table found.")
    rows = table.findAll(lambda tag: tag.name == 'tr')
    print("Rows read.")
    return rows


def clean_headers(headers, chem_scrape):
    # provide header list
    headers = [clean_data_unit(ele.text) for ele in headers if clean_data_unit(ele.text) in expected_headers]
    if chem_scrape:
        headers.append("SampleHref")
    # headers.sort()
    print(headers)
    return headers


def build_row(cols, chem_scrape):
    clean_row = []
    href = ''
    for ele in cols:
        data = clean_data_unit(ele.text)
        if chem_scrape:
            if ele.a is not None:
                href = constants.ARIZONA_URL + "JSP/" + ele.a['href']
                href = href.replace(' ', '')
        if data:
            clean_row.append(data)
    if chem_scrape:
        clean_row.append(href)
    return clean_row


def clean_analytes(rows):
    print("Cleaning data...")
    analytes = []
    for row in tqdm(rows):
        cols = row.find_all('td')
        clean_row = build_row(cols, chem_scrape)
        analytes.append(clean_row)
    return analytes


def build_analyte_df(data_rows, chem_scrape):
    print("Building dataframe...")
    header_row = data_rows.pop(0)
    headers = header_row.find_all('td')
    headers = clean_headers(headers, chem_scrape)
    print("Headers received.")
    analytes = clean_analytes(data_rows)
    if chem_scrape:
        id1 = headers.index(constants.LAB_SAMPLE)
        analytes = remove_chem_duplicates(id_list, analytes, id1)
    else:
        id1 = headers.index(constants.LAB_SAMPLE)
        id2 = headers.index(constants.ANALYTE_CODE)
        analytes = remove_coli_duplicates(id_list, analytes, id1, id2)
    print("Num unique samples: " + str(len(analytes)))
    analyte_df = pd.DataFrame(analytes)
    if analyte_df.empty is False:
        analyte_df.columns = headers
        print(analyte_df.columns)
    print("Dataframe built.")
    return analyte_df


def read_historical(columns, save_location):
    print("Reading historical data to check for duplicates...")
    db = pd.read_csv(save_location)
    if db.empty is False:
        db.columns = columns
        print(chem_scrape)
        if chem_scrape:
            id_list = db[constants.LAB_SAMPLE]
        else:
            lab_sample = db[constants.LAB_SAMPLE]
            analyte_code = db[constants.ANALYTE_CODE]
            id_list = [str(i) + str(j) for i, j in zip(lab_sample, analyte_code)]
        print("Num Duplicates to check: " + str(len(id_list)))
    return id_list


def main(chem_scrape, api_endpoint, save_location):
    for start, end in date_ranges:
        # Uncomment below code to switch from curl to selenium for web scraping
        # if driver.session_id is None:
        # driver.start_client()
        # html = get_html_selenium(start, end)
        html = get_html_curl(start, end, api_endpoint)
        data_rows = get_rows(html)
        analyte_df = build_analyte_df(data_rows, chem_scrape)
        if analyte_df.empty is False:
            analyte_df.to_csv(save_location, mode='a', header=False)
        else:
            print("Data already exists, skipping...")
        print("Sleeping 1 seconds...")
        # driver.close()
        time.sleep(1)


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print("Call program passed with argument of either CHEM or COLI ")
        print("EXAMPLE: python3 arizona_scraper.py CHEM")
        exit()
    if "COLI" in sys.argv[1]:
        print("COLI SCRAPE")
        chem_scrape = False
        # Read in existing data for duplicate check
        save_location = constants.COLI_SAVE_LOCATION
        api_endpoint = constants.COLIFORM_CALL
        expected_headers = constants.COLIFORM_HEADERS
        csv_headers = constants.CSV_COLIFORM

        id_list = read_historical(csv_headers, save_location)
        main(chem_scrape, api_endpoint, save_location)
    elif "CHEM" in sys.argv[1]:
        print("CHEM SCRAPE")
        save_location = constants.CHEM_SAVE_LOCATION
        chem_scrape = True
        api_endpoint = constants.CHEM_CALL
        expected_headers = constants.CHEM_HEADERS
        csv_headers = constants.CSV_CHEM

        # id_list = read_historical(csv_headers, save_location)
        main(chem_scrape, api_endpoint, save_location)
    else:
        print("Call program passed with argument of either CHEM or COLI ")
        print("EXAMPLE: python3 arizona_scraper.py CHEM")
        exit()
