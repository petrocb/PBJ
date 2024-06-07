import datetime
from .. import functions
import csv
class heikienAshi1bar:
    def __init__(self, account, timeFrame):
        self.account = account
        self.timeFrame = timeFrame
        self.data = functions.startPastPricesList(3, "EUR_USD", self.timeFrame, self.account)

    def tick(self):
        if self.account == "test":
            functions.update()
        self.data = functions.startPastPricesList(3, "EUR_USD", self.timeFrame, self.account)
        position = functions.getPositions(self.account)['positions']
        if position:
            position = float(position[0]['long']['units']) + float(position[0]['short']['units'])
        else:
            position = 0

        list = heikinAshi2(self.data)
        openPrice = list[0]
        close = list[1]
        if close > openPrice:
            direction = 500
            sl = self.data[1][2]

        elif close < openPrice:
            direction = -500
            sl = self.data[1][2]
        else:
            direction = 0
            sl = 0

        if position != direction:
            functions.marketOrder(direction, self.account, self.account, 0, 0, 0)

        print("\ntime:", functions.time("primary"),
              "\ntimeFrame:", self.timeFrame,
              "\nposition:", position,
              "\ndirection:", direction,
              "\nopen:", open,
              "\nclose:", close,
              "\ndiff:", close - openPrice
              )

        with open('historyData/'+self.account+'.csv', 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow([datetime.datetime.utcnow(),
            "time:", functions.time("primary"),
              "timeFrame:", self.timeFrame,
              "position:", position,
              "direction:", direction,
              "open:", openPrice,
              "close:", close,
              "diff:", close - openPrice
              ])
        csvfile.close()

def heikinAshi(data):
    open = round(0.5 * (float(data[0][1]) + float(data[0][4])), 5)
    close = round(0.25 * (float(data[1][1]) +
                          float(data[1][2]) +
                          float(data[1][3]) +
                          float(data[1][4])), 5)
    return [open, close]

def heikinAshi2(data):
    data = data[:-1]
    dict = []
    for i in data:
        dict.append({'date': i[0], 'open': float(i[1]), 'high': float(i[2]), 'low': float(i[3]), 'close': float(i[4])})
    data = dict
    heikien = []
    for i in range(len(data)):
        if i == 0:
            heikien.append({'open': round(data[i]['open'], 5),
                            'high': round(data[i]['high'], 5),
                            'low': round(data[i]['low'], 5),
                            'close': round(data[i]['close'], 5)})
        else:
            heikien.append({'open': round(0.5 * (heikien[i - 1]['open'] + heikien[i - 1]['close']), 5),
                            'high': round(data[i]['high'], 5),
                            'low': round(data[i]['low'], 5),
                            'close': round(0.25 * (data[i]['open'] + data[i]['high'] + data[i]['low'] + data[i]['close']), 5)})
    return [heikien[-1]['open'], heikien[-1]['close']]