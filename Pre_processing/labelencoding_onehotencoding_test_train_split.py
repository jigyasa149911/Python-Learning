# -*- coding: utf-8 -*-
"""
Created on Fri Jul  5 22:04:13 2019

@author: jigyasa
"""

#import numpy as np
import pandas as pd

df=pd.read_csv('data.csv')
print(df)

X=df.iloc[:,:-1].values
y=df.iloc[:,3].values

from sklearn.preprocessing import Imputer
imputer=Imputer(missing_values='NaN',strategy='mean',axis=0)
imputer=imputer.fit(X[:, 1:3])
X[:, 1:3]=imputer.transform(X[:, 1:3])


#Encoding the categorical variables.
#Encoding the independent variable
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
labelencoder_X=LabelEncoder()
X[:, 0]=labelencoder_X.fit_transform(X[:, 0])

# Creating Dummy Variable.
onehotencoder=OneHotEncoder(categorical_features=[0])
X=onehotencoder.fit_transform(X).toarray()
print(X)
#Encoding the dependent variable.
labelencoder_y=LabelEncoder()
y=labelencoder_y.fit_transform(y)
print(y)
# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=0)



