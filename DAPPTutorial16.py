import pandas as pd
import quandl
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
from statistics import mean
from sklearn import svm, preprocessing, cross_validation

style.use('fivethirtyeight')

api_key = 'SXr3AT42U72sUU3vPyyD'

def create_labels(cur_hpi, fut_hpi):
    if fut_hpi > cur_hpi:
        return 1
    else:
        return 0

def moving_average(values):
    return mean(values)

housing_data = pd.read_pickle('HPI.pickle')

housing_data = housing_data.pct_change()

housing_data.replace([np.inf, -np.inf], np.nan, inplace=True)
housing_data['US_HPI_future'] = housing_data['United States'].shift(-1)

housing_data.dropna(inplace=True)
#print(housing_data[['US_HPI_future','United States']].head())
housing_data['label'] = list(map(create_labels, housing_data['United States'], housing_data['US_HPI_future'])
) # custom funcntion

print(housing_data.head())

#housing_data['ma_apply_example'] = pd.rolling_apply(housing_data['M30'], 10, moving_average)

x = np.array(housing_data.drop(['label', 'US_HPI_future'],1))
x = preprocessing.scale(x)
y = np.array(housing_data['label'])

x_train, x_test, y_train, y_test = cross_validation.train_test_split(x,y, test_size=0.2)

clf = svm.SVC(kernel='linear')
clf.fit(x_train, y_train)

print(clf.score(x_test, y_test))
#print(housing_data.drop(['label', 'US_HPI_future'],1))