import pandas as pd
import quandl
import pickle
import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')

api_key = 'SXr3AT42U72sUU3vPyyD'

bridge_height = {'meters':[10.26,10,31,10.27,10.22,10.23,6212.42,10.28,10.25,10.31]}

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


def mortgage_30y():
    df = quandl.get("FMAC/MORTG", trim_start="1975-01-01", authtoken=api_key)
    df.rename(columns={'Value': "M30"}, inplace=True)
    df["M30"] = (df["M30"] - df["M30"][0]) / df["M30"][0] * 100.0
    df = df.resample('D').mean()
    df = df.resample('M').mean()
    return df

def sp500_data():
    df = quandl.get("YAHOO/INDEX_GSPC", trim_start="1975-01-01", authtoken=api_key)
    df["Adjusted Close"] = (df["Adjusted Close"]-df["Adjusted Close"][0]) / df["Adjusted Close"][0] * 100.0
    df=df.resample('M').mean()
    df.rename(columns={'Adjusted Close':'sp500'}, inplace=True)
    df = df['sp500']
    return df

def gdp_data():
    df = quandl.get("BCB/4385", trim_start="1975-01-01", authtoken=api_key)
    df["Value"] = (df["Value"]-df["Value"][0]) / df["Value"][0] * 100.0
    df=df.resample('M').mean()
    df.rename(columns={'Value':'GDP'}, inplace=True)
    df = df['GDP']
    return df

def us_unemployment():
    df = quandl.get("ECPI/JOB_G", trim_start="1975-01-01", authtoken=api_key)
    df["Unemployment Rate"] = (df["Unemployment Rate"]-df["Unemployment Rate"][0]) / df["Unemployment Rate"][0] * 100.0
    df=df.resample('1D').mean()
    df=df.resample('M').mean()
    return df
#--------------------
sp500 = sp500_data()
us_gdp = gdp_data()
us_unemp = us_unemployment()

m30 = mortgage_30y()
HPI_data = pd.read_pickle('fiftyStates3.pickle')
HPI_bench = HPI_Benchmark()

HPI = HPI_data.join([HPI_bench, m30, us_unemp, us_gdp, sp500])
HPI.dropna(inplace=True)
print(HPI)
print(HPI.corr())

HPI.to_pickle('HPI.pickle')

