from google.colab import drive
import pandas as pd
import glob
import os


csvfile = pd.read_csv('CollectedData_jic.csv')

#replacing all forward slashes with back slashes in path
csvfile['scorer'] = csvfile['scorer'].str.replace('/', '\\', regex=True) 
corrected_csvfile = csvfile.copy()

#pandas doesn't allow duplicate column names when creating csv file
new = corrected_csvfile.rename(columns = {'jic'pip:'jic', 'jic.1':'jic', 'jic.2':'jic', 'jic.3':'jic', 'jic.3':'jic', 'jic.4':'jic', 'jic.5':'jic', 'jic.6':'jic', 'jic.7':'jic',}, inplace=False)
finalcsv = new.to_csv('CollectedData_jic.csv', index=False)