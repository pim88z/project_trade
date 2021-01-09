import pandas as pd
import plotly.express as px

# TODO:
# Add results of paper trading algo
# Remove results weekend
# 



df = pd.read_csv('stock_data/AAPL/1min.csv')

# Choose columns to plot
df_select = df[["time", "close"]]

# print(df_select)
fig = px.line(df_select, x = 'time', y = 'close', title='Apple Share Prices over time (2014)')
fig.show()
