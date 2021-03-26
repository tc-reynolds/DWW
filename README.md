# DWW
### A Web Scraping program to gather data across all 50 States
## Install Location
Clone to C: drive

## How to run
python3 run_scrapers.py 

Logging is tracked under;
  - ./log/chem/ or ./log/coli/ or ./log/copper_lead/
  - Any crashing errors will get printed to the console. 
Data is tracked under;
  - ./data/chem/ or ./data/coli/ or ./log/copper_lead/
## DWW Scripts and information
### runscrapers.py
- This file handles logging and building web scrapers for each state. 
- It can be run in either single state mode or multi-threaded statemode by flipping the commented state of the *single_state* function call
or the *start_threading* function call in the __main__ function
- It reads states from the *api_handler.jsp_states* dictionary
### JSPScraper.py
This file handles all standardized DWW websites. Many of the websites follow the exact same format with only slightly different api-endpoints
This file is essentially a web scraping object class, with a constructor that is built by the *runscrapers.py* file
### utils.py
- Data cleaning
- Proper URL's for parsing
- Builds date ranges
- Builds selenium driver
- Ensures proper encoding
- Removes duplicates by list comparison
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
