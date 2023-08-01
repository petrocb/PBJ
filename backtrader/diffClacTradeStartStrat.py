import backtrader as bt
import functions

class diffClacTradeStartStrat(bt.Strategy):
    def __init__(self, arr):
        print("Starting strategy")
        pastPrices = []
        for x in range(20):
            pastPrices.append(self.data.close[-x])
            #print(self.data.close[-x])
        self.diff = functions.volatility(pastPrices, 20)
        self.buyOpen = False
        self.sellOpen = False
        self.spread = 0.00011
        self.arr = arr
        self.count = 43800

    def next(self):
        self.price = self.data.close[0]
        self.bid = self.price - self.spread
        self.ask = self.price + self.spread
        self.newAsk = self.ask - self.diff
        self.newBid = self.bid + self.diff
        if not self.buyOpen and not self.sellOpen:
            pastPrices = []
            for x in range(20):
                 pastPrices.append(self.data.close[-x])
                 self.diff = functions.volatility(pastPrices, 20)
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
        if self.trailingBuy > self.ask and self.buyOpen and self.sellOpen:
            # Open sell order
            self.sell(size= 1)
            self.buyOpen = False
            self.arr.append(['s', self.ask, self.bid, self.broker.getvalue(), self.data.datetime.datetime()])

        if self.trailingSell < self.bid and self.buyOpen and self.sellOpen:
            # Open buy order
            self.buy(size= 1)
            self.sellOpen = False
            self.arr.append(['b', self.ask, self.bid, self.broker.getvalue(), self.data.datetime.datetime()])

        if self.trailingBuy > self.ask and self.buyOpen :
            # Close buy order
            self.close()
            self.buyOpen = False
            self.arr.append(['cb', self.ask, self.bid, self.broker.getvalue(), self.data.datetime.datetime()])
        if self.trailingSell < self.bid and self.sellOpen:
            # Close sell order
            self.close()
            self.sellOpen = False
            self.arr.append(['cs', self.ask, self.bid, self.broker.getvalue(), self.data.datetime.datetime()])

        '''print('price:', self.price, 'newAsk:', self.newAsk, 'newBid:', self.newBid,
              'startingAsk:', self.startingAsk, 'startingBid:', self.startingBid, 'trailingBuy:', self.trailingBuy,
              'tralingBid', self.trailingSell, 'buyOpen:', self.buyOpen, 'sellOpen:', self.sellOpen)'''
        #print(self.arr)

        if self.count == 43800:
            print(self.data.datetime.date())
            self.count = 0
        self.count += 1