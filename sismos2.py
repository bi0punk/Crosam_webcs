import csv
from bs4 import BeautifulSoup
import requests
import pandas as pd
import urllib.request


page = urllib.request.urlopen('http://www.sismologia.cl/links/tabla.html').read()
soup = BeautifulSoup(page)
table = soup.find("table")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    
with open('output.csv', 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(ou)