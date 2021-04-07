from config import BASE_DIR

DATA_DIR = BASE_DIR + 'data/'
LOG_DIR = BASE_DIR + 'log/'

DATE_DIR = BASE_DIR + 'last_date_scraped/'
DATE_STATE_FILENAME = DATE_DIR + 'STATE_NAME.txt'
COLI_DATA_DIR = BASE_DIR + 'data/coli/'
CHEM_DATA_DIR = BASE_DIR + 'data/chem/'
COPPER_LEAD_DATA_DIR = BASE_DIR + 'data/copper_lead/'

COLI_LOG_DIR = LOG_DIR + 'coli/'
CHEM_LOG_DIR = LOG_DIR + 'chem/'
COPPER_LEAD_LOG_DIR = LOG_DIR + 'copper_lead/'


COLI_SAVE_LOCATION =  COLI_DATA_DIR + 'Coliform_'
CHEM_SAVE_LOCATION = CHEM_DATA_DIR + 'Chem_'
CHEM_TABLE_SAVE_LOCATION = CHEM_DATA_DIR + 'Chem_Table_'
COPPER_LEAD_SAVE_LOCATION = COPPER_LEAD_DATA_DIR + 'Copper_Lead_'

COLI_LOG_LOCATION = COLI_LOG_DIR + 'Coliform_'
CHEM_LOG_LOCATION = CHEM_LOG_DIR + 'Chem_'
COPPER_LEAD_LOG_LOCATION = COPPER_LEAD_LOG_DIR + 'Copper_Lead_'

MASTER_LOG = LOG_DIR + 'master.log'



COLIFORM_HEADERS = ['PrincipalCountyServed', 'WaterSystemNo.',
                    'WaterSystemName', 'Type', 'LabSampleNo.',
                    'CollectionDate&Time', 'Presence/AbsenceIndicator',
                    'AnalyteCode', 'AnalyteName',
                    'MonitoringPeriodBeginDate', 'MonitoringPeriodEndDate']

CHEM_HEADERS = ['PrincipalCountyServed', 'WaterSystemNo.',
                'WaterSystemName', 'LabSampleNo.',
                'Type', 'CollectionDate&Time',
                'SamplingPoint']

CHEM_HREF_HEADERS = ['SamplingPoint', 'AnalyteCode','AnalyteName','MethodCode',
                    'LessthanIndicator','LevelType','ReportingLevel',
                    'Concentrationlevel','MonitoringPeriodBeginDate','MonitoringPeriodEndDate']

COPPER_LEAD_HEADERS = ['PrincipalCountyServed', 'WaterSystemNo.', 'WaterSystemName',
                       'MonitoringPeriodBeginDate', 'MonitoringPeriodEndDate',
                       'NumberofSamples', 'Measure(mg/l)', 'Analyte']

CSV_COLIFORM = COLIFORM_HEADERS.copy()
CSV_COLIFORM.insert(0, 'UID')

CSV_CHEM = CHEM_HEADERS.copy()
CSV_CHEM.insert(0, 'UID')

CSV_COPPER_LEAD = COPPER_LEAD_HEADERS.copy()
CSV_COPPER_LEAD.insert(0, 'UID')

#Useful for unique ID's
LAB_SAMPLE = 'LabSampleNo.'
ANALYTE_CODE = 'AnalyteCode'
WATER_SYSTEMS_NO = 'WaterSystemNo.'
ANALYTE = 'Analyte'
