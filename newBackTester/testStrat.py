import functions
import csv

class TestStrat():
    def __init__(self):
        self.closes = functions.startPastPricesList()
        self.id = 0
    def tick(self, cond):
        print(self.closes)
        print(self.id)
        self.closes = functions.updatePastPrices(self.closes)
        if self.id == 0:
            print("sell")
            functions.sell()
        elif self.id == 1:
            print("close")
            functions.close(0)
        elif self.id == 2:
            print("buy")
            functions.buy()
        elif self.id == 3:
            print("close")
            functions.close(0)
        self.id += 1
