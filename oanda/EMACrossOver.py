import requests
import json
from btalib import ema
import pandas as pd
import functions

class EMACrossOver():
    def __init__(self, closes):
        self.buyOpen = False #Unsure if these need to be adjusted?
        self.sellOpen = False #Unsure if these need to be adjusted?
        self.shortEma = self.emaCalc(10, closes)  # Calculate short EMA with provided closes
        self.longEma = self.emaCalc(30, closes)   # Calculate long EMA with provided closes
        self.closes = closes
        self.diff = 0.040
        Entry_price = self.data.close
        self.stop_loss = Entry_price + self.diff

    def tick(self):
        if self.shortEma[0] < self.longEma[0] and self.shortEma[-1] >= self.longEma[-1]:
            # Sell signal: short EMA crosses below long EMA
            Entry_price = self.closes
            self.stop_loss = Entry_price + self.diff
            self.sell()
            self.buyOpen = False

        if self.sellOpen == True:
            if self.closes[-1] + self.diff < self.stop_loss[-1]:
                self.stop_loss[0] = self.data.close[-1] + self.diff
            elif self.closes[-1] + self.diff >= self.stop_loss[-1]:
                self.stop_loss[0] = self.stop_loss[-1]
            # Close Sell order: short EMA crosses above long EMA
        if self.closes[0] >= self.stop_loss:
            # self.short_ema[0] > self.long_ema[0] and self.short_ema[-1] <= self.long_ema[-1] or
            self.close()
            self.sellOpen = False

    def emaCalc(self, period, closes):
        return ema(closes, period=period)

    def buy(self):
        # Place a buy order
        # You want this to be done a certain way and im not sure of the code
        # Need to define how to tell API to initiate trade in the way you want
        pass

    def sell(self):
        # Place a sell order
        # You want this to be done a certain way and im not sure of the code
        # Need to define how to tell API to initiate trade in the way you want
        pass

    def close(self):
        # Close an existing order
        # You want this to be done a certain way and im not sure of the code
        # Need to define how to tell API to initiate trade in the way you want
        pass
