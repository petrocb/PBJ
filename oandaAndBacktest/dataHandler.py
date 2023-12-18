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
        self.oldTransactions = []

    def dataCSV(self):
        with open('EURUSD30min2020.csv', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            data = []
            for i in reader:
                data.append(i)
        return data

    def update(self):
        if self.line % 1000 == 0:
            # pass
            print(self.data[self.line][0])
            print(len(self.transactions))

        self.line += 1
        if self.line >= self.length:
            for i in self.transactions:
                self.oldTransactions.append(i)
            summary(self.oldTransactions)

    def checkSLnTP(self):
        for o in self.transactions:
            if o['type'] == "STOP_LOSS_ORDER":
                for i in self.transactions:
                    # optimization
                    if i['batchID'] > o['batchID']:
                        break
                    if o['batchID'] == i['batchID'] and o['id'] != i['id'] and i['type'] == "ORDER_FILL":
                        if float(i['units']) > 0 and float(self.data[self.line][4]) < float(o['price']):
                            self.transactions.append({
                                'id': self.id,
                                'batchID': self.id,
                                # 'type': 'STOP_LOSS_ORDER',
                                'type': 'ORDER_FILL',
                                'units': str(-abs(float(i['units']))),
                                'price': str(self.data[self.line][4]),
                                'stop': True
                            })
                        elif float(i['units']) < 0 and float(self.data[self.line][3]) > float(o['price']):
                            self.transactions.append({
                                'id': self.id,
                                'batchID': self.id,
                                # 'type': 'STOP_LOSS_ORDER',
                                'type': 'ORDER_FILL',
                                'units': str(abs(float(i['units']))),
                                'price': str(self.data[self.line][3]),
                                'stop': True
                            })
                            self.id += 1

    def performanceImprovement(self):
        units = 0
        for i in self.transactions:
            if i['type'] == "ORDER_FILL":
                units += float(i['units'])
        if units == 0:
            for i in self.transactions:
                self.oldTransactions.append(i)
            self.transactions = []
        elif units > 0:
            for i in self.transactions:
                if i['type'] == "ORDER_FILL" and float(i['units']) < 0:
                    cutPoint = self.transactions.index(i)
            try:
                for i in range(cutPoint):
                    self.oldTransactions.append(self.transactions[i])
            except UnboundLocalError:
                pass
        elif units < 0:
            for i in self.transactions:
                if i['type'] == "ORDER_FILL" and float(i['units']) > 0:
                    cutPoint = self.transactions.index(i)
            try:
                for i in range(cutPoint):
                    self.oldTransactions.append(self.transactions[i])
            except UnboundLocalError:
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

    def order(self, data):
        self.id += 1
        batchId = self.id
        self.transactions.append({
            'id': self.id,
            'batchID': batchId,
            'type': 'ORDER_FILL',
            'units': data['order']['units'],
            'price': str(self.data[self.line][5])
        })
        self.id += 1
        try:
            if float(data['order']['units']) > 0:
                self.transactions.append({
                    'id': self.id,
                    'batchID': batchId,
                    'type': 'STOP_LOSS_ORDER',
                    'price': str(float(self.data[self.line][5]) - data['order']['stopLossOnFill']['distance'])
                })
            elif float(data['units']) < 0:
                self.transactions.append({
                    'id': self.id,
                    'batchID': batchId,
                    'type': 'STOP_LOSS_ORDER',
                    'price': str(float(self.data[self.line][5]) - data['order']['stopLossOnFill']['distance'])
                })
        except KeyError:
            pass

        # return res

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

    def time(self):

        return str(datetime.strptime(f"{self.data[self.line][0]} {self.data[self.line][1]}",
                                     "%Y.%m.%d %H:%M").isoformat() + "Z")
