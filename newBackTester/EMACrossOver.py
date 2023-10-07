import requests
import json
import pandas as pd
import numpy as np
import functions

class EMACrossOver():
    def __init__(self, cond):
        self.buyOpen = False #Unsure if these need to be adjusted?
        self.sellOpen = False #Unsure if these need to be adjusted?
        self.closes = functions.startPastPricesList()
        self.short = cond[0]
        self.long = cond[1]
        self.short_ema = [functions.sma(self.closes[-self.short:])]
        self.long_ema = [functions.sma(self.closes[-self.long:])]
        self.diff = 0.040
        self.Entry_price = float(self.closes[0][1])
        self.stop_loss = self.Entry_price + self.diff
        print(self.short, self.long)

    def tick(self):
        self.closes.append(functions.updatePastPrices(self.closes))
        self.short_ema.append(functions.sma(self.closes[-self.short:]))
        self.long_ema.append(functions.sma(self.closes[-self.long:]))
        # print(self.short_ema[-1])
        # print(self.long_ema[-1])
        if self.short_ema[-1] < self.long_ema[-1] and self.short_ema[-2] >= self.long_ema[-2] and not self.sellOpen:
            # Sell signal: short EMA crosses below long EMA
            self.Entry_price = self.closes[-1][1]
            self.stop_loss = self.Entry_price + self.diff
            functions.sell()
            self.sellOpen = True

        if self.short_ema[-1] > self.long_ema[-1] and self.short_ema[-2] <= self.long_ema[-2] and self.sellOpen:
            functions.close()
            self.sellOpen = False

        # if self.sellOpen:
        #     if self.closes[-1][1] + self.diff < self.stop_loss:
        #         self.stop_loss = self.closes[-1][1] + self.diff
        #     elif self.closes[-1][1] + self.diff >= self.stop_loss:
        #         self.stop_loss = self.stop_loss
        #     # Close Sell order: short EMA crosses above long EMA
        # if self.closes[-1][1] >= self.stop_loss:
        #     # self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1] or
        #     functions.close()
        #     self.sellOpen = False

    # def emaCalc(self, period):
    #     # return ema(functions.startPastPricesList(), period=period)
    #     print(ema(functions.startPastPricesList(), period=period).df)