from os import symlink
from sys import argv
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
soup = BeautifulSoup(html_page, 'html.parser') #html.parser

article = soup.find('div',class_ = 'caas-body').text

#print(article)
import pandas as pd


df = pd.read_csv('Stock market project/Yahoo.csv')


symbols = list(df['Ticker'])


matching = [s for s in symbols if s in article]
print(matching)