COLI_SAVE_LOCATION = '/mnt/c/Water-Scraper/DWW/standard_scraper/data/coli/Coliform_'
CHEM_SAVE_LOCATION = '/mnt/c/Water-Scraper/DWW/standard_scraper/data/chem/Chem_'
COPPER_LEAD_SAVE_LOCATION = '/mnt/c/Water-Scraper/DWW/standard_scraper/data/copper_lead/Copper_Lead_'

COLI_LOG_LOCATION = '/mnt/c/Water-Scraper/DWW/standard_scraper/log/coli/Coliform_'
CHEM_LOG_LOCATION = '/mnt/c/Water-Scraper/DWW/standard_scraper/log/chem/Chem_'
COPPER_LEAD_LOG_LOCATION = '/mnt/c/Water-Scraper/DWW/standard_scraper/log/copper_lead/Copper_Lead_'
RUN_SCRAPER_LOG = '/mnt/c/Water-Scraper/DWW/standard_scraper/log/master_log.log'


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
