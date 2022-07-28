import pandas_datareader as pdr
import pandas_datareader.data as web
import datetime as dt
import numpy as np
import pandas as pd
import math
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler

#Reading in S&P 500, Ticker symbol = ^GSPC
df = web.DataReader('^GSPC', 'yahoo', start='2020-10-20', end='2022-07-25')

df = df[['High', 'Low', 'Open', 'Close', 'Volume', 'Adj Close']]
#print(df.head)

df['HL_PCT'] = (df['High'] - df['Close']) / df['Close'] * 100.0
df['HL_PCT_adj'] = (df['High'] - df['Adj Close']) / df['Adj Close'] * 100.0
df['PCT_change'] = (df['Adj Close'] - df['Open']) / df['Open'] * 100.0

df = df[['Adj Close', 'HL_PCT', 'HL_PCT_adj', 'PCT_change', 'Volume']]

#print(df.head)

forecast_col = 'Adj Close'

#this treats NaNs as outliers, rather than getting rid of data
df.fillna(-99999, inplace=True)

#math.ceil rounds values up to the nearest whole number 
#.1 is representing 10%. We want to predict out 10% of our data
#10% = % days worth of previous data to predict tomorrow?

forecast_out = int(math.ceil(0.01*len(df)))
#print(forecast_out)

df['label'] = df[forecast_col].shift(-forecast_out)

#dropping the labels not predicted yet, have NaNs
df.dropna(inplace=True) 


#print(df.head(36))

#df.drop returns new dataframe, then np.array converts it into an array. The 1 is axis=1 (column)
X = np.array(df.drop(['label'], 1))
y = np.array(df['label'])


#SKIP IF USING LIVE DATA
#X = preprocessing.scale(X)
#any new data will need to be prescaled before being evaluated on trained model
#new data needs to be scaled along side your training data,
#---> MEANING: the step of preprocessing input (training) data is usually skipped on live data


#Syntax of splicing: X[start:end:step]
#all values in array, except for the last nth rows+1 where n=forecast_out
# this way we only have X's for values we have y
#NOT NEEDED SINCE WE DROPPED NAN VALUES ABOVE
#X = X[:-forecast_out+1]

y = np.array(df['label'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#.fit_transform:
#The fit method is calculating the mean and variance of each of the features present in our data. 
#The transform method is transforming all the features using the respective mean and variance.
sc = StandardScaler()
X_train = sc.fit_transform(X_train)

#.transform:
#
X_test = sc.transform(X_test)

#classifer = clf = LinearRegression
#n_jobs allows you to thread
clf_linear = LinearRegression(n_jobs=10).fit(X_train, y_train)
metric = clf_linear.score(X_test, y_test)
metric_cv = cross_val_score(clf_linear, X_test, y_test, cv=5)
print(metric)
print(metric_cv)
print(np.mean(metric_cv))

#classifer = clf = SVM
clf_svm = svm.SVR(kernel='linear').fit(X_train, y_train)
metric = clf_svm.score(X_test, y_test)
metric_cv = cross_val_score(clf_svm, X_test, y_test, cv=5)
print(metric)
print(metric_cv)
print(np.mean(metric_cv))

#print(y_train, "\n")
#print(y_test)

#NEXT STEPS:
#1) Figure out why metric and metric_cv for clf_svm is so different. 