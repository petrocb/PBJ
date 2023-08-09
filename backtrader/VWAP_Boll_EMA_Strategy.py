import backtrader as bt
from datetime import datetime
import numpy as np

class VWAP(bt.Indicator):
    lines = ('vwap',)

    def __init__(self):
        self.cum_value = 0.0
        self.cum_volume = 0.0
        self.addminperiod(1)  # Set minimum period to 1

    def next(self):

        typical_price = (self.data.high[0] + self.data.low[0] + self.data.close[0]) / 3
        self.cum_value += typical_price * self.data.volume[0]
        self.cum_volume += self.data.volume[0]

        if self.cum_volume != 0:
            self.lines.vwap[0] = self.cum_value / self.cum_volume
        else:
            self.lines.vwap[0] = self.data.close[0]

class VWAP_Boll_EMA_Strategy(bt.Strategy):
    params = (
        ('vwap_period', 20),
    )
    def __init__(self, arr, i):
        self.vwap = VWAP()
        self.buy_signal = False
        self.sell_signal = False
        print(i[0])
        print(i[1])
        self.bollinger_dev = 1.0  # Number of standard deviations
        self.short_ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=i[0])
        self.long_ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=i[1])
        self.arr = arr

    def next(self):
        vwap_value = self.vwap.lines.vwap[0]
        std_dev = self.bollinger_dev * vwap_value
        self.bollinger_upper = vwap_value + std_dev
        self.bollinger_lower = vwap_value - std_dev

        #print((self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1]) or (self.short_ema[0] < self.long_ema[0] and self.short_ema[-1] >= self.long_ema[-1]))
        if self.data.close[0] > self.bollinger_upper and self.short_ema[0] < self.long_ema[0] and self.short_ema[-1] >= self.long_ema[-1]:
            # Sell signal: short EMA crosses below long EMA
            self.sell(size=1)
            self.buyOpen = False
            self.arr.append(['s', self.data.close[0], 0,  self.broker.getvalue(), self.data.datetime.datetime()])
            # Close Sell order: short EMA crosses above long EMA
        if self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1]:
                self.close()
                self.sellOpen = False
                self.arr.append(['cs', self.data.close[0], 0, self.broker.getvalue(), self.data.datetime.datetime()])

        if self.data.close[0] < self.bollinger_lower and self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1]:
            # Buy signal: short EMA crosses above long EMA and Price below  lower bollinger
            self.buy(size=1)
            self.sellOpen = False
            self.arr.append(['b', self.data.close[0], 0,  self.broker.getvalue(), self.data.datetime.datetime()])
            # Close buy order: short EMA crosses below long EMA
        if self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1]:
                self.close()
                self.sellOpen = False
                self.arr.append(['cb', self.data.close[0], 0, self.broker.getvalue(), self.data.datetime.datetime()])
