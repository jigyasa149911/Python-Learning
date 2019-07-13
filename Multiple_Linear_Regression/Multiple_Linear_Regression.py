# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 13:19:56 2019

@author: jigyasa
"""
# Importing the Libraaries.

import pandas as pd

#Importing the Dataset.
df=pd.read_csv('startup.csv')
print(df)

# Splitting the Dataset into Independent and Dependent Variables.
x=df.iloc[:,:-1].values
y=df.iloc[:,4].values

# Encoding the Categorical Data
from sklearn.preprocessing import LabelEncoder , OneHotEncoder
labelencoder=LabelEncoder()
x[:,3]=labelencoder.fit_transform(x[:,3])
onehotencoder=OneHotEncoder(categorical_features=[3])
x=onehotencoder.fit_transform(x).toarray()

# Avoiding Dummy Variable Trap.
x=x[:,1:]

#Splitting the dataset into training and testing sets.
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2,random_state=0)

# Fitting multiple linear regression to training set.
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
regressor.fit(x_train,y_train)

# Predicting the testing set results.
y_pred=regressor.predict(x_test)

# Checking the correctness of the prediction.
from sklearn.metrics import r2_score
print('r2_score is %f',r2_score(y_test,y_pred))