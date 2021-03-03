import utils
from utils import clean_data
# import requests
from datetime import timedelta, date
import time
from bs4 import BeautifulSoup
import subprocess
import re
import os
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
from constants import JSP_COL, CSV_COL, SAVE_LOCATION




def clean_html(raw_html):
    #Removes problematic tags
    html = re.sub(r'<.*center>', '', raw_html)
    return html


def get_html(start, end):
    #Scrapes HTML, here you put the selenium crawling:
    url = utils.url_with_date(start, end)
    print("Scraping dates: " + start + " to " + end)
    print("URL: " + url)
    #Uncomment below to use selenium, I think this is all you need.
    #All you do in this method is get the HTML
    # driver.get(url)
    # html = driver.execute_script("return document.documentElement.outerHTML ")

    result = subprocess.run(['curl', '-s', url], stdout=subprocess.PIPE)
    raw_html = result.stdout.decode('utf-8')
    html = clean_html(raw_html)
    return html

def get_jsp_rows(html):
    soup = BeautifulSoup(html, 'html.parser')
    table = soup.select_one('#AutoNumber8')
    rows = table.findAll(lambda tag: tag.name == 'tr')
    return rows


def clean_jsp_headers(headers, default_headers):
    #provide header list
    headers = [clean_data(ele.text) for ele in headers if clean_data(ele.text) in default_headers]
    # headers.sort()
    print(headers)
    return headers

def clean_analytes(rows):
    analytes = []
    for row in rows:
        cols = row.find_all('td')
        clean_row = []
        for ele in cols:
            data = clean_data(ele.text)
            #Checks for duplicates
            matches = set(id_list).intersection(set([data]))
            if len(matches) == 0:
                if data:
                    clean_row.append(data)
            else:
                #Uncomment to log duplicates found
                # print("Duplicate: " + data)
                # index_dup = id_list.index(data)
                # print("Index of duplicate: " + str(index_dup))
                # print("Value of dup in list: " + id_list[index_dup])
                clean_row = False
                break
        if clean_row:
            analytes.append(clean_row)
    return analytes

def build_analyte_df(data_rows):
    header_row = data_rows.pop(0)
    headers = header_row.find_all('td')
    analytes = clean_analytes(data_rows)
    print("Num unique samples: " + str(len(analytes)))
    analyte_df = pd.DataFrame(analytes)
    if analyte_df.empty is False:
        analyte_df.columns = clean_jsp_headers(headers, JSP_COL)
    return analyte_df

def read_historical():
    print("Reading historical data to check for duplicates...")
    db = pd.read_csv(SAVE_LOCATION)
    if db.empty is False:
        db.columns = CSV_COL
        id_list = list(db['LabSampleNo.'])
    # print(id_list)
    return id_list


date_ranges = utils.date_range(date(1999, 11, 27), date(2020, 12, 30))
#Read in existing data for duplicate check
id_list = []
id_list = read_historical()

# driver = utils.initial_driver()

for start, end in date_ranges:
    # driver.start_client()
    # driver = utils.initial_driver()
    html = get_html(start, end)
    data_rows = get_jsp_rows(html)
    analyte_df = build_analyte_df(data_rows)
    if analyte_df.empty is False:
        analyte_df.to_csv(SAVE_LOCATION, mode='a', header=False)
    else:
        print("Data already exists, skipping...")
    print("Sleeping 1 seconds...")
    # driver.close()
    time.sleep(1)
