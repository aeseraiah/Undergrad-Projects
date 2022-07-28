import quandl, math
import pandas as pd
import numpy as np
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

df = quandl.get('WIKI/GOOGL')


df = df[['Adj. Open', 'Adj. High', 'Adj. Low', 'Adj. Close', 'Adj. Volume']]

#print(df.columns)

df['HL_PCT'] = (df['Adj. High'] - df['Adj. Close']) / df['Adj. Close'] * 100.0
df['PCT_change'] = (df['Adj. Close'] - df['Adj. Open']) / df['Adj. Open'] * 100.0

df = df[['Adj. Close', 'HL_PCT', 'PCT_change', 'Adj. Volume']]


forecast_col = 'Adj. Close'

#this treats NaNs as outliers, rather than getting rid of data
df.fillna(-99999, inplace=True)

#math.ceil rounds values up to the nearest whole number 
#.01 is representing 1%. We want to predict out 1% of our data
#label col for each row will be the adj close price "35 days" or 1% into the future 

forecast_out = int(math.ceil(0.10*len(df)))
print(forecast_out)

df['label'] = df[forecast_col].shift(-forecast_out)

#dropping the labels not predicted yet, have NaNs
df.dropna(inplace=True) 

#print(df.head(36))

#df.drop returns new dataframe, then np.array converts it into an array. The 1 is axis=1 (column)
X = np.array(df.drop(['label'], 1))
y = np.array(df['label'])

X = preprocessing.scale(X) #SKIP IF USING LIVE DATA
#any new data will need to be prescaled before being evaluated on trained model
#new data needs to be scaled along side your training data,
#---> MEANING: the step of preprocessing input (training) data is usually skipped on live data


#Syntax of splicing: X[start:end:step]
#all values in array, except for the last nth rows+1 where n=forecast_out
# this way we only have X's for values we have y
#NOT NEEDED SINCE WE DROPPED NAN VALUES ABOVE
#X = X[:-forecast_out+1]

y = np.array(df['label'])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=4)


clf = LinearRegression().fit(X_train, y_train)
metric = clf.score(X_test, y_test)
print(metric)
