import utils
from utils import clean_data_unit, ascii_encoding, clean_html, remove_duplicates
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

date_ranges = utils.date_range(date(1999, 7, 3), date(2020, 12, 30))
id_list = []
api_endpoint = ''
expected_headers = []
save_location = ''
driver = utils.initial_driver()
chem_scrape = False


def get_html_curl(start, end):
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


def clean_headers(headers, default_headers):
    # provide header list
    headers = [clean_data_unit(ele.text) for ele in headers if clean_data_unit(ele.text) in default_headers]
    if chem_scrape:
        headers.append("SampleHref")
    # headers.sort()
    print(headers)
    return headers

def build_row(cols):
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
        clean_row = build_row(cols)
        analytes.append(clean_row)
    return analytes


def build_analyte_df(data_rows, expected_headers):
    print("Building dataframe...")
    header_row = data_rows.pop(0)
    headers = header_row.find_all('td')
    headers = clean_headers(headers, expected_headers)
    print("Headers received.")
    analytes = clean_analytes(data_rows)
    analytes = remove_duplicates(id_list, analytes, headers.index(constants.ID))
    print("Num unique samples: " + str(len(analytes)))
    print(analytes[0])
    print(analytes[1])
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
        id_list = list(db[constants.ID])
        print("Num Duplicates to check: " + str(len(id_list)))
    return id_list


def main():
    for start, end in date_ranges:
        # driver.start_client()
        html = get_html_curl(start, end)
        data_rows = get_rows(html)
        analyte_df = build_analyte_df(data_rows, expected_headers)
        if analyte_df.empty is False:
            analyte_df.to_csv(save_location, mode='a', header=False)
        else:
            print("Data already exists, skipping...")
        print("Sleeping 1 seconds...")
        # driver.close()
        time.sleep(1)

if len(sys.argv) == 1:
    print("Call program passed with argument of either CHEM or COLI ")
    print("EXAMPLE: python3 arizona_scraper.py CHEM")
    exit()
if "COLI" in sys.argv[1]:
    # Read in existing data for duplicate check
    save_location = constants.COLI_SAVE_LOCATION
    id_list = read_historical(constants.CSV_COLIFORM, save_location)
    api_endpoint = constants.COLIFORM_CALL
    expected_headers = constants.COLIFORM_HEADERS
    main()
elif "CHEM" in sys.argv[1]:
    save_location = constants.CHEM_SAVE_LOCATION
    id_list = read_historical(constants.CSV_CHEM, save_location)
    chem_scrape = True
    api_endpoint = constants.CHEM_CALL
    expected_headers = constants.CHEM_HEADERS
    main()
else:
    print("Call program passed with argument of either CHEM or COLI ")
    print("EXAMPLE: python3 arizona_scraper.py CHEM")
    exit()
