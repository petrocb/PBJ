import csv

import 


class SMACrossOver():
    def __init__(self):
        self.account = "SMACrossOver"
        self.buyOpen = False  # Unsure if these need to be adjusted?
        self.sellOpen = False  # Unsure if these need to be adjusted?
        self.closes = functions.startPastPricesList(30, "EUR_USD", "M30", self.account)
        self.short_ema = [functions.sma(self.closes[-10:])]
        self.long_ema = [functions.sma(self.closes[-30:])]
        self.id = 0
        self.stopLoss = 0

    def tick(self):
        # print(cond)
        functions.time()
        self.closes = functions.updatePastPrices(self.closes, 30, "EUR_USD", "M30", self.account)
        # print(self.closes[-1])
        self.short_ema.append(functions.sma(self.closes[-cond[0]:]))
        self.long_ema.append(functions.sma(self.closes[-cond[1]:]))
        if len(self.short_ema) > 2:
            self.short_ema.pop(0)
        if len(self.long_ema) > 2:
            self.long_ema.pop(0)
        if self.short_ema[-1] < self.long_ema[-1] and self.short_ema[-2] >= self.long_ema[-2] and not self.sellOpen:
            # print("!!!!SELL!!!!")
            if self.id != 0:
                functions.close(self.id, self.account)
            self.id = functions.sell(cond[2], "SMACrossOver", self.account, 0.001, 0.001)
            self.sellOpen = True
            self.buyOpen = False
            self.stopLoss = self.closes[-1][1] + cond[2]

        if self.short_ema[-1] > self.long_ema[-1] and self.short_ema[-2] <= self.long_ema[-2] and not self.buyOpen:
            # print("!!!!BUY!!!!")
            if self.id != 0:
                functions.close(self.id, self.account)
            self.id = functions.buy(cond[2], self.account, 0.001, 0.001)
            self.sellOpen = False
            self.buyOpen = True
            self.stopLoss = self.closes[-1][1] - cond[2]

        if functions.getPositions(self.account)['positions'] == [] and self.buyOpen or functions.getPositions()[
            'positions'] == [] and self.sellOpen:
            self.buyOpen = False
            self.sellOpen = False

        with open('../response.csv', 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow([self.closes[-1], self.short_ema, self.long_ema, self.sellOpen, self.buyOpen])
        csvfile.close()

        functions.checkSLnTP()
