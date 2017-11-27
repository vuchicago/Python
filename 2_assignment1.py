#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jul 30 19:05:01 2017

@author: Vuchicago
"""
##CHANGING DIRECTORIES
import os
os.chdir("/Users/vu/Documents/Courses/Python Class")
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np


Weather=pd.read_csv("Weather.csv")


Weather.index=pd.to_datetime(Weather["Date"])
Weather=Weather.sort_values(by="Date")
Weather["Temp(C)"]=Weather["Data_Value"]/10
Weather["Month"]=Weather.index.month
##Make month into a two digit number with leading 0s if single number
Weather["Month"]=Weather["Month"].apply(lambda x: '{:02d}'.format(x))
Weather["Day"]=Weather.index.day
###Make day of month into two digit number 
Weather["Day"]=Weather["Day"].apply(lambda x: '{:02d}'.format(x))
##Combining month of the year and day of month to create unique values for each
###month-day combination.  Once we delete leap days, we should
###have 365 unique combinations per yar corresopnding to unique day
Weather["Monthday"]=Weather["Month"]+Weather["Day"]
Weather= Weather[~((Weather.index.month==2) & (Weather.index.day==29))]
Weather_pre=Weather[Weather.index.year<2015]
Weather_post=Weather[Weather.index.year==2015]
High=Weather_pre.groupby("Monthday").max().reset_index()
High["idx"]=High.index+1
High=High.set_index("idx")
High=High["Temp(C)"]
Low=Weather_pre.groupby("Monthday").min().reset_index()
Low["idx"]=Low.index+1
Low=Low.set_index("idx")
Low=Low["Temp(C)"]
Record_high=Weather_post["Temp(C)"].groupby(Weather_post.index.dayofyear).max()
Record_low=Weather_post["Temp(C)"].groupby(Weather_post.index.dayofyear).min()
Record_high=Record_high[Record_high>High]
Record_low=Record_low[Record_low<Low]

"""
This is wrong because of leap year days
High=Weather[Weather.index.year<2015]["Temp(C)"].groupby(by=Weather[Weather.index.year<2015].index.dayofyear).max()
Low=Weather[Weather.index.year<2015]["Temp(C)"].groupby(by=Weather[Weather.index.year<2015].index.dayofyear).min()
Record_high=Weather[Weather.index.year==2015]["Temp(C)"].groupby(by=Weather[Weather.index.year==2015].index.dayofyear).max()
Record_low=Weather[Weather.index.year==2015]["Temp(C)"].groupby(by=Weather[Weather.index.year==2015].index.dayofyear).min()
"""

Weather=Weather.reset_index(drop=True)

plt.figure(figsize=(7,4))
plt.plot(High,'-',color='red')
plt.plot(Low,'-',color='blue')
plt.plot(Record_high,'^',color='navy')
plt.plot(Record_low,'v',color='sienna')

#plt.plot(Record_low,'.',color='red')
plt.gca().fill_between(range(1,(len(High)+1)), 
                       High, Low, 
                       facecolor='#1F77B4', 
                       alpha=0.3)


plt.legend(["High","Low","2015 Record Highs","2015 Record Lows"],loc=4, bbox_to_anchor=(1, -.4),
           frameon=True, title='Legend',prop={'size': 8})

plt.tick_params(top='off', bottom='off', left='off', 
                right='off', labelleft='off', labelbottom='on')
#The following will create a x range from Jan to December
#strftime('%-j') indicates day of the year as padded decimal number
xticks=(pd.date_range('1/1/2015','31/01/2016',freq='M')-1+pd.Timedelta('1D')).strftime('%-j').astype(int)
#Labels the month that the days of the years that were created above
xticks_label=pd.to_datetime(xticks,format='%j').strftime('%b')
#create a font
font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 12}
mpl.rc('font', **font)
#mpl.rc('xtick', labelsize=9) #if you want to control xtick size
#mpl.rc('ytick', labelsize=9) #ytick size option
#Get Current axis.  This will get the axis info and you can manipulate axis
ax1=plt.gca()
ax1.grid(False)
ax1.set_xlabel('Month')
ax1.set_ylabel('Temperature(C)')
ax1.set_xlim(1,365)
ax1.set_xticks(xticks)
plt.margins(.1)
ax1.set_xticklabels(xticks_label)
#Creates dual-axes
ax2 = ax1.twinx()
ax2.grid(False)
ax2.set_yticks(list(map(lambda x: (x * 1.8) + 32, ax1.get_yticks())))
ax2.set_ylabel('Temperature(F)')
plt.title('Illinois Temperature Highs and Lows (2005-2014) \n & Records Set in 2015')
for spine in ax1.spines.values():
    spine.set_visible(False)
for spine in ax2.spines.values():
    spine.set_visible(False)

######BOXPLOT

import pandas as pd
normal_sample=np.random.normal(loc=0,scale=1.0,size=10000)
random_sample=np.random.random(size=10000)
gamma_sample=np.random.gamma(2,size=10000)
df=pd.DataFrame({'normal':normal_sample,
                 'random':random_sample,
                 'gamma':gamma_sample})
df.describe()
plt.figure()
_=plt.boxplot(df['normal'],whis='range')
plt.clf()
_=plt.boxplot([df['normal'],df['random'],df['gamma']],whis='range')
plt.figure()
_=plt.hist(df["gamma"],bins=100)

import mpl_toolkits.axes.grid1.inset_locator as mpl_il
plt.figure()
plt.boxplot([df['normal'],df['random']],whi='range')
ax2=mpl_il.inset_axes(plt.gca(),width='60%',height='40%',loc=2)
ax2.hist(df['gamma'],bin=100)
ax2.margins(x=.5)
ax2.yaxis.tick_rifht()
plt.figure()
_=plt.boxplot([df['normal'],df['random'],df['gamma']])
########HEATMAP
plt.figure()
Y=np.random.normal(loc=0.0,scale=100,size=10000)
X=np.random.random(size=10000)
_=plt.hist2d(X,Y,bins=25)


#####ANIMATION
import matplotlib.animation as animation

n=100
x=np.random.randn(n)
def update(curr):
    if curr==n:
        a.event_source.stop()
    plt.cla()
    bins=np.arange(-4,4,.5)
    plt.hist(x[:curr],bins=bins)
    plt.axis([-4,4,0,30])
    plt.gca().set_title('Sample the Norma Distribution')
    plt.gca().set_ylabel('Frequency')
    plt.gca().set_xlabel('Value')
    plt.annotate('n={}'.format(curr),[3,27])
    
fig=plt.figure()

a=animation.FuncAnimation(fig,update,interval=100)

######INTERACTIVITY
plt.figure()
data=np.random.rand(10)
plt.plot(data)
def onclick(event):
    plt.cla()
    plt.plot(data)
    plt.gca().set_title('Event at Pixels {} {} {} and data{},{}'.format(event.x,event.y,'\n',event.xdata,event.ydata))
    
plt.gcf().canvas.mpl_connect('button_press_event',onclick)

from random import shuffle
origins=['China','Brazil','India','USA','Canada','UK','Germany','Iraq','Chile','Mexico']
shuffle(origins)
df=pd.DataFrame({'height':np.random.rand(10),
                 'weight':np.random.rand(10),
                 'origin':origins})
plt.figure()
plt.scatter(df['height'],df['weight'],picker=5)
plt.gca().set_ylabel('height')
plt.gca().set_xlabel('weight')

def onpick(event):
    origin=df.iloc[event.ind[0]]['origin']
    plt.gca().set_title('selected item came from {}'.format(origin))
    
plt.gcf().canvas.mpl_connect('pick event',onpick)