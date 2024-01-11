import matplotlib.pyplot as plt
import csv
import pandas as pd
from random import randint
# def dataCSV():
#     with open('EURUSD30min2020.csv', newline='') as csvfile:
#         reader = csv.reader(csvfile, delimiter=',', quotechar='|')
#         data = []
#         for i in reader:
#             data.append([float(i[5]), None])
#     return data
#
# x = dataCSV()
# # df = pd.DataFrame(x)
# plt.plot(x)
# plt.show()

# import json
# import matplotlib.pyplot as plt
#
# # Specify the path to your JSON file
# file_path = 'transactions.json'
#
# # Open the file and load the JSON data
# with open(file_path, 'r') as file:
#     data = json.load(file)
#
# # Extract 'units' and 'price' values
# units = [float(record['units']) for record in data]
# price = [float(record['price']) for record in data]
#
# # Plotting
# plt.figure(figsize=(10, 6))
#
# # Scatter plot
# plt.scatter(units, price, color='blue', marker='o', label='Units vs Price')
#
# # Set labels and title
# plt.xlabel('Units')
# plt.ylabel('Price')
# plt.title('Scatter Plot of Units vs Price')
# plt.legend()
# plt.grid(True)
#
# # Show the plot
# plt.show()

import matplotlib.pyplot as plt
from datetime import datetime
import csv
import json
from matplotlib.dates import date2num
import matplotlib.dates as mdates
times2 = []
prices2 = []
with open('NewData/EUR_USDM3020240111223422078324.csv', newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for i in reader:
            times2.append(i[0])
            prices2.append(float(i[4]))
            # data.append([datetime.strptime(i[0] + i[1], '%Y.%m.%d%H:%M'), float(i[5])])
times3 = []
profit = []
with open('profit1.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for i in reader:
        times3.append(datetime.strptime(i[0], "%Y-%m-%dT%H:%M:%S.%f000Z"))
        profit.append(float(i[1]))
fig, ax = plt.subplots(nrows=2)
ax[0].plot(date2num(times2), prices2, label='Data Set 2 (Continuous Line)')
ax[1].plot(date2num(times3), profit, label='Data Set 3 (Continuous Line)')
with open('transactions.json', 'r') as file:
    data = json.load(file)

for entry in data:
    time1 = datetime.strptime(entry['time'],  "%Y-%m-%dT%H:%M:%S.%f000Z")
    price1 = float(entry['price'])
    units1 = float(entry['units'])
    color = 'red' if units1 < 0 else 'green'
    ax[0].scatter(date2num(time1), price1, color=color, label='Data Set 1 (Points)')
ax[0].grid(True)
ax[0].xaxis.set_major_locator(mdates.AutoDateLocator())
ax[0].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
plt.gcf().autofmt_xdate()

ax[1].grid(True)
ax[1].xaxis.set_major_locator(mdates.AutoDateLocator())
ax[1].xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d %H:%M:%S'))
plt.gcf().autofmt_xdate()


plt.gca().xaxis_date()
plt.xlabel('Time')
plt.ylabel('Price')
plt.title('Data Sets Comparison')
plt.show()