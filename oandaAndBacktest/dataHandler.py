import json
# from unittest import MagicMock

class dataHandler:

    def __init__(self):
        self.trades = {'trades': [], 'lastTransactionID': '0'}
        self.position = {'positions': [], 'lastTransactionID': '12244'}
        self.orders = []
        self.activity = []
        self.line = 0

    def update(self):
        self.line += 1


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

    def startPastPriceList(self):
        return {'instrument': 'EUR_USD', 'granularity': 'M30', 'candles': [{'complete': True, 'volume': 2154, 'time': '2023-11-10T17:00:00.000000000Z', 'mid': {'o': '1.06694', 'h': '1.06751', 'l': '1.06641', 'c': '1.06660'}}, {'complete': True, 'volume': 2035, 'time': '2023-11-10T17:30:00.000000000Z', 'mid': {'o': '1.06658', 'h': '1.06819', 'l': '1.06658', 'c': '1.06794'}}, {'complete': True, 'volume': 1894, 'time': '2023-11-10T18:00:00.000000000Z', 'mid': {'o': '1.06793', 'h': '1.06828', 'l': '1.06730', 'c': '1.06796'}}, {'complete': True, 'volume': 1376, 'time': '2023-11-10T18:30:00.000000000Z', 'mid': {'o': '1.06797', 'h': '1.06846', 'l': '1.06787', 'c': '1.06812'}}, {'complete': True, 'volume': 1296, 'time': '2023-11-10T19:00:00.000000000Z', 'mid': {'o': '1.06812', 'h': '1.06876', 'l': '1.06808', 'c': '1.06852'}}, {'complete': True, 'volume': 1518, 'time': '2023-11-10T19:30:00.000000000Z', 'mid': {'o': '1.06853', 'h': '1.06853', 'l': '1.06788', 'c': '1.06796'}}, {'complete': True, 'volume': 1275, 'time': '2023-11-10T20:00:00.000000000Z', 'mid': {'o': '1.06796', 'h': '1.06848', 'l': '1.06772', 'c': '1.06834'}}, {'complete': True, 'volume': 1190, 'time': '2023-11-10T20:30:00.000000000Z', 'mid': {'o': '1.06836', 'h': '1.06876', 'l': '1.06836', 'c': '1.06854'}}, {'complete': True, 'volume': 613, 'time': '2023-11-10T21:00:00.000000000Z', 'mid': {'o': '1.06851', 'h': '1.06874', 'l': '1.06838', 'c': '1.06848'}}, {'complete': True, 'volume': 781, 'time': '2023-11-10T21:30:00.000000000Z', 'mid': {'o': '1.06848', 'h': '1.06863', 'l': '1.06826', 'c': '1.06847'}}]}


    def updatePastPrices(self):
        pass

    def updatePastPrices2(self):
        return {'instrument': 'EUR_USD', 'granularity': 'M30', 'candles': [{'complete': True, 'volume': 2154, 'time': '2023-11-10T17:00:00.000000000Z', 'mid': {'o': '1.06694', 'h': '1.06751', 'l': '1.06641', 'c': '1.06660'}}, {'complete': True, 'volume': 2035, 'time': '2023-11-10T17:30:00.000000000Z', 'mid': {'o': '1.06658', 'h': '1.06819', 'l': '1.06658', 'c': '1.06794'}}, {'complete': True, 'volume': 1894, 'time': '2023-11-10T18:00:00.000000000Z', 'mid': {'o': '1.06793', 'h': '1.06828', 'l': '1.06730', 'c': '1.06796'}}, {'complete': True, 'volume': 1376, 'time': '2023-11-10T18:30:00.000000000Z', 'mid': {'o': '1.06797', 'h': '1.06846', 'l': '1.06787', 'c': '1.06812'}}, {'complete': True, 'volume': 1296, 'time': '2023-11-10T19:00:00.000000000Z', 'mid': {'o': '1.06812', 'h': '1.06876', 'l': '1.06808', 'c': '1.06852'}}, {'complete': True, 'volume': 1518, 'time': '2023-11-10T19:30:00.000000000Z', 'mid': {'o': '1.06853', 'h': '1.06853', 'l': '1.06788', 'c': '1.06796'}}, {'complete': True, 'volume': 1275, 'time': '2023-11-10T20:00:00.000000000Z', 'mid': {'o': '1.06796', 'h': '1.06848', 'l': '1.06772', 'c': '1.06834'}}, {'complete': True, 'volume': 1190, 'time': '2023-11-10T20:30:00.000000000Z', 'mid': {'o': '1.06836', 'h': '1.06876', 'l': '1.06836', 'c': '1.06854'}}, {'complete': True, 'volume': 613, 'time': '2023-11-10T21:00:00.000000000Z', 'mid': {'o': '1.06851', 'h': '1.06874', 'l': '1.06838', 'c': '1.06848'}}, {'complete': True, 'volume': 781, 'time': '2023-11-10T21:30:00.000000000Z', 'mid': {'o': '1.06848', 'h': '1.06863', 'l': '1.06826', 'c': '1.06847'}}]}


    def buy(self):
        pass

    def sell(self):
        pass

    def order(self):
        pass

    def close(self):
        pass

    def getPositions(self):
        pass

    def getOrders(self):
        pass

    def getTrades(self):
        pass

    def getTransactionsSinceID(self):
        pass

    def getTransactionsSinceDate(self):
        pass

    def time(self):
        pass
