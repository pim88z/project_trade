# Statistical tests
from statsmodels.tsa.stattools import adfuller
from statsmodels.tsa.stattools import kpss

# Time series models 
from statsmodels.tsa.arima.model import ARIMA

import pandas as pd
import plotly.express as px

# Predicting share prices
# TODO:
# Make non-stationary data stationary
# Implement: gradient descent boosting maybe?
# 

# pd.Series(dftest[0:4], index=['Test Statistic','p-value','#Lags Used','Number of Observations Used'])


# Augmented dickey fuller test that tests for stationarity of time series.
def adf_test(timeseries):

    # Perform Dickey-Fuller test:
    dftest  = adfuller(timeseries, autolag='AIC')

    results = {"Test statistic": dftest[0], "p-value": dftest[1], "Laggs used": dftest[2], \
           "Number of observations used": dftest[3], "Critical value 1%": dftest[4]['1%'], \
           "Critical value 5%": dftest[4]['5%'],"Critical value 10%": dftest[4]['10%'] }
    
    if results["Test statistic"] < results["Critical value 5%"]:
       conclusion = "Time series is stationary"
    if results["Test statistic"] > results["Critical value 5%"]:
       conclusion = "Time series is non-stationary"
       
    return conclusion #results

def kpss_test(timeseries):
    print ('Results of KPSS Test:')
    kpsstest = kpss(timeseries, regression='c')
    return kpsstest



# TODO:
# Add period
def diff_timeseries(timeseries, order):
    # Convert timeseries object to list
    timeseries = list(timeseries)
    for itr in range(order):
        d_timeseries = []
        for t in range(1, len(timeseries)):
            # Difference between two adjacent elements
            dy = timeseries[t] - timeseries[t-1]
            d_timeseries.append(dy)
        timeseries = d_timeseries
    # Correct the length that is changed due to differencing the timeseries
    d_timeseries = [0]*order + d_timeseries
    return  d_timeseries

# def season_diff_timeseries(timeseries):

#     return 


# Use test data

# Company symbols
symbol    = 'AAPL' #, 'GOOG', 'TSLA', 'MSFT']
interval  = "1min"

filename  = f'./stock_data/{symbol}/interval: {interval}.csv' 

df  = pd.read_csv(filename)

# Indices
index_start = 100
index_end   = 200

order       = 2

df_select = df.loc[ index_start:index_end , ["time","close"]]

title = 'Apple Shares'
fig   = px.line(df_select, x = "time", y = 'close', title=title)
fig.show()


timeseries   = df_select["close"]
d_timeseries = diff_timeseries(timeseries, order)


print("d_timeseries")
print(d_timeseries)
print("Length")
print(len(d_timeseries))
print("Result adf")
print(adf_test(d_timeseries))


length = len(d_timeseries)
test_list = [0.05]*length


# Explanation of parameters
# p: number of time lags
# d: order of differencing
# q: order of the moving average

# split into train and test sets
X = d_timeseries
train_size = 0.7
size       = int(len(X) * train_size)
train, test = X[0:size], X[size:len(X)]

# Model parameters
p = 5
d = order
q = 1

model     = ARIMA(train, order=(p,d,q))
model_fit = model.fit()
output    = model_fit.forecast()

print("Output")
print(output)



# Replace the column values with the differenced timeseries
df_select["close"] =  d_timeseries   
df_select["predictions"] = test_list      
title     = f'Apple Shares differenced order: {order}'
fig = px.line(df_select, x = "time", y = ['close', 'predictions'], title=title)
fig.show()

# print("differenced timeseries")
# print(d_timeseries)
# print(adf_test(d_timeseries))

# print(d_timeseries)

# printing results
# print("Original timeseries")
# print(timeseries)
# print(adf_test(timeseries))


