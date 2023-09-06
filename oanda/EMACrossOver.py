import requests
import json
from btalib import ema
import pandas as pd
import functions

class EMACrossOver():
    def __init__(self, closes):
        self.buyOpen = False
        self.sellOpen = False
        self.shortEma = self.emaCalc(10, list)
        self.longEma = self.emaCalc(30, list)
        self.closes = functions.updatePastPrices()

    def tick(self):
        # if self.short_ema[0] < self.long_ema[0] and self.short_ema[-1] >= self.long_ema[-1]:
        pass

    def emaCalc(self, period, closes):
        # print(type(list))
        # list = pd.DataFrame(list['candles'])
        # print(type(list))
        #print(list)
        # return ema(list, period=period)
        #return 0
        # Extract the 'c' (close) values from the DataFrame
        #closes = [float(candle['mid']['c']) for candle in list['candles']]
        #closes = pd.Series(closes, index=pd.to_datetime([candle['time'] for candle in list['candles']]))

        # Calculate the EMA
        return ema(closes, period=period)
