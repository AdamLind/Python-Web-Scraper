# Libraries:

# - requests
# - inflection
# - beautifulsoup

# pip install requests
# pip install inflection
# pip install beautifulsoup

import requests as r
from bs4 import BeautifulSoup
import inflection

r = r.get('https://www.dailysmarty.com/topics/python')
soup = BeautifulSoup(r.content, 'html.parser')
scrape = soup.findAll('h2')

for title in scrape:
    x = str(title).replace('<h2><a data-turbolinks="false" href="/posts/', "")
    y = x.partition('"')
    z = list(y)[0].replace('-', ' ')
    q = inflection.titleize(z)
    print(q)