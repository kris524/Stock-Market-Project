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

#Shoutout to Cogeta from the discord server the data share who helped me fix this.
#The only tickers that are left however are VOW3.DE and 0175.HK but its not a big issue for now
words = article.split()
for i in range(len(words)):
    words[i] = ''.join(e for e in words[i] if e.isalnum())

#print(words)
tickers = set(words)&set(symbols)

print(tickers)