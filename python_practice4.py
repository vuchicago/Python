# -*- coding: utf-8 -*-
import pandas as pd
import numpy as np

T=np.random.binomial(10000,.5,size=20) #Flip a coin 10,000 times and do it 20 simulations
S=np.random.binomial(20,.5,size=10000) #FLip a coin 20 times for 10,000 simulations
len(S[S>=15])/10000

torn_prob=.01
prob=np.random.binomial(1,torn_prob,1000000)

two_in_row=0
for i in range(1,len(prob)):
    if prob[i]==1 and (prob[i+1]==1):
        two_in_row+=1

print('{}-two tornados in a row in {} years'.format(two_in_row,1000000/365) )  

u=np.random.uniform(0,1,size=10000000) #Normal Distribution ith mean 0, std=1

np.random.normal(1) #Normal distribution with mean 1

distribution = np.random.normal(0.8,size=1000000) #Normal distribution with mean .8 and 10000000 simulations

standard_dev=np.sqrt(np.sum((np.mean(distribution)-distribution)**2)/len(distribution)) #formula for std

np.std(distribution) #Built in python numpy std 


#######
import scipy.stats as stats

stats.kurtosis(distribution)

chisquared_2=np.random.chisquare(2,1000)
chisquared_10=np.random.chisquare(10,1000)
chisquared_20=np.random.chisquare(20,1000)
chisquared_30=np.random.chisquare(30,1000)
stats.skew(chisquared_2)
stats.skew(chisquared_10)

%matplotlib inline
import matplotlib as plt
import matplotlib.pyplot as plt
output=plt.hist([chisquared_2,chisquared_10,chisquared_20,chisquared_30],bins=50,histtype='step',
                label=["2 df","10 df","20 df","30 df"])
plt.legend(loc="upper right")


#######
df=pd.read_csv("grades.csv")
early = df[df['assignment1_submission'] <= '2015-12-31']
late = df[df['assignment1_submission'] > '2015-12-31']
early.mean()
late.mean()

from scipy import stats
stats.ttest_ind?
stats.ttest_ind(early['assignment1_grade'], late['assignment1_grade'])
stats.ttest_ind(early['assignment2_grade'], late['assignment2_grade'])
stats.ttest_ind(early['assignment3_grade'], late['assignment3_grade'])
