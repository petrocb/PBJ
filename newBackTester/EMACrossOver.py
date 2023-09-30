import requests
import json
from btalib import ema
import backtrader as bt
import pandas as pd
import numpy as np
import functions

class EMACrossOver():
    def __init__(self):
        self.buyOpen = False #Unsure if these need to be adjusted?
        self.sellOpen = False #Unsure if these need to be adjusted?
        self.closes = functions.startPastPricesList()
        print(self.closes)
        print(len(self.closes))
        self.short_ema = functions.sma(self.closes[-10:])
        self.long_ema = functions.sma(self.closes[-30:])
        self.diff = 0.040
        self.Entry_price = float(self.closes[0][1])
        self.stop_loss = self.Entry_price + self.diff

    def tick(self):
        self.closes = functions.updatePastPrices(self.closes)
        self.short_ema = functions.sma(self.closes[-10:])
        self.long_ema = functions.sma(self.closes[-30:])
        if self.short_ema < self.long_ema and self.short_ema >= self.long_ema:
            # Sell signal: short EMA crosses below long EMA
            Entry_price = self.closes
            self.stop_loss = Entry_price + self.diff
            functions.sell()
            self.buyOpen = False

        if self.sellOpen == True:
            if self.closes + self.diff < self.stop_loss:
                self.stop_loss = self.data.close + self.diff
            elif self.closes[-1] + self.diff >= self.stop_loss:
                self.stop_loss = self.stop_loss
            # Close Sell order: short EMA crosses above long EMA
        if self.closes[-1][-1] >= self.stop_loss:
            # self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1] or
            functions.close()
            self.sellOpen = False

    # def emaCalc(self, period):
    #     # return ema(functions.startPastPricesList(), period=period)
    #     print(ema(functions.startPastPricesList(), period=period).df)