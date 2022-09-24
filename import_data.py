import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np

def process_page(html_content):
    soup = BeautifulSoup(html_content, 'html.parser')
    reactor_type = soup.find('span', attrs={'id': 'MainContent_MainContent_lblType'}).text
    print(reactor_type)
    model = soup.find('span', attrs={'id': 'MainContent_MainContent_lblModel'}).text
    print(model)
    design_net_capacity = soup.find('span', attrs={'id': 'MainContent_MainContent_lblDesignNetCapacity'}).text
    print(design_net_capacity)
    electricity_supplied = soup.find('span', attrs={'id': 'MainContent_MainContent_lblGeneration'}).text
    print(electricity_supplied)
    owner = soup.find('a', attrs={'id': 'MainContent_MainContent_hypOwnerUrl'}).text
    print(owner)
    operator = soup.find('a', attrs={'id': 'MainContent_MainContent_hypOperatorUrl'}).text
    print(operator)
    country = soup.find_all('body')[-1].text.strip()
    print(country)
    commercial_operation_date = soup.find('span', attrs={'id': 'MainContent_MainContent_lblCommercialOperationDate'}).text
    print(commercial_operation_date)
    load_factor = soup.find('span', attrs={'id': 'MainContent_MainContent_lblLoadFactor'}).text
    print(load_factor)
    energy_supplied = soup.find('table', attrs={'class': 'active'})
    energy_supplied = pd.read_html(str(energy_supplied))[0]

# get the html
url = 'https://pris.iaea.org/PRIS/CountryStatistics/ReactorDetails.aspx?current={}'
for i in range(1, 2):
    page = requests.get(url.format(i))
    process_page(page.text)
