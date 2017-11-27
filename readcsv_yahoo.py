#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 20:28:39 2017

@author: Vuchicago
"""


import pandas as pd
import pandas_datareader as pdr
from pandas_datareader import data,wb 
import datetime as dt



#sp500=pdr.data.get_data_google("GSPC",start=dt.datetime(2016,10,1),
#                                end=dt.datetime(2017,7,6))
sp500.head(10)

date_int=["2017-01-03"::"2017-01-31"]
start = dt.datetime(2017, 01, 01)
end = dt.datetime.now()
init="2017-01-03"
final="2017-01-31"
sp500 = pdr.data.DataReader("SPY", 'google', start, end)
sp500[sp500["Low"]==min(sp500["Low"])] #Find the values where f is min
sp500[sp500["High"]==max(sp500["High"])] #Find the values where f is max
sp500.to_csv("spy010117_to_070717.csv") #Save dataset to csv

df=pd.read_csv("spy010117_to_070717.csv",index_col=0,
               skiprows=0,parse_dates=True) #Read csv with date as index
df.loc["2017-01-03"] # See values for certain dates
df.loc[init : final] # filter by dates
df.iloc[2:10]
df[1:100:4] #Show every 4th values up to 100
df[2:3]


