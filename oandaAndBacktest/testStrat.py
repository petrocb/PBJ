import functions

class TestStrat:

    def __init__(self, account):
        self.account = account
        self.count = 0
        self.start = functions.startPastPricesList(1, "EUR_USD", "M5", self.account)
        print(self.start)
    def tick(self):
        print(self.count)
        functions.update()

        if self.count == 0:
            functions.order(500, self.account, self.account, 0,0,0)
        elif self.count == 1:
            functions.order(-1000, self.account, self.account, 0,0,0)
        elif self.count == 2:
            functions.order(500, self.account, self.account, 0,0,0)
        self.count += 1
        self.start = functions.updatePastPrices2(self.start, 1, "EUR_USD", "M5", self.account)
        print(self.start)
