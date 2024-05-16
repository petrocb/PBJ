import requests
import json
import backtrader as bt
import pandas as pd
import numpy as np
import functions

class EMACrossOver():
    def __init__(self):
        self.buyOpen = False #Unsure if these need to be adjusted?
        self.sellOpen = False #Unsure if these need to be adjusted?
        self.closes = functions.startPastPricesList()
        self.short_ema = functions.EMA2(self.closes[0:-10])
        self.long_ema = functions.EMA2(self.closes[0:-30])
        self.diff = 0.040
        self.Entry_price = float(self.closes[0])
        self.stop_loss = self.Entry_price + self.diff
        self.id = 0

    def tick(self):
        self.closes = functions.startPastPricesList()
        self.short_ema = functions.EMA2(self.closes[0:-10])
        self.long_ema = functions.EMA2(self.closes[0:-30])
        if self.short_ema[0] < self.long_ema[0] and self.short_ema[-1] >= self.long_ema[-1]:
            # Sell signal: short EMA crosses below long EMA
            Entry_price = self.closes
            self.stop_loss = Entry_price + self.diff
            self.id = functions.sell()
            self.buyOpen = False

        if self.sellOpen == True:
            if self.closes[-1] + self.diff < self.stop_loss[-1]:
                self.stop_loss[0] = self.data.close[-1] + self.diff
            elif self.closes[-1] + self.diff >= self.stop_loss[-1]:
                self.stop_loss[0] = self.stop_loss[-1]
            # Close Sell order: short EMA crosses above long EMA
        if self.closes[0] >= self.stop_loss:
            # self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1] or
            functions.close(self.id)
            self.sellOpen = False


    # def emaCalc(self, period):
    #     # return ema(functions.startPastPricesList(), period=period)
    #     print(ema(functions.startPastPricesList(), period=period).df)