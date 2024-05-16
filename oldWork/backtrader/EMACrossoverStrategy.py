import backtrader as bt
from datetime import datetime

class EMACrossoverStrategy(bt.Strategy):
    def __init__(self, arr, i):
        self.buyOpen = False
        self.sellOpen = False
        print(i[0])
        print(i[1])
        self.short_ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=i[0])
        self.long_ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=i[1])
        self.arr = arr

    def next(self):
        #print((self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1]) or (self.short_ema[0] < self.long_ema[0] and self.short_ema[-1] >= self.long_ema[-1]))
        # print(self.short_ema[0])
        # print(self.long_ema[0])
        if self.short_ema[0] < self.long_ema[0] and self.short_ema[-1] >= self.long_ema[-1]:
            # Sell signal: short EMA crosses below long EMA
            self.sell(size=10)
            self.buyOpen = False
            self.arr.append(['s', self.data.close[0], 0,  self.broker.getvalue(), self.data.datetime.datetime()])
            # Close Sell order: short EMA crosses above long EMA
        if self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1]:
                self.close()
                self.sellOpen = False
                self.arr.append(['cs', self.data.close[0], 0, self.broker.getvalue(), self.data.datetime.datetime()])
