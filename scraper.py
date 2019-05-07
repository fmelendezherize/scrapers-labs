import urllib.request
from bs4 import BeautifulSoup
import json

url = "https://en.wikipedia.org/wiki/List_of_composers_for_the_classical_guitar"

#download the URL and extract the content to the variable html 
request = urllib.request.Request(url)
html = urllib.request.urlopen(request).read()

#pass the HTML to Beautifulsoup.
soup = BeautifulSoup(html,'html.parser')

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