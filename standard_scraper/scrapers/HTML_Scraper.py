from utils import clean_data_unit, ascii_encoding,\
    clean_html, remove_duplicates_two_ids, \
    remove_duplicates_one_id, clean_data_unit_no_spaces
import time
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
import csv

class HTML_Scraper:
    def __init__(self):
        pass
    def get_html_requests(self, url, first_try):
        self.logger.info("URL: " + url)
        try:
            result = requests.get(url)
            status_code = result.status_code
            if status_code == 200:
                html = clean_html(result.text)
                return html
            else:
                error = "Bad HTTP Response: %s" + str(status_code)
                if first_try:
                    html = self.handle_connection_error(url, True, error)
                    return html
                else:
                    self.logger.error(error)
                    return False
        except (ConnectionError,ChunkedEncodingError,
                ProtocolError,IncompleteRead) as e:
            #Retry after sleep for 2 seconds, if retry fails, exit
            if first_try:
                self.logger.warning("First try connecting... Trying again...")
                return self.handle_connection_error(url, first_try=True, error=e)
            else:
                return self.handle_connection_error(url, first_try=False, error=e)


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
            self.logger.error(error)
            self.logger.warning("No connection made, retrying....")
            time.sleep(2)
            html = self.get_html_requests(url, first_try=False)
            return html
        else:
            self.logger.error(error)
            self.logger.error("No connection can be made.... Exiting...")
            exit()