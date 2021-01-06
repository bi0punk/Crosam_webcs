

# This restores the same behavior as before.
#context = ssl._create_unverified_context()
#page = urllib.request.urlopen("https://localhost:5001/Sow", context=context)


#page = urllib.request.urlopen('https://localhost:5001/Sow')
#sopa = BeautifulSoup(page, 'lxml')

#tabla_cros = sopa.table
#tabla_cros = sopa.find('table')

#colummns_tabla_cros = tabla_cros.find_all('tr') 
#for tr in colummns_tabla_cros:          
#    td = tr.find_all('td')
#    columns = [i.text for i in td]
#    print(columns)
import urllib.request

from bs4 import BeautifulSoup
import csv
page = urllib.request.urlopen('https://api.gael.cl/general/public/sismos')

soup = BeautifulSoup(page)
table = soup.find("table")

output_rows = []
for table_row in table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text)
    output_rows.append(output_row)
    print(output_row)
    
#with open('output.csv', 'wb') as csvfile:
 #   writer = csv.writer(csvfile)
  #  writer.writerows(output_rows)













