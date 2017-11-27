#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 15:37:09 2017

@author: Vuchicago"""

import pandas as pd
import numpy as np

#####Dictionary
sports={'Archery':'Bhutan',
        'Golf': 'Scotland',
        'Sumo':'Japan',
        'Taekwondo':'Korea'}
#Create a series    
s=pd.Series(sports)        
original_sports=pd.Series(sports)

cricket_loving=pd.Series(['Australia','Pakistan','England','America','Mexico'],
                index=['Cricket','Cricket','Cricket',1,3])
#Can't append original series; has to create new series
all_sports=original_sports.append(cricket_loving)
    
        
##ilock used to look up index number will loc looks up values in keys
#Used for row selection
s.iloc[3]
s.loc['Golf']
#CASE ABOVE WOULD BE WRONG INDICES IF DIDN'T USE ILOC &LOC


s=pd.Series([100,120,101,3])

#Adding via for loop
total=0
for i in s:
    total +=i
print(total)
#Adding via vectorized implementation which is faster
total=np.sum(s)
print(total)

#CREATE 10,000 int series of values between 0 and 1000
s=pd.Series(np.random.randint(0,1000,10000))
s.head(10) #print out first 10 values of series s
#timeit magic function that measures how long on avg of 100 loops

%%timeit -n 100
summary=0
for i in s:
   summary +=i

#vectorized implementation is faster
%%timeit -n 100
s.sum()

#####BELOW IS DICTIONARY VS SERIES.  IF YOU WANT TO STORE DICTIONARY VALUES THEN 
#YOU CAN YOU USE DICTIONARY 
#PANDAS SERIES ALLOWS YOU TO DO COMPLEX DATA MANIPULATION

#DICTIONARY
purchase_1 = {'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50}
purchase_2 = {'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50}
purchase_3 = {'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00}
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], 
                  index=['Store 1', 'Store 1', 'Store 2'])

#########DATA FRAME (PANDAS) & SERIES
purchase_1 = pd.Series({'Name': 'Chris',
                        'Item Purchased': 'Dog Food',
                        'Cost': 22.50})
purchase_2 = pd.Series({'Name': 'Kevyn',
                        'Item Purchased': 'Kitty Litter',
                        'Cost': 2.50})
purchase_3 = pd.Series({'Name': 'Vinod',
                        'Item Purchased': 'Bird Seed',
                        'Cost': 5.00})
df = pd.DataFrame([purchase_1, purchase_2, purchase_3], 
                  index=['Store 1', 'Store 1', 'Store 2'])



df.loc['Store 1']['Cost'] #Will retrieve index store 1 and column "Cost" via CHAINING
#Best avoid chaining since it returns a copy of the data frame instead of a view

#TO CALL THE INDEX ON THE DATAFRAME
df.iloc[0] 
df.loc['Store 1']
df["Item Purchased"] # retrieves the column "Item Purchased" on the df dataframe

df.loc['Store 1','Cost'] #Will retrieve index Store 1 and column "Cost"
df.loc[:,['Cost','Name']] #Will retrieve all rows and columns 'Cost' and 'Name'
df.loc['Store 2',['Cost','Name']]
df.drop("Store 1") #will only drop the index on the view but will not make permanent drop
df_copy=df.drop("Store 1") #Must do this if want to make drop changes.  Axis=0 is default
df_copy=df.drop("Name",axis=1) #drop the column "Name" 
del df_copy["Name"] #will permanently delete column "Name" in dataframe
df["Location"]=None #Will add new column with values "None" 
df["Cost"]*=.8 #Will give 20% discount to Cost in df 
df["Name"][df['Cost']>3] #Select only names that have spent more than $3
df.index=[df.index,df["Name"]] #Add column "Name" as a secondary index in addition to
#current index
df=df.append(pd.Series(data={'Cost':3.00,'Item Purchased':'Kitty Food'},
                             name=('Store 2','Kevyn')))

####READ CSV VIA PANDAS.  MORE USEFUL IF DOING DATA MANIPULATION & ANALYSIS
!cat olympics.csv #Sends rest of lines to operating system.  ??
df=pd.read_csv("Olympics.csv")
df=pd.read_csv("Olympics.csv",index_col=0, skiprows=1)
df.head(10) #read first 10 rows
df.columns
df.values
df.index

##THIS WILL LOOP THROUGH THE COLUMN NAMES TO RENAME IT TO WHAT YOU WANT
for col in df.columns:
    if col[:2]=='01':
        df.rename(columns={col:"Gold"+col[4:]},inplace=True)
    if col[:2]=='02':
        df.rename(columns={col:"Silver"+col[4:]},inplace=True)
    if col[:2]=='03':
        df.rename(columns={col:"Bronze"+col[4:]},inplace=True)
    if col[:2]=='№':
        df.rename(columns={col:"#"+col[4:]},inplace=True)
 
        #BOOLEAN MASK
df["Gold"]=0 #Changes all countries to have 0 gold medals. BE CAREFUL!!!
df["Gold"]>0 #Shows countries that have won gold medals
df["Gold"]==0 #Shows countries that have not won gold medals

only_gold=df.where(df["Gold"]>0)
only_gold=df[df["Gold"]>0]
only_gold["Gold"].count() #Number of countries with gold medals
only_gold["Gold"].sum() #Total GOld medals
only_gold=only_gold.dropna() #Will drop all NA values

golds=df[(df["Gold"]==0)|(df["Gold.1"]>0)] #Or Condition.  Country that has won gold
#in summer olympics or gold in winter olympics
gold_nogold=df[(df["Gold"]==0) & (df["Gold.1"]>0)] #And Condition.  Country that
#has won winter gold but not summer gold.  Output Lichenstein

df['Country']=df.index #Create New column equal to index
df=df.set_index("Gold") #Changes index to Gold column

#CENSUS DATA
df=pd.read_csv("census.csv")
df["SUMLEV"].unique()
df=df[df["SUMLEV"]==50] #50 is county level.  40 is state level
columns_to_keep=['STNAME','CTYNAME','BIRTHS2010','BIRTHS2011','BIRTHS2012',
                 'BIRTHS2013','BIRTHS2014','BIRTHS2015','POPESTIMATE2010',
                 'POPESTIMATE2011','POPESTIMATE2012','POPESTIMATE2013',
                 'POPESTIMATE2014','POPESTIMATE2015']
df=df[columns_to_keep] #KEEPS THE ABOVE COLUMNS
#MORE INDEX
df.reset_index #(This will reset index to original)
df=df.set_index(['STNAME','CTYNAME']) #SETS BOTH STATENAME AND CITY NAME TO BE INDICES
df.loc['Michigan','Washtenaw County']
df.loc[[('Michigan','Washtenaw County'),('Michigan','Wayne County')]]

df=pd.read_csv("log.csv")
df=df.fillna(value=None,method="bfill")
df["volume"]=df["volume"].fillna(value=None,method="ffill")
df.dropna() #drops NA values
np.isnan(df.loc["volume"]) #can use np.isnan to check for NaN values for numeric columns

df=df.set_index("time")
df_index=df.index
df=df.set_index([df.index,"user"]) #set current index and column "user" as indices


    

