DATA_DIR = '/mnt/c/DWW/standard_scraper/data/'
LOG_DIR = '/mnt/c/DWW/standard_scraper/log/'
COLI_DATA_DIR = '/mnt/c/DWW/standard_scraper/data/coli/'
CHEM_DATA_DIR = '/mnt/c/DWW/standard_scraper/data/chem/'
COPPER_LEAD_DATA_DIR = '/mnt/c/DWW/standard_scraper/data/copper_lead/'

COLI_LOG_DIR = '/mnt/c/DWW/standard_scraper/log/coli/'
CHEM_LOG_DIR = '/mnt/c/DWW/standard_scraper/log/chem/'
COPPER_LEAD_LOG_DIR = '/mnt/c/DWW/standard_scraper/log/copper_lead/'


COLI_SAVE_LOCATION =  COLI_DATA_DIR + 'Coliform_'
CHEM_SAVE_LOCATION = CHEM_DATA_DIR + 'Chem_'
COPPER_LEAD_SAVE_LOCATION = COPPER_LEAD_DATA_DIR + 'Copper_Lead_'

COLI_LOG_LOCATION = COLI_LOG_DIR + 'Coliform_'
CHEM_LOG_LOCATION = CHEM_LOG_DIR + 'Chem_'
COPPER_LEAD_LOG_LOCATION = COPPER_LEAD_LOG_DIR + 'Copper_Lead_'

MASTER_LOG_DIR = '/mnt/c/DWW/standard_scraper/log/'
MASTER_LOG = MASTER_LOG_DIR + 'master.log'


DATE_INCREMENT = 30  # Days

COLIFORM_HEADERS = ['PrincipalCountyServed', 'WaterSystemNo.',
                    'WaterSystemName', 'Type', 'LabSampleNo.',
                    'CollectionDate&Time', 'Presence/AbsenceIndicator',
                    'AnalyteCode', 'AnalyteName',
                    'MonitoringPeriodBeginDate', 'MonitoringPeriodEndDate']

CHEM_HEADERS = ['PrincipalCountyServed', 'WaterSystemNo.',
                'WaterSystemName', 'LabSampleNo.',
                'Type', 'CollectionDate&Time',
                'SamplingPoint', 'SampleHref']

COPPER_LEAD_HEADERS = ['PrincipalCountyServed', 'WaterSystemNo.', 'WaterSystemName',
                       'MonitoringPeriodBeginDate', 'MonitoringPeriodEndDate',
                       'NumberofSamples', 'Measure(mg/l)', 'Analyte']

CSV_COLIFORM = ['UID', 'PrincipalCountyServed', 'WaterSystemNo.',
                'WaterSystemName', 'Type', 'LabSampleNo.',
                'CollectionDate&Time', 'Presence/AbsenceIndicator',
                'AnalyteCode', 'AnalyteName',
                'MonitoringPeriodBeginDate', 'MonitoringPeriodEndDate']

CSV_CHEM = ['UID', 'PrincipalCountyServed', 'WaterSystemNo.',
            'WaterSystemName', 'LabSampleNo.',
            'Type', 'CollectionDate&Time',
            'SamplingPoint', 'SampleHref']

CSV_COPPER_LEAD = ['UID', 'PrincipalCountyServed', 'WaterSystemNo.', 'WaterSystemName',
                       'MonitoringPeriodBeginDate', 'MonitoringPeriodEndDate',
                       'NumberofSamples', 'Measure(mg/l)', 'Analyte']

LAB_SAMPLE = 'LabSampleNo.'
ANALYTE_CODE = 'AnalyteCode'
WATER_SYSTEMS_NO = 'WaterSystemNo.'
ANALYTE = 'Analyte'
