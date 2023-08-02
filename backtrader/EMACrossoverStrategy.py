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

        elif self.short_ema[0] < self.long_ema[0] and self.short_ema[-1] >= self.long_ema[-1]:
            # Sell signal: short EMA crosses below long EMA
            if self.position:
                self.sell(size=1)
                self.sell_signal = True

        # Log signals
        if self.buy_signal:
            self.log('Buy at {:.2f}'.format(self.data.close[0]))
            self.arr.append(['Buy', self.data.close[0], self.broker.getvalue(), self.data.datetime.datetime()])
            self.buy_signal = False

        if self.sell_signal:
            self.log('Sell at {:.2f}'.format(self.data.close[0]))
            self.arr.append(['Sell', self.data.close[0], self.broker.getvalue(), self.data.datetime.datetime()])
            self.sell_signal = False