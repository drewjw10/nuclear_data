import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

id_dict = {
    'name': {
        'element_type': 'span',
        'id': 'MainContent_MainContent_lblReactorName'
    },
    'reactor_type': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblType'
    },
    'model': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblModel'
    },
    'status': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblReactorStatus'
    },
    'design_net_capacity': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblDesignNetCapacity'
    },
    'electricity_supplied': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblGeneration'
    },
    'owner': {
        'element_type': 'a', 
        'id': 'MainContent_MainContent_hypOwnerUrl'
    },
    'operator': {
        'element_type': 'a', 
        'id': 'MainContent_MainContent_hypOperatorUrl'
    },
    'construction_start_date': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblConstructionStartDate'
    },
    'first_criticality_date': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblFirstCriticality'
    },
    'first_grid_connection': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblGridConnectionDate'
    },
    'longterm_shutdown_date': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblLongTermShutdownDate'
    },
    'restart_date': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblRestartDate'
    },
    'permanent_shutdown_date': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblPermanentShutdownDate'
    },
    'commercial_operation_date': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblCommercialOperationDate'
    },
    'load_factor': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblLoadFactor'
    },
    'operation_factor': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblOperatingFactor'
    },
    'energy_availability_factor': {
        'element_type': 'span', 
        'id': 'MainContent_MainContent_lblEAF'
    }    
}

def soup_wrapper(soup, element_type, id):
    result = soup.find(element_type, attrs={'id': id}) 
    return "Missing ID" if result == None else result.text

def process_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    data_results = {}
    
    if soup.find('div', attrs={'class':'alert-inner'}) != None:
        return {'name': 'unauthorized'}

    # data without an id attribute
    country = soup.find_all('body')[-1].text.strip()
    energy_supplied = soup.find('table', attrs={'class': 'active'})
    energy_supplied = pd.read_html(str(energy_supplied))[0] if energy_supplied != None else "None"
    data_results["country"] = country
    data_results["energy_supplied"] = energy_supplied
    
    # data with an id attribute
    for entry in id_dict:
        data_results[entry] = soup_wrapper(soup, id_dict[entry]["element_type"], id_dict[entry]["id"])
    return data_results

# There are pages that will give "Unauthorized access" warnings. e.g. 742
# Ultimately, 1084 is the max ID
# It would be good to figure out if the unauthorized pages are missing data or just weird numbering
# In the meantime, need to handle those errors

# get the html and process
url = 'https://pris.iaea.org/PRIS/CountryStatistics/ReactorDetails.aspx?current={}'
data = []
for i in range(1, 1084): 
    page = requests.get(url.format(i))
    data_row = process_page(page.text)
    data_row["id"] = i
    print(data_row)
    data.append(data_row)
    time.sleep(5)

results_df = pd.DataFrame.from_dict(data)
results_df.to_excel('iaea_dataset.xlsx')