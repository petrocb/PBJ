import functions


class SMACrossOver():
    def __init__(self):
        self.buyOpen = False  # Unsure if these need to be adjusted?
        self.sellOpen = False  # Unsure if these need to be adjusted?
        self.closes = functions.startPastPricesList()
        self.short_ema = [functions.sma(self.closes[-10:])]
        self.long_ema = [functions.sma(self.closes[-30:])]
        self.diff = 0.040
        self.Entry_price = float(self.closes[0][1])
        self.stop_loss = self.Entry_price + self.diff
        self.id = 0

    def tick(self):
        self.closes = functions.updatePastPrices(self.closes)
        self.short_ema.append(functions.sma(self.closes[-10:]))
        self.long_ema.append(functions.sma(self.closes[-30:]))
        # print(self.closes[-1])
        # print(self.short_ema[-1])
        # print(self.long_ema[-1])
        if self.short_ema[-1] < self.long_ema[-1] and self.short_ema[-2] >= self.long_ema[-2] and not self.sellOpen:
            # Sell signal: short EMA crosses below long EMA
            self.Entry_price = self.closes[-1][1]
            self.stop_loss = self.Entry_price + self.diff
            self.id = functions.sell()
            self.sellOpen = True
            print("!!!!SELL!!!!")

        if self.short_ema[-1] > self.long_ema[-1] and self.short_ema[-2] <= self.long_ema[-2] and self.sellOpen:
            functions.close(self.id)
            self.sellOpen = False
            print("!!!!CLOSE!!!!")
        print("closes:", self.closes)
        print(" short:", self.short_ema,
              " long:", self.long_ema)
        print(" open:", self.sellOpen)
