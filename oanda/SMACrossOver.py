import functions
import csv

class SMACrossOver():
    def __init__(self):
        self.buyOpen = False  # Unsure if these need to be adjusted?
        self.sellOpen = False  # Unsure if these need to be adjusted?
        self.closes = functions.startPastPricesList()
        self.short_ema = [functions.sma(self.closes[-10:])]
        self.long_ema = [functions.sma(self.closes[-30:])]
        self.id = 0

    def tick(self):
        self.closes = functions.updatePastPrices(self.closes)
        self.short_ema.append(functions.sma(self.closes[-10:]))
        self.long_ema.append(functions.sma(self.closes[-30:]))
        if len(self.short_ema) > 2:
            self.short_ema.pop(0)
        if len(self.long_ema) > 2:
            self.long_ema.pop(0)
        if self.short_ema[-1] < self.long_ema[-1] and self.short_ema[-2] >= self.long_ema[-2] and not self.sellOpen:
            print("!!!!SELL!!!!")
            if self.id != 0:
                functions.close(self.id)
            self.id = functions.sell()
            self.sellOpen = True
            self.buyOpen = False

        if self.short_ema[-1] > self.long_ema[-1] and self.short_ema[-2] <= self.long_ema[-2] and not self.buyOpen:
            print("!!!!BUY!!!!")
            if self.id != 0:
                functions.close(self.id)
            self.id = functions.buy()
            self.sellOpen = False
            self.buyOpen = True


        with open('output.csv', 'a', newline='') as csvfile:
            csvWriter = csv.writer(csvfile)
            csvWriter.writerow([self.closes, self.short_ema, self.long_ema, self.sellOpen, self.buyOpen])
        csvfile.close()
        print("closes:", self.closes)
        print(" short:", self.short_ema,
              " long:", self.long_ema)
        print("sell buy open:", self.sellOpen, self.buyOpen)
