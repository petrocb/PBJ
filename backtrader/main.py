import backtrader as bt
import numpy as np


def diffCalc(pastPrices):
    diff = 0.002
    vol = np.std(pastPrices) * np.sqrt(20)
    print(vol)
    return vol * 10


class Strategy(bt.Strategy):
    def __init__(self):
        pastPrices = []
        for x in range(20):
            pastPrices.append(self.data.close[-x])
            # print(self.data.close[-x])
        self.diff = diffCalc(pastPrices)
        self.buyOpen = False
        self.sellOpen = False
        self.spread = 0.00011

    def next(self):

        self.price = self.data.close[0]  # Assuming you're using the close price as data
        self.bid = self.price - self.spread
        self.ask = self.price + self.spread
        self.newAsk = self.ask - self.diff
        self.newBid = self.bid + self.diff
        pastprices = []
        for x in range(20):
            pastprices.append(self.data.close[-x])
            # print(self.data.close[-x])

        if not self.buyOpen and not self.sellOpen:
            self.startingAsk = self.ask
            self.startingBid = self.bid
            self.trailingBuy = self.ask - self.diff
            self.trailingSell = self.bid + self.diff
            self.buyOpen = True
            self.sellOpen = True

        # trailing
        if self.trailingBuy < self.newAsk:
            self.trailingBuy = self.newAsk

        if self.trailingSell > self.newBid:
            self.trailingSell = self.newBid

        # opening trade
        if self.trailingBuy > self.price and self.buyOpen and self.sellOpen:
            # Open sell order
            # print(self.data.close[0])
            self.sell(size= 1000)
            self.buyOpen = False
            # print(self.data.datetime.date().isoformat(), 'SELL!!!!!!!!!!''price:', self.price, 'newAsk:', self.newAsk, 'newBid:', self.newBid,
            # 'startingAsk:', self.startingAsk, 'startingBid:', self.startingBid, 'trailingBuy:', self.trailingBuy,
            # 'tralingBid', self.trailingSell, 'buyOpen:', self.buyOpen, 'sellOpen:', self.sellOpen)
            print(cerebro.broker.getvalue())

        if self.trailingSell < self.price and self.buyOpen and self.sellOpen:
            # Open buy order
            # print(self.data.close[0])
            self.buy(size= 1000)
            self.sellOpen = False
            # print(self.data.datetime.date().isoformat(), 'BUY!!!!!!!!!!''price:',self.price, 'newAsk:', self.newAsk, 'newBid:', self.newBid,
            #       'startingAsk:', self.startingAsk, 'startingBid:', self.startingBid, 'trailingBuy:', self.trailingBuy,
            #       'tralingBid', self.trailingSell, 'buyOpen:', self.buyOpen, 'sellOpen:', self.sellOpen)
            print(cerebro.broker.getvalue())

        if self.trailingBuy > self.price and self.buyOpen :
            # Close buy order
            # print(self.data.close[0])
            self.close()
            self.buyOpen = False
            # print(self.data.datetime.date().isoformat(), 'CLOSE!!!!!!!!!!''price:', self.price, 'newAsk:', self.newAsk, 'newBid:', self.newBid,
            #       'startingAsk:', self.startingAsk, 'startingBid:', self.startingBid, 'trailingBuy:', self.trailingBuy,
            #       'tralingBid', self.trailingSell, 'buyOpen:', self.buyOpen, 'sellOpen:', self.sellOpen)
            print(cerebro.broker.getvalue())

        if self.trailingSell < self.price and self.sellOpen:
            # Close sell order
            # print(self.data.close[0])
            self.close()
            self.sellOpen = False
            # print(self.data.datetime.date().isoformat(), 'CLOSE!!!!!!!!!!''price:', self.price, 'newAsk:', self.newAsk, 'newBid:', self.newBid,
            #       'startingAsk:', self.startingAsk, 'startingBid:', self.startingBid, 'trailingBuy:', self.trailingBuy,
            #       'tralingBid', self.trailingSell, 'buyOpen:', self.buyOpen, 'sellOpen:', self.sellOpen)
            print(cerebro.broker.getvalue())

        '''print('price:', self.price, 'newAsk:', self.newAsk, 'newBid:', self.newBid,
              'startingAsk:', self.startingAsk, 'startingBid:', self.startingBid, 'trailingBuy:', self.trailingBuy,
              'tralingBid', self.trailingSell, 'buyOpen:', self.buyOpen, 'sellOpen:', self.sellOpen)'''


cerebro = bt.Cerebro()
cerebro.addstrategy(Strategy)
data = bt.feeds.MT4CSVData(dataname='C:/Users/St Potrock/Desktop/EURUSD2.csv',
                           timeframe=bt.TimeFrame.Minutes,
                           compression=1)
cerebro.adddata(data)
cerebro.run()
cerebro.plot()
print(cerebro.broker.getvalue())
