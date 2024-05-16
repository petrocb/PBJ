import pandas as pd
import plotly.graph_objs as go
import plotly.express as px
import datetime

# Read data from CSV
data = pd.read_csv("rawdata.csv", names=['datetime', 'value', 'label'], header=None)
data2 = pd.read_csv("EURUSD2.csv", names=['date', 'time', 'open', 'high', 'low', 'close', 'volume'])
for i in data2['date']:
     i = datetime.datetime.combine(datetime.date(int(i[0][0:4]), int(i[0][5:7]), int(i[0][8:10])))
print(data)
dates = data['datetime']
values = data['value']
labels = data['label']
close = data2['close']
print(close)
fig = px.line(y=close)
fig.add_scatter(y=values)
fig.show()
#
# trace = []
# colors = {'s': 'red', 'b': 'blue', 'c': 'green'}
#
# for label in set(labels):
#     data_subset = data[data['label'] == label]
#     trace.append(go.Scatter(
#         x=data_subset['datetime'],
#         y=data_subset['value'],
#         mode='markers',
#         name=label
#         # marker=dict(color=colors[label]),
#     ))
#
# layout = go.Layout(
#                    xaxis=dict(title='Datetime'),
#                    yaxis=dict(title='Value'))
#
# fig = go.Figure(data=trace, layout=layout)
# fig.show()