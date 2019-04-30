import requests
from bs4 import BeautifulSoup

url = "http://krasnovsolutions.com/wp-login.php"

result = requests.get(url)
content = result.content
soup = BeautifulSoup(content,'html.parser')

payload = {
    'log': '',
    'pwd': '',
}

hidden_tags = soup.find_all("input", type="hidden")
for tag in hidden_tags:
    print(tag['name'])
    print(tag['value'])
    payload[tag['name']] = tag['value']

print(payload)

post_url = "http://krasnovsolutions.com/wp-login.php"

# Use 'with' to ensure the session context is closed after use.
with requests.Session() as s:
    p = s.post(post_url, data=payload)
    r = s.get('http://krasnovsolutions.com/wp-admin/')
    print(r.status_code)
    print(r.content)

