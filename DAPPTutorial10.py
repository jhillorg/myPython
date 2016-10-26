import pandas as pd
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

api_key = 'SXr3AT42U72sUU3vPyyD'


def state_list():
    fiftyStates = pd.read_html('https://simple.wikipedia.org/wiki/List_of_U.S._states')
    return fiftyStates[0][0][1:]


def grab_initial_state_data():
    states = state_list()
    main_df = pd.DataFrame()
    for abbv in states:
        query = 'FMAC/HPI_' + str(abbv)
        df = quandl.get(query, authtoken=api_key)
        df.rename(columns={'Value': str(abbv)}, inplace=True)
        df[abbv] = (df[abbv] - df[abbv][0]) / df[abbv][0] * 100.0

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='inner', lsuffix='x')

    print(main_df.head())

    pickle_out = open('fiftyStates3.pickle', 'wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()


def HPI_Benchmark():
    df = quandl.get("FMAC/HPI_USA", authtoken=api_key)
    df.rename(columns={'Value': "United States"}, inplace=True)
    df["United States"] = (df["United States"] - df["United States"][0]) / df["United States"][0] * 100.0
    return df


# grab_initial_state_data()

fig = plt.figure()
ax1 = plt.subplot2grid((1, 1), (0, 0))

HPI_data = pd.read_pickle('fiftyStates3.pickle')

HPI_data['TX1yr'] = HPI_data['TX'].resample('A').mean()
print(HPI_data[['TX','TX1yr']].head())

#HPI_data.dropna(inplace=True) # remove NaN values
#HPI_data.fillna(method='ffill', inplace=True) # add values for NaN from prior value
#HPI_data.fillna(value=100, inplace=True) # add values for all NaN; hard coded

print(HPI_data[['TX','TX1yr']].head())

print(HPI_data.isnull().values.sum()) # print how many NaN instances


HPI_data[['TX','TX1yr']].plot(ax=ax1)

#plt.legend().remove() # hide ledgen
plt.legend(loc=4)
plt.show()

