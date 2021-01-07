import json
import requests
import csv
import os

# Import api_key. (improve)
with open('./api_key/api_key.json') as json_file:
     api_key = json.load(json_file["api_key"])

# Company symbols
symbols   = ['AAPL'] #, 'GOOG', 'TSLA', 'MSFT']
interval  = "1min"
# The give time periods respective from the current month till two years ago. 
slices = [ 'year1month1', 'year1month2', 'year1month3', 'year1month4', 'year1month5'] + \
         [ 'year1month6', 'year1month7', 'year1month8', 'year1month9', 'year1month10'] + \
         [ 'year1month11', 'year1month12', 'year2month1', 'year2month2', 'year2month3'] + \
         [ 'year2month4', 'year2month5', 'year2month6', 'year2month7', 'year2month8'] + \
         [ 'year2month9', 'year2month10', 'year2month11', 'year2month12']

for symbol in symbols:
    for time_period in slices:
        api_link   = f"https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&" + \
                    "symbol={symbol}&interval={interval}&slice={time_period}&apikey={api_key}"
        data       = requests.get(api_link)
        filename   = f'./stock_data/{symbol}/{interval}-{time_period}.csv'
        # Create directory if it's non-existent yet.
        os.makedirs(os.path.dirname(filename), exist_ok=True)
        with open(filename, 'wb') as f:
             f.write(data.content)
