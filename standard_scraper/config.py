from datetime import date

#-Change this variable to wherever you want logging/data to read/write to
BASE_DIR = '/mnt/d/DWW/standard_scraper/'
#------------------------------------------------------------------------
#-Change these variables for dates scraped or range scraped at a time
DATE_INCREMENT = 30  # Days
START_DATE = date(1999, 1, 1)
END_DATE = date.today()
#-------------------------------------------------------------------------
#-Change this to determine how many states we will scrape concurrently
THREADING_THRESHOLD = 20
#--------------------------------------------------------------------------