#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 24 00:36:03 2017

@author: Vuchicago
"""

import os
os.chdir("/Users/vu/Documents/Courses/Python Class")
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

plt.figure()
plt.subplot(1,2,1)
linear_data=np.array([1,2,3,4,5,6,7,8])
plt.plot(linear_data,'-o')
exponential_data=linear_data**2
quad_data=linear_data**3;
##the axis is wrong
plt.subplot(1,2,2)
plt.plot(exponential_data,'-o')
##fixes the axis after doing this, but it is inconvenient
plt.subplot(1,2,1)
plt.plot(exponential_data,'-d')

###This will allow you to adjust axis accordingly
plt.figure()
ax1=plt.subplot(1,2,1)
plt.plot(linear_data,'-o')
ax2=plt.subplot(1,2,2,sharey=ax1)
plt.plot(exponential_data,'-x')

#####CREATE A 3X3 COLLECTION OF GRAPHS
###ASSIGN THE FIRST GRAPH TO AX1, 5TH TO AX5, 9TH TO AX9

fig,((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9))=plt.subplots(3,3,sharex=True,sharey=True)
ax1.plot(linear_data,'-x')
ax5.plot(exponential_data,'-o')
ax9.plot(quad_data,'-v')

###This will individually set all the subplot labels.  Not necessary now but
#code might be useful
#for ax in plt.gcf().get_axes():
 #   for label in ax.get_xticklabels() + ax.get_yticklabels():
  #      label.set_visible(True)
  
###HISTOGRAMS
  ##CREATE A 2X2 COLLECTION OF HISTOGRAMS THAT DEALS WITH SAMPLE SIZE
fig,((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,sharex=True)
axs=[ax1,ax2,ax3,ax4]
for n in range(0,len(axs)):
    sample_size=10**(n+1)
    sample=np.random.normal(loc=0.0,scale=1.0,size=sample_size)
    axs[n].hist(sample,color='#1F77B4',bins=30)
    axs[n].set_title('n={}'.format(sample_size))
    
###gridspec
#CREATE A GRID THAT ALLOWS YOU TO PLOT MULTIPLE PLOTS IN 1 CHART
import matplotlib.gridspec as gridspec

plt.figure(figsize=(8,6))
gspec=gridspec.GridSpec(3,3)
top_histogram=plt.subplot(gspec[0,1:])
side_histogram=plt.subplot(gspec[1,0])
lower_right=plt.subplot(gspec[1:,1:])

y=np.random.normal(loc=0,scale=1.0,size=10000)
x=np.random.random(size=10000)
lower_right.scatter(x,y)
top_histogram.hist(x,bins=100)
s=side_histogram.hist(y,bins=100,orientation='horizontal')

#clearing the previous top and size histograms and normalizing it first
top_histogram.clear()
top_histogram.hist(x,bins=100,normed=True)
side_histogram.clear()
side_histogram.hist(y,bins=50,orientation='horizontal',normed=True,color='#1F77B4')
side_histogram.invert_xaxis()
###Changing the x and y axis limits for the lower right and top histogram
for ax in [top_histogram,lower_right]:
    ax.set_xlim(0,1)
for ax in [side_histogram,lower_right]:
    ax.set_ylim(-5,5)

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 8}
mpl.rc('font', **font)

########BOXPLOT
import pandas as pd
normal_sample=np.random.normal(loc=0.0,scale=1.0,size=10000)
random_sample=np.random.random(size=10000)
gamma_sample=np.random.gamma(2,size=10000)
df=pd.DataFrame({'normal':normal_sample,
                'random':random_sample,
                'gamma':gamma_sample})
df.describe() ###SUMMARY STATISTICS of a dataframe

plt.figure()
_=plt.boxplot(df['normal'],whis='range')

plt.clf() ###clear the currention figure
_=plt.boxplot([df['normal'],df['random'],df['gamma']],whis='range')

plt.figure()
_=plt.hist(df['gamma'],bins=100)

##PUT MULTIPLE GRAPHS IN 1 CHART
import mpl_toolkits.axes_grid1.inset_locator as mpl_il
plt.figure()
plt.boxplot([df['normal'],df['random']],whis='range')
ax2=mpl_il.inset_axes(plt.gca(),width='60%',height='40%',loc=2)
ax2.hist(df['gamma'],bins=100)
ax2.margins(x=.5)
ax2.yaxis.tick_right()
####REGULAR BOXPLOT WITH OUTLIER POINTS
plt.figure()
_=plt.boxplot([df['normal'],df['random'],df['gamma']])


#####HEATMAPS
plt.figure()
y=np.random.normal(loc=0.0,scale=1.0,size=10000)
x=np.random.random(size=10000)
_=plt.hist2d(x,y,bins=25)

###THE MORE BINS THERE ARE, THE MORE SATURATED THE MAP
plt.figure()
_=plt.hist2d(x,y,bins=100)
plt.colorbar()

######ANIMATION#####
#####BACKEND LAYER DOES MOST OF THE HEAVY LIFTING FOR ANIMATION
###AND INTERACTIVITY

import matplotlib.animation as animation
n=100
x=np.random.randn(n)
def update(curr):
    if curr==n:
        a.event_source.stop()
    plt.cla() #clear current axis
    bins=np.arange(-4,4,.5)
    plt.hist(x[:curr],bins=bins)
    plt.axis([-4,4,0,30])
    plt.gca().set_title('sampling the normal distributon')
    plt.gca().set_ylabel('Frequency')
    plt.gca().set_xlabel('Value')
    plt.annotate('n={} at {} bins'.format(curr,bins),[2,27])
    
fig=plt.figure()
a=animation.FuncAnimation(fig,update,interval=100)

####INTERACTIVITY
plt.figure()
data=np.random.rand(10)
plt.plot(data)

def onclick(event):
    plt.cla()
    plt.plot(data)
    plt.gca().set_title('Event at pixels {}, {} {} and data {},{}'.
           format(event.x,event.y,'\n',event.xdata,event.ydata))

plt.gcf().canvas.mpl_connect('button_press_event',onclick)


origins=['China','Brazil','India','USA','Canada','UK','Germany',
         'Iraq','Chile','Mexico']
import random
random.shuffle(origins)

df=pd.DataFrame({'height':np.random.rand(10),
                 'weight':np.random.rand(10),
                 'origin': origins})
plt.figure()
plt.scatter(df['height'],df['weight'],picker=5)
plt.gca().set_ylabel('height')
plt.gca().set_xlabel('weight')

def onpick(event):
    origin=df.iloc[event.ind[0]]['origin']
    plt.gca().set_title('Selected item came from {}'.format(origin))
plt.gcf().canvas.mpl_connect('pick event',onpick)