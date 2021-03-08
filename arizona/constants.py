ARIZONA_URL = 'https://azsdwis.azdeq.gov/DWW_EXT/'
COLIFORM_CALL = 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All&SourceWaterType=All&SampleType=ColiformSample&begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
CHEM_CALL = 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All&SourceWaterType=All&SampleType=NonTCRAll&begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
COLI_SAVE_LOCATION = '/mnt/c/Water-Scraper/DWW/arizona/data/Coliform1.csv'
CHEM_SAVE_LOCATION = '/mnt/c/Water-Scraper/DWW/arizona/data/Chem.csv'

DATE_INCREMENT = 15  # Days

COLIFORM_HEADERS = ['PrincipalCountyServed', 'WaterSystemNo.',
                    'WaterSystemName', 'Type', 'LabSampleNo.',
                    'CollectionDate&Time', 'Presence/AbsenceIndicator',
                    'AnalyteCode', 'AnalyteName',
                    'MonitoringPeriodBeginDate', 'MonitoringPeriodEndDate']

CHEM_HEADERS = ['PrincipalCountyServed', 'WaterSystemNo.',
                'WaterSystemName', 'LabSampleNo.',
                'Type', 'CollectionDate&Time', 'SamplingPoint', 'SampleHref']

CSV_COLIFORM = ['UID', 'PrincipalCountyServed', 'WaterSystemNo.',
                'WaterSystemName', 'Type', 'LabSampleNo.',
                'CollectionDate&Time', 'Presence/AbsenceIndicator',
                'AnalyteCode', 'AnalyteName',
                'MonitoringPeriodBeginDate', 'MonitoringPeriodEndDate']

CSV_CHEM = ['UID', 'PrincipalCountyServed', 'WaterSystemNo.',
                'WaterSystemName', 'LabSampleNo.',
                'Type', 'CollectionDate&Time',
                'SamplingPoint', 'SampleHref']

ID = 'LabSampleNo.'
COLI_CODE = 'AnalyteCode'
