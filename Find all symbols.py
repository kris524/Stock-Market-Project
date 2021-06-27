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

df  = pd.read_csv('Stock market project/NYSE.csv')
df1 = pd.read_csv('Stock market project/AMEX.csv')
df2 = pd.read_csv('Stock market project/NASDAQ.csv')

#C:\Users\krist\Documents\PYTHON PROJECTS ON VS CODE
nasdaq = list(df2['Symbol'])
amex = list(df1['Symbol'])
nyse = list(df['Symbol'])

symbols = nasdaq + amex + nyse
#print(nasdaq)

match = [ele for ele in article if ele in symbols]
print(match)


#if res ==True:
#print(article[0])
 
matching = [s for s in symbols if s in article]
print(matching)