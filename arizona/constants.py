COLI_SAVE_LOCATION = '/mnt/c/Water-Scraper/DWW/arizona/data/Coliform'
CHEM_SAVE_LOCATION = '/mnt/c/Water-Scraper/DWW/arizona/data/Chem'

DATE_INCREMENT = 30  # Days

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

LAB_SAMPLE = 'LabSampleNo.'
ANALYTE_CODE = 'AnalyteCode'
