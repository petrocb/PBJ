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
        if self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1]:
            # Buy signal: short EMA crosses above long EMA
            if not self.position:
                self.buy(size=1)
                self.buy_signal = True
                self.arr.append(['b', self.data.close[0], 0,  self.broker.getvalue(), self.data.datetime.datetime()])

        elif self.short_ema[0] < self.long_ema[0] and self.short_ema[-1] >= self.long_ema[-1]:
            # Sell signal: short EMA crosses below long EMA
            if self.position:
                self.sell(size=1)
                self.sell_signal = True
                self.arr.append(['s', self.data.close[0], self.broker.getvalue(), self.data.datetime.datetime()])
