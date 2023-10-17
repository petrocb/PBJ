import functions
import csv
import time

class SMACrossOver():
    def __init__(self):
        self.buyOpen = False  # Unsure if these need to be adjusted?
        self.sellOpen = False  # Unsure if these need to be adjusted?
        self.closes = functions.startPastPricesList(80)
        self.short_ema = [functions.sma(self.closes[-10:])]
        self.long_ema = [functions.sma(self.closes[-30:])]
        self.id = 0
        self.stopLoss = 0
        # print(self.short, self.long)


    def tick(self, cond):
        # print(cond)
        self.closes = functions.updatePastPrices(self.closes, 80)
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
                functions.close(self.id)
            self.id = functions.sell()
            self.sellOpen = True
            self.buyOpen = False
            self.stopLoss = self.closes[-1][1] + cond[2]

        if self.short_ema[-1] > self.long_ema[-1] and self.short_ema[-2] <= self.long_ema[-2] and not self.buyOpen:
            # print("!!!!BUY!!!!")
            if self.id != 0:
                functions.close(self.id)
            self.id = functions.buy()
            self.sellOpen = False
            self.buyOpen = True
            self.stopLoss = self.closes[-1][1] - cond[2]
        # print("price:", self.closes[-1][1])
        # print("stopLoss:", self.stopLoss)
        if self.buyOpen and self.closes[-1][1] < self.stopLoss:
            print("STOP")
            # time.sleep(30)
            functions.close(self.id)
            self.id = 0
            self.buyOpen = False
            self.sellOpen = False

        if self.sellOpen and self.closes[-1][1] > self.stopLoss:
            print("STOP")
            # time.sleep(30)
            functions.close(self.id)
            self.id = 0
            self.buyOpen = False
            self.sellOpen = False

        with open('response.csv', 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow([self.closes[-1], self.short_ema, self.long_ema, self.sellOpen, self.buyOpen])
        csvfile.close()
        # print("closes:", self.closes)
        # print(" short:", self.short_ema,
        #       " long:", self.long_ema)
        # print(" open:", self.sellOpen)