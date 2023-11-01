import csv
import datetime


class dataHandler:
    def __init__(self):
        self.line = 0
        self.positions = []
        self.orders = []
        self.data = []
        self.sl = 0
        self.tp = 0

    def start(self, line):
        with open('quickData.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            count = 0
            self.line = line
            for i in reader:
                self.data.append(
                    [datetime.datetime.combine(datetime.date(int(i[0][0:4]), int(i[0][5:7]), int(i[0][8:10])),
                                               datetime.time(int(i[1][0:2]), int(i[1][3:5]))), float(i[-2])])
                count += 1
            return self.data[:line]

    def update(self):
        self.line += 1
        return self.data[self.line]

    def buy(self, sld, tpd):
        self.positions.append([self.data[self.line], 'b'])
        self.sl = float(self.positions[-1][0][1]) - sld
        self.tp = float(self.positions[-1][0][1]) + tpd

    def sell(self, sld, tpd):
        self.positions.append([self.data[self.line], 's'])
        self.sl = float(self.positions[-1][0][1]) + sld
        self.tp = float(self.positions[-1][0][1]) - tpd

    def order(self, units, account, tag, sld, tpd):
        self.orders.append([self.data[self.line], units])
        self.sl = 99# float(self.positions[-1][0][1]) + sld
        self.tp = 99#float(self.positions[-1][0][1]) - tpd

    def close(self):
        self.positions.append([self.data[self.line], 'c'])

    def getPosition(self):
        return {'positions': [{'long': {'units': 0}, 'short': {'units': 0}}]}
        return {'positions': [{'instrument': 'EUR_USD',
                               'long': {'units': '3000', 'averagePrice': '1.06031', 'pl': '3.1974',
                                        'resettablePL': '3.1974', 'financing': '0.0000', 'dividendAdjustment': '0.0000',
                                        'guaranteedExecutionFees': '0.0000', 'tradeIDs': ['154', '159', '165'],
                                        'unrealizedPL': '2.6896'},
                               'short': {'units': '0', 'pl': '-4.6554', 'resettablePL': '-4.6554',
                                         'financing': '0.0000', 'dividendAdjustment': '0.0000',
                                         'guaranteedExecutionFees': '0.0000', 'unrealizedPL': '0.0000'},
                               'pl': '-1.4580', 'resettablePL': '-1.4580', 'financing': '0.0000',
                               'commission': '0.0000', 'dividendAdjustment': '0.0000',
                               'guaranteedExecutionFees': '0.0000', 'unrealizedPL': '2.6896', 'marginUsed': '87.2080'}],
                'lastTransactionID': '166'}
        return {'positions'}
        return self.positions

    def setLine(self):
        self.line = 0

    def reset(self):
        self.line = 0
        self.positions = []
        self.data = []

    def time(self):
        return self.data[self.line][0].hour

    def checkSLnTP(self):
        try:
            if (self.data[self.line][1] < self.sl and self.positions[-1][-1] == 'b') or \
                    (self.data[self.line][1] > self.sl and self.positions[-1][-1] == 's') or \
                    (self.data[self.line][1] > self.tp and self.positions[-1][-1] == 'b') or \
                    (self.data[self.line][1] < self.tp and self.positions[-1][-1] == 's'):
                return True
            else:
                return False
        except IndexError:
            return False

    def openTrades(self):
        try:
            if self.positions[-1][-1] == 'b' or self.positions[-1][-1] == 's':
                return {"positions": [0]}

            else:
                return {"positions": []}

        except IndexError as e:
            print(e)
            return {"positions": []}
        # try:
        #     if self.positions[-1][-1] == 'b' or self.positions[-1][-1] == 's':
        #         return self.positions[-1]
        #     else:
        #         return []
        # except IndexError as e:
        #     print("error", e)
        #     return []

    def getOrders(self):
        print(self.orders)
        return self.orders
