from bs4 import BeautifulSoup
import json

#pass the HTML to Beautifulsoup.
soup = BeautifulSoup(open('list_of_composer.html', 'r', encoding="latin-1"), 'html.parser')

#select table and a tag
My_table = soup.find('table', {'class':'wikitable sortable jquery-tablesorter'})
print(My_table)
links = My_table.findAll('a')

#create dictionary with composers names only
Composers = []
for link in links:
    Composers.append(link.get('title'))
    
print(Composers)

#JSON file export
with open('data.json', 'w', encoding="latin-1") as outfile:
    json.dump(Composers, outfile, indent=4)