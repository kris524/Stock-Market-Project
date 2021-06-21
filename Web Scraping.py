import numpy as np
import selenium

from bs4 import BeautifulSoup

import requests


#stock market news article we want to scrape its text
url = 'https://uk.finance.yahoo.com/news/automotive-volvo-signs-gigafactory-deal-swedish-electric-battery-maker-northvolt-103840931.html'

#use requests module to get the HTML content and save it to the html_page variable
res = requests.get(url)
html_page = res.content

#create a soup object
soup = BeautifulSoup(html_page, 'html5lib') #html.parser

text = soup.find_all('div',class_='caas-content-wrapper')
#text = soup.find_all(text=True)

print(text)
#print(soup.get_text())

#print(output)