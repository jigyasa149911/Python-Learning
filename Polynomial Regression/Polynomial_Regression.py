# -*- coding: utf-8 -*-
"""
Created on Sun Jul 28 20:26:17 2019

@author: jigyasa
"""
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data= pd.read_csv('salary.csv',delimiter='\t')


x=data.iloc[:,1:2].values
y=data.iloc[:,2].values



#fitting linear regression to the dataset
from sklearn.linear_model import LinearRegression
lin=LinearRegression()
lin.fit(x,y)
plt.scatter(x,y)


# fitting polynomial regression to the dataset
from sklearn.preprocessing import PolynomialFeatures
poly=PolynomialFeatures(degree=4)
x_poly=poly.fit_transform(x)
poly.fit(x_poly,y)
lin2=LinearRegression()
lin2.fit(x_poly,y)

#visualising the result of Linear Regression
plt.scatter(x,y,color='blue')
plt.plot(x,lin.predict(x),color='red')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.title('Truth or Bluff(Linear Regression)')
plt.show()
#visualising the result of Polynomial regression
plt.scatter(x,y,color='blue')
plt.plot(x,lin2.predict(poly.fit_transform(x)),color='red')
plt.xlabel('Position')
plt.ylabel('Salary')
plt.title('Truth or Bluff(Polynomial Regression)')
plt.show()

