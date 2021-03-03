DATE_INCREMENT = 15 #Days
ARIZONA_URL = 'https://azsdwis.azdeq.gov/DWW_EXT/'
JSP_CALL = 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All&SourceWaterType=All&SampleType=ColiformSample&begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
JSP_COL = ['PrincipalCountyServed', 'WaterSystemNo.',
           'WaterSystemName', 'Type', 'LabSampleNo.',
           'CollectionDate&Time', 'Presence/AbsenceIndicator',
           'AnalyteCode', 'AnalyteName',
           'MonitoringPeriodBeginDate', 'MonitoringPeriodEndDate']
CSV_COL = ['UUID', 'PrincipalCountyServed', 'WaterSystemNo.',
           'WaterSystemName', 'Type', 'LabSampleNo.',
           'CollectionDate&Time', 'Presence/AbsenceIndicator',
           'AnalyteCode', 'AnalyteName',
           'MonitoringPeriodBeginDate', 'MonitoringPeriodEndDate']
SAVE_LOCATION = '/mnt/c/Water-Scraper/DWW/arizona/data/Coliform.csv'