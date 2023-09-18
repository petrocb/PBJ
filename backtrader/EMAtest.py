import backtrader as bt
from datetime import datetime

class EMAtest(bt.Strategy):
    def __init__(self):
        self.ema = bt.indicators.ExponentialMovingAverage(self.data.close, period=6)


    def next(self):
        print(self.ema[0])