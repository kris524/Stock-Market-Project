import numpy as np
import selenium

from bs4 import BeautifulSoup

import requests



url = 'https://uk.finance.yahoo.com/news/automotive-volvo-signs-gigafactory-deal-swedish-electric-battery-maker-northvolt-103840931.html'
res = requests.get(url)
html_page = res.content
soup = BeautifulSoup(html_page, 'html.parser')
text = soup.find_all(text=True)


print(soup.get_text())

#print(output)