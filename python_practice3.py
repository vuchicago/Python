#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 10 13:56:35 2017

@author: Vuchicago
"""
#####               MERGING DATAFRAMES

##CHANGING DIRECTORIES
import os
os.chdir(path)
os.chdir("/Users/vu/Documents/Courses/Python Class")
#####
import pandas as pd

staff_df=pd.DataFrame([{'Name':'Kelly','Role':'Director of HR'},
                      {'Name':'Sally','Role':'Course Lisason'},
                      {'Name':'James','Role':'Grader'}])
student_df=pd.DataFrame([{'Name':'James','School':'Business'},
                        {'Name':'Mike','School':'Law'},
                        {'Name':'Sally','School':'Engineering'}])
staff_df=staff_df.set_index('Name')
student_df=student_df.set_index('Name')

#MERGING USING THE INDICES AS KEYS
outer_merge=pd.merge(staff_df,student_df,how='outer',
                     left_index=True,right_index=True)
inner_merge=pd.merge(staff_df,student_df,how='inner',
                     left_index=True,right_index=True)

#MERGE IT BY LEFT JOIN ON COLUMN "NAME"ON BOTH DATASETS WHERE THE LEFT DATASET
#AND RIGHT DATASET USES COLUMN "NAME" AS THE KEYS
staff_df=staff_df.reset_index()
student_df=student_df.reset_index()
pd.merge(staff_df,student_df,how='left',left_on='Name',right_on='Name')

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
                         {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
                         {'Name': 'James', 'Role': 'Grader', 'Location': 'Washington Avenue'}])
student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
                           {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
                           {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}])
pd.merge(staff_df, student_df, how='left', left_on='Name', right_on='Name')

staff_df = pd.DataFrame([{'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
                         {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
                         {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'}])
student_df = pd.DataFrame([{'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
                           {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'}])

test_df=pd.DataFrame([{'Funk Name': 'James',  'School': 'Business','Last Name': 'Hammond'},
                           {'Funk Name': 'Mike', 'School': 'Law', 'Last Name': 'Smith'},
                           {'Funk Name': 'Sally', 'School': 'Engineering','Last Name': 'Brooks'}])

test_df2=pd.DataFrame([{'First Name': 'James','LName': 'Hammond',  'School': 'Business'},
                           {'First Name': 'Mike', 'LName': 'Smith', 'School': 'Law'},
                           {'First Name': 'Sally','LName': 'Brooks', 'School': 'Engineering'}])
#POSSIBLE TO HAVE TO MERGE ON MULTIPLE COLUMNS.  SO YOU CAN MAKE A LIST OF
#LEFT ON AND RIGHT ON COLUMNS TO JOIN

#DOESN'T MATTER ORDERING...AS LONG AS COLUMNS NAMES EQUAL
staff_test_df=pd.merge(staff_df, student_df, how='outer', left_on=['First Name','Last Name'], 
         right_on=['First Name','Last Name'])
staff_test_df2=pd.merge(staff_df,test_df2,how='outer',left_on=['First Name','Last Name'],
         right_on=['First Name','LName'])

df=pd.read_csv('census.csv')
#CREATE DF 
KEEP=["ESTIMATESBASE2010",'STNAME','CTYNAME','SUMLEV',"CENSUS2010POP",
      'POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012',
      'POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']
df=(df[KEEP][df['SUMLEV']==50].set_index(['STNAME','CTYNAME']).dropna())

df2=(df[KEEP].drop(df[df['SUMLEV']!=50].index).dropna().
             set_index(['STNAME','CTYNAME']).rename(columns={'ESTIMATESBASE2010':'ESTIMATE BASE 2010'}))

KEEP_METRICS=['POPESTIMATE2010','POPESTIMATE2011','POPESTIMATE2012',
      'POPESTIMATE2013','POPESTIMATE2014','POPESTIMATE2015']

#BOTH SAME WAY TO DO .  CHECKING TIMEIT FEATURE
%%timeit -n 100 
check1=df[df["STNAME"]!="Illinois"].rename(columns={"STNAME":"STATE NAME"})
%%timeit -n 100
check2=df.drop(df[df["STNAME"]=="Illinois"].index).rename(columns={"STNAME":"STATE NAME"})

import numpy as np

#THREE WAYS TO CREATE A MIN AND MAX COLUMN
def min_max(row):
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    return pd.Series({'min': np.min(data), 'max': np.max(data)})

df.apply(min_max,axis=1)

def min_max(row):
    data = row[['POPESTIMATE2010'
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    row["max"]=np.max(data)
    row["min"]=np.min(data)
    return row

df.apply(min_max,axis=1)

rows=['POPESTIMATE2010',
     'POPESTIMATE2011',
     'POPESTIMATE2012',
     'POPESTIMATE2013',
     'POPESTIMATE2014',
     'POPESTIMATE2015']
df.apply(lambda x : np.max(x[rows]),  axis=1)


######group by using census data
df=pd.read_csv("census.csv")
df=df[df["SUMLEV"]==50]
#i indexes each state, j indexes all the counties within the states
for i, j in df.groupby("STNAME"):
    avg=np.average(j[KEEP])
    print("Countries in State" + i +"have a pop of " +str(avg))

df=df.set_index("STNAME")
def fun(item):
    if item[0]<"M":
        return 0
    if item[0]<"Q":
        return 1
    return 2

for group, frame in df.groupby(fun):
    print("There are " +str(len(frame)) + "records in group" +str(group))

####YOU CAN UTILIZE the agg function with a groupby to calculate metrics
f={"POPESTIMATE2010":[np.average,np.sum]}
df.groupby(df.index).agg(f)
g={"POPESTIMATE2010":np.average, "POPESTIMATE2015":np.average}
df.groupby(df.index).agg(g)

#THIS WILL AGGREGATE ALL COLUMNS, GROUPED BY THE INDEX (STNAME)
df.groupby(df.index).agg("sum")

##THIS WILL AGGREGATE COLUMNS POP2010 AND POP2011, GROUPED BY AT COLUMN LEVEL
#BY STNAME
(df.groupby(level=0)['POPESTIMATE2010','POPESTIMATE2011']
    .agg({'POPESTIMATE2010': np.average, 'POPESTIMATE2011': np.sum}))

#USING APPLY AND LAMBDA FUNCTION TO AGGREGATE THE TOTAL OF TWO COLUMNS
#THEN THE MAX OF ALL IN THE GROUP
df.groupby(df.index).apply(lambda df,a,b : sum(df[a],df[b]),'POPESTIMATE2010','POPESTIMATE2010')


### SCALES

#Add values and index.  Notice that they changed the column names after
df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good', 'good', 
                         'good', 'ok', 'ok', 'ok', 'poor', 'poor'])
df.rename(columns={0: 'Grades'}, inplace=True)
df['Grades'].astype('category').head()

grades = df['Grades'].astype('category',
                             categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 
                                         'B+', 'A-', 'A', 'A+'],
                             ordered=True)

grades>"C" 
####PUT ORDER

###HOW TO CREATE ORDER IN A SERIES
s = pd.Series(['Low', 'Low', 'High', 'Medium', 'Low', 'High', 'Low'])
s.astype("category", categories=["Low","Medium","High"],ordered=True)

##########################
####aggregates the average of the group
df = pd.read_csv('census.csv')
df = df[df['SUMLEV']==50]
df = df.set_index('STNAME').groupby(level=0)['CENSUS2010POP'].agg({'avg': np.average})
pd.cut(df['avg'],10) #BASED OFF THE VALUES, YOU CAN CUT THE VALUES UP INTO 10 euqally spaced BINS


########################PIVOT TABLES#######
df=pd.read_csv("cars.csv")
metric=["(kW)","HWY (kWh/100 km)"]
df.pivot_table(values=metric, index=["YEAR","Make"],aggfunc=np.mean)

#OR
pd.pivot_table(df,values=metric,index=["YEAR","Make"],aggfunc=np.mean)


#MARGIN=TRUE WILL SPLIT THE PIVOT TABLES UP BY THE AGGREGATE FUNCTIONS
df.pivot_table(values='(kW)', index='YEAR', columns='Make', aggfunc=[np.mean,np.min],
               margins=True)

#########DATE FUNCTIONALITY IN PANDAS
import pandas as pd
import numpy as np

####TIMESTAMP
pd.Timestamp('9/1/2016 10:05AM')

#PERIOD & Dates
pd.Period('1/2016')

pd.Period('3/5/2016')
t1 = pd.Series(list('abc'), [pd.Timestamp('2016-09-01'), pd.Timestamp('2016-09-02'),
               pd.Timestamp('2016-09-03')])
type(t1.index)

t2 = pd.Series(list('def'), [pd.Period('2016-09'), 
               pd.Period('2016-10'), pd.Period('2016-11')])
type(t2.index)

#DATE TIME VALUES OF D1
#CREATE A 4X2 DATAFRAME OF VALUES BETWEEN 10-100 AND USE D1 AS THE INDEX
d1 = ['2 June 2013', 'Aug 29, 2014', '2015-06-26', '7/12/16']
ts3 = pd.DataFrame(np.random.randint(10, 100, (4,2)), index=d1, columns=list('ab'))
#USE THE pd.to_datetime FUNCTION TO CONVERT DATETIME & PUT THEM IN STANDARD FORMAT
ts3.index = pd.to_datetime(ts3.index)

pd.to_datetime('4.7.12', dayfirst=True) #THIS TRUE OPTION MAKES IT IN EUROPEAN DATE FORMAT YYYY-MM-DD
pd.Timestamp('9/3/2016')-pd.Timestamp('9/1/2016') #Subtract date time
pd.Timestamp('9/2/2016 8:10AM') + pd.Timedelta('12D 3H') #ADD CURRENT DATE WITH TIME DELTA

dates = pd.date_range('10-01-2016', periods=9, freq='2W-SUN') #CREATE 9 time series
#beginning every sunday
dates.weekday_name #check which day of week time series is


df = pd.DataFrame({'Count 1': 100 + np.random.randint(-5, 10, 9).cumsum(),
                  'Count 2': 120 + np.random.randint(-5, 10, 9)}, index=dates)
df.index.weekday_name #CHECK WHICH DAYS OF THE WEEK IT IS
df.diff() #FIND DIFFERENCE IN EACH DAY VALUE FROM DATA POINT ABOVE
df.resample('M').mean() #MEAN OF ALL THE VALUES FOR VARIABLES COUNT1 COUNT2 IN DF
df.resample('M').sum() #SUM OF ALL THE VALUES FOR VARIABLES COUNT1 COUNT2 IN DF
df['2017'] #PARTIAL STRING INDEXING TO FIND  VALUES THAT HAVE 2017 DATE
df['2016-12'] #PARTIAL STRING INDEXING TO FIND ALL DECEMBER DATES
df['2016-12':] #PARTIAL STRING INDEXING TO FIND ALL DATES STARTING DEC 2016+
df.asfreq('W', method='ffill') #FILL IN WEEKLY INFO WITH THE PREVIOUS NON-MISSING
#VALUES BEFORE THAT WEEK


###VISUALIZATION PLOTS
import matplotlib.pyplot as plt
%matplotlib inline

df.plot()
