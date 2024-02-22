import csv
from datetime import datetime
from .. import functions

class highResLongTrend:
    def __init__(self, account):
        self.account = account
        self.data = functions.startPastPricesList(30, "EUR_USD", "D", self.account)

    def tick(self):
        if self.account == "test":
            functions.update()
        self.data = functions.updatePastPrices2(self.data, 30, "EUR_USD", "D", self.account)
        sma = functions.sma(self.data)
        lines = [sma + functions.std(self.data), sma - functions.std(self.data)]
        price = functions.startPastPricesList(1, "EUR_USD", "S5", self.account)[0][1]
        position = functions.getPositions(self.account)['positions']
        direction = 0
        if position:
            position = float(position[0]['long']['units']) + float(position[0]['short']['units'])
        else:
            position = 0
        if position == 0:
            if price > lines[0]:
                direction = 1
            elif price < lines[1]:
                direction = -1
        elif position > 0 and price < lines[1]:
            direction = 0
        elif position < 0 and price > lines[0]:
            direction = 0
        direction *= 500
        print(direction)
        if position != direction:
            functions.marketOrder(float(direction) - float(position), self.account, self.account, 0, 0, 0)

        print(direction, "    ", position)
        print("price", price)
        print("lines", lines)
        print("dif" , price - lines[0], price - lines[1])



