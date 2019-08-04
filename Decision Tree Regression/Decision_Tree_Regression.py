# -*- coding: utf-8 -*-
"""
Created on Sun Aug  4 15:06:29 2019

@author: jigyasa
"""
# Importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Importing the dataset
df=pd.read_csv('Position_Salaries.csv')
x=df.iloc[:,1:2].values
y=df.iloc[:,2].values

# Fitting the Decision Tree Regression to the dataset.
from sklearn.tree import DecisionTreeRegressor
regressor=DecisionTreeRegressor(random_state=0)
regressor.fit(x,y)

# Predicting the result for a particular position.
y_pred=regressor.predict(6.5)
print(y_pred)

# Visualising the result of Decision Tree Regression.
x_grid=np.arange(min(x),max(x),0.01)
x_grid=x_grid.reshape((len(x_grid),1))
plt.scatter(x,y,color='red')
plt.plot(x_grid,regressor.predict(x_grid),color='blue')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.title('Truth or Lie(Decsion Tree Regression')
plt.show()
