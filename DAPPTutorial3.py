import pandas as pd

df = pd.read_csv("z02122.csv")
print(df.head())
df.set_index('Date', inplace=True)
df.to_csv('z02122-new.csv')

df = pd.read_csv('z02122-new.csv')
print(df.head())

df = pd.read_csv('z02122-new.csv', index_col=0) # set index column
print(df.head())

df.columns = ['Boston_HPI'] # rename column
print(df.head())

df.to_csv('z02122-new2.csv')
df.to_csv('z02122-new3.csv', header=False) # dont write the header row

df = pd.read_csv('z02122-new3.csv', names=['Date','Boston_HPI_new']) # set col values on way in
print(df.head())

df.to_html('z02122.html')

df = pd.read_csv('z02122-new3.csv', names=['Date','Boston-HPI-2'])
print(df.head())

df.rename(columns={'Boston-HPI-2':'BOS-HPI'}, inplace=True)
print(df.head())
