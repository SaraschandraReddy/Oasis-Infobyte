# -*- coding: utf-8 -*-
"""Sales Prediction.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1E1pjVk2CB7I3EV4nmPtikplOjDlazFXq
"""

#importing the all necessary packages
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


#reading the dataset in CSV format
df=pd.read_csv("Advertising.csv")
df.head()

#represent the head part of the dataset
df.drop('Unnamed: 0',axis=1, inplace= True)
df.head()

#gives the information about the dataset
df.info()

#description about the dataset
df.describe()

df.head()

#represent the all columns in the dataset
df.columns

#visualizing between the Columns TV and Sales
plt.figure(figsize=(15,6))
sns.lineplot(x=df['TV'],y=df['Sales'])

#visualizing between the Radio TV and Sales
plt.figure(figsize=(15,6))
sns.lineplot(x=df['Radio'],y=df['Sales'])

#visualizing between the Newspaper TV and Sales
plt.figure(figsize=(15,6))
sns.lineplot(x=df['Newspaper'],y=df['Sales'])

#dividing the features and labels
X=df.iloc[: ,:-1]
Y=df.iloc[: ,-1]
X.head()

Y.head()

#splitting the dataset for training and testing
from sklearn.model_selection import train_test_split
X_train , X_test , Y_train ,Y_test = train_test_split(X , Y , test_size=0.3 , random_state=101)
print(X.shape)
print(X_train.shape)
print(X_test.shape)

print("X_train: ")
print(X_train.head())
print()
print("X_test: ")
print(X_test.head())
print()
print("Y_train: ")
print(Y_train.head())
print()
print("Y_test: ")
print(Y_test.head())

#using regressor
from xgboost import XGBRegressor
model=XGBRegressor()

model.fit(X_train  , Y_train)

#caluclating the mean 
pred=model.predict(X_test)

from sklearn.metrics import mean_absolute_error , mean_squared_error ,r2_score
mae=mean_absolute_error(Y_test , pred)
mse=mean_squared_error(Y_test , pred)
r2=r2_score(Y_test , pred)

print("Mean absolute error: {}".format(mae))
print("Mean squared error: {}".format(mse))

print("r2 score: {}".format(r2))

#giving the new values to predicts the sales
tv=float(input("Cost of TV : "))
radio=float(input("Cost of Radio : "))
newspaper=float(input("Cost of newspaper : "))

arr=[tv , radio , newspaper]
arr=np.array(arr)
arr=arr.reshape(1 , -1)

result=model.predict(arr)
print("Sales : {}".format(result))