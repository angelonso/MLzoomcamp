# -*- coding: utf-8 -*-
"""
Created on Sun Sep 29 17:53:33 2024

@author: ES72192728Y
"""
import pandas as pd
import numpy as np

q1=pd.__version__

laptops=pd.read_csv('laptops.csv')

q2=laptops.count()[0]

laptops.describe()

laptops.info()

q3=laptops["Brand"].value_counts().count()

laptops.isna().sum()

q4=2

q5=laptops['Final Price'][laptops['Brand']=='Dell'].max()

q6_1=laptops['Screen'].median()
q6_2=laptops['Screen'].mode()
laptops_filled_screen=laptops['Screen'].fillna(laptops['Screen'].mode()[0])
q6_3=laptops_filled_screen.median()

innjoo_laptops=laptops[laptops['Brand']=='Innjoo'][['RAM','Storage','Screen']]
x=innjoo_laptops.to_numpy()
XTX = x.T @ x
XTX_inv = np.linalg.inv(XTX)
y = np.array([1100, 1300, 800, 900, 1000, 1100])
w = XTX_inv @ x.T @ y
q7 = np.sum(w)