import pandas as pd
import os
import colorama
import time
import re
from pathlib import Path
from datetime import timedelta, date
from dateutil.relativedelta import relativedelta
from requests_html import HTMLSession
from bs4 import BeautifulSoup

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

import numpy as np
import constants
import config

from random import randint


def clean_data_unit(data):
    data = data.strip()
    data = data.replace('\r', '')
    data = data.replace('\n', '')
    data = " ".join(data.split())
    return data

def clean_data_unit_no_spaces(data):
    data = clean_data_unit(data)
    data = data.replace(' ', '')
    return data


def clean_html(raw_html):
    # Removes problematic tags
    html = re.sub(r'<.*center>', '', raw_html)
    return html


def remove_duplicates_two_ids(checklist, scraped_list, id1, id2):
    columns = list(zip(*scraped_list))  # Transpose rows to columns
    # print(scraped_list)
    # print(len(columns))
    sample_id_list = list(columns[id1])  # Gets only the id column
    analyte_id_list = list(columns[id2])
    zip_list = zip(sample_id_list, analyte_id_list)
    combined_list = [i + j for i, j in zip_list]
    unique_list = list_comparison(checklist, scraped_list, combined_list)
    return unique_list


# Remove duplicates based on ID
def remove_duplicates_one_id(checklist, scraped_list, id_index):
    columns = list(zip(*scraped_list))  # Transpose rows to columns
    sample_id_list = list(columns[id_index])  # Gets only the id column
    unique_list = list_comparison(checklist, scraped_list, sample_id_list)
    return unique_list


def list_comparison(checklist, scraped_list, sample_id_list):
    matches = set(checklist).intersection(sample_id_list)  # Compares for duplicate values
    for match in matches:
        match_index = sample_id_list.index(match)  # Gets row number of duplicates
        del scraped_list[match_index]
        del sample_id_list[match_index]
    # print(str(len(matches)) + " duplicates removed | " + str(len(scraped_list)) + " unique data points")

    return scraped_list


def ascii_encoding(data):
    encoded_string = data.encode("ascii", "ignore")
    data = encoded_string.decode()
    return data


def date_range(start_date, end_date):
    date_range_tup = []
    end_range = start_date + timedelta(days=config.DATE_INCREMENT)
    while end_range <= end_date:
        start_date_str = start_date.strftime("%m/%d/%Y")
        end_range_str = end_range.strftime("%m/%d/%Y")
        date_range_tup.append((start_date_str, end_range_str))
        start_date = start_date + timedelta(days=config.DATE_INCREMENT)
        end_range = start_date + timedelta(days=config.DATE_INCREMENT)
    return date_range_tup


def url_with_date(start_date, end_date, url, api_endpoint):
    api_call = api_endpoint.replace('STARTING_DATE', start_date)
    api_call = api_call.replace('ENDING_DATE', end_date)
    return url + api_call

def check_dirs():
    #If you don't have logging or data directories locally, this generates them for you
    dir_ls = [
        constants.DATA_DIR,
        constants.LOG_DIR,
        constants.COPPER_LEAD_LOG_DIR,
        constants.CHEM_LOG_DIR,
        constants.COLI_LOG_DIR,
        constants.COPPER_LEAD_DATA_DIR,
        constants.CHEM_DATA_DIR,
        constants.COLI_DATA_DIR,
    ]
    for dir in dir_ls:
        if not os.path.exists(dir):
            os.makedirs(os.path.normpath(dir))

def initial_driver():
    options = Options()
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--mute-audio")
    options.add_argument('--no-sandbox')
    options.add_argument("headless")
    options.add_argument("--log-level=3")
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument("--disable-extensions")
    options.add_argument("test-type")
    # options.add_argument("start-maximized")
    options.add_argument("enable-automation")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-browser-side-navigation")
    options.add_argument("--disable-gpu")
    # options.binary_location("/mnt/c/Program Files/Mozilla Firefox/firefox.exe")
    driver = webdriver.Chrome(executable_path=ChromeDriverManager().install(), options=options)
    # browser = webdriver.Firefox(executable_path="/mnt/c/Users/Tim/geckodriver")

    driver.implicitly_wait(15)
    return driver
