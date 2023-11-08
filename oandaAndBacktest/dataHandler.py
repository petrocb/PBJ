import json


class dataHandler:

    def __init__(self):
        self.x = 0

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

        # Serialize the back tester data to JSON
        back_tester_response = json.dumps(back_tester_data)
        return back_tester_response

    def getPriceSince(self):
        pass

    def GetBid(self):
        pass

    def getAsk(self):
        pass

    def startPastPriceList(self):
        pass

    def updatePastPrices(self):
        pass

    def updatePastPrices2(self):
        pass

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
