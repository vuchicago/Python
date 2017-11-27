#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 31 18:33:48 2017

@author: Vuchicago
"""

import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
import mpl_toolkits.axes_grid1.inset_locator as mpl_il
from matplotlib import cm

# generate 4 random variables from the random, gamma, exponential, and uniform distributions
x1 = np.random.normal(-2.5, 1, 10000)
x2 = np.random.gamma(2, 1.5, 10000)
x3 = np.random.exponential(2, 10000)+7
x4 = np.random.uniform(14,20, 10000)
n=[x1,x2,x3,x4]

def update(curr):
    x1 = np.random.normal(-2.5, 1, curr*200)
    x2 = np.random.gamma(2, 1.5, curr*200)
    x3 = np.random.exponential(2, curr*200)+7
    x4 = np.random.uniform(14,20, curr*200)
    n=[x1,x2,x3,x4]
    plt.cla()
    #bins=np.arange(0,100,2)
    bins=np.max([curr*2,10])
    plt.axis([-7,21,0,0.6])
    plt.hist(n,normed=True,bins=bins,alpha=.5)
    plt.annotate('n={} at bins={}'.format(curr,bins),[0,.4])
    plt.text(x1.mean()-1.5, 0.5, 'x1\nNormal')
    plt.text(x2.mean()-1.5, 0.5, 'x2\nGamma')
    plt.text(x3.mean()-1.5, 0.5, 'x3\nExponential')
    plt.text(x4.mean()-1.5, 0.5, 'x4\nUniform')
    if curr==50:
        a.event_source.stop()
fig=plt.figure()
a=animation.FuncAnimation(fig,update,interval=50)
###########################
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.gridspec as gridspec
import matplotlib.animation as animation
from scipy import stats
import matplotlib.colors as mcol

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
y_pos=np.arange(len(df.index))
value=df.mean(axis=1)

plt.figure()
xvalues=['1992','1993','1994','1995']
stde=stats.sem(np.transpose(df))

#### GUY USED THIS FORMULA FOR THEIR STANDARD ERROR
yerr = np.std(df,axis=1) / np.sqrt(df.shape[1]) * stats.t.ppf(1-0.05/2, df.shape[1]-1)
####
std=np.transpose(df).std()
threshold=40000


cm1 = mcol.LinearSegmentedColormap.from_list("MyCmapName",["b", "white", "purple"])
cm2= mcol.LinearSegmentedColormap.from_list("MyCmapName",["b", "white", "red"])
cpick = cm.ScalarMappable(cmap=cm1)
cpick2= cm.ScalarMappable(cmap=cm2)
cpick.set_array([])
cpick2.set_array([])




#plot = plt.scatter(value, value, c = value, cmap = 'hsv')
#plt.colorbar(plot)

bars=plt.bar(y_pos,value,yerr=2*stde,color='b')



percentages = []
y_err=2*stde
###For each bar/standard error combo, it'll create a percentage
###for its value based on it's confidence interval

for bar, y_err in zip(bars, y_err):
    low = bar.get_height() - y_err
    high = bar.get_height() + y_err
    percentage = (high-threshold)/(high-low)
    if percentage>1: percentage = 1
    if percentage<0: percentage=0
    percentages.append(percentage)
percentages


colour=cpick.to_rgba(percentages)
colors=cpick2.to_rgba(percentages)

bars=plt.bar(y_pos,value,yerr=2*stde,color=colors)
plt.colorbar(cpick2, orientation='horizontal')
plt.xticks(y_pos,xvalues,alpha=.2)
plt.axhline(y=threshold, zorder=0)
plt.title('Confidence Level Thresholds')