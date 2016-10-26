
import pandas as pd
import quandl

df1 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2,3,2,2],
                    'US_GDP_Thousands':[50,55,65,55]},
                   index = [2001,2002,2003,2004])

df2 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2,3,2,2],
                    'US_GDP_Thousands':[50,55,65,55]},
                   index = [2005,2006,2007,2008])

df3 = pd.DataFrame({'HPI':[80,85,88,85],
                    'Int_rate':[2,3,2,2],
                    'Low_tier_HPI':[50,52,50,53]},
                   index = [2001,2002,2003,2004])

#concat = pd.concat([df1, df2, df3])
#print(concat)

#df4 = df1.append(df3)
#print(df4)

#s = pd.Series([80,2,50], index = ['HPI', 'Int_rate','US_GDP_Thousands'])

#df4 = df1.append(s, ignore_index=True)
#print(df4)

df1.set_index('HPI', inplace=True)
df3.set_index('HPI', inplace=True)
joined = df1.join(df3,how='left',lsuffix='x')
print(joined)

api_key = 'SXr3AT42U72sUU3vPyyD'

df4 = pd.DataFrame({'Year':[2001,2002,2003,2004],
                    'Int_rate':[2,3,2,2],
                    'US_GDP_Thousands':[50,55,65,55]},
                   index = [2005,2006,2007,2008])

df5 = pd.DataFrame({'Year':[2001,2003,2004,2005],
                    'Unemployment':[7,8,9,6],
                    'Low_tier_HPI':[50,52,50,53]},
                   )

merged = pd.merge(df4, df5, on = 'Year')
merged.set_index('Year', inplace=True)
print(merged)