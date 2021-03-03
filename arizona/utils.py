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

import constants
from random import randint


def clean_data(data):
    data = data.strip()
    encoded_string = data.encode("ascii", "ignore")
    data = encoded_string.decode()
    data = data.replace('\r', '')
    data = data.replace('\n', '')
    data = re.sub(r'\s*', '', data)
    return data


def date_range(start_date,end_date):
    date_range_tup = []
    end_range = start_date + timedelta(days=constants.DATE_INCREMENT)
    while end_range <= end_date:
        start_date_str = start_date.strftime("%m/%d/%Y")
        end_range_str = end_range.strftime("%m/%d/%Y")
        date_range_tup.append((start_date_str, end_range_str))
        start_date = start_date + timedelta(days=constants.DATE_INCREMENT)
        end_range = start_date + timedelta(days=constants.DATE_INCREMENT)
    return date_range_tup

def url_with_date(start_date, end_date):
    api_call = constants.JSP_CALL.replace('STARTING_DATE', start_date)
    api_call = api_call.replace('ENDING_DATE', end_date)
    return constants.ARIZONA_URL + api_call

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

