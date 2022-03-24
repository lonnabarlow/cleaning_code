from turtle import width
import pandas as pd

data = pd.read_csv('artwork_sample.csv')
data.head()
print(data.head())

data.dtypes
print(data.dtypes)

data.acquisitionYear
print(data.acquisitionYear)

"""remove/ fixing"""

data.drop(0)
print(data.drop(0))

data.drop(columns = ['height', 'width','depth'])
print(data.drop(columns = ['height', 'width', 'depth']))

data.columns
print(data.columns)

data.columns.str.lower()
print(data.columns.str.lower())

data.columns = [x.lower() for x in data.columns]
print(data.columns == [x.lower() for x in data.columns])

data.columns
print(data.columns)

data.rename(columns ={"thumbnailUrl": "thumbnail"})
print(data.rename(columns ={"thumbnailUrl": "thumbnail"}))

data.rename({"thumbnailUrl": "thumbnail"}, axis=1)
print(data.rename({"thumbnailUrl": "thumbnail"}, axis=1))

data.rename({"thumbnailUrl": "thumbnail"}, inplace=True)
print(data.rename({"thumbnailUrl": "thumbnail"}, inplace=True))

"""***********"""

data['id']
print(data['id'])

data[1:5]['artist']
print(data[1:5]['artist'])

data[data.year > 1800]['year'] 
print(data[data.year > 1800]['year'])

data.loc[0, :]
print(data.loc[0, :])

data.loc[[1,5], 'id':'artistid']
print(data.loc[[1,5], 'id':'artistid'])


data.iloc[0:3, :]
print(data.iloc[0:3, :])

data.iloc[0:3, 0:3]
print(data.iloc[0:3, 0:3])

"""**************"""

data.medium
print(data.medium)

type(data.medium)
print(type(data.medium))

data.medium.str
print(data.medium.str)

data.medium.str.contains('Graphite')
print(data.medium.str.contains('Graphite'))

data.loc[data.medium.str.contains('Graphite'), ['artist','medium']]
print(data.loc[data.medium.str.contains('Graphite'), ['artist','medium']])

"""**************"""

data.title.str.strip()
print(data.title.str.strip())

data.loc[data.title.str.contains('\s$', regex=True)]
print(data.loc[data.title.str.contains('\s$', regex=True)])

# data.title.str.rstrip() data.title.str.lstrip() 

pd.isna(data.loc[:, 'datetext'])
print(pd.isna(data.loc[:, 'datetext']))

from numpy import nan

data.replace({'datetext' :{ 'date not known' : nan}})
print(data.replace({'datetext' :{ 'date not known' : nan}}))

data.replace({'datetext' :{ 'date not known' : nan}}, inplace=True)
print(data.replace({'datetext' :{ 'date not known' : nan}}, inplace=True))

data.shape
print(data.shape)


data.dropna() 
print(data.dropna())

data.dropna().shape
print(data.dropna().shape)

data.drop_duplicates()
print(data.drop_duplicates())

data.drop_duplicates(subset=['artist'])
print(data.drop_duplicates(subset=['artist']))