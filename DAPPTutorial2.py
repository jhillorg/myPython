
import pandas as pd
import datetime
import pandas_datareader.data as web
import matplotlib.pyplot as plt
from matplotlib import style
style.use('ggplot')

webStats = {'Day':[1,2,3,4,5,6],
            'Visitors':[43,53,34,45,64,34],
            'Bounce_Rate':[65,72,62,64,54,66]}


df = pd.DataFrame(webStats)

#print(df)
#print(df.head(2)) # defaults to 5
#print(df.tail(2))

print(df.set_index('Day').head())  # set_index returns a new dataframe
#df.set_index('Day', inplace=True)  # updates the dataframe
print(df.head())

print(df.Visitors)
print(df[['Day','Bounce_Rate']])

print(df.Visitors.tolist()) # converts column to list
