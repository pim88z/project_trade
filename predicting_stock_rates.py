
import pandas as pd

# Company symbols
symbol    = 'AAPL' #, 'GOOG', 'TSLA', 'MSFT']
interval  = "1min"

filename  = f'./stock_data/{symbol}/interval: {interval}.csv' 

with open(filename, "w") as csv_file:
     # Create the writer object with tab delimiter
     x = csv_file["time"]
     y = csv_file["close"]

print(x,y)