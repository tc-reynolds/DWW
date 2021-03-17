COLI_SAVE_LOCATION = '/mnt/c/Water-Scraper/DWW/arizona/data/Coliform_'
CHEM_SAVE_LOCATION = '/mnt/c/Water-Scraper/DWW/arizona/data/Chem_'

COLI_LOG_LOCATION = '/mnt/c/Water-Scraper/DWW/arizona/log/Coliform_'
CHEM_LOG_LOCATION = '/mnt/c/Water-Scraper/DWW/arizona/log/Chem_'

COPPER_LEAD_SAVE_LOCATION = '/mnt/c/Water-Scraper/DWW/arizona/data/Copper_Lead_'

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
