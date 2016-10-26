import pandas as pd
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

api_key = 'SXr3AT42U72sUU3vPyyD'

bridge_height = {'meters':[10.26,10,31,10.27,10.22,10.23,6212.42,10.28,10.25,10.31]}

df = pd.DataFrame(bridge_height)
df['STD'] = pd.rolling_std(df['meters'],2)

print(df)

df_std = df.describe()['meters']['std']
print(df_std)

df = df[ (df['STD'] < df_std) ] # WHERE type statement;

df.plot()
plt.show()
