import backtrader as bt
from datetime import datetime

class EMACrossoverStopBuy(bt.Strategy):
    def __init__(self, arr, i):
        self.buyOpen = False
        self.sellOpen = False
        print(i[0])
        print(i[1])
        self.short_ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=i[0])
        self.long_ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=i[1])
        self.diff = 0.0005
        Entry_price = self.data.close
        self.stop_loss = Entry_price - self.diff
        self.arr = arr

    def next(self):
        #print((self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1]) or (self.short_ema[0] < self.long_ema[0] and self.short_ema[-1] >= self.long_ema[-1]))
        # print(self.short_ema[0])
        # print(self.long_ema[0])
        if self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1]:
            Entry_price = self.data.close
            self.stop_loss = Entry_price - self.diff
            # buy signal: short EMA crosses above long EMA
            self.buy(size=1)
            self.sellOpen = False
            self.arr.append(['b', self.data.close[0], 0,  self.broker.getvalue(), self.data.datetime.datetime()])
        if self.buyOpen == True:
            if self.data.close[-1] - self.diff > self.stop_loss[-1]:
                self.stop_loss[0] = self.data.close[-1] - self.diff
            elif self.data.close[-1] - self.diff <= self.stop_loss[-1]:
                  self.stop_loss[0] = self.stop_loss[-1]
            # Close Sell order: short EMA crosses above long EMA
        if self.data.close[0] <= self.stop_loss:
        #self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1] or
                self.close()
                self.buyOpen = False
                self.arr.append(['cb', self.data.close[0], 0, self.broker.getvalue(), self.data.datetime.datetime()])
