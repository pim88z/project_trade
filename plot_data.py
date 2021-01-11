import pandas as pd
import plotly.express as px


# TODO:
# Add results of paper trading algo
# Remove results weekend
# 



df  = pd.read_csv('stock_data/AAPL/interval: 1min.csv')

x = df["time"]
y = df["close"]

fig = px.line(df, x = "time", y = 'close', title='Apple Share Prices over time (2014)')
fig.show()
