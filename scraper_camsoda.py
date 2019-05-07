from bs4 import BeautifulSoup
import json

#pass the HTML to Beautifulsoup.
soup = BeautifulSoup(open('camsoda_sample.html', 'r', encoding="latin-1"), 'html.parser')

#select table and a tag
elements = soup.findAll('table', {'class':'table'})
# print(elements)
# print(len(elements))

rows = elements[0].findAll('tr')
# print(len(rows))
for row in rows:
    columns = row.findAll('td')
    if len(columns) > 0:
        column_values = []
        for column in columns:
            column_values.append(column.text.strip())
        print(column_values)

rows = elements[1].findAll('tr')
# print(len(rows))
print('-- Bonus --')
for row in rows:
    columns = row.findAll('td')
    if len(columns) > 0:
        column_values = []
        for column in columns:
            column_values.append(column.text.strip())
        print(column_values)
