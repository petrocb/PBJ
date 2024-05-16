from .. import functions
class volume:
    def __init__(self, account, sld, tpd, tsld):
        self.account = account
        self.data = functions.startPastPricesList(2, "EUR_USD", "H1", self.account)

    def tick(self):
        if self.account == "test":
            functions.update()
        self.data = functions.updatePastPrices2(self.data, 2, "EUR_USD", "H1", self.account)
        position = functions.getPositions(self.account)['positions']
        # print(self.data)
        if position:
            position = float(position[0]['long']['units']) + float(position[0]['short']['units'])
        else:
            position = 0
        # print("pos", position)
        if position == 0:
            if self.data[0] < self.data[1]:
                r = -1
            elif self.data[0] > self.data[1]:
                r = 1
            # r = randint(-1, 1)
            # print("dir", r)
            # functions.marketOrder(500 * r, self.account, self.account, self.sld, self.tpd, self.tsld)
            # functions.marketOrder(500 * r, self.account, self.account,