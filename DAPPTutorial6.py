
import pandas as pd
import quandl
import pickle


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

        if main_df.empty:
            main_df = df
        else:
            main_df = main_df.join(df, how='inner', lsuffix='x')

    print(main_df.head())

    pickle_out = open('fiftyStates.pickle','wb')
    pickle.dump(main_df, pickle_out)
    pickle_out.close()

#grab_initial_state_data()

pickle_in = open('fiftyStates.pickle','rb') # builtin pickle said to be faster?
HPI_data = pickle.load(pickle_in)
#pickle_in.close()
print(HPI_data)

HPI_data.to_pickle('pickle.pickle')
HPI_data2 = pd.read_pickle('pickle.pickle')
print(HPI_data2)


