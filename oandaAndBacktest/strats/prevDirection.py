from .. import functions
class prevDirection:
    def __init__(self, account, timeFrame):
        self.account = account
        self.timeFrame = timeFrame
        self.data = functions.startPastPricesList(1, "EUR_USD", self.timeFrame, self.account)
        if functions.getPositions(self.account)['positions']:
            self.TradeMade = True
        else:
            self.TradeMade = False

    def tick(self):
        if self.account == "test":
            functions.update()
        self.data = functions.updatePastPrices2(self.data, 1, "EUR_USD", self.timeFrame, self.account)
        position = functions.getPositions(self.account)['positions']
        time = False
        if position:
            position = float(position[0]['long']['units']) + float(position[0]['short']['units'])
        else:
            position = 0
            self.TradeMade = False
        if self.timeFrame == "M30":
            if functions.time(self.account).minute == 00 or functions.time(self.account).minute == 30:
                time = True
        elif self.timeFrame == "H1":
            if functions.time(self.account).minute == 00:
                time = True
        elif self.timeFrame == "H4":
            if functions.time(self.account).hour % 4 == 0 and functions.time(self.account).minute == 00:
                time = True
        elif self.timeFrame == "D":
            if functions.time(self.account).hour == 00:
                time = True

        price = round((float(functions.getAsk(self.account)) + float(functions.getBid(self.account))) / 2, 5)
        if time and position == 0:
            if price < self.data[0][3]:
                functions.marketOrder(-500, self.account, self.account, self.data[0][1], 0, 0)
                self.TradeMade = True

            elif price > self.data[0][3]:
                functions.marketOrder(500, self.account, self.account, self.data[0][2], 0, 0)
                self.TradeMade = True


        elif time and position != 0:
            functions.marketOrder(position * -1, self.account, self.account, 0, 0, 0)
            self.TradeMade = False

        print("\ntime:", functions.time("primary"),
              "\ntimeFrame:", self.timeFrame,
              "\ntradeMade:", self.TradeMade,
              "\nposition:", position,
              "\nprice:", price)
