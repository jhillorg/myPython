
import pandas as pd
import quandl

api_key = 'SXr3AT42U72sUU3vPyyD'

df = quandl.get("FMAC/HPI_IN", authtoken=api_key)
print(df.head())

#this is a list
fiftyStates = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')

#this is a dataframe
#print(fiftyStates[0])

#this is a column
#print(fiftyStates[0][0])

#for abbv in fiftyStates[0][0][1:]:
#    print('FMAC/HPI_' + abbv)
