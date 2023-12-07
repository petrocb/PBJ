import csv
from datetime import datetime

# from newClasses import Account
from summary import summary


class dataHandler:

    def __init__(self):
        # self.account = Account()
        self.line = 0
        self.id = 0
        self.data = self.dataCSV()
        self.length = len(self.data)
        self.transactions = []

    def dataCSV(self):
        with open('EURUSDShort.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            data = []
            for i in reader:
                data.append(i)
        return data

    def update(self):
        self.line += 1
        if self.line >= self.length:
            summary(self.transactions)

    def getPrice(self):
        back_tester_data = {
            'time': '2023-11-08T21:02:09.328980331Z',
            'prices': [
                {
                    'type': 'PRICE',
                    'time': '2023-11-08T21:02:05.747261894Z',
                    'bids': [
                        {'price': '1.07100', 'liquidity': 1000000},
                        {'price': '1.07098', 'liquidity': 2000000},
                        # Add more bid data here
                    ],
                    'asks': [
                        {'price': '1.07110', 'liquidity': 1000000},
                        {'price': '1.07113', 'liquidity': 2000000},
                        # Add more ask data here
                    ],
                    'closeoutBid': '1.07095',
                    'closeoutAsk': '1.07115',
                    'status': 'tradeable',
                    'tradeable': True,
                    'quoteHomeConversionFactors': {
                        'positiveUnits': '0.81365641',
                        'negativeUnits': '0.81377559',
                    },
                    'instrument': 'EUR_USD',
                }
            ]
        }

        return back_tester_data

    def getPriceSince(self):
        pass

    def GetBid(self):
        pass

    def getAsk(self):
        pass

    def startPastPriceList(self, count):
        data = {'instrument': 'EUR_USD', 'granularity': 'M30', 'candles': []}
        self.line = count
        for i in range(count):
            data['candles'].append({
                'complete': True,
                'volume': int(self.data[i][6]),
                'time': datetime.strptime(f"{self.data[i][0]} {self.data[i][1]}", "%Y.%m.%d %H:%M").isoformat() + "Z",
                'mid': {
                    'o': self.data[i][2],
                    'h': self.data[i][3],
                    'l': self.data[i][4],
                    'c': self.data[i][5]
                }
            })

        return data

    def updatePastPrices(self):
        pass

    def updatePastPrices2(self):
        return {'instrument': 'EUR_USD', 'granularity': 'M30', 'candles': [{
            'complete': True,
            'volume': int(self.data[self.line][6]),
            'time': datetime.strptime(f"{self.data[self.line][0]} {self.data[self.line][1]}",
                                      "%Y.%m.%d %H:%M").isoformat() + "Z",
            'mid': {
                'o': self.data[self.line][2],
                'h': self.data[self.line][3],
                'l': self.data[self.line][4],
                'c': self.data[self.line][5]
            }
        }]}

    def buy(self):
        pass

    def sell(self):
        pass

    def order(self, data):
        self.transactions.append({
            'type': 'ORDER_FILL',
            'units': data['order']['units'],
            'price': str(self.data[self.line][5]),
            'fullPrice': {
                'bids': [{
                    'price': str(float(self.data[self.line][5])-0.0001+0.0006),
                    'liquidity': '1000000'
                }, {
                    'price': str(float(self.data[self.line][5])-0.0001+0.0004),
                    'liquidity': '2000000'
                }, {
                    'price': str(float(self.data[self.line][5])-0.0001+0.0002),
                    'liquidity': '2000000'
                }, {
                    'price': str(float(self.data[self.line][5])-0.0001),
                    'liquidity': '5000000'
                }
                ],
                'asks': [{
                    'price': str(float(self.data[self.line][5])+0.0001),
                    'liquidity': '1000000'
                }, {
                    'price': str(float(self.data[self.line][5])+0.0001-0.0002),
                    'liquidity': '2000000'
                }, {
                    'price': str(float(self.data[self.line][5])+0.0001-0.0004),
                    'liquidity': '2000000'
                }, {
                    'price': str(float(self.data[self.line][5])+0.0001-0.0006),
                    'liquidity': '5000000'
                }
                ]
            }
        })
        # return res

    def close(self):
        pass

    def getPositions(self):
        units = 0
        for i in self.transactions:
            if i['type'] == "ORDER_FILL":
                units += float(i['units'])
        if units == 0:
            return {'positions': [], 'lastTransactionID': 'NOT_IMPLEMENTED'}
        elif units > 0:
            return {'positions': [{'long': {'units': str(units)}, 'short': {'units': '0'}}],
                    'lastTransactionID': 'NOT_IMPLEMENTED'}
        elif units < 0:
            return {'positions': [{'long': {'units': '0'}, 'short': {'units': str(units)}}],
                    'lastTransactionID': 'NOT_IMPLEMENTED'}
    def getOrders(self):
        pass

    def getTrades(self):
        return self.account.getTradesasDict()

    def getTransactionsSinceID(self):
        return self.account.getActivityDict()

    def getTransactionsSinceDate(self):
        pass

    def time(self):

        return str(datetime.strptime(f"{self.data[self.line][0]} {self.data[self.line][1]}",
                                     "%Y.%m.%d %H:%M").isoformat() + "Z")
