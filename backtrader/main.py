import backtrader as bt



class Stratergy(bt.Strategy):
    def __init__(self):
        self.diff = 0.044
        self.buyOpen = False
        self.sellOpen = False

    def next(self):
        
        self.price = self.data.close[0]  # Assuming you're using the close price as data
        self.newAsk = self.data.close[0] + self.diff
        self.newBid = self.data.close[0] - self.diff

        if not self.buyOpen and not self.sellOpen:
            self.startingAsk = self.data.close[0]
            self.startingBid = self.data.close[0]
            self.trailingAsk = self.data.close[0] - self.diff
            self.trailingBid = self.data.close[0] + self.diff
            self.buyOpen = True
            self.sellOpen = True

        if self.trailingAsk < self.newAsk:
            self.trailingAsk = self.newAsk

        if self.trailingBid > self.newBid:
            self.trailingBid = self.newBid

        if self.trailingAsk > self.data.close[0] and self.buyOpen and self.sellOpen:
            # Open sell order
            #print(self.data.close[0])
            self.sell()
            self.buyOpen = False
            print('OPEN!!!!!!!!!!''price:', self.data.close[0], 'newAsk:', self.newAsk, 'newBid:', self.newBid,
                  'startingAsk:', self.startingAsk, 'startingBid:', self.startingBid, 'trailingAsk:', self.trailingAsk,
                  'tralingBid', self.trailingBid, 'buyOpen:', self.buyOpen, 'sellOpen:', self.sellOpen)

        if self.trailingBid < self.data.close[0] and self.buyOpen and self.sellOpen:
            # Open buy order
            #print(self.data.close[0])
            self.buy()
            self.sellOpen = False
            print('OPEN!!!!!!!!!!''price:', self.data.close[0], 'newAsk:', self.newAsk, 'newBid:', self.newBid,
                  'startingAsk:', self.startingAsk, 'startingBid:', self.startingBid, 'trailingAsk:', self.trailingAsk,
                  'tralingBid', self.trailingBid, 'buyOpen:', self.buyOpen, 'sellOpen:', self.sellOpen)

        if self.trailingAsk > self.data.close[0] and self.buyOpen:
            # Close buy order
            #print(self.data.close[0])
            #self.close()
            self.buyOpen = False
            print('CLOSE!!!!!!!!!!''price:', self.data.close[0], 'newAsk:', self.newAsk, 'newBid:', self.newBid,
                  'startingAsk:', self.startingAsk, 'startingBid:', self.startingBid, 'trailingAsk:', self.trailingAsk,
                  'tralingBid', self.trailingBid, 'buyOpen:', self.buyOpen, 'sellOpen:', self.sellOpen)

        if self.trailingBid < self.data.close[0] and self.sellOpen:
            # Close sell order
            #print(self.data.close[0])
            #self.close()
            self.sellOpen = False
            print('CLOSE!!!!!!!!!!''price:', self.data.close[0], 'newAsk:', self.newAsk, 'newBid:', self.newBid,
                  'startingAsk:', self.startingAsk, 'startingBid:', self.startingBid, 'trailingAsk:', self.trailingAsk,
                  'tralingBid', self.trailingBid, 'buyOpen:', self.buyOpen, 'sellOpen:', self.sellOpen)

        print('price:', self.data.close[0], 'newAsk:', self.newAsk, 'newBid:', self.newBid,
        'startingAsk:', self.startingAsk, 'startingBid:', self.startingBid, 'trailingAsk:', self.trailingAsk,
        'tralingBid', self.trailingBid, 'buyOpen:', self.buyOpen, 'sellOpen:', self.sellOpen)

cerebro = bt.Cerebro()

cerebro.addstrategy(Stratergy)

data = bt.feeds.MT4CSVData(dataname='C:/Users/St Potrock/Desktop/EURUSD2.csv',
                           timeframe=bt.TimeFrame.Minutes,
                           compression=1)
cerebro.adddata(data)

cerebro.run()

cerebro.plot()

print(cerebro.broker.getvalue())

