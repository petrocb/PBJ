import requests
import json
from btalib import ema

class EMACrossOver():
    def __init__(self):
        self.buyOpen = False
        self.sellOpen = False
        self.shortEma = self.emaCalc(10)
        self.longEma = self.emaCalc(30)

    def tick(self):
        # if self.short_ema[0] < self.long_ema[0] and self.short_ema[-1] >= self.long_ema[-1]:
        pass

    def emaCalc(self, peroid):
        #return ema(0, peroid=peroid)
        return 0
