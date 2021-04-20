# DWW
### A Web Scraping program to gather data across all 50 States
## Install Location
Clone to C: drive

## How to run
python3 run_scrapers.py 

## How to Configure
All configuration is stored underneath config.py.
Change overall date range scraped, how much is scraped per call, and where data is stored here.

General logging is tracked under master.log in the ./log/ directory

Specific logging is tracked under;
  - ./log/chem/ or ./log/coli/ or ./log/copper_lead/
  - Any crashing errors will get printed to the console. 
Data is tracked under;
  - ./data/chem/ or ./data/coli/ or ./log/copper_lead/
## DWW Scripts and information
### run_scrapers.py
- This file starts off all of the services for the scraping class. It uses the scraper_factory.py file to build scrapers,
  and initiates running the scraper objects once built by the factory
- It can be run in either single state mode or multi-threaded statemode by flipping the commented state of the *single_state* function call
or the *start_threading* function call in the __main__ function
- It reads states from the *api_handler.jsp_states* dictionary
### JSPScraper.py
 - Object Class
 - Handles all standardized DWW websites. Many of the websites follow the exact same format with only slightly different api-endpoints
 - Built by the *runscrapers.py* file
### utils.py
Handles all miscellanious ubiquitous tasks
- Data cleaning
- Proper URL's for parsing
- Builds date ranges
- Builds selenium driver
- Ensures proper encoding
- Removes duplicates by list comparison
### config.py
Handles variables that we may want to change
 - Date Range
 - Date Increment
### constants.py
 This file handles all unchanging constants that are not stored data. These keys include;
  - keywords like "Coliform"
  - ID's for each respective scraped row
  - log file paths
  - data file paths
  - Expected headers for each given table
### api_handler.py
 - All API endpoints and URL's for each state is stored here in different python dictionaries
 - Standardized states are in the jsp_states dictionary
### scraper_factory.py
 - Static Class
 - Builds scraper objects and returns them to the *run_scrapers.py* class

### logger_factory.py 
 - Static Class
 - Builds logger objects to handle logging for web_scraper objects

--------------------------------------

## Author: Tim Reynolds
## Co-Author: Wes Austin
###Github: github.com/tc-reynolds
###Email: timothyreynolds.cs@gmail.com

---------------------------------------


###MIT License

Copyright (c) 2021 Timothy Cooper Reynolds

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.