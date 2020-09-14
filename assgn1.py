import numpy as np
import pandas as pd
#pandas DF are combination of panda Series..
#one column data is a Series of one datatype, DF can have multiple data types

pd.set_option('display.max_columns',15)
#others - max_rows, width, precision, height, date_dayfirst, date_yearfirst
pd.set_option('display.width', 1000)
pd.options.display.float_format = '{:.2f}'.format
#read data
url='https://raw.githubusercontent.com/DUanalytics/datasets/master/csv/denco.csv'
df=pd.read_csv(url)
df
df.describe
df.shape
df.columns
df.dtypes
df.index
df.groupby("custname").count().sort_values(by='region', ascending=0)
df.iloc[0:,0:1]
df.groupby("custname").sum().sort_values(by='revenue', ascending=0)
df.groupby("custname").sum().sort_values(by='margin', ascending=0)
