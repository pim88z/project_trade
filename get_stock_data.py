import json
import requests
import csv
from   csv import reader
import os
import re

# TODO:
# Add time span in file name
# Add delta after each iteration, correct for overlap.
# Append csv file to csv file. 

# Import api_key. (improve)
with open('./api_key/api_key.json') as json_file:
     api_key = json.load(json_file)["api_key"]


# Company symbols
symbols   = ['AAPL'] #, 'GOOG', 'TSLA', 'MSFT']
interval  = "1min"
# The give time periods respective from the current month till two years ago. 
slices = [ 'year1month1', 'year1month2', 'year1month3', 'year1month4', 'year1month5'] + \
         [ 'year1month6', 'year1month7', 'year1month8', 'year1month9', 'year1month10'] + \
         [ 'year1month11', 'year1month12', 'year2month1', 'year2month2', 'year2month3'] + \
         [ 'year2month4', 'year2month5', 'year2month6', 'year2month7', 'year2month8'] + \
         [ 'year2month9', 'year2month10', 'year2month11', 'year2month12']


# TODO:
# Improve appending to csv file!
for  symbol in symbols:
     filename   = f'./stock_data/{symbol}/interval: {interval}.csv' 
     # Create directory if it's non-existent yet.
     os.makedirs(os.path.dirname(filename), exist_ok=True) 
     # All data
     all_data = []
     for time_period in slices:
         api_link   = f'https://www.alphavantage.co/query?function=TIME_SERIES_INTRADAY_EXTENDED&' + \
                      f'symbol={symbol}&interval={interval}&slice={time_period}&apikey={api_key}'
         orig       = requests.get(api_link).content
         # Splitting the byte string into a list
         data       = orig.decode('utf-8').splitlines()
         # The header of the data
         header     = data[0]
         # Data without header
         data       = data[1:]
         # Adding data of time period to all data retrieved already
         all_data  += data
     # Insert back header at the beginning of the list
     all_data.insert(0, header)
     with open(filename, "w") as csv_file:
          # Create the writer object with tab delimiter
          writer = csv.writer(csv_file, delimiter = '\t')
          for line in all_data:
              # Writerow() needs a list of data to be written, so split at all empty spaces in the line 
              writer.writerow(re.split('\s+',line)) 
          


