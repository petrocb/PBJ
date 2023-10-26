import functions
import csv
import time


class NewSMACross():
    def __init__(self, cond):
        self.cond = cond
        self.buyOpen = False
        self.sellOpen = False
        if cond[0] > cond[1]:
            self.closes = functions.startPastPricesList(self.cond[0], 'EUR_USD', "M1")
        else:
            self.closes = functions.startPastPricesList(self.cond[1], 'EUR_USD', "M1")
        self.short_ema = [functions.sma(self.closes[-self.cond[0]:])]
        self.long_ema = [functions.sma(self.closes[-self.cond[1]:])]
        self.id = 0
        self.direction = functions.startPastPricesList(60, 'EUR_USD', "M1")

    def tick(self):

        functions.checkSLnTP()
        if functions.openTrades()['positions'] == []:
            self.buyOpen = False
            self.sellOpen = False

        if self.cond[0] > self.cond[1]:
            self.closes = functions.updatePastPrices(self.closes, self.cond[0], 'EUR_USD', "M1")
        else:
            self.closes = functions.updatePastPrices(self.closes, self.cond[0], 'EUR_USD', "M1")
        self.short_ema.append(functions.sma(self.closes[-self.cond[0]:]))
        self.long_ema.append(functions.sma(self.closes[-self.cond[1]:]))
        if len(self.short_ema) > 2:
            self.short_ema.pop(0)
        if len(self.long_ema) > 2:
            self.long_ema.pop(0)
        self.direction = functions.updatePastPrices(self.direction, 60, 'EUR_USD', "M1")

        time = functions.time()
        # print(time)
        if 6 < time < 19:
            # No trades open
            if (self.short_ema[1] > self.long_ema[1]) and (self.short_ema[0] <= self.long_ema[0]) and (not self.sellOpen) and (not self.buyOpen) and (functions.getDirection(self.direction) == "up"):
                print("!!!!BUY!!!!")
                self.id = functions.buy(self.cond[2], self.cond[3], "EUR_USD")
                self.sellOpen = False
                self.buyOpen = True

            # print(self.short_ema[1] < self.long_ema[1], self.short_ema[0] >= self.long_ema[0], not self.sellOpen, not self.buyOpen)
            if (self.short_ema[1] < self.long_ema[1]) and (self.short_ema[0] >= self.long_ema[0]) and (not self.sellOpen) and (not self.buyOpen) and (functions.getDirection(self.direction) == "down"):
                print("!!!!SELL!!!!")
                self.id = functions.sell(self.cond[2], self.cond[3], "EUR_USD")
                self.sellOpen = True
                self.buyOpen = False

            # Trades open
            if self.short_ema[1] < self.long_ema[1] and self.short_ema[0] >= self.long_ema[
                0] and self.buyOpen and not self.sellOpen:
                # print("!!!!CLOSE!!!!")
                self.id = functions.close(self.id)
                self.sellOpen = False
                self.buyOpen = False

            if self.short_ema[1] > self.long_ema[1] and self.short_ema[0] <= self.long_ema[
                0] and self.sellOpen and not self.buyOpen:
                # print("!!!!CLOSE!!!!")
                self.id = functions.close(self.id)
                self.sellOpen = False
                self.buyOpen = False

            with open('response.csv', 'a', newline='') as csvfile:
                csvWriter = csv.writer(csvfile)
                csvWriter.writerow([self.closes[-1], self.short_ema, self.long_ema, self.sellOpen, self.buyOpen, functions.getDirection(self.direction)])
            csvfile.close()
