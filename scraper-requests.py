import requests
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/List_of_composers_for_the_classical_guitar"


result = requests.get(url)
print(result.status_code)

content = result.content
soup = BeautifulSoup(content,'html.parser')

#select table and a tag
My_table = soup.find('table',{'class':'wikitable sortable'})
links = My_table.findAll('a')

#create dictionary with composers names only
Composers = []
for link in links:
    Composers.append(link.get('title'))
    
print(Composers)

#JSON file export
with open('data.json', 'w') as outfile:
    json.dump(Composers, outfile, indent=4)