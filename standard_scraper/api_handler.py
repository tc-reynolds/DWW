url = 'url'
coli = 'coliform'
chem = 'chem'
copper_lead = 'copper_lead'

state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut",
               "District of Columbia", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois",
               "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan",
               "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska",
               "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon",
               "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah",
               "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

non_jsp_states = {
    'Florida': 'http://publicfiles.dep.state.fl.us/DWRM/Drinking%20Water%20Data/CHEM/2004/',
    'Wisconsin': 'https://dnr.wi.gov/dwsviewer/ContamResult',
    'New Jersey': 'https://www9.state.nj.us/DEP_WaterWatch_public/',
    'California': 'https://sdwis.waterboards.ca.gov/PDWW/',
    'Pennsylvania': 'http://www.drinkingwater.state.pa.us/dwrs/HTM/SelectionCriteria.html',
    'Washington': 'https://fortress.wa.gov/doh/eh/portal/odw/si/FindWaterQuality.aspx',
    'Michigan': 'https://mitracking.state.mi.us/',
    'Orgeon': 'https://yourwater.oregon.gov/search.htm',
    'Utah': 'https://deq.utah.gov/water-system-search-form'
}
no_data = [
    'Alabama',
    'District of Columbia',
    'South Dakota',
    'Georgia'
]
jsp_unique = {
    'Missouri': 'https://dnr.mo.gov/DWW/',
    'Virginia': 'https://odw.vdh.virginia.gov/DWW-VA/',
    'Rhode Island': 'https://dwq.health.ri.gov/DWW/',
    'Kansas': 'http://165.201.142.59:8080/DWW/SampleSearch.jsp',
    'Wyoming': 'https://sdwisr8.epa.gov/Region8DWWPUB/index.jsp',
    'Alaska': 'https://dec.alaska.gov/DWW/'
}
jsp_states = {
    'Maryland': {
        url: 'https://mdesdwis.mde.state.md.us/DWW/',
        coli: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
              '&PointOfContactType=None&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All'
              '&SourceWaterType=All&PointOfContactType=None&SampleType=NonTCRAll'
              '&begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
                     '&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Texas': {
        url: 'https://dww2.tceq.texas.gov/DWW/',
        coli: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All&SourceWaterType=All'
              '&SampleType=ColiformSample&begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All&SourceWaterType=All'
              '&SampleType=NonTCRAll&stateclassificationcode=All&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
                     '&SourceWaterType=All&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Delaware': {
        url: 'https://drinkingwater.dhss.delaware.gov/',
        coli: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All'
              '&SourceWaterType=All&PointOfContactType=None&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All'
              '&SourceWaterType=All&PointOfContactType=None&SampleType=NonTCRAll&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
                     '&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Iowa': {
        url: 'http://programs.iowadnr.gov/drinkingwaterwatch/',
        coli: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
              '&PointOfContactType=None&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All'
              '&SourceWaterType=All&PointOfContactType=None&SampleType=NonTCRAll'
              '&begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
                     '&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Illinois': {
        url: 'http://water.epa.state.il.us/dww/',
        coli: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=NonTCRAll&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
                     '&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Kentucky': {
        url: 'https://dep.gateway.ky.gov/DWW/',
        coli: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All'
              '&county=All&WaterSystemType=All&SourceWaterType=All&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=NonTCRAll&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
                     '&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Louisiana': {
        url: 'https://sdw.ldh.la.gov/DWW/',
        coli: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All'
              '&county=All&WaterSystemType=All&SourceWaterType=All&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=NonTCRAll&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
                     '&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Mississippi': {
        url: 'https://apps.msdh.ms.gov/DWW/',
        coli: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All'
              '&county=All&WaterSystemType=All&SourceWaterType=All&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=NonTCRAll&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
                     '&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'North Carolina': {
        url: 'https://www.pwss.enr.state.nc.us/NCDWW/',
        coli: 'JSP/SearchDispatch?number=&name=&companyname=&WaterSystemStatusCode=A&county=All&WaterSystemType=All'
              '&SourceWaterType=All&PointOfContactType=None&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&companyname=&WaterSystemStatusCode=A&county=All&WaterSystemType=All'
              '&SourceWaterType=All&PointOfContactType=None&SampleType=NonTCRAll&stateclassificationcode=All&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&companyname=&WaterSystemStatusCode=A&county=All&'
                     'WaterSystemType=All&SourceWaterType=All&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Vermont': {
        url: 'https://anrnode.anr.state.vt.us/DWW/',
        coli: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=NonTCRAll&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&companyname=&WaterSystemStatusCode=A&county=All&'
                     'WaterSystemType=All&SourceWaterType=All&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'West Virginia': {
        url: 'https://dww.wvdhhr.org/DWWpublic/',
        coli: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=NonTCRAll&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&companyname=&WaterSystemStatusCode=A&county=All&'
                     'WaterSystemType=All&SourceWaterType=All&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Montana': {
        url: 'http://sdwisdww.mt.gov:8080/DWW/',
        coli: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=NonTCRAll&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&companyname=&WaterSystemStatusCode=A&county=All&'
                     'WaterSystemType=All&SourceWaterType=All&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Tennessee': {
        url: 'http://environment-online.state.tn.us:8080/DWW/',
        coli: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All'
              '&SourceWaterType=All&PointOfContactType=None&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
              '&PointOfContactType=None&SampleType=NonTCRAll&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
                     '&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Indiana': {
        url: 'https://myweb.in.gov/IDEM/DWW/',
        coli: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
              '&PointOfContactType=None&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: None,
        copper_lead: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
                     '&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Oklahoma': {
        url: 'http://sdwis.deq.state.ok.us/DWW/',
        coli: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=NonTCRAll&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&companyname=&WaterSystemStatusCode=A&county=All&'
                     'WaterSystemType=All&SourceWaterType=All&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Arizona': {
        url: 'https://azsdwis.azdeq.gov/DWW_EXT/',
        coli: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=NonTCRAll&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&companyname=&WaterSystemStatusCode=A&county=All&'
                     'WaterSystemType=All&SourceWaterType=All&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Ohio': {
        url: 'http://dww.epa.ohio.gov/',
        coli: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
        '&PointOfContactType=None&SampleType=ColiformSample&'
        'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All'
        '&SourceWaterType=All&PointOfContactType=None&SampleType=NonTCRAll&'
        'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
                     '&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Idaho': {
        url: 'http://dww.deq.idaho.gov/IDPDWW/',
        coli: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=NonTCRAll&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&companyname=&WaterSystemStatusCode=A&county=All&'
                     'WaterSystemType=All&SourceWaterType=All&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Nebraska': {
        url: 'https://sdwis-dhhs.ne.gov:8443/DWW/',
        coli: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=NonTCRAll&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&companyname=&WaterSystemStatusCode=A&county=All&'
                     'WaterSystemType=All&SourceWaterType=All&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'Nevada': {
        url: 'https://ndwis.ndep.nv.gov/DWW/',
        coli: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All'
              '&SourceWaterType=All&SampleType=NonTCRAll&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&companyname=&WaterSystemStatusCode=A&county=All&'
                     'WaterSystemType=All&SourceWaterType=All&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'New Mexico': {
        url: 'https://dww.water.net.env.nm.gov/DWW/',
        coli: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
              '&PointOfContactType=None&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
              '&PointOfContactType=None&SampleType=NonTCRAll&stateclassificationcode=All&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
                     '&PointOfContactType=None&SampleType=LeadandCopperSummaries&'
                     'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    },
    'South Carolina': {
        url: 'http://dwwwebvm.dhec.sc.gov:8080/DWW/',
        coli: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
              '&PointOfContactType=None&SampleType=ColiformSample&'
              'begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples',
        chem: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
              '&PointOfContactType=None&SampleType=NonTCRAll&stateclassificationcode=All&'
              'begin_date=3%2F11%2F2019&end_date=3%2F11%2F2021&action1=Search+For+Samples',
        copper_lead: 'JSP/SearchDispatch?number=&name=&county=All&WaterSystemType=All&SourceWaterType=All'
                     '&PointOfContactType=None&SampleType=LeadandCopperSummaries'
                     '&begin_date=STARTING_DATE&end_date=ENDING_DATE&action1=Search+For+Samples'
    }
}
crawled_states = [
    'Arizona',
    'Delaware',
    'Iowa',
    'Kentucky',
    'Louisiana',
    'Mississippi',
    'North Carolina',
    'Vermont',
    'Florida',
    'West Virginia',
    'Illinois'
]


def known_states():
    known_state_list = []
    for key in jsp_states:
        known_state_list.append(key)
    return known_state_list


def crawl_new():
    print("States left to Crawl!")
    keys = jsp_states.keys()
    for key in keys:
        if key not in crawled_states:
            print(key)


def get_url(key):
    return jsp_states[key][url]

def get_coli_call(key):
    return jsp_states[key][coli]

def get_chem_call(key):
    return jsp_states[key][chem]

def get_copper_lead_call(key):
    return jsp_states[key][copper_lead]


def diff(li1, li2):
    return list(list(set(li1) - set(li2)) + list(set(li2) - set(li1)))


if __name__ == '__main__':
    known = known_states()
    print("Num States known: " + str(len(known)))
    print(known)
    unknown = diff(known, state_names)
    print("States not yet known: " + str(len(unknown)))
    print(diff(known, state_names))