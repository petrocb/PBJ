import datetime
from .. import functions
import csv


class multiResAshi:
    def __init__(self, account):
        self.account = account

    def tick(self):
        if self.account == "test":
            functions.update()
        data = {'month': functions.startPastPricesList(100, "EUR_USD", "M", self.account),
                'week': functions.startPastPricesList(100, "EUR_USD", "W", self.account),
                'day': functions.startPastPricesList(100, "EUR_USD", "D", self.account),
                '4hour': functions.startPastPricesList(100, "EUR_USD", "H4", self.account),
                '1hour': functions.startPastPricesList(100, "EUR_USD", "H1", self.account),
                '30min': functions.startPastPricesList(100, "EUR_USD", "M30", self.account),
                '15min': functions.startPastPricesList(100, "EUR_USD", "M15", self.account),
                '5min': functions.startPastPricesList(100, "EUR_USD", "M5", self.account),
                '1min': functions.startPastPricesList(100, "EUR_USD", "M1", self.account),
                }

        position = functions.getPositions(self.account)['positions']
        if position:
            position = float(position[0]['long']['units']) + float(position[0]['short']['units'])
        else:
            position = 0

        prices = {'month': heikinAshi2(data['month']),
                  'week': heikinAshi2(data['week']),
                  'day': heikinAshi2(data['day']),
                  '4hour': heikinAshi2(data['4hour']),
                  '1hour': heikinAshi2(data['1hour']),
                  '30min': heikinAshi2(data['30min']),
                  '15min': heikinAshi2(data['15min']),
                  '5min': heikinAshi2(data['5min']),
                  '1min': heikinAshi2(data['1min']),
                  }
        opinion = 0
        for i in prices:
            if prices[i]['open'] < prices[i]['close']:
                opinion += 1
                print(i, "up")
            elif prices[i]['open'] > prices[i]['close']:
                opinion -= 1
                print(i, "down")
        if position == 0:
            if opinion > 1:
                direction = 5000
            elif opinion < -1:
                direction = -5000
            else:
                direction = 0
        elif (position > 0 > opinion) or (position < 0 < opinion):
            direction = 0
        else:
            direction = 0

        if position != direction:
            functions.marketOrder(direction, self.account, self.account, 0, 0, 0)

        print("\ntime:", functions.time("primary"),
              "\ntimeFrame:", self.timeFrame,
              "\nposition:", position,
              "\ndirection:", direction,
              "\nopinion:", opinion

              )

        with open('historyData/' + self.account + '.csv', 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow([datetime.datetime.utcnow(),
                                "\ntime:", functions.time("primary"),
                                "\ntimeFrame:", self.timeFrame,
                                "\nposition:", position,
                                "\ndirection:", direction,
                                "\nopinion:", opinion])
        csvfile.close()


def heikinAshi(data):
    open = round(0.5 * (float(data[0][1]) + float(data[0][4])), 5)
    close = round(0.25 * (float(data[1][1]) +
                          float(data[1][2]) +
                          float(data[1][3]) +
                          float(data[1][4])), 5)
    return [open, close]


def heikinAshi2(data):
    # data = data[:-1]
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
                            'close': round(
                                0.25 * (data[i]['open'] + data[i]['high'] + data[i]['low'] + data[i]['close']), 5)})
    return heikien[-1]
