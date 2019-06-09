# -*- coding: utf-8 -*-
"""
Spyder Editor

Este é um arquivo de script temporário.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from IPython import get_ipython

df = pd.read_csv('https://bit.ly/2WGzsWU')

#print(df.head())

#df.info()

get_ipython().run_line_magic('matplotlib', 'inline')

#df.plot.scatter('OfficeVisits', 'Narcotics', c='PoorCare', cmap='bwr')

from sklearn.model_selection import train_test_split

feat_list = list(df.columns)
feat_list.remove('PoorCare')
X = df[feat_list]
Y = df['PoorCare']

train_data, test_data, train_target, test_target = \
train_test_split(X, Y, train_size=0.75)

from sklearn.linear_model import LogisticRegression
#metodo de newton para
logreg = LogisticRegression(solver='newton-cg')
logreg.fit(train_data, train_target)


y_pred = logreg.predict(test_data)

print(test_data)
print(y_pred)

print(df.iloc[48])

