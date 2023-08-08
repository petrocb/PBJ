import backtrader as bt
from datetime import datetime

class EMACrossoverStrategy(bt.Strategy):
    def __init__(self, arr):
        self.buy_signal = False
        self.sell_signal = False
        self.short_ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=10)
        self.long_ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=30)
        self.arr = arr

    def next(self):
        #print((self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1]) or (self.short_ema[0] < self.long_ema[0] and self.short_ema[-1] >= self.long_ema[-1]))
        if self.short_ema[0] < self.long_ema[0] and self.short_ema[-1] >= self.long_ema[-1]:
            # Sell signal: short EMA crosses below long EMA
            self.sell(size=1)
            self.buyOpen = False
            self.arr.append(['s', self.data.close[0], 0,  self.broker.getvalue(), self.data.datetime.datetime()])
            # Close Sell order: short EMA crosses above long EMA
            if self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1]:
                self.close()
                self.sellOpen = False
                self.arr.append(['b', self.data.close[0], self.broker.getvalue(), self.data.datetime.datetime()])
