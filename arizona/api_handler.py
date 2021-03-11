state_names = ["Alaska", "Alabama", "Arkansas", "Arizona", "California", "Colorado", "Connecticut", "District of Columbia", "Delaware", "Florida", "Georgia", "Hawaii", "Iowa", "Idaho", "Illinois", "Indiana", "Kansas", "Kentucky", "Louisiana", "Massachusetts", "Maryland", "Maine", "Michigan", "Minnesota", "Missouri", "Mississippi", "Montana", "North Carolina", "North Dakota", "Nebraska", "New Hampshire", "New Jersey", "New Mexico", "Nevada", "New York", "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina", "South Dakota", "Tennessee", "Texas", "Utah", "Virginia", "Vermont", "Washington", "Wisconsin", "West Virginia", "Wyoming"]

non_jsp_states = {
	'Florida' : 'http://publicfiles.dep.state.fl.us/DWRM/Drinking%20Water%20Data/CHEM/2004/',
	'Wisconsin' : 'https://dnr.wi.gov/dwsviewer/ContamResult',
	'New Jersey' : 'https://www9.state.nj.us/DEP_WaterWatch_public/',
	'California' : 'https://sdwis.waterboards.ca.gov/PDWW/',
	'Pennsylvania' : 'http://www.drinkingwater.state.pa.us/dwrs/HTM/SelectionCriteria.html',
	'Washington' : 'https://fortress.wa.gov/doh/eh/portal/odw/si/FindWaterQuality.aspx',
	'Michigan' : 'https://mitracking.state.mi.us/',
	'Ohio' : 'http://dww.epa.ohio.gov/WaterSystemDetail.jsp?tinwsys_is_number=1164&tinwsys_st_code=OH&wsnumber=OH1700011',
	'Orgeon' : 'https://yourwater.oregon.gov/search.htm',
	'Utah' : 'https://deq.utah.gov/water-system-search-form'
}
no_data = [
		'Alabama',
		'District of Columbia',
		'South Dakota'
		]
jsp_unique = {
	'Missouri' : 'https://dnr.mo.gov/DWW/',
	'Virginia' : 'https://odw.vdh.virginia.gov/DWW-VA/',
	'Rhode Island' : 'https://dwq.health.ri.gov/DWW/',
	'Kansas' : 'http://165.201.142.59:8080/DWW/SampleSearch.jsp',
	'Maryland' : 'https://mdesdwis.mde.state.md.us/DWW/',
	'Wyoming' :'https://sdwisr8.epa.gov/Region8DWWPUB/index.jsp'
}
jsp_states = {
	'Texas' : 'https://dww2.tceq.texas.gov/DWW/',
	'Delaware' : 'https://dep.gateway.ky.gov/DWW/',
	'Iowa' : 'http://programs.iowadnr.gov/drinkingwaterwatch/',
	'Illinois' : 'http://water.epa.state.il.us/dww/',
	'Kentucky' : 'https://dep.gateway.ky.gov/DWW/',
	'Louisiana' : 'https://sdw.ldh.la.gov/DWW/',
	'Mississippi' : 'https://apps.msdh.ms.gov/DWW/',
	'North Carolina' : 'https://www.pwss.enr.state.nc.us/NCDWW/',
	'Vermont' : 'https://anrnode.anr.state.vt.us/DWW/',
	'West Virginia' : 'https://dww.wvdhhr.org/DWWpublic/',
	'Alaska' : 'https://dec.alaska.gov/DWW/',
	'Montana' : 'http://sdwisdww.mt.gov:8080/DWW/',
	'Tennessee' : 'http://environment-online.state.tn.us:8080/DWW/',
	'Indiana' : 'https://myweb.in.gov/IDEM/DWW/',
	'Oklahoma' : 'http://sdwis.deq.state.ok.us/DWW/',
	'Arizona' : 'https://azsdwis.azdeq.gov/DWW_EXT/',
	'Arkansas' : 'http://sdwis.deq.state.ok.us/DWW/',
	'Georgia' : 'http://dwwwebvm.dhec.sc.gov:8080/DWW/',
	'Idaho' : 'http://dww.deq.idaho.gov/IDPDWW/',
	'Nebraska' : 'https://sdwis-dhhs.ne.gov:8443/DWW/',
	'Nevada' : 'https://ndwis.ndep.nv.gov/DWW/',
	'New Mexico' : 'https://dww.water.net.env.nm.gov/DWW/',
	'South Carolina' : 'http://dwwwebvm.dhec.sc.gov:8080/DWW/'
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
	'West Virginia'
]
jsp_call = 'SearchDispatch?number=&name=&ActivityStatusCD=All&county=All&WaterSystemType=All&SourceWaterType=All&SampleType=ColiformSample&begin_date=10%2F28%2F2020&end_date=2%2F28%2F2021&action1=Search+For+Samples'

def known_states():
	known_state_list = []
	for key in jsp_states:
		known_state_list.append(key)
	for key in jsp_unique:
		known_state_list.append(key)
	for key in non_jsp_states:
		known_state_list.append(key)
	for item in no_data:
		known_state_list.append(item)
	return known_state_list

def crawl_new():
	print("States left to Crawl!")
	keys = jsp_states.keys()
	for key in keys:
		if key not in crawled_states:
			print(key)
def get_url(key):
	return jsp_states[key]
def diff(li1, li2):
    return (list(list(set(li1)-set(li2)) + list(set(li2)-set(li1))))

# handled_states = known_states()
# states_left = diff(state_names, handled_states)
# states_left.sort()
# print("REMAINING STATES")
# print(states_left)
# print("Number of States: " + str(len(states_left)))
# print("Num Standard JSP States: " + str(len(jsp_states.keys())))
# crawl_new()