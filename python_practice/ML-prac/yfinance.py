import pandas_datareader as pdr
import pandas_datareader.data as web
import datetime as dt
from datetime import timedelta, date
import numpy as np
import pandas as pd
import math
from sklearn import preprocessing, svm
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')

#Reading in S&P 500, Ticker symbol = ^GSPC
df = web.DataReader('AMZN', 'yahoo', start='2001-10-20', end=dt.date.today())

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

#print(df.head)
#print(len(df))

#math.ceil rounds values up to the nearest whole number 
#.01 is representing 1%. We want to predict out 1% of our data
#1% = 5 days worth of previous data to predict tomorrow?

forecast_out = int(math.ceil(0.1*len(df)))
#print("forecast_out:", forecast_out,"\n")


df['label'] = df[forecast_col].shift(-forecast_out)

#print(df.tail(36))

#df.drop returns new dataframe, then np.array converts it into an array. The 1 is axis=1 (column)
X = np.array(df.drop(['label'], 1))

X = preprocessing.scale(X)

#X_lately is the stuff we're predicting against. We don't have y values for these X values
#each y value/label is the predicted value for 5 days (1%) in the future 
#X_lately shows data for the last 5 days (last 1%) of entire dataset/frame
X_lately = X[-forecast_out:]

#Syntax of splicing: X[start:end:step]
#X shows all the data before the last 5 days (99%) of the entire dataset/frame
# this way we only have X's for values we have y
X = X[:-forecast_out]

#print(X_lately)
#print(X)

#dropping the labels not predicted yet, have NaNs
df.dropna(inplace=True) 
#print("NEW DF", df)
y = np.array(df['label'])


#SKIP IF USING LIVE DATA
#X = preprocessing.scale(X)
#any new data will need to be prescaled before being evaluated on trained model
#new data needs to be scaled along side your training data,
#---> MEANING: the step of preprocessing input (training) data is usually skipped on live data

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

#.fit_transform:
#The fit method is calculating the mean and variance of each of the features present in our data. 
#The transform method is transforming all the features using the respective mean and variance.

#sc = StandardScaler()
#X_train = sc.fit_transform(X_train)

#.transform:
#X_test = sc.transform(X_test)

#classifer = clf = LinearRegression
#n_jobs allows you to thread
clf_linear = LinearRegression(n_jobs=10).fit(X_train, y_train)

#PICKLING THE MODEL
#with open('linearregression.pickle', 'wb') as f:
#    pickle.dump(clf_linear, f)
#pickle_in = open('linearregression.pickle', 'rb')
#clf = pickle.load(pickle_in)


metric_linear = clf_linear.score(X_test, y_test)
metric_cv = cross_val_score(clf_linear, X_test, y_test, cv=5)

#print(metric_linear)
#print(metric_cv)
#print(np.mean(metric_cv))

#classifer = clf = SVM
clf_svm = svm.SVR(kernel='linear').fit(X_train, y_train)
metric_svm = clf_svm.score(X_test, y_test)
metric_cv = cross_val_score(clf_svm, X_test, y_test, cv=5)

#print(metric_svm)
#print(metric_cv)
#print(np.mean(metric_cv))

#NEXT STEPS:
#1) Figure out why metric and metric_cv for clf_svm is so different. 

forecast_set_linear = clf_linear.predict(X_lately)
forecast_set_svm = clf_svm.predict(X_lately)



#finding minimums of forecasts using linear regression model and linear svm


print("\nforecasted stock prices using linear regression:\n", forecast_set_linear, "\n\nlinear_metric:\n", metric_linear, "\n\ndays out:\n", forecast_out)
#print("\nforecasted stock prices using linear svm:\n", forecast_set_svm, "\n\nsvm metric:\n", metric_svm, "\n\ndays out:\n", forecast_out)

df['Forecast'] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

for i in forecast_set_linear:
    next_date = dt.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

print(df)




min_LR = min(forecast_set_linear)
#print("\nmin_LR\n", min_LR)
min_svm = min(forecast_set_svm)
#print("\nmin_svm\n", min_svm)

#for min in range(len(forecast_set_linear)):
    #if forecast_set_linear[min] == min_LRz:
        #print(min)


def daterange(start_date, end_date):
    for n in range(int ((end_date - start_date).days)):
        yield start_date + timedelta(n)

#here you could ask for user info with sys.argv
start_date = date(2001, 10, 20)
end_date = date(2022, 7, 29)
#end_date = now = dt.datetime.now().strftime('%Y-%m-%d')
#print(end_date)


concat_list = []
for single_date in daterange(start_date, end_date):
    list = [single_date.strftime("%Y-%m-%d")]
    concat_list = concat_list + list

#print(concat_list)

#print(concat_list)
b = np.asarray(concat_list)
c = concat_list[-523:]
#print(len(c))
#print(c)

def time(days_out):
    now = dt.datetime.now()
    e = (now + dt.timedelta(days=days_out)).strftime('%Y-%m-%d')
    #print(e)

time(492)
#time(min)

df['Adj Close'].plot()
df['Forecast'].plot()

plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()