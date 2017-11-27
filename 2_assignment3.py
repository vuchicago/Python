#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 19 22:00:21 2017

@author: Vuchicago
"""


import os
os.chdir("/Users/vu/Documents/Courses/Python Class")
import pandas as pd
import matplotlib as mpl
import matplotlib.pyplot as plt
import datetime as dt
import numpy as np

Chicago=pd.read_csv("Chicago-Crime_One_year_prior_to_present.csv")
Chicago.rename(columns={'DATE  OF OCCURRENCE':"Date"},inplace=True)
Chicago.Date=pd.to_datetime(Chicago.Date)
