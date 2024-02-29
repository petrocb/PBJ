import copy
import csv

# from newClasses import Account
from summary import summary


class dataHandler:

    def __init__(self):
        # self.account = Account()
        self.line = 0
        self.id = 0
        self.dataString = "EUR_USD_S5_2024_02_29T20_13_50_2024_02_29T18_37_05_1000.csv"
        self.data = self.dataCSV()
        self.length = len(self.data)
        self.transactions = []
        self.oldTransactions = []
        self.trailingStop = []

    def refresh(self):
        self.id = 0
        self.transactions = []
        self.oldTransactions = []

    def dataCSV(self):
        with open(f'NewData/{self.dataString}', newline='') as csvfile:
            reader = csv.reader(csvfile, delimiter=',', quotechar='|')
            data = []
            for i in reader:
                data.append(i)
        return data

    def update(self):
        if self.line % 1000 == 0:
            pass
            # print("data:", self.data[self.line][0])
            # print("transactionsl", len(self.transactions))
            # # print("transactions:", self.transactions)
            print("line", self.line)
            #     print("date", self.data[self.line][0])
            #     print("oldTransactions", len(self.oldTransactions))
            #     print("transactions", len(self.transactions))
            # summary(self.time(), self.transactions)
            # self.oldTransactions = copy.deepcopy(self.transactions)
            summary(self.time(), copy.deepcopy(self.oldTransactions), False, 0, self.dataString)

        self.line += 1
        if self.line == self.length - 1:
            summary(self.time(), copy.deepcopy(self.oldTransactions), False, 0, self.dataString)
            self.refresh()

    def checkSLnTP(self):
        # for o in self.transactions:
        #     if o['type'] == "STOP_LOSS_ORDER" or o['type'] == "TAKE_PROFIT_ORDER":
        #         for i in self.transactions:
        #             try:
        #                 # optimization
        #                 if i['batchID'] > o['batchID']:
        #                     break
        #                 if o['batchID'] == i['batchID'] and i['type'] == "ORDER_FILL":
        #                     if o['type'] == "STOP_LOSS_ORDER" and float(i['units']) > 0 and float(self.data[self.line][3]) < float(o['price']):
        #                         self.id += 1
        #                         self.transactions.append({
        #                             'id': self.id,
        #                             'batchID': self.id,
        #                             'type': 'ORDER_FILL',
        #                             'units': str(-abs(float(i['units']))),
        #                             'price': str(o['price']),
        #                         })
        #                     elif o['type'] == "STOP_LOSS_ORDER" and float(i['units']) < 0 and float(self.data[self.line][2]) > float(o['price']):
        #                         self.id += 1
        #                         self.transactions.append({
        #                             'id': self.id,
        #                             'batchID': self.id,
        #                             'type': 'ORDER_FILL',
        #                             'units': str(abs(float(i['units']))),
        #                             'price': str(o['price']),
        #                         })
        #                     elif o['type'] == "TAKE_PROFIT_ORDER" and float(i['units']) > 0 and float(self.data[self.line][2]) > float(o['price']):
        #                         self.id += 1
        #                         self.transactions.append({
        #                             'id': self.id,
        #                             'batchID': self.id,
        #                             'type': 'ORDER_FILL',
        #                             'units': str(-abs(float(i['units']))),
        #                             'price': str(o['price']),
        #                         })
        #                     elif o['type'] == "TAKE_PROFIT_ORDER" and float(i['units']) < 0 and float(self.data[self.line][3]) < float(o['price']):
        #                         self.id += 1
        #                         self.transactions.append({
        #                             'id': self.id,
        #                             'batchID': self.id,
        #                             'type': 'ORDER_FILL',
        #                             'units': str(abs(float(i['units']))),
        #                             'price': str(o['price']),
        #                         })
        #             except KeyError as e:
        #                 if str(e) != "'price'":
        #                     raise KeyError

        for o in self.transactions:
            if o['type'] == "ORDER_FILL":
                for i in self.transactions:
                    if i['batchID'] == o['batchID'] and i['type'] == "STOP_LOSS_ORDER":
                        if float(o['units']) > 0 and float(self.data[self.line][3]) < float(i['price']):
                            self.id += 1
                            self.transactions.append({
                                'id': self.id,
                                'batchID': self.id,
                                'type': 'ORDER_FILL',
                                'units': str(-abs(float(o['units']))),
                                'price': str(i['price']),
                            })
                            break
                        elif float(o['units']) < 0 and float(self.data[self.line][2]) > float(i['price']):
                            self.id += 1
                            self.transactions.append({
                                'id': self.id,
                                'batchID': self.id,
                                'type': 'ORDER_FILL',
                                'units': str(abs(float(o['units']))),
                                'price': str(i['price']),
                            })
                            break
                    elif i['batchID'] == o['batchID'] and i['type'] == "TAKE_PROFIT_ORDER":
                        if float(o['units']) > 0 and float(self.data[self.line][2]) > float(i['price']):
                            self.id += 1
                            self.transactions.append({
                                'id': self.id,
                                'batchID': self.id,
                                'type': 'ORDER_FILL',
                                'units': str(-abs(float(o['units']))),
                                'price': str(i['price']),
                            })
                            break
                        elif float(o['units']) < 0 and float(self.data[self.line][3]) < float(i['price']):
                            self.id += 1
                            self.transactions.append({
                                'id': self.id,
                                'batchID': self.id,
                                'type': 'ORDER_FILL',
                                'units': str(abs(float(o['units']))),
                                'price': str(i['price']),
                            })
                            break



        # for o in self.trailingStop:
        #     for i in self.transactions:
        #         if o[0] == i['batchID'] and i['type'] == "ORDER_FILL":
        #             if float(i['units']) > 0 and o[1] > float(self.data[self.line][3]):
        #                 self.id += 1
        #                 self.transactions.append({
        #                     'id': self.id,
        #                     'batchID': self.id,
        #                     'type': 'ORDER_FILL',
        #                     'units': str(-abs(float(i['units']))),
        #                     'price': o[1],
        #                 })
        #             elif float(i['units']) < 0 and o[2] < float(self.data[self.line][2]):
        #                 self.id += 1
        #                 self.transactions.append({
        #                     'id': self.id,
        #                     'batchID': self.id,
        #                     'type': 'ORDER_FILL',
        #                     'units': str(abs(float(i['units']))),
        #                     'price': o[1],
        #                 })

    def updateTrailingStopLoss(self):
        for o in self.transactions:
            if o['type'] == "TRAILING_STOP_LOSS_ORDER":
                for m in self.transactions:
                    if o['type'] == "ORDER_FILL" and o['batchID'] == m['batchID']:
                        for i in self.trailingStop:
                            if o['batchID'] == i[0]:
                                if float(m['units']) > 0:
                                    i[1] = float(self.data[self.line][3]) - o['distance']
                                elif float(m['units']) < 0:
                                    i[2] = float(self.data[self.line][2]) + o['distance']

    def performanceImprovement(self):
        units = 0
        cutPoint = 0
        for i in self.transactions:
            if i['type'] == 'ORDER_FILL':
                units += float(i['units'])

        if units == 0:
            for i in self.transactions:
                self.oldTransactions.append(i)
            self.transactions = []

    def startPastPriceList(self, count):
        data = {'instrument': 'EUR_USD', 'granularity': 'M30', 'candles': []}
        self.line = count
        for i in range(count):
            data['candles'].append({
                'complete': True,
                'volume': int(self.data[i][6]),
                # 'time': datetime.strptime(f"{self.data[i][0]} {self.data[i][1]}", "%Y.%m.%d %H:%M").isoformat() + "Z",
                'time': self.data[i][0],
                'mid': {
                    'o': self.data[i][1],
                    'h': self.data[i][2],
                    'l': self.data[i][3],
                    'c': self.data[i][4]
                }
            })

        return data

    def updatePastPrices2(self):
        return {'instrument': 'EUR_USD', 'granularity': 'M30', 'candles': [{
            'complete': True,
            'volume': int(self.data[self.line][6]),
            # 'time': datetime.strptime(f"{self.data[self.line][0]} {self.data[self.line][1]}",
            #                           "%Y.%m.%d %H:%M").isoformat() + "Z",
            'time': self.data[self.line][0],
            'mid': {
                'o': self.data[self.line][1],
                'h': self.data[self.line][2],
                'l': self.data[self.line][3],
                'c': self.data[self.line][4]
            }
        }]}

    def marketOrder(self, data):
        self.id += 1
        batchId = self.id
        if float(data['order']['units']) > 0:
            self.transactions.append({
                'id': self.id,
                'time': self.time(),
                'batchID': batchId,
                'type': 'ORDER_FILL',
                'units': data['order']['units'],
                'price': str(self.data[self.line][4])
                # 'price': str(float(self.data[self.line][4]))
            })
        elif float(data['order']['units']) < 0:
            self.transactions.append({
                'id': self.id,
                'time': self.time(),
                'batchID': batchId,
                'type': 'ORDER_FILL',
                'units': data['order']['units'],
                'price': str(self.data[self.line][4])
                # 'price': str(float(self.data[self.line][4]))
            })
        try:
            if float(data['order']['units']) > 0:
                self.transactions.append({
                    'id': self.id,
                    'batchID': batchId,
                    'type': 'STOP_LOSS_ORDER',
                    'price': str(float(self.data[self.line][4]) - float(data['order']['stopLossOnFill']['distance']))
                })
            elif float(data['order']['units']) < 0:
                self.transactions.append({
                    'id': self.id,
                    'batchID': batchId,
                    'type': 'STOP_LOSS_ORDER',
                    'price': str(float(self.data[self.line][4]) + float(data['order']['stopLossOnFill']['distance']))
                })
        except KeyError as e:
            print(e)

        try:
            if float(data['order']['units']) > 0:
                self.transactions.append({
                    'id': self.id,
                    'batchID': batchId,
                    'type': 'TAKE_PROFIT_ORDER',
                    'price': str(float(self.data[self.line][4]) + float(data['order']['takeProfitOnFill']['distance']))
                })
            elif float(data['order']['units']) < 0:
                self.transactions.append({
                    'id': self.id,
                    'batchID': batchId,
                    'type': 'TAKE_PROFIT_ORDER',
                    'price': str(float(self.data[self.line][4]) - float(data['order']['takeProfitOnFill']['distance']))
                })
        except KeyError:
            pass

        try:
            self.transactions.append({
                'id': self.id,
                'batchID': batchId,
                'type': 'TRAILING_STOP_LOSS_ORDER',
                'distance': data['order']['trailingStopLossOnFill']['distance']
            })
            self.trailingStop.append([batchId,
                                      float(self.data[self.line][4]) - float(
                                          data['order']['trailingStopLossOnFill']['distance']),
                                      float(self.data[self.line][4]) + float(
                                          data['order']['trailingStopLossOnFill']['distance'])])
        except KeyError:
            pass

        # return res

    def limitOrder(self, data):
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

    def time(self):

        # return str(datetime.strptime(f"{self.data[self.line][0]} {self.data[self.line][1]}",
        #                              "%Y.%m.%d %H:%M").isoformat() + "Z")
        # return datetime.fromisoformat(self.data[self.line][0].replace("Z", "+00:00"))
        return self.data[self.line][0]
