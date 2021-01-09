import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plot

# TODO:
# Add results of paper trading algo
# Remove results weekend
# 



df  = pd.read_csv('stock_data/AAPL/interval: 1min.csv')

x = df["time"]
y = df["close"]

fig = px.line(df, x = "time", y = 'close', title='Apple Share Prices over time (2014)')
fig.show()

# fig = px.scatter(df, x="time", y="close")
# # fig.update_xaxes(range=[0, 1500])
# # fig.update_yaxes(range=[0, 1500])

# df.plot.scatter(x=df["time"], y=df["close"])



# fig.show()


# # 

# fig = go.Figure(go.Scatter(x = df['time'], y = df['close'],
#                   name='Share Prices (in USD)'))

# fig.update_layout(title='Apple Share Prices over time (2014)',
#                    plot_bgcolor='rgb(230, 230,230)',
#                    showlegend=True)
# fig.show()

# x = df["time"]
# y = df["close"]

#x=df_select.index df_select.index


