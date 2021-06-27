import pandas as pd

df  = pd.read_csv('Stock market project/NYSE.csv')
df1 = pd.read_csv('Stock market project/AMEX.csv')
df2 = pd.read_csv('Stock market project/NASDAQ.csv')

#C:\Users\krist\Documents\PYTHON PROJECTS ON VS CODE
nasdaq = list(df2['Symbol'])
amex = list(df1['Symbol'])
nyse = list(df['Symbol'])

#print(nasdaq)
